> **FROZEN snapshot 2026-07-11 — through July 10 runs. Jar files are the source of truth; verify each `jars/<slug>.py:<line>` anchor against the live file before citing (anchors and content drift). See README.md.**

# Sour Tangie (sourtangie) — Extraction

## Run 1
- run_date: date(2026, 7, 10) (jars/sourtangie.py:24)
- utc_logged_at: datetime(2026, 7, 11, 1, 5, 3, tzinfo=timezone.utc) (jars/sourtangie.py:26)
- sessions_prior_today: 0 (jars/sourtangie.py:25)
- equipment: RIG_6 (jars/sourtangie.py:28); equipment prose notes: not stated
- waypoints: constant name SOURTANGIE_HOLD10_DESCENT_GENTLE (jars/sourtangie.py:27, defined jars/sourtangie.py:6-11); values verbatim: Waypoint(time_s=0, temp_f=440, note='Session open — hot open'), Waypoint(time_s=10, temp_f=440, note='Hold at peak — one draw at 440°F'), Waypoint(time_s=35, temp_f=420, note='Gentle descent midpoint'), Waypoint(time_s=60, temp_f=400, note='Floor') (jars/sourtangie.py:7-10)
- load: "The format is super sticky, it reminds me of taffy, so hard to precisely portion load. But I'm pretty sure I loaded a small one." [dab_notes, jars/sourtangie.py:34]; "small taffy load" [session_char, jars/sourtangie.py:32]
- draws / cycles: not stated
- stopping condition: "full 60s" [session_char, jars/sourtangie.py:32]; "[Full 60 on both.]" [dab_notes, jars/sourtangie.py:34]
- harshness — onset timing: none reported ("no harshness reported" [session_char, jars/sourtangie.py:32])
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: not stated
- swab: "dark amber" [swab field, jars/sourtangie.py:31]
- reclaim: "minimal reclaim" [session_char, jars/sourtangie.py:32]
- intensity: "strong" [intensity field, jars/sourtangie.py:33]
- water use mid-session: not stated
- flavor / character: not stated (analysis notes "No flavor read this session, so the inferred limonene/bitter-citrus signature is still untested solo." [analysis, jars/sourtangie.py:35])
- anomalies: "jar opener, baseline skipped" [endpoint_note, jars/sourtangie.py:30]; "I did my dab at the 440 hold descent." [dab_notes, jars/sourtangie.py:34]; "Both swabs, I thought it was weird too." [dab_notes, jars/sourtangie.py:34]; "Strong on a deliberately modest load validates the 710 first-run potency caution: the jar is potent and the small load was the right call." [analysis, jars/sourtangie.py:35]

## Run 2
- run_date: date(2026, 7, 10) (jars/sourtangie.py:39)
- utc_logged_at: datetime(2026, 7, 11, 1, 10, 0, tzinfo=timezone.utc) (jars/sourtangie.py:41)
- sessions_prior_today: 1 (jars/sourtangie.py:40)
- equipment: RIG_6 (jars/sourtangie.py:43); equipment prose notes: not stated
- waypoints: constant name SOURTANGIE_430 (jars/sourtangie.py:42, defined jars/sourtangie.py:13-18); values verbatim: Waypoint(time_s=0, temp_f=380, note='Session open'), Waypoint(time_s=4, temp_f=400, note='Steep early climb'), Waypoint(time_s=8, temp_f=430, note='Endpoint'), Waypoint(time_s=60, temp_f=430, note='Hold') (jars/sourtangie.py:14-17)
- load: "bigger-than-normal load" [session_char, jars/sourtangie.py:47]; "[Load:] bigger than normal but I wouldn't say large." [dab_notes, jars/sourtangie.py:49]
- draws / cycles: "She took a big draw starting at 380 and coughed and gagged. Didn't want any more so I finished the rest on that curve." [dab_notes, jars/sourtangie.py:49]
- stopping condition: "full 60s" [session_char, jars/sourtangie.py:47]; "remainder finished on the 430°F hold" [session_char, jars/sourtangie.py:47]; "[Full 60.]" [dab_notes, jars/sourtangie.py:49]
- harshness — onset timing: "coughed/gagged at the 380°F open" [session_char, jars/sourtangie.py:47]; "She took a big draw starting at 380 and coughed and gagged." [dab_notes, jars/sourtangie.py:49]
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: not stated
- swab: "dark amber" [swab field, jars/sourtangie.py:46]; "a shade darker than Run 1, same to a casual eye" [session_char, jars/sourtangie.py:47]; "[Swab:] dark amber, minimal — Sarah's dab maybe slightly darker but casual observer would say same." [dab_notes, jars/sourtangie.py:49]
- reclaim: "minimal reclaim" [session_char, jars/sourtangie.py:47]
- intensity: "strong" [intensity field, jars/sourtangie.py:48]; "[Intensity:] strong strong." [dab_notes, jars/sourtangie.py:49]
- water use mid-session: not stated
- flavor / character: not stated
- anomalies: "Loaded for a big-draw-first, occasional-user opener who coughed/gagged at the 380°F open and tapped out; remainder finished on the 430°F hold." [session_char, jars/sourtangie.py:47]; "I had most of Sarah's dab running on a 380 to 430 ascent curve we ran before, a baseline variation. I did the majority of the 430 part. Sarah is my wife, I loaded her a dab and switched the curve to the ascent to 430 curve." [dab_notes, jars/sourtangie.py:49]

## File notes
- total runs extracted: 2
- runs where any field was ambiguous to extract (list run numbers + one factual sentence on what was ambiguous — do NOT resolve the ambiguity yourself): Run 2 — the "harshness — escalation across draws" field is ambiguous because dab_notes and session_char describe a single big-draw cough/gag event at session open followed by tap-out, not a described progression across multiple draws, so it was left as "not stated" rather than mapped to the escalation field.
