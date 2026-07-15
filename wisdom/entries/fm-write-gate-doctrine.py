from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-write-gate-doctrine',
    kind='failure-mode',
    claim="Write-gate doctrine in a skill's trigger-visible description reads to the "
          "router as a firing condition; intent is unverifiable at trigger time, so the "
          "model errs toward not firing — the readback silently stops appearing on "
          "results reports.",
    guidance="Trigger-visible text must contain only observable firing conditions; "
             "doctrine about downstream steps belongs in the workflow body. If readback "
             "sensitivity narrows again, diff what the routing layer actually sees, not "
             "just the file.",
    evidence=[
        Citation(
            source='session:158',
            role='confirms',
            provenance='mixed',
            gist="Regression window July 6–11, 2026: the text existed from skill "
                 "creation (July 2) but was invisible until the July 6 YAML repair "
                 "surfaced the full descriptions (see the frontmatter-degradation row "
                 "above — that fix was correct; the defect was in the surfaced "
                 "text). Multiple sessions affected; diagnosed Session 158 after the "
                 "user flagged \"Beat 1 used to fire flawlessly\".",
            confounds="none noted",
        ),
        Citation(
            source='session:162',
            role='confirms',
            provenance='mixed',
            gist="Recurred July 13, 2026 (Session 162), with the rescope already in "
                 "place: a clear finished-dab results report (\"Ok, that cycle was a "
                 "punch of terps! Almost gagging, coughing, tears...\") drew four turns "
                 "of analytical conversation — flavor, cycle-2 material, next-run "
                 "design — before the logging readback ever fired; the user had to "
                 "flag it (\"that's another fail for triggering the log a dab skill\"). "
                 "The observable-trigger fix was live, so this recurrence is model-side, "
                 "not skill-text: mid-rich-conversation the results-report trigger "
                 "didn't fire because the turn was being treated as exploration, not a "
                 "log signal.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Session 158 (July 6–11, 2026 regression)',
            text="Gate language (\"only the user initiates logging\", \"reports results "
                 "and wants them recorded\") sitting in a skill's frontmatter "
                 "description reads to the router as a firing condition; intent is "
                 "unverifiable at trigger time, so the model errs toward not firing "
                 "— the logging readback silently stops appearing on results "
                 "reports.",
        ),
        Position(
            stated='July 11, 2026',
            text="Fixed July 11, 2026: both skills rescoped so the gate binds the write "
                 "step (the readback is how \"wants it recorded\" gets confirmed; "
                 "nothing lands in a jar without approval) and triggers stay observable "
                 "(\"a results report always fires\"). Dated rescope notes left in both "
                 "skill files to prevent reversion-as-drift.",
        ),
        Position(
            stated='Session 162 (July 13, 2026)',
            text="Residual failure is judgment-layer with no mechanical guard — the "
                 "standing risk is that an engaging analytical exchange around a dab "
                 "suppresses the handoff to logging even when the trigger text is "
                 "correct. The exploration and the log trigger are not mutually "
                 "exclusive: a results report fires the readback even while the "
                 "conversation continues.",
        ),
    ],
    watch_for="Readback silently not firing on a clear results report, especially inside "
              "a rich analytical exchange around the dab where the turn reads as "
              "exploration, not a log signal.",
    updated='Diagnosed Session 158 (July 6–11 regression); fixed July 11, 2026; '
            'recurred Session 162 (July 13, 2026)',
)
