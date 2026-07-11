# Wisdom-Layer Audit — Evidence Matrix (snapshot 2026-07-11)

> **FROZEN ARTIFACT — data current through July 10, 2026 (last run at snapshot time).**
> Jar files in `jars/*.py` are the single source of truth. This matrix is a
> point-in-time extraction. **Before citing any cell, follow its `jars/<slug>.py:<line>`
> anchor and confirm against the live jar file** — line anchors and content
> both drift as runs are logged and frozen data is corrected. Treat this the
> way the project treats any frozen record: historical, correctable by
> exception, never the operational source.

## What this is

A per-run structured extraction of all 144 runs across 20 jars, produced by
the orchestrator/worker wisdom audit run on July 11, 2026 (the last day of
Fable-class availability). Twenty extraction workers each converted one jar
file into verbatim-quoted, line-anchored, source-field-tagged evidence rows;
the orchestrator verified every proposed wisdom change against primary prose,
and a clean-context adversarial reviewer attacked the result before it shipped.

## Files

- `SCHEMA.md` — the extraction contract the workers followed (verbatim quotes
  only, anchors on every cell, explicit `not stated`, source-field tags, no
  interpretation). This is the reusable part: re-run it against runs logged
  after July 10 to extend or diff the matrix.
- `<slug>.md` — one file per jar, per-run blocks.
- `PROPOSAL.md` — the audit's proposed wisdom-layer changes (P1–P8), each
  with counter-reading and adversarial-review status, plus the holds-up list
  and experiment portfolio. Retained as the record of what this audit
  concluded and why. The changes themselves were applied to
  `HANDOFF_WISDOM.md` and four jar `STATUS` blocks on the same PR.

## The one durable-value layer

Most of what makes this matrix queryable — dates, rigs, curves, session order,
raw dab_notes/session_char text — is mechanically derivable from the jar files
with a script and never goes stale. Only two layers actually needed model
judgment and don't cheaply regenerate:

1. **Provenance tags** — user-verbatim (`dab_notes`) vs. AI-authored
   (`analysis`/`session_char`/`endpoint_note`) on every experiential claim.
   This is what the audit repeatedly tripped over (load classes hiding in AI
   fields; a High row certified on "user-verbatim" evidence that mostly
   wasn't).
2. **Harshness facet decomposition** — onset / location / persistence /
   escalation split into separate fields. This is what made the
   chest-harshness row's conflation visible.

See the backlog item "Mechanical run-facts dump script" for the always-fresh
answer to the derivable layer. This snapshot exists for the judgment layer and
for diffing against the next audit.

## Re-running

See `.claude/skills/wisdom-audit/SKILL.md` for the full re-run procedure.
