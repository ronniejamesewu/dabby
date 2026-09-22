---
name: close-jar
description: Close a finished jar in this Dabby project -- the two-file edit (move slug from ACTIVE to CLOSED in jar_manifest.py, update the jar file's STATUS prose to closed-jar framing) plus the Jar-Done Commemoration (Harper's Index + standup set). Trigger when the user says the jar is done, the material is finished, or the last run has been logged and they confirm closure. Phrases -- "jar's done", "that was the last one", "finished the jar", "close it out", "closing [strain]". Also trigger when another skill or conversation establishes that a jar has no material remaining and the user confirms closure. This skill closes jars only -- it does not log runs (that's log-run) or create jars (that's new-jar).
---

# Close Jar

Closes a finished jar: moves the slug between tiers in the manifest,
rewrites the STATUS prose to closed-jar framing, and produces the Jar-Done
Commemoration works. The jar file's run data and profile are permanent
record and are never touched by this skill.

## Terms

| Term | Meaning |
|---|---|
| Jar | One `jars/<slug>.py` file per strain, holding its profile (`STATUS`) and logged sessions (`RUNS`). |
| Slug | The filename-safe identifier for a jar (e.g. `wwz`, `fw106`) -- used as the Python module name and the manifest key. Never shown to the user. |
| Tier | `ACTIVE` (material remaining) or `CLOSED` (jar done). Lists in `jar_manifest.py`. |
| `_check_closed_tier()` | Validator in `jar_manifest.py` that rejects a closed jar's `next_text`/`next_ai_analysis` if they reference a run number beyond the jar's completed count -- catches forward-looking language in a closed jar. |
| Harper's Index | The jar's story told in Harper's Index style, written to `STATUS.jar_index`. |

**Two registers.** Slugs, field names, `RIG_N` constants, step numbers, and
`_check_closed_tier` are machine-side vocabulary -- they never appear in a
reply to the user. The user sees full strain names, "Rig N -- ..." display
expansions, and outcome language.

## Hard rules

- **The user decides closure.** A run being the last one is not automatic
  closure -- the user must explicitly confirm the jar is done.
- **The final run must already be logged.** If the user is reporting both
  the last dab and closure in one message, log the run first (log-run
  skill), then return here.
- **Never touch RUNS.** This skill edits STATUS fields and the manifest
  only. Run data is permanent record.

## When NOT to use

- **Opening a new jar** -- that's the new-jar skill
  (`.claude/skills/new-jar/SKILL.md`).
- **Logging a run** -- that's the log-run skill
  (`.claude/skills/log-run/SKILL.md`). Even the final run of a jar is
  logged via log-run first, then this skill handles closure.
- **Correcting data in a closed jar** -- that's the correct-frozen-data
  skill (`.claude/skills/correct-frozen-data/SKILL.md`). Closed jars are
  permanent record; corrections follow that skill's by-exception procedure.

## Workflow

**1. Confirm closure with the user.**
If not already explicit, ask: "Is that the last of the [full strain name]
-- closing the jar?" Do not proceed without a yes.

**2. Verify the final run is already logged.**
Read `jars/<slug>.py` and confirm the last `CompletedRun` in `RUNS` matches
what the user described as the final session. If the final run hasn't been
logged yet, invoke the log-run skill first and return here after.

**3. Update STATUS prose to closed-jar framing.**
Edit `jars/<slug>.py` -- the `STATUS = StrainStatus(...)` block. Four
fields change:

