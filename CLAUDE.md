# Dabby — Session Instructions

At the start of every session:
1. Run `git checkout main && git pull origin main` — do this before reading any files. The working directory may be on a stale branch.
2. Read these files (all are in the repo):
   - `Dabby_Handoff_Notes.md` — source of truth, read first
   - `Dabby_Methodology.md` — thermal model and session process reasoning
   - `Dabby_Log_Generator.py` — understand current log structure before touching it

This project logs sessions on a Dr. Dabber Switch² nicknamed "Dabby the House Rig."
All material is hash rosin (ice water extracted, solventless) unless explicitly 
stated otherwise. The log records what happened, swab results, and current thinking 
on what to try next — not a formal calibration program.

## Updating the Log

Edit `Dabby_Log_Generator.py` directly. Run with `python3 Dabby_Log_Generator.py` 
to produce `index.html`. Commit both files to a feature branch, then open a PR.

Never write `index.html` by hand — always run the generator and push its output.

## Date and Time Logging

User timezone: **America/Denver (MDT, UTC-6)**

When logging a run:
1. Capture `utc_logged_at = datetime.now(timezone.utc)` at logging time.
2. Derive local time by subtracting 6 hours (MDT) from UTC.
3. Confirm with the user before writing: "Logging this as [LOCAL DATE] at [LOCAL TIME] MDT ([UTC TIME] UTC) — correct the date or time if that's off."
4. Only surface the date discrepancy if UTC and local dates differ (i.e. after ~6pm MDT when UTC has rolled over).
5. Use the confirmed local date as `run_date` in the COMPLETED_RUNS tuple.

## Confirm Before Acting

Before taking any substantive action — editing files, updating methodology, 
proposing curve changes, restructuring the log — present what you are about to 
do and wait for explicit confirmation. Do not proceed until the user approves. 
Stating the plan and immediately executing is not proposing — it is narrating. 
Stop and wait.

Mechanical steps that follow from an already-approved decision do not need a 
separate confirmation: running the generator after changes are agreed, committing, 
pushing, and opening PRs can all be done without asking.

## PR Workflow

Changes go to a feature branch, then a PR to merge into `main`. Every PR 
automatically gets a preview URL posted as a comment so the rendered log can be 
reviewed before merging.

PR descriptions should be plain English, not code diffs. Example format:

> Logged The Hive #1 Run 2 (May 8, 2026). Same curve as Run 1 — very light swab,  
> really nice session. Added note to try a lower endpoint (420–425°F) on Run 3.

One sentence per meaningful change. No technical details unless they affect 
interpretation of the results.

If work continues on an open PR across multiple commits or sessions, update the PR 
description to reflect what's actually in it. Use the GitHub MCP tool to read the 
current description first, then rewrite it to cover all changes to date.

## Reference Sections

The four reference sections (Device & Session Constants, Swab Color Reference, Baseline
Curve, Terpene Reference) are collapsible grey-header blocks on the main index page.
Keep them that way:

- Grey headers are intentional — they signal "reference material, not a run." Do not
  apply accent colors or green styling to them.
- Do not move them to a separate page. They live on index alongside the strain content
  and collapse when not needed.

## Accent Color Rules

Each strain gets one accent color assigned in STRAIN_STATUS and ACCENT_PALETTE.
When adding or changing a color:

1. No greens. The log page uses a green family (#2D5A3D, #4A7C59, #F0F7F2). Accent 
   colors in the green hue range (~90–165°) will clash with the UI chrome.
2. Minimum hue separation. Aim for at least 30° HSL hue distance from every existing 
   accent, or a clear lightness difference if hues are close.
3. When ACCENT_PALETTE runs out it cycles — add new entries rather than let colors repeat.

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
