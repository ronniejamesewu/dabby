# Steps 3 & 4 Cleanup Tasks

Identified in Session 46. Twelve items across four categories. Items 1–4 touch
code; items 5–12 are doc fixes. Read `DABBY_ARCHITECTURE.md` before starting —
especially the N5 resolution and Step 3 completion notes.

This doc is a to-do list, not a settled plan. Propose before implementing.
Confirm with the user before touching any file.

---

## Category A — Generator / Data rendering gaps (items 1–4)

These require changes to `Dabby_Data.py` and `Dabby_Log_Generator.py`.
Run `python Dabby_Log_Generator.py` after changes and verify `index.html`
visually before committing. All four can be done in one PR.

### 1. ✓ DONE Session 49 `CompletedRun.analysis` not rendered

The field exists in the schema (`Dabby_Data.py` line ~53) and is populated at
logging time, but `render_run_section()` in `Dabby_Log_Generator.py` (line ~365)
never renders it.

Per the N5/C1 resolution in `DABBY_ARCHITECTURE.md`: `analysis` must render
**read-only inside the run's own section** as permanent in-run history. It is
NOT the source of "What to Try Next" — that comes from `StrainStatus.next_*`.

**What to propose to user:** where in the run section should `analysis` appear
(after the results rows, before the section closes), and what label ("Analysis:",
"AI Analysis:", etc.). Do not implement until confirmed.

All existing runs have `analysis = ""` — the renderer should skip empty values
(consistent with how `swab`, `session_char`, etc. are handled at lines 381–393).

**New info from Session 48:**
- **Label question open:** "AI Analysis:" is now the label for `StrainStatus.next_ai_analysis`
  in the What to Try Next section. Using the same label for the per-run frozen `analysis`
  in the run section risks conflation. Resolve the label before implementing — options
  include "AI Analysis (this run):", "Analysis:", or a distinct visual treatment.
- **`read`/`verdict` transition state:** `read` and `verdict` ARE currently rendered
  in run sections. When items 1–3 ship, the renderer must handle both states without
  requiring migration to complete first: show `analysis` if non-empty; show `read`/`verdict`
  if non-empty (pre-migration runs). Both can coexist during the migration period.
- **Field ordering confirmed:** `dab_notes` before `analysis` in the run section.

---

### 2. ✓ DONE Session 49 `CompletedRun.dab_notes` not rendered

Same situation as `analysis`. The field exists, is intended as the verbatim
user dump captured at logging time, but is never rendered.

**What to propose to user:** label ("Dab Notes:" — matches the `StrainStatus`
rendering at line 79) and position in the run section (before `analysis`,
confirmed in Session 48 — `dab_notes` is the raw input, `analysis` is built from it).

All existing runs have `dab_notes = ""` — skip empty values.

---

### 3. ✓ DONE Session 49 `EquipmentConfig` not rendered in run sections

`run.equipment` (`EquipmentConfig` with `insert`, `carb_cap`,
`pearl_diameter_mm`) is captured per-run but never rendered in `index.html`.
It only appears in `HANDOFF_STATE.md` (via `generate_handoff_state()`).

Per the arch doc B1: "Step 3's iteration loop is where equipment first renders."
User confirmed in Session 46 that equipment should render as a record of what
happened, and is more useful than the Mode row.

