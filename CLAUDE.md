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
to produce `index.html`. Commit both files to a feature branch, then open a PR.

Never write `index.html` by hand — always run the generator and push its output.

## Confirm Before Acting

Before taking any action — editing files, running the generator, committing, 
updating methodology or handoff notes — present what you are about to do and 
wait for explicit confirmation. Do not proceed until the user approves. Stating 
the plan and immediately executing is not proposing — it is narrating. Stop and wait.

## PR Workflow

Changes go to a feature branch, then a PR to merge into `main`. Every PR 
automatically gets a preview URL posted as a comment so the rendered log can be 
reviewed before merging.

PR descriptions should be plain English, not code diffs. Example format:

> Logged The Hive #1 Run 2 (May 8, 2026). Same curve as Run 1 — very light swab,  
> really nice session. Added note to try a lower endpoint (420–425°F) on Run 3.

One sentence per meaningful change. No technical details unless they affect 
interpretation of the results.

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
