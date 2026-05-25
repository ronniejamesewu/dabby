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
6. Before adding any new wisdom rows: did I check whether an existing row should be updated instead, and does each new or updated Evidence entry cite specific runs with inline observations (e.g. "WW Z R5 (smaller load, no harshness, mild)"), never just run numbers or vague phrases like "multiple strains"? Trim Evidence to the strongest examples — don't accumulate every confirming run.
7. Were any open backlog items in `Dabby_Handoff_Notes.md` rendered obsolete by changes this session, or do any have a scheduled revisit date that has arrived?

Each "yes" produces one update to the relevant table or section below (or to the backlog itself, for Q7).

---

## Cross-Strain Patterns

| Pattern | Evidence | Confidence | First Observed | Notes |
|---|---|---|---|---|
| Tail harshness at endpoints ≥430°F | OC R7, Hive1 R2-5, Fembot3 R1-2, MB9ZST R1-2, RF R2, MBD R1-4, BB36#1 R1 | High — 7 strains, consistent across both ramp and flat-hold curve shapes | Sessions 9–14 | Both curve shapes show harshness at this endpoint; it is the temperature, not the shape |
| Ramp outperforms flat hold at same endpoint (session character, staged flavors) | OC R6 (ramp) vs R7 (flat) at 430°F; Hive1 R5 (ramp) vs R3-4 (flat) | Moderate — 2 strains, paired same-day comparisons | Session 14 | Swab does not distinguish between curve shapes within the clean range; subjective session character is the primary readout |
| Swab is a floor indicator, not a fine-grained calibration metric | OC R7 (plain amber clean swab + "harsh in last 20s" — clean swab, harshness present); WW Z R5 vs R6 (same curve, same equipment, same light golden swab, but R5 no harshness/mild and R6 tail harshness/hard — load size moves session character without moving swab); MB9ZST R5 (super light golden swab + harshness + burnt taste at last draw) | High — three independent strain contexts showing swab doesn't track session character within the clean range | Ongoing | Dark/burnt residue is a reliable signal to reduce endpoint; within the light-golden-to-amber range, swab cannot reliably distinguish curve shapes or small endpoint differences |
| Higher endpoint → stronger effect (larger bolus, faster peak) | OC R5 at 460°F — stronger effect noted; MB9ZST R1-2 at 430°F Gemlock — strong effects noted but equipment confounded | Low — 1 clean data point; others confounded | Session ~10 | Rate-of-delivery hypothesis: same material at lower temps over a longer curve delivers similar total cannabinoids but with a slower, smoother absorption profile; CBN hypothesis rejected |
| MB9ZST and BB36#1: tail harshness persisting below 430°F — may need a lower ceiling | MB9ZST R3 (420°F harsh), R4 (415°F still present); BB36#1 R2-3 (415°F harsh) | Moderate — 2 strains, multiple confirming runs each | Sessions 39–44 | Rain Fruit resolved cleanly at 420°F; these two strains appear to require a lower ceiling (~410°F or below). Insufficient data to confirm whether this is strain-specific or equipment-related (both are Gemlock-era) |
| Harshness onset is threshold-crossing, not temperature-pinned | WW Z R3–4: same curve (430°F endpoint ramp), harshness appeared at 414°F (R3) and 420°F (R4) — 6°F shift on identical curve | Low — 2 runs, one strain, Gemlock-era | Session 57 | Harshness builds continuously through the ramp and is noticed when it crosses a perceivable level, not at a fixed temperature. "Tail harshness" may describe when harshness became noteworthy, not an endpoint-specific signal. Needs cross-strain confirmation. |
| Load size influences both harshness and effect strength | WW Z R5 (smaller load, no harshness, mild) vs R6 (fuller load, tail harshness, hard hit) — same curve, same equipment | Low — 2 runs, one strain; load not precisely measured | Session 59 | Cleanest within-strain load comparison in the log. Both harshness and intensity scaled up together with load size. Mechanism unclear: denser vapor, more total material, or both. Needs cross-strain confirmation before treating as a pattern. |
| Bitter citrus / citrus rind note recurs across strains | MB9ZST R1 (tangerine/bitter citrus), MBD R4 (citrus rind), OC R12 (bitter citrus — user: "increasingly familiar"), FW106 R2 (bitter citrus throughout) | Low — four strains, different producers, different genetics; note recurs across multiple sessions. OC and FW106 both have citrus lineage (limonene inferred), making the note less diagnostic for those two | Sessions 39, 47, 70, 73 | Origin unknown. Limonene is inferred in all four strains' terpene profiles — could be limonene expression at these temperature ranges, or an unrelated coincidence. OC and FW106 having citrus genetics weakens the cross-strain argument somewhat; MB9ZST and MBD are the more surprising occurrences. Not worth weighting in per-run analysis until a mechanism or genetic correlation is established. Watch for recurrence. |

