from wisdom_core import *

ENTRY = WisdomEntry(
    key='water-sip-reset',
    kind='pattern',
    claim="Water sip clears mid-session harshness — threshold reset, not suppression. "
          "Usually resets mid-session harshness on Rig 6, but the reset is not "
          "guaranteed.",
    guidance="Water mid-session usually resets mid-session harshness on Rig 6, but the "
             "reset is not guaranteed — six full resets, LunarZ R3 the one partial "
             "reduction, and Sour Tangie R5 the first outright non-response (under a "
             "heavy cumulative load). Whether it generalizes to other rigs is untested.",
    grade='observation',
    grade_basis="Eight instances, four strains, all on Rig 6; not yet cross-rig.",
    evidence=[
        Citation(
            source='hive1 R6',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6, 420°F baseline, 60s, first dab of day: harshness at ~43s "
                 "resolved by water mid-session — next draw through active dense vapor "
                 "was clean. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R22',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6, 425°F, second dab: harshness in inter-draw pause resolved by "
                 "water, terpene character opened. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R25',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6 — one of three further FW106 instances (R25, R28, R29): water "
                 "reduced or resolved mid-session harshness; see the frozen analyses.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R28',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6 — one of three further FW106 instances (R25, R28, R29): water "
                 "reduced or resolved mid-session harshness; see the frozen analyses.",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R29',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6 — one of three further FW106 instances (R25, R28, R29): water "
                 "reduced or resolved mid-session harshness; see the frozen analyses.",
            confounds="none noted",
        ),
        Citation(
            source='lunarz R2',
            role='confirms',
            provenance='ai-authored',
            gist="July 11, 2026 — water *between cycles* resolved mild-to-medium "
                 "heartburn-like chest harshness from cycle 1, no post-session "
                 "persistence; first between-cycle instance — prior five were "
                 "mid-session. Provenance untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='lunarz R3',
            role='counters',
            provenance='ai-authored',
            gist="July 12, 2026 — a water sip reduced but did not eliminate "
                 "mild-to-medium chest harshness — the first partial-only response in "
                 "the log; all prior six were full resets. Provenance untagged in "
                 "source.",
            confounds="heavier 4th-consecutive-dab cumulative exposure is one candidate "
                      "for the incomplete reset, single-run weight.",
        ),
        Citation(
            source='sourtangie R5',
            role='counters',
            provenance='ai-authored',
            gist="July 12, 2026 — a water sip did not clear escalating mild→medium "
                 "chest-and-throat harshness at all, the log's first full non-response. "
                 "Provenance untagged in source.",
            confounds="bigger-than-normal load, 2nd dab, two cycles, and a lot of hits "
                      "make heavy cumulative exposure / dense vapor the confound — the "
                      "harshness may have been past a resettable threshold, single-run "
                      "weight.",
        ),
    ],
    positions=[
        Position(
            stated='Sessions 123, updated 136, 158, 159, 160',
            text="Mechanism unresolved across all eight instances — particulate load, "
                 "mucosal sensitization, and thermal sensitization are all consistent. "
                 "What water reset (and how quickly) is not distinguishable from these "
                 "data. Operationally: water mid-session usually resets mid-session "
                 "harshness on Rig 6, but the reset is not guaranteed — six full resets, "
                 "LunarZ R3 the one partial reduction, and Sour Tangie R5 the first "
                 "outright non-response (under a heavy cumulative load). Whether it "
                 "generalizes to other rigs is untested.",
        ),
    ],
    watch_for="Cross-rig instances — all eight are Rig 6; generalization to other rigs "
              "is untested.",
    updated='Sessions 123, 136, 158, 159, 160',
)
