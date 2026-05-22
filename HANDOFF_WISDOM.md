# Dabby — Accumulated Wisdom
AI-maintained at session close. Structured tables that support superseding entries
(rows can be updated or marked superseded when understanding evolves — not strict
append-only). Each entry is traceable to the session and data that produced it.

Session-close checklist:
1. Did any new cross-strain pattern emerge or get confirmed?
2. Did equipment configuration change or produce a new observation?
3. Did a failure mode occur this session (data integrity / process)?
4. Was any methodology position tested, confirmed, or revised?
5. Were any decisions made that shouldn't be re-litigated? (Includes confirmed-correct audits — "we checked X and it's fine" belongs in Decisions — Do Not Re-Litigate in `Dabby_Handoff_Notes.md`, not the backlog.)

Each "yes" produces one update to the relevant table or section below.

---

## Cross-Strain Patterns

| Pattern | Evidence | Confidence | First Observed | Notes |
|---|---|---|---|---|
| Tail harshness at endpoints ≥430°F | OC R7, Hive1 R2-5, Fembot3 R1-2, MB9ZST R1-2, RF R2, MBD R1-4, BB36#1 R1 | High — 7 strains, consistent across both ramp and flat-hold curve shapes | Sessions 9–14 | Both curve shapes show harshness at this endpoint; it is the temperature, not the shape |
| Ramp outperforms flat hold at same endpoint (session character, staged flavors) | OC R6 (ramp) vs R7 (flat) at 430°F; Hive1 R5 (ramp) vs R3-4 (flat) | Moderate — 2 strains, paired same-day comparisons | Session 14 | Swab does not distinguish between curve shapes within the clean range; subjective session character is the primary readout |
| Swab is a floor indicator, not a fine-grained calibration metric | Multiple strains — load size, material color, oxidation state, swab timing, pressure are uncontrolled variables | High — consistent interpretation across all logged strains | Ongoing | Dark/burnt residue is a reliable signal to reduce endpoint; within the light-golden-to-amber range, swab cannot reliably distinguish curve shapes or small endpoint differences |
| Higher endpoint → stronger effect (larger bolus, faster peak) | OC R5 at 460°F — stronger effect noted; MB9ZST R1-2 at 430°F Gemlock — strong effects noted but equipment confounded | Low — 1 clean data point; others confounded | Session ~10 | Rate-of-delivery hypothesis: same material at lower temps over a longer curve delivers similar total cannabinoids but with a slower, smoother absorption profile; CBN hypothesis rejected |
| MB9ZST and BB36#1: tail harshness persisting below 430°F — may need a lower ceiling | MB9ZST R3 (420°F harsh), R4 (415°F still present); BB36#1 R2-3 (415°F harsh) | Moderate — 2 strains, multiple confirming runs each | Sessions 39–44 | Rain Fruit resolved cleanly at 420°F; these two strains appear to require a lower ceiling (~410°F or below). Insufficient data to confirm whether this is strain-specific or equipment-related (both are Gemlock-era) |
| Harshness onset is threshold-crossing, not temperature-pinned | WW Z R3–4: same curve (430°F endpoint ramp), harshness appeared at 414°F (R3) and 420°F (R4) — 6°F shift on identical curve | Low — 2 runs, one strain, Gemlock-era | Session 57 | Harshness builds continuously through the ramp and is noticed when it crosses a perceivable level, not at a fixed temperature. "Tail harshness" may describe when harshness became noteworthy, not an endpoint-specific signal. Needs cross-strain confirmation. |
| Load size influences both harshness and effect strength | WW Z R5 (smaller load, no harshness, mild) vs R6 (fuller load, tail harshness, hard hit) — same curve, same equipment | Low — 2 runs, one strain; load not precisely measured | Session 59 | Cleanest within-strain load comparison in the log. Both harshness and intensity scaled up together with load size. Mechanism unclear: denser vapor, more total material, or both. Needs cross-strain confirmation before treating as a pattern. |

---

## Equipment Observations

| Configuration | Observed Effect | Evidence | Confidence | Notes |
|---|---|---|---|---|
| Gemlock joystick, no pearl (vs. Cloud Vortex 21.0 + 6mm pearl) | Lighter swabs than spinner config. Visible vapor at lower temps than expected with prior spinner setup. Spinner may produce more harshness at same endpoint and load size. | MB9ZST R1-2 — first Gemlock-era runs; WW Z R1 (spinner) vs R2 (Gemlock) — first same-strain cross-config swab comparison: golden/amber on spinner, wheat-clean on Gemlock; endpoint also dropped 20°F (partial confound) | Low — cross-strain and cross-variable confounds persist | Lighter swabs *may* indicate less material remaining at end of cycle, which *may* indicate the joystick vaporizes more efficiently than the spinner + pearl setup — both steps are inferences, neither is settled. Treat as a persistent confound when comparing Gemlock runs against spinner-era data. Do not assume equivalence between configs in analysis. **Gemlock era ended May 21, 2026 — joystick broke mid-session; back on Cloud Vortex 21.0 + 6mm pearl as of WW Z Run 8.** WW Z R8–9 (small load, spinner) both produced harshness; WW Z R5 (small load, Gemlock) was clean — same curve, same endpoint, same load class. Two confirming data points pointing at spinner config as a harshness contributor at 420°F for this strain. Still within-strain only; cross-strain confirmation needed. |

