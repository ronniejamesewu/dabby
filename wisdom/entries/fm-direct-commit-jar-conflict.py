from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-direct-commit-jar-conflict',
    kind='failure-mode',
    claim="Direct commit to main causing a jar-file merge conflict: committing data "
          "changes directly to main between sessions, where a PR whose branch was cut "
          "before it is later merged, risks a jars/<slug>.py merge conflict silently "
          "dropping run data.",
    guidance="Never commit data directly to main — use a feature branch and PR.",
    evidence=[],
    positions=[
        Position(
            stated='Not yet observed',
            text="`deploy.yml` always regenerates `index.html` from source, so index "
                 "staleness is not the risk. The risk is a `jars/<slug>.py` merge "
                 "conflict silently dropping run data. The per-jar split narrows the "
                 "blast radius — two sessions editing different jars no longer collide "
                 "— but two edits to the *same* jar still can. Never commit data "
                 "directly to main — use a feature branch and PR.",
        ),
    ],
    updated='Not yet observed',
)
