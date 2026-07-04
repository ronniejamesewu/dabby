---
name: log-run
description: Log a completed dab run into this Dabby project — the full pipeline from the user's report to a merged PR. Trigger when the user reports results of a dab ("that was intense, swabs were golden...", "ok here's how it went", "log it") or asks to log/record a run, including post-dated runs ("I dabbed twice yesterday"). Also trigger for reconciliation: when .pending_dabs.json holds party-mode captures waiting to be logged, or the generator's PENDING DABS tripwire fires. Covers the Beat 1/Beat 2 readback, drafting analysis for approval, writing the jar file, regenerating, and shipping the PR. A run is logged ONLY when the user initiates it — never from a captured timestamp, a planned next run, or a conversational mention alone.
---

# Log Run

The pipeline from "here's how it went" to a merged, rendered run. The protocol
content lives in `Dabby_Handoff_Notes.md` and `CLAUDE.md` — this skill is the
assembly order and the gates, not a copy of the rules. Where a step says
"apply the X rules", read that section live and apply it; don't work from
memory of it.

## Hard gates — read these before step 1

- **Only the user initiates logging.** A pending capture, a "What to Try
  Next" plan, or a strain mentioned in passing is never a reason to write a
  run. If results haven't been reported and logging hasn't been asked for,
  there is nothing to do here.
- **`next_*` fields are advisory.** The user deviating from the planned run is
  correct and appropriate — treat the deviation as data (and, per the
  deviation rules in `Dabby_Handoff_Notes.md`, ask what drove it only if not
  obvious, as a single Beat 2 question).
- **`dab_notes` is verbatim.** The user's exact words, in the order said,
  including hypotheses and asides. Paraphrasing this field is a documented
  failure mode (Sessions 66, 69). Party-mode queue notes are already verbatim
  — carry them over exactly and append anything the user adds at
  reconciliation.
- **Confirm before writing.** The readback (step 4) and the analysis drafts
  (step 5) are approval gates. Writing files before the user approves is the
  narrating-instead-of-proposing failure mode.
- **Two registers.** Field names (`utc_logged_at`, `sessions_prior_today`,
  `analysis`), jar slugs, `RIG_N`-style constants, and this file's own step
  names ("Beat 1", "Beat 2") are machine-side vocabulary — they never appear
  in a message to the user. The user-facing register is the display forms:
  what `pending_dab.py` prints under its "say it to the user" banner, "Rig N
  — ..." expansions, curve tables, and the settled display labels in step 5.
  Leaking machine-side vocabulary is a documented failure mode (Sessions
  142–143); steps 1, 4, and 5 hand you the display forms — compose around
  them instead of translating from memory.

## When NOT to use this skill

- **No jar exists for the strain** — jar creation comes first and is the
  new-jar skill; invoke it, then return here. Check `jar_manifest.py`'s
  inline name comments (or grep `jars/*.py` for `STATUS.name`) before
  concluding a jar is missing — and check open PRs too (a jar may exist on an
  unmerged branch).
- **Correcting an already-logged run** (wrong date, wrong equipment, wrong
  swab) — that's the correct-frozen-data skill
  (`.claude/skills/correct-frozen-data/SKILL.md`).
- **Session-open / "about to dab"** — that's the dab skill (capture only).

## Workflow

**0. Session state.** If the session-open sequence hasn't run this session,
do it now — in short: `git checkout main && git pull` (unless mid-work on a
feature branch with uncommitted changes), read all three of
`HANDOFF_STATE.md` / `HANDOFF_WISDOM.md` (it takes two Read calls) /
`Dabby_Handoff_Notes.md`, and check open PRs. The dab skill's steps 2–5 are
the full definition if anything here is unclear. Never draft a readback from
stale or unread state.

**1. Timestamp — the queue is the source of truth.**

```
python pending_dab.py list
```

- **Entry exists for this dab** → `python pending_dab.py consume` and use its
  paste-ready lines exactly as printed — date, logging timestamp, and the
  dab-of-the-day count are all computed for you. Never run `datetime.now()`
  for a dab that has a captured entry — recalculating at reporting time is a
  documented, thrice-triggered failure mode (Sessions 121, 140 ×2). The
  say-it-to-the-user block underneath is the readback's factual skeleton:
  local time, dab-of-the-day, and the equipment default *as of that entry's
  timestamp* (per-entry, so post-dated reconciliation can't inherit a stale
  rig). The entry clears itself once the run is written and the generator
  runs.
