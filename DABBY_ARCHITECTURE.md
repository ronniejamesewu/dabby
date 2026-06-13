# Dabby — Target Architecture

## What This Document Is

A first-principles design for the Dabby session log system, treating the current
codebase as a proven prototype. It describes the target architecture, the reasoning
behind it, and a step-wise implementation plan. Each step is independently mergeable
and leaves the system in a better state than it was.

This document supersedes `REFACTOR_TEMPLATE_DRIVEN.md`. Do not execute that plan —
the schema design is wrong in ways documented below. (`REFACTOR_TEMPLATE_DRIVEN.md`
was deleted in Session 34.)

---

## Live Status

**Steps 1–4 are done. Steps 5–6 remain.** This document is now primarily a
reference for the target architecture (Data Model, Generator, Handoff, Guardrails,
Workflow below). The session-by-session execution narrative that used to lead this
file has been moved to **History — Execution Log** at the end.

**Remaining work:**
- **Step 5 — Workflow Simplification.** Make the PR workflow optional for routine
  run logging (local-first review). *Gated by C3 below.*
- **Step 6 — CLAUDE.md User Configuration Block.** Extract user-specific values
  (timezone, device, insert, technique) into a single configurable section.

**Open question:**
- **C3 — "PR workflow optional."** The PR preview is also the content-loss tripwire
  and the structural enforcement of propose-don't-narrate, in a project with two
  logged content-loss incidents. Any local-first path needs a mandatory
  rendered-diff review gate with teeth, not a soft visual check. C3 gates Step 5.

See **History — Execution Log** for how Steps 1–4 were executed and for the
resolved questions (B4, N2, N5, C1, C2).

---

## Current State

