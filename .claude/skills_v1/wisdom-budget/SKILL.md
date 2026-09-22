---
name: wisdom-budget
description: Trigger when the generator prints a WISDOM WARNING line for the brief soft-cap, the full-block LIVE entry count, or a per-entry-file size, or when the user asks to compress, trim, split, shrink, or free up room in the wisdom layer, the brief, or a specific wisdom entry, or asks how close the wisdom layer is to any of its budget thresholds.
---

# Wisdom-Layer Budget

Routes the wisdom layer's three generator-emitted budget warnings to their designed
response: enumerate compression/merge/split candidates, propose tier moves or entry-file
splits with drafted `resolution` one-liners, user triage, apply, regenerate, verify the
number actually moved under budget. Origin: `BACKLOG.md`'s `wisdom-budget` item (Session
165, July 16, 2026) — the three warnings printed with no routed response, and
threshold-triggered judgment has already failed to fire twice on this project
(Sessions 145, 151; see `Dabby_Handoff_Notes.md` Known Claude Failure Modes). This skill
is the mechanization; it does not replace the judgment of what to compress.

This is a sibling of `wisdom-audit`, not a substitute for it. `wisdom-audit` asks "is
this entry still true against the primary data." This skill asks "is the brief or an
entry file over its size budget, and if so, which lever brings it back under." A budget
pass never changes what an entry claims — it only changes how much of the brief a
settled or oversized entry occupies.

## Terms

| Term | Meaning |
|---|---|
| Wisdom layer | `wisdom/entries/<key>.py` files, the `LIVE`/`COMPRESSED` tier lists in `wisdom/manifest.py`, and the generated `WISDOM_BRIEF.md` that renders them |
| Brief soft cap | `BRIEF_SOFT_CAP` in `wisdom_core.py` (36,000 chars) — the generator warns above this. Distinct from `BRIEF_HARD_CAP` (40,000), which errors the build; this skill responds to the warning, well before the hard cap is reached |
| Full-block LIVE count | `FULL_BLOCK_LIVE_WARN` (40) — the count of `LIVE` entries rendered as full blocks in the brief: pattern / equipment / failure-mode / theory kinds. `decision`-kind entries render as one-liners and are excluded from this count and from this skill's candidate search |
| Per-entry-file cap | `ENTRY_FILE_WARN` (20,000 bytes), enforced in `wisdom/manifest.py`'s preflight — the byte size of one `wisdom/entries/<key>.py` file |
| Tier move | Relocating a key between `LIVE` and `COMPRESSED` in `wisdom/manifest.py`. The entry file itself is not touched by the move alone — a move to `COMPRESSED` additionally requires setting that entry's `resolution` field |
| Resolution one-liner | The `resolution` field on `WisdomEntry` (<=200 chars, required non-empty for any `COMPRESSED`-tier entry) — the sentence the brief renders in its Compressed section in place of the full block |
| Distill | Compressing an entry's brief-facing surface into a shorter form that says nothing the entry file doesn't already establish — no new claim, no stronger grade, no resolved question |
| Split | Retiring an oversized entry file into two or more new-keyed files, each carrying a lineage note in prose pointing back to the original key. Keys are never renamed or reused; a split always creates new keys |
| Compact-to-git | Removing a fully-superseded `Position`'s text from an entry file's live prose (git already preserves it in history) and replacing it with a short pointer note in the entry |
| Valve | Which lever — tier move/merge, split, or compact-to-git — actually reduces the specific metric that is over budget. The three warnings do not share a valve; picking the wrong one for a given warning does nothing |
| Clean-context adversarial review | A fresh agent, no memory of the drafting session, that attacks every proposed resolution/split/compaction against the entry file's own text before the user sees it — the same mechanism as `wisdom-audit` step 6 |

