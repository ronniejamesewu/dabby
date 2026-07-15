from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-push-files-content-loss',
    kind='failure-mode',
    claim="Silent content loss via GitHub MCP push_files — passing full `index.html` "
          "content as a string literal to push_files strips charts, simplifies "
          "sections.",
    guidance="Use git for all routine commits. push_files is acceptable only for "
             "temporary files on non-main branches when git checkout is impractical, "
             "and never for `index.html`.",
    evidence=[
        Citation(
            source='session:4',
            role='confirms',
            provenance='ai-authored',
            gist="Passing full `index.html` content as a string literal to push_files "
                 "(Session 4; risk persisted through ~Session 28); push_files strips "
                 "charts, simplifies sections. (provenance untagged in source)",
            confounds="none noted",
        ),
    ],
    updated='Session 4; risk persisted through ~Session 28',
)
