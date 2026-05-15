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

## Status & Re-opened Questions

**Status: proposed plan, not settled architecture.** Its claims are unverified
until Steps 1–2 have actually executed and validated them. A Session 35
independent critique found two factual errors against the codebase (the Step 1
deploy-workflow assumption; the Step 2 backfill guide), structural mis-framings
(B1–B4 below), and an over-assertion pattern. This document's authority was
accruing faster than its verification. It is **not** "do not re-litigate" and its
"non-deletable source of truth" framing is downgraded accordingly — it earns
durable status only as steps execute and confirm it.

The following are explicitly re-opened. Each carries a *recommended direction*,
not a settled decision — recording a recommendation as settled architecture is
exactly the failure this audit corrects.

- **B4 — the schema is not "solved."** `too_hot` (vs `amber`) is a real fix, but
  the Principle-1 tension is unresolved, not minor: `endpoint_note="same as Run
  1"` is *derivable* from waypoint equality; `section_note` is experimental
  prose; `extra_rows` is unconstrained; the bespoke per-run "Mode:" line and the
  heterogeneous result-row labels (Swab/Vapor/Verdict/Diagnosis/Read/Note/…) have
  no structured home; OC Runs 1–2 (both → `OC_RUNS12`, rendered as two
  cross-referencing sections) can only be represented by storing comparison prose
  as data — the exact anti-pattern this doc condemns. *Recommended:* resolve
  derive-vs-store **in this document before Step 3**, using OC Runs 1–2 and the
  Mode lines as the explicit test cases. Until then do not call the schema
  "semantically correct."

- **C1 — "run analysis is historically stable" (Principle 4 / Guardrail 1).**
  Decided in a zero-runs ideation session, never tested against the project's
  actual core loop, which is *belief revision* (its single most valuable artifact
  is the wholesale retraction of the 15–35°F thermal offset). *Recommended:* keep
  the per-run `analysis` frozen as the audit trail — but **decouple** the rendered
  "current What to Try Next" from it. Render current guidance from the revisable
  wisdom layer, not from the last run's frozen field. (This decouples "historical
  record" — correctly frozen — from "current recommendation" — which must stay
  current. It is a recommended direction, not a new settled decision.)

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

## Current State

**What exists and works:**
- Data/code split: `Dabby_Data.py` (data) and `Dabby_Log_Generator.py` (rendering)
- Dataclasses: `Waypoint`, `CompletedRun`, `StrainStatus`, `TerpeneEntry`
- Dashboard, strain browser, collapsible run sections, Chart.js curves
- GitHub Actions: deploy on push to main, preview URL on PR
- 28 logged runs across 9 strains

**Structural debt:**

1. **Run content lives in the renderer, not in the data.** Session observations
   (swab, session character, intensity, AI analysis) are string literals inside
   `build_html()` in `Dabby_Log_Generator.py`. They are not in `Dabby_Data.py`.
   Adding a run requires editing two files.

2. **`build_html()` enumerates strains instead of iterating over them.** ~540 lines
   of per-strain inline HTML. Adding a strain or run requires adding code, not data.

3. **The generator is 32K tokens — too large to read in a single Claude pass.**
   The primary cause is ~560 lines of CSS embedded as a Python f-string. The
   secondary cause is the per-strain HTML blocks in `build_html()`.

4. **Equipment state is global and static.** `GLOBAL_INFO` describes the current
   rig configuration, but "current" is not always the same as the configuration used
   in any given run. Equipment can change and revert. Prior runs may have used a
   different joystick, insert, or pearl configuration. This is unstructured and
   unqueryable.

5. **The handoff conflates two different kinds of content.** `Dabby_Handoff_Notes.md`
   mixes derivable state (run counts, pending next directions) with accumulated
   AI-authored wisdom (cross-strain patterns, failure modes, methodology constraints).
   The first can be generated from data. The second requires AI authorship and is
   not derivable from data alone.

6. **`REFACTOR_TEMPLATE_DRIVEN.md` moves rendering metadata into the data layer.**
   It adds `amber`, `curve_label`, `results_header`, `curve_header` (raw HTML) to
   `CompletedRun`. These are presentation concerns, not data concerns. Moving them
   into the data layer trades one coupling for another rather than eliminating it.
   The correct move is to store semantic facts in data and derive presentation from
   them in the generator.

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

**4. Run analysis is historically stable.** *(Re-opened — see C1 in Status &
Re-opened Questions. Recommended: keep the per-run field frozen as the audit
trail, but decouple the rendered "current What to Try Next" from it.)*

