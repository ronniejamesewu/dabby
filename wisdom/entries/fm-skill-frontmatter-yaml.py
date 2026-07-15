from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-skill-frontmatter-yaml',
    kind='failure-mode',
    claim="An unquoted YAML plain-scalar `description:` containing a colon-space "
          "fails skill frontmatter parsing; the harness silently falls back to the "
          "title-cased directory name, so the description degrades to the bare "
          "skill name.",
    guidance="No structural guard exists. After editing any skill's `description`, "
             "verify the live skill list renders the full text, not the bare name. "
             "Avoid \": \" inside plain-scalar descriptions — use an em dash (the "
             "review fix) or a block scalar.",
    evidence=[
        Citation(
            source='session:150',
            role='confirms',
            provenance='ai-authored',
            gist="Found July 6, 2026 (Session 150 skill-library review) — dab and "
                 "log-run had shipped this way, so the two highest-traffic skills "
                 "were routing on one-word descriptions (\"Dab\", \"Log Run\"). "
                 "Provenance untagged in source.",
            confounds="none noted",
        ),
    ],
    updated='Session 150 (July 6, 2026)',
)
