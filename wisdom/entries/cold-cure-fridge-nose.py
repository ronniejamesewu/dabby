from wisdom_core import *

ENTRY = WisdomEntry(
    key='cold-cure-fridge-nose',
    kind='pattern',
    claim="Cold-cure continues in fridge post-purchase — nose improves over time.",
    guidance="Not actionable for curve design. Relevant for interpreting cold nose "
             "observations over time — early-jar nose reads may understate eventual "
             "expression. Do not read \"improves\" as established gain — the "
             "mechanism (off-gassing, redistribution, or transformation) is "
             "unresolved without GC-MS.",
    grade='observation',
    grade_basis="Two jars, same fridge, same direction; single-session conversational "
                "report, not run-level data.",
    evidence=[
        Citation(
            source='watermellos R14',
            role='confirms',
            provenance='user-verbatim',
            gist="Pre-dab (user: \"great cold nose on this jar but doesn't at all "
                 "deliver that flavor when vaped — jar is probably continuing to cure "
                 "in the fridge\").",
            confounds="Same fridge as the other confirming jar — not independent "
                      "storage conditions.",
        ),
        Citation(
            source='conversation:bb362-fridge-nose',
            role='confirms',
            provenance='user-verbatim',
            gist="(user: \"nose today is much louder than it was when I first got it "
                 "from Matt\").",
            confounds="Same fridge as the other confirming jar — not independent "
                      "storage conditions; single-session conversational report, not "
                      "run-level data (no run number cited).",
        ),
    ],
    positions=[
        Position(
            stated='Session 102',
            text="Both are cold-cure badder stored in user's fridge. Not actionable "
                 "for curve design. Relevant for interpreting cold nose observations "
                 "over time — early-jar nose reads may understate eventual "
                 "expression. Watch for recurrence on new jars.",
        ),
        Position(
            stated='July 11, 2026',
            text="Caveat (July 11, 2026): the \"nose improves\" framing assumes "
                 "maturation, but a session's storage-physics research left the "
                 "mechanism genuinely unresolved — the louder fridge nose could be "
                 "net terpene off-gassing (depletion), structural redistribution, or "
                 "transformation, with no GC-MS to distinguish. Do not read "
                 "\"improves\" as established gain. See BACKLOG \"Fresh-press "
                 "storage — portion-and-freeze.\"",
        ),
    ],
    watch_for="Recurrence on new jars.",
    updated='Session 102, updated July 11, 2026',
)
