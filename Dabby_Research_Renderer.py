"""
Dabby Research Renderer — renders the research/ lineage catalog to research.html.

Standalone: imports only Dabby_Core (for Denver time) — never the log generator or a jar file. Reads
research/strains/*.md, research/lineage_nodes.md, research/brands.md and
research/SOURCES.md; writes research.html next to index.html.

Doubles as the catalog validator — an entry missing a required field fails
the build (exit 1) instead of rendering a half-card. Required per entry:
  H1 title, Grower, Processor, Type, a Sources section, and a formula line —
  Cross (single cultivar), Composition (blend), or Selection (pheno pick of a
  named cultivar) — unless the Type is a wash / mix / hunt product, which has
  no formula by construction, or the Type is itself unresolved.

Usage:  python Dabby_Research_Renderer.py
Needs:  pip install markdown
"""

import html as _html
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from Dabby_Core import denver_local  # shared stable layer; loads no jars

try:
    import markdown
except ImportError:
    print("Dabby_Research_Renderer.py needs the 'markdown' package: pip install markdown")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
RESEARCH = ROOT / "research"
STRAINS = RESEARCH / "strains"
OUT = ROOT / "research.html"
CLASSICS_PATH = ROOT / ".claude" / "skills" / "research-strain" / "references" / "classics_stoplist.md"

MD_EXTENSIONS = ["tables", "sane_lists"]

# Field bullets the card extracts. Grower/Processor share a line joined by " · ".
FIELD_RE = re.compile(r"\*\*(Grower|Processor|Type|Cross|Composition|Selection|Breeder|Spelling):\*\*\s*(.*?)(?=\s+·\s+\*\*|$)")

# Type-line keywords → badge. Order matters: "blend" beats "cross" for a
# co-press whose Type line mentions both.
TYPE_BADGES = (
    ("blend", "blend"),
    ("wash", "wash"),
    ("mix", "wash"),
    ("hunt", "wash"),
    ("single cultivar", "cross"),
)
NO_FORMULA_BADGES = {"wash"}

# A pheno number stated on the Type line but not carried into the formula
# bullet itself — e.g. "single cultivar, pheno **#9**" — Perle di Sole and
# Zcrewdriver share an identical formula and are distinguished only by this.
PHENO_TYPE_RE = re.compile(r"pheno\s+#(\d+)")

# Node-name bullets in lineage_nodes.md: "- **Name** = ..." or "- **Name** — ...".
NODE_BULLET_RE = re.compile(r"^- \*\*(.+?)\*\*", re.M)

# A parent list split on the verbatim cross (×) / co-press (+) symbols.
PARENT_SPLIT_RE = re.compile(r"(\s[×+]\s)")


# ── Parsing ───────────────────────────────────────────────────────────────────

def strip_md(s):
    """Inline markdown → plain text for card lines."""
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s.strip()


