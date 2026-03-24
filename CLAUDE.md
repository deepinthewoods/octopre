# 8-Channel Audio DSP — Project Guide

## Pipeline Overview

This project uses a spec-driven pipeline to produce two PCBs (digital board + analog board):

```
spec.md → .zen files → pcb layout → layout.kicad_pcb
                                   → make_initial.py → layout_initial.kicad_pcb
                                                      → user places ICs in KiCad
                                                      → layout.py → final layout.kicad_pcb
```

### Pipeline Steps

1. **spec.md** — Source of truth for the circuit design
2. **.zen files** — Zener HDL describing both boards' schematics
3. **`pcb layout`** — Compiles .zen → `layout.kicad_pcb` (all components)
4. **`make_initial.py`** — Strips passives → `layout_initial.kicad_pcb` (ICs only)
5. **Manual placement** — User opens `layout_initial.kicad_pcb` in KiCad, places ICs/connectors/headers, saves
6. **`layout.py`** — Reads positions from `layout_initial.kicad_pcb`, applies to full `layout.kicad_pcb`, auto-places passives on 1mm grid

### When spec.md changes

Re-run the pipeline. Key rules:
- **Always regenerate** .zen files from the updated spec
- **Only update** the KiCad PCB layout file if components were added or removed
- **Only regenerate `layout_initial.kicad_pcb`** when large components (ICs, connectors, headers) are added or removed. This file contains the user's manual placements — never overwrite it otherwise.
- **Always preserve** manually-placed component positions — never move them
- **Re-run layout.py** to place any new passives or adjust for removed ones

### Passive Anchor Annotations (in .zen files)

Each passive component gets an annotation indicating which pad should be closest to which connected component:

- **Decoupling caps**: VCC pad anchored to the IC power pin, GND pad unconstrained
- **Series resistors / coupling caps**: Placed between two connected components. Annotate which pad faces which component
- **Bulk caps**: Anchored near the IC but with looser constraint
- GND pads are unconstrained (don't care about pour proximity)

### layout.py Behavior

- Reads full `layout.kicad_pcb` (all components from pcb layout)
- Reads `layout_initial.kicad_pcb` for manually-placed IC positions and layers
- Applies IC positions and layers to non-passive components in the full PCB
- Supports double-sided placement (digital board):
  - Passives are placed on the same side (F.Cu/B.Cu) as their anchor IC
  - If no space on the anchor's side, falls back to the opposite side
  - Layer flipping swaps all F.*/B.* layer references in the footprint block
  - Overlap checking is per-layer (components on different sides don't collide)
- For each passive:
  - Finds anchor pad and target pin location via net connectivity
  - Searches outward from anchor point on 1mm grid
  - Tries 0° and 90° orientations, picks best fit
  - For "between" passives: places at midpoint between two anchor components
- Writes updated `layout.kicad_pcb` with all components placed

### layout_guidance.md

A generated file describing which large components should be placed near each other,
and general layout advice derived from the spec. Updated when .zen files change.

## File Structure

```
spec.md                                    # Circuit specification (source of truth)
boards/digital/digital.zen                 # Digital board Zener HDL
boards/digital/layout/layout.kicad_pcb     # Full PCB (generated, then updated by layout.py)
boards/digital/layout/layout_initial.kicad_pcb  # ICs only (for manual placement)
boards/analog/analog.zen                   # Analog board Zener HDL
boards/analog/layout/layout.kicad_pcb      # Full PCB
boards/analog/layout/layout_initial.kicad_pcb   # ICs only
components/                                # Downloaded component definitions
make_initial.py                            # Strips passives from PCB → _initial file
layout.py                                  # Auto-places passives using _initial positions
layout_guidance.md                         # Manual placement guide for ICs/connectors
```

## Custom Skills

- `/rebuild` — After editing spec.md: regenerates .zen, builds KiCad, detects changes. **Stops** if large components (ICs, connectors, modules) were added/removed, so user can manually place them in KiCad first. If only passives changed, runs layout.py automatically.
- `/layout` — After manually placing large components in KiCad and saving: runs layout.py to auto-place passives on 1mm grid near their anchor components.
