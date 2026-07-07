# What good lineage research actually looks like

This exists because a real research pass on "Papaya + Z Pie #22" (a 710 Labs
jar) undershot badly compared to the same question run through Perplexity —
not because the source-hierarchy design was wrong, but because the research
stopped after a few generic searches instead of following what those
searches turned up. Perplexity found 710 Labs' own genetics page for Papaya
(stating the cross as undisclosed — "Mystery," clone-only) and 710's own
product copy for Z Pie #22; the under-effort pass missed both and cited a
single non-anchor source instead. The difference wasn't a missing step on a
checklist — it was that Perplexity kept pulling threads and the other pass
didn't.

## Calibrate expectations: 710 Labs is the best case, not the typical case

710 Labs is a large producer with dedicated genetics pages and real product
copy — that's why the example below found so much. It's also, per
`grep -h "'Producer'" jars/*.py`, the single most common producer in this
log (roughly a third of jars as of last check) — so "710 Labs shows up"
isn't itself rare. What's true is that the producer mix in this log varies
widely: 710 Labs alongside several small, one-person or boutique operations
(Quasi Farms, Nikka T, Riptide, and others) with little or no web presence.
For the small end of that range, a producer/breeder anchor source
frequently won't exist, and that's the expected, normal outcome — not a
sign the research fell short. Don't assume either direction from the
producer name alone; check. The
stopping rule below ("stop when two searches in a row add nothing new")
applies exactly the same way whether that point arrives after three
searches because a small producer genuinely has nothing published, or after
fifteen because a large one has a rich trail to follow. Don't burn excess
effort trying to force an anchor to appear where the evidence says there
isn't one, and don't hedge apologetically when the honest report is
"searched, found little to nothing, lineage is genuinely unconfirmed" — that
outcome is complete and correct, not a partial result.

**But "assume small producer" is itself an assumption — verify it, don't
apply it blindly.** A third real test (Orange Candy, producer listed only as
"Nikka T") assumed going in that this was a small, obscure maker with no web
presence. The first search corrected that immediately: Nikka T is Nick
Tanem, a well-known, award-winning hash pioneer (Essential Extracts) with
real published material. The research correctly updated on that evidence
instead of forcing the "small producer, expect nothing" expectation onto
what it found. The actual rule underneath both calibration notes in this
file is the same one: match effort and confidence to what the evidence
says, not to a prior guess about the producer — whether that guess is
"this is 710 Labs, there'll be a lot" or "this is some small outfit, there
won't be anything."

## This is not a checklist to satisfy — read this part first

A list of required steps gets satisficed: do the minimum each bullet implies,
check the box, stop. That's exactly what happened before — "run several
searches" got read as "run three and be done." Adding more required steps
just creates a harder version of the same failure mode: a subagent can run
the mandatory producer-site search, get an unclear result, write "not
found," and move on — technically compliant, still shallow. A checklist
can't tell the difference between "I looked hard and it's genuinely not
there" and "I looked once and gave up."

What's actually being asked for is a *disposition*, not a sequence: notice
something you didn't expect in a result, decide whether it's worth chasing,
reformulate your next search based on what you just learned, and keep going
until doing more genuinely stops teaching you anything — not until you've
done a fixed number of things.

## The stopping rule

Not "did I do N searches" — **stop when two searches or fetches in a row
add nothing you didn't already know.** Before that point, if a result
mentions a name, a claim, or a detail that's new, that's a thread — decide
explicitly whether to pull it, don't just note it and move past it.

## The accountability check

