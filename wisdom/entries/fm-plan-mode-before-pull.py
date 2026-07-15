from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-plan-mode-before-pull',
    kind='failure-mode',
    claim="Plan mode entered before `git pull` leads to stale reads and missing new "
          "`RIG_N` constants.",
    guidance="Exit plan mode first if already in it. The dab skill sequences capture "
             "→ sync ahead of everything else.",
    evidence=[],
    resolution="Plan mode entered before `git pull` — the dab skill sequences capture "
               "→ sync ahead of everything else.",
    updated='Structurally resolved section (July 2026)',
)