- **No entry, results just happened** → capture now (`python pending_dab.py
  start`), then consume it. "Now" is legitimately `utc_logged_at` — the field
  means time-of-logging.
- **No entry, dab was earlier** (hours ago same day, or a prior day) → the
  date/time protocol in `CLAUDE.md` governs, read it live — in short: a
  user-stated clock time or relative offset converts to UTC and becomes
  `utc_logged_at` (its rule 6); a post-date with no recallable time gets the
  casual-register ask and `None` if unrecoverable (its rule 8). When in doubt
  which branch applies, that protocol decides, not this list.
- **Multiple entries (party queue)** → reconcile oldest-first, one run at a
  time, each through this full workflow. The queue note is the verbatim
  `dab_notes` foundation for its run; the capture time is that run's
  `utc_logged_at` and its local date is the `run_date`. Ask the
  hard-to-recall fields in the casual register ("do you happen to remember
  the swab color on the first one?") — at a party, "Not recorded" is an
  acceptable swab value; a genuinely empty swab field fails validation by
  design.

**2. Identify the jar and the run number.** Resolve strain → slug via
`jar_manifest.py`; read `jars/<slug>.py` if not already read this session.
Take the next run number from `HANDOFF_STATE.md`'s generated `Next run: N`
on the strain's header — never from memory or list position. Equipment
default: for a queue-backed run, `consume` already printed it, computed as of
that entry's timestamp (this mechanizes the stale-default class that
mislogged seven runs; see the Session 140 failure mode). Only a run that
never had a queue entry needs the manual path: the "Most recent run (all
jars, by utc_logged_at)" line in `HANDOFF_STATE.md` for a run being logged
now; for a manual post-date, the most recent run logged **before** the run's
logging timestamp — check the chronology across jars. If the user's report
mentions any equipment change, apply the equipment-change and new-rig rules
in `Dabby_Handoff_Notes.md`.

**3. Gather the content fields.** Apply the Session Logging Protocol in
`Dabby_Handoff_Notes.md` — read it live. In particular: swab color and curve
numbers cannot be logged vague (ask as many clarifying questions as needed);
ask intensity ("How hard did it hit?") if not reported. The dab-of-the-day
count comes printed from `consume` for queue-backed runs; compute it by hand
only for a run that never had an entry (same `run_date`, earlier
`utc_logged_at`, any jar — silently, no narration; the validator cross-checks
the stored value either way, so a miscount fails the generate).
`duration_seconds`: the programmed curve's terminus unless the report
suggests the session ended early — then ask when it stopped. On Beat 2
candidates, reason through the physics first: two readings that describe the
same physical event (a hot insert running out of material IS the temperature
signal) are not an ambiguity worth a question.

