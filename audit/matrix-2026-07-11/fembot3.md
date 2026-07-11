> **FROZEN snapshot 2026-07-11 — through July 10 runs. Jar files are the source of truth; verify each `jars/<slug>.py:<line>` anchor against the live file before citing (anchors and content drift). See README.md.**

# Fembot #3 (slug: fembot3) — Extraction

## Run 1
- run_date: date(2026, 5, 9) (jars/fembot3.py:25)
- utc_logged_at: None (jars/fembot3.py:27)
- sessions_prior_today: 0 (jars/fembot3.py:26)
- equipment: RIG_1 (jars/fembot3.py:29); equipment prose notes: not stated
- waypoints: constant name FEMBOT3_RUN1 (jars/fembot3.py:6-11); values verbatim: Waypoint(time_s=0, temp_f=380, note='Session open') (jars/fembot3.py:7), Waypoint(time_s=15, temp_f=390, note='Early ascent') (jars/fembot3.py:8), Waypoint(time_s=40, temp_f=410, note='Mid ascent') (jars/fembot3.py:9), Waypoint(time_s=65, temp_f=430, note='Endpoint') (jars/fembot3.py:10); endpoint_note: "<strong>Endpoint:</strong> 430°F" [endpoint_note, jars/fembot3.py:30]
- load: not stated
- draws / cycles: not stated
- stopping condition: not stated
- harshness — onset timing: "Slight harshness at the tail." [session_char, jars/fembot3.py:32]
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: not stated
- swab: "Light golden — clean. Two heads mostly white, two with light golden coloring. No darkening." [swab field, jars/fembot3.py:31]
- reclaim: not stated
- intensity: not stated (no `intensity` field present on this CompletedRun entry)
- water use mid-session: not stated
- flavor / character: "Very tasty on the ascent. No visible vapor until mid-range." [...] "Effects upbeat, creative, not too body-heavy — consistent with sativa-dominant character." [session_char, jars/fembot3.py:32]
- anomalies: none

## Run 2
- run_date: date(2026, 5, 9) (jars/fembot3.py:39)
- utc_logged_at: None (jars/fembot3.py:41)
- sessions_prior_today: 1 (jars/fembot3.py:40)
- equipment: RIG_1 (jars/fembot3.py:43); equipment prose notes: not stated
- waypoints: constant name FEMBOT3_RUN2 (jars/fembot3.py:12-15); values verbatim: Waypoint(time_s=0, temp_f=430, note='Steady hold — flat 430°F from session open') (jars/fembot3.py:13), Waypoint(time_s=60, temp_f=430, note='Endpoint') (jars/fembot3.py:14); duration_seconds: 60 (jars/fembot3.py:44); endpoint_note: "<strong>Setpoint:</strong> 430°F steady (no ramp)" [endpoint_note, jars/fembot3.py:45]
- load: not stated
- draws / cycles: not stated
- stopping condition: not stated
- harshness — onset timing: "Harshness in the last third." [session_char, jars/fembot3.py:47]
- harshness — location (throat/chest/exhale as QUOTED): not stated
- harshness — persistence past session end: not stated
- harshness — escalation across draws: not stated
- swab: "Light golden — clean. Consistent with Run 1." [swab field, jars/fembot3.py:46]
- reclaim: not stated
- intensity: not stated (no `intensity` field present on this CompletedRun entry)
- water use mid-session: not stated
- flavor / character: "Very tasty, great effects." [session_char, jars/fembot3.py:47]
- anomalies: extra_rows note: "Try 420°F steady flat hold on Run 3." [extra_rows, jars/fembot3.py:49]; analysis note (AI-authored, secondary): "Harshness at the tail is consistent with Run 1 (ramp to 430°F endpoint) — two data points now pointing at 430°F as slightly above ideal for this material, regardless of curve shape. Swab is clean, so this is a session character signal rather than a floor indicator." [analysis, jars/fembot3.py:51]

## File notes
- total runs extracted: 2
- runs where any field was ambiguous to extract (list run numbers + one factual sentence on what was ambiguous — do NOT resolve the ambiguity yourself):
  - Run 1 and Run 2: neither CompletedRun entry in this file has an `intensity`, `load`, `draws`/`cycles`, `stopping condition`, `reclaim`, or `water use` field, nor a `dab_notes` field, so all experiential detail for those categories had to be sourced (or found absent) from the single `session_char` string per run rather than from a dedicated field.
  - Run 1 and Run 2: harshness location, persistence-past-session-end, and escalation-across-draws are not addressed anywhere in the available text (only onset timing is stated), so it is unclear whether this reflects true absence of the phenomenon or simply that it was not recorded.
