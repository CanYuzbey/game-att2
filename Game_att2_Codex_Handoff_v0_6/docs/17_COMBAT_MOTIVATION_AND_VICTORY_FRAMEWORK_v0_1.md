# Game att2 — Combat Motivation and Victory Framework v0.1

Status date: 2026-08-01

Status: owner-directed prototype framework; Jeff is the bounded survey-test example.

## Implemented prototype status

- Motivation profiles, encounter parameters, and victory routes load from validated
  content data.
- Outcomes are evaluated after state mutation and recorded separately for player and
  enemy, so one encounter may legitimately produce mutual success.
- Jeff selects among legal bargain and attack intents deterministically. Configured
  scoring and an exact action-target repetition penalty prevent a fixed loop without
  adding opaque randomness.
- The reciprocal-repair bargain transfers existing inventory/body assets through the
  shared rule engine. Destroying the arm, spending the cream, or choosing hostility
  changes the available response naturally.
- Feedback schema 0.3 / questionnaire 0.2 stores motivation signals, actor outcomes,
  target distribution, ratings, and open-text inference without claiming that the
  participant is independent.
- Blood 0 is now a death resolution. Limb for Life may preserve an otherwise viable
  objective route by sacrificing a usable non-Core limb; it is a cost, not an
  independently completed objective.
- Bargain rejection returns to combat without a direct stat modifier.

## Owner-approved product decisions

1. Motivation is a general precondition for enemies and combat, not a Jeff-only rule.
2. Combat is a core mechanic but is not automatically the purpose of an encounter.
3. Player and opponent may both achieve their objectives in one resolution.
4. Capability defeat does not prescribe one universal ending. Depending on actor
   motivation and remaining affordances it may lead to bargaining, surrender,
   mercy, exploitation, escape, or another approved response.
5. Victory routes must feel like consequences of ordinary state and behavior. They
   are not bonus objectives or a narrow list of designer-authored answers.

## Required separation

| Layer | Question | Runtime role |
|---|---|---|
| Motivation | Why does the actor enter or continue the conflict? | Filters and scores legal responses. |
| Objective | What state is the actor trying to create? | Supplies testable predicates. |
| Victory route | Which state can satisfy the objective? | Evaluated from current facts after mutation. |
| Resolution | How did the encounter stop? | Records bargain, death, nonfatal collapse, incapacity, surrender, escape, or objective completion. |
| Outcome | How successful was each actor? | Complete, partial, failed, or unresolved per actor. |

Actions never select an outcome directly. They mutate Blood, body, inventory,
capabilities, pressure, or other approved facts. Victory-route predicates are then
evaluated against the resulting state.

## Generic motivation taxonomy

- `RESTORATION`: acquire or preserve body/resources needed to recover.
- `SURVIVAL`: remain viable or escape an unacceptable continuation cost.
- `CONTROL`: protect, contain, delay, or deny access to an objective.
- `ELIMINATION`: collapse, kill, or dominate the opponent.

Boss-specific objectives compose with these motivations; they do not require a new
hard-coded combat engine branch.

## Generic victory-route taxonomy

- `BLOOD_DEATH`
- `CAPABILITY_BREAK`
- `SURRENDER`
- `OBJECTIVE_COMPLETION`
- `BOSS_SPECIFIC`

The route registry is finite and data-driven. A boss-specific predicate must still
refer to explicit runtime state and pass the causal-resolution loop.

## Jeff survey hypothesis

Jeff uses the reversible prototype motivation `RECIPROCAL_REPAIR`:

```text
Jeff wants the player's Clotting Cream for his Open Wound Torso.
The player wants Jeff's graftable Right Arm.
Marking that Right Arm communicates demand.
If both assets remain available, Jeff may offer the marked arm for the cream.
```

This is a prototype hypothesis, not final canon. It was chosen because it tests all
of the owner's product decisions with existing assets and no new balance number:

- combat can create leverage rather than require death;
- both actors can succeed through one exchange;
- destroying the desired arm or consuming the cream naturally removes the bargain;
- continuing with a hostile Main action naturally rejects the offer;
- the same body system still supports combat, incapacity, pressure, and harvest
  routes.

Jeff initially uses non-lethal coercion: Desperate Swing alternates pressure between
the player's current offensive Left Arm and Torso rather than repeating one target.
Hostile continuation returns to legal combat without a rejection buff or debuff. This
prototype does not invent a wound mapping, anatomy rule, or direct Jeff-to-Blood value.

## Defeat acceptance and negotiation direction

Defeat acceptance is an internal assessment, not a resolution action. Objective
viability, remaining offense, recovery hope, desperation, honor, and character traits
may make negotiation, surrender, escape, resistance, or mercy-seeking more likely.

Either actor may propose a bounded negotiation. The intended future interaction is a
multi-exchange minigame: demand, offered bundle, motivation/personality evaluation,
counter-offer, acceptance, or return to combat. The current Jeff single-step bargain
is an instrumented test shortcut and must not be mistaken for the final system.

## Test hypotheses

| Hypothesis | Success evidence | Failure evidence |
|---|---|---|
| Players infer that Jeff wants repair material | Post-play answer identifies cream, wound care, trade, or survival | Most answers describe unexplained aggression or pure murder |
| Players perceive more than one resolution path | Players mention bargain plus at least one combat route | Players believe only arm destruction is legal |
| Mutual success feels natural | Bargain is described as state-derived and understandable | Bargain feels like a detached bonus prompt |
| Jeff's choices respond to state | Players connect mark, inventory, limb state, target, or Rage to behavior | Jeff is still described as random or repetitive |

No single self-test confirms these hypotheses. Valid external sessions and coded
responses are required before locking motivation, balance, or final narrative.

## Deferred decisions

- Final Jeff canon and dialogue.
- `Cover It` runtime implementation and exact values. Document 31 later approves its
  one-round paper target/source/redirection/trade-off contract without activating it.
- Direct Jeff-to-Blood threat and Ruined player-Torso consequence.
- Final generalized surrender psychology and boss-specific motivations.
- Whether all encounters expose motivation clues at the same information level.
- Multi-round negotiation timing, offer vocabulary, evaluation, and exit rules.

## Later Package A catastrophic-survival reconciliation (2026-08-19)

Document 37 supersedes the prototype's broad `usable non-Core limb` selection for
future paper design. The actor chooses an exact eligible attached usable Left Arm,
Right Arm, or Legs, or accepts death; selection is not random. The sacrifice may
preserve an otherwise viable route but never completes an objective by itself, and no
generic victory route requires Limb for Life. Existing prototype runtime and content
remain unchanged.
