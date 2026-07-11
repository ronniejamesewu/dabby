#!/usr/bin/env python3
"""Pending-dab queue — mechanical timestamp capture and chat-ready facts for run logging.

Captures the true time of a dab the moment it is announced, so logging never
depends on anyone remembering it later (documented failure mode: timestamps
recalculated at reporting time — Sessions 121 and 140). Party mode uses the
same queue: capture verbatim fragments now, reconcile with the full logging
protocol later.

The output of `start`, `brief`, and `consume` is written in the display
register — full strain names, "Rig N — ..." expansions, plain-language curve
tables, local clock times — so the facts can be said to the user as printed.
Internal identifiers (slugs, RIG_N, field names) never appear in the
say-it-like-this sections; chat leakage of internal vocabulary is a documented
failure mode (Sessions 142–143).

Usage:
  python pending_dab.py start [--note "user's verbatim words"]
      Capture NOW as a pending dab. Run this the moment the user announces a
      dab ("about to hit it", "grabbing one", or a party-mode fragment). The
      note is optional and verbatim — never a paraphrase. Deliberately does
      NOT read the jar files: capture runs before git sync and must never fail
      because a jar is mid-edit. Facts come from `brief`, after the sync.
  python pending_dab.py brief [--strain "Fire Water #106"]
      Print the session-open facts for the dab skill's reply, resolved to
      display form from the jar data on disk: dab time and dab-of-the-day
      count, the strain's next planned run with its curve as a table, and the
      working equipment default (chronologically most recent run, all jars).
      Run it after git sync and the handoff reads.
  python pending_dab.py list
      Show pending entries, oldest first.
  python pending_dab.py consume
      Print paste-ready run_date / utc_logged_at / sessions_prior_today lines
      for the OLDEST pending entry, plus the same facts in say-it-to-the-user
      form (local time, dab-of-the-day, the equipment default as of that
      timestamp — computed per-entry, so post-dated reconciliation can't
      inherit a stale rig). Does NOT delete the entry — the generator
      auto-prunes it once a run with a matching utc_logged_at exists, and
      refuses to generate while unmatched entries remain (the tripwire in
      Dabby_Log_Generator.py).
  python pending_dab.py discard N
      Deliberately remove entry N (1-based, as shown by list) — for captures
      that will never become runs.

Storage: .pending_dabs.json beside this script — gitignored, session-local.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

from Dabby_Core import (denver_local, denver_local_date, denver_abbrev,
                        _fmt_equipment_display, fmt_curve_table)

QUEUE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.pending_dabs.json')

SAY = "── say it to the user (display form — as printed, or wrapped in your own words) ──"
ASSISTANT = "── for the assistant (not user text) ──"


def _load():
    if not os.path.isfile(QUEUE_PATH):
        return []
    with open(QUEUE_PATH, encoding='utf-8-sig') as fh:  # -sig: BOM-tolerant (PowerShell writes BOMs)
        return json.load(fh)


def _save(entries):
    with open(QUEUE_PATH, 'w', encoding='utf-8') as fh:
        json.dump(entries, fh, indent=2, ensure_ascii=False)


def _fmt(entry, idx):
    utc = datetime.fromisoformat(entry['utc'])
    local = denver_local(utc)
    note = f' — "{entry["note"]}"' if entry.get('note') else ''
    return f"  [{idx}] {local:%b %d %I:%M %p} Denver ({utc:%Y-%m-%d %H:%M} UTC){note}"


# ── display-register helpers ─────────────────────────────────────────────────

def _say_time(utc):
    """'7:42pm MDT, July 2' — a UTC timestamp as the user would say it."""
    local = denver_local(utc)
    clock = local.strftime('%I:%M%p').lstrip('0').lower()
    return f"{clock} {denver_abbrev(utc)}, {local.strftime('%B')} {local.day}"


def _say_date(d):
    """'June 29' — a date as the user would say it (no year; this log is dense)."""
    return f"{d.strftime('%B')} {d.day}"


def _ordinal(n):
    suffix = 'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"


def _load_jar_data():
    """(runs, statuses, closed_slugs) from the jar files on disk. Lazy import so
    `start` never depends on the jars being importable — capture must not fail
    because a jar is mid-edit."""
    from jar_manifest import load_all_jars, CLOSED
    runs, statuses = load_all_jars()
    return runs, statuses, set(CLOSED)


def _sessions_prior(utc, runs, other_entries=()):
    """Dabs earlier on the same Denver day: logged runs by the validator's exact
    rule (same run_date, earlier utc_logged_at, any jar) plus still-pending
    entries from earlier today that no logged run matches yet."""
    day = denver_local_date(utc)
    logged_utcs = {r.utc_logged_at for r in runs if r.utc_logged_at is not None}
    n = sum(1 for r in runs
            if r.run_date == day and r.utc_logged_at is not None and r.utc_logged_at < utc)
    for e in other_entries:
        e_utc = datetime.fromisoformat(e['utc'])
        if e_utc < utc and e_utc not in logged_utcs and denver_local_date(e_utc) == day:
            n += 1
    return n


def _latest_run(runs, before_utc=None):
    """(run, per-strain run number) for the chronologically most recent run —
    optionally only among runs logged before `before_utc` (the post-dated
    equipment-default rule). None when nothing qualifies."""
    candidates = [r for r in runs if r.utc_logged_at is not None
                  and (before_utc is None or r.utc_logged_at < before_utc)]
    if not candidates:
        return None, 0
    latest = max(candidates, key=lambda r: r.utc_logged_at)
    run_n = sum(1 for r in runs[:runs.index(latest) + 1] if r.strain == latest.strain)
    return latest, run_n


def _resolve_strain(query, statuses):
    """STATUS for a strain named loosely (full name, fragment, or slug).
    Returns (status, error_lines) — exactly one is set."""
    q = query.strip().lower()
    exact = [s for s in statuses if s.name.lower() == q or s.slug == q]
    if len(exact) == 1:
        return exact[0], None
    partial = [s for s in statuses if q in s.name.lower()]
    if len(partial) == 1:
        return partial[0], None
    if partial:
        names = "; ".join(s.name for s in partial)
        return None, [f"'{query}' is ambiguous — it matches: {names}. Re-run with the full name."]
    names = "; ".join(s.name for s in statuses)
    return None, [f"No jar matches '{query}'. A jar must exist before its first run can be "
                  f"logged — creating one is the new-jar skill.",
                  f"Jars on disk: {names}."]


# ── commands ─────────────────────────────────────────────────────────────────

def _first_run_caution(note):
    """Best-effort party-mode guard: if the capture note names a jar with no
    logged runs, return a go-easy clause for start's one-liner — the warning
    is only useful before the dab, and party mode never runs `brief`. Capture
    must never fail on jar data, so any problem here returns silence."""
    if not note:
        return ''
    try:
        runs, statuses, closed = _load_jar_data()
        low = note.lower()
        logged = {r.strain for r in runs}
        for s in statuses:
            if s.slug not in closed and s.name not in logged and s.name.lower() in low:
                return " First run of this jar — potency unknown, go easy."
        return ''
    except Exception:
        return ''


def cmd_start(args):
    now = datetime.now(timezone.utc).replace(microsecond=0)
    entries = _load()
    entries.append({'utc': now.isoformat(), 'note': args.note or ''})
    _save(entries)
    waiting = (f" ({len(entries)} dabs waiting to be logged, including this one.)"
               if len(entries) > 1 else "")
    print(f"Got it — {_say_time(now)}.{waiting}{_first_run_caution(args.note or '')}")


def cmd_brief(args):
    entries = _load()
    notes = []

    if entries:
        utc = datetime.fromisoformat(entries[-1]['utc'])
        time_line = f"Dab time: {_say_time(utc)}"
    else:
        utc = datetime.now(timezone.utc).replace(microsecond=0)
        time_line = f"Right now: {_say_time(utc)}"
        notes.append("No dab is captured — if one was just announced, run start first.")

    try:
        runs, statuses, closed = _load_jar_data()
    except Exception as e:  # a jar mid-edit must not eat the time facts
        print(SAY)
        print(time_line)
        print(ASSISTANT)
        print(f"Jar data failed to load ({e.__class__.__name__}: {e}) — the time above is "
              f"safe; fix the jar problem before any readback.")
        return

    prior = _sessions_prior(utc, runs, entries[:-1] if entries else entries)
    say = [f"{time_line} — {_ordinal(prior + 1)} dab of the day"]

    if args.strain:
        status, err = _resolve_strain(args.strain, statuses)
        if err:
            notes.extend(err)
        else:
            done = sum(1 for r in runs if r.strain == status.name)
            say.append(f"Strain: {status.name} — {done} runs logged; next is Run {done + 1}")
            if done == 0:  # jar opener — the papzp22 R1 / dbrb R1 caution, mechanized
                say.append("First run of this jar — potency unknown. Keep the load "
                           "modest until the first session reads it.")
            if status.slug in closed:
                notes.append(f"This jar is CLOSED ({status.name}) — its guidance is "
                             f"if-it-shows-up-again framing, not an active plan.")
            if status.next_text:
                plan = status.next_text.strip()
                prefix = f"run {done + 1}:"  # next_text conventionally opens "Run N:" — don't double it
                if plan.lower().startswith(prefix):
                    plan = plan[len(prefix):].strip()
                say.append(f"Plan on file for Run {done + 1}: {plan}")
            if status.next_waypoints:
                say.append(fmt_curve_table(status.next_waypoints))

    latest, run_n = _latest_run(runs)
    if latest is not None:
        say.append(f"Working rig: {_fmt_equipment_display(latest.equipment)}")
        if latest.run_date is not None:
            gap = (denver_local_date(utc) - latest.run_date).days
            ago = "today" if gap == 0 else ("yesterday" if gap == 1 else f"{gap} days ago")
            say.append(f"Last run anywhere: {latest.strain} Run {run_n} — "
                       f"{_say_date(latest.run_date)} ({ago})")
            if gap > 3:
                notes.append("Gap exceeds 3 days: apply the session-open equipment "
                             "soft check in Dabby_Handoff_Notes.md.")

    print(SAY)
    for line in say:
        print(line)
    if notes:
        print(ASSISTANT)
        for line in notes:
            print(line)


def cmd_list(args):
    entries = _load()
    if not entries:
        print("No pending dabs.")
        return
    print(f"{len(entries)} pending dab(s), oldest first:")
    for i, e in enumerate(entries, 1):
        print(_fmt(e, i))


def cmd_consume(args):
    entries = _load()
    if not entries:
        print("No pending dabs. If no capture happened for this run, follow the "
              "standard date/time protocol in CLAUDE.md instead.")
        return
    e = entries[0]
    utc = datetime.fromisoformat(e['utc'])
    local = denver_local(utc)

    jar_problem = None
    try:
        runs, statuses, _closed = _load_jar_data()
    except Exception as exc:
        runs, jar_problem = [], f"{exc.__class__.__name__}: {exc}"

    print("Oldest pending dab — paste these into the CompletedRun:")
    print(f"        run_date=date({local.year}, {local.month}, {local.day}),")
    if jar_problem is None:
        print(f"        sessions_prior_today={_sessions_prior(utc, runs)},")
    print(f"        utc_logged_at=datetime({utc.year}, {utc.month}, {utc.day}, "
          f"{utc.hour}, {utc.minute}, {utc.second}, tzinfo=timezone.utc),")
    if e.get('note'):
        print(f'Captured note (verbatim dab_notes source): "{e["note"]}"')

    print(SAY)
    if jar_problem is None:
        print(f"{_say_time(utc)} — {_ordinal(_sessions_prior(utc, runs) + 1)} dab of the day")
        prev, prev_n = _latest_run(runs, before_utc=utc)
        if prev is not None:
            when = _say_date(prev.run_date) if prev.run_date is not None else "date unknown"
            print(f"Equipment default: {_fmt_equipment_display(prev.equipment)}")
            print(f"  (most recent run logged before this dab: {prev.strain} Run {prev_n}, {when})")
    else:
        print(f"{_say_time(utc)}")

    print(ASSISTANT)
    if jar_problem is not None:
        print(f"Jar data failed to load ({jar_problem}) — count sessions_prior_today by "
              f"hand (same run_date, earlier utc_logged_at, any jar) and take the "
              f"equipment default from HANDOFF_STATE.md's most-recent-run line.")
    if len(entries) > 1:
        print(f"({len(entries) - 1} more pending after this one — run list to see them.)")
    print("This entry clears automatically once the generator sees a run with this "
          "exact utc_logged_at; consume does not delete it.")


def cmd_discard(args):
    entries = _load()
    if not 1 <= args.index <= len(entries):
        print(f"No entry [{args.index}] — {len(entries)} pending. Run list first.")
        sys.exit(1)
    e = entries.pop(args.index - 1)
    _save(entries)
    print(f"Discarded: {_fmt(e, args.index).lstrip()}")
    print(f"Pending entries: {len(entries)}.")


def main():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    sp = sub.add_parser('start', help='capture now as a pending dab')
    sp.add_argument('--note', default='', help="user's verbatim words, if any")
    sb = sub.add_parser('brief', help='print session-open facts in display form')
    sb.add_argument('--strain', default='', help='strain name (or fragment) to resolve')
    sub.add_parser('list', help='show pending entries')
    sub.add_parser('consume', help='print paste-ready lines for the oldest entry')
    sd = sub.add_parser('discard', help='remove an entry that will never become a run')
    sd.add_argument('index', type=int, help='entry number from list (1-based)')
    args = p.parse_args()
    {'start': cmd_start, 'brief': cmd_brief, 'list': cmd_list,
     'consume': cmd_consume, 'discard': cmd_discard}[args.cmd](args)


if __name__ == '__main__':
    main()
