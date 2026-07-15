from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-equipment-list-position',
    kind='failure-mode',
    claim="Equipment default taken from `COMPLETED_RUNS` list position (manifest order, "
          "not chronology).",
    guidance="Post-dated runs still need the chronology check against their own "
             "`utc_logged_at` (log-run skill, step 2).",
    grade_basis="Session 140; seven runs corrected in PR #206.",
    evidence=[
        Citation(
            source='session:Session 140',
            role='confirms',
            provenance='ai-authored',
            gist="Seven runs corrected in PR #206.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Session 140',
            text="`HANDOFF_STATE.md` generates the \"Most recent run (all jars, by "
                 "utc_logged_at)\" line; the default is read, not derived.",
        ),
    ],
    updated='Session 140 (PR #206)',
    resolution="Equipment default taken from `COMPLETED_RUNS` list position (manifest "
               "order, not chronology).",
)
