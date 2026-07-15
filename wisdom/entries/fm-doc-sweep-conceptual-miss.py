from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-doc-sweep-conceptual-miss',
    kind='failure-mode',
    claim="Doc sweep for renamed/deleted artifacts misses conceptual workflow "
          "descriptions — grepping only for literal filename occurrences when "
          "sweeping docs after a rename or delete.",
    guidance="After replacing literal filename occurrences, scan each doc for "
             "add/edit/read workflow instructions and verify they still make sense "
             "against the new architecture. Filename grep is necessary but not "
             "sufficient.",
    evidence=[
        Citation(
            source='session:108',
            role='confirms',
            provenance='ai-authored',
            gist="Session 108 — per-jar migration doc sweep: first pass found 4 "
                 "literal `Dabby_Data.py` occurrences and replaced them; second pass "
                 "(after user flagged) found 5 more instructions describing the old "
                 "workflow without naming the file (provenance untagged in source).",
            confounds="none noted",
        ),
    ],
    updated='Session 108',
)
