from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-frozen-prose-not-promoted',
    kind='failure-mode',
    claim="Actionable guidance with forward operational value, captured only in frozen "
          "run prose (dab_notes/analysis) and never promoted to an operational layer, "
          "never fires again — no session-open surface re-reads frozen prose.",
    guidance="When a run captures guidance with forward operational value, promote it to "
             "an operational layer (wisdom row, protocol line, or skill step) at session "
             "close — frozen prose is archival, not operational.",
    evidence=[
        Citation(
            source='papzp22 R1',
            role='confirms',
            provenance='ai-authored',
            gist="710 Labs' \"don't go hard on first run of a jar, unknown potency\" "
                 "packaging note was captured in papzp22 R1's notes (June 13, 2026, "
                 "discovered post-hoc after three cycles) and never promoted. "
                 "(Provenance untagged in source.)",
            confounds="none noted",
        ),
        Citation(
            source='dbrb R1',
            role='confirms',
            provenance='mixed',
            gist="dbrb R1's jar opener then ran the heaviest-delivery curve with no "
                 "warning — user dizzy post-session, asked \"did you forget to warn "
                 "me?\"",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Session 152 (July 9, 2026)',
            text="Fix direction: backlog item \"First-run-of-jar potency caution\" "
                 "(mechanical caution line in the session-open brief for zero-run jars). "
                 "General rule until mechanized: when a run captures guidance with "
                 "forward operational value, promote it to an operational layer (wisdom "
                 "row, protocol line, or skill step) at session close — frozen prose is "
                 "archival, not operational.",
        ),
    ],
    updated='Session 152 (July 9, 2026)',
)
