> **FROZEN snapshot 2026-07-11 — through July 10 runs. Jar files are the source of truth; verify each `jars/<slug>.py:<line>` anchor against the live file before citing (anchors and content drift). See README.md.**

# Rain Fruit (jars/rainfruit.py) — Extraction

## Run 1
- run_date: date(2026, 5, 10) (jars/rainfruit.py:37)
- utc_logged_at: None (jars/rainfruit.py:39)
- sessions_prior_today: 2 (jars/rainfruit.py:38)
- equipment: RIG_1 (jars/rainfruit.py:41); equipment prose notes: not stated
- waypoints: constant name RF_RUN1 (jars/rainfruit.py:6); values verbatim: (time_s=0, temp_f=380, note='Session open'), (time_s=15, temp_f=390, note='Early ascent'), (time_s=40, temp_f=410, note='Mid ascent'), (time_s=65, temp_f=430, note='Endpoint') (jars/rainfruit.py:7-10); endpoint_note: "<strong>Endpoint:</strong> 430°F — baseline ramp" [endpoint_note field, jars/rainfruit.py:42]
- load: not stated
- draws / cycles: not stated
- stopping condition: not stated
- harshness — onset timing: none reported — "No harshness." [session_char, jars/rainfruit.py:44]
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: not stated
- swab: "Notably clean — lighter than target. No darkening." [swab field, jars/rainfruit.py:43]
- reclaim: not stated
- intensity: "Strong" [intensity field, jars/rainfruit.py:45]
- water use mid-session: not stated
- flavor / character: "Really clear fruit notes throughout. Strong effects — pressure up and behind the eyes." [session_char, jars/rainfruit.py:44]
- anomalies: "utc_logged_at=None" — no timestamp captured for this run, unlike Runs 2 and 3 [utc_logged_at field, jars/rainfruit.py:39]

## Run 2
- run_date: date(2026, 5, 11) (jars/rainfruit.py:50)
- utc_logged_at: datetime(2026, 5, 11, 22, 44, tzinfo=timezone.utc) (jars/rainfruit.py:52)
- sessions_prior_today: 0 (jars/rainfruit.py:51)
- equipment: RIG_1 (jars/rainfruit.py:54); equipment prose notes: not stated
- waypoints: constant name RF_RUN2 (jars/rainfruit.py:12); values verbatim: (time_s=0, temp_f=375, note='Session open — 5°F below baseline, testing lower open'), (time_s=15, temp_f=385, note='Early ascent'), (time_s=40, temp_f=410, note='Mid ascent'), (time_s=65, temp_f=430, note='Endpoint') (jars/rainfruit.py:13-16); endpoint_note: "<strong>Endpoint:</strong> 430°F &nbsp;|&nbsp; Open 5°F below baseline — testing lower open" [endpoint_note field, jars/rainfruit.py:55]
- load: not stated
- draws / cycles: not stated
- stopping condition: not stated
- harshness — onset timing: "Got a bit hot in the last 10 seconds." [session_char, jars/rainfruit.py:57]; secondary: "Tail heat in the last 10 seconds is consistent with the cross-strain pattern at 430°F endpoints (Hive #1 Run 5, Fembot #3 Runs 1–2)." [analysis, jars/rainfruit.py:59]
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: not stated
- swab: "Light golden — clean." [swab field, jars/rainfruit.py:56]
- reclaim: not stated
- intensity: "Mild" [intensity field, jars/rainfruit.py:58]
- water use mid-session: not stated
- flavor / character: "Tasty." [session_char, jars/rainfruit.py:57]
- anomalies: none

## Run 3
- run_date: date(2026, 5, 11) (jars/rainfruit.py:63)
- utc_logged_at: datetime(2026, 5, 12, 0, 30, tzinfo=timezone.utc) (jars/rainfruit.py:65)
- sessions_prior_today: 1 (jars/rainfruit.py:64)
- equipment: RIG_1 (jars/rainfruit.py:67); equipment prose notes: not stated
- waypoints: constant name RF_RUN3 (jars/rainfruit.py:18); values verbatim: (time_s=0, temp_f=375, note='Session open'), (time_s=15, temp_f=385, note='Early ascent'), (time_s=40, temp_f=410, note='Mid ascent'), (time_s=55, temp_f=420, note='Approach endpoint — down 10°F'), (time_s=65, temp_f=420, note='Hold at 420°F for 10 seconds') (jars/rainfruit.py:19-23); endpoint_note: "<strong>Endpoint:</strong> 420°F (10-second hold) — down 10°F from prior runs" [endpoint_note field, jars/rainfruit.py:68]
- load: not stated
- draws / cycles: not stated
- stopping condition: not stated
- harshness — onset timing: not stated
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: "Notably less harshness. Slow build to intensity — not hard hitting." [session_char, jars/rainfruit.py:70]; secondary: "420°F endpoint did not produce the tail harshness that appeared at 430°F on Run 2 — consistent with the cross-strain pattern." [analysis, jars/rainfruit.py:72]
- swab: "Clean golden." [swab field, jars/rainfruit.py:69]
- reclaim: not stated
- intensity: "Mild-moderate" [intensity field, jars/rainfruit.py:71]
- water use mid-session: not stated
- flavor / character: not stated
- anomalies: none

## File notes
- total runs extracted: 3
- runs where any field was ambiguous to extract: none
