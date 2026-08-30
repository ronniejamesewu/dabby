# Research Layer — Strain Lineage Catalog

Pre-jar knowledge layer: what is known about strains *before* (and independent
of) owning a jar. Written by research sessions (see
`.claude/skills/research-strain/SKILL.md`), consumed at shopping time and by
the new-jar skill at jar-creation time. Not read by the generator; nothing
here renders into `index.html`.

## Files

| File | Holds |
|---|---|
| `strains/<kebab-name>.md` | One entry per purchasable strain/product: what it is, lineage claims with provenance, chain to classics, open questions, sources |
| `lineage_nodes.md` | Shared ancestry nodes (middle-tier cultivars, dead-ends, conflicts) referenced by many strain entries — single source of truth so shared nodes never drift apart across entries |
| `brands.md` | Brand-level metadata: grower/processor roles, business model, market channel, trust notes, key surfaces |
| `SOURCES.md` | The source atlas — which surfaces hold lineage info, by tier. Append-on-discovery |

## Conventions (breaking these corrupts the record)

- **Evidence words** — every claim carries exactly one: `user-direct`
  (told to Eric directly — top tier) · `stated` (the named party published
  it; anchor) · `corroborated` (multiple independent non-anchor sources
  converge; attributed) · `lead` (single non-anchor mention) · `assumed`
  (reasoned default; the reasoning is named) · `undisclosed` (searched,
  nothing published — record date and what was searched) · `conflicted`
  (competing claims recorded verbatim, never averaged) · `dead-end`
  (breeder explicitly declines: clone-only / mystery / tree-widget leaf).
- **Claimant + date on every lineage line.** "Erva states X (IG menu,
  July 18 2026)" — never a bare fact. Anchor tier means *what the party
  says*, not what is biologically true.
- **Parent order is data — never normalize.** Convention is seed parent
  (mother) × pollen parent (father); A×B and B×A can be deliberate
  reciprocal crosses (see Erva's Rainbow Colonel / Rainbow Chem).
- **Symbols verbatim.** `×` = genetic cross; `+` = co-press blend of
  separately washed cultivars (In House's own storefront convention);
  `#N` = pheno selection; "Pheno Wash"/"Mix" = multi-pheno wash. A `+`
  product is a blend, not a strain — it changes the jar's component count.
- **Grower and processor are separate axes** with separate track records;
  lineage claims attach to the grower/breeder side, technique reputation
  to the processor side. Never collapse into a single "producer" unless
  the operation is genuinely one party.
- **Found lineages don't go stale; not-found verdicts do.** An
  `undisclosed` entry records what was searched and when, and invites
  re-running — it is not a permanent answer (the Red Pebbles precedent:
  a clean web not-found was overturned by one IG menu).
- **No name inference, ever.** A lineage guessed from a strain name is
  worse than no answer.
- **Image archiving:** cited IG posts should have their menu slides
  screenshot-archived at capture time (posts and accounts vanish).
  Entries citing unarchived posts say `archive pending`.

## Provenance

Created Aug 30, 2026 from the founding research campaign: 27 strains
(8 Erva × In House collab, 19 In House), two fan-out passes of Sonnet
workers on the raw-read contract plus logged-in Instagram menu reads.
Campaign record lives in the session transcript; per-claim provenance
lives in each entry.
