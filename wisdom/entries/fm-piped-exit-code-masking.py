from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-piped-exit-code-masking',
    kind='failure-mode',
    claim="Piping the generator's output (e.g. through tail) masks its exit code — a "
          "failing validation looks green to a shell chain keyed on the pipe's last "
          "command, and a broken state can be committed and pushed before anyone "
          "notices.",
    guidance="Check the generator's exit status explicitly — run it unpiped, or test "
             "its own status immediately — before any commit that includes its "
             "outputs. A red generator inside a green-looking pipeline has shipped "
             "once already.",
    evidence=[
        Citation(
            source='session:wisdom-migration-2026-07-15',
            role='confirms',
            provenance='ai-authored',
            gist="During review-finding fixes, a fix script pushed a brief-rendered "
                 "field over its cap; the generator exited 1 with a WISDOM ERRORS "
                 "block, but its output was piped through tail and the && chain keyed "
                 "off tail's exit — the failing state was committed and pushed, and "
                 "caught only on the next explicit generator run.",
            confounds="none noted",
        ),
    ],
    updated='Session 165 (July 16, 2026)',
)
