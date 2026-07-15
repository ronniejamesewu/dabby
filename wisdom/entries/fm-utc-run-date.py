from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-utc-run-date',
    kind='failure-mode',
    claim="UTC date used as local run_date — run_date field recorded UTC calendar "
          "date instead of America/Denver local date.",
    guidance="validate() rejects any run_date later than the America/Denver calendar "
             "date of its utc_logged_at. Use pending_dab.py consume to print "
             "paste-ready date/timestamp lines.",
    evidence=[
        Citation(
            source='oc R6',
            role='confirms',
            provenance='ai-authored',
            gist="run_date used UTC calendar date — provenance untagged in source.",
            confounds="None noted.",
        ),
        Citation(
            source='oc R7',
            role='confirms',
            provenance='ai-authored',
            gist="run_date used UTC calendar date — provenance untagged in source.",
            confounds="None noted.",
        ),
        Citation(
            source='hive1 R4',
            role='confirms',
            provenance='ai-authored',
            gist="run_date used UTC calendar date — provenance untagged in source.",
            confounds="None noted.",
        ),
        Citation(
            source='hive1 R5',
            role='confirms',
            provenance='ai-authored',
            gist="run_date used UTC calendar date — provenance untagged in source.",
            confounds="None noted.",
        ),
        Citation(
            source='papzp22 R4',
            role='confirms',
            provenance='ai-authored',
            gist="run_date used UTC calendar date — provenance untagged in source.",
            confounds="None noted.",
        ),
        Citation(
            source='papzp22 R5',
            role='confirms',
            provenance='ai-authored',
            gist="run_date used UTC calendar date — provenance untagged in source.",
            confounds="None noted.",
        ),
    ],
    resolution="Caught by validate() — run_date must not exceed the America/Denver "
               "calendar date of utc_logged_at.",
    updated='Pre-July-3, 2026',
)
