> **FROZEN snapshot 2026-07-11 — through July 10 runs. Jar files are the source of truth; verify each `jars/<slug>.py:<line>` anchor against the live file before citing (anchors and content drift). See README.md.**

## Run 1
- run_date: date(2026, 5, 10) (jars/mbd.py:42)
- utc_logged_at: None (jars/mbd.py:44)
- sessions_prior_today: 0 (jars/mbd.py:43)
- equipment: RIG_1 (jars/mbd.py:46); equipment prose notes: not stated
- waypoints: constant name MBD_RUN1 (jars/mbd.py:6); values verbatim: (time_s=0, temp_f=380, note='Session open'), (time_s=15, temp_f=390, note='Early ascent'), (time_s=40, temp_f=410, note='Mid ascent'), (time_s=65, temp_f=430, note='Endpoint') (jars/mbd.py:7-10); endpoint_note: "<strong>Endpoint:</strong> 430°F" [endpoint_note, jars/mbd.py:47]
- load: not stated
- draws / cycles: not stated
- stopping condition: not stated
- harshness — onset timing: "No harshness on either run." [analysis, jars/mbd.py:63] (note: this quote is stored in Run 2's `analysis` field, not in Run 1's own record — see File notes)
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: not stated
- swab: "Darker golden — between light golden target and amber. Nothing tasted burnt. Flagged as something to watch on subsequent runs." [swab field, jars/mbd.py:48]
- reclaim: not stated
- intensity: "Mild — tolerance confound (5 sessions prior day)" [intensity field, jars/mbd.py:50]
- water use mid-session: not stated
- flavor / character: "Tasty first half, second half faded to generic." [session_char, jars/mbd.py:49]
- anomalies: none

## Run 2
- run_date: date(2026, 5, 10) (jars/mbd.py:54)
- utc_logged_at: None (jars/mbd.py:56)
- sessions_prior_today: 1 (jars/mbd.py:55)
- equipment: RIG_1 (jars/mbd.py:58); equipment prose notes: not stated
- waypoints: constant name MBD_RUN2 (jars/mbd.py:12); values verbatim: (time_s=0, temp_f=380, note='Session open — same curve as Run 1'), (time_s=15, temp_f=390, note='Early ascent'), (time_s=40, temp_f=410, note='Mid ascent'), (time_s=65, temp_f=430, note='Endpoint') (jars/mbd.py:13-16); endpoint_note: "<strong>Endpoint:</strong> 430°F — same as Run 1" [endpoint_note, jars/mbd.py:59]
- load: not stated
- draws / cycles: not stated
- stopping condition: not stated
- harshness — onset timing: "No harshness on either run." [analysis, jars/mbd.py:63]
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: not stated
- swab: "Lighter than Run 1 — closer to the light golden target." [swab field, jars/mbd.py:60]
- reclaim: not stated
- intensity: "Moderate" [intensity field, jars/mbd.py:62]
- water use mid-session: not stated
- flavor / character: "Distinct bacon character on the first half." [session_char, jars/mbd.py:61]; "Flavor expressed distinctly on the first half." [analysis, jars/mbd.py:63]
- anomalies: none

## Run 3
- run_date: date(2026, 5, 11) (jars/mbd.py:67)
- utc_logged_at: datetime(2026, 5, 12, 5, 24, tzinfo=timezone.utc) (jars/mbd.py:69)
- sessions_prior_today: 2 (jars/mbd.py:68)
- equipment: RIG_1 (jars/mbd.py:71); equipment prose notes: not stated
- waypoints: constant name MBD_RUN3 (jars/mbd.py:18); values verbatim: (time_s=0, temp_f=375, note='Session open'), (time_s=15, temp_f=385, note='Early ascent'), (time_s=40, temp_f=410, note='Mid ascent'), (time_s=55, temp_f=420, note='Approach endpoint — down 10°F from prior runs'), (time_s=65, temp_f=420, note='Hold at 420°F for 10 seconds') (jars/mbd.py:19-23); endpoint_note: "<strong>Endpoint:</strong> 420°F (10-second hold) — down 10°F, ramp from 375°F open" [endpoint_note, jars/mbd.py:72]
- load: not stated
- draws / cycles: not stated
- stopping condition: not stated
- harshness — onset timing: "Little bit harsh in the last 5 seconds." [session_char, jars/mbd.py:74]
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: "No harshness earlier in the session." [session_char, jars/mbd.py:74]
- swab: "Clean golden." [swab field, jars/mbd.py:73]
- reclaim: not stated
- intensity: "Medium-hard" [intensity field, jars/mbd.py:75]
- water use mid-session: not stated
- flavor / character: not stated
- anomalies: run_date=date(2026, 5, 11) (jars/mbd.py:67) vs utc_logged_at=datetime(2026, 5, 12, 5, 24, tzinfo=timezone.utc) (jars/mbd.py:69) — the two dates fall on different UTC calendar days.

## Run 4
- run_date: date(2026, 5, 12) (jars/mbd.py:79)
- utc_logged_at: datetime(2026, 5, 13, 2, 30, tzinfo=timezone.utc) (jars/mbd.py:81)
- sessions_prior_today: 0 (jars/mbd.py:80)
- equipment: RIG_1 (jars/mbd.py:83); equipment prose notes: not stated
- waypoints: constant name MBD_RUN4 (jars/mbd.py:25); values verbatim: (time_s=0, temp_f=380, note='Session open — same as Runs 1 and 2'), (time_s=15, temp_f=390, note='Early ascent'), (time_s=40, temp_f=410, note='Mid ascent'), (time_s=65, temp_f=430, note='Endpoint') (jars/mbd.py:26-29); endpoint_note: "<strong>Endpoint:</strong> 430°F — same as Runs 1 and 2" [endpoint_note, jars/mbd.py:84]
- load: not stated
- draws / cycles: not stated
- stopping condition: not stated
- harshness — onset timing: "Tail harshness again, consistent with prior 430°F runs." [session_char, jars/mbd.py:86]
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: not stated
- swab: "Light golden." [swab field, jars/mbd.py:85]
- reclaim: not stated
- intensity: "Big effect, seemingly short duration." [intensity field, jars/mbd.py:87]
- water use mid-session: not stated
- flavor / character: "Interesting bitter note throughout — citrus rind character." [session_char, jars/mbd.py:86]
- anomalies: run_date=date(2026, 5, 12) (jars/mbd.py:79) vs utc_logged_at=datetime(2026, 5, 13, 2, 30, tzinfo=timezone.utc) (jars/mbd.py:81) — the two dates fall on different UTC calendar days.

## File notes
- total runs extracted: 4
- runs where any field was ambiguous to extract (list run numbers + one factual sentence on what was ambiguous — do NOT resolve the ambiguity yourself): Run 1 — the only harshness-related text found ("No harshness on either run.") is located in Run 2's `analysis` field (jars/mbd.py:63), not within Run 1's own `CompletedRun` entry, so its attribution to Run 1 specifically is not directly anchored.
