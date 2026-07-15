from wisdom_core import *

ENTRY = WisdomEntry(
    key='ramp-vs-flat-hold',
    kind='pattern',
    claim="Ramp outperforms flat hold at the same endpoint on flavor staging / "
          "session character (scoped July 11, 2026) — not on harshness, where it "
          "favors neither leg cleanly.",
    guidance="Treat the ramp advantage as scoped to flavor staging / session "
             "character, not harshness. All evidence is Rig 1 era (retired) — do not "
             "extrapolate to current rigs without a deliberate test. Swab does not "
             "distinguish curve shapes within the clean range; subjective session "
             "character is the primary readout.",
    grade='directional',
    grade_basis="2 strains, paired same-day comparisons with opposite session-order "
                "structures.",
    evidence=[
        Citation(
            source='oc R6',
            role='confirms',
            provenance='ai-authored',
            gist="Ramp, 4th session of day, at 430°F. Provenance untagged in source.",
            confounds="Paired against R7, which ran 5th in a heavy day — the OC "
                      "comparison is order-confounded.",
        ),
        Citation(
            source='oc R7',
            role='context',
            provenance='ai-authored',
            gist="Flat, 5th session of day, at 430°F. Provenance untagged in source.",
            confounds="Ran 5th in a heavy day, so its worse showing is "
                      "order-confounded.",
        ),
        Citation(
            source='hive1 R5',
            role='confirms',
            provenance='ai-authored',
            gist="Ramp, 3rd dab; won on flavor against the order gradient — \"distinct "
                 "flavors through the first two-thirds\". \"harsh in the last ~10 "
                 "seconds\". Provenance untagged in source.",
            confounds="The harshness picture favors ramp on neither leg cleanly — R5 "
                      "ramp was harsh in the last ~10 seconds while the R3 flat leg "
                      "was never harsh.",
        ),
        Citation(
            source='hive1 R3',
            role='context',
            provenance='ai-authored',
            gist="Flat, 1st dab; \"faded to generic\". \"never harsh\". Provenance "
                 "untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='hive1 R4',
            role='context',
            provenance='ai-authored',
            gist="Flat, 2nd dab. Provenance untagged in source.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Session 14',
            text="Paired same-day comparisons with opposite session-order structures. "
                 "OC R6 (ramp, 4th session of day) vs R7 (flat, 5th session of day) at "
                 "430°F; Hive1 R5 (ramp, 3rd dab) vs R3-4 (flat, 1st/2nd dab). Hive1's "
                 "ramp won on flavor AGAINST the order gradient (\"distinct flavors "
                 "through the first two-thirds\" on the 3rd dab vs \"faded to generic\" "
                 "on the 1st); OC's flat leg ran 5th in a heavy day, so its worse "
                 "showing is order-confounded.",
        ),
        Position(
            stated='July 11, 2026 audit',
            text="Scoped to flavor staging / session character (July 11, 2026 audit) — "
                 "the harshness picture favors ramp on neither leg cleanly (Hive1 R5 "
                 "ramp: \"harsh in the last ~10 seconds\"; R3 flat: \"never harsh\"). "
                 "All evidence is Rig 1 era (retired equipment). Swab does not "
                 "distinguish between curve shapes within the clean range; subjective "
                 "session character is the primary readout.",
        ),
    ],
    counter_reading="OC's flat leg ran 5th in a heavy day, so its worse showing is "
                    "order-confounded; and the harshness picture favors ramp on "
                    "neither leg cleanly (R5 ramp harsh in the last ~10s vs R3 flat "
                    "never harsh). The flavor edge may be session-order or "
                    "dimension-limited, not a curve-shape effect.",
    updated='Session 14; scoped July 11, 2026 audit',
)
