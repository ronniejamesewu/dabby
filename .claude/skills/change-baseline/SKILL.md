---
name: change-baseline
description: Change the BASELINE_CURVE starting-point recommendation in Dabby_Core.py. This is a multi-step protocol -- freeze the retiring curve under a named constant, migrate all run-level references, redefine BASELINE_CURVE, and update Dabby_Methodology.md. Trigger when accumulated evidence across strains suggests a different starting curve would serve new jars better. Phrases -- "the baseline should change", "new starting point", "update the baseline", "baseline is now X". This is a rare, high-impact operation -- most sessions never need it.
---

# Change Baseline

Changes the `BASELINE_CURVE` starting-point recommendation. This is a
rare, high-impact operation -- the baseline has changed once in project
history (commit d5ab834, from 380-390-410-430 to 380-400-416). The
5-step protocol is codified from the "Changing BASELINE_CURVE without
renaming the retiring constant" failure-mode row in `HANDOFF_WISDOM.md`.

The preflight ban in `jar_manifest.py` catches any `waypoints=BASELINE_CURVE`
inside RUNS that slips through -- but the protocol here prevents the
situation from arising.

## Terms

| Term | Meaning |
|---|---|
| `BASELINE_CURVE` | The current recommended starting-point curve for new strains. Lives in `Dabby_Core.py`. Mutable -- its definition changes when the recommendation changes. |
| Frozen constant | A named alias (`BASELINE_416`, `BASELINE_420`) that pins a specific set of waypoints permanently. Historical runs reference these, not `BASELINE_CURVE`, so they're immune to future baseline changes. |
| Run-level reference | `waypoints=BASELINE_CURVE` inside a `CompletedRun` in RUNS. These must be migrated to the frozen constant before `BASELINE_CURVE` is redefined. |
| STATUS-level reference | `next_waypoints=BASELINE_CURVE` inside a `StrainStatus`. These correctly point at the current recommendation and must NOT be changed -- they should track the new baseline. |
| Preflight ban | The check in `jar_manifest.py` `_validate_manifest_preflight()` that rejects `waypoints=BASELINE_CURVE` inside RUNS. Catches any migration miss at generate time. |

**Two registers.** `BASELINE_CURVE`, `BASELINE_416`, `BASELINE_420`,
`waypoints=`, `next_waypoints=`, constant names, and this file's step
names are machine-side vocabulary -- they never appear in a reply to the
user. The user sees curve descriptions as temperatures-and-shape prose
or `fmt_curve_table()` tables.

## Hard rules

- **Name by endpoint temperature, not equipment era.** The retiring
  constant is named `BASELINE_XXX` where XXX is the endpoint temperature
  (e.g. `BASELINE_416`, `BASELINE_420`). Equipment names break when the
  baseline changes without an equipment change.
- **Never replace_all on the bare substring `waypoints=BASELINE_CURVE`.**
  It matches inside `next_waypoints=BASELINE_CURVE` (STATUS kwargs) and
  would wrongly pin What to Try Next guidance to the retired curve.
  Always use the field-anchored grep: `waypoints=BASELINE_CURVE,` at the
  start of the kwarg, inside RUNS only.
- **STATUS-level `next_waypoints=BASELINE_CURVE` is correct and must not
  be changed.** It should track whatever the new baseline is.

## When NOT to use

- **Logging a run** -- that's the log-run skill. If a run happens to use
  the baseline curve, the log-run skill assigns the appropriate frozen
  constant (currently `BASELINE_420`).
- **Creating a new jar** -- the new-jar skill sets
  `next_waypoints=BASELINE_CURVE` for new jars, which is correct.
- **A single strain needs a different curve** -- that's a per-strain
  adjustment in `StrainStatus.next_waypoints`, not a baseline change.
  The baseline changes only when accumulated cross-strain evidence
  suggests a different universal starting point.

## Workflow

**0. Present the plan and wait for approval.**
Before editing anything: run the step 2 grep read-only to count the
run-level references, then present the full plan -- the retiring constant
name, the migration count, the proposed new curve, and the methodology
edit -- and wait for explicit approval. This skill's trigger can be
AI-recognized ("accumulated evidence suggests..."), and editing core plus
multiple jar files is a substantive action under this project's
confirm-before-acting rule. Once approved, steps 1-5 are mechanical and
need no further per-step confirmation.

