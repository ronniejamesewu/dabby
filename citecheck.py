#!/usr/bin/env python3
"""citecheck.py — deterministic citation checker for the Dabby docs.

Built for the July 2026 project audit (AUDIT.md); kept because the wisdom
consolidation pass ("pass 3", Dabby_Handoff_Notes.md backlog) needs guardrail 2:
"every citation dropped from wisdom must be verifiable in a frozen analysis."

Three checks, no LLM, no network:

  1. RUN CITATIONS — every "FW106 R26" / "WM R16–18" / "Hive #1 Run 6"-style
     reference in the prose docs resolves to a real run: the short form maps to
     a jar (alias table derived from jar_manifest.py's slug + inline-comment
     names) and the cited run number is <= that jar's len(RUNS).
  2. FILENAMES — every filename the docs mention exists on disk.
  3. IDENTIFIERS — every code identifier the docs name (RIG_N, BASELINE_*,
     function names in backticks) greps to a definition in the .py files.

Hits are TRIAGE INPUT, not auto-fail: historical failure-mode rows deliberately
reference retired artifacts (e.g. Dabby_Data.py), and closed-jar prose cites
runs by design. A human (or auditing Claude) dispositions every hit.

Usage: python3 citecheck.py            (exit 0 always; output is the report)
"""
import os
import re
import sys
import importlib

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

# Docs scanned for run citations (the charter's list):
CITATION_DOCS = ['HANDOFF_WISDOM.md', 'Dabby_Handoff_Notes.md', 'Dabby_Methodology.md']
# Docs scanned for filename / identifier mentions (wider prose+skills net):
MENTION_DOCS = CITATION_DOCS + [
    'CLAUDE.md', 'Dabby_UI_Principles.md', 'DESIGN_BRIEF.md',
    'jar_return_check.md', 'switch2_thermal_model.md',
    'register_leak_diagnostic_exercise.md',
    '.claude/skills/dab/SKILL.md', '.claude/skills/log-run/SKILL.md',
    '.claude/skills/new-jar/SKILL.md',
    '.claude/skills/new-jar/references/lineage_research_bar.md',
]


# ── jar data ─────────────────────────────────────────────────────────────────

def load_manifest():
    """[(slug, full_name)] parsed from jar_manifest.py's tier lists + inline
    name comments — the convention CLAUDE.md mandates for every manifest entry."""
    pairs = []
    pat = re.compile(r"^\s*'([a-z0-9]+)',\s*#\s*(.+?)\s*$")
    with open(os.path.join(ROOT, 'jar_manifest.py'), encoding='utf-8') as fh:
        for line in fh:
            m = pat.match(line)
            if m:
                pairs.append((m.group(1), m.group(2)))
    return pairs


def run_counts(pairs):
    """slug -> len(RUNS), by importing each jar the same way jar_manifest does."""
    counts = {}
    for slug, _name in pairs:
        mod = importlib.import_module(f'jars.{slug}')
        counts[slug] = len(mod.RUNS)
    return counts