**What exists and works:**
- **Per-jar architecture (Session 108):** `Dabby_Core.py` (dataclasses, `RIG_N`,
  `BASELINE_*`, `GLOBAL_INFO`, `TERPENE_REFERENCE`, color resolution, parameterized
  `validate`/`validate_accent_colors`) + `jars/<slug>.py` (one file per jar, each
  exporting `RUNS` + `STATUS`) + `jar_manifest.py` (`ACTIVE`/`PAUSED`/`CLOSED` tiers
  and `load_all_jars()`) + `Dabby_Log_Generator.py` (rendering). This supersedes the
  former `Dabby_Data.py` / `Dabby_Archive.py` split (PR #109), which is retired —
  closed jars are now jar files in the `CLOSED` tier, not a separate archive module.
- Dataclasses: `Waypoint`, `Insert`, `CarbCap`, `Pearl`, `EquipmentConfig`, `CompletedRun`, `StrainStatus`, `TerpeneEntry`
- Dormancy lifecycle: `_check_dormancy()` prints advisory notices (21-day threshold); archiving/reactivation is a slug move in `jar_manifest.py`
- Dashboard, strain browser, collapsible run sections, Chart.js curves
- GitHub Actions: deploy on push to main, preview URL on PR
- 86 logged runs across 13 strains with runs (17 jar files total: 15 active incl. 4 status-only placeholders, 2 closed)

**Structural debt:**

1. ~~**Run content lives in the renderer, not in the data.**~~ **RESOLVED Session 43.** All `CompletedRun` and `StrainStatus` content fields populated. Adding a run requires editing only `Dabby_Data.py`.

2. ~~**`build_html()` enumerates strains instead of iterating over them.**~~ **RESOLVED Session 43.** The target `for ss in STRAIN_STATUS:` loop is live. No strain names in the generator.

3. **The generator token count.** ~~32K tokens~~ → Step 1 (Session 36): 25,479 tokens; → **Step 3 (Session 43): ~5.8K tokens — well under the 25K single-pass limit.**

4. **Equipment state is global and static.** `GLOBAL_INFO` describes the current
   rig configuration, but "current" is not always the same as the configuration used
   in any given run. Equipment can change and revert. Prior runs may have used a
   different joystick, insert, or pearl configuration. This is unstructured and
   unqueryable.

5. ~~**The handoff conflates two different kinds of content.**~~ **RESOLVED Session 45.** `HANDOFF_STATE.md` is generated from `Dabby_Data.py`; `HANDOFF_WISDOM.md` holds AI-authored wisdom in structured tables; `Dabby_Handoff_Notes.md` retains operational notes only.

6. **`REFACTOR_TEMPLATE_DRIVEN.md` moves rendering metadata into the data layer.**
   It adds `amber`, `curve_label`, `results_header`, `curve_header` (raw HTML) to
   `CompletedRun`. These are presentation concerns, not data concerns. Moving them
   into the data layer trades one coupling for another rather than eliminating it.
   The correct move is to store semantic facts in data and derive presentation from
   them in the generator.

---

## Removed Capabilities

**Per-strain terpene tables (`terpene_table_rows` / `terpene_table_note`).** Removed alongside the introduction of `Dabby_Archive.py`. `StrainStatus` previously carried two optional fields for rendering a strain-specific terpene table; only MB9ZST used them, and the `terpene_table_note` openly stated "This is the generic cannabis palette" — the same five-terpene reference every strain implicitly carries, dressed up as Neapolitan-specific. The epistemic flags in `CLAUDE.md` already disclaim per-strain terpene profiles as inferred, not measured; rendering a strain-labeled table of the generic palette was content that contradicted those flags. All nine other strain-specific `*_TERPS` arrays were dead code (orphaned by Step 3's migration to prose `terpene_note`). Net deletion: ~50 lines plus two dataclass fields.

**To re-add if a strain with genuinely measured terpene data appears:** add `terpene_table_rows: list[tuple] | None = None` and `terpene_table_note: str = ""` back to `StrainStatus`, and restore the rendering block in `render_strain_profile()` (between `info_table` and the `terpene_note` paragraph). The conditional `if ss.terpene_table_rows is not None:` keeps it dormant for strains without measured data, so the existing prose `terpene_note` field continues to serve everyone else.

---

## Architecture Principles

**1. Data carries semantic content, not rendering metadata.**

The data layer records what happened and what it meant. The generator decides how
to present it. A run knows it was `too_hot: True`. The generator decides that
`too_hot=True` renders in amber. If the color scheme changes, touch the generator,
not every run entry.

**2. The generator iterates, never enumerates.**

`build_html()` must contain no strain names. It loops over `COMPLETED_RUNS` and
`STRAIN_STATUS`. Adding a new strain or run is a data change, not a code change.

**3. Equipment state is per-run context.**

Equipment can change and revert between runs. Each run happened against a specific
configuration. That configuration is part of the run's record and is required for
correct comparison between runs.

**4. Run analysis is historically stable.** *(RESOLVED Session 41 via N5 — see
the Session 41 note in Status & Re-opened Questions.)*

The analysis field on a `CompletedRun` records the state of understanding at the
moment it was written. It is frozen (correctable by exception when genuinely
wrong, not silently revisable when the AI changes its thinking) **and rendered
read-only in that run's own section** as permanent in-run history. It is *not*
the source of the strain's current "What to Try Next" — that renders from the
revisable `StrainStatus.next_*` fields. Historical record (frozen, in-run) and
current recommendation (revisable, strain-level) are different things sourced
from different places. Mid-session guidance changes not backed by a new run go
to `StrainStatus.next_*`, never into a prior run's frozen `analysis`.

**5. Analysis synthesizes; it does not react.**

A run's analysis is not a response to that run in isolation. It is a synthesis of:
- Full strain history (all prior runs and their analyses for this strain)
- Cross-strain patterns documented in the wisdom layer
- Equipment state for this run and how it compares to prior runs
- Any emerging cross-log patterns not yet formalized in the wisdom layer

"What to Try Next" tracks the accumulated state of understanding about a strain,
not a prescription. A run that doesn't follow the prior suggestion is not a
deviation — it is more data. Run N's analysis remains part of the context for
Run N+1's analysis regardless of whether Run N+1 followed Run N's suggestion.

**6. The handoff has two distinct layers with different authors.** *(The
state/wisdom split stands; the **append-only** structure of the wisdom layer is
re-opened — see C2 in Status & Re-opened Questions.)*

- **State layer:** derived from data, generated by a script. Current run counts,
  last dates, pending next directions (from last run's analysis per strain).
  No AI authorship required. Never goes stale as long as the data is current.

- **Wisdom layer:** AI-authored at session close. Cross-strain patterns, equipment
  hypotheses, failure modes, methodology constraints. Cannot be generated from data.
  Structured as append-only tables so contributions are traceable and confidence
  levels are explicit.

**7. Local-first workflow; GitHub as optional delivery.** *(Re-opened — see C3 in
Status & Re-opened Questions. The PR preview is also a content-loss tripwire;
recommended that PR stays the default at least through Step 3.)*

The core operation — structured data → rendered HTML — is a local computation.
It requires Python and a filesystem. Nothing else. The PR preview workflow was
designed for an API-only environment where local rendering was impossible; in
Claude Code that constraint is gone. The standard session workflow requires no
network operations. GitHub remains the correct tool for larger changes (refactors,
UI work) where preview and audit trail are valuable.

---

## Target Data Model

### `EquipmentConfig`

```python
@dataclass
class Insert:
    brand: str       # "Dr. Dabber", "OM Quartz", etc.
    model: str       # "stock", "Sapphire Plus (v2)", etc.
    material: str    # "quartz", "sapphire"

@dataclass
class CarbCap:
    brand: str       # "Cloud Vortex", "Gemcup Glass"
    model: str       # "21.0", "Gemlock joystick"
    airflow: str     # "stock" by default — variant string when known

@dataclass
class Pearl:
    diameter_mm: int
    material: str    # "quartz" — future materials TBD

@dataclass
class EquipmentConfig:
    insert: Insert
    carb_cap: CarbCap
    pearls: list[Pearl]   # empty list = no pearls; sorted in __post_init__ for stable equality
    glass_top: str        # flat string — no sub-dimensions to track yet

    def __post_init__(self):
        self.pearls = sorted(self.pearls, key=lambda p: (p.diameter_mm, p.material))
```

**Note on `EquipmentConfig` fields:** No field defaults. All four fields must be
passed explicitly at every call site. `validate()` rejects `equipment=None`. Runs
are comparable when all four fields match; `pearls` is sorted in `__post_init__`
so list order doesn't affect equality. Named `RIG_N` constants (one per physical
rig configuration) keep the call sites concise — the Rig Reference block on the
rendered log documents each rig's meaning for human readers.

### `CompletedRun` (extended)

```python
@dataclass
class CompletedRun:
    # Logistical (existing)
    strain: str
    run_date: date | None
    sessions_prior_today: int | None
    utc_logged_at: datetime | None
    waypoints: list[Waypoint]

    # Equipment (new)
    equipment: EquipmentConfig = None   # Python-level optional only; validate()
                                        # rejects None post-backfill — every
                                        # shipped run carries explicit equipment

    # Semantic status (new — replaces amber flag in REFACTOR_TEMPLATE_DRIVEN.md)
    too_hot: bool = False               # drives amber styling; amber is presentation,
                                        # too_hot is the fact

    # Curve description (new — replaces curve_header HTML string)
    duration_seconds: int = 65
    endpoint_note: str = ""             # "steady (no ramp)", "same as Run 1", etc.
    # section_note REMOVED — dropped Session 37 (user decision, no basis
    # required). Sole instance (Hive1 R3) deletes at Step 3.0.

    # Session content (new — currently string literals in build_html())
    swab: str = ""
    session_char: str = ""
    intensity: str | None = None
    read: str = ""                      # interpretation
    verdict: str = ""
    extra_rows: list = None             # genuinely one-off result rows not covered above

    # Analysis (new — currently string literals in build_html())
    dab_notes: str = ""                 # user's read
    analysis: str = ""                  # AI synthesis (historically stable)
```

**Note on field boundaries:** The exact field set — and its *granularity* (one
frozen Mode/Results string vs. decomposed `swab`/`session_char`/`read`/`verdict`
fields) — is settled during Step 3 against the 28 existing runs as the test
suite. Expect minor revisions as fields meet real data. `extra_rows` holds
genuinely one-off result rows (e.g. OC R5 "Observation:") as **frozen verbatim
literals**, not a typed escape hatch. (`proposed_waypoints` was dropped as
unused — proposed/revisable curves live on `StrainStatus.next_waypoints`.)

**Schema question status — RESOLVED Session 41** (see the Session 41 note in
Status & Re-opened Questions). B4's closed-predicate-catalog / typed-STORE
shape is **superseded**. The interpretive connective tissue — the
Mode/Hold/Endpoint line, per-run Results rows, `endpoint_note`, `read`,
`verdict`, `analysis` — is **frozen verbatim authored prose**, the same
discipline as `analysis`; nothing is derived, so N2's referent-selection rule
was a pseudo-problem and dissolves. Numerics are *not* re-stored: waypoints
remain the single source for curve numbers (the chart and curve table already
read them) and the curve line is not re-rendered from them — the "render
numerics from structured fields" variant was rejected (it fails the bespoke
lines, e.g. MBD R3, and makes the Step-3.0 delta enumeration circular). Machine
string↔waypoint consistency is consciously declined; the pre-commit
rendered-HTML check is the proportionate guard. `section_note` stays dropped.
Field *granularity* is the only thing still settled at Step 3, against the
28 runs.

**Note on `too_hot`:** Replaces `amber: bool` from `REFACTOR_TEMPLATE_DRIVEN.md`.
Semantically the same fact but named for what it means, not how it renders. The
generator maps `too_hot=True` → amber styling. If styling changes, the data is
unaffected.

**Note on the `equipment` default:** Keep `= None` — it is the only permitted
default, and the rule is behavioral, not mechanism-dependent. Never give this field
a value-producing default: a concrete instance or `field(default_factory=...)`
silently hands unspecified runs a config, reintroducing the exact defect Step 2
eliminates. Do not rely on dataclasses' mutable-default guard to catch a bad
default here — it only rejects arbitrary unhashable defaults on Python ≥3.11, so it
is a version-dependent backstop, not the reason. `validate()` rejecting `None` is
the enforcement.

**Note on `analysis` placement (RESOLVED Session 41 via N5).** The analysis for
a run lives on the `CompletedRun` that generated it, not on `StrainStatus`. It
is frozen and **rendered read-only inside that run's own section** — the
permanent record of how understanding evolved, each run carrying the state of
thought at that moment. It is **not** the source of the current "What to Try
Next". The strain-level "What to Try Next" renders from revisable
`StrainStatus` fields (`next_dab_notes`/`next_ai_analysis`/`next_waypoints`),
which become **explicit `StrainStatus` fields**. Today these are inline
arguments to `what_to_try_next_html()` in `build_html()`, already authored
independently of any run's `analysis` — N5 makes that latent reality explicit
and *removes* a coupling rather than adding one. Sourcing the rendered guidance
from the last run's frozen `analysis` is explicitly rejected: it both stales
the guidance and, once `analysis` is a real field, would orphan it into
write-only data (the gap the Session 41 independent audit caught).

**Schema question #6 — RESOLVED Session 41.** `next_text` — the dashboard
strain-browser one-liner — stays a **hand-maintained `StrainStatus` field**
(current revisable state), consistent with the rest of the
`StrainStatus.next_*` guidance block under N5. It is *not* derived from the
last run's frozen `analysis`.

### `StrainStatus` (extended)

```python
@dataclass
class StrainStatus:
    # Existing
    name: str
    profile_anchor: str
    next_text: str                      # #6 RESOLVED: stays hand-maintained
                                        # current state, not derived
    accent: str | None
    slug: str

    # Profile content (new — currently string literals in build_html())
    info: list = None                   # rows for info_table()
    terpene_note: str = ""              # <p class="note"> in profile section
    # (terpene_table_rows + terpene_table_note removed — see "Removed Capabilities")

    # Current "What to Try Next" — revisable strain-level guidance (N5).
    # Today these are inline args to what_to_try_next_html(); Step 3 makes
    # them explicit fields. NOT sourced from any run's frozen analysis.
    next_dab_notes: str = ""
    next_ai_analysis: str = ""
    next_waypoints: list = None
```

---

## Target Generator Architecture

After the refactor, `build_html()` contains no strain names and looks structurally
like this:

```python
def build_html():
    # Per-jar era (Session 108): validate() / validate_accent_colors() now take
    # explicit args — validate(COMPLETED_RUNS, STRAIN_STATUS) and
    # validate_accent_colors(STRAIN_STATUS, _ACCENT_RESOLVED). This sketch keeps the
    # original no-arg form as the 6-step design record; see Dabby_Log_Generator.py
    # for the live signatures.
    validate()
    validate_accent_colors()

    for ss in STRAIN_STATUS:
        if not has_runs(ss.name):
            continue
        sections.append(render_strain_profile(ss))
        for i, run in enumerate(runs_for(ss.name), start=1):
            sections.append(render_run_section(ss, i, run))   # incl. run.analysis, read-only
        sections.append(render_what_to_try_next(ss))           # from ss.next_*, NOT last run (N5)
```

Adding a strain: create `jars/<slug>.py` (from the boilerplate pattern) and add its slug to `ACTIVE` in `jar_manifest.py`. Zero generator edits.
Adding a run: add a `CompletedRun` to that jar's `RUNS` list in `jars/<slug>.py`. Zero generator edits.
*(Per-jar architecture, Session 108 — supersedes the original single-`Dabby_Data.py` workflow described in the 6-step plan. The generator loop is unchanged; it iterates the assembled `COMPLETED_RUNS`/`STRAIN_STATUS` that `jar_manifest.load_all_jars()` now produces.)*

The CSS block moves to `style.css`, referenced via `<link>` in the HTML head.
This removes ~13K characters of CSS, but **measured at the current run count (28
runs, Session 36) the generator is still 25,479 tokens — over the 25K single-pass
limit.** Every prior estimate ("~22K", "under the limit, decays until Step 3")
was optimistic; CSS extraction alone never brought it under the limit at this run
count. Only Step 3 — replacing the ~460-line per-strain inline-HTML region with a
data-driven loop — brings the generator durably under the limit. Step 1 is a
prerequisite that shrinks the file and separates concerns; it is not itself the
single-pass fix.

---

## Target Handoff Architecture

### State layer — `HANDOFF_STATE.md` (generated)

Produced by a `generate_handoff_state()` function run as part of the generator.
Contains:

- Current run counts per strain
- Last run date per strain
- Current "What to Try Next" per strain (from `StrainStatus.next_*` — **not**
  the last run's frozen `analysis`; corrected per N5, Session 41)
- Current equipment configuration per strain (last run's `equipment`)
- Dashboard stats

No AI authorship. Always current as long as data is current. Replaces the
"Current Strain Status" section of `Dabby_Handoff_Notes.md`.

### Wisdom layer — `HANDOFF_WISDOM.md` (AI-maintained)

AI-authored at session close via a defined checklist. Structured tables that
support superseding entries — rows can be updated or marked superseded when
understanding evolves; new rows are reserved for genuinely novel patterns.
Evidence columns must cite specific runs with inline observations (no vague
"multiple strains" entries). Each entry is traceable to the session and data
that produced it.

**Structure:**

```markdown
## Cross-Strain Patterns
| Pattern | Evidence | Confidence | First Observed |
|---|---|---|---|
| Tail harshness at endpoints ≥430°F | Hive1 R5, Fembot3 R1-2, RF R2, MB9ZST R1-4 | High — 6 points, 5 strains | Session 9 |
| Ramp outperforms flat hold at same endpoint | OC R6 vs R7, Hive1 R5 vs R3-4 | Moderate — 2 strains | Session 14 |

## Equipment Observations
| Configuration | Observed Effect | Evidence | Confidence |
|---|---|---|---|
| Gemlock joystick, no pearl | Lighter swabs, possibly more complete vaporization | MB9ZST R1-2 | Low — 2 points |

## Failure Modes
| Mode | Conditions | Session | Notes |
|---|---|---|---|
| UTC date used as local date | Late-evening logging | Session 6 | OC R6-7 logged as May 10, were May 9 |

## Methodology State
Current settled positions on key questions...
```

### Session-close protocol

At session close, the AI runs a checklist before updating the handoff:

1. Did any new cross-strain pattern emerge or get confirmed?
2. Did equipment configuration change or produce a new observation?
3. Did a failure mode occur this session?
4. Was any methodology position tested, confirmed, or revised?
5. Were any decisions made that shouldn't be re-litigated?
6. Before adding any new wisdom rows: existing row to update instead? Evidence cites specific runs with inline observations?
7. Open backlog items rendered obsolete this session, or any with a scheduled revisit date that has arrived?

Each "yes" produces one update to the relevant wisdom layer table (or to the
backlog itself, for Q7). The state layer is regenerated automatically by the
generator run. See `HANDOFF_WISDOM.md` for the authoritative checklist wording.

---

## Guardrails

These are protocol constraints, not schema constraints. They govern AI behavior
during sessions, not data structure.

**Guardrail 1: Run analysis is historically stable.** *(RESOLVED Session 41 via
N5 — frozen-record intent stands; the rendered "current" guidance is decoupled
to `StrainStatus.next_*`.)*

Once a run's `analysis` field is written and committed, it is a permanent record
of the state of understanding at that moment, rendered read-only in that run's
own section. Mid-session recommendation revisions that are not backed by a new
run go to the revisable `StrainStatus.next_*` fields (the rendered "What to Try
Next"), never into a prior run's frozen `analysis`. Corrections to `analysis`
are permitted when the original was factually wrong — but require an explicit
reason and are the exception, not the default flow.

**Guardrail 2: Analysis must synthesize, not react.**

When writing a new run's `analysis`, the AI must draw on:
- All prior runs and analyses for this strain (full strain history)
- Cross-strain patterns from the wisdom layer
- Equipment state for this run and how it differs from prior runs
- Any emerging cross-log patterns visible in `COMPLETED_RUNS` but not yet in
  the wisdom layer

A run that doesn't follow the prior suggestion is not a deviation — it is more
data. "What to Try Next" tracks accumulated understanding, not a plan. Run N's
analysis remains part of the input to Run N+1's analysis regardless of whether
Run N+1 followed Run N's suggestion.

**Guardrail 3: Equipment comparisons must account for configuration.**

When comparing runs across different equipment configurations, flag the difference
explicitly. A lighter swab on a Gemlock run vs. a spinner cap run may reflect
equipment, not temperature. Runs are only directly comparable when their
`EquipmentConfig` matches. Cross-configuration comparisons require the equipment
difference to be acknowledged in the analysis.

**Guardrail 4: Logging is confirmed interpretation, not silent translation.**
*(Added Session 41. Operational detail — the clarify-vs-thread-pull rule and
the necessity-class fields — lives once, in the Session Logging Protocol in
`Dabby_Handoff_Notes.md`.)*

The AI never freezes loose user input into log content without first stating its
reading back in plain language for correction — unconditionally, regardless of
how confident it feels (this project's documented failure mode is
over-confidence, so the readback cannot be gated on the AI noticing its own
uncertainty). It may ask questions to resolve genuine ambiguity, and at most one
discretionary "that's curious" question beyond what the user said; the user ends
the exchange with "just log it" at any time, and unresolved vagueness is
recorded as vague, never upgraded to a confident claim.

---

## Workflow

### Standard session (run logging)

```
1. User describes the run
2. AI edits jars/<slug>.py — adds a CompletedRun to that jar's RUNS list
3. AI runs: python3 Dabby_Log_Generator.py
4. User opens index.html in browser — immediate local review
5. User confirms
6. AI commits: git add jars/<slug>.py index.html HANDOFF_STATE.md && git commit
7. At session close: AI updates HANDOFF_WISDOM.md via checklist, commits
```

No branches required for routine run logging. No PR required. No network required
until the user decides to push.

### When to use the PR workflow

The PR workflow (branch → push → preview URL → merge) remains available and is
appropriate for:
- Refactors that touch the generator
- UI or CSS changes
- Any change where seeing the rendered output at a real URL before committing to
  main has value
- Changes that benefit from an audit trail in the PR description

It is not required for routine run logging.

---

## Public Release Considerations

Nothing in this architecture walls off public release. The following are left open
deliberately — they are the natural next steps after this architecture is
implemented, not after-thoughts.

**CLAUDE.md User Configuration block.** The session protocol is generic; the
user-specific parameters (timezone, device, insert type, technique) are currently
hardcoded. Extracting them to a User Configuration section at the top of CLAUDE.md
makes the template configurable without a build step. A new user edits four lines.

**Zero required external services.** The target architecture has no hard GitHub
dependency in the critical path. Python + browser is the minimum viable stack.
Git for history, any static host for sharing — neither is required.

**Community template = this repo minus the data.** The generator is already
generic (no strain names in rendering logic, post-refactor). The `jars/` directory
contains this user's data; `Dabby_Core.py` and `jar_manifest.py` are generic. A
community template ships with an example jar and a setup doc. The CLAUDE.md protocol
and wisdom layer start empty for a new user.

---

## Step-Wise Implementation Plan

Each step is independently mergeable to main and has a clear completion
condition. Work can be paused between any two steps. "Independent" means *in the
forward order below* — it does not mean the steps can be reordered. The dependency
chain is real: Step 2 adds the equipment *data* only, and Step 3's loop is what
*renders* it (rendering is deliberately kept out of Step 2 — see B1 below), and
Step 4's generated state layer reads Step 3's `analysis` field and Step 2's
`equipment`. Execute 1 → 2 → 3 → 4 → 5 → 6.

---

### Step 1 — CSS Extraction ✓ DONE — Session 36

CSS moved to `style.css`; generator emits `<link rel="stylesheet">`. Both workflows
copy `style.css` into `_site/`. Full rationale and completion notes in History.

---

### Step 2 — Equipment State on `CompletedRun` ✓ DONE — Session 36

`EquipmentConfig` (no field defaults) + per-run `equipment`; all runs backfilled;
`validate()` rejects `None`. Full rationale and completion notes in History.

---

### Step 3 — Content Migration (Template-Driven Refactor) ✓ DONE — Session 43

All run content moved to `CompletedRun`/`StrainStatus`; `build_html()` is a
data-driven loop with no strain names; per-strain byte-identity oracle passed.
Full rationale and sub-steps in History.

---

### Step 4 — Handoff Restructuring ✓ DONE — Session 45

Handoff split into generated `HANDOFF_STATE.md` + AI-maintained `HANDOFF_WISDOM.md`;
`Dabby_Handoff_Notes.md` trimmed to protocol/decisions/backlog. Full rationale and
sub-steps in History.

---

### Step 5 — Workflow Simplification

**What:** Update CLAUDE.md to reflect the local-first workflow. Make the PR
workflow optional rather than required for routine run logging.

**What changes in CLAUDE.md:**
- Standard confirmation step: "I've run the generator, `index.html` is open in
  your browser — does it look right?" replaces the PR preview URL as the default
  review mechanism for run logging.
- PR workflow documented as appropriate for refactors, UI changes, anything
  where preview URL has value.
- Session-close commit: `git add + git commit` without a branch.

**Completion condition:** A run can be logged, reviewed locally, and committed
to main without opening a PR. PR workflow remains available and documented.

---

### Step 6 — CLAUDE.md User Configuration Block

**What:** Add a User Configuration section at the top of CLAUDE.md. Extract
hardcoded user-specific values (timezone, device model, insert type, technique)
from the protocol body into that section.

**Why this is last:** It is the first step that explicitly prepares the template
for use by others. All prior steps improve the architecture for the current user.
This step makes the template configurable without changing the protocol.

**What the section looks like:**

```markdown
# User Configuration
Timezone: America/Denver (MDT, UTC-6)
Device: Dr. Dabber Switch²
Insert: Quartz (standard)
Technique: Cold start
Material: Hash rosin, solventless
```

A new user forks the repo and edits these five lines. The protocol below is
unchanged.

**Completion condition:** All timezone references, device references, and
technique references in the protocol body point to the User Configuration
section rather than hardcoding values. A hypothetical new user can configure
the template by editing one section.

---

## What This Document Replaces

`REFACTOR_TEMPLATE_DRIVEN.md` — superseded and deleted in Session 34. The goal
(data-driven generator) was correct; the schema design (rendering metadata in
data, HTML strings in dataclass fields, `results_header` preserving an accidental
inconsistency) was wrong. Step 3 of this plan targets the same goal with a
*better* schema — **resolved Session 41** (see the Session 41 note in Status &
Re-opened Questions): no rendering metadata and no HTML strings as typed data,
but also no predicate catalog — the interpretive prose is frozen verbatim
authored text (N2 dissolved) and the rendered "current" guidance is decoupled
from the frozen per-run record (N5). No open sub-problems gate Step 3.


---

## History — Execution Log

*Archived narrative: how Steps 1–4 were executed, and the audit history that
resolved the re-opened questions (B4, N2, N5, C1, C2). Kept as the record of what
was decided and when — not live guidance. Steps 5–6 and the one open question (C3)
are summarized in Live Status at the top.*


### Status & Re-opened Questions (Sessions 35–45)

**Status: proposed plan, not settled architecture.** Its claims are unverified
until Steps 1–2 have actually executed and validated them. A Session 35
independent critique found two factual errors against the codebase (the Step 1
deploy-workflow assumption; the Step 2 backfill guide), structural mis-framings
(B1–B4 below), and an over-assertion pattern. This document's authority was
accruing faster than its verification. It is **not** "do not re-litigate" and its
"non-deletable source of truth" framing is downgraded accordingly — it earns
durable status only as steps execute and confirm it.

**Session 36 — Step 1 executed; token estimate refuted by execution.** CSS
extraction shipped. The structural change is verified: `style.css` is
byte-identical to the previously-inline CSS, `index.html`'s only change is the
`<style>`→`<link>` head swap (body byte-identical), and both workflows were
patched to copy `style.css`. But the token claim was **refuted by measurement**:
post-extraction the generator is **25,479 tokens — still ~480 over the 25K
single-pass limit**, not the "~22K, under the limit" the Step 1 Why and B2
asserted. CSS extraction alone does not achieve single-pass readability at the
current run count; the ~460-line per-strain inline-HTML region is now the
dominant mass. Step 1's completion condition was corrected from "reads in a
single pass" to a structural condition, and the single-pass guarantee now rests
entirely on Step 3. This is the document being corrected by execution exactly as
its Status framing anticipated.

**Session 36 — Step 2 executed (PR #61).** `EquipmentConfig` (no field defaults)
and the `equipment` field added; all 28 runs backfilled and verified by a
mechanical oracle (date rule cross-checked against an independent positional
rule — zero mismatches, zero `None`); `validate()` rejects `None` (negative-tested);
`index.html` byte-identical (data-only, B1 held). Two execution-driven
refinements to this doc: (a) **`carb_cap` is model-level, not category-level** —
user supplied ground truth ("Cloud Vortex 21.0"; "Gemlock joystick"); the doc's
`"spinner"/"gemlock"` examples were placeholders, and model strings better serve
the field's purpose (a future *different* spinner would be silently equated under
`"spinner"`). (b) **Two named constants (`_SPINNER`/`_GEMLOCK`) instead of 28
inline literals** — the 24 pre-cutover runs were genuinely one physical config;
one definition to verify beats 24 transcriptions, and the no-default/explicit-
per-run/`validate()`-rejects-`None` intent is fully met. Step 2's completion
condition is reworded below to match.

**Session 37 — B4 audited twice and reframed (not resolved).** B4's proposed
resolution was drafted, then independently audited in two memory-disabled fresh
sessions (each given source + the prior critique, forbidden the author's argued
draft). Both converged: the resolution *shape* (closed catalog + typed STORE +
bounded deliberate drop) is sound, but the "total classifier" framing is
over-asserted and falsified on existing data. Net effect: B4's vague
"derive-vs-store unresolved" is replaced by a precise bounded heuristic plus two
named open sub-problems (N2 predicate-selection; N5 C1 coupling) that keep
Step 3 gated. `section_note` dropped (user's call, no basis). Raw audit
artifacts distilled here and deleted (Session 35 precedent). No code changes;
`Dabby_Data.py` / `Dabby_Log_Generator.py` / `index.html` untouched. No runs
logged.

**Session 45 — Step 4 executed (branch: claude/architecture-step-4-4nI0U).** Handoff restructured into three layers: (1) `HANDOFF_STATE.md` — generated by `generate_handoff_state()` in `Dabby_Log_Generator.py`, written automatically on every generator run, covers per-strain run counts / last dates / current equipment / full `next_*` guidance; (2) `HANDOFF_WISDOM.md` — AI-maintained structured tables (Cross-Strain Patterns, Equipment Observations, Failure Modes, Methodology State), not strict append-only per C2 — superseding entries permitted; (3) trimmed `Dabby_Handoff_Notes.md` — operational notes, session protocol, decisions, failure modes only (Current Strain Status, Thermal Model, Curve Design, Harm Reduction sections removed). CLAUDE.md startup reads updated to four files: `HANDOFF_STATE.md`, `HANDOFF_WISDOM.md`, `Dabby_Handoff_Notes.md`, `Dabby_Data.py`. Generator read dropped from default startup (rendering-only post-Step-3). Session-close protocol explicit and checklistable. C2 resolved (executed as non-strict). C3 remains open (gates Step 5). Step 5 is next.

**Session 43/44 — Step 3 executed (branch: claude/architecture-planning-0VWIu, PR pending).** All 9 strains migrated to data-driven rendering. Byte-identity oracle passed strain-by-strain (Step 3b/3c) and on the final full-page check (Step 3d). `build_html()` contains no strain names — the target loop is live. Generator: 926 lines → 524 lines; ~25.5K tokens → ~5.8K tokens — durably under the 25K single-pass limit. `CompletedRun` and `StrainStatus` content fields populated for all runs; unused `_ac`/`_spr`/`_cnt` variables removed. The `analysis` and `dab_notes` fields exist in the schema but are empty for current runs — those runs were authored before the refactor; field granularity was settled against all 28 runs as the test suite (per the Step 3 note). Step-3.0 normalization commit shipped separately and first (the `GLOBAL_INFO` Terp Tools fix — "Cloud Vortex auto spinner cap" → "Cloud Vortex 21.0" — was bundled here). Structural debts 1 and 2 in Current State are resolved.

**Session 41 — N2 dissolved, N5 resolved; B4/C1 closed; Step 3 ungated.**
The two open sub-problems were resolved through this project's audit
discipline: two parallel memory-disabled subagent auditors (the fast pass),
then one independent memory-off session given the source plus the fast pass
but forbidden the author's argued draft. The independent auditor diverged from
the fast pass on two points and was right both times; those divergences won.

- **N2 — dissolved (premise rejected).** B4's "closed predicate catalog +
  typed STORE" presumed the curve-relation clause is *derived*; it is
  *authored*. There is no referent-selection rule because nothing is derived.
  The full Mode/Hold/Endpoint line and per-run Results literals are **frozen
  verbatim authored prose** — same authoring/freezing discipline as
  `analysis`. The "render numerics from structured waypoints" variant was
  evaluated and **rejected**: it provably fails the bespoke lines (MBD R3 —
  dual holds + "ramp from 375°F open"), collapsing into verbatim transcription
  exactly on the hard cases while being redundant on the easy ones, and it
  makes the Step-3.0 delta enumeration circular (normalizing Mode lines *is*
  the N2 decision). Machine string↔waypoint consistency is **consciously
  declined** — the project never had it, its epistemic flags disclaim it, no
  logged incident is of that class, and the mandatory pre-commit
  rendered-HTML check at 28-runs / one-author is the proportionate guard
  (Session-37 "rigor scales with stakes").
- **N5 / C1 — resolved by decoupling, with `analysis` explicitly rendered.**
  `CompletedRun.analysis` is frozen (audit trail, Guardrail 1) **and rendered
  read-only inside each run's own section** as that run's permanent synthesis.
  The strain-level "What to Try Next" renders from revisable `StrainStatus`
  fields (`next_dab_notes` / `next_ai_analysis` / `next_waypoints` /
  `next_text`). This separates "historical record" (frozen, in-run) from
  "current recommendation" (revisable, strain-level) — realizing Principles
  4 & 5 and removing the Target-Data-Model contradiction. The "leave
  `analysis` unrendered / history in git only" option was rejected: it
  recreates the unstructured-history problem the refactor exists to kill.
- **B4 — closed.** No predicate catalog; the typed-catalog shape from the
  Session 37 audits is superseded. The only remaining schema question is
  *which* named string fields exist — a small fixed set tested against the
  28 runs at Step 3 (the existing line-299 note), not a slope.
- **C1 — closed**, subsumed by N5 (per-run field frozen *and* rendered as
  in-run history; current guidance decoupled to `StrainStatus.next_*`).
- **C2 — RESOLVED Session 45** (executed as non-strict append-only: superseding entries permitted). **C3 remains open** — gates Step 5.
- **Step 3 is ungated** under N2-minimal + N5(ii), with the Step-3.0 scope
  correction recorded in Step 3 below. Docs only this session; no
  code/`index.html` change.

---

The items below were re-opened by prior audits. **B4, N2, N5, C1, and C2 are resolved** (C2 Session 45 — see above) — their
entries are kept as the record of what was decided and when, not as live
questions. **C3 remains open** (gates Step 5).

- **B4 — RESOLVED Session 41** (was: "resolved in shape only, two sub-problems
  open" — Session 37). The Session 37 audits converged on a closed predicate
  catalog + typed STORE; Session 41 superseded that — the catalog presumed
  *derivation* where the artifact is *authorship*. Final: no catalog, no
  referent rule; the curve-relation prose and per-run Results literals are
  frozen verbatim authored fields (**N2 dissolved**). `section_note` stays
  dropped. Mixed author/tense result rows (e.g. OC R5 "Observation:") are
  frozen verbatim literals like any other per-run row — no schema needed for
  them. `next_text` (open #6) is resolved: hand-maintained current state on
  `StrainStatus` (see N5). See the Session 41 note above.

- **C1 — RESOLVED Session 41 (via N5).** Session 35 recommended keeping the
  per-run `analysis` frozen but decoupling the rendered "current What to Try
  Next" from it. Adopted — with the gap the Session 41 independent audit
  caught: the frozen `analysis` is **also rendered read-only in each run's own
  section** (its permanent in-run history), and the strain-level "What to Try
  Next" renders from revisable `StrainStatus.next_*`. Decoupling *without*
  rendering would have orphaned `analysis` into write-only data — the failure
  the first-classing was meant to eliminate. See the Session 41 note above.

- **C2 — append-only wisdom tables (Principle 6 / Step 4b).** Append-only leaves a
  15–35°F-offset row and its retraction both standing for the reader to reconcile;
  the prose's *replacement-with-explanation* is the value. The doc's own example
  table even mis-attributes "tail harshness ≥430°F" to Session 9 when the cited
  evidence is Sessions 10–12. *Recommended:* keep the state/wisdom split; drop the
  strict append-only structure for a form that supports superseding understanding.

- **C3 — "PR workflow optional" (Principle 7 / Step 5).** The PR preview is not
  just retired-API overhead; it is also the content-loss tripwire and the
  structural enforcement of propose-don't-narrate, in a project with two logged
  content-loss incidents. *Recommended:* PR stays the default at least through
  Step 3 (the riskiest change most needs the preview); any local-first path needs
  a mandatory rendered-diff review gate with teeth, not a soft visual "looks
  right?".

---

#### Step 1 — CSS Extraction

**What:** Move the ~560-line CSS f-string from `Dabby_Log_Generator.py` into a
`style.css` file. Update the generator to emit `<link rel="stylesheet"
href="style.css">` in the HTML head.

**Why:** Cleanly separates presentation from logic; CSS becomes independently
editable without opening a Python file; removes ~13K characters of CSS from the
generator, shrinking the Step 3 surface. **It does not, on its own, bring the
generator under the 25K single-pass limit at the current run count** — measured
post-extraction (Session 36): 25,479 tokens, still ~480 over. Single-pass
readability is deferred entirely to Step 3.

**Completion condition (structural — single-pass is NOT a Step 1 condition):**
`style.css` exists and is byte-identical to the previously-inline CSS;
`index.html`'s only change is the `<style>`→`<link>` head swap with the body
byte-identical; `style.css` is copied into `_site/` by **both** workflows. The
**deployed** `gh-pages` page — not just a local file open — renders identically
(Chart.js, fonts, layout unchanged); a local open would still be styled even with
the workflow gap, so checking only locally would miss the failure entirely.
Single-pass readability was measured unmet post-extraction (25,479 tokens) and
moves to Step 3.

**Notes:** For GitHub Pages, `style.css` must be committed alongside `index.html`,
both in the repo root. **The deploy workflow does require changes — verified
against the files, not assumed.** `deploy.yml` and `preview.yml` both publish only
`index.html` (`mkdir -p _site && cp index.html _site/`); `keep_files: true` does
not save `style.css` because it has never existed on `gh-pages` (nothing to keep).
Step 1 must add `cp style.css _site/` to the Prepare step of **both** workflows in
the same change. Without it the live site and every PR preview render completely
unstyled while this step's completion condition still reads "renders identically" —
the failure is invisible until the page goes blank.

---

#### Step 2 — Equipment State on `CompletedRun`

**What:** Add `EquipmentConfig` dataclass (no field defaults — see the data model
note) and an `equipment` field to `CompletedRun`. Backfill all 28 existing runs
with their configuration at the time they were logged.

**Why:** Equipment can change and revert. Without per-run equipment state, runs
using different configurations are silently compared as if equivalent. Backfilling
establishes the baseline before new runs accumulate.

**`equipment=None` semantics:** `None` is *not* a meaningful value — it does not
mean "inherit the session default." That reading would silently reintroduce the
exact global-static-equipment defect this step exists to eliminate (structural
debt #4): a May spinner run, read back after the default moved to Gemlock, would
report the wrong rig. `None` is Python-level optionality only — a transitional
tripwire that `validate()` rejects at build time so the backfill is forced to
completion. Post-Step-2, no committed run has `equipment=None`.

**Pre-May-13 configuration (reconstructible from the data — not an open blocker):**
`Dabby_Data.py` `GLOBAL_INFO` already records it: *"Prior sessions: Cloud Vortex
auto spinner cap + 6mm quartz pearl in insert."* The data answers both the cap and
the pearl. Confirm with the user as a sanity check, not a gate: "the data says
spinner cap + 6mm pearl before May 13, Gemlock + no pearl from MB9ZST Run 1 —
correct me if either is wrong."

**Backfill guide:**
- Runs 1 through the run *before* MB9ZST Run 1 (May 13): quartz insert, spinner
  cap, `pearl_diameter_mm=6`
- MB9ZST Run 1 (May 13) onward: quartz insert, gemlock cap,
  `pearl_diameter_mm=None` (no pearl — pearl retired with the Gemlock switch)

**B1 — Step 2 is data only; rendering is deferred to Step 3.** Wiring equipment
into the per-strain blocks now is throwaway work: Step 3 deletes those blocks. It
would also *grow* the generator (the token-count problem this effort exists to
solve) right before Step 3 shrinks it. So Step 2 ships `EquipmentConfig`, the
backfill, and `validate()`; Step 3's iteration loop is where equipment first
renders.

**Completion condition:** Every `CompletedRun` carries an explicit `equipment`
value — either an inline `EquipmentConfig(...)` or a named module constant whose
three fields are fully specified at its single definition (the chosen form:
`_SPINNER`/`_GEMLOCK`, since the log has exactly two real-world regimes and
fewer definitions means fewer transcription chances). No reliance on a field
default. `validate()` rejects any run with `equipment=None` (negative-tested,
not just asserted). Rendering is intentionally **not** in scope (see B1 above). Note: `validate()` can only catch `None` — it
cannot detect a
wrong-but-valid config (e.g. a spinner run mislabeled Gemlock), which is why
`EquipmentConfig` has no defaults and the pre-May-13 config (spinner + 6mm pearl
per the data) is sanity-checked with the user rather than assumed.

---

#### Step 3 — Content Migration (Template-Driven Refactor) ✓ DONE — Session 43

**What:** The main refactor — and the highest-risk change in the plan. Move all
run content out of `build_html()` into `CompletedRun`/`StrainStatus` fields,
replace the per-strain HTML blocks with a data-driven iteration loop, and (per
B1) make that loop render each run's `equipment`.

**Gating — RESOLVED Session 41.** N2 and N5 (the two sub-problems that gated
this step) are closed: N2 dissolved (frozen verbatim authored prose, no
catalog, no numeric re-derivation); N5 resolved (frozen `analysis` rendered
read-only in-run; "What to Try Next" from revisable `StrainStatus.next_*`).
Step 3 is ungated, with the Step-3.0 scope correction below — which is what
makes the byte-identity oracle non-circular under N2-minimal.

**B3 — this is ~80% of the project's risk; the even-handed "six steps" framing
underplays it.** It migrates 28 runs into a brand-new schema *and* rewrites a
~460-line generator region, in a project whose handoff records two separate
silent-content-loss incidents. The decomposition below exists to give the
refactor a real mechanical oracle instead of resting on unaided review of the
largest diff in the project's history.

**Sub-steps:**

**3.0 — Normalization commit (separate, on the *old* generator, first).
SCOPE-CORRECTED Session 41.** Resolve only the **trivial non-Mode-line**
inconsistencies in the existing enumerated generator: `<h3>Curve</h3>` vs
`<h3 class="amber">Curve Used</h3>`, `Results` vs `Observations`,
`session_order_note()` present on some first runs but not others. **Mode/Hold/
Endpoint lines and per-run Results rows are explicitly OUT of 3.0 scope — they
are frozen verbatim, never normalized.** This is the N2-minimal correction:
normalizing bespoke Mode lines would *be* the N2 decision (a canonical
Mode-line grammar for cases like MBD R3's dual holds / "ramp from 375°F open"),
so "freeze the 3.0 deltas first" would be circular if 3.0 touched them. With
Mode lines frozen, the 3.0 delta set is small, enumerable, and independent of
the refactor. Do this as one small, deliberate, separately-reviewed commit
whose `index.html` diff is exactly that enumerated non-Mode delta set and
nothing else. Enumerate and freeze that delta list *before* the refactor — it
is the byte-identity oracle's fixed referent (the post-3.0 artifact, not
today's `index.html`). Then the refactor can target *true byte-identity*.

**3a.** Extend `CompletedRun` with the content fields from the data model above
(including the `equipment` rendering wiring deferred from Step 2). `analysis` is
a `CompletedRun` field, frozen, **rendered read-only in that run's own section**
(N5(ii) — the explicit fate the Session 41 audit required: a frozen-but-unrendered
field would orphan the history into `git log` only). Extend `StrainStatus` with
profile content fields **and** the explicit `next_dab_notes`/`next_ai_analysis`/
`next_waypoints` fields (today inline `what_to_try_next_html()` args; now real
revisable fields — the source of the rendered "What to Try Next"). `next_text`
stays hand-maintained (#6 resolved). None of the `next_*` fields are sourced
from any run's frozen `analysis`.

**3b + 3c — strain-by-strain, with a byte-identity oracle.** Do not migrate all
28 runs and rewrite the whole region in one move. Build the data-driven loop
*alongside* the existing enumerated renderer, then migrate **one strain
end-to-end** (profile, every run, What-to-Try-Next) into the new path and assert
the loop's output for that strain's sections is **byte-identical** to the
post-3.0 enumerated output. Proceed strain by strain — each is an independently
checkable unit with a mechanical pass/fail, not a 460-line diff read by eye. Only
once all 9 strains render byte-identically through the loop is the enumerated
region (between the `# ── WW Z` and `# ── Assemble` dividers — treat the dividers
as authoritative; line numbers drift as runs are logged) deleted. The loop
renders each run's frozen `analysis` read-only inside its run section;
`what_to_try_next_html()` pulls from `StrainStatus.next_*` (**not** the last
run's `analysis` — N5); the loop renders `equipment` per B1. The verbatim-freeze
discipline covers **every** per-run literal (Mode/Results rows, `amber` flags,
headers, the Hive1 R3 `section_note` deletion), not just curve strings — that is
what makes the per-strain byte-identity assertion meaningful against the post-3.0
referent.

**3d.** Final check: full `index.html` byte-identical to the post-3.0 baseline.
The normalization commit (3.0) is the *only* intentional-behavior-change
boundary; the refactor itself changes no output. Any non-zero diff here is a
refactor bug, not an accepted normalization.

**Completion condition:** `build_html()` contains no strain names. Adding a run
requires editing only `Dabby_Data.py`. The Step-3.0 non-Mode delta set was
enumerated and frozen *before* the refactor and is the oracle's referent; every
per-run literal (not just curve strings) was transcribed verbatim; every strain
passed the byte-identity oracle individually; final `index.html` is
byte-identical to the post-3.0 baseline. Each run's frozen `analysis` renders
read-only in its section; "What to Try Next" renders from `StrainStatus.next_*`.
Generator remains under 25K tokens.

**Note:** There is no safe pause *inside* one strain's migration, but the plan
now pauses safely *between* strains — that is the point of the decomposition. The
earlier "3b and 3c must be done together in one atomic pass" framing is
superseded by the strain-by-strain oracle.

---

#### Step 4 — Handoff Restructuring ✓ DONE — Session 45

**What:** Split `Dabby_Handoff_Notes.md` into a generated state layer and a
structured wisdom layer.

**Sub-steps:**

**4a.** Write `generate_handoff_state()` — produces `HANDOFF_STATE.md` from
`Dabby_Data.py`. Covers: run counts per strain, last dates, current
"What to Try Next" per strain (from `StrainStatus.next_*` — **not** the last
run's frozen `analysis`; corrected per N5), current equipment config. Call from
the generator alongside `build_html()`.

**4b.** Restructure `Dabby_Handoff_Notes.md` into `HANDOFF_WISDOM.md`. Migrate
the cross-strain patterns, equipment observations, failure modes, and methodology
state into the structured table format. Remove the "Current Strain Status" section
(now generated). Preserve the infrastructure notes, decisions-made section, and
changelog.

**Session 52 note:** `Dabby_Handoff_Notes.md` further pruned — infrastructure
section, chart styling, dashboard implementation details, and changelog removed.
File now contains session logging protocol, behavioral decisions (pruned), failure
modes (pruned), and backlog only.

**4c.** Update CLAUDE.md session-start protocol: read `HANDOFF_STATE.md` (state)
and `HANDOFF_WISDOM.md` (wisdom) instead of `Dabby_Handoff_Notes.md`. Update
session-close protocol: regenerate state (automatic via generator), update wisdom
via checklist.

**C2 execution note:** The wisdom layer is not strict append-only (per the C2
recommendation — superseding entries are permitted; old rows can be updated or
marked superseded when understanding evolves). A note to this effect appears at
the top of `HANDOFF_WISDOM.md`. The state/wisdom split stands; only the strict
append-only structure was dropped.

**Completion condition:** `HANDOFF_STATE.md` is a generated artifact — never edited
by hand. `HANDOFF_WISDOM.md` has structured tables. Session-close protocol is
explicit and checklistable. **Completed Session 45.**

---
