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

   "Verbatim" binds the note *content*, not the shell syntax — if the words
   contain quotes, `$`, or backticks, quote/escape however the shell needs
   (single quotes, here-string) so the exact text lands in the file. Verify
   with `python pending_dab.py list` if the fragment was gnarly.

2. Reply with **one short line** confirming capture time, e.g.
   `Got it — 7:42pm ✓`. Nothing else: no strain resolution, no rig talk, no
   questions, no wit. If the strain is unknown or ambiguous, that's a
   reconciliation problem for later, not a question for now.

3. Repeat per dab. Entries stack; the queue is the record.

That's the whole mode. Reconciliation (draining the queue with the full
logging protocol) belongs to the log-run skill and happens at the user's
desk, not at the party.

## Normal mode workflow

**1. Capture.** Immediately:

```
python pending_dab.py start
```

Add `--note "<verbatim>"` if the announcement carried any observations worth
keeping (load size, strain, intent). If the script errors (e.g. wrong cwd),
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
`HANDOFF_WISDOM.md`, `Dabby_Handoff_Notes.md`. If the announcement names a
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
Session 86).

**5. Equipment soft-check.** Apply the "Session-open soft check" in
`Dabby_Handoff_Notes.md` — read it live for the current threshold and wording
rather than trusting any number remembered or written here. Its input is the
"Most recent run (all jars, by utc_logged_at)" line in `HANDOFF_STATE.md`,
generated precisely so this check never requires a cross-jar query. Whether
or not the check fires, that line's rig is the working equipment default.

**6. Reply.** Confirm the capture time (local, from the script's output).
State the working rig in full expansion on first mention (format per the
Beat 1 readback expansion rules in `Dabby_Handoff_Notes.md`). If a jar was
read, state its planned next run from `STATUS` — as the plan on file, not a
prescription; the user deviating from it is normal and is itself data. Then
get out of the way. Do not ask what they're going to do; do not start logging.

**Mid-session re-invocation** ("grabbing another"): run step 1 always; skip
steps 2–5 if they already ran this session; give a one-line confirmation. If
you're a fresh context resuming a session and can't tell whether they ran,
run them — repeated reads are cheap, a stale readback is not.

**No strain named** ("gonna dab something tonight"): steps 1–4 now; step 3's
jar read waits until a strain is chosen.

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
# pending_dab.py exists and its commands are as described:
python pending_dab.py --help

# The generated most-recent-run line (step 5) still exists:
grep -n "Most recent run" HANDOFF_STATE.md

# The mandatory-reads gate and its file list are still current:
grep -n "MANDATORY" -A 8 CLAUDE.md

# The equipment soft-check and Beat 1 expansion rules are where step 5-6 point:
grep -n "Session-open soft check\|Beat 1 readback expansion" Dabby_Handoff_Notes.md

# "gh is not installed" (step 4) still true:
gh --version  # expected: command not found

# The tripwire that gives capture its teeth is still in the generator:
grep -n "_check_pending_dabs" Dabby_Log_Generator.py
```

Dogfood-test status: not yet run end-to-end in a live session. Test protocol:
fresh agent in an isolated worktree, session-open prompt naming a real strain;
verify capture happens first, the sequence runs in order, and no run gets
logged. Party variant: terse fragment in, one line out, verbatim note in the
queue. Update this note after the first real test.
