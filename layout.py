#!/usr/bin/env python3
"""
layout.py — Passive component auto-placement for KiCad PCB files.

Reads a .kicad_pcb file where large components (ICs, connectors, headers)
have been manually placed. Places unplaced passive components (resistors,
capacitors, ferrite beads, LEDs, diodes, test points) on a 1.5mm grid
near their connected anchor components, avoiding overlaps.

Usage:
    python layout.py boards/digital/layout/layout.kicad_pcb
    python layout.py boards/analog/layout/layout.kicad_pcb
"""

import os
import re
import sys
import math
import uuid as _uuid
from dataclasses import dataclass, field
from typing import Optional


# =============================================================================
# Config
# =============================================================================

GRID_MM = 1.5  # placement grid
MAX_SEARCH_RADIUS_MM = 30.0  # max distance from anchor to search
IC_ESCAPE_DEPTH_MM = 3.0  # how far escape zones extend outward from IC pads
IC_ESCAPE_WIDTH_MM = 1.0  # half-width of each pad escape corridor
THT_CLEARANCE_MM = 3.0  # extra clearance around through-hole connectors (mating, soldering)
SMD_CLEARANCE_MM = 1.2  # default clearance between SMD components

# Layer constants
FRONT_LAYER = "F.Cu"
BACK_LAYER = "B.Cu"

# 6-layer stackup: layer name → type
# L1 F.Cu    = mixed  (top, components + routing)
# L2 In1.Cu  = power  (GND plane)
# L3 In2.Cu  = signal (internal routing)
# L4 In3.Cu  = power  (power plane: 3V3_DIG, VBAT, 3V3_ANA)
# L5 In4.Cu  = power  (GND plane)
# L6 B.Cu    = mixed  (bottom, components + routing)
LAYER_STACKUP = {
    "F.Cu":   "mixed",
    "In1.Cu": "power",
    "In2.Cu": "signal",
    "In3.Cu": "power",
    "In4.Cu": "power",
    "B.Cu":   "mixed",
}

# Layer flip mapping — all front/back layer pairs in KiCad
LAYER_FLIP_MAP = {
    "F.Cu": "B.Cu", "B.Cu": "F.Cu",
    "F.SilkS": "B.SilkS", "B.SilkS": "F.SilkS",
    "F.Fab": "B.Fab", "B.Fab": "F.Fab",
    "F.CrtYd": "B.CrtYd", "B.CrtYd": "F.CrtYd",
    "F.Paste": "B.Paste", "B.Paste": "F.Paste",
    "F.Mask": "B.Mask", "B.Mask": "F.Mask",
    "F.Adhes": "B.Adhes", "B.Adhes": "F.Adhes",
}

# Footprint patterns for passive components (auto-placed)
PASSIVE_PATTERNS = [
    r"R_\d{4}",       # resistors (R_0402, R_0603, etc.)
    r"C_\d{4}",       # capacitors
    r"LED_\d{4}",     # LEDs
    r"D_SOD",         # diodes
    r"TestPoint",     # test points
]

# Courtyard margins (half-size in mm) by footprint type
# These are approximate — real courtyard comes from footprint
FOOTPRINT_SIZES = {
    "0201": (0.6, 0.35),
    "0402": (0.8, 0.5),
    "0603": (1.2, 0.7),
    "0805": (1.5, 0.9),
    "1206": (2.0, 1.0),
    "1210": (2.1, 1.3),
    "Pad_1.0x1.0mm": (0.7, 0.7),
    "SOD-323": (1.4, 0.8),
    "SOD-123": (1.8, 1.0),
}

DEFAULT_PASSIVE_SIZE = (1.0, 0.6)


# =============================================================================
# Data structures
# =============================================================================

@dataclass
class Pad:
    number: str
    net_name: str
    x_offset: float  # relative to component center
    y_offset: float


@dataclass
class Component:
    ref: str
    footprint: str
    x: float
    y: float
    angle: float
    uuid: str
    is_passive: bool
    is_placed: bool  # True if manually placed (not at auto-gen position)
    layer: str = FRONT_LAYER  # "F.Cu" or "B.Cu"
    pads: list = field(default_factory=list)
    width: float = 0.0   # courtyard half-width
    height: float = 0.0  # courtyard half-height
    cx_off: float = 0.0  # bounding box center offset from component origin (local coords)
    cy_off: float = 0.0
    is_through_hole: bool = False  # THT components block both sides
    path_name: str = ""  # .zen component name from Path property (e.g. "C_U6_AVDD")
    start_offset: int = 0   # byte offset in file
    end_offset: int = 0     # byte offset in file

    def bbox_center(self) -> tuple:
        """Global position of the bounding box center, accounting for rotation."""
        dx, dy = rotate_pad_offset(self.cx_off, self.cy_off, self.angle)
        return self.x + dx, self.y + dy


