# Migration Inventory — HANDOFF_WISDOM.md → wisdom/entries/

*Line numbers reference HANDOFF_WISDOM.md at commit 4ae0674 (the migration source, frozen
in git). Tier: L = LIVE, C = COMPRESSED. Worker: transposition model tier (Haiku =
mechanical, Sonnet = clean transposition, Opus = strikes/provenance nuance/new
counter_reading text). Every entry above `observation` needs a `counter_reading`
authored at migration — those all sit in the Opus set.*

## pattern (source: Cross-Strain Patterns table, lines 28–42)

| key | src line | old grade | tier | worker |
|---|---|---|---|---|
| tail-harshness-430 | 28 | High | L | Opus |
| ramp-vs-flat-hold | 29 | Moderate | L | Opus |
| swab-floor-indicator | 30 | High | L | Opus |
| endpoint-effect-strength | 31 | Low | L | Sonnet |
| lower-ceiling-strains | 32 | Moderate | L | Opus |
| harshness-threshold-crossing | 33 | Low | L | Sonnet |
| load-size-effects | 34 | Low | L | Opus |
| bitter-citrus-note | 35 | Low | L | Sonnet |
| cold-cure-fridge-nose | 36 | Low | L | Sonnet |
| draw-count-depletion-proxy | 37 | Moderate | L | Opus |
| bb36-retronasal-blueberry | 38 | Low | L | Sonnet |
| water-sip-reset | 39 | Low | L | Opus |
| descent-limiting-factor | 40 | Low | L | Opus |
| chest-harshness-hot-open | 41 | Low | L | Opus |
| post-session-discomfort | 42 | Low | L | Opus |

## equipment (source: Equipment Observations table, lines 50–54)

| key | src line | old grade | tier | worker |
|---|---|---|---|---|
| rig1-vs-rig2-gemlock | 50 | Low | L | Sonnet |
| rig3-sapphire | 51 | Moderate | L | Opus |
| rig4-sapphire-ruby | 52 | Low | L | Opus |
| rig5-dual-ruby | 53 | Moderate | L | Opus |
| rig6-piston-joystick | 54 | Low | L | Opus |

## failure-mode (source: Failure Modes section, lines 63–89; no grade)

Structurally resolved one-liners (lines 67–75) → COMPRESSED, Haiku:
`fm-utc-run-date` (67), `fm-deploy-race` (68), `fm-rig-labels` (69), `fm-curly-quotes`
(70), `fm-plan-mode-before-pull` (71), `fm-sessions-prior-consistency` (72),
`fm-closed-jar-prose` (73), `fm-equipment-list-position` (74), `fm-boiling-point-reasoning` (75).

Live rows (lines 81–89) → LIVE:

| key | src line | worker |
|---|---|---|
| fm-push-files-content-loss | 81 | Sonnet |
| fm-device-capability-overassert | 82 | Sonnet |
| fm-direct-commit-jar-conflict | 83 | Sonnet |
| fm-doc-sweep-conceptual-miss | 84 | Sonnet |
| fm-baseline-change-protocol | 85 | Opus |
| fm-skill-frontmatter-yaml | 86 | Opus |
| fm-frozen-prose-not-promoted | 87 | Opus |
| fm-bamboo-swab-artifact | 88 | (hand-built, Phase 1 sample) |
| fm-write-gate-doctrine | 89 | Opus |

## decision (source: Decisions table, lines 98–110; no grade; one-line brief render)

All LIVE, Sonnet: `dec-curve-shape-classifier` (98), `dec-read-verdict-superseded` (99),
`dec-read-maps-to-analysis` (100), `dec-rendering-labels` (101), `dec-end-of-jar-framing`
(102), `dec-equipment-schema` (103), `dec-insert-display` (104), `dec-fw106-r4-session-order`
(105), `dec-460-experiment-closed` (106), `dec-wm-dark-gold-second-cycle` (107),
`dec-architecture-doc-deleted` (108), `dec-tail-harshness-pair-hunt-closed` (109),
`dec-matrix-snapshots-frozen` (110).

## theory (source: Methodology State, lines 119–265)

| key | src lines | old grade | tier | worker |
|---|---|---|---|---|
| thermal-model | 119–137 | directional* | L | Sonnet |
| tail-harshness-mechanism | 139–162 | speculative* | L | Opus |
| epistemic-calibration-s99 | 164–171 | n/a → resolution | C | Haiku |
| baseline-philosophy | 173–181 | directional* | L | Opus |
| sapphire-insert-model | 183–190 | observation* | L | Sonnet |
| harm-reduction | 192–209 | directional* | L | Sonnet |
| thermal-injury-vapor-temp | 213–238 | speculative* | L | Sonnet |
| curve-design-theory | 242–265 | directional* | L | Opus |

*Theory sections carry no explicit grade in the old file; the starred values are the
orchestrator's proposed mapping, to be sanity-checked at review. `epistemic-calibration-s99`
compresses: it documents a completed one-time audit whose durable rules already live in
CLAUDE.md's Epistemic Flags.

## Not migrating

- The session-close checklist (old file lines 6–20) → constant in `wisdom_core.py`,
  rendered as the brief's footer.
- Known Claude Failure Modes in `Dabby_Handoff_Notes.md` — different file, out of scope.

Census: 37 full-block LIVE + 13 decision one-liners + 10 COMPRESSED = 60 entries.
