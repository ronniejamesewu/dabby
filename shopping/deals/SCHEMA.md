# Deals schema

Register of the JSON shape used by every file under `shopping/deals/`. Owned by
`menu_price.py`. Facts only — no opinions, no fabricated specifics.

## File-level

```
{
  "store":    str   store_key, matches menu_fetch.STORES key
  "captured": str   ISO date the posted text was read (posted files only;
                     feed files carry the fetch's own captured date)
  "source":   str   URL or named source ("reefermadnessdenver.com",
                     "r/LightshadeDispensary + r/COents weekly thread")
  "deals":    [Deal, ...]
}
```

Two files may exist per store: `<store_key>.json` (hand-authored, `source:
"posted"` per deal) and `<store_key>_feed.json` (machine-written by `deals
fetch`/`deals load`, `source: "feed"` per deal). `load_deals(store_key)`
reads both when present and merges their `deals` lists; each deal keeps its
own `source`.

## Deal object

```
{
  "id":         str   stable id; tiers of one storefront deal share a prefix
                       (e.g. "lightshade_710labs_window", "lightshade_710labs_allday")
  "name":       str   short human label
  "source":     "feed" | "posted"
  "kind":       "percent" | "target_price" | "bogo" | "bundle"
  "value":      number | null   percent (0-100) for kind=percent; dollar
                       target for kind=target_price/bogo; null for bundle
  "brand":      str | null      posted/feed brand text, matched normalized
  "scope":      "brand" | "store" | "category" | "product"
  "category":   str | null
  "days":       [0-6] | null    Sun=0..Sat=6; null = every day
  "start":      ISO date | null
  "end":        ISO date | null
  "hours":      {"start": "HH:MM", "end": "HH:MM"} | null   local (Denver) time window
  "excludes":   [regex str, ...]   tested against row.raw_name BEFORE any percent
  "includes":   [regex str, ...] | null
  "menu_type":  "rec" | "med" | "both"
  "stack":      "no" | "yes" | "unknown"   whether THIS deal combines with
                       OTHER deals (separate from the store-wide stacking rule
                       in menu_fetch.STORES[store]["stacking"])
  "notes":      str   facts only ("exclusions unstated", "gummies, non-concentrate")
  "requires_id": bool (optional, default false)   set true for discounts gated on
                       ID verification the engine cannot check (industry/veteran/
                       senior, etc.) -- price_on never auto-applies these; `deals
                       list` still surfaces them as informational
}
```

`applicable(deal, row, when)` checks, in order: day-of-week, hours window,
start/end date, menu_type, scope/brand/category match, then excludes/includes
against `row.raw_name`. `price_on` only folds `kind: "percent"` deals into
the price math; `target_price`, `bogo`, and `bundle` deals are still listed
(surfaced in output/notes) but not computed.
