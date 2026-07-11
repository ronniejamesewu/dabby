> **FROZEN snapshot 2026-07-11 — through July 10 runs. Jar files are the source of truth; verify each `jars/<slug>.py:<line>` anchor against the live file before citing (anchors and content drift). See README.md.**

## Run 1
- run_date: date(2026, 7, 10) (jars/lunarz.py:24)
- utc_logged_at: datetime(2026, 7, 11, 5, 11, 1, tzinfo=timezone.utc) (jars/lunarz.py:26)
- sessions_prior_today: 2 (jars/lunarz.py:25)
- equipment: RIG_6 (jars/lunarz.py:28); equipment prose notes: not stated
- waypoints: constant name LUNARZ_HOLD10_DESCENT_GENTLE (jars/lunarz.py:27); values verbatim: Waypoint(time_s=0, temp_f=440, note='Session open — hot open'), Waypoint(time_s=10, temp_f=440, note='Hold at peak — one draw at 440°F'), Waypoint(time_s=35, temp_f=420, note='Gentle descent midpoint'), Waypoint(time_s=60, temp_f=400, note='Floor') (jars/lunarz.py:7-10)
- load: "I loaded slightly larger than normal but thank you for the warning." [dab_notes, jars/lunarz.py:34]; "slightly-larger-than-normal load" [session_char, jars/lunarz.py:32]
- draws / cycles: "[Cycle 1:] Whoa this guy wants maybe less heat. And a second cycle. I'm gonna stay on this curve but leave a note on the jar and to try a lower temp hold, maybe 430. I'll report back after second cycle." [dab_notes, jars/lunarz.py:34]
- stopping condition: "Terminated after the second one." [dab_notes, jars/lunarz.py:34]; "Stopped after the wispy draw." [session_char, jars/lunarz.py:32]
- harshness — onset timing: "Some harshness in chest after one big dense hit and one short wispy hit." [dab_notes, jars/lunarz.py:34]; "chest harshness entered on the second cycle after a dense draw and a short wispy one" [session_char, jars/lunarz.py:32]
- harshness — location (throat/chest/exhale as QUOTED): "harshness in chest" [dab_notes, jars/lunarz.py:34]; "chest harshness" [session_char, jars/lunarz.py:32]
- harshness — persistence past session end: "[Did it linger:] it lingered." [dab_notes, jars/lunarz.py:34]; "lingering past session end" [session_char, jars/lunarz.py:32]
- harshness — escalation across draws: "after one big dense hit and one short wispy hit" [dab_notes, jars/lunarz.py:34]; "after a dense draw and a short wispy one" [session_char, jars/lunarz.py:32]
- swab: "dark golden" [swab field, jars/lunarz.py:31]
- reclaim: "normal amount of reclaim" [dab_notes, jars/lunarz.py:34]; "normal reclaim" [session_char, jars/lunarz.py:32]
- intensity: "medium-high" [intensity field, jars/lunarz.py:33]
- water use mid-session: not stated
- flavor / character: "It was super flavorful throughout first cycle and first rip of second cycle. Some citrus but faint." [dab_notes, jars/lunarz.py:34]; "super flavorful through cycle 1 and the first draw of cycle 2 with faint citrus" [session_char, jars/lunarz.py:32]
- anomalies: "[Curve choice:] I'm doing the 440 10 second hold descent curve instead." [dab_notes, jars/lunarz.py:34]; endpoint_note: "10s hold at 440°F, then gentle descent; jar opener, baseline skipped" [endpoint_note, jars/lunarz.py:30]

## File notes
- total runs extracted: 1
- runs where any field was ambiguous to extract (list run numbers + one factual sentence on what was ambiguous — do NOT resolve the ambiguity yourself): Run 1 — the "harshness — escalation across draws" field has no sentence explicitly labeled as escalation; the only available text is the dab_notes/session_char description of a dense draw followed by a wispy draw, reused verbatim under that field.
