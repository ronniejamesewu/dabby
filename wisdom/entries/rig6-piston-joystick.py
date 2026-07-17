from wisdom_core import *

ENTRY = WisdomEntry(
    key='rig6-piston-joystick',
    kind='equipment',
    claim="Rig 6 (sapphire + Wym Stick Piston joystick, no pearls): directed "
          "airflow delivers more per draw than the spinner + dual ruby pearls at "
          "the same setpoint, harshness one draw earlier — consistent with higher "
          "per-draw efficiency.",
    guidance="Joystick efficiency is directional, not equivalence — rig and draw discipline changed together; session order and load are recurring confounds. Localized dark swab spots can be same-dab material pooled in the airflow dead zone, not a floor or insert signal (papzp22 R9). Cap heat after 430°F cycles: operational.",
    grade='observation',
    grade_basis="Low — six strains, nineteen runs.",
    evidence=[
        Citation(
            source='fw106 R20',
            role='confirms',
            provenance='ai-authored',
            gist="FW106 R20 (June 17, 2026 — inaugural; 425°F, 60s, first dab, 4 "
                 "draws; massive intensity vs. Rig 5; harshness draw 2+; dark "
                 "golden swab). [provenance untagged in source]",
            confounds="none noted",
        ),
        Citation(
            source='hive1 R6',
            role='confirms',
            provenance='ai-authored',
            gist="Hive #1 R6–R8 (June 19–20, 2026 — 420°F baseline: R6 first dab, "
                 "harshness ~43s resolved with water; R7 second dab, clean "
                 "throughout; R8 first dab, larger load, very little harshness, "
                 "heavy terpene-load cough). [provenance untagged in source]",
            confounds="none noted",
        ),
        Citation(
            source='papzp22 R4',
            role='confirms',
            provenance='ai-authored',
            gist="papzp22 R4–R6 (June 21–22, 2026 — draw discipline; R6: zero "
                 "harshness first cycle at 430°F, second-cycle harshness last "
                 "~20s, medium). [provenance untagged in source]",
            confounds="none noted",
        ),
        Citation(
            source='bp4rw13 R5',
            role='confirms',
            provenance='ai-authored',
            gist="bp4rw13 R5–R9 and WM R16–R18 (June 26–July 1, 2026 — corrected "
                 "to Rig 6 on July 2, 2026 from mislogged Rig 5, stale jar-local "
                 "defaults after 14–15-day jar gaps; bp4rw13 R5–R8 form the "
                 "cleanest within-jar cycle-count/swab gradient in the log: 3 "
                 "cycles → brown, 1 → golden, 2 → amber-to-brown, 1 → amber; R9: "
                 "third dab, toasty near-combustion flavor became the stopping "
                 "condition). [provenance untagged in source]",
            confounds="Equipment corrected to Rig 6 on July 2, 2026 from mislogged "
                      "Rig 5 (stale jar-local defaults after 14–15-day jar gaps).",
        ),
        Citation(
            source='papzp22 R9',
            role='confirms',
            provenance='user-verbatim',
            gist="July 16, 2026 — beige swab with a localized dark-gold spot on a "
                 "per-dab-swabbed insert; user correction at logging: 'pooled "
                 "reclaim FROM THE DAB THATS BEING CLEANED... an airflow issue "
                 "with the joystick technique rather than leftover reclaim in the "
                 "insert.' Same-dab material outside the directed airflow degrades "
                 "in place — airflow-gated vaporization at spot scale.",
            confounds="One instance; whether joystick sweep technique eliminates "
                      "the dead zone is untested.",
        ),
        Citation(
            source='lhbh R3',
            role='confirms',
            provenance='ai-authored',
            gist="plus LHBH R3–R5 (June 18, 2026 — R5 detailed in Observed "
                 "Effect; R3 sparse reclaim in Notes; R3/R4 load comparison in the "
                 "cross-strain load-size row) — see the frozen analyses. "
                 "[provenance untagged in source]",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='June 17–22, 2026 (observed effect)',
            text="Directed airflow (Piston, .094\" bore, no pearls). Joystick "
                 "advantage confirmed on FW106 and LHBH: delivers more per draw "
                 "than the Cloud Vortex spinner + dual ruby pearls at the same "
                 "setpoint — FW106 R20 (inaugural run) was a massive intensity "
                 "step-up from Rig 5 at the same endpoint and curve (user "
                 "confirmed not misremembering), with harshness arriving one draw "
                 "earlier (draw 2 vs. Rig 5's draw-3 pattern at 425°F), consistent "
                 "with higher per-draw efficiency. At 420°F: LHBH R5 showed draw-3 "
                 "harshness (third dab of day); Hive #1 R7 was clean (second dab "
                 "of day) — consistent with session order as the confound — and "
                 "Hive #1 R8 (first dab, larger load) showed very little harshness "
                 "that never escalated, load size confirmed as the key variable "
                 "separating Hive #1 R6 (harsh) from R8 (clean) with session order "
                 "matched. papzp22 R4–R5: draw discipline (shorter draws) produced "
                 "non-escalating harshness at ~35–38s at 425°F across two runs, "
                 "and the within-draw density drop present on Rig 5 at 420°F for "
                 "this strain was absent on Rig 6 — consistent with the joystick "
                 "sustaining vapor delivery better than the pearl setup, though "
                 "rig and draw discipline changed simultaneously and contributions "
                 "can't be isolated. papzp22 R6: zero harshness through a full 60s "
                 "first cycle at 430°F — 5°F above the prior two Rig 6 runs' "
                 "consistent 35–38s onset; water was taken mid-cycle for terpene "
                 "intensity (not harshness), and whether preemptive water "
                 "prevented harshness or the higher endpoint changed the session "
                 "dynamics is unresolved.",
        ),
        Position(
            stated='Through July 2, 2026 (notes)',
            text="Dark golden swab matches the duration-swab pattern; LHBH R5's "
                 "light golden at 420°F (vs. dark golden at 425°F on the same rig) "
                 "is consistent with lower endpoint producing a lighter swab at "
                 "the same duration. Sparse reclaim on LHBH R3 is directional for "
                 "joystick vaporization efficiency vs. Rig 5. Terpene-load cough "
                 "(coughing without harshness at dense vapor delivery) documented "
                 "on Rig 6 at 420°F with larger load (Hive #1 R8), consistent with "
                 "FW106 R1 on Rig 4. The pending first-dab 420°F test for LHBH "
                 "(LHBH R6) remains open. Device and cap heat after two "
                 "consecutive 430°F cycles (papzp22 R6) is an operational "
                 "observation, not a ceiling signal. papzp22 R4–R5 dates corrected "
                 "July 2, 2026 (UTC-rollover bug). bp4rw13 R9: with the rig change "
                 "ruled out by the equipment correction, session order (third dab, "
                 "accumulated heat exposure) and late-jar material state are the "
                 "live candidates for the toasty, near-combustion flavor — "
                 "unresolved from one run, first data point, not a pattern.",
        ),
    ],
    counter_reading="Joystick efficiency isn't isolated: papzp22 R4–R5 changed rig "
                    "and draw discipline together, the FW106 R20 step-up rests on "
                    "user recall, and load size and session order account for much "
                    "of the 420°F harshness variance independent of the rig.",
    watch_for="The pending first-dab 420°F LHBH test (LHBH R6); whether water or "
              "the higher endpoint prevented papzp22 R6 harshness; recurrence of "
              "bp4rw13 R9's toasty near-combustion flavor.",
    updated='FW106 R20 (June 17, 2026) through July 2, 2026 equipment correction; airflow dead-zone observation Session 169 (July 16, 2026).',
)
