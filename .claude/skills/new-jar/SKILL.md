---
name: new-jar
description: Create a new jar file for a strain that doesn't have one yet in this Dabby project — the two-file edit (jars/<slug>.py boilerplate + slug added to jar_manifest.py's ACTIVE tier), including a web-search lineage check and correctly handling any number of physical strain components (single strain, two-strain blends, three-strain blends, whatever a given producer calls them). Trigger this whenever the user says things like "new jar", "add a strain", "starting a new jar for X", "got a new jar today", or names a strain they haven't logged before. Also trigger it implicitly any time a run is being logged for a strain whose name doesn't match any existing STATUS.name across jars/*.py — a jar must exist before that run can be logged, so jar creation is a required sub-step, not an optional one. Also invoke this skill when another skill or workflow (e.g. a party-mode run-capture reconciliation pass) needs to create a jar for a previously-unlogged strain.
---

# New Jar

Creates the empty jar a strain needs before its first run can be logged. Per
this project's convention, jar creation always ships on its own — an empty
`RUNS = []` jar with a filled-out profile is a complete, useful unit by
itself, not something that has to wait for the first session.

## Terms

| Term | Meaning |
|---|---|
| Jar | This project's unit of a strain's session log — one `jars/<slug>.py` file per strain, holding its profile (`STATUS`) and its logged sessions (`RUNS`). |
| Slug | The short, filename-safe identifier for a jar (e.g. `dbrb`, `papzp22`) — used as the Python module name and the manifest key. Never shown to the user; always render the full strain name in any user-facing text. |
| `STATUS` | The `StrainStatus` dataclass instance in a jar file — the strain's profile and current "what to try next" guidance. Defined in `Dabby_Core.py`. |
| Manifest preflight | The startup check in `jar_manifest.py` (`_validate_manifest_preflight()`) that runs before any jar is loaded — catches duplicate slugs, a manifest entry with no matching file, a file with no matching entry, and disallowed imports. Runs every time the generator runs, not something this skill invokes separately. |

## When NOT to use this skill

- **The strain already has a `jars/<slug>.py` file.** Logging a run into an
  existing jar is normal run-logging (see `CLAUDE.md` / `Dabby_Handoff_Notes.md`),
  not jar creation — check `jars/*.py` and `jar_manifest.py` first (see step
  1 of the mid-run-logging trigger below).
- **Closing a jar** (moving a slug from `ACTIVE` to `CLOSED` in
  `jar_manifest.py` and updating its prose to closed-jar framing) is the
  close-jar skill (`.claude/skills/close-jar/SKILL.md`).
  Don't extend this skill to do it — closing a jar surfaces different
  questions than opening one.
- **Correcting an existing jar's profile** (a typo, an updated nose
  description, a corrected producer name) is a direct edit to the existing
  file, not a new-jar operation — don't run the full interview for a
  one-field fix.

## Why this is two files, not one

`jars/<slug>.py` holds the strain's profile and (eventually) its runs.
`jar_manifest.py`'s `ACTIVE` list is what actually makes the generator load
it — a jar file with no manifest entry is an orphan the manifest preflight
will flag, and a manifest entry with no file will fail to import. Both edits
happen in the same pass so neither is ever missing on its own.

## Workflow

**1. Gather the strain profile.** Ask for:
- Full strain name, exactly as it should render (e.g. "Lemon Heads + Blueberry Haze")
- Genetics/lineage as reported (parent strains, breeder crosses) — treat this as a starting claim to verify in step 2, not a settled fact
- How many distinct physical strain components are combined in this one jar — ask this directly ("is this one strain, or is more than one strain physically combined in the jar?"), never infer it from a producer's product name. A jar can have 1, 2, or more components (710 Labs alone ships single strains, two-strain "Thumbprint"/"Geode"-style jars, and three-strain "Neapolitan" jars — other producers use entirely different names for the same underlying structures, or invent their own component counts). The name is flavor text; the component count is the fact that determines the info table shape in step 3.
- The actual physical consistency/format of each component (cold cure badder, jam, sauce, live rosin, etc.) — ask for this explicitly and separately from any tier or grade language (see trap below)
- Producer
- Any producer-published tasting notes, if available
- Nose, only if the user has actually smelled the jar — otherwise leave it as "Not yet recorded" rather than guessing

Don't ask about equipment or curve — those aren't jar-level fields. Equipment
is per-run (`CompletedRun.equipment`), and every new jar starts from
`BASELINE_CURVE` per this project's baseline philosophy: strain-specific
curve adjustment happens empirically from swab results, never from strain
name or inferred terpene profile up front.

**Watch for the sourcing-tier trap.** Producers use their own proprietary
words for a "personal reserve" / top-tier sourcing designation — 710 Labs
calls theirs "persy," other producers use other terms entirely. Whatever the
word, it's a sourcing/quality tier, not a physical consistency. If a tier
word comes up, ask what the material actually looks and feels like
(badder, jam, sauce, etc.) as a separate question — don't write the tier
word into a consistency/format field, and don't assume you've seen every
producer's version of this word before. The pattern to catch is "grade
language standing in for a physical description," not any specific word.

**2. Look up the lineage.** A single search-and-skim tends to surface thin,
unreliable snippets for this kind of niche genealogy — worse than not
searching at all if a weak result gets written up as if it were solid. Spawn
a `general-purpose` subagent instead, once per new jar, even when the user
gave a lineage confidently (e.g. off the jar label) — the claimed cross
itself is usually right, but what's more likely to be stale is what that
strain's own ancestry looks like beyond the first generation, which feeds
both the terpene inference in step 4 and the cross-strain check in step 6.

**Don't idle on the handoff.** The agent→agent report delivery has failed
before (first live exercise, July 2, 2026 — the research completed but the
report never came back; details in Provenance below). Once step 1's
gathering and step 3's prep are done, start the inline `WebSearch`/`WebFetch`
fallback in parallel with the same brief and stopping rule — first usable
result wins.

Before writing the brief, read
[`references/lineage_research_bar.md`](references/lineage_research_bar.md).
A real comparison against Perplexity on the same strain showed the gap
wasn't a missing step — it was that the research stopped after a few
generic searches instead of following what they turned up. A longer
checklist doesn't fix that; a subagent can satisfy any fixed list of steps
just as mechanically as it satisfied "run several searches" the first time.
What actually needs conveying is a disposition (keep pulling threads until
that stops teaching you anything) and an accountability mechanism (account
for every thread you didn't chase) — not more boxes to check. Include that
file's stopping rule and accountability check in the subagent's brief
verbatim, along with the worked example, not a summary of them.

Brief the subagent with something like:

> "Research the genetic lineage of the cannabis strain '<strain name>' for a
> session-logging project. The user reports it's <claimed lineage, if any> —
> verify this and trace the ancestry tree as deep as sourcing stays reliable
> (parents, grandparents, further if well-documented), stopping and saying
> so explicitly once sourcing thins out rather than guessing further back.
>
> Source hierarchy — two tiers, not many: the producer's or breeder's own
> site, or a dispensary page clearly quoting them directly, is the sole
> anchor. Everything else — Leafly, AllBud, seed-bank listings, forums,
> wikis, casual mentions — is not evidence on its own, no matter how
> official-looking the site is. Treat every claim from a non-anchor source as
> a lead to verify, not a fact to report: if it names something the anchor
> doesn't cover, or there's no anchor at all, run a follow-up search on that
> specific claim rather than either discarding it for looking unofficial or
> accepting it for looking official. Confidence scales like this: an anchor
> source confirming a claim is solid; multiple independent non-anchor sources
> converging on the same claim (with no anchor available) is corroborated but
> still attributed, not solid; a single non-anchor mention is a lead, not a
> claim, until something else confirms it. If a non-anchor source conflicts
> with the anchor, the anchor wins and the conflict gets reported, not
> averaged away.
>
> This is not a checklist to satisfy — running the minimum searches implied
> and stopping is exactly the failure mode this brief exists to prevent.
> Search for the producer's/breeder's own page specifically (`site:<their
> domain> <strain>`, `"<producer name>" genetics <strain>`) as your first
> move, not a fallback. Producers in this project range from a large,
> well-documented company (710 Labs, this log's single most common producer)
> to small, one-person operations with no web presence at all — don't assume
> either way from the name; let what you actually find set your confidence.
> Finding nothing for a small producer is a normal, complete outcome, not a
> sign to try harder or feel apologetic about it. Stop searching only when
> two searches or fetches in a row add nothing
> you didn't already know — not after a fixed number of queries, and not
> after a fixed number either way regardless of whether that point arrives
> at search 2 (nothing published) or search 12 (a lot published). When a
> result mentions a name, claim, or detail you didn't expect, decide
> explicitly whether to chase it rather than noting it and moving on.
>
> [paste in the stopping rule, accountability check, and worked example from
> references/lineage_research_bar.md here]
>
> Fetch and actually read the most promising pages with WebFetch rather than
> trusting search snippets. Report back in under 500 words: the ancestry
> tree as far as it's reliably sourced, which tier each claim came from,
> your confidence per generation, any unresolved disagreement, and the
> thread-accounting list (every named entity/claim you encountered, pursued
> or not, and why)."

Take whatever the subagent returns as an attributed claim ("per 710 Labs'
own listing, as of this search"), not an established fact — lineage claims
in this industry are frequently disputed or revised, and this project's
epistemic standard already treats genetics-derived terpene inference as a
hedge, not a measurement. If the subagent reports the lineage as unconfirmed
past a certain generation, say so plainly in the terpene note rather than
inferring terpenes from a shaky premise.

**3. Pick the info table shape.** Driven by the component count from step 1,
never by the producer's product name:

| Component count | Info table shape | Reference file |
|---|---|---|
| 1 | `'Strain'` singular, `'Consistency'` row | [`jars/cag.py`](../../../jars/cag.py) |
| 2 or more | `'Strains'` plural, `'Format'` row, a `'{Producer} Notes'` row (only if real tasting-copy text exists — don't add an empty placeholder), a `next_ai_analysis` flagging load position as not reliably distinguishable between components | [`jars/dbrb.py`](../../../jars/dbrb.py) |

For 3+ components, extend the `'Strains'` row to list every component, not
just two. Read the reference files live rather than copying a template here
— that keeps this step matching current convention instead of a static copy
that can drift out of sync with it. Put the producer's specific
product-format name (Thumbprint, Geode, Neapolitan, whatever it's called)
inside the `Format` value as descriptive text — it's never what decides
which shape to use.

**Match wording to precedent when the producer recurs.** Grep `jars/*.py`
for the producer name gathered in step 1. If prior jars from that producer
already exist (e.g. multiple 710 Labs "Close Friends Persy Thumbprint" jars),
read them and match their established phrasing exactly for the format
description, tier language, and any other producer-specific wording, rather
than re-deriving a slightly different version each time. This is the same
"read the live files, not a cached copy" approach as the shape check above —
it stays accurate as those jars evolve instead of drifting out of sync the
way a separately maintained reference file would.

**4. Draft the terpene note.** Read `TERPENE_REFERENCE` in `Dabby_Core.py`
(CONTENTS index near the top of the file points to the line number) and pick
the terpenes that plausibly follow from the lineage gathered and checked in
steps 1–2 — don't invent aroma/compound names. Frame it explicitly as
inference: `"Terpene inference: <compound(s)> inferred dominant from
<lineage> — <why>. Not measured. See Terpene Reference."` This project's
epistemic rule is explicit on this: terpene profiles are inferred from
genetics, never presented as measured specifications — and here the lineage
itself is also a searched, attributed claim, not a verified fact, so the
inference is now two hedges deep. That's fine; say so plainly if the search
turned up disagreement rather than picking whichever source is convenient.

**Labeling mixed-confidence lineage in the info table and terpene note.**
Step 2's research often comes back with several sub-claims (an immediate
cross, then each parent's own parentage) at different confidence levels, not
one flat answer. Ask one question before deciding how to write it up: **is
anything genuinely unknown, or does everything have an answer, just at
different evidence tiers?**

- **Something is genuinely unknown** (no source independently confirms it —
  every mention just repeats one origin claim) → use a short magnitude
  marker in the info-table line, e.g. `2/3 confirmed`, and spell out which
  piece is still open in the terpene note. This tells the reader how much
  of the tree is actually still a question. Real example: Orange Candy's
  lineage had three sub-claims (the immediate cross, and each parent's own
  parentage) — two confirmed via the breeder's own product pages, one
  (Naran J's parentage) genuinely open because every source tracing it
  back led to the same single unverified origin. Info line: `'Orange Candy
  (Philosopher Seeds lineage: Naran J × Tropimango — 2/3 confirmed, see
  terpene note)'`.
- **Everything has an answer, just at different tiers** (e.g. one claim is
  producer-confirmed, another is corroborated by several independent
  sources but not by the producer/breeder itself) → don't use a magnitude
  marker here — it would misleadingly imply something is still missing
  when nothing is. Spell out which claim sits at which tier instead. Real
  example: Papaya + Z Pie #22's Georgia Pie component — the immediate
  cross was producer-confirmed (710 Labs' own copy), and Georgia Pie's own
  parentage was independently corroborated by multiple non-producer
  sources (not a single repeated origin, several agreeing sources) even
  though no producer page confirms it. Info line: `'...Z Pie #22 (Z ×
  Georgia Pie — Georgia Pie: Gelatti × Kush Mints #11, see terpene note)'`,
  with the terpene note distinguishing "confirmed" from "corroborated
  across multiple sources, not producer-confirmed" rather than fractioning
  something that was fully answered, just at a lower evidence tier.

A fraction answers "how much do we know"; a tier label answers "how solid
is what we know." Using the wrong one for the situation either hides an
open question (fraction applied when nothing's actually confirmed at all)
or manufactures a false gap (fraction applied to something fully answered
at a merely-corroborated tier).

**5. Propose a slug.** Derive an abbreviation from the strain name — look at
`jar_manifest.py`'s `ACTIVE`/`CLOSED` lists for the existing range of styles
(`wwz`, `fw106`, `dbrb`, `bp4rw13`, `papzp22`) before proposing one. State the
proposed slug and get explicit confirmation; don't silently commit to it.
Avoid abbreviations that read as something else out of context (this
project's failure-mode log specifically flags "fb" reading as Facebook).

**6. Draft `next_ai_analysis`.** Two to three sentences: confirm the starting
point is `BASELINE_CURVE` — read its current waypoints live from
`Dabby_Core.py` (the provenance grep below is the command); never state the
curve from a copy in this file or from memory —
include the first-run potency caution — keep the load modest until the first
session reads potency; every new jar gets this line, no exceptions
(precedent: the Sour Tangie and LunarZ jars; the instances that earned it:
papzp22 R1's packaging warning discovered post-hoc, dbrb R1's post-session
dizziness after a heavy jar opener). `pending_dab.py brief` also prints this
caution mechanically for any zero-run jar, but the jar copy renders in What
to Try Next where the brief doesn't reach — write both, they're not
redundant —
and note anything from `WISDOM_BRIEF.md` (already read at session open) that's genuinely relevant to a
first run on this genetics/format combination (e.g. a multi-component jar
needs the load-position caveat from step 3). If nothing specific applies,
say so plainly rather than padding — `next_text` stays the boilerplate `'No
runs yet — start from baseline curve'`.

**Check the ancestry tree from step 2 against strains already in the log.**
Grep `jars/*.py` info fields for any ancestor name the research subagent
returned. A hit doesn't establish anything — shared lineage isn't a
mechanism — but it's worth surfacing as a hedged, directional note (e.g.
"shares an OG Kush-family ancestor with Frostbite OG — worth watching
whether similar session character shows up, though shared ancestry doesn't
establish a mechanism"), the same way this project already treats every
other genetics-based claim. Only add this if the subagent's tree actually
reached a shared ancestor with reasonable confidence — don't stretch for a
connection that isn't really there.

**7. Confirm before writing.** Per this project's global rule, present the
full draft — strain name, slug, info table, terpene note, next_ai_analysis —
and wait for explicit approval before touching any file. This is a new
strain's profile going into a shared repo; get it right before it's written,
not after.

**8. Write `jars/<slug>.py`.** Match the structure in `jars/dbrb.py` exactly:
docstring naming the strain and slug, `from datetime import date, datetime,
timezone` + `from Dabby_Core import *` (the only imports the manifest
preflight allows), an empty waypoint-constants comment block, `RUNS = []`,
and the `StrainStatus(...)` block with `profile_anchor='#<slug>-profile'`,
`accent=None`, `next_waypoints=BASELINE_CURVE`, `jar_index=''`.

Writing hazard: the profile prose is full of apostrophes and quotes — if any
HTML lands in a field, use single-quote attributes (`style='...'`), never
escaped double quotes; the Edit tool is documented to convert `\"` into
backslash + curly quote, and the manifest preflight now rejects that
signature. If it happens, fix by byte position with a Python script, not the
Edit tool.

**9. Add the slug to `jar_manifest.py`.** Append it to the end of the
`ACTIVE` list. Per that file's own docstring, "list order within a tier is
display order" — not alphabetical, and appending to the end is the existing
convention (verify: `head -30 jar_manifest.py` — the `ACTIVE` list is not in
alphabetical order). Use the inline comment convention:
`'<slug>',  # Full Strain Name`.

**10. Validate.** Run the project's generate command (`python
Dabby_Log_Generator.py` on Windows) and confirm it completes with no
`VALIDATION ERRORS`, `MANIFEST ERRORS`, `TIER ERRORS`, or `PENDING DABS`
output — this exercises the manifest preflight (including the curly-quote
contamination scan) and `validate()` (including the Layer 0 date,
sessions_prior_today, swab, and read/verdict checks — moot for an empty
`RUNS = []` jar but enumerated here so an unexpected one isn't a surprise)
against the full assembled set, not just the new jar in isolation.

**11. Ship it.** Follow this repo's standard PR workflow from CLAUDE.md —
feature branch (never commit straight to `main`), commit the new jar file,
the manifest edit, and the regenerated `index.html`/`HANDOFF_STATE.md`,
push, open a PR with a plain-English description (e.g. "Added a new jar for
Lemon Heads + Blueberry Haze — no runs yet, starting from baseline curve").
Don't duplicate the PR mechanics here; CLAUDE.md's PR Workflow section is
the source of truth for that.

## When invoked mid-run-logging or from another skill

If this triggers because a run is being logged for a strain with no jar yet,
or because another skill (e.g. a party-mode reconciliation pass) is calling
into this one, use whatever strain details are already known from that
context instead of re-asking for them — only ask for what's genuinely
missing. The output (an empty jar, committed via steps 8–11) is the same
either way; only how much of step 1 (and whether step 2's search turns up
anything new) requires fresh work changes.

**Where party mode lives:** capture is the dab skill
(`.claude/skills/dab/SKILL.md`, "Party mode" section); reconciliation —
the pass where a previously-unlogged strain surfaces and calls into this
skill — is the log-run skill's reconciliation loop
(`.claude/skills/log-run/SKILL.md`). There is no separate `party-mode`
skill directory, by design.

## Provenance and maintenance

Last verified against the repo: 2026-07-02. Everything below was checked
against actual file contents as of that date, not assumed — re-run these if
this skill starts giving results that don't match reality:

```
# Baseline curve values (step 6) haven't changed:
grep -n "^BASELINE_CURVE" -A 5 Dabby_Core.py

# Reference jar files this skill points to still exist and still match the
# shapes described in step 3:
grep -n "info=\[" -A 6 jars/cag.py jars/dbrb.py

# Slugs cited as style examples (step 5) still exist:
grep -n "'wwz'\|'fw106'\|'dbrb'\|'bp4rw13'\|'papzp22'" jar_manifest.py

# Manifest list order is display order, not alphabetical (step 9):
head -30 jar_manifest.py

# The generate command (step 10) is still current:
grep -n "Generate the log" CLAUDE.md

# Whether a party-mode or close-jar skill has since been built (see above):
ls .claude/skills/

# "710 Labs is this log's most common producer" (step 2 brief) still holds:
grep -h "'Producer'" jars/*.py
```

**Step 2 subagent path — first live exercise July 2, 2026 (dogfood test,
dbrb hide-and-recreate, PASS-WITH-FINDINGS):** the nested spawn launched and
its research visibly completed in its own transcript (user-observed), but
the agent→agent handoff **never delivered the report back** despite repeated
retrieval attempts. Caveat on the caveat: this was a two-level test harness
(an agent testing an agent spawning an agent); a normal session has one less
nesting level. The jar that graded PASS was built entirely from the inline
`WebSearch`/`WebFetch` fallback with the same brief and stopping rule. (The
nested agent's report did surface later, delivered to the top-level session
after its parent completed — and its quality matched or exceeded the inline
pass, with anchor-confirmed crosses and full thread accounting. So the brief
produces good research on both paths; only the handoff timing is unreliable.)
Operational rule: spawn the subagent per this skill, but once step 1/3 prep
is done, start the inline fallback in parallel rather than idling on the
handoff — first usable result wins. Test outcome for the record: recreated
jar matched golden on info-table shape, slug, boilerplate, and the
load-position caveat; tier labeling followed this skill's current guidance
(the golden predates it); lineage landed one generation shallower on the
Larry OG branch and deeper on branches the golden skips.
