from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-cross-session-write-collision',
    kind='failure-mode',
    claim="Parallel sessions can both legitimately edit the same shared knowledge "
          "surface — a logging session's close and an open restructuring branch "
          "collided on the wisdom layer; the merge would have silently deleted the "
          "logging session's update.",
    guidance="Before merging any branch that restructures a shared surface, diff that "
             "surface against current main and transpose any concurrent delta "
             "explicitly — a session-scoped freeze cannot bind sessions that don't "
             "know about it. Per-entry sharding narrows the blast radius; same-entry "
             "edits still collide.",
    evidence=[
        Citation(
            source='session:164-vs-migration-merge-2026-07-15',
            role='confirms',
            provenance='ai-authored',
            gist="Session 164 (Sour Tangie R9/R10) updated the chest-harshness row in "
                 "HANDOFF_WISDOM.md and merged to main while the wisdom-migration "
                 "branch — which tombstones that file — was open. The migration PR "
                 "went unmergeable; resolution required transposing the Session 164 "
                 "delta verbatim into wisdom/entries/chest-harshness-hot-open.py (two "
                 "counter citations + a dated Position) before completing the merge. "
                 "No data lost; the loss was one unreviewed merge away.",
            confounds="none noted",
        ),
    ],
    updated='Session 165 (July 16, 2026)',
)
