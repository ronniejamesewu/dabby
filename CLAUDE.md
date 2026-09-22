# Dabby — phone capture (experiment branch)

Eric logs dab sessions on a Dr. Dabber Switch². This branch tests a minimal loop. Read nothing at startup. Reply in one line unless he asks for more. Never ask more than one question per turn.

**When he names a jar (before or after a dab):**
1. `python3 pending_dab.py start` (captures the timestamp; do this before anything else).
2. Find the slug in `jar_manifest.py`, read `jars/<slug>.py`.
3. `PYTHONIOENCODING=utf-8 python3 pending_dab.py brief` for rig and dab-of-day.
4. Reply with one line: jar, rig, curve if he named one, and the jar's `next_text` verbatim. Then wait.

If the jar or rig doesn't exist, say so in one line and stop; he'll handle it on desktop.

**When he reports the dab:**
1. `PYTHONIOENCODING=utf-8 python3 pending_dab.py consume` for the paste-ready timestamp fields.
2. Append a `CompletedRun` to that jar's `RUNS`, copying the shape of the previous run. Fields: `strain`, `run_date`, `sessions_prior_today`, `utc_logged_at` (from consume); `waypoints` = the jar's constant matching the curve he named (match on the comment or name; if none matches, ask one question); `equipment` = the rig from brief (`RIG_N`); `duration_seconds=60`; `endpoint_note='<strong>Open:</strong> X°F &nbsp;|&nbsp; <strong>Floor:</strong> Y°F'` from the first and last waypoint; `swab` = what he said, or `'Not recorded'`; `dab_notes` = his words verbatim; `session_char=''`, `intensity=None`, `analysis=''`.
3. Update `STATUS.next_text` only if he said what to try next, in his words.
4. `python3 Dabby_Log_Generator.py`. If it errors, fix the jar edit; don't tell him unless you can't.
5. `git add jars/ index.html HANDOFF_STATE.md WISDOM_BRIEF.md && git commit -m "Log <jar> run" && git push`.
6. Reply with one line: what was recorded.

No analysis, no readback ritual, no PR, no handoff or wisdom edits. Swab is the only thing worth one gentle ask if missing. Timezone America/Denver.