- `next_text`: Closed-jar framing. Convention (own-jar form from
  `jars/wwz.py`; guest form from `jars/fembot3.py` and `jars/ms23.py` --
  note `jars/mb9zst.py` predates the recommendation clause and matches
  neither template, don't copy it):
  - User's own jar: `'Jar done -- N runs. If it shows up again: [one-
    sentence starting point recommendation]'`
  - Guest jar: `'Not my jar -- closed after N runs. If it shows up again:
    [recommendation].'`
  Never "on the next jar" -- per Decisions in `Dabby_Handoff_Notes.md`,
  most strains won't reappear.

- `next_dab_notes`: Summarize the final run's user observations and
  jar-closing context. One or two sentences.

- `next_ai_analysis`: Closed-jar voice. Jar summary (equipment config and
  endpoint that worked), the "if this strain shows up again" recommendation
  with brief reasoning. Strip any forward-looking experimental framing
  ("Run N+1 should test..."). 3-4 sentences max.

- `next_waypoints`: Set to `None`. A closed jar has no planned next curve.

**Do not touch** `RUNS`, `info`, `terpene_note`, `accent`, `name`, `slug`,
`profile_anchor`, or `jar_index` (jar_index is written in step 5a, not
here).

Draft all four fields in chat and get the user's approval before editing
the file -- the same gate as log-run's analysis drafts. Step 1's closure
confirmation approved *closing the jar*, not this prose; the
recommendation in `next_ai_analysis` is substantive AI judgment, not a
mechanical reframe.

**4. Move the slug in `jar_manifest.py`.**
Read `jar_manifest.py` first to find the current list positions. Remove
the slug's line (including the inline name comment) from the `ACTIVE` list
and append it to the end of the `CLOSED` list, preserving the inline
comment convention: `'slug',  # Full Strain Name`.

**5. Jar-Done Commemoration.**
Two works, generated after steps 3-4. Both require the full run history
(read the entire jar file) and the voice defined in
`Dabby_Handoff_Notes.md` Voice & Role.

**5a. Harper's Index.**
The jar's story told in Harper's Index style. Can draw from data across
the full project (other jars, wisdom layer) so long as it serves this
jar's thread. Before writing, read the `jar_index` field in `jars/wwz.py`
and `jars/mb9zst.py` as examples of the format and register. Write to
`STATUS.jar_index` in `jars/<slug>.py`. The format is an HTML `<div>` with
`<strong>` labels and `<br>` separators -- match the existing pattern
exactly. Use single-quote HTML attributes (`style='...'`) to avoid the
Edit-tool curly-quote contamination hazard. Present the draft to the user
for approval before writing.

**5b. Standup set.**
A tight 4-minute set in the project voice, riffing on the jar's full run
history. Find the single strongest theme -- what this jar was actually
about -- and build everything around it. Don't retell chronologically.
Don't riff on premises the user taught you as if you discovered them.
**Conversation only -- not persisted.** Present it, the user reacts,
move on.

**6. Generate and verify.**
Run `python Dabby_Log_Generator.py`. Must complete with no VALIDATION
ERRORS, MANIFEST ERRORS, or TIER ERRORS. TIER ERRORS from
`_check_closed_tier()` mean the `next_text` or `next_ai_analysis` still
contains forward-looking run references -- fix the prose in step 3.

**7. Ship.**
Feature branch, commit the jar file + `jar_manifest.py` + regenerated
`index.html` + `HANDOFF_STATE.md`. PR via GitHub MCP `create_pull_request`
(the `gh` CLI is not installed). Plain-English description, e.g.: "Closed
the [strain] jar after N runs. [one sentence on the recommendation carried
forward]."

If this session already has an open PR, push to that branch instead of
opening another.

## Recovery paths (don't improvise these)

- **TIER ERRORS on generate** -- the `next_text` or `next_ai_analysis`
  references a run beyond the jar's count. Fix the forward-looking language
  in the STATUS block and rerun.
- **Edit-tool curly-quote contamination in jar_index HTML** -- the manifest
  preflight rejects the backslash+curly signature. Fix by byte position
  with a Python script, not the Edit tool.

## Provenance and maintenance

Created 2026-07-04. Verify these still hold if this skill starts giving
results that don't match reality:

```
# Closed-jar prose examples (step 3 -- own-jar and guest forms):
grep -n "next_text\|next_ai_analysis\|next_waypoints" jars/wwz.py | tail -5
grep -n "next_text\|next_ai_analysis\|next_waypoints" jars/fembot3.py | tail -5
grep -n "next_text\|next_ai_analysis\|next_waypoints" jars/ms23.py | tail -5

# The _check_closed_tier validator (step 6):
grep -n "_check_closed_tier" jar_manifest.py

# Harper's Index examples (step 5a):
grep -n "jar_index" jars/wwz.py
grep -n "jar_index" jars/mb9zst.py

# Manifest tier lists location (step 4):
grep -n "^ACTIVE\|^CLOSED" jar_manifest.py

# Inline name comment convention (step 4):
head -35 jar_manifest.py

# Jar-Done Commemoration spec (step 5):
grep -n "Jar-Done Commemoration" Dabby_Handoff_Notes.md

# Voice & Role (step 5b):
grep -n "Voice & Role" Dabby_Handoff_Notes.md

# Other skills this one cross-references:
ls .claude/skills/
```

Dogfood-test status: **Not yet tested.**
