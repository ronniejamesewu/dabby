from wisdom_core import *

ENTRY = WisdomEntry(
    key='dec-tail-harshness-pair-hunt-closed',
    kind='decision',
    claim="Tail Harshness Mechanism section audited and holds — do not re-audit for "
          "unexploited discriminating pairs",
    guidance="Do not re-run the pair-hunt across the run matrix looking for "
             "discriminating pairs. What's missing is data, not analysis — matched "
             "loads stopped at deliberately different session lengths, already named "
             "in the section as \"what would move it.\" Do not re-run the pair-hunt; "
             "run that experiment.",
    evidence=[
        Citation(
            source='session:106',
            role='context',
            provenance='ai-authored',
            gist="The empty-insert control remains one of the two strongest anchors "
                 "for the Tail Harshness Mechanism section, per the July 11, 2026 "
                 "wisdom audit's pair-hunt across the full 144-run matrix.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Session (wisdom audit, July 11, 2026)',
            text="The July 11, 2026 wisdom audit hunted the full 144-run matrix for "
                 "existing run pairs that would discriminate among the four candidate "
                 "mechanisms (vapor density / accumulated heat / airway sensitization / "
                 "particle accumulation) and found none the section doesn't already "
                 "cite; the empty-insert control and FW106 R23-vs-R5 remain the two "
                 "strongest anchors. What's missing is data, not analysis — matched "
                 "loads stopped at deliberately different session lengths, already "
                 "named in the section as \"what would move it.\" Do not re-run the "
                 "pair-hunt; run that experiment.",
        ),
    ],
    updated='Session (wisdom audit, July 11, 2026)',
)
