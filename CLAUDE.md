# CLAUDE.md

> **MANDATORY — COMPLETE BEFORE ANY RESPONSE**
>
> At the start of every session, before producing any reply:
> 1. `git checkout main && git pull origin main` — the working directory may be on a stale branch.
> 2. Read all three: `HANDOFF_STATE.md`, `HANDOFF_WISDOM.md`, `Dabby_Handoff_Notes.md`.
> 3. If the opening message names a strain, also read `Dabby_Data.py`.
>
> These are not optional. Do not respond first and read later. Do not answer from memory or summaries.

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Dabby — Session Instructions

## Session-Start Reads

The three mandatory files and what they contain:
- `HANDOFF_STATE.md` — generated per-strain status: run counts, last dates, current equipment, current What to Try Next per strain. This is the working surface for run logging.
- `HANDOFF_WISDOM.md` — accumulated cross-strain patterns, equipment observations, failure modes, and methodology state.
- `Dabby_Handoff_Notes.md` — operational notes, session protocol, decisions made, known failure modes.

## Conditional Reads

Read these files when the session topic requires them:
- `Dabby_Data.py` — active run data, strain status, waypoints, and schema. Skip only when the session is clearly non-strain work (backlog, infra/CI, generator internals, UI/layout, documentation). If the opening message names a strain, read this before responding — not as a follow-up if questions get complex, but before the first reply. A Claude that hasn't read the data file will answer confidently from `HANDOFF_STATE.md` summaries and hallucinate the run history behind them. Users won't catch it until something is wrong. Frozen runs from finished jars live in `Dabby_Archive.py` (not a session-start read — see "Updating the Log").
- `Dabby_Log_Generator.py` — for generator/rendering work.
- `Dabby_Methodology.md` — for curve design or methodology questions.
- `Dabby_UI_Principles.md` — for UI/layout changes.

This project logs sessions on a Dr. Dabber Switch² nicknamed "Dabby the House Rig."
All material is hash rosin (ice water extracted, solventless) unless explicitly 
stated otherwise. The log records what happened, swab results, and current thinking 
on what to try next — not a formal calibration program.

## Commands

- **Generate the log:** `python3 Dabby_Log_Generator.py` (Windows: `python
  Dabby_Log_Generator.py`) — reads `Dabby_Data.py`, writes `index.html` and
  `HANDOFF_STATE.md`.
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
  plus explicit `from Dabby_Data import _ACCENT_RESOLVED, _resolve_accent_colors`
  (wildcard skips underscore names), plus `from Dabby_Archive import
  ARCHIVED_RUNS, ARCHIVED_STATUS` and a four-line reassignment block that
  combines archived + active lists and re-runs accent color resolution over the
  combined list. CSS is external in `style.css` (Session 36), linked from the
  generated `<head>`.
- **Adding a run or strain is data-only (Step 3 complete, Session 43).** All
  content — waypoints, dates, equipment, swab/session/verdict fields, `next_*`
  fields — lives in `Dabby_Data.py`. The generator loop in `build_html()`
  picks up new strains automatically. `Dabby_Log_Generator.py` requires no
  edits for run logging.
- **Equipment is per-run.** `EquipmentConfig` with nested `Insert`/`CarbCap`/`Pearl`
  dataclasses; sequenced `RIG_N` constants; Rig Reference block on the rendered log
  documents each rig. `validate()` rejects `equipment=None` — no field defaults by design.
- **Charts:** Chart.js from CDN, one per curve via `curve_chart_html()`, fed by
  the same waypoint list as the table; needs internet to render.
- **`DABBY_ARCHITECTURE.md`** is a living 6-step refactor plan (Steps 1–4 done;
  Steps 5–6 remaining). Read it before any structural/schema change; it
  supersedes the deleted `REFACTOR_TEMPLATE_DRIVEN.md`.
- **Infra hazards:** never use GitHub MCP `push_files` for `index.html` or
  routine commits (caused silent content loss — use git); `push_files` is
  acceptable only for temporary files on non-main branches when git checkout
  of that branch is impractical, and never for `index.html`. Never hand-write
  `index.html`.

## Updating the Log

Adding or changing a run is data-only: edit `Dabby_Data.py` — add the waypoint
constant, add a `CompletedRun` entry with all content fields, and update the
strain's `StrainStatus` `next_*` fields. Then run `python3 Dabby_Log_Generator.py`
to regenerate `index.html`. Commit both files to a feature branch, then open a PR.
`Dabby_Log_Generator.py` requires no edits for run logging.

Never write `index.html` by hand — always run the generator and commit its output.

`Dabby_Archive.py` is NOT a session-start read. It holds frozen runs from finished jars
(historical record, never edited). When writing `analysis` or `next_ai_analysis`, check
`HANDOFF_WISDOM.md` first — most cross-strain patterns are summarized there with specific
run citations. Read `Dabby_Archive.py` only when: (a) a wisdom citation points to archived
runs and the summary feels thin for the analysis at hand, (b) a pattern is flagged as
needing cross-strain confirmation and you want to search for it, or (c) a wisdom entry is
vague and you need the underlying run prose.

## Changing the Baseline Curve

`BASELINE_CURVE` always means "current recommended starting point for new strains." The invariant is maintained by renaming the retiring curve before redefining it. Skipping the rename causes every historical `CompletedRun` that referenced `BASELINE_CURVE` to silently render the new curve — wrong data, no error.

