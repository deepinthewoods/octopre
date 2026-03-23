---
name: layout
description: Run passive component auto-placement after user has manually placed ICs/connectors in KiCad. Reads the saved .kicad_pcb file, places passives on 1mm grid near their anchor components, avoids overlaps.
---

# Layout — Passive Auto-Placement

Run this after manually placing large components (ICs, connectors, headers) in KiCad and saving the PCB file.

## Steps

1. **Verify readiness**
   - Check that `layout_initial.kicad_pcb` exists for both boards
   - Check that `layout.kicad_pcb` (full PCB) exists for both boards
   - If `layout_initial.kicad_pcb` is missing, run `python make_initial.py` first
   - Warn the user if any large component in `_initial` appears unplaced

2. **Run layout.py**
   - Execute `python layout.py boards/digital/layout/layout.kicad_pcb`
   - Execute `python layout.py boards/analog/layout/layout.kicad_pcb`
   - The script will:
     - Read full `layout.kicad_pcb` (all components)
     - Read `layout_initial.kicad_pcb` for manually-placed IC positions
     - Apply IC positions to the full PCB
     - For each passive, find optimal position on 1mm grid near anchor
     - Orient each passive so its anchor pad faces the target component pin
     - For "between" passives: place at midpoint between two anchor components
     - Write the updated `layout.kicad_pcb`

3. **Report results**
   - List all passives that were placed, with their positions
   - Flag any passives that couldn't be placed (no valid grid position found)
   - Remind user to open KiCad and review the placement

## Key Rules

- NEVER move components that already have a non-origin position — these were manually placed
- Place passives on a 1mm grid
- Try both 0° and 90° orientations, pick the one that puts the anchor pad closest to its target
- If a passive can't be placed without overlapping, expand the search radius and report it
