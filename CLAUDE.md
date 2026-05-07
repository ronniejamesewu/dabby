# Dabby — Session Instructions

At the start of every session, read these files (all are in the repo):
- `Dabby_Handoff_Notes.md` — source of truth, read first
- `Dabby_Methodology.md` — thermal model and calibration reasoning
- `Dabby_Log_Generator.py` — understand current log structure before touching it

This project documents temperature curve calibration for live rosin sessions 
on a Dr. Dabber Switch² nicknamed "Dabby the House Rig." All material is hash 
rosin (ice water extracted, solventless) unless explicitly stated otherwise.

## Updating the Log

Edit `Dabby_Log_Generator.py` directly. Run with `python3 Dabby_Log_Generator.py` 
to produce `index.html`. Commit and push both files to main.

Never write `index.html` by hand — always run the generator and push its output.

## Epistemic Flags

- Terpene profiles are inferred from genetics, not measured. The same generic 
  cannabis terpene palette appears across most strains. Do not present inferences 
  as specifications or dress up the generic palette as strain-specific knowledge.
- Swab color is a within-strain directional signal only. Do not compare across strains.
- Nose is a weak secondary signal. User has a non-discerning palate. Use genetics 
  as primary source.
- Do not assume a large titanium-to-insert offset. Setpoints are reasonable proxies 
  for material contact temperature.
- Do not reason about cold-material thermal shock. Cold start means material and 
  insert co-heat from ambient together.
- Do not import flower rosin assumptions. Hash rosin vaporizes more cleanly at lower 
  temperatures — efficiency argument, not heat sensitivity.
- Baseline curve is the starting point for all strains. Do not design different 
  starting curves from strain name, terpene profile, or consistency alone. Empirical 
  swab results drive adjustment.
