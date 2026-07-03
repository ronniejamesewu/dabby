# Register Leak Diagnostic — Answer (Session 145)

**Do not read this until you've confirmed with the user, per the gate in
`register_leak_diagnostic_exercise.md`, that your independent diagnosis is
thorough.** If you're reading this without having done that, stop, go run
the exercise properly, and come back.

---

## 1. The leak

"...when I logged **the swab field**..." — `swab` is the literal
`CompletedRun` dataclass field name (see `Dabby_Core.py`). The display form
is "swab color," or simply "the swab" / "what I read for the swab."

## 2. Why it counts as a leak

The two-registers rule (dab and log-run skills, "Hard gates" / "Two
registers") states that field names, jar slugs, `RIG_N`-style constants, and
step labels are machine-side vocabulary that never appears in a message to
the user. "The swab field" names the schema field directly. It isn't
disguised or backticked — it reads as completely ordinary English — but
it's still exactly the concept the rule prohibits: a raw internal name
standing in for a user-facing description of what happened.

## 3. The mechanism — why the pre-send check didn't catch it

Both skills specify the same check, worded as: "anything backticked,
snake_case, ALL_CAPS, a jar slug, or a step label gets swapped for its
display form." That check is **syntactic** — it scans for a *form*
(formatting markers, naming conventions, known slug strings) rather than a
*meaning*. "The swab field" trips none of the five listed triggers: it's
not backticked, not snake_case, not ALL_CAPS, not a slug, not a step label.
It is a plain, grammatically normal English phrase that happens to name a
schema concept as a field. The check was built to catch a leak *dressed up*
in code formatting; it has no rule for a schema concept referenced in
ordinary prose. This is a coverage gap in the check's design, not a
one-off lapse in applying it correctly.

## 4. Same failure recurring, or a new variant?

**A new variant of the same root cause, not a repeat of the exact Session
142–143 failure.** The July 3, 2026 mechanization fixed the
*composition-from-memory* problem: Claude translating internal facts into
prose during a scripted step (a readback, an analysis draft) and letting raw
vocabulary slip in along the way. The fix was to have `pending_dab.py
brief`/`consume` print the relevant facts already in display form, so the
skills could compose replies *from that printed output* rather than
reconstructing display language from memory at each output point.

This leak did not happen during that kind of composition. It happened in a
spontaneous, off-template aside — flagging an autocorrect-correction
assumption in a wrap-up sentence — that has no corresponding printed
display-form block to compose from, because nothing in the printed facts
covers "here's an assumption I made correcting a typo." The mechanization
closed the surface where Claude reconstructs *known, anticipated* facts from
memory; it did not (and structurally cannot, without a check that scans
every sentence for schema-concept references regardless of phrasing) close
an ad hoc, improvised remark.

The underlying priming mechanism is the same one the wisdom file already
names for the 142–143 leaks: several consecutive tool calls had just written
`swab='...'` directly into the jar file, so "swab" as a *field* was maximally
active in working memory at composition time. What's genuinely new is the
surface: a scripted output step vs. an improvised footnote. The fix that
closed the first surface doesn't reach the second.

## Suggested fix direction (not yet actioned — flag to the user, don't act unilaterally)

The pre-send check needs a semantic net alongside its syntactic one — something
closer to "am I naming a schema concept as a field/record/entry, even in
plain, unformatted words?" rather than only pattern-matching on formatting.
This is more plausibly a backlog item (open design question: can this be
made mechanical at all, or does it stay a judgment-layer check like several
other entries in `Dabby_Handoff_Notes.md`'s "Live failure modes" section?)
than an immediate rewrite of the skills' pre-send check language.
