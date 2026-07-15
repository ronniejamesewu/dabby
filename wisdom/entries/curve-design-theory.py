from wisdom_core import *

ENTRY = WisdomEntry(
    key='curve-design-theory',
    kind='theory',
    claim="Higher endpoint + shorter session stopped at the depletion signal; fastest "
          "ascent with no staged ascent waypoints; fast ramp trades staging for density; "
          "bounded-hold descent curves are viable on the Switch² and deliver rather than "
          "cook.",
    guidance="Run higher-and-shorter, stopping when vapor drops, not the timer. Don't "
             "stage ascent waypoints (set target at 0s). Bounded-hold descents: cap peak "
             "to ~one draw, then descend at/above sapphire passive decay (gentler slope "
             "re-creates flat-440). Before blaming session-order for a toasty note, check "
             "it didn't deplete fast.",
    grade='directional',
    grade_basis="Session 91 reasoning, refined by descent-curve runs across five strains — "
                "all Rig 6, three of five jar-openers; directional and single-rig, "
                "toasty-flavor mechanism unresolved.",
    evidence=[
        Citation(
            source='fw106 R23',
            role='confirms',
            provenance='ai-authored',
            gist="June 25, 2026 — Rig 6, 440°F→350°F over 30s programmed to mimic quartz "
                 "passive decay; material vaporized completely in 2 draws, no harshness, "
                 "medium intensity (normal load depleted too quickly). One run; the "
                 "programmed descent produced a qualitatively different session profile "
                 "from flat hold at the same endpoint. (provenance untagged in source)",
            confounds="One run; the sapphire insert lags the programmed curve — actual "
                      "descent expected slower than specified.",
        ),
        Citation(
            source='watermellos R16',
            role='confirms',
            provenance='ai-authored',
            gist="June 26, 2026 — Rig 6, FW106_DESCENT_440 (440→350 over 30s, hold to 60s), "
                 "larger load, first dab of day; cycle 1 clean throughout (no harshness "
                 "despite opening hotter than any prior WM run), material wound down at the "
                 "350°F floor ~10s before end, three productive recovery cycles confirmed "
                 "material remained rather than depleted. Retires the \"not a useful lever "
                 "on Rig 5\" position on mechanism grounds. (provenance untagged in source)",
            confounds="Rig 6 — equipment corrected July 2, 2026 from mislogged Rig 5. The "
                      "350°F floor dropped below WM's vaporization threshold — that's the "
                      "failure mode, not the descent mechanism itself. Session-order "
                      "confound present (R16 first dab; comparison run R15 was second dab) "
                      "— curve vs. session-order effect on harshness remains unresolved.",
        ),
        Citation(
            source='bp4rw13 R5',
            role='confirms',
            provenance='ai-authored',
            gist="June 30, 2026 — same gentle descent shape (440°F→400°F over 60s), first "
                 "dab, big load; no harshness on cycle 1, session ended on intensity "
                 "overwhelm after three cycles, not harshness. Replicates WM R16's "
                 "clean-first-cycle finding. (provenance untagged in source)",
            confounds="Corrected to Rig 6, July 2, 2026 — originally mislogged Rig 5. The "
                      "limiting-factor shift (harshness → intensity) is consistent across "
                      "three strains, all on Rig 6 — cross-rig generalization untested.",
        ),
        Citation(
            source='bp4rw13 R9',
            role='context',
            provenance='ai-authored',
            gist="July 1, 2026 — third dab of the day, same descent curve; produced a "
                 "toasty, near-combustion flavor that became the actual stopping "
                 "condition, a first for this jar. (provenance untagged in source)",
            confounds="Third dab of the day — accumulated heat exposure / session order "
                      "is the hypothesized driver over material state.",
        ),
        Citation(
            source='bp4rw13 R10',
            role='context',
            provenance='ai-authored',
            gist="July 2, 2026 — fresh first dab the next day, identical curve and jar "
                 "material; no toasty flavor, ran two full clean cycles — points at "
                 "accumulated heat exposure / session order over material state as R9's "
                 "driver. (provenance untagged in source)",
            confounds="none noted",
        ),
        Citation(
            source='bp4rw13 R11',
            role='context',
            provenance='ai-authored',
            gist="July 2, 2026 — second dab of the day, same day as R10; also no toasty "
                 "flavor, consistent with a threshold that needs more accumulated exposure "
                 "than a single second dab provides. (provenance untagged in source)",
            confounds="Only partially replicates R9's condition (third dab, not second) "
                      "and doesn't close the question — a deliberate third-same-day dab on "
                      "this curve is still the cleanest remaining test.",
        ),
        Citation(
            source='hive1 R10',
            role='context',
            provenance='ai-authored',
            gist="July 3, 2026 — second dab of the day, gentle descent, deliberate second "
                 "cycle; a hint of toast on a second cycle that depleted fast (1.5 draws). "
                 "Raises residue-scorch (thin leftover material scorching under continued "
                 "heat once the bulk was vaporized) as a competing mechanism to "
                 "session-order for toasty/degradation flavor. (provenance untagged in "
                 "source)",
            confounds="Does not overturn the bp4rw13 R9–R11 reasoning — R9's toast arrived "
                      "on a normal-length, non-fast-depleting cycle, so residue-scorch "
                      "doesn't obviously apply there — but it means \"toasty flavor\" is "
                      "not yet a single-mechanism signal across the log.",
        ),
        Citation(
            source='papzp22 R7',
            role='context',
            provenance='ai-authored',
            gist="June 27, 2026 — basis for the app-display-tracking-cues position: "
                 "intermediate descent-curve waypoints, even when they fall exactly on the "
                 "linear path between open and floor, are the visual checkpoints the user "
                 "navigates by during the dab; design descents with at least one "
                 "intermediate waypoint. (provenance untagged in source)",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R31',
            role='context',
            provenance='ai-authored',
            gist="July 6, 2026 — slow high-floor descent (440→430@25s→420@50s) whose slope "
                 "was gentler than the sapphire's ~1°F/s passive decay, so the PID held "
                 "the insert near 440 the whole way (≈ flat 440): near gag-inducing "
                 "density, dark amber swab, heavy reclaim, larger-than-normal load read "
                 "\"depleted\" after only a couple of draws. Sustained peak cooks. "
                 "(provenance untagged in source)",
            confounds="Original reclaim explanation (material boiling off and "
                      "re-condensing on the glass) corrected by exception July 7, 2026 "
                      "(user-driven): vaporization is airflow-gated so a big load drawn "
                      "twice stays in the cup, and the dark amber is material degrading in "
                      "place (degradation is heat-gated, vaporization is not); \"depleted "
                      "early\" was likely a premature read off a wispy draw.",
        ),
        Citation(
            source='bp4rw13 R12',
            role='confirms',
            provenance='ai-authored',
            gist="July 7, 2026 — bounded-hold counterpoint on the same rig: a 10s hold at "
                 "440 then a descent to 400 at a slope the sapphire can actually follow "
                 "came back amber with light reclaim and a strong effect — material "
                 "delivered, not cooked. (provenance untagged in source)",
            confounds="Two strains, one run each (with FW106 R31) — a directional "
                      "observation, not a pattern.",
        ),
        Citation(
            source='dbrb R1',
            role='confirms',
            provenance='ai-authored',
            gist="July 9, 2026 (Session 152) — second deliver-side strain: same "
                 "bounded-hold curve, jar opener, golden swab, minimal reclaim, big and "
                 "still-climbing intensity, ended on satiety one draw into cycle 2. "
                 "(provenance untagged in source)",
            confounds="Jar-opener with no within-jar reference point.",
        ),
        Citation(
            source='sourtangie R1',
            role='confirms',
            provenance='ai-authored',
            gist="July 10, 2026 (Session 153) — third deliver-side strain: same "
                 "bounded-hold curve, jar opener, small load, minimal reclaim and strong "
                 "effect (delivered) — but a dark amber swab rather than golden. "
                 "(provenance untagged in source)",
            confounds="A reminder that the deliver-vs-cook read comes off reclaim and "
                      "effect, not swab color, which is within-strain only; jar-opener "
                      "with no within-jar reference point.",
        ),
        Citation(
            source='lunarz R1',
            role='context',
            provenance='ai-authored',
            gist="July 10, 2026 (Session 154) — fourth deliver-side strain: same "
                 "bounded-hold curve, jar opener, slightly-larger-than-normal load, dark "
                 "golden swab with normal reclaim, medium-high intensity and strong flavor "
                 "(delivered) — but the only deliver-side run so far that also threw chest "
                 "harshness lingering past session end. (provenance untagged in source)",
            confounds="The lingering chest harshness is a partial counter on the deliver "
                      "side. Five runs across five strains now, still directional, not a "
                      "pattern (single rig; three of the five are jar-openers with no "
                      "within-jar reference point).",
        ),
    ],
    positions=[
        Position(
            stated='Session 91',
            text="**Shorter and higher:** Higher endpoint temperature vaporizes material "
                 "more completely and faster — less is lost to reclaim. The complement is "
                 "stopping when vapor production drops rather than riding the timer. "
                 "Harshness is primarily depletion-driven (hot empty insert after the load "
                 "is spent); lowering temperature delays depletion without fixing the "
                 "mechanism. The practical path is higher temperature with a shorter "
                 "session, stopping at the depletion signal rather than lowering "
                 "temperature to extend session length.",
        ),
        Position(
            stated='Session 91',
            text="**No intermediate ascent waypoints needed:** With cold start, the device "
                 "heats toward the setpoint at maximum rate (+10°F/sec) automatically. "
                 "Setting the target temperature at 0s produces the fastest possible "
                 "ascent. Staged waypoints on the ascent only slow the climb below what "
                 "the device would naturally do — they are not a design feature, they are "
                 "a drag.",
        ),
        Position(
            stated='Session 91',
            text="**Fast ramp as compromise:** A fast ramp (e.g. FW106_FASTER — 8s to "
                 "endpoint) preserves some terpene staging (lighter terpenes have a window "
                 "of dominance before heavier ones come off) while delivering better vapor "
                 "density and efficiency than a slow ramp. Flat hold collapses staging "
                 "entirely; slow ramp maximizes it but wastes the low-vapor-density early "
                 "phase. Fast ramp sits at the intersection where both are acceptable. "
                 "This is a designed compromise, not a best-of-both-worlds solution — "
                 "slower ramp wins on flavor complexity when a strain has legible "
                 "character worth staging.",
        ),
        Position(
            stated='Session 91',
            status='superseded',
            superseded_note="Retired by WM R16 (June 26, 2026): the passive-decay framing "
                            "was wrong at the foundation — the Switch² PID controller "
                            "actively executes the programmed descent, so descent curves "
                            "are viable on the Switch² (demonstrated on Rig 6).",
            text="**[Retired by WM R16] Descent curves are not a useful lever on Rig 5:** "
                 "The Switch² descent rate is spec'd at −3°F/sec with the quartz insert. "
                 "Sapphire's higher thermal mass means it holds heat longer — empirically "
                 "~1°F/sec passive decay on Rig 5, consistent with WM Run 9. A 40-50s "
                 "session at 1°F/sec produces a ~40-50°F drop — marginal within the "
                 "session window and not fast enough to replicate the banger's passive "
                 "thermal decay (~6-9°F/sec). Descent curve experiments are not worth "
                 "prioritizing on the current hardware. *This passive-decay framing was "
                 "wrong — see WM R16 paragraph below.*",
        ),
        Position(
            stated='June 25, 2026 (FW106 R23)',
            text="**FW106 R23 (June 25, 2026) revisits on Rig 6 with a programmed "
                 "descent:** Curve programmed to mimic quartz passive decay (440°F→350°F "
                 "over 30s), not relying on passive sapphire decay. The sapphire insert "
                 "lags the programmed curve — actual descent expected slower than "
                 "specified. Result on Rig 6: material vaporized completely in 2 draws, no "
                 "harshness, medium intensity (normal load depleted too quickly). One run; "
                 "the programmed descent produced a qualitatively different session profile "
                 "from flat hold at the same endpoint. Worth exploring further; see FW106 "
                 "run history.",
        ),
        Position(
            stated='June 26, 2026 (WM R16)',
            text="**WM R16 (June 26, 2026) retires the \"not a useful lever on Rig 5\" "
                 "position:** The prior position was based on sapphire's slow passive heat "
                 "loss (~1°F/sec empirical) making descent too slow to be useful. This "
                 "framing was wrong at the foundation: the Switch² PID controller actively "
                 "executes the programmed descent by targeting lower setpoints and "
                 "stopping the heater — passive heat loss is the physical mechanism, but "
                 "the controller tracks the programmed curve rather than free-decaying. WM "
                 "R16 (Rig 6 — equipment corrected July 2, 2026 from mislogged Rig 5) ran "
                 "FW106_DESCENT_440 (440→350 over 30s, hold to 60s, larger load, first dab "
                 "of day): cycle 1 was clean throughout (no harshness despite opening "
                 "hotter than any prior WM run), material wound down at the 350°F floor "
                 "~10s before end, and three productive recovery cycles confirmed material "
                 "remained rather than depleted. The 350°F floor dropped below WM's "
                 "vaporization threshold — that's the failure mode, not the descent "
                 "mechanism itself. Descent curves via programmed waypoints are viable on "
                 "the Switch² — demonstrated on Rig 6. Note (July 2, 2026): after the "
                 "equipment correction, no descent run has actually been logged on Rig 5 — "
                 "the old position is retired on mechanism grounds (the PID argument "
                 "applies to any insert), not on Rig 5 data. Session-order confound "
                 "present (R16 first dab; comparison run R15 was second dab) — curve vs. "
                 "session-order effect on harshness remains unresolved.",
        ),
        Position(
            stated='June 30, 2026 (bp4rw13 R5)',
            text="**bp4rw13 R5 (June 30, 2026) adds a third strain to the descent-curve "
                 "pattern:** Same gentle descent shape (440°F→400°F over 60s), first dab, "
                 "big load. No harshness on cycle 1; session ended on intensity overwhelm "
                 "after three cycles — not harshness. Replicates WM R16's "
                 "clean-first-cycle finding (both corrected to Rig 6, July 2, 2026 — "
                 "originally mislogged Rig 5). The limiting factor shift (harshness on all "
                 "four prior ramp runs → intensity on the descent) is now consistent "
                 "across three strains, all on Rig 6 — cross-rig generalization untested.",
        ),
        Position(
            stated='July 1–2, 2026 (bp4rw13 R9–R11)',
            text="**bp4rw13 R9–R11 (July 1–2, 2026) test the toasty-flavor / session-order "
                 "hypothesis:** R9 (third dab of the day, same descent curve) produced a "
                 "toasty, near-combustion flavor that became the actual stopping condition "
                 "— a first for this jar. R10 (fresh first dab the next day, identical "
                 "curve and jar material) showed no toasty flavor and ran two full clean "
                 "cycles, pointing at accumulated heat exposure / session order over "
                 "material state as R9's driver. R11 (second dab of the day, same day as "
                 "R10) also showed no toasty flavor — consistent with a threshold that "
                 "needs more accumulated exposure than a single second dab provides, but "
                 "this only partially replicates R9's condition (third dab, not second) "
                 "and doesn't close the question. A deliberate third-same-day dab on this "
                 "curve is still the cleanest remaining test.",
        ),
        Position(
            stated='July 3, 2026 (Hive #1 R10)',
            text="**Hive #1 R10 (July 3, 2026) raises a competing mechanism for "
                 "toasty/degradation flavor — residue-scorch, not session order:** R10 "
                 "(second dab of the day, gentle descent, deliberate second cycle) showed "
                 "a hint of toast on a second cycle that depleted fast (1.5 draws). The "
                 "user pushed back on an initial draft that reached for the bp4rw13 "
                 "session-order framing here — the more parsimonious read for *this* run "
                 "is a thin residue of leftover material scorching under continued heat "
                 "once the bulk was already vaporized, not accumulated cross-session "
                 "exposure (consistent with FW106 R11-12's degradation-flavor pattern from "
                 "material sitting in a hot insert past clean vaporization). This doesn't "
                 "overturn the bp4rw13 R9–R11 reasoning above — R9's toasty flavor arrived "
                 "on a normal-length, non-fast-depleting cycle, so residue-scorch doesn't "
                 "obviously apply there — but it means \"toasty flavor\" is not yet a "
                 "single-mechanism signal across the log. Before citing session-order for "
                 "a toasty/degradation note, check whether the cycle depleted unusually "
                 "fast first; only reach for the accumulated-exposure framing when "
                 "residue-scorch doesn't fit the timing.",
        ),
        Position(
            stated='June 27, 2026 (papzp22 R7)',
            text="**Descent curve waypoints serve as app display tracking cues:** The "
                 "Switch² app displays active waypoints in real time during a session. "
                 "Intermediate waypoints on a descent curve — even when they fall exactly "
                 "on the linear path between open and floor — are not redundant; they are "
                 "the visual checkpoints the user navigates by during the dab. Design "
                 "descent curves with at least one intermediate waypoint for session "
                 "management. A two-waypoint descent (open → floor only) is mathematically "
                 "equivalent but removes the mid-session reference. (papzp22 R7, June 27, "
                 "2026.)",
        ),
        Position(
            stated='July 6–7, 2026 (FW106 R31 / bp4rw13 R12)',
            text="**FW106 R31 / bp4rw13 R12 (July 6–7, 2026) — sustained peak cooks, "
                 "bounded hold delivers; plus a mechanism correction:** FW106 R31 ran a "
                 "slow high-floor descent (440→430@25s→420@50s) whose slope was gentler "
                 "than the sapphire's ~1°F/s passive decay — so the PID held the insert "
                 "near 440 the whole way (≈ flat 440). Result on Rig 6: near gag-inducing "
                 "density, dark amber swab, heavy reclaim, and a larger-than-normal load "
                 "that read \"depleted\" after only a couple of draws. The original R31 "
                 "analysis explained the reclaim as material boiling off uninhaled and "
                 "re-condensing on the glass; corrected by exception July 7, 2026 "
                 "(user-driven) — vaporization here is airflow-gated (it needs vigorous "
                 "carb-cap draw), so a big load drawn only twice simply stays in the cup, "
                 "and the dark amber is that material degrading *in place* (degradation is "
                 "heat-gated and runs whether or not anyone draws; vaporization does not). "
                 "No relocation to the glass; the reclaim was insert-side residue, and "
                 "\"depleted early\" was likely a premature read off a wispy draw. bp4rw13 "
                 "R12 the next night is the bounded-hold counterpoint on the same rig: a "
                 "10s hold at 440 then a descent to 400 at a slope the sapphire can "
                 "actually follow came back amber with light reclaim and a strong effect — "
                 "material delivered, not cooked. Two strains, one run each — a "
                 "directional observation, not a pattern. Design implication: cap peak to "
                 "roughly one draw's worth, then descend at a slope near or above the "
                 "sapphire's passive decay; a gentler slope just re-creates flat-440. "
                 "Arrhenius supplies why the descent is worth anything at all — "
                 "degradation rate is roughly exponential in temperature (~doubles per "
                 "~18°F), so 440→400 is a several-fold slower cook even though the "
                 "sapphire stays hot (shape only — activation energy unknown, not a "
                 "calibrated figure). dbrb R1 (July 9, 2026, Session 152) adds a second "
                 "strain on the deliver side: same bounded-hold curve as bp4rw13 R12, jar "
                 "opener, golden swab, minimal reclaim, big and still-climbing intensity, "
                 "ended on satiety one draw into cycle 2. Sour Tangie R1 (July 10, 2026, "
                 "Session 153) is a third deliver-side strain: same bounded-hold curve, "
                 "jar opener, small load, minimal reclaim and strong effect (delivered) — "
                 "but a dark amber swab rather than golden, a reminder that the "
                 "deliver-vs-cook read comes off reclaim and effect, not swab color, which "
                 "is within-strain only. LunarZ R1 (July 10, 2026, Session 154) is a "
                 "fourth deliver-side strain: same bounded-hold curve, jar opener, "
                 "slightly-larger-than-normal load, dark golden swab with normal reclaim, "
                 "medium-high intensity and strong flavor (delivered) — but the only "
                 "deliver-side run so far that also threw chest harshness lingering past "
                 "session end. Five runs across five strains now, still directional, not a "
                 "pattern (single rig; three of the five are jar-openers with no within-jar "
                 "reference point).",
        ),
    ],
    counter_reading="All descent / bounded-hold evidence is single-rig (Rig 6) and mostly "
                    "jar-openers with no within-jar reference; deliver-vs-cook rests on one "
                    "run per strain, and session-order-vs-curve confounds are unresolved "
                    "(WM R16 first-dab vs R15 second-dab). LunarZ R1 threw lingering chest "
                    "harshness on the deliver side. A skeptic reads the descent \"deliver\" "
                    "as unconfirmed — possibly a session-order or load effect rather than a "
                    "curve-shape one — and the whole set as directional, not a pattern.",
    watch_for="A descent run off Rig 6 would test cross-rig generalization; a deliberate "
              "third-same-day dab on the descent curve is the cleanest remaining "
              "toasty/session-order test.",
    updated='Session 91; descent revisits June 25–July 7, 2026; rig corrections July 2, '
            '2026; R31 mechanism correction July 7, 2026',
)