The analysis field on a `CompletedRun` records the state of understanding at the
moment it was written. It should not be casually overwritten. Mid-session updates
that aren't backed by a new run belong in the wisdom layer, not in the run object.
Historically stable means: correctable by exception when genuinely wrong, not
silently revisable whenever the AI changes its thinking.

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
class EquipmentConfig:
    insert: str                    # "quartz", "sapphire"
    carb_cap: str                  # "gemlock", "spinner", "directional"
    pearl_diameter_mm: int | None  # None = no pearl (explicit); 3, 4, 6, etc.
```

**Note on `EquipmentConfig` defaults:** No field has a default. Every call site
must pass all three explicitly. This is deliberate: a default like
`carb_cap="gemlock"` would let a spinner-era run constructed as `EquipmentConfig()`
silently validate as Gemlock — equal to a real Gemlock config and undetectable by
`validate()`. Removing defaults forces the configuration to be stated per run,
which is the entire point of per-run equipment state.

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
    hold_seconds: int = 65
    endpoint_note: str = ""             # "steady (no ramp)", "same as Run 1", etc.
    section_note: str = ""              # experimental context (e.g. Hive1 Run 3)

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
    proposed_waypoints: list[Waypoint] | None = None
```

**Note on field boundaries:** The exact field set is validated during Step 3
(content migration). The 28 existing runs are the test suite. Expect minor revisions
as fields meet real data. `extra_rows` is the escape hatch for genuinely one-off
content that doesn't fit structured fields.

**Open schema question (decide in Step 3, not pre-decided here):** Several proposed
fields are in tension with Principle 1 (data carries semantic content, not rendering
metadata). `endpoint_note="same as Run 1"` and `section_note` are comparison/
presentation prose, not facts — and "same as Run 1" is *derivable* from waypoint
equality rather than stored. `extra_rows` is an unconstrained escape hatch that
tends to absorb content the schema should capture. Step 3b must decide, per field,
whether to derive or store, and constrain `extra_rows` to genuinely non-recurring
content. This document does not pre-settle it.

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

**Note on `analysis` placement:** The analysis for a strain lives on the
`CompletedRun` that generated it, not on `StrainStatus`. The generator renders
the last run's analysis as the current "What to Try Next" section. This produces
a permanent history of how understanding evolved — each run carries the state of
thought at that moment. Note that `next_dab_notes`/`next_ai_analysis`/
`next_waypoints` are not being *removed* from `StrainStatus` — they were never
`StrainStatus` fields. They are currently inline arguments to
`what_to_try_next_html()` in `build_html()`; post-refactor they are sourced from
the last `CompletedRun` for the strain.

