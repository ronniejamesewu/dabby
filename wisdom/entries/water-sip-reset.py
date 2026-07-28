from wisdom_core import *

ENTRY = WisdomEntry(
    key='water-sip-reset',
    kind='pattern',
    claim="Water sip clears mid-session harshness — threshold reset, not suppression. "
          "Usually resets mid-session harshness on Rig 6, but the reset is not "
          "guaranteed.",
    guidance="Water usually resets mid-session harshness on Rig 6, but not reliably — "
             "six full resets against three partials, Sour Tangie R5 a full "
             "non-response, and bb362 R7 (Rig 7) a non-reset read as relocation toward "
             "the chest. Both Rig 7 instances failed the clean Rig 6 reset; cross-rig "
             "looks worse, not just untested.",
    grade='observation',
    grade_basis="Twelve instances, six strains — ten Rig 6, two Rig 7 (papzp22 R10 "
                "partial, bb362 R7 a non-reset read as relocation); neither cross-rig "
                "instance is a clean reset.",
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
            source='lunarz R4',
            role='confirms',
            provenance='user-verbatim',
            gist="July 19, 2026 — 430°F 15s extended-hold descent (\"purple\"), Rig 6 "
                 "— \"super dry\" throat harshness, a water sip helped; degree of "
                 "reset (full vs partial) not specified.",
            confounds="2nd dab, large load, three cycles; heavy terpene coughing; "
                      "full-vs-partial reset not stated.",
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
        Citation(
            source='oc R15',
            role='counters',
            provenance='user-verbatim',
            gist="July 17, 2026 — \"purple\" 430°F 15s-hold descent, chest/heartburn "
                 "harshness: a water sip between hits softened it but it returned to "
                 "prior level by the end of cycle 2 — a partial, temporary reduction "
                 "like LunarZ R3, not a full reset. The second partial-only response "
                 "in the log.",
            confounds="2nd dab, big (~double) load, two cycles; chest-located "
                      "harshness under heavy cumulative exposure, single-run weight.",
        ),
        Citation(
            source='papzp22 R10',
            role='counters',
            provenance='user-verbatim',
            gist="July 22, 2026 — grey 450°F, Rig 7 (SAML RBR wet top) debut — a water "
                 "sip brought the chest/heartburn down 'somewhat' but did not clear it; "
                 "a partial reduction like LunarZ R3 and OC R15, the third partial-only "
                 "response in the log, and the first instance on a rig other than Rig 6.",
            confounds="First non-Rig-6 instance (the cross-rig watch_for), but heavily "
                      "confounded — RBR debut, large load, chest-located harshness, "
                      "upright-posture change in cycle 2; degree ('somewhat') not "
                      "quantified.",
        ),
        Citation(
            source='bb362 R7',
            role='counters',
            provenance='user-verbatim',
            gist="July 23, 2026 — purple 430°F descent, Rig 7 (SAML RBR wet top), 4th "
                 "dab — a small cycle-1 throat harshness did not reset on a water sip; "
                 "on the user's read the water \"washed the harshness further down the "
                 "esophagus,\" turning it to heartburn. Not a reduction at all — the "
                 "log's first instance of water apparently relocating harshness toward "
                 "the chest rather than clearing it. Second Rig 7 datum (after papzp22 "
                 "R10).",
            confounds="4th dab (heavy cumulative exposure); Rig 7 / RBR top; "
                      "chest-located outcome; single vivid instance at the user's-read "
                      "weight — relocation is a sensation report, not a measured route.",
        ),
    ],
    positions=[
        Position(
            stated='Sessions 123, updated 136, 158, 159, 160, 171, 172',
            text="Mechanism unresolved across all ten instances — particulate load, "
                 "mucosal sensitization, and thermal sensitization are all consistent. "
                 "What water reset (and how quickly) is not distinguishable from these "
                 "data. Operationally: water mid-session usually resets mid-session "
                 "harshness on Rig 6, but the reset is not guaranteed — six full resets "
                 "plus LunarZ R4 (helped, full-vs-partial unstated), two partial "
                 "reductions (LunarZ R3, OC R15), and Sour Tangie R5 the first outright "
                 "non-response (under a heavy cumulative load). Whether it generalizes "
                 "to other rigs is untested.",
        ),
        Position(
            stated='Session 174 (July 22, 2026)',
            text="papzp22 R10 is the first non-Rig-6 instance (Rig 7, SAML RBR wet top) "
                 "and a partial reduction — the third partial-only response (with LunarZ "
                 "R3, OC R15), so partial-not-full now has three instances against six "
                 "full resets. It touches the cross-rig watch_for but does not answer it: "
                 "one partial datum on a new top, itself confounded by the RBR debut, a "
                 "large load, chest-located harshness, and a within-session posture "
                 "change — not clean cross-rig generalization. Held at observation.",
        ),
        Position(
            stated='July 23, 2026 (bb362 R7)',
            text="Second non-Rig-6 instance and the log's first apparent relocation: on "
                 "the RBR wet top (Rig 7) a water sip did not reset a cycle-1 throat "
                 "harshness — the user's read was that it washed the harshness further "
                 "down toward the esophagus, turning it to heartburn. With papzp22 R10 "
                 "(also Rig 7, partial-only), both cross-rig instances have now failed "
                 "the clean Rig 6 reset. Confounded (4th dab, chest-located, RBR top, "
                 "user's-sensation weight), so it does not establish a rig mechanism — "
                 "but it moves the cross-rig read from 'untested' toward 'looks worse.' "
                 "Held at observation.",
        ),
    ],
    watch_for="A clean Rig 6-style full reset reproducing off Rig 6 — both Rig 7 "
              "instances so far have failed it; and whether the bb362 R7 relocation "
              "reading recurs.",
    updated='Sessions 123, 136, 158, 159, 160, 171 (July 19, 2026); oc R15 Session 172 (July 17, 2026); papzp22 R10 Session 174 (July 22, 2026); bb362 R7 July 23, 2026',
)
