---
name: new-rig
description: Create a new RIG_N equipment constant in Dabby_Core.py when the user's reported equipment doesn't match any existing rig. Trigger when dab notes mention equipment changes ("new glass top", "tried the sapphire", "swapped pearl", "no pearl today") and the resulting combination doesn't match an existing RIG_N. Also trigger when the log-run skill's equipment-change detection (Beat 1) identifies a novel equipment config. This skill creates the constant only -- the run is logged afterward by the log-run skill using the new constant.
---

# New Rig

Creates a new `RIG_N` equipment constant in `Dabby_Core.py` when the
user's reported equipment doesn't match any existing rig. The protocol
is from `Dabby_Handoff_Notes.md` (the "New rig creation" block under
Equipment Protocol), mechanized here.

Adding a new `RIG_N` constant requires no edits to the generator or
display helpers -- `_RIG_LABELS` in `Dabby_Core.py` auto-discovers all
`RIG_N` globals at import time (the Session 75 failure mode stays
structurally impossible).

## Terms

| Term | Meaning |
|---|---|
| `RIG_N` | A shared equipment constant in `Dabby_Core.py`. Each is an `EquipmentConfig` with four fields: `insert`, `carb_cap`, `pearls`, `glass_top`. Sequence number N is monotonically increasing. |
| `EquipmentConfig` | Dataclass in `Dabby_Core.py` with nested `Insert`, `CarbCap`, `Pearl` dataclasses and a `glass_top` string. |
| `_RIG_LABELS` | Auto-discovery dict in `Dabby_Core.py` that finds all `RIG_N` globals at import. Adding a new constant is the only step needed -- no edits to this or the display helpers. |
| Four fields | `insert` (brand, model, material), `carb_cap` (brand, model, airflow), `pearls` (list of Pearl with diameter_mm and material), `glass_top` (string). |

**Two registers.** `RIG_N`, `EquipmentConfig`, `Insert`, `CarbCap`,
`Pearl`, `_RIG_LABELS`, and this file's step names are machine-side
vocabulary -- they never appear in a reply to the user. The user sees
"Rig N" with the full expansion (e.g. "Rig 3 -- sapphire (Dr. Dabber
Sapphire Plus v2) . Cloud Vortex 21.0 spinner . 6mm quartz pearl .
stock Dr. Dabber bubbler").

## Hard rules

- **The user confirms before any constant is written.** A `RIG_N` is a
  shared constant -- it lives in core, not in a jar file. Always present
  the proposed definition and get explicit approval.
- **Unchanged fields default from the prior run's equipment.** Only the
  changed component needs to be stated by the user; everything else
  carries forward.
- **Check for existing matches first.** If the resulting config matches
  an existing `RIG_N`, use that one -- don't create a duplicate.

## When NOT to use

- **Equipment hasn't changed** -- the user is on the same rig as last
  time. Just use the existing `RIG_N` in the run.
- **Logging a run** -- that's the log-run skill
  (`.claude/skills/log-run/SKILL.md`). This skill creates the constant;
  log-run uses it.
- **Correcting equipment on a historical run** -- that's the
  correct-frozen-data skill
  (`.claude/skills/correct-frozen-data/SKILL.md`). If the correction
  reveals a need for a new rig constant, come here first, then return
  to correct-frozen-data.

## Workflow

**1. Identify what changed.**
From the user's dab notes or explicit statement, determine which of the
four equipment fields changed compared to their most recent run's
equipment. For a run being logged now, the current rig is
`HANDOFF_STATE.md`'s "Most recent run" line. When invoked from the
log-run skill for a queue-backed or post-dated run, use the equipment
default log-run's step 2 already resolved (computed as of that entry's
timestamp) -- the "Most recent run" line reflects now, not then, and a
stale default is the exact mechanism that mislogged seven runs
(Session 140).

**2. Confirm all four fields.**
Present the proposed config to the user, showing all four fields.
Unchanged fields default from the prior run's equipment -- state this
explicitly: "Keeping [prior rig's insert/cap/pearls/glass] for the
unchanged fields."

Ask necessity-bounded clarifying questions for the changed component(s).
For example, if the user says "new glass top," ask brand and model. If
they say "tried the sapphire," confirm which sapphire insert (the
project has one specific model: Dr. Dabber Sapphire Plus v2).

**3. Check for an existing match.**
Read `Dabby_Core.py` and compare the proposed config against all existing
`RIG_N` constants. If an exact match exists, use that rig -- don't
create a duplicate. Report to the user: "That matches Rig N -- using
that."

**4. Propose the new constant.**
If no match exists, draft the new `RIG_N` constant with:
- The next sequence number (current highest + 1)
- A comment block above it following the existing pattern: insert
  description, carb cap description, pearl description, glass top,
  and date of first use
- The `EquipmentConfig(...)` definition with properly nested dataclasses

Present the full proposed definition to the user for approval.

**5. Write to `Dabby_Core.py`.**
After user approval, add the new constant to `Dabby_Core.py` in the
EQUIPMENT section, after the last existing `RIG_N`. Follow the existing
spacing convention (one blank line between constants, comment block
above the definition).

**6. Validate.**
Run `python Dabby_Log_Generator.py` to confirm the new constant is
auto-discovered by `_RIG_LABELS` and doesn't break anything. The
generator must complete clean.

**7. Ship as part of the run-logging PR.**
The new rig constant is committed alongside the run that first uses it
-- not as a separate PR. The log-run skill handles the rest of the
workflow from here.

If this session doesn't have a run to log (e.g. the user is
pre-registering equipment for a future session), commit on its own
feature branch and open a PR.

## Recovery paths (don't improvise these)

- **User is unsure about a field** -- use the prior run's value as
  default and state the assumption in the readback and the run's
  `analysis` (never write AI-authored text into `dab_notes` -- that
  field is the user's verbatim words only). Can be corrected later via
  correct-frozen-data if wrong.
- **The new constant breaks validation** -- check that the
  `EquipmentConfig` fields match the dataclass signatures in
  `Dabby_Core.py`. Common mistakes: `pearls` must be a list (even if
  empty: `pearls=[]`), `glass_top` is a plain string, and `airflow` on
  `CarbCap` is required — pass `airflow="stock"` explicitly unless a
  variant is known (the source comment says "stock by default" but there
  is no dataclass default; omitting it raises TypeError).
- **Duplicate detection missed a match** -- if a run is logged with a
  new `RIG_N` that turns out to duplicate an existing one, the duplicate
  constant can be removed and the run's equipment corrected via
  correct-frozen-data.

## Provenance and maintenance

Created 2026-07-04. Based on the 4-step "New rig creation" protocol
under Equipment Protocol in `Dabby_Handoff_Notes.md`.
Verify these still hold if this skill starts giving results that don't
match reality:

```
# Current RIG_N constants (step 3 -- check for matches):
grep -n "^RIG_" Dabby_Core.py

# Auto-discovery mechanism (step 6 -- no edits needed):
grep -n "_RIG_LABELS" Dabby_Core.py

# EquipmentConfig dataclass fields (step 4):
grep -n "class EquipmentConfig\|class Insert\|class CarbCap\|class Pearl" Dabby_Core.py

# Equipment section location (step 5):
grep -n "EQUIPMENT" Dabby_Core.py

# Other skills this one cross-references:
ls .claude/skills/
```

Dogfood-test status: **Not yet tested.**
