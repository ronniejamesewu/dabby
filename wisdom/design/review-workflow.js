export const meta = {
  name: 'wisdom-migration-review',
  description: 'Adversarial per-entry review of the wisdom migration against source',
  phases: [{ title: 'Review', detail: 'two-direction drift check per entry' }],
}

const FLAGS = {
  'tail-harshness-430': "Worker flags: papzp22 R6 / sourtangie R2 counters had no provenance tag in source, defaulted ai-authored. July 11 audit 'tightened citations' (hive1 R2/R3/R4, mbd R1/R2/R3, rainfruit R1) placed as role='struck'; rainfruit R1 and hive1 R3-R4 arguably read as genuine counter-evidence rather than strikes — adjudicate struck-vs-counters.",
  'swab-floor-indicator': "Worker flags: WW Z R5/R6 provenance defaulted ai-authored here, but WW Z R6 is tagged user-verbatim in the adjacent tail-harshness row (old line 28) — check whether ai-authored understates it.",
  'load-size-effects': "Worker flags: bb362 R4, wwz R5/R6, lhbh R3/R4 provenance defaulted ai-authored. Optional counter_reading added at observation grade drawn from the row's own split-direction language — keep or drop?",
  'draw-count-depletion-proxy': "Worker flags: source does not pin which of FW106 R6/R10 was first vs last dab — cited with shared clause. All provenance defaulted ai-authored.",
  'water-sip-reset': "Worker flags: LunarZ R3 (partial reduction) and Sour Tangie R5 (non-response) mapped role='counters' though the source cites all eight as instances of the phenomenon — adjudicate counters-vs-context.",
  'chest-harshness-hot-open': "Worker flags: papzp22 R7 marked mixed; lunarz R1 marked user-verbatim on a short quote; sourtangie R7 left ai-authored despite explicit user attribution without verbatim quote. counter_reading authored fresh.",
  'post-session-discomfort': "Worker flags: all 9 confirming instances provenance-defaulted (WM R1 mixed). FW106 R11/R12 and Hive1 R13/R14 split from grouped source instances; the R11-vs-R12 quote-to-run assignment is assumed — verify against the source text.",
  'rig1-vs-rig2-gemlock': "Worker flags: Position 1 has no date visible in source — stated='undated in source'. Check nothing better was available.",
  'rig3-sapphire': "Worker flags: all five citations provenance-defaulted; counter_reading authored fresh from the row's own load/tolerance confounds — check it doesn't overstate.",
  'rig5-dual-ruby': "Worker flags: evidence-cell run ranges (WM R2-R4, FW106 R18-R19, R11-R12, eleven-runs cluster) collapsed to one Citation each anchored on first-named run with full list in gist — verify no run got lost in collapsing.",
  'fm-baseline-change-protocol': "Worker flags: 'When' cell cites git commit d5ab834 — mapped to session: form. Adjudicate.",
  'fm-frozen-prose-not-promoted': "Worker flags: papzp22 R1 packaging-note quote provenance defaulted ai-authored — check.",
  'fm-write-gate-doctrine': "Worker flags: Conditions-column mechanism with its verbatim gate-language quotes exceeded the claim cap and was preserved as the first Position instead — verify placement lost nothing.",
  'tail-harshness-mechanism': "Worker flags: cross-run pairs (LHBH R3/R4, BB36#2 R2/R3, FW106 R23-vs-R5, R4-to-R6, R15, Hive R9/R10 R13/R14, row-B runs) placed in positions not evidence, so they don't appear in citation counts — verify all pair text survived verbatim. Provenance defaulted throughout; sourtangie R3 mixed.",
}

