from wisdom_core import *

ENTRY = WisdomEntry(
    key='baseline-philosophy',
    kind='theory',
    claim="Single baseline curve for all hash rosin with cold start; strain adjustment is "
          "empirical via swab results, not terpene reasoning. The baseline is first-contact "
          "(the safest opening for unknown potency), not best-operating for a known strain.",
    guidance="Do not design different starting curves from strain name, consistency type, or "
             "inferred terpene profile without empirical justification. New strains start "
             "from the current baseline. Promoting a winning operating curve to baseline "
             "needs two bars, not \"it delivers\".",
    grade='directional',
    grade_basis="Multi-strain Rig 5 data drove the Session 107 upgrade (FW106, BB36 #2, OC "
                "R14); Watermellos did not replicate; first-contact framing added Session 157.",
    evidence=[
        Citation(
            source='oc R14',
            role='confirms',
            provenance='ai-authored',
            gist="Matched the pattern: improved vapor density and swab results on the faster "
                 "ramp (multi-strain Rig 5 data behind the Session 107 upgrade). Provenance "
                 "untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='watermellos R10',
            role='counters',
            provenance='ai-authored',
            gist="The fast-ramp improvement did not replicate for Watermellos — almost no "
                 "vapor on draw 1; the upgrade may be material-specific rather than "
                 "universal. Provenance untagged in source.",
            confounds="The Watermellos exception is strain-level data, not a baseline "
                      "revision signal.",
        ),
        Citation(
            source='dbrb R1',
            role='context',
            provenance='ai-authored',
            gist="710 warning — a 440°F open on a mystery jar collides with the first-run "
                 "potency caution, which is what disqualifies a hot deliverer as baseline "
                 "even when it is a strain's operating curve. Provenance untagged in source.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Baseline Philosophy (core position)',
            text="Single baseline curve for all hash rosin with cold start. Strain-specific "
                 "adjustment happens empirically via swab results, not terpene-profile "
                 "reasoning. Do not design different starting curves from strain name, "
                 "consistency type, or inferred terpene profile without empirical "
                 "justification.",
        ),
        Position(
            stated='Session 107',
            text="**Current baseline (as of Session 107):** 380°F open → 400°F @4s → 420°F "
                 "@8s, hold to 60s. Fast 8-second ramp. Prior baseline (380→400→416, ~20s "
                 "ramp, 50s session) retired as `BASELINE_416`. Upgrade driven by "
                 "multi-strain Rig 5 data: FW106 and BB36 #2 both showed improved vapor "
                 "density and swab results on the faster ramp; OC R14 matched the pattern. "
                 "Wispy-vapor-with-material-remaining was a two-strain signal on the prior "
                 "baseline that the faster ramp resolved. Note: the fast-ramp improvement "
                 "did not replicate for Watermellos (WM R10 — almost no vapor on draw 1) — "
                 "the upgrade may be material-specific rather than universal. New strains "
                 "still start from the current baseline; the Watermellos exception is "
                 "strain-level data, not a baseline revision signal.",
        ),
        Position(
            stated='Session 157',
            text="**Baseline is first-contact, not best-operating (Session 157).** The "
                 "baseline's job is the safest opening for a jar of *unknown* potency — not "
                 "the best curve for a known strain. A hot deliverer like the 440°F "
                 "bounded-hold-descent can be a strain's operating curve while disqualified "
                 "as *baseline*: a 440°F open on a mystery jar collides with the first-run "
                 "potency caution (710 warning, dbrb R1). Promoting a winning operating "
                 "curve to baseline needs two bars, not \"it delivers\": (1) the descent "
                 "pattern past Low/single-rig — cross-rig plus a session-order-matched "
                 "440-descent-vs-420-ramp head-to-head; (2) a cooler-opening variant that "
                 "survives unknown-potency first contact. Do-Not-Re-Litigate: per-strain "
                 "440 wins are not, alone, a baseline-change argument. See BACKLOG "
                 "\"Baseline-change proposal.\"",
        ),
    ],
    counter_reading="The Session 107 fast-ramp upgrade did not replicate for Watermellos "
                    "(WM R10 — almost no vapor on draw 1), so \"single baseline for all hash "
                    "rosin\" may be over-generalized from a Rig 5 / subset-of-strains result "
                    "— a skeptic reads the current baseline as material-specific, not "
                    "universal.",
    watch_for="Cross-rig, session-order-matched 440-descent-vs-420-ramp head-to-head plus a "
              "cooler-opening variant surviving unknown-potency first contact would reopen "
              "the baseline question.",
    updated='Session 107; first-contact framing Session 157',
)