---

## Failure Modes

Operational and data-integrity failures worth tracking across sessions.
(AI behavioral failure modes are in `Dabby_Handoff_Notes.md` → Known Claude Failure Modes.)

| Mode | Conditions | When | Notes |
|---|---|---|---|
| UTC date used as local run_date | Late-evening logging when UTC has already rolled over (after ~6 PM MDT) | OC R6-7, Hive1 R4-5 | Logged as the next calendar day. Protocol: derive local time (UTC−6 MDT / UTC−7 MST), confirm with user before writing. `run_date` must reflect the confirmed local date |
| Silent content loss via GitHub MCP push_files | Passing full `index.html` content as a string literal to push_files | Session 4; risk persisted through ~Session 28 | push_files strips charts, simplifies sections. Use git for all routine commits. push_files is acceptable only for temporary files on non-main branches when git checkout is impractical, and never for `index.html` |
| Deploy race condition — live site not updated after merge | deploy.yml (push-to-main trigger) and preview cleanup (PR-closed trigger) both writing to gh-pages simultaneously | PR #39 | deploy job committed locally but push rejected as non-fast-forward. Fixed: concurrency group `gh-pages` on both `deploy.yml` and `preview.yml` — jobs queue rather than race |
| Over-asserting device capability limits without verification | Assuming hardware constraints (e.g. waypoint count) from device category rather than actual specs | Session 47 | Claimed Switch² waypoint count was bounded by being a consumer device — user corrected with real limits (+10°F/sec heat, −3°F/sec cool, 10–90s window). Verify device specifications before using hardware constraints as reasoning inputs |
| Edit tool curly-quote contamination in HTML string attributes | Writing Python strings containing `style=\"...\"` via Edit tool | Session 51 | Edit tool converted straight double quotes to U+201C/U+201D curly quotes, leaving literal `\` + curly-quote in rendered HTML — style attribute silently ignored. Fix: use single-quote HTML attributes (`style='...'`) so no backslash escaping is needed. If curly quotes appear, fix by byte position via Python script, not Edit tool |

---

## Decisions — Do Not Re-Litigate

| Decision | Rationale | Session |
|---|---|---|
| Curve shape classifier lives in the generator as a rendering utility function, not as a `@property` on `CompletedRun` (supersedes Session 46 decision) | A string label is display logic — it belongs in the rendering layer, not the data model. The label is not queryable: if shape-based querying is needed in future, either query waypoints directly (e.g. `run.waypoints[-1].temp_f`, monotonicity checks) or add structured boolean/int properties to `CompletedRun` at that point. Do not add properties speculatively before a real query exists | Session 47 |
| `read` and `verdict` on `CompletedRun` are superseded by `analysis` — migration complete | Both fields predate the formal `analysis` field and hold AI-authored interpretive text that `analysis` was designed to replace. Migration completed Session 49: all 13 pre-Step-3 runs with non-empty `read`/`verdict` had content moved verbatim into `analysis` (Hive1 R3, the one run with both, was combined read-first). `extra_rows` is not affected. Do not populate `read` or `verdict` on new runs. | Sessions 48–49 |
| `read` content maps to `analysis`, not `dab_notes` | Both `read` and `verdict` were AI-authored — terpene reasoning, cross-strain pattern references, floor indicator framing. `dab_notes` is the user's verbatim words; pre-Step-3 runs have no user-verbatim record because the field didn't exist yet. Do not backfill `dab_notes` with `read` content. | Session 49 |
| Rendering labels for new run-section fields settled: "Equipment:" inline in Curve block; "Notes on this dab:" for `dab_notes`; "AI Run Analysis:" for `analysis` | "AI Run Analysis:" distinguishes the frozen per-run synthesis from "AI Analysis:" used in What to Try Next (revisable guidance). "Notes on this dab:" is user-voice and distinct from AI fields. Equipment line derives human-readable text from `carb_cap` + `pearl_diameter_mm` — never echo the Python constant name. | Session 49 |

---

## Methodology State

Settled positions on key questions. Update when a position is tested, confirmed, or
revised. Include the session and data that prompted the revision.

### Thermal Model
The old 15–35°F titanium-to-insert offset estimate is retired. Current position:

- Quartz insert wall is ~1mm thick at ~1.4 W/m·K conductivity — bulk thermal time
  constant under one second. The insert equilibrates internally almost instantly.
- Physical contact points between titanium and quartz transfer heat efficiently;
  the air gap is not the dominant resistance when contact geometry is intact.
- Offset is probably small under most operating conditions. Dominant remaining
  uncertainties: vaporization cooling (phase change draws heat locally during
  active vaporization) and dynamic lag during steep ascent (titanium ahead of
  insert during fast climbs).
- Short flat tails — even 10 seconds — are sufficient for the insert to reach the
  setpoint. Do not flag short flat tails as inadequate for offset closure.
- Setpoints are reasonable proxies for material contact temperature.

**Do not rebuild the 1D thermal resistance model.** The interface efficiency
parameter (η) concept was developed and abandoned — the two dominant parameters
were partially redundant and the underlying geometry is unknowable. Swab result
is the ground truth.

### Tail Harshness Mechanism — Open Question
Two competing hypotheses, neither isolated with current data:

- **Vapor density:** Smaller load → less dense vapor → less irritation at any given moment during the session.
- **Accumulated heat exposure:** Smaller load → material spent sooner → fewer draws through a hot empty insert after the load is done.

Both predict the same outcome in a small-load test, so they can't be distinguished by load size alone. The accumulated heat framing points at *when you stop* as the real variable — not load size per se. Relevant for future experimental design. First articulated Session 60 based on WW Z run history; one data point (Run 5, small load, clean tail) supports the load-size direction but doesn't settle the mechanism.

### Baseline Philosophy
Single baseline curve for all hash rosin with cold start. Strain-specific
adjustment happens empirically via swab results, not terpene-profile reasoning.
Do not design different starting curves from strain name, consistency type, or
inferred terpene profile without empirical justification.

### Sapphire Insert
When acquired: fresh empirical calibration from scratch. Do not scale from quartz
curves. Two mechanisms that differentiate sapphire from quartz: (1) higher
volumetric heat capacity — absorbs cold-material contact perturbation more stably
at session open; (2) better surface temperature uniformity during vaporization —
~20x higher bulk conductivity replenishes heat faster when local vaporization
creates cold spots. Reddit consensus of 10–20°F lower setpoints for equivalent
results is consistent with this model.

### Harm Reduction
Source: ACS Omega 2017 peer-reviewed study.

- Benzene and methacrolein are documented degradation products of terpene
  thermolysis. Benzene formation begins in small amounts around 400°F and increases
  significantly with temperature.
- Alarming toxicant levels in published studies used 500–550°C (932–1022°F) —
  far above typical practice. At conservative setpoints (375–440°F) benzene
  formation is at the low end of the documented range.
- **Session 57 correction (user-reported, paper not re-read):** Measured byproduct
  quantities were in low ppb even at the high study temperatures — far below EPA
  allowable levels in hundreds of ppm. The "meaningfully safer" framing overstates
  what the evidence supports at our operating range. Do not invoke degradation
  byproducts as a harm reduction argument for temperature choices within 375–460°F.
  The thermal injury mechanism (see below) has the stronger evidence base.

**Resolved:** The 440°F vs. 460°F question falls well below the temperature range
where the research documents meaningful risk. No further discussion needed.

---

### Thermal Injury and Vapor Temperature
Session 57.

The maté throat/esophageal cancer research is relevant harm reduction context. The
cancer association is thermal, not chemical — risk tracks with drinking temperature,
not consumption volume. IARC classified hot beverages above 65°C (149°F) as Group 2A
(probably carcinogenic) in 2016, substantially on maté data. Mechanism: repeated
thermal insult to mucosal epithelium → chronic inflammation → increased malignant
transformation risk.

Applied to dabbing: if harshness tracks primarily with hot vapor hitting tissue —
and it appears to (Session 57 analysis: cannabinoids dominate the volatile fraction
at ~60–80%, heat is the primary driver of both intensity and harshness) — then
harshness is not just an experience signal. It may be the signal of the thing worth
minimizing on harm reduction grounds.

Key unknown: actual vapor temperature at the throat. Insert temperature ≠ vapor
temperature — water and pathway cooling is significant and rig-dependent. Whether
vapor arrives above 65°C (149°F) at the throat is unknown. Fast ramp with dense
vapor likely arrives warmer than a slow ramp. This is worth holding as a working
concern, not a resolved finding.

Open question flagged Session 57: water cooling that reduces vapor temperature enough
to protect tissue may also condense some target volatiles (cannabinoids, terpenes)
before they're inhaled — a real tradeoff between harm reduction and delivery
efficiency. Not yet discussed.