def aliases_for(slug, name):
    """Candidate short forms the docs use for a jar. Derived mechanically from
    the slug and the full name so a new jar needs no edit here:
      - the slug itself, upper and as-written        (fw106, FW106, papzp22)
      - the full name                                 (Fire Water #106)
      - name with '#'-spacing collapsed / dropped     (BB36#1; Fembot3; Hive1)
      - initials of the alpha words + trailing number (Fire Water #106 -> FW106,
        Rain Fruit -> RF, Mango Banana #9 + Z + Sour Tangie -> MB9ZST)
      - leading-'The'-stripped variants               (The Hive #1 -> Hive #1)
      - first two letters of a single-word name       (Watermellos -> WM)
    """
    out = {slug, slug.upper(), name}
    stripped = name[4:] if name.startswith('The ') else name
    out.add(stripped)
    # collapse '#N' spacing:  'Blueberry 36 #1' -> 'Blueberry 36#1'; also 'Fembot #3' -> 'Fembot3'
    out.add(re.sub(r'\s*#\s*', '#', stripped))
    out.add(re.sub(r'\s*#\s*', '', stripped))
    # initials: alpha words contribute first letters; digit groups append
    words = re.findall(r'[A-Za-z]+|\d+', stripped.replace('#', ' '))
    initials = ''.join(w[0].upper() if w.isalpha() else w for w in words)
    if len(words) > 1:
        out.add(initials)
    # single-word names abbreviate to their first two letters (Watermellos -> WM)
    if len(words) == 1 and words[0].isalpha():
        out.add(words[0][:2].upper())
    # 'BB36 #2' style: initials of alpha words + space-# number
    m = re.match(r'^(.*?)\s*#\s*(\d+)$', stripped)
    if m:
        alpha = re.findall(r'[A-Za-z]+|\d+', m.group(1))
        ini = ''.join(w[0].upper() if w.isalpha() else w for w in alpha)
        out.add(f'{ini}#{m.group(2)}')
        out.add(f'{ini} #{m.group(2)}')
        out.add(f'{ini}{m.group(2)}')
    return {a for a in out if len(a) >= 2}


# Irregular short forms the docs use that no mechanical rule derives from the
# name: "WM" abbreviates the two halves of "Watermellos"; "BB36 #N" abbreviates
# "Blueberry 36 #N" the same way. Hand-seeded, kept tiny; everything else is
# derived in aliases_for(). New-jar shorthand the user coins gets added here.
IRREGULAR_ALIASES = {
    'WM': 'watermellos',
    'BB36 #1': 'bb361', 'BB36#1': 'bb361',
    'BB36 #2': 'bb362', 'BB36#2': 'bb362',
    'BB36 #4': 'bb364', 'BB36#4': 'bb364',
}


# ── check 1: run citations ───────────────────────────────────────────────────

def check_citations(pairs, counts):
    alias_map = dict(IRREGULAR_ALIASES)   # alias (as written) -> slug
    for slug, name in pairs:
        for a in aliases_for(slug, name):
            alias_map.setdefault(a, slug)
    # longest-first so 'BB36 #2 R4' doesn't half-match a shorter alias
    alias_alt = '|'.join(re.escape(a) for a in
                         sorted(alias_map, key=len, reverse=True))
    # ALIAS + R26 / Run 26 / Runs 1-4 / R16–18 / R2-5
    cite_re = re.compile(
        rf'\b({alias_alt})\s+(?:Runs?\s+|R)(\d+)(?:\s*[–—-]\s*R?(\d+))?')
    hits, total = [], 0
    for doc in CITATION_DOCS:
        path = os.path.join(ROOT, doc)
        with open(path, encoding='utf-8') as fh:
            for lineno, line in enumerate(fh, 1):
                for m in cite_re.finditer(line):
                    alias, lo, hi = m.group(1), int(m.group(2)), m.group(3)
                    hi = int(hi) if hi else lo
                    total += 1
                    slug = alias_map[alias]
                    n = counts[slug]
                    if hi > n or lo < 1 or hi < lo:
                        hits.append(f'{doc}:{lineno}: "{m.group(0)}" -> jar '
                                    f"'{slug}' has {n} runs")
    return total, hits


# ── check 2: filenames ───────────────────────────────────────────────────────

FILE_RE = re.compile(r'\.?\b(?!e\.g|i\.e)[\w][\w./-]*\.(?:py|md|yml|css|html|json)\b')
# Names that appear in docs but are patterns/templates, not literal files:
TEMPLATE_NAMES = {'jars/<slug>.py', '<slug>.py', 'style.css.map'}
# Session-local / gitignored files that legitimately may not exist on disk:
ALLOWED_ABSENT = {'.pending_dabs.json', 'settings.local.json'}