// key, source lines in HANDOFF_WISDOM.md, model, effort
const E = [
  ['tail-harshness-430','26-28','opus','high'],
  ['ramp-vs-flat-hold','26-27,29','opus','high'],
  ['swab-floor-indicator','26-27,30','opus','high'],
  ['endpoint-effect-strength','26-27,31','opus','high'],
  ['lower-ceiling-strains','26-27,32','opus','high'],
  ['harshness-threshold-crossing','26-27,33','opus','high'],
  ['load-size-effects','26-27,34','opus','high'],
  ['bitter-citrus-note','26-27,35','opus','high'],
  ['cold-cure-fridge-nose','26-27,36','opus','high'],
  ['draw-count-depletion-proxy','26-27,37','opus','high'],
  ['bb36-retronasal-blueberry','26-27,38','opus','high'],
  ['water-sip-reset','26-27,39','opus','high'],
  ['descent-limiting-factor','26-27,40','opus','high'],
  ['chest-harshness-hot-open','26-27,41','opus','high'],
  ['post-session-discomfort','26-27,42','opus','high'],
  ['rig1-vs-rig2-gemlock','48-50','opus','high'],
  ['rig3-sapphire','48-49,51','opus','high'],
  ['rig4-sapphire-ruby','48-49,52','opus','high'],
  ['rig5-dual-ruby','48-49,53','opus','high'],
  ['rig6-piston-joystick','48-49,54','opus','high'],
  ['fm-baseline-change-protocol','79-80,85','opus','high'],
  ['fm-skill-frontmatter-yaml','79-80,86','opus','high'],
  ['fm-frozen-prose-not-promoted','79-80,87','opus','high'],
  ['fm-write-gate-doctrine','79-80,89','opus','high'],
  ['thermal-model','119-137','opus','high'],
  ['tail-harshness-mechanism','139-162','opus','high'],
  ['baseline-philosophy','173-181','opus','high'],
  ['sapphire-insert-model','183-190','opus','high'],
  ['harm-reduction','192-209','opus','high'],
  ['thermal-injury-vapor-temp','213-238','opus','high'],
  ['curve-design-theory','242-265','opus','high'],
  ['fm-push-files-content-loss','79-81','sonnet','medium'],
  ['fm-device-capability-overassert','79-80,82','sonnet','medium'],
  ['fm-direct-commit-jar-conflict','79-80,83','sonnet','medium'],
  ['fm-doc-sweep-conceptual-miss','79-80,84','sonnet','medium'],
  ['fm-bamboo-swab-artifact','79-80,88','sonnet','medium'],
  ['dec-curve-shape-classifier','96-98','sonnet','medium'],
  ['dec-read-verdict-superseded','96-97,99','sonnet','medium'],
  ['dec-read-maps-to-analysis','96-97,100','sonnet','medium'],
  ['dec-rendering-labels','96-97,101','sonnet','medium'],
  ['dec-end-of-jar-framing','96-97,102','sonnet','medium'],
  ['dec-equipment-schema','96-97,103','sonnet','medium'],
  ['dec-insert-display','96-97,104','sonnet','medium'],
  ['dec-fw106-r4-session-order','96-97,105','sonnet','medium'],
  ['dec-460-experiment-closed','96-97,106','sonnet','medium'],
  ['dec-wm-dark-gold-second-cycle','96-97,107','sonnet','medium'],
  ['dec-architecture-doc-deleted','96-97,108','sonnet','medium'],
  ['dec-tail-harshness-pair-hunt-closed','96-97,109','sonnet','medium'],
  ['dec-matrix-snapshots-frozen','96-97,110','sonnet','medium'],
  ['epistemic-calibration-s99','164-171','sonnet','medium'],
  ['fm-utc-run-date','63-67','sonnet','medium'],
  ['fm-deploy-race','63-65,68','sonnet','medium'],
  ['fm-rig-labels','63-65,69','sonnet','medium'],
  ['fm-curly-quotes','63-65,70','sonnet','medium'],
  ['fm-plan-mode-before-pull','63-65,71','sonnet','medium'],
  ['fm-sessions-prior-consistency','63-65,72','sonnet','medium'],
  ['fm-closed-jar-prose','63-65,73','sonnet','medium'],
  ['fm-equipment-list-position','63-65,74','sonnet','medium'],
  ['fm-boiling-point-reasoning','63-65,75','sonnet','medium'],
]

const SCHEMA = {
  type: 'object',
  properties: {
    key: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', enum: ['high', 'medium', 'low'] },
          old_quote: { type: 'string' },
          new_state: { type: 'string' },
          why: { type: 'string' },
        },
        required: ['severity', 'old_quote', 'new_state', 'why'],
      },
    },
    notes: { type: 'string' },
  },
  required: ['key', 'findings'],
}

phase('Review')
log(`Reviewing ${E.length} migrated entries against source`)

const results = await parallel(E.map(([key, lines, model, effort]) => () => {
  const flag = FLAGS[key] ? `\n\nThe transposition worker self-flagged judgment calls on this entry — adjudicate each explicitly in your notes:\n${FLAGS[key]}` : ''
  return agent(
`You are an adversarial migration auditor for the Dabby project (repo root /home/user/dabby). One wisdom entry was migrated from markdown to a typed Python file under a strict contract: TRANSPOSITION, NOT CONDENSATION — evidence prose moves verbatim; only claim/guidance/grade_basis/watch_for/counter_reading are newly authored, and those must be faithful distillations that never upgrade or downgrade the source's confidence.

Inputs:
1. Read /home/user/dabby/wisdom/design/TRANSPOSITION.md — the contract and field semantics.
2. Read the SOURCE: /home/user/dabby/HANDOFF_WISDOM.md line(s) ${lines} (ground truth).
3. Read the RESULT: /home/user/dabby/wisdom/entries/${key}.py

The failure mode you hunt is narrative-seeking drift during re-containering. Run BOTH directions explicitly:
- PASS A (claims inflated): does any newly authored field state more than the source supports? Did any confound, hedge, or qualifier present in the source vanish or soften?
- PASS B (counter-evidence cleaned): does any countering instance read stronger than the source recorded? Were weaknesses OF counter-instances (their own confounds, provenance softness) dropped?

Also verify: verbatim-moved prose is actually verbatim (meaning-changing paraphrase is a finding); every source citation is present with a faithful role (confirms/counters/context/struck); strike annotations survived with reason and date; retired/superseded framings survived AS retired, with their retirement notes; grade mapping follows Low->observation, Moderate->directional, High->tested; nothing in the new file lacks a basis in the source. Restructuring itself is approved and NOT a finding (containers, field names, prose split across citations/positions, brief terseness).${flag}

Report via structured output: key='${key}', findings=[] if clean (each finding: severity, verbatim old_quote, what the new file says or omits as new_state, why it changes the epistemic picture), notes for flag adjudications and anything you checked that deserves a remark. Do not edit any file.`,
    { label: `review:${key}`, phase: 'Review', model, effort, schema: SCHEMA }
  )
}))

const done = results.filter(Boolean)
const withFindings = done.filter(r => r.findings && r.findings.length > 0)
const high = withFindings.flatMap(r => r.findings.filter(f => f.severity === 'high').map(f => ({ key: r.key, ...f })))
return {
  reviewed: done.length,
  attempted: E.length,
  entries_with_findings: withFindings.length,
  high_severity: high,
  all: done,
}