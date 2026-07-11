> **FROZEN snapshot 2026-07-11 — through July 10 runs. Jar files are the source of truth; verify each `jars/<slug>.py:<line>` anchor against the live file before citing (anchors and content drift). See README.md.**

# dbrb.py — Extraction

## Run 1
- run_date: date(2026, 7, 9) (jars/dbrb.py:17)
- utc_logged_at: datetime(2026, 7, 10, 1, 54, 21, tzinfo=timezone.utc) (jars/dbrb.py:19)
- sessions_prior_today: 0 (jars/dbrb.py:18)
- equipment: RIG_6 (jars/dbrb.py:21); equipment prose notes: "jar opener, baseline skipped" [endpoint_note, jars/dbrb.py:23]
- waypoints: constant name DBRB_HOLD10_DESCENT_GENTLE (jars/dbrb.py:20, defined jars/dbrb.py:6-11); values verbatim:
  - Waypoint(time_s=0, temp_f=440, note='Session open — hot open') (jars/dbrb.py:7)
  - Waypoint(time_s=10, temp_f=440, note='Hold at peak — one draw at 440°F') (jars/dbrb.py:8)
  - Waypoint(time_s=35, temp_f=420, note='Gentle descent midpoint') (jars/dbrb.py:9)
  - Waypoint(time_s=60, temp_f=400, note='Floor') (jars/dbrb.py:10)
- load: "load normalish, maybe a tad bigger" [dab_notes, jars/dbrb.py:27]
- draws / cycles: "full first cycle plus one draw of a second" [session_char, jars/dbrb.py:25]; "I took a thirty second break and ran second cycle. Took a good hit, still tasty, but at that point I'd had enough. I terminated the cycle." [dab_notes, jars/dbrb.py:27]
- stopping condition: "ended on satiety rather than harshness" [session_char, jars/dbrb.py:25]; "Took a good hit, still tasty, but at that point I'd had enough. I terminated the cycle." [dab_notes, jars/dbrb.py:27]
- harshness — onset timing: "It was mild, not sure when it showed up even, because of the coughing, but it was there at the end." [dab_notes, jars/dbrb.py:27]
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: "heavy terp coughing on draw 1; mild harshness at end of cycle 1, second cycle clean" [session_char, jars/dbrb.py:25]; "tasting all that was in between coughing really hard on the terps. I kind of wonder if the terps are the thing causing harshness." [dab_notes, jars/dbrb.py:27]
- swab: "golden" [swab field, jars/dbrb.py:24]
- reclaim: "minimal reclaim" [session_char, jars/dbrb.py:25]
- intensity: "big" [intensity field, jars/dbrb.py:26]
- water use mid-session: not stated
- flavor / character: "Definitely a garlic funk cold nose. Not getting a lot of fruit but it's still cold from the fridge." [dab_notes, jars/dbrb.py:27]; "I succeeded in getting both strains. So there was this garlicky cheesy note, and then there was also this lemon pledge note. Maybe a squeeze of lime." [dab_notes, jars/dbrb.py:27]; "both strains present on draw 1 — garlic-cheese and lemon-pledge/lime" [session_char, jars/dbrb.py:25]
- anomalies: "[Clarified: harshness was end of first cycle, second cycle clean as far as could tell; load normalish, maybe a tad bigger; \"Sean's\" logged as \"swabs\".]" [dab_notes, jars/dbrb.py:27]; "[Later, post-logging:] Whoa fuck dizzy." [dab_notes, jars/dbrb.py:27]; "big intensity, still climbing post-session (dizziness reported well after session end)" [session_char, jars/dbrb.py:25]; "jar opener, baseline skipped" [endpoint_note, jars/dbrb.py:23]; "Run 1, jar opener, deviating from the on-file baseline plan: the bounded 10s-440°F hold with gentle descent to 400°F that delivered on Banana Punch #4 + Randy Watzon #13 R12 two nights earlier" [analysis, jars/dbrb.py:28]

## File notes
- total runs extracted: 1
- runs where any field was ambiguous to extract: none
