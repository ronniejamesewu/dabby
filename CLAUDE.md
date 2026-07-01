# CLAUDE.md

> **MANDATORY — COMPLETE BEFORE ANY RESPONSE**
>
> At the start of every session, before producing any reply:
> 1. `git checkout main && git pull origin main` — the working directory may be on a stale branch.
> 2. Read all three: `HANDOFF_STATE.md`, `HANDOFF_WISDOM.md`, `Dabby_Handoff_Notes.md`.
> 3. If the opening message names a strain, also read that strain's jar file in `jars/` (filename = the strain's slug — `Glob jars/*.py` to discover, or check `jar_manifest.py`).
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
- `jars/<slug>.py` — one file per jar, holding that jar's runs (`RUNS`), status (`STATUS`), and local waypoint constants. This is the per-strain run data, status, waypoints. If the opening message names a strain, read its jar file before responding — not as a follow-up if questions get complex, but before the first reply. A Claude that hasn't read the jar file will answer confidently from `HANDOFF_STATE.md` summaries and hallucinate the run history behind them. Users won't catch it until something is wrong. Discover the slug via `Glob jars/*.py` or `jar_manifest.py`. Closed jars are jar files too (in the `CLOSED` tier) — not a separate archive file.
- `Dabby_Core.py` — dataclasses, `RIG_N` constants, `BASELINE_*` curves, `GLOBAL_INFO`, `TERPENE_REFERENCE`, color resolution, `validate()`. Read for schema/equipment/baseline questions. If the named jar has `RUNS = []`, read this file at session start — use the CONTENTS index at the top to jump directly to `CompletedRun` and `StrainStatus`.
- `jar_manifest.py` — the `ACTIVE` / `CLOSED` tier lists and the load function that assembles all jars. Read for lifecycle work.
- `Dabby_Log_Generator.py` — for generator/rendering work.
- `Dabby_Methodology.md` — for curve design or methodology questions.
- `Dabby_UI_Principles.md` — for UI/layout changes.

This project logs sessions on a Dr. Dabber Switch² nicknamed "Dabby the House Rig."
All material is hash rosin (ice water extracted, solventless) unless explicitly 
stated otherwise. The log records what happened, swab results, and current thinking 
on what to try next — not a formal calibration program.

## Commands

- **Generate the log:** `python3 Dabby_Log_Generator.py` (Windows: `python
  Dabby_Log_Generator.py`) — assembles the jar files via `jar_manifest.py`, writes
  `index.html` and `HANDOFF_STATE.md`.
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

- **Per-jar architecture (Session 108).** Three layers: (1) `Dabby_Core.py` =
  dataclasses (`Waypoint`, `Insert`, `CarbCap`, `Pearl`, `EquipmentConfig`,
  `CompletedRun`, `StrainStatus`, `TerpeneEntry`), `GLOBAL_INFO`, `FIRST_RUN_DATE`,
  `BASELINE_416`, `BASELINE_CURVE`, `RIG_1`–`RIG_5`, `TERPENE_REFERENCE`,
  accent-color resolution, and the parameterized `validate(runs, statuses)` /
  `validate_accent_colors(statuses, resolved)`. (2) `jars/<slug>.py` = one file per
  jar, each exporting `RUNS` (list of `CompletedRun`) and `STATUS` (a single
  `StrainStatus`), plus that jar's local waypoint constants; each imports only
  `datetime` and `from Dabby_Core import *`. (3) `jar_manifest.py` = `ACTIVE` /
  `CLOSED` slug lists + `load_all_jars()`, which assembles them (closed first,
  then active) into the combined `COMPLETED_RUNS` / `STRAIN_STATUS`.
  `Dabby_Log_Generator.py` = rendering only; imports `from Dabby_Core import *`,
  `from Dabby_Core import _resolve_accent_colors`, and
  `from jar_manifest import load_all_jars`, then
  `COMPLETED_RUNS, STRAIN_STATUS = load_all_jars()` and re-runs accent resolution
  over the combined list. CSS is external in `style.css` (Session 36).
