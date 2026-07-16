from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-device-capability-overassert',
    kind='failure-mode',
    claim="Over-asserting device capability limits without verification — assuming "
          "hardware constraints (e.g. waypoint count) from device category rather than "
          "actual specs.",
    guidance="Verify device specifications before using hardware constraints as "
             "reasoning inputs.",
    evidence=[
        Citation(
            source='session:47',
            role='confirms',
            provenance='ai-authored',
            gist="Claimed Switch² waypoint count was bounded by being a consumer "
                 "device — user corrected with real limits (+10°F/sec heat, "
                 "−3°F/sec cool, 10–90s window). (provenance untagged in "
                 "source)",
            confounds="none noted",
        ),
    ],
    updated='Session 47',
)