@dataclass
class PlacementResult:
    ref: str
    x: float
    y: float
    angle: float
    layer: str
    anchor_ref: str
    anchor_pad: str


@dataclass
class EscapeZone:
    """Keep-out rectangle extending outward from an IC pad to preserve escape routing."""
    cx: float   # center x (global coords)
    cy: float   # center y (global coords)
    half_w: float
    half_h: float
    layer: str


# =============================================================================
# KiCad PCB Parser
# =============================================================================

def is_passive_footprint(fp_name: str) -> bool:
    """Check if a footprint is a passive component."""
    for pattern in PASSIVE_PATTERNS:
        if re.search(pattern, fp_name):
            return True
    return False


def get_footprint_size(fp_name: str) -> tuple:
    """Get approximate half-dimensions (w, h) in mm for a footprint.
    Used as fallback when courtyard data is not available."""
    for key, size in FOOTPRINT_SIZES.items():
        if key in fp_name:
            return size
    return DEFAULT_PASSIVE_SIZE


def parse_courtyard_size(block: str) -> Optional[tuple]:
    """Parse courtyard bounding box from fp_line elements on CrtYd layers.

    Returns (half_width, half_height, cx_offset, cy_offset) or None if no courtyard data found.
    cx_offset, cy_offset is the center of the bounding box relative to the component origin.
    """
    # Collect all coordinates from fp_line elements on courtyard layers
    coords = []
    for m in re.finditer(r'\(fp_line\b', block):
        line_start = m.start()
        line_end = find_matching_paren(block, line_start)
        line_block = block[line_start:line_end + 1]
        if 'CrtYd' not in line_block:
            continue
        # Extract start and end coordinates
        start_m = re.search(r'\(start\s+([\d.-]+)\s+([\d.-]+)\)', line_block)
        end_m = re.search(r'\(end\s+([\d.-]+)\s+([\d.-]+)\)', line_block)
        if start_m:
            coords.append((float(start_m.group(1)), float(start_m.group(2))))
        if end_m:
            coords.append((float(end_m.group(1)), float(end_m.group(2))))

    # Also check fp_rect on courtyard layers
    for m in re.finditer(r'\(fp_rect\b', block):
        rect_start = m.start()
        rect_end = find_matching_paren(block, rect_start)
        rect_block = block[rect_start:rect_end + 1]
        if 'CrtYd' not in rect_block:
            continue
        start_m = re.search(r'\(start\s+([\d.-]+)\s+([\d.-]+)\)', rect_block)
        end_m = re.search(r'\(end\s+([\d.-]+)\s+([\d.-]+)\)', rect_block)
        if start_m:
            coords.append((float(start_m.group(1)), float(start_m.group(2))))
        if end_m:
            coords.append((float(end_m.group(1)), float(end_m.group(2))))

    if not coords:
        return None

    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    cx_off = (min(xs) + max(xs)) / 2
    cy_off = (min(ys) + max(ys)) / 2
    half_w = (max(xs) - min(xs)) / 2
    half_h = (max(ys) - min(ys)) / 2
    return (half_w, half_h, cx_off, cy_off)


def _size_from_pads_or_fallback(block: str, fp_name: str) -> tuple:
    """Estimate component half-size from pad extents, with margin.
    Falls back to a conservative default if no pads found.

    Returns (half_width, half_height, cx_offset, cy_offset).
    """
    pad_xs = []
    pad_ys = []
    for pm in re.finditer(r'\(pad\s+"?\w+"?\s+\w+\s+\w+(?:\s+locked)?\s*\(at\s+([\d.-]+)\s+([\d.-]+)', block):
        pad_xs.append(float(pm.group(1)))
        pad_ys.append(float(pm.group(2)))
    if pad_xs and pad_ys:
        cx_off = (min(pad_xs) + max(pad_xs)) / 2
        cy_off = (min(pad_ys) + max(pad_ys)) / 2
        half_w = (max(pad_xs) - min(pad_xs)) / 2 + 0.75
        half_h = (max(pad_ys) - min(pad_ys)) / 2 + 0.75
        return (half_w, half_h, cx_off, cy_off)

    # No pads found — conservative fallback
    return (3.0, 3.0, 0.0, 0.0)


def parse_sexp_value(text: str, key: str) -> Optional[str]:
    """Extract a simple value from s-expression: (key "value") or (key value)."""
    pattern = rf'\({key}\s+"([^"]*)"'
    m = re.search(pattern, text)
    if m:
        return m.group(1)
    pattern = rf'\({key}\s+([^\s\)]+)'
    m = re.search(pattern, text)
    if m:
        return m.group(1)
    return None


def find_matching_paren(text: str, start: int) -> int:
    """Find the matching closing paren for the opening paren at start."""
    depth = 0
    i = start
    in_string = False
    while i < len(text):
        c = text[i]
        if c == '"' and (i == 0 or text[i-1] != '\\'):
            in_string = not in_string
        elif not in_string:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return len(text) - 1


