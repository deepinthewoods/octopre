---
name: rebuild
description: Rebuild pipeline after spec.md changes. Regenerates .zen files, builds KiCad project, detects component changes. Stops if large components (ICs, connectors, modules) were added/removed so user can manually place them before running /layout.
---

# Rebuild Pipeline

Run this after editing `spec.md` to push changes through the design pipeline.

## Steps

1. **Read current state**
   - Read `spec.md` for the updated specification
   - Read existing `.zen` files to understand current circuit
   - Run `pcb bom <board>.zen -f json` for both boards to snapshot current component list

2. **Update .zen files**
   - Regenerate/update `.zen` files for both `digital/` and `analog/` boards to match spec.md
   - Preserve passive anchor annotations
   - Run `pcb fmt` on all changed files
   - Run `pcb build` for both boards to validate

3. **Detect component changes**
   - Run `pcb bom` again on both boards after rebuild
   - Diff old vs new BOM
   - Classify changes:
     - **Large components** (ICs, modules, connectors, headers, trim pots): anything that needs manual placement
     - **Passive components** (resistors, capacitors, inductors, ferrite beads, diodes): auto-placed by layout.py

4. **If large components changed: STOP**
   - Print a summary of added/removed large components
   - Run `pcb layout` to regenerate `layout.kicad_pcb` for affected boards
   - Run `python make_initial.py` to regenerate `layout_initial.kicad_pcb`
   - Update `layout_guidance.md` with placement advice for any new large components
   - Tell the user: "Open `layout_initial.kicad_pcb` in KiCad, place the new components, save, then run `/layout`"
   - Do NOT run layout.py — the user needs to place ICs first

5. **If only passives changed (or no changes): continue**
   - Run `pcb layout` to regenerate `layout.kicad_pcb` for affected boards
   - Update `layout_guidance.md` if needed
   - Run `python layout.py` for both boards to place/re-place passives
   - Report what was placed/moved

## Key Rules

- NEVER move manually-placed components
- ALWAYS preserve existing component positions in the KiCad PCB file
- Only update the KiCad PCB layout when components are added or removed
- Passive anchor annotations in .zen files are the source of truth for layout.py
