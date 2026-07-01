# Jar-Return Check — Design Notes

## Originating example

bp4rw13 Run 5 (June 30, 2026). 14 days and six-plus other jars since the last
run on this jar (Run 4, June 16). First descent curve on the jar. Big load.
Result: overwhelming intensity — memory gap after cycle 2, couldn't continue
after cycle 3. "Fucking big, buzzy." The session wasn't bad; it was too much.

The hypothesis: coming back to a jar after an extended stretch on other jars means
material familiarity and dosing intuition have faded. The jar may have continued
curing. The user's calibration to that specific material's ceiling is stale.
A lighter first load is the sensible adjustment.

## What "gap" means

Not purely calendar days. The more informative signal is how many other jars have
been run since the last session on this one — that tracks how far the user's
active working memory of the jar has drifted. Both inputs (days + other-jar count)
are relevant; neither alone tells the full story.

## Four implementation options discussed

**Option A: Principle only, no trigger**
State the underlying concern and leave everything to judgment.
*"Returning to a jar after an extended break — in calendar days or other jars run
since — means material familiarity and dosing intuition have faded. Factor this
into pre-run discussion when the gap seems meaningful."*
No threshold, no prescribed language. Future Claude decides when and how.
Cleanest but vaguest.

**Option B: Named signal, no prescribed response**
Name what to look at; leave the response open.
*"A long jar gap is a session-prep signal. Relevant inputs: days since last run,
how many other jars have been run since, whether the upcoming curve is new or
familiar. Weigh these and bring it up in pre-run discussion if the combination
seems worth flagging."*
Middle ground — structured inputs, unscripted output.

**Option C: Documented pattern in HANDOFF_WISDOM**
Don't add a protocol rule. Add a Cross-Strain Patterns row citing Run 5 as
evidence: *"Big load on first run back after long jar gap → overwhelming session."*
Future Claude picks it up as analytical context during pre-run synthesis,
the same way it draws on any pattern. No procedural gate — just knowledge.

**Option D: Pre-run framing guidance**
Fold it into what pre-run discussion already is, not a separate checklist step.
*"Pre-run prep should account for jar context: how long since last run, whether
the curve is new or familiar, what the jar's history suggests about load
sensitivity. A jar returning from a long gap deserves a mention; how to handle
it is Claude's call."*

## Recommendation

**C or D.** C because it lives where pattern knowledge lives and builds from
evidence rather than protocol — future Claude encounters it as a known pattern,
not a rule to follow. D if explicit pre-run behavior shaping is preferred without
the mechanical gate. A is too vague to reliably surface; B risks ending up neither
principled nor specific enough to be useful.

Avoid making this a hard-threshold procedural check (count ≥ 2 → say X). The
underlying situation calls for judgment, not a trigger condition.

## Why tabled

Nuanced enough that the right framing deserved a considered, un-stoned decision.
The four options are meaningfully different in how much they prescribe vs. leave
open, and the wrong choice would either under-surface the signal or over-mechanize
the response. Better to get it right than fast.