**Open schema question (#6, decide in Step 3):** `next_text` — the dashboard
strain-browser one-liner — *is* a hand-maintained `StrainStatus` field and is
unaddressed by this migration. Step 3 must decide whether it is derived from the
last run's `analysis` (consistent with the "derive from last run" principle) or
remains hand-maintained.

### `StrainStatus` (extended)

```python
@dataclass
class StrainStatus:
    # Existing
    name: str
    profile_anchor: str
    next_text: str
    accent: str | None
    slug: str

    # Profile content (new — currently string literals in build_html())
    info: list = None                   # rows for info_table()
    terpene_note: str = ""              # <p class="note"> in profile section
    terpene_table_rows: list = None     # only MB9ZST currently
    terpene_table_note: str = ""        # note above terpene table (MB9ZST only)

    # NOTE: next_dab_notes/next_ai_analysis/next_waypoints are NOT removed here —
    # they were never StrainStatus fields (currently inline args to
    # what_to_try_next_html()). Post-refactor they are sourced from the last
    # CompletedRun. Open (#6): next_text above is hand-maintained — derive from
    # last run's analysis or keep manual? Decide in Step 3.
```

---

## Target Generator Architecture

After the refactor, `build_html()` contains no strain names and looks structurally
like this:

```python
def build_html():
    validate()
    validate_accent_colors()

    for ss in STRAIN_STATUS:
        if not has_runs(ss.name):
            continue
        sections.append(render_strain_profile(ss))
        for i, run in enumerate(runs_for(ss.name), start=1):
            sections.append(render_run_section(ss, i, run))
        sections.append(render_what_to_try_next(ss, last_run(ss.name)))
```

Adding a strain: add entries to `Dabby_Data.py`. Zero generator edits.
Adding a run: add an entry to `COMPLETED_RUNS` in `Dabby_Data.py`. Zero generator edits.

The CSS block moves to `style.css`, referenced via `<link>` in the HTML head.
Generator drops from ~32K tokens to ~22K (the CSS block is ~10K) — under the 25K
single-pass limit, but not by much. The margin also decays: every run logged
before Step 3 adds inline HTML to `build_html()`. Step 1 is a real but temporary
reprieve; Step 3 is the durable fix that keeps the generator small structurally.

---

## Target Handoff Architecture

### State layer — `HANDOFF_STATE.md` (generated)

Produced by a `generate_handoff_state()` function run as part of the generator.
Contains:

- Current run counts per strain
- Last run date per strain
- Current "What to Try Next" per strain (last run's `analysis` and `dab_notes`)
- Current equipment configuration per strain (last run's `equipment`)
- Dashboard stats

No AI authorship. Always current as long as data is current. Replaces the
"Current Strain Status" section of `Dabby_Handoff_Notes.md`.

### Wisdom layer — `HANDOFF_WISDOM.md` (AI-maintained)

AI-authored at session close via a defined checklist. Structured as append-only
tables — new entries are added; old entries are not rewritten unless explicitly
correcting an error. Each entry is traceable to the session and data that produced
it.

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

Each "yes" produces one append to the relevant wisdom layer table. The state layer
is regenerated automatically by the generator run.

---

## Guardrails

These are protocol constraints, not schema constraints. They govern AI behavior
during sessions, not data structure.

**Guardrail 1: Run analysis is historically stable.** *(Re-opened — see C1 in
Status & Re-opened Questions. The frozen-record intent is sound; what is
re-opened is coupling it to the rendered "current" guidance.)*

Once a run's `analysis` field is written and committed, it is a permanent record
of the state of understanding at that moment. Mid-session recommendation revisions
that are not backed by a new run belong in the wisdom layer (as a "Methodology
State" update), not in a prior run's `analysis` field. Corrections are permitted
when the original analysis was factually wrong — but require an explicit reason
and are the exception, not the default flow.

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

---

## Workflow

### Standard session (run logging)

```
1. User describes the run
2. AI edits Dabby_Data.py — adds run to COMPLETED_RUNS
3. AI runs: python3 Dabby_Log_Generator.py
4. User opens index.html in browser — immediate local review
5. User confirms
6. AI commits: git add Dabby_Data.py index.html HANDOFF_STATE.md && git commit
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
generic (no strain names in rendering logic, post-refactor). `Dabby_Data.py`
contains this user's data. A community template ships with example data and a
setup doc. The CLAUDE.md protocol and wisdom layer start empty for a new user.

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

### Step 1 — CSS Extraction

**What:** Move the ~560-line CSS f-string from `Dabby_Log_Generator.py` into a
`style.css` file. Update the generator to emit `<link rel="stylesheet"
href="style.css">` in the HTML head.

**Why:** Brings the generator from ~32K tokens to ~22K — under the 25K single-pass
limit but not *well* under, and the margin decays until Step 3 (see the note in
Target Generator Architecture). Clean separation of presentation from logic. CSS
becomes independently editable without opening a Python file.

**Completion condition:** Generator reads in a single pass. `style.css` exists and
is copied into `_site/` by both workflows. The **deployed** `gh-pages` page — not
just a local file open — renders identically (Chart.js, fonts, layout unchanged).
A local open would still be styled even with the workflow gap, so checking only
locally would miss the failure entirely.

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

### Step 2 — Equipment State on `CompletedRun`

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

**Completion condition:** Every `CompletedRun` has an explicitly-constructed
`equipment` (all three `EquipmentConfig` fields named at the call site).
`validate()` rejects any run with `equipment=None`. Rendering is intentionally
**not** in scope (see B1 above). Note: `validate()` can only catch `None` — it
cannot detect a
wrong-but-valid config (e.g. a spinner run mislabeled Gemlock), which is why
`EquipmentConfig` has no defaults and the pre-May-13 config (spinner + 6mm pearl
per the data) is sanity-checked with the user rather than assumed.

---

### Step 3 — Content Migration (Template-Driven Refactor)

**What:** The main refactor — and the highest-risk change in the plan. Move all
run content out of `build_html()` into `CompletedRun`/`StrainStatus` fields,
replace the per-strain HTML blocks with a data-driven iteration loop, and (per
B1) make that loop render each run's `equipment`.

**B3 — this is ~80% of the project's risk; the even-handed "six steps" framing
underplays it.** It migrates 28 runs into a brand-new schema *and* rewrites a
~460-line generator region, in a project whose handoff records two separate
silent-content-loss incidents. The decomposition below exists to give the
refactor a real mechanical oracle instead of resting on unaided review of the
largest diff in the project's history.

**Sub-steps:**

**3.0 — Normalization commit (separate, on the *old* generator, first).** The
current `build_html()` has accidental inconsistencies — `<h3>Curve</h3>` vs
`<h3 class="amber">Curve Used</h3>`, `Results` vs `Observations`,
`session_order_note()` on some first runs but not others, bespoke per-run Mode
lines. Resolve these *in the existing enumerated generator* as one small,
deliberate, separately-reviewed commit whose `index.html` diff is intentional
behavior change and nothing else. Bundling deliberate output changes into the
structural refactor would destroy the only checkable safety property the refactor
can have. Normalize first, separately; then the refactor can target *true
byte-identity*.

**3a.** Extend `CompletedRun` with the content fields from the data model above
(including the `equipment` rendering wiring deferred from Step 2). Extend
`StrainStatus` with profile content fields. Note: `next_dab_notes`/
`next_ai_analysis`/`next_waypoints` are *not* removed from `StrainStatus` — they
were never fields there; they are inline `what_to_try_next_html()` arguments
today (see the data-model note and the open `next_text` question).

**3b + 3c — strain-by-strain, with a byte-identity oracle.** Do not migrate all
28 runs and rewrite the whole region in one move. Build the data-driven loop
*alongside* the existing enumerated renderer, then migrate **one strain
end-to-end** (profile, every run, What-to-Try-Next) into the new path and assert
the loop's output for that strain's sections is **byte-identical** to the
post-3.0 enumerated output. Proceed strain by strain — each is an independently
checkable unit with a mechanical pass/fail, not a 460-line diff read by eye. Only
once all 9 strains render byte-identically through the loop is the enumerated
region (between the `# ── WW Z` and `# ── Assemble` dividers — treat the dividers
as authoritative; line numbers drift as runs are logged) deleted.
`what_to_try_next_html()` pulls from the last run's `dab_notes`, `analysis`,
`proposed_waypoints`; the loop renders `equipment` per B1.

**3d.** Final check: full `index.html` byte-identical to the post-3.0 baseline.
The normalization commit (3.0) is the *only* intentional-behavior-change
boundary; the refactor itself changes no output. Any non-zero diff here is a
refactor bug, not an accepted normalization.

**Completion condition:** `build_html()` contains no strain names. Adding a run
requires editing only `Dabby_Data.py`. Every strain passed the byte-identity
oracle individually; final `index.html` is byte-identical to the post-3.0
baseline. Generator remains under 25K tokens.

**Note:** There is no safe pause *inside* one strain's migration, but the plan
now pauses safely *between* strains — that is the point of the decomposition. The
earlier "3b and 3c must be done together in one atomic pass" framing is
superseded by the strain-by-strain oracle.

---

### Step 4 — Handoff Restructuring

**What:** Split `Dabby_Handoff_Notes.md` into a generated state layer and a
structured wisdom layer.

**Sub-steps:**

**4a.** Write `generate_handoff_state()` — produces `HANDOFF_STATE.md` from
`Dabby_Data.py`. Covers: run counts per strain, last dates, current
"What to Try Next" per strain (last run's analysis), current equipment config.
Call from the generator alongside `build_html()`.

**4b.** Restructure `Dabby_Handoff_Notes.md` into `HANDOFF_WISDOM.md`. Migrate
the cross-strain patterns, equipment observations, failure modes, and methodology
state into the structured table format. Remove the "Current Strain Status" section
(now generated). Preserve the infrastructure notes, decisions-made section, and
changelog.

**4c.** Update CLAUDE.md session-start protocol: read `HANDOFF_STATE.md` (state)
and `HANDOFF_WISDOM.md` (wisdom) instead of `Dabby_Handoff_Notes.md`. Update
session-close protocol: regenerate state (automatic via generator), update wisdom
via checklist.

**Completion condition:** `HANDOFF_STATE.md` is a generated artifact — never edited
by hand. `HANDOFF_WISDOM.md` has structured tables. Session-close protocol is
explicit and checklistable.

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
*better* schema — but the schema is not yet settled (see B4 in Status &
Re-opened Questions); the Principle-1 derive-vs-store decision must be resolved
before Step 3, not at execution time.
