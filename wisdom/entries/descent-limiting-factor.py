from wisdom_core import *

ENTRY = WisdomEntry(
    key='descent-limiting-factor',
    kind='pattern',
    claim="Descent curve changes limiting factor from harshness to intensity.",
    guidance="A descent curve (open hot, move off peak immediately) front-loads the "
             "terpene bolus and shifts the stopping condition off harshness — expect "
             "depletion, intensity, or satiety to end the session instead. Evidence is "
             "all Rig 6 and first-dab; treat cross-rig and load effects as untested.",
    grade='observation',
    grade_basis="Low — four strains, all first-dab runs, all Rig 6; consistent "
                "direction, single-rig.",
    evidence=[
        Citation(
            source='fw106 R23',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6, 440→350°F over 30s, hold to 60s, first dab, normal load — no "
                 "harshness, clean cycle 1, material spent in 2 draws. (provenance "
                 "untagged in source)",
            confounds="none noted",
        ),
        Citation(
            source='watermellos R16',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6; same descent shape, first dab, larger load — clean cycle 1 "
                 "throughout, no harshness despite 440°F open, 350°F floor too low as "
                 "failure mode. (provenance untagged in source)",
            confounds="corrected July 2, 2026 from mislogged Rig 5.",
        ),
        Citation(
            source='bp4rw13 R5',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6; 440→400°F over 60s, first dab, big load — no harshness cycle "
                 "1, terpene-load cough, session ended on intensity after 3 cycles not "
                 "harshness. (provenance untagged in source)",
            confounds="corrected July 2, 2026 from mislogged Rig 5.",
        ),
        Citation(
            source='dbrb R1',
            role='confirms',
            provenance='ai-authored',
            gist="July 9, 2026 — Rig 6, bounded 10s-440°F hold then gentle descent to "
                 "400°F, first dab, jar opener, normalish-plus load — mild harshness at "
                 "end of cycle 1, session ended one draw into cycle 2 on satiety, not "
                 "harshness. (provenance untagged in source)",
            confounds="dbrb R1 fits with caveats: mild harshness did appear at end of "
                      "cycle 1 (just wasn't limiting), and its curve was the "
                      "bounded-hold variant rather than the pure descent — shape isn't "
                      "identical across the four.",
        ),
    ],
    positions=[
        Position(
            stated='Sessions 130, 131, 137, 152',
            text="All four ended on something other than a harshness threshold — "
                 "material depletion (FW106 R23), overwhelming intensity (WM R16, "
                 "bp4rw13 R5), or satiety (dbrb R1) was the stopping condition instead. "
                 "Opening hot and moving away from peak temperature immediately "
                 "front-loads the terpene bolus without sustaining high-temperature "
                 "exposure through the session. Cross-strain consistency is directional "
                 "— but all four runs are Rig 6 (WM R16 and bp4rw13 R5 corrected July "
                 "2, 2026); no descent run has actually been logged on Rig 5, so "
                 "cross-rig generalization is untested. All four were first-dab runs "
                 "(session-order confound absent). Load varied; load size is an "
                 "unresolved secondary variable. dbrb R1 fits with caveats: mild "
                 "harshness did appear at end of cycle 1 (just wasn't limiting), and "
                 "its curve was the bounded-hold variant rather than the pure descent — "
                 "shape isn't identical across the four.",
        ),
    ],
    watch_for="A descent run on Rig 5 (none logged yet) would test cross-rig "
              "generalization; holding load constant would isolate the unresolved load "
              "variable.",
    updated='Sessions 130, 131, 137, 152; rig corrections July 2, 2026; dbrb R1 July 9, 2026',
)
