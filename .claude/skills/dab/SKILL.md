---
name: dab
description: Session-open ritual and dab-time capture for this Dabby project. Trigger whenever the user announces a dab is starting or imminent — "about to hit it", "grabbing one", "grabbing a dab of X", "we are gonna do a run", "warming up the rig", or any message naming a strain with dabbing intent — and ALSO on every additional dab announced mid-session ("grabbing another"). Trigger in party mode when the user says "party mode" or sends a terse strain-plus-observations fragment while socializing (e.g. "party mode: FW, normal load, harsh at 30") — party mode captures and replies in one line, nothing else. This skill captures the timestamp mechanically and performs the mandatory session-open sequence (git sync, handoff reads, open-PR check, equipment soft-check) — in normal mode; party mode captures only and explicitly defers that sequence to reconciliation. It never logs a run — logging is the log-run skill, and only the user initiates logging.
---

# Dab

Session-open ritual and timestamp capture. The single most perishable fact in
any run is *when it happened* — everything else can be reconstructed, 7:42pm
cannot. So capture comes first, before git, before reads, before any reply.

## Terms

| Term | Meaning |
|---|---|
| Capture | Writing the current UTC time (plus the user's verbatim words, if any) to `.pending_dabs.json` via `pending_dab.py start`. Capture is NOT logging — no run is written, nothing is committed. |
| The queue | `.pending_dabs.json` — session-local, gitignored. The generator refuses to run while entries in it have no matching logged run, so captures cannot be silently forgotten. |
| Party mode | Minimal-interaction capture for group settings: one command, one line back, zero questions. All judgment deferred to reconciliation (see log-run skill). |
| Session-open sequence | The mandatory startup steps from `CLAUDE.md`: git sync, the three handoff reads, plus the open-PR check and equipment soft-check from `Dabby_Handoff_Notes.md`. |

**Two registers.** Everything in this file — the Terms table, command names,
field names, `RIG_N`-style constants, jar slugs, step numbers — is machine-side
vocabulary and never appears in a reply to the user. The user-facing register
is what `pending_dab.py` prints under its "say it to the user" banner, plus
your own outcome language ("nothing else to log tonight", never "queue
drained"). Leaking machine-side vocabulary into chat is a documented failure
mode (Sessions 142–143); the fix is built into steps 5–6 — the facts arrive
pre-rendered, so compose around them instead of translating from memory.

## Hard rules

- **Capture ≠ logging.** A captured timestamp is not a mandate to write a run.
  Runs are logged only when the user initiates logging (reports results and
  wants them recorded). Never propose logging a run the user didn't ask to log.
- **Capture always comes first.** If the git pull hangs or the session derails,
  the true time must already be on disk.
- **Party mode does nothing but capture.** No git, no reads, no readback, no
  clarifying questions, no riffs. One line back. The user is at a party;
  every extra sentence costs them socially. This *defers* CLAUDE.md's
  mandatory session-open gate rather than violating it: nothing is answered
  from project state and nothing is written to the repo during party mode, so
  there is no response that needed the reads — the gate runs in full at
  reconciliation (log-run skill), before anything is actually logged. The
  queue file is the bridge that makes the deferral safe.

## When NOT to use this skill

- **The user is reporting a finished dab and wants it logged now** — still run
  step 1 (capture; the timestamp is legitimately `utc_logged_at`, which means
  time-of-logging), then hand off to the log-run skill for everything else.
- **The user is asking a question, correcting data, or doing infra work** — no
  dab is happening; follow `CLAUDE.md`'s normal session-start instructions.
- **A run is being written to a jar file** — that's log-run's job. This skill
  never edits `jars/*.py`.

## Party mode

Trigger: the user says "party mode", invokes `/dab party`, or sends a terse
fragment that reads like capture-and-go ("FW, big load, harsh at 40 — party").

1. Run, with the user's words verbatim (never paraphrased, never expanded):

   ```
   python pending_dab.py start --note "<the user's exact words>"
   ```

   Strip the mode-invocation syntax itself (`party mode:`, `/dab party`)
   from the note — everything after it is the verbatim payload.
   "Verbatim" binds the note *content*, not the shell syntax — if the words
   contain quotes, `$`, or backticks, quote/escape however the shell needs
   (single quotes, here-string) so the exact text lands in the file. Verify
   with `python pending_dab.py list` if the fragment was gnarly.

2. Reply with **one short line** confirming capture time — the script already
   prints it in the right form (`Got it — 7:42pm MDT, July 2.`); echo or trim
   it. Nothing else: no strain resolution, no rig talk, no questions, no wit.
   If the strain is unknown or ambiguous, that's a reconciliation problem for
   later, not a question for now.

3. Repeat per dab. Entries stack; the queue is the record.

That's the whole mode. Reconciliation (draining the queue with the full
logging protocol) belongs to the log-run skill and happens at the user's
desk, not at the party.

## Normal mode workflow

**1. Capture.** Immediately:

```
python pending_dab.py start
```

Add `--note "<verbatim>"` when the message carries anything beyond bare
intent — observations, load size, plans. A bare "grabbing a dab of X" needs
no note (the capture time is the payload; the strain lives in your reply and
the session context), though adding one is harmless. If the script errors (e.g. wrong cwd),
fall back to capturing UTC by hand — `python -c "from datetime import
datetime, timezone; print(datetime.now(timezone.utc))"` — and record it in
your reply so it survives; then fix the script problem.

**2. Sync.** `git checkout main` and `git pull origin main` — per the
mandatory gate at the top of `CLAUDE.md`. Exception, with a concrete test:
run `git status --short` first — if it shows uncommitted changes, or this
conversation has already made commits on a feature branch, do **not** switch
branches (you'd be abandoning live session work, which is different from the
stale leftover branch the CLAUDE.md gate protects against). Name the branch
you're staying on in your reply and continue there.

**3. Mandatory reads.** All three, before replying: `HANDOFF_STATE.md`,
`HANDOFF_WISDOM.md`, `Dabby_Handoff_Notes.md`. The wisdom file exceeds a
single Read call — page through to the end; answering from page 1 is the
exact failure the mandatory-reads gate exists to prevent. If the announcement names a
strain, resolve it to its jar file — check the inline name comments in
`jar_manifest.py`'s `ACTIVE`/`CLOSED` lists (or grep `jars/*.py` for the
strain name itself; it appears in each jar's `name='...'` field) — and read
`jars/<slug>.py` too, now, not later. If the strain
matches no jar, say so: a jar must exist before its first run can be logged,
and creating one is the new-jar skill (invoke it when the user is ready — its
own instructions cover composing from this context).

**4. Open-PR check.** List open PRs via the GitHub MCP `list_pull_requests`
tool (owner/repo from `git remote -v`; the `gh` CLI is not installed here —
`gh --version` fails). Active work may live on an unmerged branch; a strain's
true current state may be ahead of what main says (documented failure mode,
Session 86). What to do with hits: a PR touching `jars/*.py` supersedes main
for the affected strain — read its diff before your readback; infra-only PRs
just get noted and skipped.

**5. Facts.** Run:

```
python pending_dab.py brief --strain "Fire Water #106"
```

(full strain name or any unambiguous fragment; omit `--strain` if none was
named). Everything under its "say it to the user" banner is pre-rendered in
display form: dab time, dab-of-the-day count, the plan on file with its curve
table, and the working rig in full expansion — that rig line is the equipment
default. Lines under the "for the assistant" banner are instructions to you,
never quoted. If a note there flags a gap over the threshold, apply the
"Session-open soft check" in `Dabby_Handoff_Notes.md` — read it live for the
current wording.

**6. Reply.** Build it from the printed facts: quote or lightly wrap the
say-banner lines, add a sentence of your own voice. The plan on file is stated
as the plan on file, not a prescription — the user deviating from it is normal
and is itself data. Then get out of the way. Do not ask what they're going to
do; do not start logging.

Worked example — shape and register, not sentences to recite:

> Got it — 7:42pm. First one of the day. Fire Water #106, Run 30 on deck —
> plan on file is the gentle descent, first dab, moderate load:
>
> ```
>    0s   440°F   Session open — hot open, gentle descent start
>   30s   420°F   Gentle descent midpoint
>   60s   400°F   Floor
> ```
>
> Still on Rig 6 — Dr. Dabber Sapphire Plus (v2) · Wym Stick Piston (stock —
> .094" bore airflow) · Dr. Dabber stock bubbler. Fire when ready.

Before sending, one check: anything backticked, snake_case, ALL_CAPS, a jar
slug, or a protocol step name in the reply gets swapped for its display form
— the printed facts already are the display forms, so this normally means
"delete the improvisation, keep the printed line."

**Mid-session re-invocation** ("grabbing another"): run step 1 always; skip
steps 2–4 if they already ran this session, but re-run step 5's command for
each new capture — the dab-of-the-day count moves with every dab. Give a
one-line confirmation built from its output. If you're a fresh context
resuming a session and can't tell whether steps 2–4 ran, run them — repeated
reads are cheap, a stale readback is not.

**No strain named** ("gonna dab something tonight"): steps 1–5 now, `brief`
without `--strain`; step 3's jar read waits until a strain is chosen.

## Recovery paths (don't improvise these)

- `pending_dab.py start` fails → capture UTC by hand (step 1), state it in the
  reply, then debug.
- `git pull` conflicts or fails → the capture is already safe on disk; resolve
  the git problem before proceeding to reads, and say what happened.
- Strain name matches nothing → check open PRs (step 4) before concluding it's
  new; a jar may exist on an unmerged branch.

## Provenance and maintenance

Created 2026-07-02 against the Layer 0 mechanical floor (PR #207). Verify
these still hold if the skill starts giving results that don't match reality:

```
# pending_dab.py exists and its commands (incl. brief, step 5) are as described:
python pending_dab.py --help

# brief prints the say-banner facts in display form (safe to run — reads only):
python pending_dab.py brief --strain "The Hive #1"

# The mandatory-reads gate and its file list are still current:
grep -n "MANDATORY" -A 8 CLAUDE.md

# The equipment soft-check wording step 5 defers to:
grep -n "Session-open soft check" Dabby_Handoff_Notes.md

# "gh is not installed" (step 4) still true:
gh --version  # expected: command not found

# The tripwire that gives capture its teeth is still in the generator:
grep -n "_check_pending_dabs" Dabby_Log_Generator.py
```

Dogfood-test status: **tested July 2, 2026 — PASS-WITH-FINDINGS on both
scenarios, findings applied same day.** Protocol: fresh agent in an isolated
worktree; normal mode ("grabbing a dab of The Hive #1") executed all six
steps in order, capture first, correct Rig 6 default from the generated state
line, no run logged; party mode produced a one-line reply and a byte-verbatim
queue note. Findings that shaped the current text: the bare-announcement
`--note` guidance, the two-Read-call warning on the wisdom file, the
infra-PR-vs-jar-PR handling in step 4, and stripping the mode-invocation
prefix from party notes. Re-run the same protocol after any structural change
to the workflow steps.
