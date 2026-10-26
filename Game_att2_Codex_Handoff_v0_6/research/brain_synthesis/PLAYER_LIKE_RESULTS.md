# Player-like and Adversarial Brain Synthesis Results

Date: 2026-08-25

Status: **SYNTHETIC DESIGN RESEARCH. NOT HUMAN PLAYTEST EVIDENCE, CURRENT PAPER
AUTHORITY, PRODUCTION BALANCE, OR IMPLEMENTATION APPROVAL.**

## Outcome

The v0.2 repair was rejected. The Item Card was consuming an Attention Slot and the
Commitment guarantee was masking that self-created pressure.

The optimized candidate is:

- four Body/Technique Attention Slots;
- one separate deliberately Readied Item Card with no automatic replacement;
- mandatory six-card Body Core;
- three selected compatible Techniques: two Main, one Preparation, at least two
  exact sources;
- weighted persistent draw without a Main/category guarantee;
- permanent paired Brain Parts with one primary lever;
- one validated Blood-paid redraw before commitment.

## Algorithms used

1. Exhaustive enumeration of every two-, three-, and four-Technique package.
2. Six transparent procedural-persona policies.
3. Paired seeded Monte Carlo comparisons for Brain/no-Brain effects.
4. Generated state-machine cases for causal and action-budget invariants.
5. Hostile source-loss and exact-source commitment checks.

Full rationale and primary references are in `METHODS.md`.

## Why three Techniques with 2 Main + 1 Preparation won

| Package | Build choices | Main drought avg / worst | Worst post-loss | Technique share | Brutal result |
|---|---:|---:|---:|---:|---|
| Two: 1 Main + 1 Prep | 9 | 4.96% / 10.27% | 19.93% | 25.14% avg | Too little Technique identity; hostile packages fail |
| Three: 1 Main + 2 Prep | 9 | 15.35% / 24.43% | 46.53% | 35.20% avg | Unplayable drought profile |
| Three: 2 Main + 1 Prep | 9 | 0.93% / 1.57% | 2.93% | 32.91% avg | Best compromise |
| Four: 2 Main + 2 Prep | 9 | 5.83% / 8.50% | 15.80% | 41.22% avg | More deck presence, worse reliability |
| Four: 3 Main + 1 Prep | 3 | 0.23% / 0.23% | 0.47% | 41.01% avg | Reliable but almost no package authorship |

The three-card 2M/1P rule preserves nine build combinations and avoids a guarantee.
It is less consistent than the four-card 3M/1P package, but the latter forces all
three Main Techniques and leaves only the Preparation choice. That is deck-building
theatre, not meaningful authorship.

## High-confidence candidate distribution

Each of the nine candidate packages ran 2,000 seeded six-round sessions under each
Brain condition: 36,000 sessions and 216,000 observed rounds total.

| Brain | Main drought avg / worst | Post-loss avg / worst | Prep+Main coverage | Technique share | Attack share |
|---|---:|---:|---:|---:|---:|
| None | 0.92% / 1.52% | 1.67% / 2.85% | 97.74% | 33.31% | 20.88% |
| Access fixture | 0.60% / 0.98% | 1.09% / 1.88% | 96.04% | 33.52% | 24.75% |

The Access Brain changed attack presence by 3.87 percentage points without dominating
Technique share or eliminating imperfect hands. That is a healthy structural shape,
although human perceptibility remains unknown.

## Procedural-persona results

Each persona played all nine candidate packages over 250 seeds: 13,500 observed
rounds per persona and 81,000 rounds total.

| Persona | Main use | Preparation | Item use | 2+ Main options | 2+ Main categories | Technique visible | Technique use | Main A/D/U |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Bruiser | 99.94% | 96.06% | 0.00% | 91.84% | 77.77% | 88.90% | 31.43% | 62.12 / 3.08 / 34.81 |
| Survivor | 99.89% | 99.52% | 16.64% | 79.94% | 59.90% | 78.87% | 37.65% | 30.45 / 19.52 / 50.03 |
| Schemer | 99.71% | 99.52% | 16.67% | 77.56% | 59.27% | 78.31% | 38.15% | 31.31 / 16.70 / 52.00 |
| Adapter | 99.76% | 99.52% | 16.67% | 80.89% | 62.96% | 79.15% | 37.27% | 35.40 / 15.30 / 49.31 |
| Satisficer | 99.96% | 99.52% | 9.11% | 90.32% | 70.16% | 94.80% | 22.11% | 60.39 / 16.40 / 23.21 |
| Wanderer | 97.76% | 69.62% | 13.36% | 66.99% | 53.10% | 86.84% | 30.25% | 45.91 / 13.62 / 40.47 |

No single card exceeded 18.05% of selections. Bruiser refusing the item while
survival/utility personas used the one available item demonstrates that the Readied
lane can support different priorities. This comes from transparent synthetic utility
weights, not observed human psychology.

## Invariant and reproducibility evidence

- Unit suite: 21 tests passed.
- Generated configurations: 20,000.
- Generated rounds: 100,041.
- Action-budget, item-timing, source-legality, and Commitment failures: 0.
- Shared-source Preparation/Main commitment failures: 0.
- Repeated player-like reports with identical inputs: byte-identical.
- No production source, config, approved scenario, or content was imported or changed.

## Brutal failures still open

1. Preparation is almost automatic for five policies. Until cards face meaningful
   costs, risks, conflicts, or enemy pressure, the staged Preparation layer may be
   busywork.
2. Survivor and Schemer behavior remains close. The neutral catalogue offers limited
   defensive Main expression; automatic defence may justify that, but the fixture
   cannot decide it.
3. The Brain's access change may be too subtle for players to perceive.
4. Execution Brain balance remains unproven and unsafe when its nerf is avoidable.
5. Item readiness may still feel like artificial forgetting to humans.
6. Technique acquisition could become a second roguelite progression grind and
   compete with the Brain.
7. Persona policies deliberately prefer a Main whenever legal; Main-use percentages
   therefore measure availability more than human willingness.
8. The Blood-paid redraw and its unapproved cost were not simulated. Reported drought
   is pre-redraw.
9. The Access fixture is a homogeneous all-slot stress profile, not finished per-slot
   Brain content.

## Evidence verdict

The optimized candidate is structurally playable, causally coherent, resistant to the
tested bad builds, and more faithful to the owner's original identity than either a
full active deck or v0.2. It is not proven experientially balanced or fun. The correct
status is **continue to a bounded human diagnostic; do not implement in production**.
