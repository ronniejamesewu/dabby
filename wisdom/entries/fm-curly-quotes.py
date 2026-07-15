from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-curly-quotes',
    kind='failure-mode',
    claim="Edit-tool curly-quote contamination in HTML string attributes — manifest "
          "preflight rejects the backslash+curly signature in jar files.",
    guidance="Use single-quote HTML attributes (`style='...'`); if curly quotes "
             "appear, fix by byte position via Python script, not the Edit tool.",
    updated='undated in source',
    resolution="Edit-tool curly-quote contamination in HTML string attributes",
)