def parse_components(pcb_text: str) -> list:
    """Parse all footprint components from KiCad PCB text."""
    components = []
    # Find all top-level (footprint ...) blocks
    fp_pattern = re.compile(r'\n\t\(footprint ')
    for m in fp_pattern.finditer(pcb_text):
        start = m.start() + 1  # skip the leading newline
        end = find_matching_paren(pcb_text, start)
        block = pcb_text[start:end + 1]

        fp_name = parse_sexp_value(block, "footprint")
        uuid = parse_sexp_value(block, "uuid")

        # Parse layer: (layer "F.Cu") or (layer "B.Cu")
        layer = parse_sexp_value(block, "layer") or FRONT_LAYER

        # Parse position: (at x y) or (at x y angle)
        at_match = re.search(r'\(at\s+([\d.-]+)\s+([\d.-]+)(?:\s+([\d.-]+))?\)', block)
        x, y, angle = 0.0, 0.0, 0.0
        if at_match:
            x = float(at_match.group(1))
            y = float(at_match.group(2))
            if at_match.group(3):
                angle = float(at_match.group(3))

        # Parse reference designator
        ref = ""
        ref_match = re.search(r'\(property\s+"Reference"\s+"([^"]*)"', block)
        if ref_match:
            ref = ref_match.group(1)

        # Determine if passive
        passive = is_passive_footprint(fp_name) if fp_name else False

        # Determine component size: try courtyard first, then pad extents, then fallback
        cx_off, cy_off = 0.0, 0.0
        courtyard = parse_courtyard_size(block)
        if courtyard:
            w, h, cx_off, cy_off = courtyard
        elif passive:
            w, h = get_footprint_size(fp_name) if fp_name else DEFAULT_PASSIVE_SIZE
        else:
            # No courtyard data — estimate from pad extents + margin
            w, h, cx_off, cy_off = _size_from_pads_or_fallback(block, fp_name)

        # Parse pads and their nets
        pads = []
        pad_iter = re.finditer(r'\(pad\s+"?(\w+)"?\s+\w+\s+\w+(?:\s+locked)?\s*\(at\s+([\d.-]+)\s+([\d.-]+)', block)
        for pm in pad_iter:
            pad_num = pm.group(1)
            px = float(pm.group(2))
            py = float(pm.group(3))
            # Find net for this pad
            pad_start = pm.start()
            pad_end = find_matching_paren(block, pad_start)
            pad_block = block[pad_start:pad_end + 1]
            net_match = re.search(r'\(net\s+\d+\s+"([^"]*)"', pad_block)
            net_name = net_match.group(1) if net_match else ""
            pads.append(Pad(number=pad_num, net_name=net_name, x_offset=px, y_offset=py))

        # Detect through-hole components (pins go through both sides)
        through_hole = bool(re.search(r'\(attr\s+through_hole\)', block))

        # Parse .zen component name from Path property (e.g. "C_U6_AVDD.C" → "C_U6_AVDD")
        path_name = ""
        path_match = re.search(r'\(property\s+"Path"\s+"([^"]*)"', block)
        if path_match:
            path_name = path_match.group(1).split('.')[0]

        # A component is "placed" if it has a non-zero position
        # (pcb layout tool places all components, but at auto-generated positions)
        is_placed = True  # all components start as "placed" by pcb layout

        comp = Component(
            ref=ref,
            footprint=fp_name or "",
            x=x, y=y, angle=angle,
            uuid=uuid or "",
            is_passive=passive,
            is_placed=is_placed,
            layer=layer,
            is_through_hole=through_hole,
            path_name=path_name,
            pads=pads,
            width=w, height=h,
            cx_off=cx_off, cy_off=cy_off,
            start_offset=start,
            end_offset=end + 1,
        )
        components.append(comp)

    return components


# =============================================================================
# Placement Engine
# =============================================================================

def rotate_pad_offset(pad_x: float, pad_y: float, comp_angle: float) -> tuple:
    """Rotate pad offset from component-local to global coordinates."""
    if comp_angle == 0:
        return pad_x, pad_y
    angle_rad = math.radians(comp_angle)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    return (pad_x * cos_a - pad_y * sin_a,
            pad_x * sin_a + pad_y * cos_a)


def pad_global_pos(comp: 'Component', pad: 'Pad') -> tuple:
    """Get the global position of a pad on a component."""
    dx, dy = rotate_pad_offset(pad.x_offset, pad.y_offset, comp.angle)
    return comp.x + dx, comp.y + dy


def boxes_overlap(ax, ay, aw, ah, bx, by, bw, bh, margin=1.2) -> bool:
    """Check if two axis-aligned boxes overlap (with margin)."""
    return (abs(ax - bx) < (aw + bw + margin) and
            abs(ay - by) < (ah + bh + margin))


