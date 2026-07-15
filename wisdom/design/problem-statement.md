# Wisdom Layer Redesign — Problem Statement

## What this layer is

An AI-maintained knowledge layer for a dab-session logging project: the accumulated synthesis of what the project has learned across runs and jars. Its content units are claims and positions of varying maturity — graded by confidence, backed by cited run evidence where citations carry per-instance confounds and a provenance tag distinguishing the user's verbatim words from AI-authored records, and revisable in place as understanding evolves, up to and including outright supersession. Some units are terse and stable; others are long-form evidence prose that grows with every relevant run. Primary run data lives elsewhere (one Python file per jar, never edited after the fact); this layer is synthesis over that data, edited at session close.

## What's failing

- The layer is a single markdown file and one of three mandatory session-open reads. It is ~84k chars / ~31k tokens — past the Read tool's 25k single-pass cap, so the mandatory read now requires paging, which is the precondition for the documented "answered from a partial read" failure the mandatory-read gate exists to prevent.
- A consolidation pass on July 3, 2026 cut it 90.9k → 63.3k chars. It regrew ~20k chars in ten days. Nothing watched: the regrowth was noticed by accident when a Read call paged. Any fix that is only a cut has empirically failed once already.
- The three mandatory reads together cost ~50k tokens of context at every session open, regardless of session type. For a run-logging session most of it is load-bearing; for an infrastructure or design session, maybe a third is. The cost function is context spent per session, not just file size.
- The heaviest content units are evidence essays of 3,000–3,800 chars each, currently living inside markdown table cells — a container hostile to structured prose.

## Growth mechanisms (diagnosed, must each be answered structurally)

1. **Citation accretion** — evidence-backed entries enumerate every confirming/countering run with a per-instance confound; the busiest carry 8+ instances across up to 6 strains.
2. **Provenance layer** — a July 2026 audit added per-citation user-verbatim vs. AI-authored tagging after untagged citations were found laundering AI-authored data as user observations. This is deliberate, load-bearing weight — the design must accommodate it, not trim it.
3. **Append-log prose** — long-form positions accrete a new dated paragraph per notable run rather than folding into prior text.
4. **Supersede-in-place** — retired framings are kept in full under their own retraction notes rather than removed.

The design must say, for each: where the next instance goes, and what bounds the growth of anything read unconditionally.

## Consumers and read moments

- **Session open, every session, any type** (the expensive one): needs awareness of what has been learned and at what confidence, what operational hazards are live, and what has been settled — enough that the session doesn't hallucinate, re-derive, or re-litigate. Does *not* need instance-level evidence.
- **Drafting per-run analysis** (frequent): needs the relevant claims, their confidence, and strongest evidence; instance-level detail only when citing or comparing closely.
- **Session-close edits** (frequent): updating an entry needs that entry's full evidence list and provenance. Edits must stay cheap — this happens most sessions.
- **Confidence promotions** (occasional): require full evidence plus a stated counter-reading.
- **Full audit** (rare): re-derives entries from primary run data; reads everything.

## Requirements

1. **Bounded unconditional surface.** Whatever every session must read fits one Read call with real headroom, and its size does not grow with instance count. The designer proposes and justifies the target.
2. **Zero information loss.** Instances, confounds, provenance tags, counter-evidence, supersession history all survive somewhere. Growth pressure is legitimate; the architecture absorbs it rather than periodically fighting it.
3. **Deterministic read triggers.** On-demand detail is keyed, with rules a fresh session can execute mechanically ("editing entry X → open X's detail first"), not vibes.
4. **Mechanical enforcement.** Size and structural invariants are checked by code at generate time and fail loudly. Regrowth of the unconditional surface must be impossible to miss for ten days.
5. **No drift between layers.** If a summary and its detail are separate artifacts, divergence must be either structurally impossible (generated) or mechanically caught. Discipline-only rules have a documented failure record in this project.
6. **Cheap session-close writes.** The routine edit path can't require heavy tooling or ceremony.
7. **Enumerated blast radius.** The layer is referenced by the project instructions file's session-start gate, two workflow skills, a session-close checklist, and an audit skill. The design lists every surface it touches. Known hazard: literal-filename greps miss conceptual workflow descriptions; the sweep must check meaning, not just names.
8. **Reviewed migration.** Any pass that condenses or restructures evidence prose goes through a clean-context adversarial diff review before merge — project rule with three confirming incidents behind it.

## House precedent

The project already solved unbounded growth once, for run data. Three ingredients, all load-bearing: a bounded always-read summary that is *generated*, never hand-maintained; detail sharded into keyed files with a deterministic open-when-named rule; and validators plus a manifest preflight so structural mistakes fail the build instead of shipping. Also in-house: a two-tier compression pattern (active entries in full; resolved ones as one-liners with full history left in git) that has kept one fast-growing category flat for weeks.

## Deliverables

Artifact layout; read policy per moment above; the session-close edit workflow; the enforcement spec; a migration plan; the touched-surfaces list; and an explicit answer to "what stops regrowth" for each of the four growth mechanisms.

## Anti-anchoring terms

The designer receives this statement plus a few content samples spanning the range of entry shapes and sizes — not the current file, its section list, or its table of contents. The incumbent organization is not a requirement. Content may be regrouped, merged, or given different homes wherever the requirements are better served. Nothing earns a place by already existing; retiring content to git history with a pointer is an allowed move where the requirements tolerate it.
