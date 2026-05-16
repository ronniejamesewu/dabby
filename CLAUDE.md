# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Dabby — Session Instructions

At the start of every session:
1. Run `git checkout main && git pull origin main` — do this before reading any files. The working directory may be on a stale branch.
2. Read these files (all are in the repo):
   - `Dabby_Handoff_Notes.md` — source of truth, read first
   - `Dabby_Methodology.md` — thermal model and session process reasoning
   - `Dabby_Log_Generator.py` — understand current log structure before touching it
   - `Dabby_UI_Principles.md` - source of truth for UI implementation

This project logs sessions on a Dr. Dabber Switch² nicknamed "Dabby the House Rig."
All material is hash rosin (ice water extracted, solventless) unless explicitly 
stated otherwise. The log records what happened, swab results, and current thinking 
on what to try next — not a formal calibration program.

## Commands

- **Generate the log:** `python3 Dabby_Log_Generator.py` (Windows: `python
  Dabby_Log_Generator.py`) — reads `Dabby_Data.py`, writes `index.html`.
- `validate()` and `validate_accent_colors()` run automatically at the top of
  `build_html()`. A data error prints `VALIDATION ERRORS:` and exits 1 — a bad
  edit fails the generate step instead of producing a broken page.
- **No test suite, linter, or build system.** The logged runs are the de-facto
  regression suite; correctness is verified by eyeballing rendered `index.html`
  (locally or via the PR preview URL).
- **Deploy is automatic:** push to `main` → `deploy.yml` regenerates and
  publishes to GitHub Pages. Each PR auto-gets a preview URL via `preview.yml`.
  Both share a `gh-pages` concurrency group to avoid a merge race.

## Architecture

- **Two-file split (Session 31).** `Dabby_Data.py` = all data + dataclasses
  (`Waypoint`, `CompletedRun`, `EquipmentConfig`, `StrainStatus`,
  `TerpeneEntry`), `GLOBAL_INFO`, `COMPLETED_RUNS`, `STRAIN_STATUS`,
  `TERPENE_REFERENCE`, accent-color resolution, and `validate()`.
  `Dabby_Log_Generator.py` = rendering only; imports `from Dabby_Data import *`
  plus an explicit `from Dabby_Data import _ACCENT_RESOLVED` (wildcard skips
  underscore names). CSS is external in `style.css` (Session 36), linked from
  the generated `<head>`.
- **Run content is split across both files (key gotcha).** Structured data
  (waypoints, dates, equipment) lives in `Dabby_Data.py`; the per-run narrative
  (swab/vapor/verdict, "What to Try Next") is still string literals inside
  `build_html()`. `build_html()` enumerates one inline block per strain between
  `# ── <STRAIN>` and `# ── Assemble` dividers (known structural debt).
- **Equipment is per-run.** `EquipmentConfig` with two named regimes
  `_SPINNER`/`_GEMLOCK`; cutover at MB9ZST Run 1 (May 13 2026). `validate()`
  rejects `equipment=None` — no field defaults by design.
- **Charts:** Chart.js from CDN, one per curve via `curve_chart_html()`, fed by
  the same waypoint list as the table; needs internet to render.
- **`DABBY_ARCHITECTURE.md`** is a living 6-step refactor plan (Steps 1–2 done;
  Step 3 — the data-driven loop that eliminates the two-file run-content split —
  gated on open sub-problems N2/N5). Read it before any structural/schema
  change; it supersedes the deleted `REFACTOR_TEMPLATE_DRIVEN.md`.
- **Infra hazards:** never use GitHub MCP `push_files` for `index.html` or
  routine commits (caused silent content loss — use git); never hand-write
  `index.html`.

## Updating the Log

Adding or changing a run touches **two files** (see Architecture): put
structured data (waypoints, dates, equipment, `STRAIN_STATUS`) in
`Dabby_Data.py`, and the run's narrative HTML block plus its
`what_to_try_next_html()` call in `build_html()` in `Dabby_Log_Generator.py`.
Then run `python3 Dabby_Log_Generator.py` to regenerate `index.html`. Commit
all three files to a feature branch, then open a PR.

Never write `index.html` by hand — always run the generator and commit its
output. Editing only `Dabby_Data.py` silently renders a page where dashboard
counts increment but the run section is missing — verify the rendered HTML
before committing.

## Date and Time Logging

User timezone: **America/Denver (MDT, UTC-6)**

When logging a run:
1. Capture `utc_logged_at = datetime.now(timezone.utc)` at logging time.
2. Derive local time by subtracting 6 hours (MDT) from UTC.
3. Confirm with the user before writing: "Logging this as [LOCAL DATE] at [LOCAL TIME] MDT ([UTC TIME] UTC) — correct the date or time if that's off."
4. Only surface the date discrepancy if UTC and local dates differ (i.e. after ~6pm MDT when UTC has rolled over).
5. Use the confirmed local date as `run_date` in the COMPLETED_RUNS tuple.
6. If the user corrects the time with a specific clock time ("it was at 8:30pm"), convert that to UTC and use it as `utc_logged_at` — not `datetime.now()`. If the user gives a relative offset ("about 10 minutes ago"), subtract from `datetime.now(timezone.utc)`. Either way, present the derived time in the confirmation prompt.
7. The handoff's `## Last updated:` header and changelog entry date must be the **local date derived from `utc_logged_at` of the last run logged this session** (UTC−6) — not the UTC date, and not `run_date` (which reflects when the dab happened, not when logging occurred). For sessions with no new runs, apply UTC−6 to the current time.

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

When the user asks for the handoff to be updated, treat it as a session-close signal. Before writing, scan for open items in the handoff that can be resolved now, known issues in the generator or log files, and inconsistencies between what was done and what the handoff says. Propose these alongside the handoff update so they can be bundled into the same PR.

If there is already an open PR when the handoff update is written, push the handoff changes to that same branch — do not open a separate PR for the handoff alone.

## Reference Sections

The four reference sections (Device & Session Constants, Swab Color Reference, Baseline
Curve, Terpene Reference) live on the main index page as collapsible blocks. Do not
move them to a separate page — they collapse when not needed and are rarely accessed.

## Reasoning Standard

For methodology, design, and schema decisions, apply first-principles reasoning: decompose every undefined term to its atomic meaning before proceeding.

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
