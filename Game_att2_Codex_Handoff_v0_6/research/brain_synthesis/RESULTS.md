# Brain Synthesis Pre-Implementation Test Report

> **SUPERSEDED DIAGNOSTIC (2026-08-25):** this report caught the embedded-item hand
> pressure but repaired it with a Commitment guarantee. Later player-like testing
> found the cleaner correction: keep one deliberately Readied Item Card in a separate
> lane, prohibit automatic replacement, retain four real Attention Slots, and remove
> the guarantee. See `PLAYER_LIKE_RESULTS.md`.

Date: 2026-08-22

Status: **STRUCTURAL RESEARCH EVIDENCE. NOT PRODUCTION BALANCE APPROVAL, HUMAN
PLAYTEST EVIDENCE, CURRENT GAME AUTHORITY, OR IMPLEMENTATION AUTHORIZATION.**

## Bottom line

The unguarded synthesis is not ready to implement. It is technically executable but
produces too many rounds without a Main action at realistic small hand sizes.

The revised synthesis with a neutral Commitment floor is structurally playable in
this fixture: it produced no dead hands, Main droughts, illegal action attempts, or
action-budget violations. It is still not proven balanced, fun, understandable, or
good over long-term play. Four total Attention Slots are the best human-test candidate,
not an approved final value.

## What was tested

- Three systems: owner original, later active deck, and v0.2 synthesis.
- 18 configurations, 5,000 deterministic six-round sessions each.
- 540,000 observed rounds in the final matrix.
- Three, four, and five total Attention Slots.
- Balanced, aggressive, and defensive technique/deck profiles.
- Right Arm source loss after round three.
- Synthesis both with and without the Commitment floor.
- No Brain, Access Brain, and Execution Brain diagnostic fixtures.
- Readied Item Card visibility, use budget, and exact-source invalidation.

The neutral fixture deliberately contains no real enemy balance, damage numbers,
economy, rarity, progression pacing, or production card content.

## Decisive results

| Configuration | Main drought | Post-loss drought | Prep + Main available | Dead hand | Verdict |
|---|---:|---:|---:|---:|---|
| Owner original, 4 slots | 0.00% | 0.00% | 83.02% | 0.00% | Structural pass |
| Later balanced active deck, 4 slots | 0.00% | 0.00% | 100.00% | 0.00% | Structural pass |
| Synthesis, 3 slots, no floor | 26.03% | 39.15% | 57.52% | 0.00% | Revise |
| Synthesis, 4 slots, no floor | 10.34% | 18.27% | 83.57% | 0.00% | Revise |
| Synthesis, 5 slots, no floor | 1.64% | 3.08% | 97.03% | 0.00% | Structural pass, capacity-heavy |
| Synthesis, 3 slots, floor | 0.00% | 0.00% | 28.74% | 0.00% | Playable but tactically narrow |
| Synthesis, 4 slots, floor | 0.00% | 0.00% | 46.38% | 0.00% | Best next test candidate |
| Synthesis, 5 slots, floor | 0.00% | 0.00% | 61.18% | 0.00% | Playable; capacity-risk |
| Later defensive active deck, 4 slots | 64.38% | 71.05% | 35.62% | 0.00% | Revise |
| Synthesis defensive profile, 4 slots, floor | 0.00% | 0.00% | 60.85% | 0.00% | Structural pass |

All final configurations had 100% fixture item visibility before source-specific
invalidation. All recorded action-budget violations and invalid action attempts were
zero.

## Brutal interpretation

### Unguarded synthesis

Bad. A system that regularly shows options but cannot commit a Main action creates
fake choice. At three slots it fails more than one round in four; after source loss it
fails almost two rounds in five. At four slots it still fails often enough to become a
routine frustration. Do not implement that version.

### Synthesis with the Commitment floor

It fixes the catastrophic failure without making the Brain responsible for basic game
function. That separation is important: the player should not need a permanent Brain
upgrade merely to receive a playable turn.

However, “can always act” is a low bar. At four slots, the synthesis presents both
Preparation and Main timing in 46.38% of rounds. The owner original reaches 83.02%,
and the balanced later active deck reaches 100%. The synthesis may therefore feel
more constrained and less tactically expressive even while remaining legal.

Three slots are too narrow for a serious first human fixture. Five slots improve
coverage, but risk solving design quality through raw option capacity and weakening
future slot progression. Four is the least-bad diagnostic starting point.

### Mandatory Body Core

This is the strongest evidence for the hybrid. An unrestricted defensive active deck
collapsed to 64.38% Main drought. The synthesis stayed functional because body-owned
Main cards remained present. Player deck-building is valuable, but it needs either
composition rules or a mandatory embodied core. The synthesis protects originality
and reduces self-authored non-functional decks.

The cost is dilution: at four slots, 65.20% of visible synthesis action cards came from
Body and 34.80% from Techniques. That preserves embodied identity, but Technique
selection could feel weaker than advertised. Human testing must determine whether
one-third technique presence feels like authorship or garnish.

### Brain balance

The Access Brain was controlled through the same without-replacement draw cycle. A
+60% attack / -35% defence weighting moved draw share only modestly: attacks 35.58%
to 36.34%, defence 32.11% to 29.76%. This is structurally safe from obvious Brain
dominance, but may be too subtle for players to notice. Larger weights could recreate
draw frustration, so visibility and perception matter more than raw percentages.

The Execution Brain is the dangerous design. A symmetric +0.25 buff / -0.25 nerf is
not balanced merely because the numbers match. Its evaluated net was +0.25 when the
nerf was ignored, +0.125 when players valued it halfway, and 0 only when the full
penalty mattered. Any avoidable, delayed, or irrelevant nerf turns the Brain into a
strict permanent upgrade and threatens body/graft importance.

### Item Cards

The owner-style Readied Item Card survived the structural test. It stayed outside the
random Body/Technique draw, consumed a Preparation opportunity rather than inventing
an extra action, and disappeared when its exact Left Arm source was lost. This does not
prove that readiness choices are interesting or that healing will not dominate.

## Comparison verdict

| Aspect | Owner original | Later active deck | Revised synthesis |
|---|---|---|---|
| Distinct identity | Best | Weakest | Nearly as strong as original |
| Basic consistency | Strong with floor | Strong only with build constraints | Strong with floor |
| Player-authored build | Limited | Best | Strong but diluted by Body Core |
| Item-card originality | Preserved | Lost to direct inventory | Preserved |
| Brain roguelite identity | Strongest | Generic risk | Preserved, but nerfs need proof |
| Tactical timing coverage | Better than synthesis | Best in balanced profile | Currently weakest |
| Resistance to bad deck builds | Strong | Worst | Best evidence-backed compromise |
| Complexity and teaching cost | Lowest | Medium | Highest |

The revised synthesis is the best **candidate structure**, not the proven best game.
It earns that position because it combines embodied reliability, deliberate Item
Cards, and player-selected Techniques while preserving permanent Brain Parts. It also
has the greatest risk of becoming administrative system soup.

## Verification

- Built-in unit suite: 12 tests passed.
- Repeated 1,000-session JSON matrices: byte-for-byte identical.
- Final 5,000-session matrix: completed successfully.
- Runtime isolation: the fixture imports no production source, configuration, tests,
  examples, or catalogue files.

## Claims this evidence cannot support

No automated fixture can establish fun, comprehension, fairness, accessibility,
emotional clarity, satisfactory choice, final balance, or long-term replay value.
Those require human sessions using representative content. The next test must watch
whether players understand why cards appear, perceive Brain buffs and nerfs, value
Technique selection, remember the action budget, and experience the Readied Item as
preparation rather than artificial forgetting.
