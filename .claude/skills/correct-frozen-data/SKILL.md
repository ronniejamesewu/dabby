---
name: correct-frozen-data
description: Correct errors in already-logged, historically-frozen run data in this Dabby project -- wrong equipment, wrong date, wrong swab color, etc. This is correction by exception, not casual revision. Trigger when the user or the AI identifies an error in a previously logged run's data fields that needs correcting. Phrases -- "that run had the wrong rig", "the equipment was actually X", "fix the date on Run N", "that swab color was wrong". Also trigger when a pattern analysis reveals systematic errors across multiple runs (e.g. stale equipment defaults). This skill corrects frozen data by exception -- it never casually overwrites analysis when thinking changes (that goes to StrainStatus.next_ai_analysis per the frozen-analysis rule).
---

# Correct Frozen Data

Corrects errors in already-logged run data -- the one exception to the
"analysis is frozen and historically stable" rule. The procedure was fully
worked out in PR #206 (the seven-run equipment correction, July 2, 2026).

## Terms

| Term | Meaning |
|---|---|
| Frozen data | Any field on a `CompletedRun` that has already been committed. Once written, these are historically stable -- correctable by exception when genuinely wrong, never casually overwritten. |
| By-exception note | A dated parenthetical appended to a run's frozen `analysis` field marking what was corrected, when, and why. The traceable record that a correction happened. |
| Error mechanism | The root cause of the error -- stale equipment defaults, UTC-rollover date bugs, typos. Determines whether the error is systemic (affecting multiple runs) or one-off. |
| Derived claims | Statements in `HANDOFF_WISDOM.md`, `Dabby_Methodology.md`, or `StrainStatus` fields that cite the corrected run(s) and may need revision. |

**Two registers.** Field names (`utc_logged_at`, `equipment`, `analysis`),
`RIG_N` constants, jar slugs, and this file's step names are machine-side
vocabulary -- they never appear in a reply to the user. The user sees full
strain names, rig display expansions, and outcome language.

## Hard rules

- **Corrections are by exception only.** This skill fixes genuinely wrong
  data. Revising current thinking about a strain goes to
  `StrainStatus.next_ai_analysis`, not a prior run's frozen `analysis`.
- **The user is the sole witness.** Always confirm with the user before
  changing any frozen data -- they were there, the AI was not.
- **Every correction gets a dated note.** The by-exception note in the
  `analysis` field makes the correction traceable. Never silently change
  a frozen field.

## When NOT to use

- **Revising current thinking about a strain** -- changes to current
  strategy go to `StrainStatus.next_ai_analysis`, not a prior run's
  frozen `analysis`. That's normal log-run work.
- **Logging a new run** -- that's the log-run skill
  (`.claude/skills/log-run/SKILL.md`).
- **Fixing a validation error on a run being logged right now** -- that's
  a log-run recovery path, not a correction to historical data.
- **Closing a jar** -- that's the close-jar skill
  (`.claude/skills/close-jar/SKILL.md`).

## Workflow

**1. Establish the error mechanism.**
Before correcting anything, understand *why* the data is wrong:
- Which field(s) are wrong
- What the correct value is and why you're confident
- Whether the same error could affect other runs (same session, same jar,
  same time period)

A systematic error (stale equipment default, UTC-rollover date bug)
requires a cross-jar sweep (step 2). A one-off typo skips to step 3 with
a single-run scope.

**2. Build the cross-jar chronology (systematic errors only).**
When the error mechanism could affect multiple runs:
- Identify the time window during which the error could have occurred
- Grep across `jars/*.py` for all runs in that window (by `run_date` or
  `utc_logged_at`)
- Build a chronological list ordered by `utc_logged_at` across all jars
- For each run, check whether it's affected by the error mechanism

The Session 140 equipment correction is the worked example: the mechanism
was "stale jar-local equipment default after a 14-15-day gap"; the
chronology showed every run from June 17 to July 1 was Rig 6 except two
clusters (WM R16-18 and bp4rw13 R5-R8) that immediately followed long
jar-local gaps.

**3. Check `dab_notes` for user-voice evidence.**
Read the affected run's `dab_notes` for any user-reported information that
confirms or contradicts the proposed correction. `dab_notes` is the user's
verbatim words at logging time -- the closest thing to ground truth.

If `dab_notes` contradicts the proposed correction, stop and discuss with
the user.

**4. Confirm with the user.**
Present:
- Which run(s) are affected
- What the current (wrong) value is
- What the proposed correct value is
- The evidence for the correction

For systematic errors affecting many runs, present the full list and get
blanket confirmation rather than asking per-run.

**5. Correct the fields + add dated by-exception notes.**
For each affected run in `jars/<slug>.py`:
- Change the incorrect field(s) to the correct value(s)
- Append a dated by-exception note to the run's frozen `analysis` field.
  Convention from PR #206 -- append at the end of the existing analysis
  text as a parenthetical:

  `" (Equipment corrected July 2, 2026 from Rig 5 to Rig 6 -- stale
  jar-local default after a 15-day gap; see Dabby_Handoff_Notes.md
  backlog.)"`

  Do not rewrite the rest of the analysis; only append the correction note.

**6. Sweep every derived claim.**
Corrections to run data can invalidate claims in three places:
- `HANDOFF_WISDOM.md` -- cross-strain patterns, equipment observations,
  failure modes that cite the corrected run(s)
- `Dabby_Methodology.md` -- methodology positions that cite the corrected
  run(s)
- `StrainStatus` fields (`next_ai_analysis`, `next_text`) in the affected
  jar(s) -- recommendations built on the wrong data

For each: grep for the run citation (e.g. "WM R16", "bp4rw13 R5"), read
the surrounding context, and determine whether the claim still holds with
the corrected data. If not, revise the claim in the same pass. If a
cross-rig claim collapses because corrected runs are now all on one rig,
state that explicitly.

**7. Generate and verify.**
`python Dabby_Log_Generator.py` -- must complete clean.

**8. Ship.**
Single PR with all corrections, wisdom/methodology revisions, and
regenerated output. PR description: plain English stating what was
corrected, the error mechanism, how many runs were affected, and what
derived claims were revised.

If this session already has an open PR, push to that branch instead of
opening another.

## Recovery paths (don't improvise these)

- **User disagrees with the proposed correction** -- stop. The user was
  there; the AI was not. Do not override.
- **Correction changes rendered output unexpectedly** -- review the
  `index.html` diff after generating. Equipment changes should only affect
  the Equipment line in the run section; date changes affect the section
  title.
- **A derived claim in HANDOFF_WISDOM.md cites many runs, only some
  corrected** -- revise only the parts that depended on the corrected
  data. Do not rewrite the entire claim.

## Provenance and maintenance

Created 2026-07-04. The procedure is modeled on PR #206 (July 2, 2026).
Verify these still hold if this skill starts giving results that don't
match reality:

```
# By-exception correction note convention (step 5):
grep -rn "corrected.*202[0-9]" jars/*.py | head -10

# The frozen-analysis rule this skill is the exception to:
grep -n "correctable by exception" Dabby_Handoff_Notes.md
grep -n "correctable by exception" CLAUDE.md

# PR #206 as the worked example (confirm it exists):
# Use GitHub MCP pull_request_read, owner: ronniejamesewu, repo: dabby, pr: 206

# The sweep targets (step 6):
grep -n "Cross-Strain Patterns\|Equipment Observations\|Methodology State" HANDOFF_WISDOM.md | head -5

# Other skills this one cross-references:
ls .claude/skills/
```

Dogfood-test status: **Not yet tested.**