def check_filenames():
    hits, total = [], 0
    for doc in MENTION_DOCS:
        with open(os.path.join(ROOT, doc), encoding='utf-8') as fh:
            for lineno, line in enumerate(fh, 1):
                for m in FILE_RE.finditer(line):
                    fname = m.group(0)
                    if ('<' in line[max(0, m.start() - 1):m.end() + 1]
                            or fname in TEMPLATE_NAMES
                            or os.path.basename(fname) in ALLOWED_ABSENT):
                        continue
                    total += 1
                    # resolve relative to repo root, the doc's own dir, and its parent
                    doc_dir = os.path.dirname(os.path.join(ROOT, doc))
                    cand = [os.path.join(ROOT, fname),
                            os.path.join(doc_dir, fname),
                            os.path.join(os.path.dirname(doc_dir), fname)]
                    # bare basenames may live in known dirs
                    if '/' not in fname:
                        cand += [os.path.join(ROOT, d, fname)
                                 for d in ('jars', '.github/workflows')]
                    if not any(os.path.isfile(c) for c in cand):
                        hits.append(f'{doc}:{lineno}: {fname}')
    return total, hits


# ── check 3: identifiers ─────────────────────────────────────────────────────

IDENT_RES = [
    re.compile(r'\bRIG_\d+\b'),
    re.compile(r'\bBASELINE_[A-Z0-9_]+\b'),
    re.compile(r'`([A-Za-z_][A-Za-z0-9_]*)\(\)`'),     # `validate()` style
    re.compile(r'`(_[A-Za-z0-9_]+|[A-Z][A-Z0-9_]{2,})`'),  # `_RIG_LABELS`, `GLOBAL_INFO`
]


# Doc-convention placeholders — pattern names, not literal identifiers:
PLACEHOLDERS = {'RIG_N', 'BASELINE_XXX', 'BASELINE_*'}


def python_definitions():
    """Names defined in project .py files: def/class at any indent, plus
    module-level assignments including tuple targets (A, B = ...)."""
    defs = set()
    py_files = [f for f in os.listdir(ROOT) if f.endswith('.py')]
    py_files += [os.path.join('jars', f) for f in os.listdir(os.path.join(ROOT, 'jars'))
                 if f.endswith('.py')]
    def_re = re.compile(r'^\s*(?:def|class)\s+(\w+)', re.MULTILINE)
    assign_re = re.compile(r'^(\w+(?:\s*,\s*\w+)*)\s*=[^=]', re.MULTILINE)
    for f in py_files:
        with open(os.path.join(ROOT, f), encoding='utf-8') as fh:
            src = fh.read()
        for m in def_re.finditer(src):
            defs.add(m.group(1))
        for m in assign_re.finditer(src):
            for name in m.group(1).split(','):
                defs.add(name.strip())
    return defs


def check_identifiers():
    defs = python_definitions()
    hits, total = [], 0
    seen = set()
    for doc in MENTION_DOCS:
        with open(os.path.join(ROOT, doc), encoding='utf-8') as fh:
            for lineno, line in enumerate(fh, 1):
                for rex in IDENT_RES:
                    for m in rex.finditer(line):
                        name = m.group(1) if m.groups() and m.group(1) else m.group(0)
                        if name in PLACEHOLDERS:
                            continue
                        total += 1
                        if name not in defs and (doc, name) not in seen:
                            seen.add((doc, name))
                            hits.append(f'{doc}:{lineno}: `{name}` has no definition '
                                        f'in the .py files')
    return total, hits


# ── report ───────────────────────────────────────────────────────────────────

def main():
    pairs = load_manifest()
    counts = run_counts(pairs)
    print(f'Jars in manifest: {len(pairs)}; total runs: {sum(counts.values())}')
    print()

    for title, (total, hits) in [
        ('RUN CITATIONS', check_citations(pairs, counts)),
        ('FILENAMES', check_filenames()),
        ('IDENTIFIERS', check_identifiers()),
    ]:
        print(f'== {title}: {total} checked, {len(hits)} to triage ==')
        for h in hits:
            print(f'  {h}')
        print()

    print('Reminder: hits are triage input, not failures — historical rows cite '
          'retired artifacts on purpose. Disposition each hit; do not bulk-fix.')


if __name__ == '__main__':
    main()
