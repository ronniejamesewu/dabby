---
name: research-strain
description: Research a cannabis strain's lineage, breeder, and grower/processor provenance deeply enough to reason about effects and terpene expression — the shopping-time and pre-jar research workflow for this Dabby project. Trigger when the user is considering buying a jar ("thinking about grabbing X", "what's this strain about", "worth buying?"), asks to research a strain or a drop menu, or names strains from a dispensary drop; also trigger when invoked by the new-jar skill for a strain with no research catalog entry. Writes findings to the research/ catalog (research/strains/, research/lineage_nodes.md, research/brands.md, research/SOURCES.md). Does NOT create jar files (new-jar), log runs (log-run), or touch wisdom entries.
---

# Research Strain

Turns "what is this strain?" into a catalog entry: lineage claims with
provenance, a chain to interpretable classics, and honest dead-ends.
Procedure distilled from the founding 27-strain campaign (Aug 28–30, 2026;
PRs #279 + this skill's introduction PR), including a live A/B retrieval
test and two fan-out worker passes.

## Terms

| Term | Meaning |
|---|---|
| Catalog | The `research/` layer: `strains/<kebab-name>.md`, `lineage_nodes.md`, `brands.md`, `SOURCES.md`. Conventions in `research/README.md` are binding |
| Anchor | The named party's own published words (their site, storefront listing, IG menu, or a page clearly quoting them). Certifies WHAT THEY CLAIM, never biological truth |
| Classics basis | The stop-list in [`references/classics_stoplist.md`](references/classics_stoplist.md) — cultivars whose contribution to effects/taste can be reasoned about directly |
| Done-condition | A tree is done when every leaf is a classic, a documented dead-end, or an honestly-recorded evidence exhaustion — depth is evidence-limited, never fixed-N, but generation 2 must be attempted, not skipped |
| Raw-read contract | WebSearch for discovery only; WebFetch banned (it summarizes pages through a small model and misses JS-rendered content); pages read as raw browser text |

**Two registers.** Machine-side (never user-facing): file paths, slugs,
tool names, "worker/agent/subagent", evidence-word tokens, tabIds.
User-facing: full strain names, plain-English findings ("Erva's own menu
says…", "nobody has published…"), and the betting-line register for
inference.

## Hard rules

- **Never infer lineage from a strain name.** A name reading may be
  recorded as an observation about the name only.
- **Every claim carries an evidence word + claimant + date** per
  `research/README.md`. Anchor tier = what the party says. Conflicts are
  recorded verbatim, never averaged or majority-voted.
- **Parent order and symbols verbatim** (`×` cross / `+` co-press blend /
  `#N` pheno / "Pheno Wash"). A×B ≠ B×A (possible reciprocal crosses).
- **Lineage claims attach to the grower/breeder axis; technique
  reputation to the processor axis.** Never collapse them.
- **WebFetch is banned** for all lineage reads — workers and main session.
- **Instagram is main-session only** (user's logged-in Chrome). Workers
  record IG post URLs/handles as leads — a surfaced URL is a win.
  Following a private account, DMing, or commenting is the user's action
  on the user's account — surface it as a suggestion, never do it.
- **Found lineages persist; not-found verdicts expire.** An undisclosed
  verdict records what was searched and when.
- **Database register in catalog files.** Entries are public and read by
  a terse community: facts, source, date — no editorializing, no process
  narration, no hype/demand notes, inference as one short labeled line
  at most (see the register rule in `research/README.md`). Analysis and
  interest reads belong in conversation, never in the entries.
- Catalog writes go through the standard PR workflow — never straight to
  main.

## When NOT to use

- **Creating the jar file** for a strain — that's new-jar
  (`.claude/skills/new-jar/SKILL.md`), which calls into this skill when
  no catalog entry exists.
- **Logging a run** — log-run.
- **Terpene/effects questions about an already-cataloged strain** — read
  its catalog entry first; re-run this skill only if its open questions
  or staleness warrant.

## Workflow

**1. Catalog check.** `Glob research/strains/*.md` and read any entry for
the target (and `research/lineage_nodes.md` for its parents). Fresh found
entry → skip to step 6. Not-found entry → note what was already searched;
re-run only the gaps. Missing → continue.

**2. Context gathering.** Producer/grower/washer as the user knows them
(their wording, e.g. "grown by X, washed by Y", is the axes). Read
`research/brands.md` for the brands involved and `research/SOURCES.md`
for the surfaces and hazards. New brand → its entry gets drafted in step 7.

**3. Public-web pass — Sonnet workers on the raw-read contract.** Spawn
`general-purpose` subagents, `model: sonnet` explicitly (never inherit
silently), batched ~4–6 strains per worker for sweeps, or nodes-per-worker
for ancestry passes. The brief must include, verbatim or equivalent:
- The research bar: stopping rule, accountability check, worked examples —
  paste from [`references/lineage_research_bar.md`](references/lineage_research_bar.md).
- The source hierarchy (anchor vs lead vs corroborated) and the
  grower-axis rule.
- The termination rule with the classics stop-list pasted in.
- Known leads from the catalog (breeder partners, storefronts, prior
  findings) so workers extend rather than re-derive.
- Name-collision warnings specific to the targets.
- Retrieval tooling, exactly: WebSearch discovery only; WebFetch banned;
  browser reads via ToolSearch-loaded
  `mcp__Claude_Browser__tabs_create` / `navigate` / `get_page_text`;
  tabs_create ONCE, own tabId passed on EVERY call (parallel workers
  share the browser); close own tab; never fall back to WebFetch.
- Report format: per-strain/per-node findings with tier + confidence,
  IG leads, thread accounting, methods note.

**4. Recurse to the done-condition.** Dedupe leaf nodes across targets
(shared parents collapse — resolve once in `lineage_nodes.md`), then run
an ancestry pass on the unresolved cohort. Generation 2 must be attempted.
Classify every terminal: classic / documented dead-end / evidence
exhausted / conflicted.

**5. Instagram pass — main session, user's Chrome.** For nodes the web
left open: producer and breeder accounts' drop menus and grids (menus
carry lineage lines under strain names). Screenshot menus with
`save_to_disk` where the renderer cooperates — posts and accounts vanish;
the archive may become the only surviving anchor. Private accounts: read
the bio (often informative), then suggest the follow to the user.

**6. Synthesis — the part the user actually wants.** Express the strain
in the classics basis: lineage tree with tiers → terpene-expression
inference (labeled as inference from genetics per the project's epistemic
flags; terpene inheritance segregates rather than averages — see
[`references/domain_priors.md`](references/domain_priors.md)) → effects
prior → interest read cross-referenced against the user's own jar history
(the log is the ground truth for how they respond to known genetics).
Interest reads talk like a betting line, conditional on the claims
("if the Mazar × GMO claim holds…"), never like a review.

**7. Write the catalog.** New/updated `research/strains/<kebab-name>.md`
per the conventions; shared parents into `lineage_nodes.md` (never
duplicated into strain files); brand deltas into `brands.md`; newly
discovered productive surfaces appended to `SOURCES.md`. Then feature
branch, commit, PR per CLAUDE.md.

## Recovery paths (don't improvise these)

- **Worker orphaned by a session restart** (task notification says
  stopped/no completion record) — SendMessage the same agent id to
  resume; its transcript survives. Tell it to recreate its browser tab.
- **Browser renderer timeout** (`Page.captureScreenshot timed out`) —
  retry the call solo (not in a batch); the flake is intermittent.
- **Cloudflare / age-gate walls** — note and move on; the info usually
  exists on another surface (see SOURCES.md hazards).
- **Two anchors conflict** (e.g. producer menu vs breeder retail listing)
  — the producer's claim wins *for that producer's jar*; the conflict is
  recorded in the entry's Open questions, not resolved by fiat.
- **A plausible identification from catalog adjacency** (name ≈ a known
  cultivar) — record as corroborated/lead at best; the Amalfi precedent
  (see `research/strains/amalfi.md`) is the canonical overturn.

## Provenance and maintenance

Created Aug 30, 2026, from the founding 27-strain campaign (Erva × In
House collab + In House catalog): A/B retrieval test (WebFetch vs raw
reads, Red Pebbles), two 4-worker fan-out passes, logged-in IG menu
reads. Done-condition ("classics basis frontier") set by Eric Aug 30.

```
# catalog layer exists and conventions doc is present:
ls research/README.md research/strains/ research/lineage_nodes.md research/brands.md research/SOURCES.md

# new-jar delegates here (step 2 should reference research-strain):
grep -n "research-strain" .claude/skills/new-jar/SKILL.md
```

Dogfood-test status: **Executed end-to-end Aug 31, 2026** — 10 strains
(Erva/In House drop menus), same session as authoring. Result: all ten
anchored; 1 strain fully terminated at entry from existing shared nodes
(Blockberry); 2 identified as repackaged breeder releases (Garlic Drip =
Bloom's, Peach OZ = Dying Breed's); 1 worker instead of the founding
campaign's 8. Findings folded back: steps 3/5 may reorder when the
session already knows which anchor surface holds the answer (IG-first is
correct when the producer's menus are the known source); producer
credit-comments are an anchor class (now in SOURCES.md); menu-image
archiving remains aspirational — no save_to_disk archive was captured
this run either (renderer flake + flow cost), so `archive pending`
accumulates as debt.