def _path_match_score(passive_path: str, comp: 'Component') -> int:
    """Score how well a passive's .zen path name matches a candidate anchor.

    Higher score = better match. Returns 0 for no match.
    Uses the Path property naming convention: C_U6_AVDD → should anchor to U6.
    """
    if not passive_path or not comp.path_name:
        return 0
    # Check if the component's path prefix or ref appears in the passive's path name
    # e.g. passive "C_U6_AVDD" contains "U6" (comp.ref) or "U6" (comp.path_name)
    score = 0
    if comp.ref in passive_path:
        score = max(score, len(comp.ref))
    if comp.path_name in passive_path:
        score = max(score, len(comp.path_name))
    # Check path segments: "C_U6_AVDD" split → ["C","U6","AVDD"]
    # Match if any segment equals the comp ref or path prefix
    for seg in passive_path.split('_'):
        if seg and (seg == comp.ref or seg == comp.path_name):
            score = max(score, len(seg) + 10)  # exact segment match bonus
    return score


def find_anchor(passive: Component, components: list, net_components: dict) -> tuple:
    """Find the best anchor component for a passive.

    Returns (anchor_component, anchor_pad_number, passive_pad_number)
    where passive_pad_number is the pad that should be closest to the anchor.

    Uses path-name matching to assign decoupling caps to their target ICs,
    and deprioritizes connectors (J-prefix) to avoid clustering around headers.
    """
    # Collect all non-passive candidates from non-GND nets
    candidates = []
    for pad in passive.pads:
        if not pad.net_name or pad.net_name in ("GND", ""):
            continue
        connected = net_components.get(pad.net_name, [])
        for comp, comp_pad in connected:
            if comp.ref == passive.ref or comp.is_passive:
                continue
            candidates.append((comp, comp_pad, pad.number))

    if candidates:
        # Score each candidate
        def anchor_score(entry):
            comp, comp_pad, ppad = entry
            # Path-name match (highest priority)
            path_score = _path_match_score(passive.path_name, comp)
            # Connector penalty: deprioritize J-prefix refs
            is_connector = 1 if comp.ref.startswith('J') else 0
            # Sort key: higher path_score is better, non-connector is better
            return (-path_score, is_connector)

        candidates.sort(key=anchor_score)
        best = candidates[0]
        return best

    # If no non-passive anchor found on non-GND nets, try any non-passive on any net
    for pad in passive.pads:
        if not pad.net_name:
            continue
        connected = net_components.get(pad.net_name, [])
        for comp, comp_pad in connected:
            if comp.ref == passive.ref:
                continue
            if not comp.is_passive:
                return (comp, comp_pad, pad.number)

    # Fallback: any connected component
    for pad in passive.pads:
        if not pad.net_name:
            continue
        connected = net_components.get(pad.net_name, [])
        for comp, comp_pad in connected:
            if comp.ref != passive.ref:
                return (comp, comp_pad, pad.number)

    return (None, None, None)


def find_between_anchors(passive: Component, components: list, net_components: dict) -> tuple:
    """For series components (both pads connected to non-GND non-passive components),
    find two anchor points to place between."""
    anchors = []
    for pad in passive.pads:
        if not pad.net_name or pad.net_name in ("GND", ""):
            continue
        connected = net_components.get(pad.net_name, [])
        for comp, comp_pad in connected:
            if comp.ref != passive.ref and not comp.is_passive:
                anchors.append((comp, comp_pad, pad.number))
                break
    if len(anchors) >= 2:
        return anchors[0], anchors[1]
    return None, None


POWER_NET_KEYWORDS = ("VCC", "VDD", "3V3", "1V8", "VBAT", "AVDD", "DVDD", "VBUS", "PWR", "VSYS")


def is_power_net(net_name: str) -> bool:
    """Check if a net is a power supply net (not a signal needing escape routing)."""
    upper = net_name.upper()
    return any(kw in upper for kw in POWER_NET_KEYWORDS)


