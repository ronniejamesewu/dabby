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

def card_html(e, node_ids):
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
</script>"""


def build_html(entries):
    nodes_md = (RESEARCH / "lineage_nodes.md").read_text(encoding="utf-8")
    node_ids = parse_node_ids(nodes_md)
    cards = "".join(card_html(e, node_ids) for e in entries)
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
    OUT.write_text(build_html(entries), encoding="utf-8")
    unresolved = [e["title"] for e in entries if e["badge"] == "unresolved"]
    print(f"Wrote {OUT.name}: {len(entries)} entries"
          + (f"; unresolved type on: {', '.join(unresolved)}" if unresolved else ""))


if __name__ == "__main__":
    main()