**What to propose:** how to display it (e.g. "Equipment: Gemlock joystick,
no pearl" derived from `carb_cap` + `pearl_diameter_mm`). Never echo the
Python constant name (`_GEMLOCK`, `_SPINNER`) — always expand to readable text.
Propose position and format before implementing.

`pearl_diameter_mm=None` means no pearl. `pearl_diameter_mm=6` means 6mm pearl.

---

### 4. ✓ DONE Session 47 `Mode` row hardcoded "Custom Ascent" for all runs

**Location:** `Dabby_Log_Generator.py` line 375.

Current code:
```python
c += (f'<p><strong>Mode:</strong> Custom Ascent &nbsp;|&nbsp;'
      f' <strong>Hold:</strong> {run.hold_seconds} seconds &nbsp;|&nbsp;'
      f' {run.endpoint_note}</p>')
```

This is wrong for flat-hold runs (Hive1 Runs 3–4, Fembot3 Runs 2–3, OC Run 7)
where the waypoints are all the same temperature.

**Resolution agreed in Session 46:** Add `curve_shape` as a `@property` on
`CompletedRun` in `Dabby_Data.py`. Derive it from the waypoint temperature
sequence. A `@property` is preferred over a stored field because:
- Derived-not-authored distinction is structurally unambiguous
- Always consistent with waypoints by construction
- Queryable identically to a field (`run.curve_shape`)
- No `__post_init__` boilerplate, no `field(init=False)` workaround

**Shape set** (finite, agreed in Session 46):
- Ramp Up
- Ramp Down
- Steady Hold
- Valley (down then up)
- Hill (up then down)
- Ramp Up + Hold (ascending then plateau)
- Ramp Down + Hold (descending then plateau)
- Staircase Up / Staircase Down (if needed — may collapse into Ramp + Hold)

**Classifier logic:** analyze the diff sequence of `[wp.temp_f for wp in waypoints]`.
Propose the classifier implementation and the exact label strings to the user
before writing. Verify against all runs in `COMPLETED_RUNS` — especially the
ramp+hold runs (MB9ZST R3-4, MBD R3, BB36 R2-3, RF R3).

Also check line 469 — a second hardcoded "Custom Ascent" in `what_to_try_next_html()`
for the proposed baseline curve display. May need the same fix.

**Actual resolution (Session 47):** Implemented as `_classify_curve_shape()` in
`Dabby_Log_Generator.py` — a rendering utility function, not a `@property` on
`CompletedRun`. Display logic stays in the generator layer. Supersedes the Session 46
decision to use a property. See wisdom layer for the rationale.

---

## Category B — Instruction gaps (items 5–7)

Doc fixes in `Dabby_Handoff_Notes.md`. No generator changes needed.

### 5. ✓ DONE Session 48 Session logging protocol missing `dab_notes` instruction

The Session Logging Protocol section does not instruct Claude to populate
`CompletedRun.dab_notes` when logging a run.

**What to add:** An instruction that `dab_notes` should be populated with the
user's verbatim dump at logging time — not a paraphrase, not a structured
extraction. It is the primary freeform record. The structured fields (`swab`,
`session_char`, `intensity`) are extracted from it.

---

### 6. ✓ DONE Session 48 Session logging protocol missing `analysis` instruction

The Session Logging Protocol section does not instruct Claude to write
`CompletedRun.analysis` when logging a run.

**What to add:** An instruction covering:
- When to write it (after the run is confirmed and logged)
- What it should contain (per Guardrail 2 in `DABBY_ARCHITECTURE.md`: synthesize
  full strain history, cross-strain patterns from wisdom layer, equipment state
  context — not a reaction to the current run in isolation)
- That it is historically stable once written (Guardrail 1): correctable by
  exception, never casually overwritten when thinking changes

---

### 7. ✓ DONE Session 48 "Adding a new run" checklist omits both fields

**Location:** `Dabby_Handoff_Notes.md` line ~46 and line ~50.

Line ~46: lists content fields to populate as
`endpoint_note`, `swab`, `session_char`, `intensity`, `read`, `verdict`, `extra_rows`
— omits `dab_notes` and `analysis`.

Line ~50: the constructor example similarly omits both fields.

Update both to include `dab_notes` and `analysis` with a brief note on each.

---

## Category C — Handoff Notes drift (items 8–10) ✓ DONE Session 46

Targeted fixes in `Dabby_Handoff_Notes.md`.

### 8. ✓ Introduction lists `Dabby_Methodology.md` as default alongside read

Demoted to conditional — now reads "For curve design or methodology questions:
also read `Dabby_Methodology.md`". Consistent with CLAUDE.md.

---

### 9. ✓ CRITICAL section had stale "edit generator" sequence

Fixed: "edit `Dabby_Data.py` → run generator → commit both files."

---

### 10. ✓ Known Claude Failure Modes startup entry listed old files

Updated to current four required reads: `HANDOFF_STATE.md`, `HANDOFF_WISDOM.md`,
`Dabby_Handoff_Notes.md`, `Dabby_Data.py` — with generator/methodology/UI
principles noted as conditional.

---

## Category D — Methodology doc drift (items 11–12) ✓ DONE Session 46

Targeted fixes in `Dabby_Methodology.md`.

### 11. ✓ Session Process step 7: calibration endpoint language

Fixed: "Each run informs the next — adjust based on swab result and session
character, log the outcome."

---

### 12. ✓ "Empirical calibration via swab is ground truth"

Fixed: "Swab result is the empirical ground truth. Terpene profile reasoning
is a starting framework, not a prediction."

---

## Category E — Schema rename (item 13)

### 13. ✓ DONE Session 48 Rename `hold_seconds` → `duration_seconds` on `CompletedRun`

**Location:** `Dabby_Data.py` — `CompletedRun` field definition and all explicit
constructor calls in `COMPLETED_RUNS`. `Dabby_Log_Generator.py` — `render_run_section()`
uses `run.hold_seconds`.

`hold_seconds` is misleading — it implies a flat hold phase, but it is the total
session duration. Most runs use the default (65s); a few specify 60s or 45s
explicitly. The Mode line currently renders it as `Hold: N seconds` which compounds
the confusion now that `hold_seconds` coexists with `Hold` as a curve shape label.

**What to do:**
1. Rename field to `duration_seconds` in `CompletedRun` (default stays 65)
2. Update all explicit `hold_seconds=N` constructor calls in `COMPLETED_RUNS`
3. Update `render_run_section()` — `run.hold_seconds` → `run.duration_seconds`
4. Decide whether the Mode line label changes from `Hold:` to `Duration:` — probably
   yes, since `Hold:` is now ambiguous alongside the `Hold` curve shape label

Straightforward rename — no behavior change. Grep for `hold_seconds` to find all
call sites before starting.

**Done:** Field renamed in `Dabby_Data.py` (definition + all 17 explicit constructor
calls), `run.hold_seconds` → `run.duration_seconds` in `Dabby_Log_Generator.py`,
`Hold:` → `Duration:` in the Mode line label, schema def updated in
`DABBY_ARCHITECTURE.md`. `Dabby_Handoff_Notes.md:259` reference is historical
changelog text — intentionally left as-is.

---

## Category F — endpoint_note convention (item 14)

### 14. ✓ DONE Session 49 `endpoint_note` population convention undocumented

`endpoint_note` exists in the schema and is fully populated across all runs, but
there are no AI instructions for how to populate it when logging a new run. The
field definition comment in `Dabby_Data.py` gives only two plain-text examples
(`"steady (no ramp)"`, `"same as Run 1"`); the actual convention — deduced from
the Step 3b/3c migration — uses inline HTML with `<strong>` label tags and three
distinct label variants depending on curve shape.

**Convention deduced from Step 3 migration:**
- Ramp runs: `<strong>Endpoint:</strong> 430°F` + optional comparison note
  (e.g. `"— same as Run 1"`, `"— down 10°F from prior runs"`)
- Flat hold runs: `<strong>Setpoint:</strong> 430°F steady (no ramp)`
- Cold start with explicit open point: `<strong>Open:</strong> 350°F &nbsp;|&nbsp; <strong>Endpoint:</strong> 460°F`
- Rate note (one-off, WW Z R1): `<strong>Rate:</strong> ~0.6°F/sec`

The Step 3 values were migrated verbatim from the old `build_html()` blocks —
not freshly authored. A future session cold-starting from the handoff has no
basis for the HTML formatting or the `Endpoint:` vs `Setpoint:` vs `Open:`
label distinctions.

**What to add:** An instruction in `Dabby_Handoff_Notes.md` (Session Logging
Protocol or the "Adding a new run" block) covering the HTML format, the three
label variants, and when each applies. The field definition comment in
`Dabby_Data.py` should be updated to match.

---

## Notes for implementation

**Ordering:** Items 8–12 (doc fixes) are independent and low-risk — do them
first or last, doesn't matter. Items 1–4 depend on user confirming the rendering
approach (position, labels, format) before any code is written.

**PRs:** Suggested grouping:
- PR A: items 1–4 (generator + data changes) — needs preview URL to verify rendering
- PR B: items 5–12 (doc fixes only) — lower risk, could go direct to main or PR

**Do not:** hand-write `index.html`, use `push_files` for routine commits,
implement rendering without proposing the format to the user first.

**After merging:** run the session-close wisdom checklist in `HANDOFF_WISDOM.md`
and update `HANDOFF_STATE.md` by running the generator.