def compute_escape_zones(components: list) -> list:
    """Compute escape route zones extending outward from pads on ICs and connectors.

    For each non-passive component, creates rectangular keep-out zones extending
    outward from each pad. This prevents passives from blocking the paths
    where traces need to escape from pins.

    For SMD ICs: GND pads are skipped (connect via planes), power pads are skipped
    (decoupling caps should be placed near power pins, not pushed away).

    For through-hole connectors: ALL pads get escape zones (THT pads need routing
    clearance on all nets, including GND which routes to vias, not planes directly).
    """
    zones = []
    for comp in components:
        if comp.is_passive or not comp.pads:
            continue

        bcx, bcy = comp.bbox_center()

        for pad in comp.pads:
            if not pad.net_name:
                continue
            # For SMD components, skip GND and power pads
            if not comp.is_through_hole:
                if pad.net_name == "GND":
                    continue
                if is_power_net(pad.net_name):
                    continue

            px, py = pad_global_pos(comp, pad)

            # Direction from component center to pad = "outward"
            dx = px - bcx
            dy = py - bcy
            dist = math.sqrt(dx * dx + dy * dy)
            if dist < 0.01:
                continue

            nx, ny = dx / dist, dy / dist

            # Through-hole connectors get deeper escape zones
            depth = THT_CLEARANCE_MM if comp.is_through_hole else IC_ESCAPE_DEPTH_MM

            # Zone center is offset outward from pad
            zone_cx = px + nx * depth / 2
            zone_cy = py + ny * depth / 2

            # Orient the rectangle: long axis along escape direction
            if abs(nx) > abs(ny):
                zone_hw = depth / 2
                zone_hh = IC_ESCAPE_WIDTH_MM
            else:
                zone_hw = IC_ESCAPE_WIDTH_MM
                zone_hh = depth / 2

            zones.append(EscapeZone(
                cx=zone_cx, cy=zone_cy,
                half_w=zone_hw, half_h=zone_hh,
                layer=comp.layer,
            ))

    return zones


def snap_to_grid(val: float, grid: float) -> float:
    """Snap a value to the nearest grid point."""
    return round(val / grid) * grid


def place_passive(passive: Component, anchor: Component, anchor_pad: Pad,
                  passive_pad_num: str, placed: list, grid: float,
                  between_pos: tuple = None,
                  board_bounds: tuple = None,
                  target_layer: str = FRONT_LAYER,
                  escape_zones: list = None) -> Optional[PlacementResult]:
    """Try to place a passive near its anchor on the grid, avoiding overlaps.

    board_bounds: (min_x, min_y, max_x, max_y) — reject positions outside.
    target_layer: which PCB side to place on ("F.Cu" or "B.Cu").
                  Only checks overlaps against components on the same layer.
    """

    if between_pos:
        # Place between two anchors
        target_x, target_y = between_pos
    else:
        # Target position: near the anchor's pad (in global coordinates)
        target_x, target_y = pad_global_pos(anchor, anchor_pad)

    # Filter placed components: same layer OR through-hole (blocks both sides)
    same_layer_placed = [p for p in placed if p.layer == target_layer or p.is_through_hole]

    # Determine optimal orientation
    # Try to orient the passive so the anchor pad faces the target
    best_result = None
    best_dist = float('inf')

    for angle in [0, 90]:
        # Swap width/height for 90-degree rotation
        pw = passive.width if angle == 0 else passive.height
        ph = passive.height if angle == 0 else passive.width

        # Search in expanding radius (start at 0 to try exact target first)
        for radius_steps in range(0, int(MAX_SEARCH_RADIUS_MM / grid) + 1):
            for dx in range(-radius_steps, radius_steps + 1):
                for dy in range(-radius_steps, radius_steps + 1):
                    # Only check perimeter of current radius (or center for r=0)
                    if radius_steps > 0 and abs(dx) != radius_steps and abs(dy) != radius_steps:
                        continue

                    cx = snap_to_grid(target_x + dx * grid, grid)
                    cy = snap_to_grid(target_y + dy * grid, grid)

                    # Check board boundary (component must fit inside)
                    if board_bounds:
                        bmin_x, bmin_y, bmax_x, bmax_y = board_bounds
                        if (cx - pw < bmin_x or cx + pw > bmax_x or
                                cy - ph < bmin_y or cy + ph > bmax_y):
                            continue

                    # Check overlap with placed components on the same layer
                    overlap = False
                    for p in same_layer_placed:
                        p_w = p.width if p.angle in (0, 180) else p.height
                        p_h = p.height if p.angle in (0, 180) else p.width
                        bcx, bcy = p.bbox_center()
                        # Through-hole components (connectors, headers) need extra
                        # clearance for mating connectors and soldering access
                        margin = THT_CLEARANCE_MM if p.is_through_hole else SMD_CLEARANCE_MM
                        if boxes_overlap(cx, cy, pw, ph, bcx, bcy, p_w, p_h, margin=margin):
                            overlap = True
                            break

                    # Check IC pad escape zones on the same layer
                    if not overlap and escape_zones:
                        for ez in escape_zones:
                            if ez.layer != target_layer:
                                continue
                            if boxes_overlap(cx, cy, pw, ph,
                                             ez.cx, ez.cy, ez.half_w, ez.half_h,
                                             margin=0.0):
                                overlap = True
                                break

                    if not overlap:
                        dist = math.sqrt((cx - target_x)**2 + (cy - target_y)**2)
                        if dist < best_dist:
                            best_dist = dist
                            best_result = PlacementResult(
                                ref=passive.ref,
                                x=cx, y=cy,
                                angle=float(angle),
                                layer=target_layer,
                                anchor_ref=anchor.ref,
                                anchor_pad=anchor_pad.number,
                            )

            # If we found a placement in this radius, use it
            if best_result is not None:
                return best_result

    return best_result


