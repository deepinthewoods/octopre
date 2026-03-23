#!/usr/bin/env python3
"""
layout.py — Passive component auto-placement for KiCad PCB files.

Reads a .kicad_pcb file where large components (ICs, connectors, headers)
have been manually placed. Places unplaced passive components (resistors,
capacitors, ferrite beads, LEDs, diodes, test points) on a 1mm grid
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

GRID_MM = 1.0  # placement grid
BOARD_WIDTH = 70.0  # mm
BOARD_HEIGHT = 55.0  # mm
MAX_SEARCH_RADIUS_MM = 30.0  # max distance from anchor to search

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
    pads: list = field(default_factory=list)
    width: float = 0.0   # courtyard half-width
    height: float = 0.0  # courtyard half-height
    start_offset: int = 0   # byte offset in file
    end_offset: int = 0     # byte offset in file


@dataclass
class PlacementResult:
    ref: str
    x: float
    y: float
    angle: float
    anchor_ref: str
    anchor_pad: str


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
    """Get approximate half-dimensions (w, h) in mm for a footprint."""
    for key, size in FOOTPRINT_SIZES.items():
        if key in fp_name:
            return size
    return DEFAULT_PASSIVE_SIZE


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
        w, h = get_footprint_size(fp_name) if fp_name else DEFAULT_PASSIVE_SIZE

        # If not passive, estimate size from footprint (larger components)
        if not passive and fp_name:
            # For non-passive, use a larger default
            if "ESP32" in fp_name:
                w, h = 13.0, 10.0
            elif "ES8388" in fp_name:
                w, h = 3.0, 3.0
            elif "BQ25798" in fp_name:
                w, h = 3.0, 3.0
            elif "TPS62130" in fp_name:
                w, h = 2.5, 2.5
            elif "LP5907" in fp_name:
                w, h = 1.5, 1.5
            elif "74HC4052" in fp_name:
                w, h = 5.5, 4.0
            elif "USB4105" in fp_name:
                w, h = 5.0, 4.5
            elif "USBLC6" in fp_name:
                w, h = 1.5, 1.2
            elif "OPA2134" in fp_name:
                w, h = 3.0, 2.5
            elif "PinHeader" in fp_name or "PinSocket" in fp_name:
                # Estimate from pin count
                pin_match = re.search(r'(\d+)x(\d+)', fp_name)
                if pin_match:
                    rows = int(pin_match.group(1))
                    pins = int(pin_match.group(2))
                    w = rows * 2.54 / 2 + 1.0
                    h = pins * 2.54 / 2 + 1.0
                else:
                    w, h = 3.0, 3.0
            else:
                w, h = 2.0, 2.0

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
            pads=pads,
            width=w, height=h,
            start_offset=start,
            end_offset=end + 1,
        )
        components.append(comp)

    return components


# =============================================================================
# Placement Engine
# =============================================================================

def boxes_overlap(ax, ay, aw, ah, bx, by, bw, bh, margin=0.1) -> bool:
    """Check if two axis-aligned boxes overlap (with margin)."""
    return (abs(ax - bx) < (aw + bw + margin) and
            abs(ay - by) < (ah + bh + margin))


def find_anchor(passive: Component, components: list, net_components: dict) -> tuple:
    """Find the best anchor component for a passive.

    Returns (anchor_component, anchor_pad_number, passive_pad_number)
    where passive_pad_number is the pad that should be closest to the anchor.
    """
    best_anchor = None
    best_pad = None
    passive_pad = None

    # For each pad on the passive, find connected non-passive components
    for pad in passive.pads:
        if not pad.net_name or pad.net_name in ("GND", ""):
            continue
        # Find non-passive components on the same net
        connected = net_components.get(pad.net_name, [])
        for comp, comp_pad in connected:
            if comp.ref == passive.ref:
                continue
            if not comp.is_passive:
                # Prefer power-pin connections for decoupling caps
                best_anchor = comp
                best_pad = comp_pad
                passive_pad = pad.number
                return (best_anchor, best_pad, passive_pad)

    # If no non-passive anchor found, try any non-passive on any net
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


def snap_to_grid(val: float, grid: float) -> float:
    """Snap a value to the nearest grid point."""
    return round(val / grid) * grid


def place_passive(passive: Component, anchor: Component, anchor_pad: Pad,
                  passive_pad_num: str, placed: list, grid: float,
                  between_pos: tuple = None) -> Optional[PlacementResult]:
    """Try to place a passive near its anchor on the grid, avoiding overlaps."""

    if between_pos:
        # Place between two anchors
        target_x, target_y = between_pos
    else:
        # Target position: near the anchor's pad (in global coordinates)
        target_x = anchor.x + anchor_pad.x_offset
        target_y = anchor.y + anchor_pad.y_offset

    # Determine optimal orientation
    # Try to orient the passive so the anchor pad faces the target
    best_result = None
    best_dist = float('inf')

    for angle in [0, 90]:
        # Swap width/height for 90-degree rotation
        pw = passive.width if angle == 0 else passive.height
        ph = passive.height if angle == 0 else passive.width

        # Search in expanding radius
        for radius_steps in range(1, int(MAX_SEARCH_RADIUS_MM / grid) + 1):
            for dx in range(-radius_steps, radius_steps + 1):
                for dy in range(-radius_steps, radius_steps + 1):
                    # Only check perimeter of current radius
                    if abs(dx) != radius_steps and abs(dy) != radius_steps:
                        continue

                    cx = snap_to_grid(target_x + dx * grid, grid)
                    cy = snap_to_grid(target_y + dy * grid, grid)

                    # Check overlap with all placed components
                    overlap = False
                    for p in placed:
                        p_w = p.width if p.angle in (0, 180) else p.height
                        p_h = p.height if p.angle in (0, 180) else p.width
                        if boxes_overlap(cx, cy, pw, ph, p.x, p.y, p_w, p_h):
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
                                anchor_ref=anchor.ref,
                                anchor_pad=anchor_pad.number,
                            )

            # If we found a placement in this radius, use it
            if best_result is not None:
                return best_result

    return best_result


def parse_initial_positions(initial_path: str) -> dict:
    """Read manually-placed positions from _initial.kicad_pcb.

    Returns dict of ref → (x, y, angle) for non-passive components.
    """
    with open(initial_path, 'r') as f:
        text = f.read()

    positions = {}
    components = parse_components(text)
    for comp in components:
        if comp.ref:
            positions[comp.ref] = (comp.x, comp.y, comp.angle)
    return positions


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

    # Apply manual positions to non-passive components
    for comp in components:
        if not comp.is_passive and comp.ref in manual_positions:
            comp.x, comp.y, comp.angle = manual_positions[comp.ref]

    # Classify
    passives = [c for c in components if c.is_passive]
    non_passives = [c for c in components if not c.is_passive]
    print(f"  {len(non_passives)} non-passive (from manual placement)")
    print(f"  {len(passives)} passive (to auto-place)")

    # Build net → component+pad mapping
    net_components = {}
    for comp in components:
        for pad in comp.pads:
            if pad.net_name:
                if pad.net_name not in net_components:
                    net_components[pad.net_name] = []
                net_components[pad.net_name].append((comp, pad))

    # Start with non-passives as placed
    placed = list(non_passives)
    results = []
    failed = []

    for passive in passives:
        # Check if this is a "between" component (series R, coupling C)
        anchor1, anchor2 = find_between_anchors(passive, components, net_components)

        if anchor1 and anchor2:
            comp1, pad1, ppad1 = anchor1
            comp2, pad2, ppad2 = anchor2
            # Place at midpoint between the two anchors
            mid_x = (comp1.x + pad1.x_offset + comp2.x + pad2.x_offset) / 2
            mid_y = (comp1.y + pad1.y_offset + comp2.y + pad2.y_offset) / 2
            result = place_passive(passive, comp1, pad1, ppad1, placed, GRID_MM,
                                   between_pos=(mid_x, mid_y))
        else:
            # Find single anchor
            anchor, anchor_pad, passive_pad = find_anchor(passive, components, net_components)
            if anchor is None:
                failed.append(passive.ref)
                continue
            result = place_passive(passive, anchor, anchor_pad, passive_pad, placed, GRID_MM)

        if result:
            # Update passive position
            passive.x = result.x
            passive.y = result.y
            passive.angle = result.angle
            placed.append(passive)
            results.append(result)
        else:
            failed.append(passive.ref)

    # Write updated PCB file
    print(f"\nPlaced {len(results)} passives, {len(failed)} failed")

    if failed:
        print(f"Failed to place: {', '.join(failed)}")

    # Collect all components that need position updates
    all_updates = []

    # Non-passives: apply positions from _initial file
    for comp in non_passives:
        if comp.ref in manual_positions:
            mx, my, ma = manual_positions[comp.ref]
            all_updates.append((comp, mx, my, ma))

    # Passives: apply auto-placed positions
    for comp in passives:
        if comp.ref in [r.ref for r in results]:
            result = next(r for r in results if r.ref == comp.ref)
            all_updates.append((comp, result.x, result.y, result.angle))

    # Sort by file offset (descending) so we can replace without shifting issues
    all_updates.sort(key=lambda u: u[0].start_offset, reverse=True)

    for comp, new_x, new_y, new_angle in all_updates:
        block = pcb_text[comp.start_offset:comp.end_offset]

        at_pattern = re.compile(r'\(at\s+[\d.-]+\s+[\d.-]+(?:\s+[\d.-]+)?\)')
        if new_angle != 0:
            new_at = f'(at {new_x:.4f} {new_y:.4f} {new_angle:.0f})'
        else:
            new_at = f'(at {new_x:.4f} {new_y:.4f})'

        new_block = at_pattern.sub(new_at, block, count=1)
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

    # Write output
    out_path = pcb_path
    with open(out_path, 'w') as f:
        f.write(pcb_text)

    print(f"Written to {out_path}")
    print("\nPlacement summary:")
    for r in results:
        print(f"  {r.ref:12s} → ({r.x:7.2f}, {r.y:7.2f}) @ {r.angle:3.0f}°  "
              f"anchor: {r.anchor_ref}.{r.anchor_pad}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python layout.py <path-to-kicad_pcb>")
        sys.exit(1)
    run_placement(sys.argv[1])