---

## Equipment Observations

| Configuration | Observed Effect | Evidence | Confidence | Notes |
|---|---|---|---|---|
| Rig 1 vs. Rig 2 (spinner + pearl vs. Gemlock, no pearl) | Lighter swabs than spinner config. Visible vapor at lower temps than expected with prior spinner setup. Spinner may produce more harshness at same endpoint and load size. | MB9ZST R1-2 — first Gemlock-era runs; WW Z R1 (spinner) vs R2 (Gemlock) — first same-strain cross-config swab comparison: golden/amber on spinner, wheat-clean on Gemlock; endpoint also dropped 20°F (partial confound) | Low — cross-strain and cross-variable confounds persist | Lighter swabs *may* indicate less material remaining at end of cycle, which *may* indicate the joystick vaporizes more efficiently than the spinner + pearl setup — both steps are inferences, neither is settled. Treat as a persistent confound when comparing Gemlock runs against spinner-era data. Do not assume equivalence between configs in analysis. **Gemlock era ended May 21, 2026 — joystick broke mid-session; back on Cloud Vortex 21.0 + 6mm pearl as of WW Z Run 8.** WW Z R8–9 (small load, spinner) both produced harshness; WW Z R5 (small load, Gemlock) was clean — same curve, same endpoint, same load class. Two confirming data points pointing at spinner config as a harshness contributor at 420°F for this strain. Still within-strain only; cross-strain confirmation needed. **Rig 2 ended May 21, 2026. Rig 3 (sapphire insert, Cloud Vortex 21.0 + 6mm pearl) in use as of May 22, 2026.** |
| Rig 3 (sapphire insert — Dr. Dabber Sapphire Plus v2) | Run 8 (420°F): ultra-clean swab, very strong delayed effect, harshness 11s into the hold. Run 9 (415°F, small load): clean first draw, wispy vapor, trace harshness only as load ran out — load-size confound. Run 10 (415°F, ~25% larger load): no harshness across two full draws — load-size confound resolved. 415°F confirmed clean on the sapphire. Slightly more reclaim at 415°F vs. 420°F; medium effect vs. Run 8's very intense, suggesting 415°F sits at the lower edge of the useful band. Run 11 (417°F, slightly larger load): harshness entered immediately at endpoint arrival — not a hold-duration effect, the temperature itself was the trigger. Ceiling confirmed at 415–417°F. 415°F is the operating point. Intensity trade-off across 2°F is real — 415°F delivered medium, 417°F very hard (eyes blurring, body feels like it's vibrating at 14 min post-session). Run 12 (416°F, third dab of day): harshness entered 15s into the hold (~35s total), mild and never acute. | OC Runs 8–12 (May 22–23, 2026) — five data points | Moderate — five runs, one strain; gradient mapped across 415–417°F | Empirical calibration from scratch. Do not scale from quartz curves. Three adjacent endpoints now mapped: 415°F clean, 416°F mild harshness mid-hold, 417°F immediate on arrival. The gradient is resolved — each degree in this band meaningfully shifts harshness onset. Operating point is 415°F; 416°F is workable if mild late harshness is acceptable. Tolerance confound on Run 12 (third dab of day) means intensity comparison to 415°F is pending a first-dab repeat. |
| Rig 4 (sapphire insert + 5mm synthetic ruby pearl) | Ruby is corundum (same material as the sapphire insert, Al₂O₃) — ~2x volumetric heat capacity and ~20x thermal conductivity over quartz. Despite the smaller diameter, the 5mm ruby carries comparable absolute thermal mass to the 6mm quartz pearl (higher density and heat capacity offset the volume reduction). Full corundum pathway (insert and pearl both Al₂O₃) likely runs at higher effective temperature than sapphire + quartz pearl at the same setpoint. FW106 R1 (baseline, 416°F): very clean swab, strong terpene expression, terpene-load cough without harshness, mild harshness at 19s into 416°F hold. FW106 R2 (same curve, 3 draws): same clean swab, harshness entered at 5s into hold (earlier than R1's 19s) and escalated draw-by-draw to nearly unbearable on draw 3. Watermellos R1 (same baseline curve): golden swab — distinctly warmer than FW106's ultra-clean light beige on both runs. First cross-strain swab comparison on Rig 4; suggests swab color reflects strain character rather than rig behavior alone. | FW106 R1 (May 24, 2026 — very clean swab, terpene-load cough without harshness, mild harshness at 19s into 416°F hold, medium intensity); FW106 R2 (May 24, 2026 — same clean swab, harshness escalated mild→nearly unbearable across 3 draws, pretty big intensity); Watermellos R1 (May 25, 2026 — golden swab on same baseline curve that returned ultra-clean light beige on FW106 R1–2) | Low — three runs, two strains; no cross-rig comparison yet | Whether corundum pearl pushes harshness earlier (denser vapor) or later (material done sooner) remains unresolved. R2's draw-count escalation introduces a third candidate: airway sensitization or session heat accumulation across draws, both enabled by the pearl's rapid re-equilibration between draws. Next: limit to 1–2 draws at 416°F to isolate draw-count from endpoint temperature. Cross-rig comparison on the same strain (e.g. OC on Rig 4 vs. Rig 3) still needed to isolate pearl effect from strain character. |
| Rig 5 (sapphire insert + two 5mm synthetic ruby pearls) | Inaugural run: beige swab — lighter than Rig 4's golden on Watermellos at the same curve and endpoint. No in-session harshness on 2 controlled draws; mild post-session throat harshness. Intensity big. Run 3 (same 2-draw limit, Rig 5 held constant): ultra clean beige, no in-session or post-session harshness, immediate big effect — consistent with Run 2. Two-run consistency on Rig 5 at 2 draws, no harshness either time. Whether dual pearl vaporizes more completely (explaining lighter swab) or the swab difference is draw-count-driven is unresolved — draw count also changed from Run 1 (Rig 4, many draws) to Run 2 (Rig 5, 2 draws). | Watermellos R2 (May 25, 2026 — beige swab lighter than Rig 4 golden on same strain/curve; no in-session harshness on 2 draws; mild post-session harshness; pretty big intensity); Watermellos R3 (May 25, 2026 — ultra clean beige; no in-session or post-session harshness on 2 draws; immediate big effect) | Low — two runs, one strain; draw count and rig changed simultaneously between R1 and R2; R3 holds rig constant | Two consecutive clean 2-draw runs on Rig 5. Rig 4→5 confound still unresolved — cross-rig comparison at same draw count needed. Next: add draws on Rig 5 at baseline to find where harshness re-enters with rig held constant. |

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
| New `RIG_N` constant added without updating `_RIG_LABELS` in generator | Adding `RIG_N` to `Dabby_Data.py` without a matching entry in `_RIG_LABELS` in `Dabby_Log_Generator.py` | Rig 4 missing from `_RIG_LABELS` — FW106 R1–2 and Watermellos R1 displayed without "Rig 4 — " prefix; Rig 4 absent from Rig Reference table entirely. Discovered and fixed Session 75 | Update both files in the same commit when adding a new rig. Backlog item exists to auto-discover `RIG_N` constants from the module to eliminate this structurally |
| Edit tool curly-quote contamination in HTML string attributes | Writing Python strings containing `style=\"...\"` via Edit tool | Session 51 | Edit tool converted straight double quotes to U+201C/U+201D curly quotes, leaving literal `\` + curly-quote in rendered HTML — style attribute silently ignored. Fix: use single-quote HTML attributes (`style='...'`) so no backslash escaping is needed. If curly quotes appear, fix by byte position via Python script, not Edit tool |

---

## Decisions — Do Not Re-Litigate

| Decision | Rationale | Session |
|---|---|---|
| Curve shape classifier lives in the generator as a rendering utility function, not as a `@property` on `CompletedRun` (supersedes Session 46 decision) | A string label is display logic — it belongs in the rendering layer, not the data model. The label is not queryable: if shape-based querying is needed in future, either query waypoints directly (e.g. `run.waypoints[-1].temp_f`, monotonicity checks) or add structured boolean/int properties to `CompletedRun` at that point. Do not add properties speculatively before a real query exists | Session 47 |
| `read` and `verdict` on `CompletedRun` are superseded by `analysis` — migration complete | Both fields predate the formal `analysis` field and hold AI-authored interpretive text that `analysis` was designed to replace. Migration completed Session 49: all 13 pre-Step-3 runs with non-empty `read`/`verdict` had content moved verbatim into `analysis` (Hive1 R3, the one run with both, was combined read-first). `extra_rows` is not affected. Do not populate `read` or `verdict` on new runs. | Sessions 48–49 |
| `read` content maps to `analysis`, not `dab_notes` | Both `read` and `verdict` were AI-authored — terpene reasoning, cross-strain pattern references, floor indicator framing. `dab_notes` is the user's verbatim words; pre-Step-3 runs have no user-verbatim record because the field didn't exist yet. Do not backfill `dab_notes` with `read` content. | Session 49 |
| Rendering labels for new run-section fields settled: "Equipment:" inline in Curve block; "Notes on this dab:" for `dab_notes`; "AI Run Analysis:" for `analysis` | "AI Run Analysis:" distinguishes the frozen per-run synthesis from "AI Analysis:" used in What to Try Next (revisable guidance). "Notes on this dab:" is user-voice and distinct from AI fields. Equipment line derives human-readable text from the nested EquipmentConfig fields via `_fmt_equipment_display()` — never echo the Python identifier (`RIG_3` etc.) to the user; always use the display name (Rig 3). | Session 49 |
| End-of-jar What to Try Next uses "if this strain shows up again" framing — never "on the next jar" | Most strains won't reappear, and even if they do, the next jar deserves its own treatment. Future jar-close sessions write `next_text` and `next_ai_analysis` in that voice. | Session 64 |
| Equipment schema: nested `Insert`/`CarbCap`/`Pearl` dataclasses; sequenced `RIG_N` constants with "Rig N" display; `pearls: list[Pearl]` sorted in `__post_init__` for stable equality; `airflow` front-loaded on `CarbCap` for confirmed-coming variation; `glass_top` flat string (no sub-dimensions yet); Terp Tools row deleted from `GLOBAL_INFO` (superseded by Rig Reference) | Insert, pearl, cap, and glass-top variation are all real or confirmed-coming. Schema captures the four independent variables. Sequenced naming eliminates rename churn when new variables appear. Pearl/insert/cap normalized as nested dataclasses; glass top deferred to flat string until sub-dimensions appear. Audited by Plan agent before execution. | Session 65 |
| Insert display: show material only when `model == "stock"` (`"{brand} stock {material}"`); named models use `"{brand} {model}"` only | Material is redundant when the model name is self-describing. If a future named insert needs material surfaced, add it at that point. Applies in both `_fmt_equipment_display()` and the Rig Reference table. | Session 65 |

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
Three hypotheses, none isolated with current data:

- **Vapor density:** Smaller load → less dense vapor → less irritation at any given moment during the session.
- **Accumulated heat exposure:** Smaller load → material spent sooner → fewer draws through a hot empty insert after the load is done.
- **Airway sensitization:** Each draw progressively irritates airway tissue regardless of vapor temperature. The insert temperature profile is roughly similar across draws (convective cooling during the draw, rapid re-equilibration after via the titanium-insert interface), so escalating harshness across draws reflects increasing airway sensitivity rather than increasing vapor temperature. Harshness ceiling at a given setpoint may be higher than multi-draw observations suggest if draw count is controlled.

Both the first two hypotheses predict the same outcome in a small-load test, so they can't be distinguished by load size alone. The accumulated heat framing points at *when you stop* as the real variable — not load size per se. The airway sensitization hypothesis predicts harshness ceiling scales with draw count independent of load size or setpoint — FW106 R2 (three draws, escalating to nearly unbearable on draw 3 at a setpoint that was clean on draw 1) is the first data point; Watermellos R2 (two controlled draws, post-session harshness dropped from Run 1's pronounced soreness to mild — confounded by simultaneous Rig 4→5 change) is a second directional data point; Watermellos R3 (same 2-draw limit, Rig 5 held constant — no in-session or post-session harshness, second consecutive clean run) is a third directional data point with rig held constant. First two hypotheses articulated Session 60; airway sensitization added Session 73; R3 added Session 77.

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