**Protocol:**

1. **Name the retiring curve by its endpoint temperature** — e.g., `BASELINE_416`, not `LEGACY_BASELINE`. Endpoint-temperature names are durable: they survive equipment changes and are self-documenting. Equipment-era names (e.g., `BASELINE_SAPPHIRE`) break down the moment the baseline changes without an equipment change.

2. **Define the retiring constant first.** Copy the current `BASELINE_CURVE` waypoints verbatim into `BASELINE_XXX` before redefining `BASELINE_CURVE`.

3. **Replace all COMPLETED_RUNS references.** Grep for `waypoints=BASELINE_CURVE,` (with trailing comma). Every match is a historical run that must be updated to `waypoints=BASELINE_XXX,`. Use `replace_all=True` in Edit — it's safe because the comma distinguishes these from `next_waypoints=BASELINE_CURVE` in STRAIN_STATUS (which does not have the leading `waypoints=` pattern).

4. **`next_waypoints=BASELINE_CURVE` in STRAIN_STATUS is intentional.** Those forward-pointing entries correctly reference the new baseline — do not change them.

5. **Check Dabby_Archive.py.** Confirm no `BASELINE_CURVE` references exist there. Archived runs use individual named constants and should always be clean, but verify.

6. **Update Dabby_Methodology.md Section 5 table** to reflect the new curve parameters (opening setpoint, ascent rate, endpoint, hold time).

7. Run the generator, verify output, commit.

## Date and Time Logging

User timezone: **America/Denver (MDT, UTC-6)**

When logging a run:
1. Capture `utc_logged_at = datetime.now(timezone.utc)` at logging time.
2. Derive local time by subtracting 6 hours (MDT) from UTC.
3. Confirm with the user before writing: "Logging this as [LOCAL DATE] at [LOCAL TIME] MDT ([UTC TIME] UTC) — correct the date or time if that's off."
4. Only surface the date discrepancy if UTC and local dates differ (i.e. after ~6pm MDT when UTC has rolled over).
5. Use the confirmed local date as `run_date` in the COMPLETED_RUNS tuple.
6. If the user corrects the time with a specific clock time ("it was at 8:30pm"), convert that to UTC and use it as `utc_logged_at` — not `datetime.now()`. If the user gives a relative offset ("about 10 minutes ago"), subtract from `datetime.now(timezone.utc)`. Either way, present the derived time in the confirmation prompt.
7. The handoff's `## Last updated:` header must be the **local date derived from `utc_logged_at` of the last run logged this session** (UTC−6) — not the UTC date, and not `run_date` (which reflects when the dab happened, not when logging occurred). For sessions with no new runs, apply UTC−6 to the current time.
8. For post-date runs, `utc_logged_at` can't be derived from `datetime.now()` — ask casually: "Do you have a sense of what time it was?" Use `None` if they don't know.

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

Changes go to a feature branch, then a PR to merge into `main`. Never commit data directly to main — always use a feature branch and PR. Every PR automatically gets a preview URL posted as a comment so the rendered log can be reviewed before merging.

PR descriptions should be plain English, not code diffs. Example format:

> Logged The Hive #1 Run 2 (May 8, 2026). Same curve as Run 1 — very light swab,  
> really nice session. Added note to try a lower endpoint (420–425°F) on Run 3.

One sentence per meaningful change. No technical details unless they affect 
interpretation of the results.

If work continues on an open PR across multiple commits or sessions, update the PR 
description to reflect what's actually in it. Use the GitHub MCP tool to read the 
current description first, then rewrite it to cover all changes to date.

When the user asks for the handoff to be updated, treat it as a session-close signal. Run the checklist in `HANDOFF_WISDOM.md` (six questions at the top) — each "yes" produces one update to the relevant wisdom table or section (or to the backlog in `Dabby_Handoff_Notes.md`, for Q6). Then update `Dabby_Handoff_Notes.md` (header date) and run the generator to regenerate `HANDOFF_STATE.md`. Before writing, scan for known issues and inconsistencies between what was done and what the docs say. Propose these alongside the update so they can be bundled into the same PR.

`HANDOFF_STATE.md` is always regenerated by running `python3 Dabby_Log_Generator.py` — never edit it by hand.

If there is already an open PR when the handoff update is written, push the handoff changes to that same branch — do not open a separate PR for the handoff alone.

## Reference Sections

The four reference sections (Device & Session Constants, Swab Color Reference, Baseline
Curve, Terpene Reference) live on the main index page as collapsible blocks. Do not
move them to a separate page — they collapse when not needed and are rarely accessed.

## Reasoning Standard

For methodology, design, and schema decisions, apply first-principles reasoning: decompose every undefined term to its atomic meaning before proceeding.

## Epistemic Flags

General:
- Match confidence to evidence weight. One run is an observation. Two 
  consistent runs are directional. Do not write "confirmed," "established," 
  or "resolved" until the evidence would be surprising if it reversed.
- Do not promote correlates to causal variables. If the mechanism is 
  unresolved, describe what happened and flag the mechanism as open. 
  Example: "harshness entered on draw 3" is data; "the 2-draw ceiling" 
  treats draw count as the boundary variable when it may be a proxy for 
  depletion, cumulative heat exposure, or something else.

Domain-specific:
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
