#!/usr/bin/env python3
"""
make_initial.py — Strip a KiCad PCB to only non-passive components.

Creates a _initial.kicad_pcb file containing only ICs, connectors, headers,
and other large components that need manual placement. Passives (resistors,
capacitors, ferrite beads, LEDs, diodes, test points) are removed.

Usage:
    python make_initial.py boards/digital/layout/layout.kicad_pcb
    python make_initial.py boards/analog/layout/layout.kicad_pcb

Output:
    boards/digital/layout/layout_initial.kicad_pcb
    boards/analog/layout/layout_initial.kicad_pcb
"""

import re
import sys
import os
import uuid as _uuid


# Board outline dimensions (mm) from spec
BOARD_WIDTH = 70.0
BOARD_HEIGHT = 55.0
MOUNTING_HOLE_DIA = 3.0
MOUNTING_HOLE_INSET = 3.0  # mm from board edge to hole center

# Footprint patterns for passive components (to be removed)
PASSIVE_PATTERNS = [
    r"R_\d{4}",       # resistors (R_0402, R_0603, etc.)
    r"C_\d{4}",       # capacitors
    r"C_\d{5}",       # larger caps
    r"LED_\d{4}",     # LEDs
    r"D_SOD",         # diodes
    r"TestPoint",     # test points
]


def is_passive_footprint(fp_name: str) -> bool:
    for pattern in PASSIVE_PATTERNS:
        if re.search(pattern, fp_name):
            return True
    return False


def find_matching_paren(text: str, start: int) -> int:
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


def add_board_outline(pcb_text: str) -> str:
    """Add a board outline (Edge.Cuts rectangle) if not already present.

    Places a 70x55mm rectangle centered around the existing component positions.
    Also adds 3mm mounting holes at corners.
    """
    if 'Edge.Cuts' in pcb_text and 'gr_rect' in pcb_text:
        return pcb_text  # outline already exists

    # Find the center of all component positions to place outline around them
    at_matches = re.findall(r'\(at\s+([\d.-]+)\s+([\d.-]+)', pcb_text)
    if not at_matches:
        cx, cy = 150.0, 100.0  # default center
    else:
        xs = [float(m[0]) for m in at_matches]
        ys = [float(m[1]) for m in at_matches]
        cx = (min(xs) + max(xs)) / 2
        cy = (min(ys) + max(ys)) / 2

    # Board rectangle corners
    x1 = round(cx - BOARD_WIDTH / 2, 2)
    y1 = round(cy - BOARD_HEIGHT / 2, 2)
    x2 = round(cx + BOARD_WIDTH / 2, 2)
    y2 = round(cy + BOARD_HEIGHT / 2, 2)

    outline = f'''
\t(gr_rect (start {x1} {y1}) (end {x2} {y2})
\t\t(stroke (width 0.05) (type default))
\t\t(fill none)
\t\t(layer "Edge.Cuts")
\t\t(uuid "{_uuid.uuid4()}")
\t)'''

    # Insert before the final closing paren
    insert_pos = pcb_text.rfind(')')
    pcb_text = pcb_text[:insert_pos] + outline + '\n' + pcb_text[insert_pos:]

    print(f"  Added board outline: {BOARD_WIDTH}x{BOARD_HEIGHT}mm at ({x1},{y1})-({x2},{y2})")
    return pcb_text


def strip_passives(pcb_path: str):
    with open(pcb_path, 'r') as f:
        pcb_text = f.read()

    # Find all footprint blocks and mark passives for removal
    removals = []
    fp_pattern = re.compile(r'\n\t\(footprint ')
    for m in fp_pattern.finditer(pcb_text):
        start = m.start()  # include the leading newline
        block_start = m.start() + 1
        end = find_matching_paren(pcb_text, block_start)

        block = pcb_text[block_start:end + 1]
        fp_match = re.search(r'\(footprint\s+"([^"]*)"', block)
        if fp_match:
            fp_name = fp_match.group(1)
            if is_passive_footprint(fp_name):
                removals.append((start, end + 1))

    # Remove passive blocks in reverse order to preserve offsets
    result = pcb_text
    for start, end in reversed(removals):
        result = result[:start] + result[end:]

    # Add board outline if not already present
    result = add_board_outline(result)

    # Write output
    out_path = pcb_path.replace('.kicad_pcb', '_initial.kicad_pcb')
    with open(out_path, 'w') as f:
        f.write(result)

    total = len(list(fp_pattern.finditer(pcb_text)))
    kept = total - len(removals)
    print(f"Read {pcb_path}: {total} components")
    print(f"Removed {len(removals)} passives, kept {kept} non-passives")
    print(f"Written to {out_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python make_initial.py <path-to-layout.kicad_pcb>")
        sys.exit(1)
    strip_passives(sys.argv[1])
