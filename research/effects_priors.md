# Effects Priors — Lineage Reputation Tags

Which way a cultivar's *reputation* leans: `daytime` (uplifting / energetic),
`heavy` (sedating / body), or `none` (a known cultivar with a mixed or
balanced reputation — counted as untagged, never as unknown). Read by
`Dabby_Research_Renderer.py` to compute each jar's **lineage lean**: the
share of its pedigree that traces to daytime-tagged and heavy-tagged names.

## What this is not

- Not a measurement and not a forecast. Every tag is an attributed
  reputation claim; the lineage under it is an attributed claim too — the
  lean is two hedges deep.
- Not a dose. Traits segregate rather than average: a jar with a quarter
  of its pedigree in Sour Diesel has odds of expressing it, not 25% of it.
- Not brand reputation (that never enters the repo). These are
  cultivar-level reputations in general circulation.
- The owner's jar log outranks this table. A `log` source line beats any
  number of `training` lines, and a jar actually run overrides its own
  lineage read.

## Rules

- Two tags only. Unsure → `none`, or no row at all.
- A tag may sit on an interior name (GMO, Mazar, Pinesoul): the walk stops
  there and counts that name's whole share, without expanding its parents.
- Names match after the renderer's normalization and alias table; the
  `Also matches` column lists further exact spellings (cuts, lines) that
  take the same tag. No substring or fuzzy matching.
- Source classes: `log` (the owner's jar log — cite the jar) · `training`
  (scene consensus per model training — the weakest class; verify before
  leaning on it).
- One line per name. Changing a tag regenerates every lean on the page.

## Tags

| Name | Lean | Also matches | Source |
|---|---|---|---|
| Sour Diesel | daytime | AJ's Cut Sour Diesel; Sour Diesel IBL | training |
| East Coast Sour Diesel | daytime | | training |
| NYC Diesel | daytime | | training |
| Tangie | daytime | | training |
| Clementine | daytime | | training |
| California Orange | daytime | | training |
| Agent Orange | daytime | | training |
| Lemon G | daytime | | training |
| Haze | daytime | Original Haze; Neville's Haze | log — Lemon Heads + Blueberry Haze ("daytime, upright, functional", `jars/lhbh.py`); training |
| Super Silver Haze | daytime | | training |
| Super Lemon Haze | daytime | | training |
| Amnesia Haze | daytime | | training |
| Ghost Train Haze | daytime | | training |
| Jack Herer | daytime | Jack the Ripper; J1 | training |
| Cinderella 99 | daytime | C-99; C99 | training |
| Space Queen | daytime | | training |
| Durban Poison | daytime | Durban | training |
| Thai | daytime | Chocolate Thai | training |
| Colombian Gold | daytime | | training |
| Acapulco Gold | daytime | | training |
| Panama Red | daytime | | training |
| Malawi | daytime | | training |
| Green Crack | daytime | | training |
| Trainwreck | daytime | | training |
| Golden Goat | daytime | | training |
| Strawberry Cough | daytime | | training |
| Goji OG | daytime | | training (weaker than the lines above) |
| Pinesoul | daytime | | training — a Goji OG pheno per `lineage_nodes.md`; tagged as a whole |
| Headbanger | daytime | | training — Sour Diesel × Biker Kush per scene consensus; unverified |
| Granddaddy Purple | heavy | | training |
| Purple Punch | heavy | | training |
| Bubba Kush | heavy | | training |
| Grape Ape | heavy | | training |
| Afghani | heavy | | training |
| Sensi Star | heavy | | training |
| Ice Cream Cake | heavy | | training |
| Do-Si-Dos | heavy | | training |
| Triple OG | heavy | | training |
| GG4 | heavy | | training |
| GMO | heavy | | training — tagged as a whole (its parents Chem D × GSC are both `none`) |
| Mazar | heavy | | training — tagged as a whole |
| Papaya | none | | Reputation says relaxing; the one log hint (Fembot #3, an inferred Rambutan cross: "upbeat, creative") points the other way. Owner unsure, Sept 21 2026 — left untagged. In more trees than any other name; revisit when the log has a lean read on a Papaya jar |

Names on the classics stop-list with no row here (Zkittlez, Gelato, GSC,
Sunset Sherbert, Runtz, OG Kush, Chem D, Skunk #1, Strawberry Banana,
Wedding Cake / Wedding Crasher, Grape Pie, Blueberry, Headband, White
Widow, Super Skunk…) are deliberately untagged: mixed or balanced
reputations.

## Provenance

Drafted Sept 21, 2026 in conversation with the owner, after a hand-run
"which jars lean daytime" pass over the Lightshade Federal Heights and
IgadI Northglenn menus. The owner's log records how hard a run hit, not
which way it leaned — until it does, almost every line here is `training`.
