# Dabby — phone capture (experiment branch)

Eric logs dab sessions on a Dr. Dabber Switch². This branch tests a minimal loop. Read nothing at startup. Replies are at most three lines: the facts first, then room for the voice in `Dabby_Handoff_Notes.md`'s Voice & Role section (read it once, only when a reply calls for more than facts). Never ask more than one question per turn.

**When he names a jar (before or after a dab):**
1. `python3 pending_dab.py start` (captures the timestamp; do this before anything else).
2. Find the slug in `jar_manifest.py`, read `jars/<slug>.py`.
3. `PYTHONIOENCODING=utf-8 python3 pending_dab.py brief` for rig and dab-of-day.
4. Reply with one line: jar, rig, curve if he named one, and the jar's `next_text` verbatim. Then wait.

If the jar or rig doesn't exist, say so in one line and stop; he'll handle it on desktop.

**When he reports the dab:**
1. `PYTHONIOENCODING=utf-8 python3 pending_dab.py consume` for the paste-ready timestamp fields.
2. Append a `CompletedRun` to that jar's `RUNS`, copying the shape of the previous run. Fields: `strain`, `run_date`, `sessions_prior_today`, `utc_logged_at` (from consume); `waypoints` = a new local constant in the jar file copied from `PRESETS[color]` in `Dabby_Core.py` when he names a slot color (grey, orange, teal, blue, purple), or reuse the jar's existing constant if one already has those exact waypoints; if he names no curve, ask one question; `equipment` = the rig from brief (`RIG_N`); `duration_seconds` = the last waypoint's `time_s`; `endpoint_note='<strong>Open:</strong> X°F &nbsp;|&nbsp; <strong>Floor:</strong> Y°F'` from the first and last waypoint; `swab` = what he said, or `'Not recorded'`; `dab_notes` = his words verbatim; `session_char=''`, `intensity=None`, `analysis=''`.
3. Update `STATUS.next_text` only if he said what to try next, in his words.
4. `python3 Dabby_Log_Generator.py`. If it errors, fix the jar edit; don't tell him unless you can't.
5. `git add jars/ index.html HANDOFF_STATE.md WISDOM_BRIEF.md && git commit -m "Log <jar> run" && git push`.
6. Open a PR into `phone-capture` with the GitHub MCP `create_pull_request` tool (no `gh` here), one plain sentence, then merge it with `merge_pull_request`. Don't wait for approval; it's a data-only change.
7. Reply, up to three lines: what was recorded.

No analysis, no readback ritual, no PR, no handoff or wisdom edits. Swab is the only thing worth one gentle ask if missing. Timezone America/Denver.