- **Jar isolation invariant.** Jar files never import from other jar files. If two
  jars need the same curve, the waypoint values are duplicated locally (e.g.
  Watermellos carries its own copies of the FW106 curves it borrowed). Shared
  constants (`BASELINE_*`, `RIG_N`) come from `Dabby_Core`, never duplicated.
- **Adding a run is data-only.** Edit the jar file in `jars/`: add the local
  waypoint constant, add a `CompletedRun` to `RUNS`, update the jar's `STATUS`
  `next_*` fields. The generator loop picks it up automatically — no generator
  edits for run logging. A new strain = a new `jars/<slug>.py` (from the
  boilerplate pattern) + its slug added to `ACTIVE` in `jar_manifest.py` with an
  inline name comment (`'slug',  # Full Strain Name`); `validate()` and the manifest
  preflight catch a missed half.
- **Lifecycle.** Two tiers: `ACTIVE` (material remaining) and `CLOSED` (jar
  done). Closing a jar = move its slug from `ACTIVE` to `CLOSED` in
  `jar_manifest.py`. The jar file itself is never touched by the move. The
  rendered log shows each jar's last-run date, which is sufficient to surface
  idle jars without a separate dormancy check.
- **Equipment is per-run.** `EquipmentConfig` with nested `Insert`/`CarbCap`/`Pearl`
  dataclasses; sequenced `RIG_N` constants; Rig Reference block on the rendered log
  documents each rig. `validate()` rejects `equipment=None` — no field defaults by design.
- **Charts:** Chart.js from CDN, one per curve via `curve_chart_html()`, fed by
  the same waypoint list as the table; needs internet to render.
- **Infra hazards:** never use GitHub MCP `push_files` for `index.html` or
  routine commits (caused silent content loss — use git); `push_files` is
  acceptable only for temporary files on non-main branches when git checkout
  of that branch is impractical, and never for `index.html`. Never hand-write
  `index.html`.

## Updating the Log

Adding or changing a run is data-only: edit the strain's `jars/<slug>.py` — add the
local waypoint constant, add a `CompletedRun` to `RUNS` with all content fields, and
update the jar's `STATUS` `next_*` fields. Then run `python3 Dabby_Log_Generator.py`
to regenerate `index.html`. Commit the jar file and the regenerated output to a
feature branch, then open a PR. `Dabby_Log_Generator.py` requires no edits for run
logging.

Never write `index.html` by hand — always run the generator and commit its output.

Closed jars are jar files like any other (in the `CLOSED` tier of
`jar_manifest.py`) — historical record, never edited. When writing `analysis` or
`next_ai_analysis`, check `HANDOFF_WISDOM.md` first — most cross-strain patterns are
summarized there with specific run citations. Read a closed jar's `jars/<slug>.py`
only when: (a) a wisdom citation points to its runs and the summary feels thin for
the analysis at hand, (b) a pattern is flagged as needing cross-strain confirmation
and you want to search for it, or (c) a wisdom entry is vague and you need the
underlying run prose.

## Date and Time Logging

User timezone: **America/Denver (MDT, UTC-6)**

When logging a run:
1. Capture `utc_logged_at = datetime.now(timezone.utc)` at logging time.
2. Derive local time by subtracting 6 hours (MDT) from UTC.
3. Confirm with the user before writing: "Logging this as [LOCAL DATE] at [LOCAL TIME] MDT ([UTC TIME] UTC) — correct the date or time if that's off."
4. Only surface the date discrepancy if UTC and local dates differ (i.e. after ~6pm MDT when UTC has rolled over).
5. Use the confirmed local date as `run_date` in the new `CompletedRun` entry (added to the jar's `RUNS` list).
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

The five reference sections (Device & Session Constants, Swab Color Reference, Baseline
Curve, Terpene Reference, Rig Reference) live on the main index page as collapsible blocks.
Do not move them to a separate page — they collapse when not needed and are rarely accessed.

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
