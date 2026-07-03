# Register Leak Diagnostic Exercise — Session 145

This is a **blinded diagnostic exercise**, not a normal failure-mode write-up.
It exists to test whether a fresh Claude session — using only this project's
existing skill documentation and failure-mode history — can independently
diagnose a specific internal-vocabulary leak, without being handed the
answer first. The answer lives in a separate file,
`register_leak_diagnostic_answer.md`, gated behind a user-confirmation step
below. **Do not open that file, grep it, or peek at its contents until
you've completed the gate.** Doing so defeats the entire point of this
document existing in two pieces.

---

## The incident

Context: mid-session, the log-run skill's pipeline, The Hive #1 Runs 9–10.
Claude had just finished writing the jar file — including edits containing
literal lines like `swab='Golden — minimal reclaim.'` — regenerating,
committing, and shipping a PR with both runs. Immediately after, in a plain
wrap-up chat message (not a file edit, not code, not a scripted readback
step), Claude wrote:

> "One flag on the way in: I read "Sean's were golden and minimal" as
> "swabs" (autocorrect glitch) when I logged the swab field — shout if
> that's wrong."

The user's reaction: "Oh geeze that leak from your internals was terrible."

---

## Your task

Before reading anything past the Gate section below, or opening the answer
file, work through this yourself:

1. **Find the actual leaked term or phrase** in the quoted sentence above.
   Be specific — quote the exact words, not a paraphrase of the general
   problem.
2. **Explain why it counts as a leak** under this project's two-registers
   rule. Go read that rule live in the dab and log-run skills' "Hard gates"
   / "Two registers" sections right now — don't answer from memory of what
   you think it says.
3. **Explain the mechanism** — why did this get past the pre-send check both
   skills specify? Re-read the check's exact wording in both skill files
   before answering. What, specifically, does the check test for, and why
   didn't this leak trip it?
4. **Cross-reference against the known-failure-mode history** in
   `Dabby_Handoff_Notes.md` — search for "Internal vocabulary leaking into
   chat" and read its full entry, including the Session 142–143 provenance
   and the July 3, 2026 mechanization it describes (display-form printing
   via `pending_dab.py brief`/`consume`). Is this incident the *same*
   failure recurring, or a genuinely different variant of it? State which,
   and defend the distinction with specifics from that entry — don't just
   assert an answer.

---

## Gate — read before opening the answer file

**Do not open `register_leak_diagnostic_answer.md` yet.**

First, present your diagnosis — all four points above — to the user in
chat, in your own words, and explicitly ask whether it's thorough. Something
in the shape of: "Here's my diagnosis of the leak... does this look
complete, or am I missing something?" Then wait for their actual response.

Only after the user has **explicitly confirmed** (a "yes," "looks good," a
correction you've incorporated and then re-confirmed with them — silence,
or the conversation simply moving to a different topic, does not count) may
you open and read `register_leak_diagnostic_answer.md`.

If you find yourself tempted to open it "just to check your work" before
that confirmation — don't. If you already did, by accident or otherwise,
say so to the user plainly rather than quietly proceeding as if the gate
had been honored. A blinded exercise that silently un-blinds itself isn't
worth running.

After confirming with the user and then reading the answer file: compare
your diagnosis against it point by point. If they diverge on any of the
four points, that divergence is itself useful data for the user — surface
it explicitly rather than quietly absorbing the answer file's framing as
more authoritative than your own reasoning turned out to be.

---

## Provenance

Session 145, July 3, 2026. Origin: a real leak caught by the user during
live use of the log-run skill (PR #216) — not a synthetic or constructed
test case. This is the first blinded-diagnosis-style exercise in this
skill library; prior dogfood tests (see the dab and log-run skills' own
"Provenance and maintenance" sections) hand the tester a protocol to
*execute* and check the result against reality, not a hidden answer to
converge on independently through reasoning alone. If this format proves
useful for training future sessions on this project's specific failure
modes, it's a candidate pattern to reuse for other incidents. If it proves
awkward in practice — future sessions routinely skipping the gate, or the
two-file split creating more confusion than it prevents — that's worth
noting back into this file or the backlog, not silently abandoning the
format.
