from wisdom_core import *

ENTRY = WisdomEntry(
    key='tail-harshness-mechanism',
    kind='theory',
    claim="Tail-session harshness has four candidate mechanisms — vapor density, "
          "accumulated heat / depletion, airway sensitization, particle accumulation — "
          "none isolated with current data; several predict the same outcomes and can't "
          "be separated.",
    guidance="Treat the mechanism as unresolved — describe what happened, don't promote "
             "a single driver. Depletion is weakened but survives when a load runs dry; "
             "the 'when you stop' / session-exposure framing holds the strongest data "
             "points. Vapor density and airway sensitization are not separable.",
    grade='speculative',
    grade_basis="Four candidate mechanisms, none isolated with current data; several "
                "predict identical outcomes and no current run separates them.",
    evidence=[
        # ── Vapor density ──
        Citation(
            source='fw106 R18',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 5, 425°F, first dab: short-draw first cycle gave wispy vapor and "
                 "very little harshness; the pre-warmed second cycle gave sustained "
                 "density and more harshness — the cleanest within-session "
                 "density-harshness pairing in the log to date. (provenance untagged in "
                 "source)",
            confounds="accumulated airway exposure across cycles an unresolved confound.",
        ),
        Citation(
            source='fw106 R19',
            role='confirms',
            provenance='ai-authored',
            gist="same curve, single cycle, 2nd dab: harshness escalated none → slight → "
                 "lots across three draws with dense vapor present throughout — the "
                 "pairing holds without the cross-cycle confound. (provenance untagged "
                 "in source)",
            confounds="The cross-cycle confound absent (single cycle).",
        ),
        Citation(
            source='fw106 R20',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6: the pairing holds on new equipment; harshness arrived one draw "
                 "earlier at the joystick's higher per-draw delivery — consistent with "
                 "more material per draw crossing the threshold one draw sooner. "
                 "(provenance untagged in source)",
            confounds="New equipment (Rig 6, higher per-draw delivery) differs from the "
                      "Rig 5 instances.",
        ),
        # ── Accumulated heat exposure / material depletion ──
        Citation(
            source='fw106 R8',
            role='confirms',
            provenance='ai-authored',
            gist="smaller load, very little reclaim, harshness midway through draw 2 — "
                 "depletion-consistent harshness when a load runs dry; see also the "
                 "draw-count-as-depletion-proxy row. (provenance untagged in source)",
            confounds="session order can't be ruled out, but the minimal reclaim "
                      "independently corroborates exhaustion.",
        ),
        Citation(
            source='fw106 R14',
            role='counters',
            provenance='ai-authored',
            gist="first dab, 2 draws, material confirmed remaining by reclaim — the "
                 "first run where the session-order and draw-count confounds are both "
                 "clean and harshness appeared anyway; depletion does not explain this "
                 "run. (provenance untagged in source)",
            confounds="vapor density (heavy load → denser vapor; load placement/geometry "
                      "varies with gooey consistency) remains a live candidate and the "
                      "most tractable unresolved confound.",
        ),
        Citation(
            source='watermellos R15',
            role='counters',
            provenance='ai-authored',
            gist="60s single cycle, dense vapor throughout, no depletion signal — "
                 "depletion ruled out for this run; the clearest data point yet for "
                 "session duration, not draw count or depletion, as the harshness "
                 "driver; same signature as FW106 R14, two strains. (provenance untagged "
                 "in source)",
            confounds="vapor density remains an unresolved confound.",
        ),
        # ── Airway sensitization ──
        Citation(
            source='watermellos R4',
            role='confirms',
            provenance='ai-authored',
            gist="the most direct test of the draw-count pattern: rig and curve held "
                 "constant, draw count the only variable changed — harshness around draw "
                 "3 with earlier draws clean. (provenance untagged in source)",
            confounds="draw count may be a proxy rather than the causal variable (see "
                      "Epistemic Calibration).",
        ),
        Citation(
            source='fw106 R3',
            role='confirms',
            provenance='ai-authored',
            gist="the first cross-strain point for the draw-count pattern — harshness "
                 "around draw 3 with earlier draws clean. (provenance untagged in "
                 "source)",
            confounds="rig and curve changes are unresolved confounds for the "
                      "cross-strain comparison.",
        ),
        # ── Water-reset and hot-air control observations ──
        Citation(
            source='session:106',
            role='confirms',
            provenance='ai-authored',
            gist="empty-insert control — Rig 5, 8s ramp to 420°F + 60s hold programmed, "
                 "no material loaded, three draws (the same draw count that consistently "
                 "triggers harshness onset with material present) — no in-session "
                 "harshness, no post-session soreness; the log's first zero-material "
                 "control point: material presence (or the condensed aerosol it "
                 "produces) is a necessary condition for harshness, and pure thermal "
                 "injury from inhaled hot air is ruled out as the primary mechanism. "
                 "(provenance untagged in source)",
            confounds="session-order confound absent, unplanned accidental run.",
        ),
        Citation(
            source='hive1 R6',
            role='confirms',
            provenance='ai-authored',
            gist="clean post-depletion hot-air draws replicated the hot-air-alone "
                 "finding on a second strain and rig (Rig 6). (provenance untagged in "
                 "source)",
            confounds="none noted.",
        ),
        Citation(
            source='sourtangie R3',
            role='confirms',
            provenance='mixed',
            gist="July 11, 2026, Rig 6 — a third instance across a within-session cycle "
                 "boundary: mild throat-and-chest harshness during the material-present "
                 "first cycle resolved and did not return on the long, mostly-empty "
                 "second-cycle draw (hot air, spent material) — consistent with material "
                 "presence being necessary and hot air alone insufficient, at "
                 "single-instance weight; the user read it as \"a point for accumulation "
                 "not thermal.\"",
            confounds="single-instance weight; vapor density, aerosol composition, and "
                      "depletion all survive this data point.",
        ),
        Citation(
            source='fw106 R22',
            role='context',
            provenance='ai-authored',
            gist="harshness appeared in the pause between draws — not mid-draw, not on "
                 "the exhale — distinct from every prior harshness timing in the log; "
                 "flagged for recurrence, not yet elevated to a pattern. (provenance "
                 "untagged in source)",
            confounds="single-run, single-strain observation.",
        ),
    ],
    positions=[
        Position(
            stated='Open question — through Session 120',
            text="Four candidate mechanisms, none isolated with current data:\n\n"
                 "- Vapor density: Smaller load → less dense vapor → less irritation at "
                 "any given moment during the session.\n"
                 "- Accumulated heat exposure: Smaller load → material spent sooner → "
                 "fewer draws through a hot empty insert after the load is done. This "
                 "framing points at *when you stop* as the real variable — not load size "
                 "per se.\n"
                 "- Airway sensitization: Each draw progressively irritates airway "
                 "tissue regardless of vapor temperature. The insert temperature profile "
                 "is roughly similar across draws (convective cooling during the draw, "
                 "rapid re-equilibration after via the titanium-insert interface), so "
                 "escalating harshness across draws reflects increasing airway "
                 "sensitivity rather than increasing vapor temperature. Harshness at a "
                 "given setpoint may be lower than multi-draw observations suggest if "
                 "fewer draws are taken — but draw count may be a proxy for session "
                 "duration or cumulative exposure rather than the causal variable "
                 "itself.\n"
                 "- Particle accumulation (user-proposed, FW106 R20 / Session 120): "
                 "larger aerosol particles deposit in upper airways, causing harshness "
                 "independent of temperature. Plausible aerosol physics; distinct from "
                 "the other three; untestable with current setup; captured at "
                 "single-data-point weight.\n\n"
                 "Vapor density and accumulated heat predict the same outcome in a "
                 "small-load test, so they can't be distinguished by load size alone. "
                 "Vapor density and airway sensitization predict the same draw-by-draw "
                 "escalation; no current run separates them.",
        ),
        Position(
            stated='Vapor density — FW106 R18–R20 (Session 120)',
            text="Density and harshness travel together within sessions. (FW106 R18, "
                 "R19, R20 in evidence.) The LHBH R3/R4 and BB36 #2 R2/R3 timing "
                 "directions (below) are also consistent with density or particle "
                 "accumulation. Directional support for vapor density as a harshness "
                 "driver — not separable from airway sensitization. Draw velocity is an "
                 "uncontrolled variable throughout (harder draws change convective "
                 "cooling and pearl spin simultaneously; net effect untracked). What "
                 "would move it: varying density with load, draw count, and session "
                 "order held fixed — pearl configuration or deliberate draw-velocity "
                 "variation are the available levers.",
        ),
        Position(
            stated='Accumulated heat exposure / material depletion',
            text="Weakened as a primary driver; depletion-consistent harshness when a "
                 "load runs dry remains supported (FW106 R8 in evidence). "
                 "Counter-evidence, strongest first: FW106 R14 and WM R15 (in evidence); "
                 "plus — LHBH R3/R4 (same curve, same rig: larger load → harshness 10s "
                 "earlier — opposite of depletion's prediction; the clearest "
                 "within-strain counter-indication of depletion in the log to date; "
                 "session-order confound present but unlikely to account for a 10-second "
                 "directional shift). BB36 #2 R2/R3 (possibly-smaller load → later "
                 "harshness — direction consistent with vapor density, inconsistent with "
                 "depletion; two uncontrolled runs, one strain — not enough to weight "
                 "the hypotheses). FW106 R23 (descent 440°F→350°F: material spent in 2 "
                 "draws, no harshness) vs. FW106 R5 (flat 440°F hold: harshness ~28s) is "
                 "the first within-strain comparison with endpoint matched and session "
                 "exposure the differing variable — the cleanest FW106 data point for "
                 "cumulative session exposure, not endpoint temperature alone, as the "
                 "driver (one run; descent curve was new; nothing established). Current "
                 "state: depletion as a primary driver is further weakened and the "
                 "density/accumulation framing correspondingly strengthened (LHBH "
                 "R3/R4); the accumulated-exposure framing — *when you stop* as the "
                 "operative variable — holds the strongest of these data points (WM "
                 "R15). What would move it: matched loads stopped at deliberately "
                 "different session lengths before depletion.",
        ),
        Position(
            stated='Airway sensitization',
            text="The draw-count pattern that seeded this hypothesis — harshness around "
                 "draw 3 with earlier draws clean (WM R4 and FW106 R3 in evidence) — is "
                 "consistent across strains (rig and curve changes are unresolved "
                 "confounds for the cross-strain comparison), but draw count may be a "
                 "proxy rather than the causal variable (see Epistemic Calibration "
                 "below). Its distinguishing prediction: the harshness ceiling scales "
                 "with draw count independent of load size or setpoint. Within-day "
                 "session order recurs as the most parsimonious explanation for "
                 "otherwise-unexplained harshness: FW106 R4's exhale-path harshness (2nd "
                 "dab of day — the log's first exclusively-exhale harshness) resolved "
                 "when R6 ran the same setup as a first dab and came back clean. The "
                 "multi-day extension (throat tissue carrying thermal load across days — "
                 "user-proposed after FW106 R14) was cut against the next day: FW106 "
                 "R15, identical conditions and load class with no day off, was "
                 "dramatically better — if multi-day accumulation were the primary "
                 "driver, R15 should have been similar or worse. Demoted from "
                 "directional support to open speculation; run-to-run variance at this "
                 "operating point is the more parsimonious read. A first dab after a day "
                 "or more off is still the test that would resolve it. Sensitization "
                 "remains entangled with vapor density — both predict escalation under "
                 "sustained exposure. Hive #1 gives two same-day 1st→2nd-dab pairs on "
                 "its gentle descent curve with inconsistent results: R9→R10 (June 19, "
                 "2026) showed no shift in harshness-onset timing at all (~15s remaining "
                 "both runs); R13→R14 (July 4, 2026) showed a large shift toward earlier "
                 "onset (~4s remaining, confounded by a delayed draw, to ~40s "
                 "remaining). Within-day session order does not move the harshness "
                 "threshold consistently even within one strain on one curve — when an "
                 "effect appears, it isn't reliable enough yet to treat as a settled "
                 "within-day driver.",
        ),
        Position(
            stated='Water-reset and hot-air control observations',
            text="Hot air alone does not cause harshness. (Session 106 empty-insert "
                 "control, Hive #1 R6, and Sour Tangie R3 in evidence.) Water reset: "
                 "harshness crosses a threshold mid-session and water reverses it — five "
                 "instances, two strains, all Rig 6; citations in the Cross-Strain "
                 "Patterns water-sip row. What water resets (particulate load, mucosal "
                 "sensitization, thermal sensitization) is not distinguishable from "
                 "these data. One observation not captured in that row: FW106 R22 (in "
                 "evidence).",
        ),
        Position(
            stated='July 11, 2026 audit',
            text="Post-session airway discomfort — see Cross-Strain Patterns row (B). "
                 "(Reframed July 11, 2026 audit.) This thread formerly read post-session "
                 "throat soreness as tracking most clearly with opening temperature, on "
                 "three Watermellos data points (WM R1, R9 confirming; R10 no soreness). "
                 "The audit consolidated post-session discomfort across the whole log "
                 "into Cross-Strain Patterns row (B) and found the opening-temperature "
                 "framing doesn't survive: the phenomenon also appears on ordinary 380°F "
                 "opens (WM R1 itself is a 416°F rapid-heat open, but WM R2, FW106 R4, "
                 "and bb362 R2 are 380°F opens with post-session throat discomfort). "
                 "Opening temperature is now one candidate among several, not the "
                 "tracking variable. See row (B) for the full instance list with each "
                 "run's documented confound; WM R1's own confound is the user's \"I "
                 "totally did more draws than I should have,\" and WM R9's is early load "
                 "depletion plus 2nd-dab order.",
        ),
    ],
    counter_reading="Draw count may be a proxy for depletion, cumulative heat exposure, "
                    "or session duration rather than the causal variable; run-to-run "
                    "variance at this operating point is the more parsimonious read for "
                    "several otherwise-unexplained runs.",
    watch_for="Matched loads stopped at different session lengths before depletion; "
              "density varied with load/draw/order held fixed; a first dab after a day+ "
              "off; recurrence of R22's between-draw timing.",
    updated='Sessions 99–120; reframed July 11, 2026 audit',
)
