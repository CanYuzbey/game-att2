# Player-like Test Method Selection

Status: **RESEARCH METHOD NOTE. NOT HUMAN EVIDENCE OR GAMEPLAY AUTHORITY.**

## Methods applied

### Transparent procedural personas

Six deterministic policies represent deliberately different utility priorities:
Bruiser, Survivor, Schemer, Adapter, Satisficer, and Wanderer. The approach is a
small, inspectable adaptation of procedural-persona research, where different utility
weights produce different synthetic play styles. The project fixture does not use
MCTS or claim that these policies predict real people.

Primary reference: [Holmgård et al., Monte-Carlo Tree Search for Persona Based Player
Modeling](https://ojs.aaai.org/index.php/AIIDE/article/view/12849).

### Exhaustive adversarial package enumeration

The evaluator checks every two-, three-, and four-Technique subset in the neutral
catalogue instead of validating only a designer-favoured balanced build. It records
the worst, average, and best drought, timing coverage, Technique share, and source
diversity. This is finite combinatorial search, not a sample of human deck-building.

### Generated state-machine cases

Seeded generation varies slot count, Technique package, Brain fixture, source-loss
round, lost source, encounter length, Commitment rule, and Item-lane ownership. It
asserts action-budget, item-timing, source-legality, and Commitment invariants. This
follows the project skill's recommendation to use property/state-machine testing when
examples leave combinatorial gaps.

Property-based testing is useful for broad invariant coverage, but generated inputs
can miss sparse meaningful states unless generation is guided. That is why exhaustive
package enumeration and explicit source-loss cases remain separate.

Primary reference: [Lampropoulos, Hicks, and Pierce, Coverage Guided Property Based
Testing](https://doi.org/10.1145/3360607).

### Paired seeded Monte Carlo distributions

The same packages and seed ranges compare no-Brain and Access-Brain configurations.
This isolates tendency changes, drought risk, and source-loss sensitivity without
pretending that neutral fixture values are production balance values.

## Methods considered but not applied

- **Full MCTS:** rejected for this stage. Six rounds and a provisional utility model
  make exhaustive legal-plan scoring simpler and more inspectable.
- **Reinforcement learning:** rejected. It would optimize an invented reward function
  and risk laundering fixture assumptions into apparent balance evidence.
- **MAP-Elites:** its quality-diversity principle motivated using behaviorally distinct
  policies, but evolving a large agent archive is unnecessary for this bounded card
  model. Primary reference: [Guerrero-Romero and Perez-Liebana, MAP-Elites to Generate
  a Team of Agents that Elicits Diverse Automated Gameplay](https://kisenshi.github.io/files/paper-map-elites-generation-team-agents-behaviour.pdf).
- **LLM simulated players:** rejected as balance evidence. Their explanations may be
  useful for heuristic review but are not stable behavioral measurements.

## Evidence limit

These methods can expose broken builds, dominant structural incentives, unreachable
or illegal states, policy collapse, and distribution risk. They cannot prove fun,
comprehension, emotional tension, accessibility, fairness, or long-term replay desire.