**1. Define the retiring constant.**
In `Dabby_Core.py`, create a new constant named by the current
`BASELINE_CURVE`'s endpoint temperature (e.g. if the current baseline
ends at 420, the constant is `BASELINE_420`). Place it in the DATA
section after the existing frozen constants and before `BASELINE_CURVE`.
Copy the current `BASELINE_CURVE` waypoints exactly.

If the retiring constant already exists (someone anticipated this),
verify its waypoints match the current `BASELINE_CURVE` exactly. If
they don't, stop -- something is wrong.

**2. Migrate all run-level references.**
Find all run-level references with the field-anchored grep:

```
grep -n 'waypoints=BASELINE_CURVE' jars/*.py
```

For each match:
- If the line starts with `waypoints=` (or is inside a `CompletedRun`
  constructor in the RUNS list), change `BASELINE_CURVE` to the retiring
  frozen constant name
- If the line starts with `next_waypoints=` (inside a `StrainStatus`
  constructor), do NOT change it -- it should track the new baseline

The discriminator is the field name prefix, not the trailing comma.
After migration, verify zero run-level references remain:

```
grep -n 'waypoints=BASELINE_CURVE' jars/*.py
```

All remaining matches should be `next_waypoints=` lines only. The
preflight ban in `jar_manifest.py` will also catch any misses at
generate time.

**3. Redefine `BASELINE_CURVE`.**
In `Dabby_Core.py`, replace the `BASELINE_CURVE` waypoints with the new
recommended starting curve. Present the proposed new curve to the user
for confirmation before writing.

**4. Update `Dabby_Methodology.md` and sweep the skills.**
Update the Section 5 curve table to reflect the new baseline. Read the
current table first to understand its format.

Then sweep `.claude/skills/` for copies of the retiring baseline: grep
for the old endpoint temperature and the retiring constant's name (e.g.
`grep -rn "420°F @8s\|BASELINE_420" .claude/skills/`) and update any hit
-- log-run's step 6 names the current frozen constant, and other skills
may reference the current curve. A skill carrying the retired baseline
is a wrong runbook.

**5. Generate, verify, and ship.**
Run `python Dabby_Log_Generator.py` -- must complete clean.

Verify with `git diff main -- index.html`: the rendered output should
show no changes for historical runs (they now reference the frozen
constant, which has identical waypoints). Only the "What to Try Next"
sections for jars using `next_waypoints=BASELINE_CURVE` should reflect
the new curve.

Ship as a single PR. PR description: plain English stating what the old
baseline was, what the new one is, the evidence behind the change, and
how many run-level references were migrated.

## Recovery paths (don't improvise these)

- **Preflight ban fires after step 3** -- a run-level reference was
  missed in step 2. Find it with the grep in step 2 and migrate it.
- **Rendered output shows historical run changes** -- the migration in
  step 2 was incomplete or incorrect. A historical run's waypoints
  should point to the frozen constant, not `BASELINE_CURVE`.
- **The retiring constant already exists with different waypoints** --
  stop. This means `BASELINE_CURVE` was changed without following this
  protocol. Investigate the discrepancy before proceeding.

## Provenance and maintenance

Created 2026-07-04. Codified from the "Changing BASELINE_CURVE without
renaming the retiring constant" failure-mode row in `HANDOFF_WISDOM.md`
and the migration completed July 4, 2026 (`BASELINE_420` frozen, 10
run-level references migrated across 5 jars, preflight ban added to
`jar_manifest.py`).

Verify these still hold if this skill starts giving results that don't
match reality:

```
# Current frozen constants (step 1):
grep -n "^BASELINE_" Dabby_Core.py

# Current BASELINE_CURVE definition (step 3):
grep -n -A4 "^BASELINE_CURVE" Dabby_Core.py

# Run-level vs STATUS-level references (step 2):
grep -rn "waypoints=BASELINE_CURVE" jars/*.py

# Preflight ban (step 2 verification):
grep -n "BASELINE_CURVE" jar_manifest.py

# Methodology table (step 4):
grep -n "Section 5\|Baseline" Dabby_Methodology.md | head -5

# Other skills this one cross-references:
ls .claude/skills/
```

Dogfood-test status: **Partially tested.** The migration half of this
protocol (steps 1-2) was executed July 4, 2026 (this session). The
full end-to-end workflow (including steps 3-5 with an actual baseline
change) has not been tested.