**4. Beat 1 / Beat 2 readback.** Always, unconditionally: state the parsed
facts — date and time (from step 1's printed block, never recomputed), strain
in full name, run number, curve as a table, swab, equipment in full expansion
on first mention, session order (first-of-day gets the celebratory energy the
protocol calls for; otherwise matter-of-fact). Then Beat 2 per the protocol:
at most one or two ambiguous-AND-consequential interpretation checks, clearly
separated, the invitation as the last line. Wait for the user's response.

The readback never announces its own structure — "Beat 1", "Beat 2", and
field names stay out of it; it's just facts, then questions. Worked example
(shape and register, not sentences to recite):

> Logging this as **Fire Water #106, Run 30** — July 2 at 8:14pm MDT, second
> dab of the day. The gentle descent again:
>
> ```
>    0s   440°F   Session open — hot open, gentle descent start
>   30s   420°F   Gentle descent midpoint
>   60s   400°F   Floor
> ```
>
> Full 60 seconds, moderate load, swab golden. Rig 6 — Dr. Dabber Sapphire
> Plus (v2) · Wym Stick Piston (stock — .094" bore airflow) · Dr. Dabber
> stock bubbler.
>
> One thing to pin down before I write it: "harsh at the end" — end of the
> last draw, or after the heater shut off? Different signals. Everything
> else look right?

Before sending: anything backticked, snake_case, ALL_CAPS, a jar slug, or a
step label gets swapped for its display form.

**5. Draft `analysis`, `next_ai_analysis`, and the new `next_text` one-liner
in chat.** Select the applicable recipes from the analysis-toolkit skill
(`.claude/skills/analysis-toolkit/SKILL.md`) before drafting — scan the
trigger conditions and apply every recipe that matches. Then apply the
sourcing and confidence rules from `Dabby_Handoff_Notes.md` (`analysis` traces every
claim to this session's report, this strain's history, or the wisdom layer;
equipment differences between compared runs are confounds; user hypotheses
enter at "user suggested X" weight) and the epistemic flags in `CLAUDE.md`.
Check `HANDOFF_WISDOM.md` for cross-strain patterns before writing —
abandoning established equipment framing for an improvised mechanism is a
documented failure mode. `next_ai_analysis` is a concrete recommendation
with brief reasoning, 4–5 sentences max, not a recap — and it ends with the
predict-before-running pair (one sentence of expected observation, one of
what would surprise, written before the run exists; convention in
`Dabby_Handoff_Notes.md`, What to Try Next — AI Analysis).

Present the drafts under their settled display labels (Session 49 decision)
— never under the field names:

> **AI Run Analysis** *(frozen with the run)*
> …the run's synthesis…
>
> **What to Try Next:** …the one-liner…
>
> **AI Analysis** *(the What to Try Next reasoning)*
> …the recommendation… Expected: …one sentence… Surprising: …one sentence…

The step 4 pre-send check applies here too. Register inside analysis prose:
the strain being logged gets its full name; cross-strain run citations follow
the log's established style as the wisdom layer writes them (e.g. "FW106 R26",
"BB36 #2") — that shorthand is rendered convention, not a leak.

Show both drafts and wait. Approval = an explicit go-ahead, corrections to
apply, **or** "just log it" at any point — per the protocol's "user ends it
anytime" rule, that means write as read, with unresolved prose vagueness
logged verbatim rather than sharpened. Silence is not approval.

**6. Write the jar file.** After approval, in one pass:
- New curve → add a local waypoint constant to the jar (no confirmation
  needed — mechanical step per `CLAUDE.md`); reused curve → reference the
  jar's existing constant. Naming convention (from the live jars): uppercase
  slug + endpoint temperature (`LHBH_425`, `BP4RW13_430`); descriptive suffix
  for shapes (`BP4RW13_DESCENT_GENTLE`).
- Run used the current baseline curve → **use `BASELINE_420`** (or whichever
  frozen constant matches the current baseline endpoint). All run-level
  references now use frozen constants — `waypoints=BASELINE_CURVE` inside
  RUNS is banned by the preflight check in `jar_manifest.py` and will fail
  the generate step. `next_waypoints=BASELINE_CURVE` in STATUS is correct
  (it tracks the current recommendation). If the baseline itself changes,
  that's the change-baseline skill
  (`.claude/skills/change-baseline/SKILL.md`).
- Append the `CompletedRun` to `RUNS` — timestamp lines pasted from step 1,
  `dab_notes` verbatim, `endpoint_note` per its convention in
  `Dabby_Handoff_Notes.md` (never blank), `read`/`verdict` left empty
  (validators enforce both).
- Update `STATUS` — `next_text`, `next_dab_notes`, `next_ai_analysis`,
  `next_waypoints`.
- Keep personal identifying information out of every field except
  `dab_notes`/`next_dab_notes` (the only non-rendered fields).

**7. Generate and verify.** `python Dabby_Log_Generator.py`. It must end with
`Written: index.html` / `Written: HANDOFF_STATE.md`. If it prints VALIDATION
ERRORS or MANIFEST ERRORS: the message says exactly what to fix — fix the
data it names, never the validator, and rerun. A PENDING DABS failure has two
legitimate readings: an entry you *should* have consumed for the run you just
wrote (fix the run's `utc_logged_at` to match), or entries for runs not yet
reconciled — mid-queue, that second case is exactly what the sanctioned
escape hatch is for: `DABBY_ALLOW_PENDING=1` for the intermediate generates
(see the reconciliation loop below), never as a way to skip reconciliation
entirely. The **final** generate of any session must pass clean, without the
env var. Eyeball the rendered run section in `index.html` if anything about
the edit was unusual.

**8. Ship.** Feature branch — never commit to main; name it with the jar's
slug or full strain words (`log-fw106-run30`), never a shorthand that reads
as something else (the documented "fb" problem). Commit the jar file +
`index.html` + `HANDOFF_STATE.md`, push, open the PR via the GitHub MCP
`create_pull_request` tool (the `gh` CLI is not installed) with a
plain-English description per `CLAUDE.md`'s example. If this session already
has an open PR, push to that branch instead of opening another. Merging
waits for the user unless they've said otherwise.

Status lines to the user are outcome language, one line, e.g. "Logged and
rendered clean — nothing else to log tonight. PR's up: <link>." Never the
tooling's own vocabulary for its internals, and no narration of steps that
fired or didn't.

**Reconciliation loop (multiple queue entries):** one run at a time through
steps 1–7, oldest first. Intermediate generates use `DABBY_ALLOW_PENDING=1`
(the written run's own entry auto-prunes; the still-unreconciled ones are the
expected leftovers). Commit after each run — jar + regenerated outputs — so
the history reads like the evening did. The last run's generate drops the env
var and must pass clean: that's the proof the queue is fully drained. Then
one branch, one PR, per step 8.

## Recovery paths (don't improvise these)

- **Edit fails on string mismatch twice** → stop retrying; Grep the exact
  current bytes of the target region and re-read the file (required after any
  branch switch, and after your own earlier edits).
- **Validation error on generate** → the message is prescriptive; fix the
  named data. A date error means recompute from `utc_logged_at`; a
  sessions_prior_today error means recount across all jars.
- **PR preview doesn't update** → check `mergeable_state`; if `dirty`, merge
  main into the branch and push (documented failure mode — don't blame
  propagation without checking the pipeline).
- **Push rejected** → never force-push (blocked here, HTTP 403) and never
  amend pushed commits; cut a fresh branch from `origin/main` and re-apply.

## Provenance and maintenance

Created 2026-07-02 against the Layer 0 mechanical floor (PR #207). Verify
these still hold if the skill starts giving results that don't match reality:

```
# The queue tooling this skill leans on (consume prints the paste block AND
# the say-it-to-the-user block with the per-entry equipment default):
python pending_dab.py --help
grep -n "_check_pending_dabs" Dabby_Log_Generator.py

# Generated facts used in step 2 (manual/non-queue path):
grep -n "Most recent run\|Next run:" HANDOFF_STATE.md | head -5

# The display helpers the say-blocks and curve tables come from:
grep -n "fmt_curve_table\|_fmt_equipment_display" Dabby_Core.py | head -5

# The protocol sections steps 3-5 point at:
grep -n "Session Logging Protocol\|Beat 1\|Equipment Protocol" Dabby_Handoff_Notes.md
grep -n "endpoint_note\|deviates from the planned\|user ends it anytime" Dabby_Handoff_Notes.md

# Recovery-path claims (PR preview staleness; PR #206 correction example):
grep -n "mergeable_state" Dabby_Handoff_Notes.md
git ls-remote origin refs/pull/206/head

# Validators that backstop steps 3, 6, 7:
grep -n "sessions_prior_today\|UTC-rollover\|superseded by analysis\|do not log without" Dabby_Core.py

# The schema quick-reference for step 6:
grep -n "Logging quick-reference" -A 3 Dabby_Core.py
```

Dogfood-test status: **re-tested July 3, 2026 — PASS-WITH-FINDINGS** after
the display-register mechanization. Protocol variant: scripted fictional run
(The Hive #1 Run 9, canned user turns) in an isolated worktree, register-
focused — full pipeline through a clean no-env-var generate, validator
cross-checks passed, queue entry auto-pruned. Leakage grep over the
user-facing messages: readback, draft headers, and status line all clean —
zero machine-side vocabulary (the Session 143 leak surfaces). Finding
applied same day: analysis-draft citations use the wisdom layer's short-form
register (step 5's register note is the fix). This variant did not re-verify
golden-match field accuracy — for suspected mechanical-field regressions,
re-run the July 2, 2026 golden-run replay (Watermellos Run 18 stripped from
its jar, the user's actual verbatim report replayed; that run PASSED with
every mechanical field exact-matched, and its findings — duration_seconds
derivation, the post-dated equipment-default caveat in step 2, next_text in
the step 5 gate, step 0's inline summary — are in the current text).
Test-design note for golden re-runs: also revert the jar's STATUS next_*
fields to their pre-run state, or the replayed analysis is partially
anchored by the golden run's conclusions. Re-run after any structural change
to the workflow steps, with the leakage grep as a pass/fail criterion.
