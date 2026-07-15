from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-closed-jar-prose',
    kind='failure-mode',
    claim="Jar closed with active-planning prose intact when next_text or next_ai_analysis references a run beyond the jar's completed count.",
    guidance="Reframe closing prose away from planning mode. Use: \"Not my jar — [N] dabs. If it shows up again: [starting point].\" Code validates this pattern.",
    evidence=[],
    updated='July 4 (analysis-toolkit skill)',
    resolution="Jar closed with active-planning prose intact — _check_closed_tier() errors when next_text/next_ai_analysis references runs beyond completed count.",
)
