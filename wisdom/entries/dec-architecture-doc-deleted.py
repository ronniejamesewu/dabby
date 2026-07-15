from wisdom_core import *

ENTRY = WisdomEntry(
    key='dec-architecture-doc-deleted',
    kind='decision',
    claim="`DABBY_ARCHITECTURE.md` deleted — Steps 5–6 moved to backlog as concise "
          "items",
    guidance="Doc was written for an active 6-step refactor; Steps 1–4 complete, Steps "
             "5–6 are both CLAUDE.md edits that don't need 1000 lines of planning "
             "context. Valuable settled content already lives in `HANDOFF_WISDOM.md` "
             "and `CLAUDE.md`; history is in git.",
    evidence=[
        Citation(
            source='session:109',
            role='context',
            provenance='ai-authored',
            gist="Doc was written for an active 6-step refactor; Steps 1–4 complete, "
                 "Steps 5–6 are both CLAUDE.md edits that don't need 1000 lines of "
                 "planning context. Valuable settled content already lives in "
                 "`HANDOFF_WISDOM.md` and `CLAUDE.md`; history is in git.",
            confounds="none noted",
        ),
    ],
    updated='Session 109',
)