def parse_initial_positions(initial_path: str) -> dict:
    """Read manually-placed positions from _initial.kicad_pcb.

    Returns dict of ref → (x, y, angle, layer) for non-passive components.
    """
    with open(initial_path, 'r') as f:
        text = f.read()

    positions = {}
    components = parse_components(text)
    for comp in components:
        if comp.ref:
            positions[comp.ref] = (comp.x, comp.y, comp.angle, comp.layer)
    return positions


def parse_board_bounds(pcb_text: str) -> Optional[tuple]:
    """Parse board outline rectangle from Edge.Cuts layer.

    Returns (min_x, min_y, max_x, max_y) or None if not found.
    """
    for m in re.finditer(r'\(gr_rect\b', pcb_text):
        start = m.start()
        end = find_matching_paren(pcb_text, start)
        block = pcb_text[start:end + 1]
        if 'Edge.Cuts' not in block:
            continue
        start_m = re.search(r'\(start\s+([\d.-]+)\s+([\d.-]+)\)', block)
        end_m = re.search(r'\(end\s+([\d.-]+)\s+([\d.-]+)\)', block)
        if start_m and end_m:
            x1, y1 = float(start_m.group(1)), float(start_m.group(2))
            x2, y2 = float(end_m.group(1)), float(end_m.group(2))
            return (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
    return None


def parse_board_outline(pcb_text: str) -> Optional[str]:
    """Extract the gr_rect on Edge.Cuts layer from PCB text, if present."""
    # Find gr_rect blocks and check if they're on Edge.Cuts
    for m in re.finditer(r'\(gr_rect\b', pcb_text):
        start = m.start()
        end = find_matching_paren(pcb_text, start)
        block = pcb_text[start:end + 1]
        if 'Edge.Cuts' in block:
            return block
    return None


def flip_footprint_layers(block: str) -> str:
    """Swap all front/back layer references in a footprint block.

    Flips F.Cu↔B.Cu, F.SilkS↔B.SilkS, F.Fab↔B.Fab, etc.
    Uses a placeholder to avoid double-swapping.
    """
    # Replace via placeholder to avoid F→B→F round-trip
    placeholder_map = {}
    for i, (src, dst) in enumerate(LAYER_FLIP_MAP.items()):
        placeholder = f"__LAYER_PLACEHOLDER_{i}__"
        placeholder_map[placeholder] = dst
        block = block.replace(f'"{src}"', f'"{placeholder}"')
    for placeholder, dst in placeholder_map.items():
        block = block.replace(f'"{placeholder}"', f'"{dst}"')
    return block


# Zone configuration: which layers get GND copper pours
# Digital board: DGND everywhere (F.Cu, In1.Cu=GND plane, In4.Cu=GND plane, B.Cu)
# Analog board: same GND net, but user may split DGND/AGND pours manually later
GROUND_ZONE_LAYERS = ["F.Cu", "In1.Cu", "In4.Cu", "B.Cu"]


def generate_zone_sexp(net_num: int, net_name: str, layer: str,
                       bounds: tuple, zone_uuid: str) -> str:
    """Generate a KiCad zone (copper pour) s-expression.

    bounds: (min_x, min_y, max_x, max_y) from board outline.
    """
    x1, y1, x2, y2 = bounds
    return (
        f'\t(zone\n'
        f'\t\t(net {net_num})\n'
        f'\t\t(net_name "{net_name}")\n'
        f'\t\t(layer "{layer}")\n'
        f'\t\t(uuid "{zone_uuid}")\n'
        f'\t\t(hatch edge 0.5)\n'
        f'\t\t(connect_pads\n'
        f'\t\t\t(clearance 0.3)\n'
        f'\t\t)\n'
        f'\t\t(min_thickness 0.2)\n'
        f'\t\t(fill yes\n'
        f'\t\t\t(thermal_gap 0.3)\n'
        f'\t\t\t(thermal_bridge_width 0.3)\n'
        f'\t\t)\n'
        f'\t\t(polygon\n'
        f'\t\t\t(pts\n'
        f'\t\t\t\t(xy {x1} {y1})\n'
        f'\t\t\t\t(xy {x2} {y1})\n'
        f'\t\t\t\t(xy {x2} {y2})\n'
        f'\t\t\t\t(xy {x1} {y2})\n'
        f'\t\t\t)\n'
        f'\t\t)\n'
        f'\t)\n'
    )


def add_ground_zones(pcb_text: str, bounds: tuple) -> str:
    """Add GND copper pour zones to the PCB on all ground layers.

    Skips layers that already have a GND zone defined.
    """
    # Find GND net number
    gnd_match = re.search(r'\(net\s+(\d+)\s+"GND"\)', pcb_text)
    if not gnd_match:
        print("  Warning: GND net not found, skipping zone generation")
        return pcb_text

    gnd_net = int(gnd_match.group(1))

    # Check which layers already have zones
    existing_zone_layers = set()
    for m in re.finditer(r'\(zone\b', pcb_text):
        start = m.start()
        end = find_matching_paren(pcb_text, start)
        block = pcb_text[start:end + 1]
        layer_m = re.search(r'\(layer\s+"([^"]+)"\)', block)
        if layer_m:
            existing_zone_layers.add(layer_m.group(1))

    zones_added = []
    zone_text = ""
    for layer in GROUND_ZONE_LAYERS:
        if layer in existing_zone_layers:
            continue
        zone_uuid = str(_uuid.uuid4())
        zone_text += generate_zone_sexp(gnd_net, "GND", layer, bounds, zone_uuid)
        zones_added.append(layer)

    if zone_text:
        # Insert before the final closing paren
        insert_pos = pcb_text.rfind(')')
        pcb_text = pcb_text[:insert_pos] + zone_text + pcb_text[insert_pos:]
        print(f"  Added GND zones on: {', '.join(zones_added)}")
    else:
        print("  GND zones already present on all layers")

    return pcb_text


def fix_layer_types(pcb_text: str) -> str:
    """Correct copper layer types to match the intended 6-layer stackup."""
    for layer_name, layer_type in LAYER_STACKUP.items():
        # Match: (id "LayerName" currenttype) — with or without alias
        pattern = re.compile(
            rf'(\(\d+\s+"{re.escape(layer_name)}"\s+)\w+(.*?\))'
        )
        pcb_text = pattern.sub(rf'\g<1>{layer_type}\2', pcb_text)
    return pcb_text


def run_placement(pcb_path: str):
    """Main placement routine.

    Reads the full layout.kicad_pcb (all components).
    Reads layout_initial.kicad_pcb for manually-placed IC positions.
    Applies IC positions, then auto-places passives.
    """
    # Determine initial file path
    initial_path = pcb_path.replace('.kicad_pcb', '_initial.kicad_pcb')
    if not os.path.exists(initial_path):
        print(f"Error: {initial_path} not found.")
        print(f"Run make_initial.py first, place components in KiCad, then re-run this.")
        sys.exit(1)

    print(f"Reading full PCB: {pcb_path}")
    with open(pcb_path, 'r') as f:
        pcb_text = f.read()

    components = parse_components(pcb_text)
    print(f"Found {len(components)} components")

    # Read manually-placed positions from initial file
    print(f"Reading manual placements: {initial_path}")
    manual_positions = parse_initial_positions(initial_path)
    print(f"  {len(manual_positions)} positions read")

    # Apply manual positions (including layer) to non-passive components
    for comp in components:
        if not comp.is_passive and comp.ref in manual_positions:
            comp.x, comp.y, comp.angle, comp.layer = manual_positions[comp.ref]

    # Classify
    passives = [c for c in components if c.is_passive]
    non_passives = [c for c in components if not c.is_passive]
    print(f"  {len(non_passives)} non-passive (from manual placement)")
    print(f"  {len(passives)} passive (to auto-place)")

    # Parse board outline for boundary checking
    board_bounds = parse_board_bounds(pcb_text)
    if board_bounds:
        print(f"  Board bounds: ({board_bounds[0]}, {board_bounds[1]}) → ({board_bounds[2]}, {board_bounds[3]})")
    else:
        print("  Warning: no board outline found, skipping boundary checks")

    # Build net → component+pad mapping
    net_components = {}
    for comp in components:
        for pad in comp.pads:
            if pad.net_name:
                if pad.net_name not in net_components:
                    net_components[pad.net_name] = []
                net_components[pad.net_name].append((comp, pad))

    # Compute IC pad escape zones to keep routing paths clear
    escape_zones = compute_escape_zones(components)
    print(f"  {len(escape_zones)} IC pad escape zones computed")

    # Start with non-passives as placed
    placed = list(non_passives)
    results = []
    failed = []

    for passive in passives:
        # Check if this is a "between" component (series R, coupling C)
        anchor1, anchor2 = find_between_anchors(passive, components, net_components)

        result = None
        if anchor1 and anchor2:
            comp1, pad1, ppad1 = anchor1
            comp2, pad2, ppad2 = anchor2
            # Place at midpoint between the two anchors (using rotated pad positions)
            p1x, p1y = pad_global_pos(comp1, pad1)
            p2x, p2y = pad_global_pos(comp2, pad2)
            mid_x = (p1x + p2x) / 2
            mid_y = (p1y + p2y) / 2
            # Try anchor's layer first, then the other side
            primary_layer = comp1.layer
            alt_layer = BACK_LAYER if primary_layer == FRONT_LAYER else FRONT_LAYER
            result = place_passive(passive, comp1, pad1, ppad1, placed, GRID_MM,
                                   between_pos=(mid_x, mid_y),
                                   board_bounds=board_bounds,
                                   target_layer=primary_layer,
                                   escape_zones=escape_zones)
            if result is None:
                result = place_passive(passive, comp1, pad1, ppad1, placed, GRID_MM,
                                       between_pos=(mid_x, mid_y),
                                       board_bounds=board_bounds,
                                       target_layer=alt_layer,
                                       escape_zones=escape_zones)
        else:
            # Find single anchor
            anchor, anchor_pad, passive_pad = find_anchor(passive, components, net_components)
            if anchor is None:
                failed.append(passive.ref)
                continue
            # Try anchor's layer first, then the other side
            primary_layer = anchor.layer
            alt_layer = BACK_LAYER if primary_layer == FRONT_LAYER else FRONT_LAYER
            result = place_passive(passive, anchor, anchor_pad, passive_pad, placed, GRID_MM,
                                   board_bounds=board_bounds,
                                   target_layer=primary_layer,
                                   escape_zones=escape_zones)
            if result is None:
                result = place_passive(passive, anchor, anchor_pad, passive_pad, placed, GRID_MM,
                                       board_bounds=board_bounds,
                                       target_layer=alt_layer,
                                       escape_zones=escape_zones)

        if result:
            # Update passive position and layer
            passive.x = result.x
            passive.y = result.y
            passive.angle = result.angle
            passive.layer = result.layer
            placed.append(passive)
            results.append(result)
        else:
            failed.append(passive.ref)

    # Report placement stats
    front_count = sum(1 for r in results if r.layer == FRONT_LAYER)
    back_count = sum(1 for r in results if r.layer == BACK_LAYER)
    print(f"\nPlaced {len(results)} passives ({front_count} front, {back_count} back), {len(failed)} failed")

    if failed:
        print(f"Failed to place: {', '.join(failed)}")

    # Collect all components that need position updates: (comp, x, y, angle, layer)
    all_updates = []

    # Non-passives: apply positions + layer from _initial file
    for comp in non_passives:
        if comp.ref in manual_positions:
            mx, my, ma, ml = manual_positions[comp.ref]
            all_updates.append((comp, mx, my, ma, ml))

    # Passives: apply auto-placed positions + layer
    for comp in passives:
        if comp.ref in [r.ref for r in results]:
            result = next(r for r in results if r.ref == comp.ref)
            all_updates.append((comp, result.x, result.y, result.angle, result.layer))

    # Sort by file offset (descending) so we can replace without shifting issues
    all_updates.sort(key=lambda u: u[0].start_offset, reverse=True)

    for comp, new_x, new_y, new_angle, new_layer in all_updates:
        block = pcb_text[comp.start_offset:comp.end_offset]

        # Update position
        at_pattern = re.compile(r'\(at\s+[\d.-]+\s+[\d.-]+(?:\s+[\d.-]+)?\)')
        if new_angle != 0:
            new_at = f'(at {new_x:.4f} {new_y:.4f} {new_angle:.0f})'
        else:
            new_at = f'(at {new_x:.4f} {new_y:.4f})'

        new_block = at_pattern.sub(new_at, block, count=1)

        # Flip layers if the component is moving to a different side
        orig_layer = parse_sexp_value(block, "layer") or FRONT_LAYER
        if new_layer != orig_layer:
            new_block = flip_footprint_layers(new_block)

        pcb_text = pcb_text[:comp.start_offset] + new_block + pcb_text[comp.end_offset:]

    # Copy board outline from _initial file, or keep existing one
    has_outline = False
    for m in re.finditer(r'\(gr_rect\b', pcb_text):
        start = m.start()
        end = find_matching_paren(pcb_text, start)
        block = pcb_text[start:end + 1]
        if 'Edge.Cuts' in block:
            has_outline = True
            break

    if not has_outline:
        with open(initial_path, 'r') as f:
            initial_text = f.read()
        initial_outline = parse_board_outline(initial_text)
        if initial_outline:
            insert_pos = pcb_text.rfind(')')
            pcb_text = pcb_text[:insert_pos] + '\n\t' + initial_outline + '\n' + pcb_text[insert_pos:]
            print(f"  Copied board outline from {initial_path}")

    # Fix layer types to match intended stackup
    pcb_text = fix_layer_types(pcb_text)

    # Add GND copper pour zones on ground layers
    if board_bounds:
        pcb_text = add_ground_zones(pcb_text, board_bounds)

    # Write output
    out_path = pcb_path
    with open(out_path, 'w') as f:
        f.write(pcb_text)

    print(f"Written to {out_path}")
    print("\nPlacement summary:")
    for r in results:
        side = "F" if r.layer == FRONT_LAYER else "B"
        print(f"  {r.ref:12s} → ({r.x:7.2f}, {r.y:7.2f}) @ {r.angle:3.0f}° [{side}]  "
              f"anchor: {r.anchor_ref}.{r.anchor_pad}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python layout.py <path-to-kicad_pcb>")
        sys.exit(1)
    run_placement(sys.argv[1])
