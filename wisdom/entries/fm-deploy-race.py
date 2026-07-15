from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-deploy-race',
    kind='failure-mode',
    claim="Deploy race condition — live site silently stale after merge",
    guidance="If the condition recurs (site stale with no error), recovery is an empty commit to main.",
    evidence=[
        Citation(
            source='session:91',
            role='confirms',
            provenance='ai-authored',
            gist="Preview cleanup moved to the daily scheduled `cleanup-previews.yml`, so nothing competes with `deploy.yml` for the `gh-pages` concurrency slot.",
            confounds="none noted",
        ),
    ],
    updated='Session 91',
    resolution="Deploy race condition on gh-pages concurrency; fixed by moving preview cleanup to daily scheduled task.",
)
