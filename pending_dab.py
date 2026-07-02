#!/usr/bin/env python3
"""Pending-dab queue — mechanical timestamp capture for run logging.

Captures the true time of a dab the moment it is announced, so logging never
depends on anyone remembering it later (documented failure mode: timestamps
recalculated at reporting time — Sessions 121 and 140). Party mode uses the
same queue: capture verbatim fragments now, reconcile with the full logging
protocol later.

Usage:
  python pending_dab.py start [--note "user's verbatim words"]
      Capture NOW as a pending dab. Run this the moment the user announces a
      dab ("about to hit it", "grabbing one", or a party-mode fragment). The
      note is optional and verbatim — never a paraphrase.
  python pending_dab.py list
      Show pending entries, oldest first.
  python pending_dab.py consume
      Print paste-ready run_date / utc_logged_at lines for the OLDEST pending
      entry. Does NOT delete it — the generator auto-prunes an entry once a
      run with a matching utc_logged_at exists, and refuses to generate while
      unmatched entries remain (the tripwire in Dabby_Log_Generator.py).
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

from Dabby_Core import denver_local

QUEUE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.pending_dabs.json')


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


def cmd_start(args):
    now = datetime.now(timezone.utc).replace(microsecond=0)
    entries = _load()
    entries.append({'utc': now.isoformat(), 'note': args.note or ''})
    _save(entries)
    local = denver_local(now)
    print(f"Captured: {local:%B %d, %Y %I:%M %p} Denver ({now:%H:%M} UTC). "
          f"Pending entries: {len(entries)}.")


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
    print("Oldest pending dab — paste these into the CompletedRun:")
    print(f"        run_date=date({local.year}, {local.month}, {local.day}),")
    print(f"        utc_logged_at=datetime({utc.year}, {utc.month}, {utc.day}, "
          f"{utc.hour}, {utc.minute}, {utc.second}, tzinfo=timezone.utc),")
    if e.get('note'):
        print(f'Captured note (verbatim dab_notes source): "{e["note"]}"')
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
    sub.add_parser('list', help='show pending entries')
    sub.add_parser('consume', help='print paste-ready lines for the oldest entry')
    sd = sub.add_parser('discard', help='remove an entry that will never become a run')
    sd.add_argument('index', type=int, help='entry number from list (1-based)')
    args = p.parse_args()
    {'start': cmd_start, 'list': cmd_list,
     'consume': cmd_consume, 'discard': cmd_discard}[args.cmd](args)


if __name__ == '__main__':
    main()
