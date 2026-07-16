from wisdom_core import *

ENTRY = WisdomEntry(
    key='rig4-sapphire-ruby',
    kind='equipment',
    claim="Rig 4 (sapphire insert + 5mm ruby pearl): full corundum pathway likely runs at higher effective temperature than sapphire + quartz pearl at the same setpoint; single-pearl heat loss during a draw is directional, not settled.",
    guidance="Rig 4 likely runs hotter than a quartz-pearl setup at the same setpoint — treat as a comparison confound, not a measured offset. Whether the corundum pearl pushes harshness earlier or later, and the within-draw density pattern, remain unresolved — don't treat either as settled.",
    grade='observation',
    grade_basis="Five runs, two strains; first same-curve same-duration cross-rig swab "
                "comparison complete (dark gold matched); within-draw pattern comparison "
                "still open.",
    evidence=[
        Citation(
            source='fw106 R1',
            role='confirms',
            provenance='ai-authored',
            gist="FW106 R1–2 (baseline, 416°F): very clean swabs both runs; mild "
                 "harshness at 19s into the hold on R1. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R2',
            role='confirms',
            provenance='ai-authored',
            gist="On R2 harshness entered at 5s and escalated draw-by-draw to nearly "
                 "unbearable on draw 3. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='watermellos R1',
            role='confirms',
            provenance='ai-authored',
            gist="Watermellos R1 (same baseline curve): golden swab — distinctly warmer "
                 "than FW106's ultra-clean light beige on both runs; first cross-strain "
                 "swab comparison on Rig 4, suggests swab color reflects strain "
                 "character rather than rig behavior alone. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R16',
            role='confirms',
            provenance='ai-authored',
            gist="FW106 R16 (420°F 8s ramp, 60s hold): within-draw vapor pattern every "
                 "draw — thick at draw start, wispy through the length of the draw — not "
                 "seen on Rig 5 at the same curve; dark golden swab, heavy reclaim. "
                 "Provenance untagged in source.",
            confounds="Runny load geometry confound.",
        ),
        Citation(
            source='fw106 R17',
            role='context',
            provenance='ai-authored',
            gist="FW106 R17 (Rig 5, same 60s curve): dark golden swab matching R16 — "
                 "first same-curve, same-duration cross-rig swab comparison; session "
                 "character not captured. Provenance untagged in source.",
            confounds="Rig 5 run, not Rig 4 — the cross-rig comparison partner; session "
                      "character not captured.",
        ),
    ],
    positions=[
        Position(
            stated='Rig 4 introduced — FW106 R1–2 (May 24, 2026)',
            text="Ruby is corundum (same material as the sapphire insert, Al₂O₃) — ~2x "
                 "volumetric heat capacity and ~20x thermal conductivity over quartz. "
                 "Despite the smaller diameter, the 5mm ruby carries comparable absolute "
                 "thermal mass to the 6mm quartz pearl. Full corundum pathway (insert and "
                 "pearl both Al₂O₃) likely runs at higher effective temperature than "
                 "sapphire + quartz pearl at the same setpoint.",
        ),
        Position(
            stated='FW106 R16 (June 12, 2026)',
            text="Directional for single-pearl thermal behavior: one pearl loses heat "
                 "faster during a draw than two can sustain.",
        ),
        Position(
            stated='Through FW106 R18 (June 15, 2026)',
            text="Whether corundum pearl pushes harshness earlier (denser vapor) or "
                 "later (material done sooner) remains unresolved. R2's draw-count "
                 "escalation introduces a third candidate: airway sensitization or "
                 "session heat accumulation across draws, both enabled by the pearl's "
                 "rapid re-equilibration between draws. Swab consistent across Rig 4→Rig 5 "
                 "at 60s (R16/R17); the within-draw pattern question is still open. FW106 "
                 "R18 (Rig 5, 425°F instead of planned 420°F) did not answer the "
                 "same-endpoint comparison — pearl-count isolation at 420°F on Rig 5 "
                 "remains open.",
        ),
    ],
    watch_for="Pearl-count isolation at 420°F on Rig 5 (still open — FW106 R18 ran "
              "425°F); within-draw density pattern vs Rig 5 at the same draw count.",
    updated='May 24 – June 15, 2026',
)