**Two registers.** Never surface to the user: entry keys (`curve-design-theory`), field
names (`resolution`, `updated`, `grade_basis`), slugs, `RIG_N`, tier-list names (`LIVE`,
`COMPRESSED`), or phase/step labels. The user sees: plain-English findings ("the curve
design note," "the endpoint theory entry"), strain names, rig display names, and what a
proposed change would say and why.

## Hard rules

- **This skill proposes; the user disposes.** No entry changes tier and no `resolution`,
  split, or compaction is written until the user approves it, item by item. Same hard
  rule as `wisdom-audit`.
- **Distill, never upgrade.** A `resolution` one-liner (or a split's lineage note, or a
  compaction's pointer note) may not strengthen a claim, promote a grade, resolve an open
  question, or add specificity the entry file does not already carry. If a draft can't be
  traced word-for-word back to the entry's own `claim`/`guidance`/`positions`, it isn't a
  distillation — rewrite it or flag the candidate instead of forcing one. The entry file
  keeps everything; compression is about the *brief*, not the record.
- **Mandatory clean-context adversarial review before anything merges.** Every proposed
  resolution one-liner, split, and compact-to-git pointer goes through a fresh-context
  review pass (mirrors `wisdom-audit` step 6) before the user sees the final proposal.
  This is not ceremonial — compression drift tracks the author's own working narrative in
  either direction and self-review misses it at any model scale. Three logged instances on
  this project: Session 146 (four confounds silently dropped from a condense pass), the
  July 11, 2026 audit (its own first-draft proposal committed milder versions of the same
  failure class), and the July 15, 2026 migration (fabricated specifics in transposed
  entries, caught only by comparison against ground truth). See `Dabby_Handoff_Notes.md`
  Known Claude Failure Modes for the full record of all three.
- **Never fill a silence.** Same rule as the brief's session-close checklist footer: when
  the entry is silent on a date, session, or reason, write `undated in source`,
  `none noted`, "provenance untagged" — never a plausible fill, even inside a one-liner
  that is otherwise obviously safe.
- **Never hand-edit `WISDOM_BRIEF.md`.** It is overwritten on the next generate. If a
  number still looks wrong after a generate, the fix is in an entry file or the manifest,
  never in the brief.
- **Match the valve to the warning — the three do not share one.** The brief soft-cap and
  the full-block LIVE count both respond to the same valve (tier move `LIVE`→`COMPRESSED`,
  or merging two overlapping entries into one survivor and compressing the redundant key).
  The per-entry-file cap is a different valve entirely (split or compact-to-git) and is
  usually not fixed by a tier move — an oversized entry doesn't get smaller by being
  marked `COMPRESSED`; it still has to render a `resolution`, but the file itself, and its
  byte count, sit untouched by a tier move.
- **The three budgets are coupled — a split can trip the other two.** Splitting an
  oversized entry (the per-entry-file valve) replaces one full-block LIVE entry with two
  or more, which *raises* the full-block LIVE count and *grows* the brief. When the
  full-block count or the brief size is already near its own warn threshold, a split fixes
  the file cap by tripping one or both of the others. Before proposing a split, check the
  current full-block LIVE count and brief size (step 2's generator run prints both) and
  compute where the split lands them. If it would breach another budget, the split must be
  paired with a compression elsewhere (a tier move or merge that vacates the room the new
  keys will occupy) in the *same* proposal — never shipped as a fix that silently relights
  a different warning. The valves are independent in which metric they *reduce*; they are
  not independent in what they *cost*.
- **A merge that would also promote a grade is not a budget compression.** If folding two
  entries into one survivor would newly satisfy a grade threshold (e.g. the `tested`
  cross-jar floor), that is a grade promotion under the wisdom-audit promotion gate — it
  needs a `counter_reading` and belongs to a `wisdom-audit`-style change, not a budget
  merge. Flag it and stop; do not let a size fix double as an uncontested grade bump.
- **Verify with an unpiped generator run and an explicit exit-code check.** Never pipe the
  generator's output through `tail`, `grep`, or any other filter when checking whether a
  fix worked — a failing validation can look green to a shell chain keyed on the pipe's
  last command (`fm-piped-exit-code-masking`, Session 165 — a broken state shipped this
  way once already). Run it unpiped and check the exit status as its own step.

## When NOT to use

- **A wisdom entry's claim or grade needs re-checking against the primary jar data** —
  that's `wisdom-audit`, not this skill. This skill never re-derives whether a claim still
  holds; it only asks whether the brief or a file is over its size budget.
- **A specific frozen run field is wrong** — that's `correct-frozen-data`.
- **The baseline curve should change** — that's `change-baseline`.
- **Nothing is over budget and the user isn't asking about it** — there is nothing to do.
  Do not run a speculative compression pass just because the brief has grown since the
  last check; wait for the warning or the user's ask.

## Workflow

**1. Session-start gate first.** If this is a fresh session, complete the CLAUDE.md gate
(git sync; read `WISDOM_BRIEF.md` + `Dabby_Handoff_Notes.md`, and `HANDOFF_STATE.md` once
run/jar/state work begins) before anything else.

**2. Establish which warning(s) are actually firing, unpiped.** Run the generator directly
and read its output yourself — do not pipe it:

```
# bash
python3 Dabby_Log_Generator.py; echo "exit: $?"

# PowerShell
python Dabby_Log_Generator.py; Write-Host "exit: $LASTEXITCODE"
```

Read every `WISDOM WARNING:` line printed. Confirm the exit code is 0 — the three budget
warnings alone do not fail the build (only the 40,000-char hard cap does); a nonzero exit
means something else is also wrong and needs fixing first, separately from this skill.

**3. Enumerate candidates, per warning family.**

*Brief soft-cap and full-block LIVE count (same valve — tier move or merge).* Read
`wisdom/manifest.py`'s `LIVE` list. For every entry whose kind is not `decision`, read the
entry file (`wisdom/entries/<key>.py`) and look for:
- A stale `updated` field with no new citations or positions in a long time, whose claim
  now reads as settled with nothing live left to watch (`watch_for` empty or clearly
  resolved).
- Two or more `LIVE` entries whose `claim` fields cover overlapping ground — a merge
  candidate. Merging means one entry (the survivor) absorbs the retiring entry's citations
  into its own evidence/positions in prose, and the retiring key moves to `COMPRESSED`
  with a `resolution` pointing (in the entry file only — never in the brief-facing
  wording) to the survivor.
- A `tested`-grade pattern or theory with no open `watch_for` and no counter-evidence
  added in many sessions — a compression candidate, not a grade change.

*Per-entry-file cap (different valve — split or compact-to-git).* Read the flagged file in
full — for the current standing case this is `wisdom/entries/curve-design-theory.py`
(26,631 bytes against the 20,000-byte warn). Decide between the two valves the warning
text itself names:
- **Split** if the entry actually holds two or more separable claims bundled under one
  key. No decision speaks to this entry specifically, and no split has been executed on
  this project — there is no precedent to copy. `wisdom/design/DECISIONS.md` decision 8
  is the nearest reasoning by analogy (it kept `tail-harshness-mechanism` as one entry on
  the grounds that competing answers to *one* question are not separate questions) — read
  it for the test to apply, not as a ruling about this entry. Apply that test here: are
  the bundled claims answers to one question, or genuinely separate questions? A split
  creates new keys, each with a lineage note in prose pointing back to the retiring key;
  the old key does not get reused.
- **Compact-to-git** if the bulk of the size is `Position` entries whose `status` is
  `superseded` and whose content has no forward value beyond the `superseded_note` already
  summarizing why. Compacting removes the superseded position's full paragraph from the
  live file and replaces it with a short pointer (the text is already in git history via
  normal commits — nothing new needs preserving).

**4. Draft each candidate's change before showing anyone.**
- Tier move: the retiring key, and a `resolution` (<=200 chars) built only from words and
  facts already in that entry's `claim`/`guidance`/`positions`. Trace every clause back to
  source before it's considered a draft.
- Merge: which entry survives, what moves into its evidence/positions, and the retiring
  entry's `resolution` pointing at the survivor's *content* in plain English (not its
  key). Check whether the merged survivor's own file size stays under the per-entry-file
  cap — a merge that fixes one warning by tripping another is not a fix, and is worth
  flagging explicitly if it happens.
- Split: the new key names, a one-paragraph description of what content moves to each,
  and the lineage-note wording for each new file plus the old key's retirement note.
- Compact-to-git: exactly which `Position` paragraph(s) are being removed and the
  replacement pointer text.

**5. Clean-context adversarial review.** Spawn a fresh agent (`model: fable` while
available, else `opus`) with the full draft proposal and read access to every entry file
it touches. Brief it to attack: does every resolution one-liner distill rather than
strengthen; does a split cleanly partition the source without orphaning a citation or
confound; does a compact-to-git pointer actually correspond to real, findable git history;
is any silence being filled with a plausible-sounding fact the source doesn't state.
Reconcile every finding into the proposal before the user sees it, and mark what changed
as a result.

**6. Present for triage.** Show the proposal in plain English, one item at a time, two
registers respected — what would change, why, and what it would say once compressed. The
user approves or rejects each item independently; a partial approval is a normal outcome
(apply only what's approved, leave the rest, and the corresponding warning may persist
until a later pass finds a better candidate).

**7. Apply only the approved items.**
- Tier move: move the key in `wisdom/manifest.py` (`LIVE` list to `COMPRESSED` list, or
  vice versa for a reversal) and set `resolution` in `wisdom/entries/<key>.py`. Nothing
  else in the entry file changes.
- Merge: edit the survivor's entry file to fold in the retiring entry's evidence/positions
  in prose, move the retiring key to `COMPRESSED` in the manifest, and set its
  `resolution`.
- Split: create the new `wisdom/entries/<new-key>.py` files with lineage notes, add the
  new keys to `wisdom/manifest.py` in place of the old key, and either retire the old key
  to `COMPRESSED` with a `resolution` pointing to the new keys, or remove it entirely if
  every citation has moved — resolve this specific mechanic against
  `wisdom/design/DECISIONS.md` and the manifest's orphan-file check before deciding, since
  this project has not executed a split yet and there is no precedent run to copy.
- Compact-to-git: edit the entry file's prose only, stripping the superseded position's
  full paragraph and inserting the pointer note.

**8. Regenerate and verify the number actually moved, unpiped.** Run the same unpiped
command as step 2 again. Confirm the exit code is 0, and — critically — confirm the
specific metric that was over budget now reads under it: re-check `WISDOM_BRIEF.md`'s
char count, recount full-block `LIVE` entries, or re-check the flagged file's byte size,
whichever warning this pass targeted. The absence of a printed warning is not sufficient
on its own if the run was piped anywhere upstream of your own read of it — read the
console output directly.

**9. Ship.** Feature branch, commit, PR with a plain-English description (no field names,
keys, or tier-list names) describing what was trimmed and why it doesn't lose anything —
mirror the PR Workflow section of `CLAUDE.md`. If a `LIVE` entry's `resolution` also
happens to close an open `BACKLOG.md` item (e.g. the standing `curve-design-theory`
per-file item), note that in the PR and offer the session-close checklist's Q6.

## Recovery paths (don't improvise these)

- **The generator still warns after applying approved changes** — the valve chosen didn't
  move the needle enough. Return to step 3, pick the next candidate, and apply it. Never
  hand-edit `WISDOM_BRIEF.md` to make the number look right; it is overwritten on the next
  generate regardless.
- **The adversarial reviewer flags a resolution as strengthened, or a compaction as
  dropping a confound** — rewrite it from the entry's own words; do not defend the
  original wording. Re-check whether the same drift class appears in any other item in
  the same proposal (errors of this kind travel in families, per the Session 146 record).
- **No believable compression candidate exists for a warning that's firing** — say so to
  the user rather than manufacturing one. Same shape as `wisdom-audit`'s
  no-counter-reading rule: a forced compression is worse than an unresolved warning.
- **The tree looks clean but you ran the generator through a pipe to get there** — that
  is not verification. Rerun unpiped, per step 8, and check the exit code explicitly
  before trusting either the presence or the absence of a warning.
- **A merge candidate's survivor would cross the per-entry-file cap** — don't apply the
  merge as drafted. Either trim what moves into the survivor, or treat it as two separate
  compression passes (tier-move valve first, entry-file valve later) rather than one.

## Provenance and maintenance

Created July 16, 2026, from the `wisdom-budget` item in `BACKLOG.md` (Session 165, with
the entry-file scope sharpened by the July 15, 2026 migration and the Session 167 backlog
note on `curve-design-theory`). Verify these still hold if this skill starts giving
results that don't match reality:

```
# current LIVE/COMPRESSED tier sizes:
python3 -c "from wisdom.manifest import LIVE, COMPRESSED; print(len(LIVE), len(COMPRESSED))"

# current brief size and full-block LIVE count (also re-validates everything else):
python3 Dabby_Log_Generator.py; echo "exit: $?"
wc -c WISDOM_BRIEF.md

# heaviest entry files, to find the next per-file-cap candidate:
wc -c wisdom/entries/*.py | sort -n | tail -5

# the three warn/error constants, if this skill's numbers ever look stale:
python3 -c "from wisdom_core import BRIEF_SOFT_CAP, BRIEF_HARD_CAP, FULL_BLOCK_LIVE_WARN, ENTRY_FILE_WARN; print(BRIEF_SOFT_CAP, BRIEF_HARD_CAP, FULL_BLOCK_LIVE_WARN, ENTRY_FILE_WARN)"
```

Dogfood-test status: **Not yet tested.** The first real test case is the standing
per-entry-file warning on `curve-design-theory.py` (26,631 bytes against the 20,000-byte
warn as of July 16, 2026) — see its own `BACKLOG.md` item.