def parse_entry(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors = []

    title = None
    for ln in lines:
        if ln.startswith("# "):
            title = ln[2:].strip()
            break
    if not title:
        errors.append("missing H1 title")

    fields = {}
    for ln in lines:
        if ln.startswith("- **"):
            for key, val in FIELD_RE.findall(ln):
                fields.setdefault(key, val.strip())

    headings = [ln[3:].strip() for ln in lines if ln.startswith("## ")]

    for req in ("Grower", "Processor", "Type"):
        if req not in fields:
            errors.append(f"missing **{req}:** bullet")
    if not any(h.lower().startswith("sources") for h in headings):
        errors.append("missing '## Sources' section")

    # Classify on the designation only (text before the first " — " or ";"),
    # so a discussion clause mentioning "blend" cannot decide the badge.
    badge = "unresolved"
    type_lc = re.split(r"\s+—\s+|;", fields.get("Type", ""), maxsplit=1)[0].lower()
    for kw, b in TYPE_BADGES:
        if kw in type_lc:
            badge = b
            break

    formula_key = next((k for k in ("Composition", "Cross", "Selection") if k in fields), None)
    if formula_key is None and badge not in NO_FORMULA_BADGES and "Type" in fields:
        if badge != "unresolved":
            errors.append("missing **Cross:** or **Composition:** bullet for a non-wash type")

    has_open = any(h.lower().startswith("open question") for h in headings)
    terminated = any("terminated" in h.lower() for h in headings)
    if has_open:
        status = "open"
    elif terminated:
        status = "terminated"
    else:
        status = "none noted"

    return {
        "slug": path.stem,
        "title": title or path.stem,
        "fields": fields,
        "badge": badge,
        "formula_key": formula_key,
        "status": status,
        "markdown": text,
        "errors": errors,
    }


def short_axis(val):
    """'Erva (stated — Erva-branded drop menu)' → 'Erva'. Keeps 'undisclosed'."""
    v = strip_md(val)
    v = re.split(r"\s+[\(—–-]\s*|\s\(", v, maxsplit=1)[0]
    v = v.replace("likely ", "")
    return v.strip() or "—"


def formula_only(val):
    """Drop the evidence clause: 'A × B — stated (…)' → 'A × B'."""
    v = strip_md(val)
    return re.split(r"\s+—\s+", v, maxsplit=1)[0].strip()


def evidence_word(val):
    """First evidence word in the clause after the formula, if any."""
    v = strip_md(val).lower()
    m = re.search(r"\b(measured|user-direct|stated|corroborated|lead|assumed|undisclosed|conflicted|dead-end)\b", v)
    return m.group(1) if m else ""


def kebab(name):
    """'TMZ (Too Much Zkittlez)' -> 'tmz'; 'Guava'z' -> 'guava-z'. Drops any
    parenthetical before kebabbing so pheno-count asides ('(phenos #74/#62)')
    and mid-name parentheticals normalize the same way."""
    name = re.sub(r"\([^)]*\)", "", name)
    name = re.sub(r"[^a-z0-9]+", "-", name.lower())
    return name.strip("-")


def parse_node_ids(nodes_md):
    """Every '- **Node Name** ...' bullet in lineage_nodes.md -> its kebab id."""
    return {kebab(m) for m in NODE_BULLET_RE.findall(nodes_md)}


def link_formula(formula, node_ids):
    """Escape a formula line, linking any × / + separated parent whose kebab
    matches a lineage-node id to '#node-<id>'."""
    parts = PARENT_SPLIT_RE.split(formula)
    out = []
    for part in parts:
        if PARENT_SPLIT_RE.fullmatch(part):
            out.append(esc(part))
            continue
        nid = kebab(part)
        if nid in node_ids:
            out.append(f'<a href="#node-{nid}">{esc(part)}</a>')
        else:
            out.append(esc(part))
    return "".join(out)


LI_STRONG_RE = re.compile(r"<li><strong>(.*?)</strong>")


def add_node_ids(nodes_html):
    """Give each lineage-node <li> (one whose first child is <strong>) an
    id="node-<kebab>" so strain-card formulas can link straight to it."""
    def repl(m):
        nid = kebab(m.group(1))
        return f'<li id="node-{nid}"><strong>{m.group(1)}</strong>'
    return LI_STRONG_RE.sub(repl, nodes_html)


# ── Lineage tree (SVG) ──────────────────────────────────────────────────────────
#
# lineage_tree(slug) walks the catalog's own formula bullets -- a strain
# entry's Cross/Composition/Selection line, a lineage_nodes.md node's head
# formula, and any plain "Name = A x B" sub-formula embedded in a node's
# prose -- into a nested dict, per the fixed status vocabulary documented on
# the function itself. render_tree_svg() draws it as static inline SVG.
# Both are pure: they read research/*.md fresh on each call but write and
# print nothing, so importing this module has no side effects.

LINEAGE_DEPTH_CAP = 5  # generations below the root before a subtree is capped

# Spelling variants actually seen in the catalog -- not a general normalizer.
# Keys are normalize_basic() output; values are looked up again from there.
NAME_ALIASES = {
    "zkittles": "Zkittlez",
    "the original z": "Zkittlez",
    "g.m.o": "GMO",
    "gmo cookies": "GMO",
    "dosidos": "Do-Si-Dos",
    "gdp": "Granddaddy Purple",
    "strawnana": "Strawberry Banana",
    "strawguava": "Strawberry Guava",
    "gsc (forum)": "GSC",
    "sunset sherbet": "Sunset Sherbert",
    "gpwc": "Grape Pie Wedding Crasher",
    "rainbow pie": "Grape Rainbow Pie",
    "honey bananas": "Honey Banana",
    "peach rings": "Peach Ringz",
    "the white og": "White OG",
}

DEAD_KEYWORDS_RE = re.compile(r"dead-end|clone-only|clone only|\bmystery\b", re.I)
LINEAGE_EVIDENCE_RE = re.compile(
    r"\b(measured|user-direct|stated|corroborated|lead|assumed|undisclosed|conflicted|dead-end)\b", re.I)
EMBED_NAME_RE = re.compile(r"([A-Z][A-Za-z0-9'/#-]*(?:\s+[A-Z0-9#][A-Za-z0-9'/#-]*){0,5})\s=\s")


def normalize_basic(s):
    """Shared lookup-key shape: drop '#', lowercase, collapse whitespace."""
    return re.sub(r"\s+", " ", s.replace("#", "")).strip().lower()


def strip_pheno_key(key):
    """Fallback key with a trailing pheno/selection marker stripped
    ('moonbow 112 f2 60' -> 'moonbow'). Only tried after the exact key
    misses, so a real per-pheno definition (an embedded 'Moonbow #112 = ...')
    is never shadowed by a same-named sibling pheno that has none."""
    prev, k = None, key
    while k != prev:
        prev = k
        k = re.sub(r"\s+f\d+$", "", k)
        k = re.sub(r"\s+\d+[a-z]?$", "", k)
    return k.strip()


def lookup_candidates(token):
    """Ordered lookup keys for a parent token: alias-resolved exact name
    first, then with any parenthetical dropped (aliased again, so 'The
    Original Z (Zkittlez)' still finds the 'the original z' alias once its
    trailing annotation is gone), then each with a trailing pheno marker
    stripped. Exact always precedes stripped, so a name that IS a full
    match never gets mangled by the fallback."""
    disp = token.strip()
    key0 = normalize_basic(disp)
    key_noparen0 = normalize_basic(re.sub(r"\s*\([^)]*\)", " ", disp))
    cands = []
    for base_key in (key0, key_noparen0):
        target = NAME_ALIASES.get(base_key, base_key)
        for k in (normalize_basic(target), strip_pheno_key(normalize_basic(target))):
            if k and k not in cands:
                cands.append(k)
    return cands


def is_fully_parenthesized(token):
    t = token.strip()
    if not (t.startswith("(") and t.endswith(")")):
        return False
    depth = 0
    for i, c in enumerate(t):
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0 and i != len(t) - 1:
                return False
    return depth == 0


def split_formula(formula):
    """Split a formula on top-level x/X-cross or unicode x/+ (blend),
    honoring parens so '(Grape Pie x Wedding Crasher)' stays one token."""
    f = re.sub(r"(?<=\s)[xX](?=\s)", "×", formula)
    tokens, depth, cur, i, n = [], 0, "", 0, len(f)
    while i < n:
        c = f[i]
        if c == "(":
            depth += 1
            cur += c
        elif c == ")":
            depth -= 1
            cur += c
        elif depth == 0 and c in "×+":
            tokens.append(cur.strip())
            cur = ""
        else:
            cur += c
        i += 1
    tokens.append(cur.strip())
    return [t for t in tokens if t]


def _matching_paren(text, open_idx):
    depth = 0
    for i in range(open_idx, len(text)):
        if text[i] == "(":
            depth += 1
        elif text[i] == ")":
            depth -= 1
            if depth == 0:
                return i
    return None


def extract_formula(text):
    """From text starting right after a head '=', return (formula,
    remaining_text). Scans at paren-depth 0 for the end of the formula: an
    em dash ' -- ', or a '(...)' whose interior holds no cross/blend symbol
    (an evidence clause, not a nested formula group -- a group that DOES
    hold one, e.g. '(Sunset Sherbert x Dosidos)', is skipped over and
    folded into the formula)."""
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c == ")":
            # unmatched close -- we've walked out of an enclosing paren that
            # opened before this substring started (e.g. an embedded match
            # found inside someone else's parenthetical aside); stop here.
            return text[:i].strip(), text[i:].strip()
        if c == "(":
            j = _matching_paren(text, i)
            if j is None:
                break
            inner = text[i + 1:j]
            if re.search(r"\s×\s|\s\+\s", inner) or re.search(r"(?<=\s)[xX](?=\s)", inner):
                i = j + 1
                continue
            if len(inner) <= 12 and not re.search(r"classics?", inner, re.I) \
                    and not LINEAGE_EVIDENCE_RE.search(inner):
                # a short inline annotation like "(clone)" or "(Archive)" --
                # not an evidence clause, the formula continues past it
                i = j + 1
                continue
            return text[:i].strip(), text[i:].strip()
        if text[i:i + 3] == " — ":
            return text[:i].strip(), text[i + 3:].strip()
        i += 1
    return text.strip(), ""


_NAME_CONNECTORS = {"di", "de", "la", "du", "von", "van"}


def _looks_like_name(s):
    """A single-token 'formula' (a clean rename, not a real cross) -- every
    word capitalized/numeric, short lowercase connectors aside. Rejects a
    prose fragment like 'Sugar Coat backcrossed with JOMO', which has no
    x/+ operator and must fall through to a leaf, not a fake one-parent
    cross, per the "never guess" rule."""
    s = s.strip()
    if not s or len(s) > 40 or "," in s or not re.match(r"^[A-Z]", s):
        return False
    words = re.findall(r"[A-Za-z0-9#'.-]+", s)
    if not words or len(words) > 6:
        return False
    for w in words:
        if w.lower() in _NAME_CONNECTORS:
            continue
        if not re.match(r"^[A-Z0-9#]", w):
            return False
    return True


def _valid_formula(formula):
    # Space-padded × / + only -- an evidence count like "corroborated ×5"
    # (no spaces) must never be mistaken for a cross operator.
    return bool(re.search(r"\s×\s|\s\+\s", formula)) or _looks_like_name(formula)


def lineage_evidence_caption(text):
    """First evidence word plus a short claimant from the clause after a
    formula's em dash -- catalog text only, e.g. 'stated · Erva'."""
    if not text:
        return ""
    m = LINEAGE_EVIDENCE_RE.search(text)
    if not m:
        return ""
    word = m.group(1).lower()
    rest = text[m.end():].strip()
    claim = re.match(r"by\s+([A-Z][A-Za-z0-9&' .-]*?)(?=[\s.,;(]|$)", rest)
    if not claim:
        claim = re.match(r"\(([A-Z][A-Za-z0-9&' -]*?)(?=[,)]|$)", rest)
    if claim and claim.group(1).strip():
        return f"{word} · {claim.group(1).strip()}"
    return word


def _field_evidence_caption(raw_value):
    v = strip_md(raw_value)
    parts = re.split(r"\s+—\s+", v, maxsplit=1)
    return lineage_evidence_caption(parts[1]) if len(parts) > 1 else ""


def _build_classics_set():
    """The stop-list's ' · '-separated phrases, each ' / '-alternative
    registered separately; a bare number alternative ('41' in 'Gelato /
    Gelato 33 / 41 / 45') is read as that group's base word + number."""
    text = CLASSICS_PATH.read_text(encoding="utf-8") if CLASSICS_PATH.exists() else ""
    out = set()
    for para in re.split(r"\n\s*\n", text):
        flat = re.sub(r"\s+", " ", para).strip()
        if "·" in flat:
            for phrase in flat.split("·"):
                alts = [a.strip() for a in phrase.strip().split(" / ") if a.strip()]
                if not alts:
                    continue
                base_word = alts[0].split()[0] if alts[0].split() else ""
                for a in alts:
                    a = re.sub(r"\s*\([^)]*\)", "", a).strip()
                    if base_word and re.match(r"^\d+$", a):
                        a = f"{base_word} {a}"
                    if a:
                        out.add(normalize_basic(a))
        m = re.match(r"^Pre-2018-clause examples accepted[^:]*:\s*(.+)$", flat)
        if m:
            for a in m.group(1).split(","):
                a = re.sub(r"\s*\([^)]*\)", "", a).strip().rstrip(".")
                if a:
                    out.add(normalize_basic(a))
    return out


def _join_bullets(md_text):
    """'- **Name** = ...' bullets with wrapped continuation lines joined
    into one flat string each; a '## ' heading or a new '- ' bullet ends
    the one before it."""
    bullets, current = [], None
    for line in md_text.splitlines():
        if line.startswith("## "):
            if current is not None:
                bullets.append(current)
            current = None
        elif line.startswith("- "):
            if current is not None:
                bullets.append(current)
            current = line.strip()
        elif line.strip() and current is not None:
            current += " " + line.strip()
    if current is not None:
        bullets.append(current)
    return [re.sub(r"\s+", " ", b).strip() for b in bullets]


def _parse_node_bullet_head(bullet):
    m = re.match(r"^- \*\*(.+?)\*\*\s*(.*)$", bullet)
    if not m:
        return None, None
    return m.group(1), m.group(2)


def _node_name_variants(name_raw):
    """' / '-alternatives (Sherbadough / Sherbidos) each become a key; an
    internal parenthetical that reads as a full alternate name (TMZ (Too
    Much Zkittlez)) registers that too."""
    variants = []
    for part in [p.strip() for p in name_raw.split(" / ")]:
        stripped = re.sub(r"\s*\([^)]*\)", "", part).strip()
        if stripped:
            variants.append(stripped)
        for inner in re.findall(r"\(([^)]+)\)", part):
            if len(inner.split()) >= 2:
                variants.append(inner.strip())
    return variants or [name_raw]


def _parse_formula_window(rest):
    """Search only the bullet's first sentence (up to '. ' + an uppercase
    letter) for a head formula -- keeps a LATER, unrelated '=' elsewhere in
    the bullet (e.g. a different breeder's same-named cultivar, quoted for
    contrast) from being mistaken for this node's own parents."""
    m = re.search(r"\.\s+(?=[A-Z])", rest)
    window = rest[:m.start() + 1] if m else rest
    eq_m = re.search(r"(?:^|\s)=\s", window)
    if not eq_m:
        return None, "", window
    formula, evidence_src = extract_formula(window[eq_m.end():])
    if not _valid_formula(formula):
        return None, "", window
    return formula, evidence_src, window


_NODE_IDX_CACHE = None
_STRAIN_IDX_CACHE = None
_CLASSICS_CACHE = None


def _build_node_indexes():
    path = RESEARCH / "lineage_nodes.md"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    heads, embedded = {}, {}
    for bullet in _join_bullets(text):
        name_raw, rest = _parse_node_bullet_head(bullet)
        if name_raw is None:
            continue
        formula, evidence_src, window = _parse_formula_window(rest)
        record = {"formula": formula, "evidence": lineage_evidence_caption(evidence_src), "raw": bullet}
        for variant in _node_name_variants(name_raw):
            heads.setdefault(normalize_basic(variant), record)
        for em in EMBED_NAME_RE.finditer(rest):
            prefix = rest[:em.start()]
            if not (em.start() == 0 or prefix.endswith(". ") or prefix.endswith("; ")
                    or prefix.endswith("→ ")):
                continue  # not a clause boundary -- e.g. "...catalog states
                          # Rainbow Juice = ..." is a quoted citation, not a
                          # new node definition
            eformula, esrc = extract_formula(rest[em.end():])
            if not _valid_formula(eformula):
                eformula, esrc = None, ""  # still a definition (e.g. a
                # dead-end/clone-only note) -- keep it as a leaf rather than
                # letting the name fall through to "unresolved"
            if eformula is not None and len(split_formula(eformula)) < 2:
                eformula = None  # half-parsed (mid-formula aside) -- never draw a one-parent cross
            # No evidence caption: the words near an embedded formula belong to
            # the host bullet's prose, not reliably to this name.
            record = {"formula": eformula, "evidence": "", "raw": bullet, "embedded": True}
            raw_name = em.group(1)
            ekeys = [normalize_basic(raw_name)]
            if "/" in raw_name:  # "Jet Fuel/G6" -- both names refer to it
                ekeys += [normalize_basic(p) for p in raw_name.split("/") if p.strip()]
            for ekey in ekeys:
                if ekey not in heads:  # a head formula always outranks an embedded one
                    embedded.setdefault(ekey, record)
    return heads, embedded


def _get_node_indexes():
    global _NODE_IDX_CACHE
    if _NODE_IDX_CACHE is None:
        _NODE_IDX_CACHE = _build_node_indexes()
    return _NODE_IDX_CACHE


def _build_strain_index():
    idx = {}
    for p in sorted(STRAINS.glob("*.md")):
        e = parse_entry(p)
        idx.setdefault(normalize_basic(e["title"]), e)
    return idx


def _get_strain_index():
    global _STRAIN_IDX_CACHE
    if _STRAIN_IDX_CACHE is None:
        _STRAIN_IDX_CACHE = _build_strain_index()
    return _STRAIN_IDX_CACHE


def _get_classics():
    global _CLASSICS_CACHE
    if _CLASSICS_CACHE is None:
        _CLASSICS_CACHE = _build_classics_set()
    return _CLASSICS_CACHE


def _resolve_child(token, depth, seen, drawn):
    """Resolve one parent token into a lineage_tree() node. `seen` holds
    identities of ancestors already expanded on this same root-to-here
    path, in this same tree -- a repeat becomes a leaf instead of
    re-drawing its subtree."""
    if is_fully_parenthesized(token):
        inner = token.strip()[1:-1].strip()
        if depth > LINEAGE_DEPTH_CAP:
            return {"name": inner, "status": "depth-cap", "children": [], "evidence": "", "raw": inner}
        children = [_resolve_child(t, depth + 1, seen, drawn) for t in split_formula(inner)]
        return {"name": inner, "status": "cross", "children": children, "evidence": "", "raw": inner}

    disp = re.sub(r"\s+", " ", token).strip()
    cands = lookup_candidates(disp)
    classics = _get_classics()
    for k in cands:
        if k in classics:
            return {"name": disp, "status": "classic", "children": [], "evidence": "", "raw": disp}

    node_heads, embedded = _get_node_indexes()
    rec, identity = None, None
    for k in cands:
        if k in node_heads:
            rec, identity = node_heads[k], "node:" + k
            break
    if rec is None:
        for k in cands:
            if k in embedded:
                rec, identity = embedded[k], "embed:" + k
                break

    if rec is not None:
        if rec["formula"] is None:
            # Only the bullet's first sentence speaks about the node itself; later
            # sentences quote other breeders' same-name cultivars (Zangria).
            head_clause = re.split(r"\.\s", rec["raw"], maxsplit=1)[0]
            status = "dead-end" if (DEAD_KEYWORDS_RE.search(head_clause)
                                    and not rec.get("embedded")) else "open"
            return {"name": disp, "status": status, "children": [], "evidence": rec["evidence"], "raw": rec["raw"]}
        if identity in seen or identity in drawn:
            return {"name": disp, "status": "repeat", "children": [], "evidence": "", "raw": rec["raw"]}
        if depth > LINEAGE_DEPTH_CAP:
            return {"name": disp, "status": "depth-cap", "children": [], "evidence": rec["evidence"], "raw": rec["raw"]}
        drawn.add(identity)
        children = [_resolve_child(t, depth + 1, seen | {identity}, drawn) for t in split_formula(rec["formula"])]
        return {"name": disp, "status": "cross", "children": children, "evidence": rec["evidence"], "raw": rec["raw"]}

    strain_idx = _get_strain_index()
    se = next((strain_idx[k] for k in cands if k in strain_idx), None)
    if se is not None:
        identity = "strain:" + normalize_basic(se["title"])
        fkey = se["formula_key"]
        if fkey is None:
            raw = strip_md(se["fields"].get("Type", ""))
            return {"name": disp, "status": "open", "children": [], "evidence": "", "raw": raw}
        raw_value = se["fields"][fkey]
        raw = strip_md(raw_value)
        f_only = formula_only(raw_value)
        if f_only.strip().lower().startswith("undisclosed"):
            return {"name": disp, "status": "open", "children": [], "evidence": "undisclosed", "raw": raw}
        if identity in seen or identity in drawn:
            return {"name": disp, "status": "repeat", "children": [], "evidence": "", "raw": raw}
        if depth > LINEAGE_DEPTH_CAP:
            return {"name": disp, "status": "depth-cap", "children": [], "evidence": "", "raw": raw}
        ev = _field_evidence_caption(raw_value)
        drawn.add(identity)
        children = [_resolve_child(t, depth + 1, seen | {identity}, drawn) for t in split_formula(f_only)]
        return {"name": disp, "status": "cross", "children": children, "evidence": ev, "raw": raw}

    return {"name": disp, "status": "unresolved", "children": [], "evidence": "", "raw": disp}


def lineage_tree(slug):
    """Nested lineage-tree dict for research/strains/<slug>.md:
      {"name": str, "status": str, "children": [...], "evidence": str, "raw": str}
    Status vocabulary -- root only: cross, blend, wash, undisclosed; non-root
    interior: cross; leaves: classic, dead-end, open, unresolved, repeat,
    depth-cap. Pure and read-only: rebuilds its lookup indexes from disk on
    each call, writes and prints nothing.
    """
    e = parse_entry(STRAINS / f"{slug}.md")
    fields, fkey = e["fields"], e["formula_key"]

    if fkey is None:
        return {"name": e["title"], "status": "wash", "children": [], "evidence": "",
                "raw": strip_md(fields.get("Type", ""))}

    raw_value = fields[fkey]
    f_only = formula_only(raw_value)
    raw = strip_md(raw_value)
    if f_only.strip().lower().startswith("undisclosed"):
        return {"name": e["title"], "status": "undisclosed", "children": [], "evidence": "", "raw": raw}

    status = "blend" if e["badge"] == "blend" else "cross"
    seen = {"strain:" + normalize_basic(e["title"])}
    children = [_resolve_child(t, 1, seen, set()) for t in split_formula(f_only)]
    return {"name": e["title"], "status": status, "children": children,
            "evidence": _field_evidence_caption(raw_value), "raw": raw}


def _walk_unresolved(tree, out):
    if tree["status"] == "unresolved":
        out.append(tree["name"])
    for c in tree["children"]:
        _walk_unresolved(c, out)


# SVG layout constants and rendering.
_LNODE_H, _LROW_H, _LPAD_X, _LPAD_TOP = 36, 50, 14, 20
_LNODE_MAXW, _LNODE_MINW = 190, 84


def _svg_caption(node):
    status, ev = node["status"], node["evidence"]
    if status == "blend":
        return "blend (+)"
    if status == "repeat":
        return "shown above"
    if status == "depth-cap":
        return "depth limit"
    if status == "unresolved":
        return "? " + (ev or "no catalog node")
    if status in ("classic", "dead-end", "open"):
        return ev or status
    return ev


def _truncate(s, max_chars=24):
    s = s.strip()
    if len(s) <= max_chars:
        return s, s
    return s[:max_chars - 1].rstrip() + "…", s


def _lwidest(node, best=0):
    disp, _ = _truncate(node["name"])
    cap, _ = _truncate(_svg_caption(node), 30)
    w = max(len(disp) * 6.6 + 24, len(cap) * 5.4 + 24)
    best = max(best, min(w, _LNODE_MAXW), _LNODE_MINW)
    for c in node["children"]:
        best = _lwidest(c, best)
    return best


def _llayout(node, depth, rows, out, col_w):
    placed = [_llayout(c, depth + 1, rows, out, col_w) for c in node["children"]]
    if placed:
        y = sum(p["y"] for p in placed) / len(placed)
    else:
        y = _LPAD_TOP + rows[0] * _LROW_H
        rows[0] += 1
    me = {"node": node, "x": _LPAD_X + depth * col_w, "y": y, "kids": placed, "depth": depth}
    out.append(me)
    return me


def render_tree_svg(tree):
    """A lineage_tree() dict -> static inline SVG: left to right, one
    generation per column, leaves stacked, parents centred on their
    children, curved edges. No JS, no external assets."""
    node_w = int(_lwidest(tree))
    col_w = node_w + 20
    nodes, rows = [], [0]
    _llayout(tree, 0, rows, nodes, col_w)
    max_depth = max(n["depth"] for n in nodes)
    w = _LPAD_X * 2 + max_depth * col_w + node_w
    h = _LPAD_TOP + rows[0] * _LROW_H + 40
    edges, boxes = [], []
    for n in nodes:
        for k in n["kids"]:
            x1, y1, x2, y2 = n["x"] + node_w, n["y"], k["x"], k["y"]
            mx = (x1 + x2) / 2
            edges.append(f'<path class="le" d="M{x1},{y1:.1f} C{mx},{y1:.1f} {mx},{y2:.1f} {x2},{y2:.1f}"/>')
        node = n["node"]
        cls = "root" if n["depth"] == 0 else node["status"]
        disp, full_name = _truncate(node["name"])
        cap_text = _svg_caption(node)
        cap, full_cap = _truncate(cap_text, 30)
        title = ""
        if disp != full_name or cap != full_cap:
            title = f'<title>{_html.escape(full_name)}'
            if full_cap:
                title += f' — {_html.escape(full_cap)}'
            title += "</title>"
        cap_el = (f'<text class="lc" x="{n["x"] + 10}" y="{n["y"] + 12:.1f}">{_html.escape(cap)}</text>'
                  if cap else "")
        boxes.append(
            f'<g class="ln {cls}">'
            f'<rect x="{n["x"]}" y="{n["y"] - _LNODE_H / 2:.1f}" width="{node_w}" height="{_LNODE_H}" rx="8"/>'
            f'{title}'
            f'<text class="lt" x="{n["x"] + 10}" y="{n["y"] - 2:.1f}">{_html.escape(disp)}</text>'
            f'{cap_el}</g>')
    legend_y = h - 12
    legend_items = [("classic", "classic — stop here"), ("dead-end", "dead-end — breeder won't say"),
                     ("open", "open — nobody's published it"), ("unresolved", "? unresolved — catalog gap")]
    lx, legend_parts = _LPAD_X, []
    for cls, label in legend_items:
        legend_parts.append(f'<rect class="ll {cls}" x="{lx}" y="-9" width="13" height="10" rx="3"/>'
                             f'<text x="{lx + 18}" y="0">{_html.escape(label)}</text>')
        lx += 18 + len(label) * 5.6 + 22
    legend = f'<g class="legend" transform="translate({_LPAD_X},{legend_y})">' + "".join(legend_parts) + "</g>"
    style = """
    svg.lineage{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
      --l-bg:#fbfaf7;--l-ink:#1c1b19;--l-mute:#77736b;--l-line:#cfcac0;--l-card:#ffffff;
      --l-classic:#ece8df;--l-dead:#e3e1dc;--l-accent:#8a4a2b}
    @media (prefers-color-scheme:dark){svg.lineage{--l-bg:#171614;--l-ink:#ece9e2;--l-mute:#9a958b;--l-line:#3d3a35;
      --l-card:#211f1c;--l-classic:#2e2b26;--l-dead:#262422;--l-accent:#d08a63}}
    svg.lineage .lbg{fill:var(--l-bg)} svg.lineage .le{fill:none;stroke:var(--l-line);stroke-width:1.5}
    svg.lineage .ln rect{fill:var(--l-card);stroke:var(--l-line);stroke-width:1}
    svg.lineage .lt{font-size:12.5px;font-weight:600;fill:var(--l-ink)} svg.lineage .lc{font-size:10px;fill:var(--l-mute)}
    svg.lineage .root rect{fill:var(--l-ink);stroke:var(--l-ink)} svg.lineage .root .lt{fill:var(--l-bg)} svg.lineage .root .lc{fill:var(--l-line)}
    svg.lineage .classic rect,svg.lineage .ll.classic{fill:var(--l-classic);stroke:var(--l-classic)}
    svg.lineage .dead-end rect,svg.lineage .ll.dead-end{fill:var(--l-dead);stroke:var(--l-mute);stroke-dasharray:1 3;stroke-linecap:round}
    svg.lineage .dead-end .lt{fill:var(--l-mute)}
    svg.lineage .open rect,svg.lineage .unresolved rect,svg.lineage .ll.open,svg.lineage .ll.unresolved{fill:none;stroke:var(--l-accent);stroke-width:1.5;stroke-dasharray:5 4}
    svg.lineage .open .lt,svg.lineage .open .lc,svg.lineage .unresolved .lt,svg.lineage .unresolved .lc{fill:var(--l-accent)}
    svg.lineage .repeat rect{fill:var(--l-card);stroke:var(--l-line);stroke-width:1;opacity:.6}
    svg.lineage .repeat .lt,svg.lineage .repeat .lc{fill:var(--l-mute)}
    svg.lineage .depth-cap rect{fill:none;stroke:var(--l-mute);stroke-width:1;stroke-dasharray:2 3}
    svg.lineage .depth-cap .lt,svg.lineage .depth-cap .lc{fill:var(--l-mute)}
    svg.lineage .legend text{font-size:10px;fill:var(--l-mute)}
    """
    return (f'<svg class="lineage" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'style="max-width:100%;height:auto" role="img">'
            f'<title>{_html.escape(tree["name"])} lineage tree</title><style>{style}</style>'
            f'<rect class="lbg" width="{w}" height="{h}" rx="10"/>'
            + "".join(edges) + "".join(boxes) + legend + "</svg>")


# ── Markdown rendering ────────────────────────────────────────────────────────

LINK_RE = re.compile(r"\]\(((?:\.\./)?)([A-Za-z0-9_-]+)\.md\)")


def rewrite_links(md):
    """Cross-file markdown links → in-page anchors."""
    def repl(m):
        target = m.group(2)
        if target == "lineage_nodes":
            return "](#lineage-nodes)"
        if target == "brands":
            return "](#brands)"
        if target == "SOURCES":
            return "](#sources)"
        return f"](#{target})"
    return LINK_RE.sub(repl, md)


def md_to_html(md, drop_h1=True):
    md = rewrite_links(md)
    if drop_h1:
        md = re.sub(r"^# .*\n", "", md, count=1)
    return markdown.markdown(md, extensions=MD_EXTENSIONS)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


# ── Page assembly ─────────────────────────────────────────────────────────────

def card_html(e, node_ids, gaps):
    f = e["fields"]
    grower = short_axis(f.get("Grower", "—"))
    proc = short_axis(f.get("Processor", "—"))
    if e["formula_key"]:
        formula = formula_only(f[e["formula_key"]])
        ev = evidence_word(f[e["formula_key"]])
    else:
        formula = strip_md(f.get("Type", ""))
        ev = evidence_word(f.get("Type", ""))
    formula_html = link_formula(formula, node_ids)
    # A pheno number stated on the Type line but absent from the formula
    # itself distinguishes otherwise-identical formulas (e.g. Perle di Sole
    # vs Zcrewdriver, both "TMZ × Orange Mints"). Appended as plain text —
    # never folded into the linked formula above.
    if "#" not in formula:
        pheno_m = PHENO_TYPE_RE.search(strip_md(f.get("Type", "")))
        if pheno_m:
            formula_html += f" #{pheno_m.group(1)}"
    search = " ".join([e["title"], formula, grower, proc, e["badge"], f.get("Breeder", ""), f.get("Spelling", "")]).lower()
    status_cls = {"open": "rs-open", "terminated": "rs-done", "none noted": "rs-none"}[e["status"]]
    status_txt = {"open": "open questions", "terminated": "chain terminated", "none noted": "no open questions"}[e["status"]]
    ev_html = f'<span class="rc-ev">{esc(ev)}</span>' if ev else ""
    tree = lineage_tree(e["slug"])
    tree_html = ""
    if tree["status"] in ("cross", "blend"):
        # Tap-to-enlarge without script: a hidden checkbox toggles the label
        # (which holds the one copy of the SVG) between fit-to-card and a
        # full-size, scrollable overlay. --tree-w is the SVG's natural width.
        svg = render_tree_svg(tree)
        tree_w = int(re.search(r'viewBox="0 0 (\d+) ', svg).group(1))
        zid = f'zoom-{esc(e["slug"])}'
        hint = '<div class="rc-zoom-hint">tap tree to enlarge</div>' if tree_w > ZOOM_HINT_MIN_W else ""
        tree_html = (f'<div class="rc-tree"><input type="checkbox" class="rc-zoom-toggle" id="{zid}" hidden>'
                     f'<label class="rc-zoom" for="{zid}" style="--tree-w:{tree_w}px">{svg}'
                     f'<span class="rc-zoom-x" aria-hidden="true">×</span></label>{hint}</div>')
        unresolved = []
        _walk_unresolved(tree, unresolved)
        for name in unresolved:
            gaps.setdefault(name, set()).add(e["title"])
    return (
        f'<details class="research-card" id="{esc(e["slug"])}" data-search="{esc(search)}">'
        f'<summary>'
        f'<div class="rc-head">'
        f'<span class="rc-name">{esc(e["title"])}</span>'
        f'<span class="rc-badge rc-{e["badge"]}">{esc(e["badge"])}</span>'
        f'<span class="rc-status {status_cls}">{status_txt}</span>'
        f'</div>'
        f'<div class="rc-formula">{formula_html} {ev_html}</div>'
        f'<div class="rc-axes">grower: {esc(grower)} &nbsp;·&nbsp; processor: {esc(proc)}</div>'
        f'</summary>'
        f'{tree_html}'
        f'<div class="rc-body">{md_to_html(e["markdown"])}</div>'
        f'</details>'
    )


def collapsible(section_id, title, inner):
    return (
        f'<details class="collapsible grey" id="{section_id}">'
        f'<summary><h2>{title}</h2></summary>'
        f'<div class="collapsible-body research-doc">{inner}</div>'
        f'</details>'
    )


# Trees narrower than this fit a card at full size on most screens -- no hint.
ZOOM_HINT_MIN_W = 440

JS = """<script>
(function(){
var inp=document.getElementById("researchSearch");
var cards=document.querySelectorAll(".research-card");
var none=document.getElementById("noResults");
var count=document.getElementById("cardCount");
function apply(){
var q=inp.value.toLowerCase().trim();var v=0;
cards.forEach(function(c){var m=!q||c.dataset.search.indexOf(q)!==-1;c.classList.toggle("hidden",!m);if(m)v++;});
none.style.display=v===0?"block":"none";
count.textContent=v+" of "+cards.length;
}
inp.addEventListener("input",apply);apply();
})();
(function(){
function openAncestors(el){while(el){if(el.tagName==="DETAILS")el.open=true;el=el.parentElement;}}
function openTarget(hash){if(!hash)return;openAncestors(document.querySelector(hash));}
openTarget(window.location.hash);
window.addEventListener("hashchange",function(){openTarget(window.location.hash);});
document.querySelectorAll("a[href^='#']").forEach(function(a){a.addEventListener("click",function(){
openAncestors(document.querySelector(this.getAttribute("href")));});});
})();
document.addEventListener("keydown",function(ev){if(ev.key==="Escape"){
document.querySelectorAll(".rc-zoom-toggle:checked").forEach(function(c){c.checked=false;});}});
</script>"""


def build_html(entries, gaps):
    nodes_md = (RESEARCH / "lineage_nodes.md").read_text(encoding="utf-8")
    node_ids = parse_node_ids(nodes_md)
    cards = "".join(card_html(e, node_ids, gaps) for e in entries)
    browser = (
        '<div class="section" id="catalog">'
        '<div class="section-header"><h2>Strain Catalog</h2></div>'
        '<p class="note">Pre-jar lineage catalog. Every claim carries an evidence word, a claimant, and a date — anchor tier means what the party says, not what is biologically true. Tap a card for the full entry.</p>'
        '<div class="search-wrap research-search">'
        '<input class="search-input" type="search" placeholder="Search strains, parents, growers…" id="researchSearch" autocomplete="off">'
        '<span class="rc-count" id="cardCount"></span>'
        '</div>'
        f'<div class="research-list">{cards}'
        '<div class="no-results" id="noResults">No entries match</div>'
        '</div>'
        '</div>'
    )

    nodes = add_node_ids(md_to_html(nodes_md))
    brands = md_to_html((RESEARCH / "brands.md").read_text(encoding="utf-8"))
    sources = md_to_html((RESEARCH / "SOURCES.md").read_text(encoding="utf-8"))
    conventions = md_to_html((RESEARCH / "README.md").read_text(encoding="utf-8"))

    sections = (
        collapsible("lineage-nodes", "Lineage Nodes", nodes)
        + collapsible("brands", "Brands", brands)
        + collapsible("sources", "Source Atlas", sources)
        + collapsible("conventions", "Conventions", conventions)
    )

    stamp = denver_local(datetime.now(timezone.utc)).strftime("%B %d, %Y")
    footer = (f'<div class="footer">Document last updated: {stamp} &nbsp;·&nbsp; '
              f'{len(entries)} entries &nbsp;·&nbsp; Dabby the House Rig</div>')

    cover = ('<div class="cover">'
             '<h1>Dabby the House Rig</h1>'
             '<p class="subtitle"><a href="index.html">Session Log</a> &nbsp;·&nbsp; Research</p>'
             '</div>')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dabby the House Rig — Research</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="doc">
{cover}
{browser}
{sections}
{footer}
</div>
{JS}
</body>
</html>"""


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    paths = sorted(STRAINS.glob("*.md"))
    if not paths:
        print("VALIDATION ERRORS:\n  research/strains/ has no entries")
        sys.exit(1)
    for req in ("lineage_nodes.md", "brands.md", "SOURCES.md", "README.md"):
        if not (RESEARCH / req).exists():
            print(f"VALIDATION ERRORS:\n  research/{req} missing")
            sys.exit(1)

    entries = [parse_entry(p) for p in paths]
    problems = [(e["slug"], err) for e in entries for err in e["errors"]]
    if problems:
        print("VALIDATION ERRORS:")
        for slug, err in problems:
            print(f"  research/strains/{slug}.md: {err}")
        sys.exit(1)

    entries.sort(key=lambda e: e["title"].lower())
    gaps = {}
    OUT.write_text(build_html(entries, gaps), encoding="utf-8")
    unresolved = [e["title"] for e in entries if e["badge"] == "unresolved"]
    print(f"Wrote {OUT.name}: {len(entries)} entries"
          + (f"; unresolved type on: {', '.join(unresolved)}" if unresolved else ""))

    print(f"Lineage gaps: {len(gaps)} unresolved names")
    for name in sorted(gaps, key=str.lower):
        trees = ", ".join(sorted(gaps[name]))
        print(f"  {name} — in: {trees}")


if __name__ == "__main__":
    main()