At the end of your report, list every named entity, claim, or lead you
encountered during research — including ones you decided *not* to chase —
and say why for each. ("Mentioned '808 Genetics' clone-history claim about a
different sourcing detail — didn't pursue further, tangential to the
lineage question.") This is the part that actually resists satisficing: it's
not a box to check, it's an accounting that makes it visible if you skipped
something without a real reason. If you can't articulate why you dropped a
thread, that's a signal you should have pulled it.

## What it looks like when this is done well — two real cases, not one

The first case below (710 Labs) is the best-case scenario: a large producer
with real published material to find. The second (a small hash maker) is
closer to the typical case in this log. Both are examples of doing the work
right — the difference in outcome reflects a difference in what's actually
out there, not a difference in effort.

**Case 1 — 710 Labs (large producer, real trail to follow):**

> **Papaya (outer ring):** Searched the strain name generically first, then
> specifically hunted for 710 Labs' own page — found it: genetics listed as
> "Mystery" / "Clone Only." That's an answer, but a thin one (no actual
> lineage), so continued rather than stopping there. Follow-up searches
> surfaced 808 Genetics' clone-history claim (Citral #13 × Ice #2) as one
> lead; instead of accepting one source, kept searching and found four more
> independent sources converging on the same cross — corroborated, still not
> producer-confirmed, reported at that confidence level. Then pushed one
> generation further into Citral #13's and Ice #2's own parents; that's
> where results got vague and inconsistent ("Pakistani indica-derived,"
> "Afghan/Skunk/NL-type" with no specific cross named) — two follow-up
> searches added nothing new at that depth, so stopped there and said so
> explicitly rather than reporting vague ancestry as settled.
>
> **Z Pie #22 (center):** 710's own product copy directly named the
> immediate cross (Z × Georgia Pie) — high confidence, producer-anchor.
> Followed the thread into Georgia Pie's own parents rather than treating
> the immediate cross as the finish line: multiple independent sources
> converged on Gelatti × Kush Mints #11, and — notably — a "Gushers"
> component that appears in informal descriptions never showed up in any
> source once actually searched for directly. That's a thread worth
> flagging as a likely correction, not just a different opinion, precisely
> because it was checked rather than assumed. Pushed one generation further
> into Gelatti's own parents; here two sources genuinely disagreed (Gelato ×
> Biscotti vs. Gelato × London Pound Cake) — reported as an open
> disagreement rather than picking one to sound resolved.

**Case 2 — Swollen Heads Hash Co. (small producer, honest "unconfirmed"):**

> **Papaya con Chamoy:** No producer/breeder page existed for this specific
> product — a small hash maker with no dedicated genetics page. Searched the
> product name plus "genetics" and "lineage," found nothing tying it to a
> documented cross. Two adjacent leads turned up — a generic "Papaya" cultivar
> from Nirvana Seeds, and an unrelated "Chamoy" cultivar from a different
> breeder with its own disputed lineage — but neither one actually named or
> confirmed *this* product, and one more round of searching specifically
> trying to connect them came back empty. At that point, two searches in a
> row added nothing new, so stopped: reported the two adjacent leads as
> exactly that (adjacent, not confirmed), noted that "papaya con chamoy" reads
> as a flavor-descriptive name (papaya fruit with chamoy, a tart-spicy
> condiment) rather than a cultivar name, and drew **no** terpene inference
> from an unconfirmed lineage rather than defaulting to a generic guess. This
> is the correct outcome, not a shortfall — there was nothing more to find,
> and the report says so plainly instead of padding it out.

The pattern in both cases: the first answer wasn't the finish line, an
unexpected detail (or its absence) got chased rather than noted and dropped,
and the tree went deeper — or the search concluded honestly — once doing
more stopped adding anything. Neither case stopped at a preset number of
steps; both stopped when the evidence itself ran out.

## Provenance and maintenance

Last verified against the repo: 2026-07-02. All three cases above are real
outcomes from actual research runs, not hypothetical illustrations. The
710 Labs and Nikka T cases trace to real jars in this log (`papzp22.py`,
`oc.py`); the Swollen Heads case (Papaya con Chamoy) was a live research
exercise on a strain that is not a logged jar — there is no
`jars/<slug>.py` to diff it against — re-run the dogfood test pattern
(hide a real jar in an isolated worktree per `SKILL.md`'s data-safety
protocol, run this skill fresh against a reconstructed prompt, diff the
result against `git show origin/main:jars/<slug>.py`) against a new strain
if this file's guidance stops producing results this good.

The "most producers here are small" claim is a fact about this project's
actual jar log as of the date above, not a permanent property — re-check it
periodically:

```
# Producer field across all jars, to see the actual current mix:
grep -h "'Producer'" jars/*.py
```
