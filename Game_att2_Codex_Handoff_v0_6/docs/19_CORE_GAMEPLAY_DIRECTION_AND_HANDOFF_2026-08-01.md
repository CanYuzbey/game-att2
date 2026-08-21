# Game att2 — Core Gameplay Direction and New-Conversation Handoff

Status date: 2026-08-21

Status: owner-resolved core-gameplay direction plus reversible prototype defaults.
The four H1 owner questions were resolved on 2026-08-11 and are specified in
`20_H1_HYBRID_COMBAT_SPEC_v0_1.md`, which the owner approved for implementation
planning on the same date. The bounded execution approval and verified 2026-08-12
fidelity result are consolidated in `21_H1_IMPLEMENTATION_RECORD_v0_1.md`. This
implementation is not evidence that the
loop is fun. Exact timing, damage, wound, and balance values remain research variables
requiring human playtest.

The 2026-08-12 owner diagnostic found that the fixed one-second terminal task is not
an adequate reflex-system test. The required interaction-family separation, current
timing-outcome explanation, revised diagnostic requirements, and optimized next
questions are recorded in
`23_REFLEX_INTERACTION_TAXONOMY_AND_DIAGNOSTIC_REVISION_v0_1.md`. Its taxonomy and
exact mappings remain proposals; no broader runtime gate is open.

The first question from that revision is resolved: the rival's attack normally
defines compatible response/input routes, the expected route, and their baseline
difficulty, while the player may direct the input type by choosing another legal
route. Some attacks intentionally have easy responses and others hard responses.

The timing shape is also resolved: routine attacks use a symmetric early/late curve
for learnability, while specifically defined harder attacks may use different visible
early and late state consequences.

The readiness boundary is resolved for visual-lab research planning: one small,
visible shared readiness resource replaces a standalone Block-pressure meter in the
lab hypothesis. Repeated Block creates stronger family-specific strain, low Blood
visibly amplifies existing strain, and explicit body impairment separately changes
legality or effectiveness. Blood remains the core health/currency/fuel resource.

This is not production-system or runtime approval. Exact accumulation, recovery,
terminology, and campaign integration remain provisional. VL-WP1 through VL-WP3 are
complete, and the owner approved VL-WP4 on 2026-08-13 for local diagnostic execution
and review only, then deferred it before execution later that day. The current H1
fixture remains unchanged and preserved for later research.

The 2026-08-16 Package D owner amendment in document 33 resolves body-state
capability mapping on paper. Local source condition owns Full, Strained, Desperate,
Dormant, or Invalid profiles; a closed effect-package interface owns reusable effect
semantics; and capped actor-relative Integrity Echo may alter one micro-axis without
changing legality, Attention Slots, plays, Lead, or automatic-response availability.
Runtime and effect content remain unapproved.

## 1. Why this document exists

The project accumulated many valid but interdependent questions. Future work should
not ask the owner to decide each minor variable independently. Work from five macro
decisions; treat smaller questions as configurable details beneath them.

The immediate subject is core gameplay. Art, presentation polish, content volume,
final narrative, full run structure, and release planning remain outside this gate.

## 2. Owner-approved direction

1. Combat remains turn-based at the strategic layer.
2. Core play must also contain reflexive execution moments that distinguish it from a
   purely menu-driven turn system; blocking an incoming strike through timing is the
   first concrete example.
3. At round start, the player can read the opponent's limbs, visible limb-state data,
   Blood band rather than necessarily exact Blood, and possibly a basic motivation
   clue. Observation and dialogue may reveal additional information.
4. Targeting a valued limb may cause protection, healing, counterpressure, sacrifice,
   bargaining, surrender, escape, or another motivation-supported response. There is
   no universal “targeted limb means defend” rule.
5. Recovery from a bad situation should reward diagnosis, sequencing, and timing:
   stabilize wounds, predict the next action, reduce the opponent's future options,
   trade ideal reward for safety, or pressure the opponent into another resolution.
6. State-derived outcomes remain binding. A reflex input modifies an action's
   execution; it does not teleport to an authored ending or restore an unusable source.

### Combat identity guardrail - approved 2026-08-13

The strategic layer must not evolve into an upgraded *Swords and Sandals*-style loop
of selecting attacks, comparing statistics, watching damage, and repeating. More
wounds, equipment, range rules, or numbers would not solve that identity problem by
themselves.

The intended loop is:

```text
read the opponent and current bodies
-> receive a bounded hand of tactical opportunities
-> choose a body-sourced action/card and commit its target and risk
-> perform any legal reflex interaction
-> apply Blood, wound, body, extraction, and position consequences
-> rebuild the next set of legal opportunities from the changed state
```

Cards are not merely a visual skin for an unchanged attack menu. The body should help
determine which opportunities can appear and must determine whether their physical
sources can execute them. Reflexes are not decorative quick-time events; they modify
how well a legal strategic commitment resolves. Neither layer may make the other
decorative.

Space and reach remain subordinate supporting grammar. Clinch, Engaged, and Distant
are outcomes of actions, defenses, reflex results, or other explicit combat events;
they are not freely editable movement choices. They can change card legality and
action profiles, but they must not create a standalone walk-forward/attack/walk-back
loop. Unmaintained exceptional range settles toward Engaged, while a dedicated range
build may sustain it through authored tactical opportunities.

The approved neutral cadence gives unmaintained Clinch one complete later playable
round and unmaintained Distant two complete later playable rounds before the next
round begins Engaged. Explicit maintenance or a new range outcome preserves or resets
the state. These are design meanings, not runtime implementation approval.

This guardrail does not approve a full deckbuilder, hand size, draw/discard algorithm,
movement-card list, broader reflex implementation, or new content.

### Brain Module progression approved; final numbers and Head interaction deferred

Document 39 is the current Brain/Attention authority. Rare Brain Parts persist through
death, are configured one per Attention Slot before a run, and remain locked for that
run. Usable body sources contribute exact card instances; weighted selection without
replacement guarantees neither Attack nor Defence. Hard-filtered slots resolve before
flexible slots and shade when no eligible match exists.

Unused legal cards persist. Spent/Invalid replacement waits for Decision Refresh, and
one validated immediate redraw per round spends a later-authored Blood cost. Inventory
remains directly accessible outside Attention Slots. Reflex defence remains automatic
and cardless. Final slot counts, weights, redraw cost, Brain Part/card content,
Head/Stun interaction, rare extra plays, save/runtime implementation, and UI remain
deferred. The historical three-slot/five-slot values are comparison fixtures only.

Document 40 resolves the Director-record collision: the approved baseline does not
add a separate collectible-technique or active-deck layer. Body construction authors
the eligible card pool and Brain configuration authors access. Conventional deck
construction remains a future hypothesis only if later evidence exposes a specific
authorship problem.

## 3. Target player experience

The desired combat question is:

> I understand enough of what this opponent wants and may do. Which body source do I
> risk, which enemy capability do I alter, and can I execute the response under
> pressure without destroying the body value I came to obtain?

Strategy determines **what and why**. Reflex execution influences **how well** the
committed response works. Neither layer should make the other decorative.

## 4. Five macro decisions

### Macro A — Information and prediction

Use four information layers as the reversible default:

| Layer | Default handling |
|---|---|
| Public physical facts | Limbs, broad limb condition, visible wounds/tags, equipment, posture/range, Blood band |
| Telegraph | Broad, partial, or exact next-action information |
| Discoverable | Motivation clues, valued limb, action source, recovery options, surrender/bargain tendency |
| Hidden | Exact Blood where appropriate, internal scoring, unrevealed special action, exact mental threshold |

Additional core-supporting public facts:

- whether the current target is reachable;
- which visible source appears committed to the telegraphed action;
- active protection and exposed-source states;
- projected immediate danger when an approved wound rule supports it;
- whether the actor still has an obvious attack, movement, or recovery capability.

Focus/observation improves information quality. Dialogue primarily reveals motive,
need, willingness, or fear. Neither should expose unexplained internal numbers.

### Macro B — Hybrid turn and reflex structure

**Owner amendment, 2026-08-16:** document 32 supersedes the reversible ordering below
for future design work with a public Lead, Lead-first lock, bounded telegraph, Reply
lock, sequential Lead resolution, full state recomputation, and unchanged Reply
revalidation. It preserves the Preparation/Main budget and automatic reflex boundary.
The older phase model remains historical context and does not change current runtime.

Use this modifiable phase model for the first hybrid prototype:

```text
1. State phase
   Apply approved ongoing effects; show public state and broad intent.

2. Preparation phase
   Choose one: Focus/observe, Fast treatment/item, short dialogue, or another later-
   approved preparation action. There is no universal short-step control.

3. Commitment phase
   Choose one Main action/card: attack, extraction tool, prepared defense,
   range-producing tactical action, treatment, negotiation attempt, surrender/escape
   attempt, or another legal action.

4. Revalidation phase
   Recompute sources, reach, costs, statuses, and objective viability.
   Cancel an action whose source or target is no longer legal.

5. Execution/reflex phase
   A telegraphed action may open a configured reflex opportunity. The player performs
   a valid response such as Block. Timing quality modifies the already-legal action.

6. Consequence phase
   Apply Blood/body/wound/item/position mutations and capability changes.

7. Response and resolution phase
   Re-evaluate intent, continuation, surrender, bargain, escape, incapacity, and death.
```

#### Reversible action-budget default

- one Preparation choice;
- one Main action;
- reflex opportunities are event-triggered, not another freely spendable Main action;
- each committed action names its body/tool source;
- one physical source cannot simultaneously perform incompatible Main and reflex jobs;
- range has no separate movement-point or generic reposition cost; the full tactical
  action/card and its defense/reflex result own any range outcome and cost;
- do not add Stamina or another universal resource to production combat until
  Blood/body/tempo and the approved lab evidence prove it necessary; an isolated
  shared-readiness lab hypothesis is permitted only after its bounded plan passes.

This intentionally replaces the current survey convenience of using both Focus and a
Fast item before the Main action. Retain the old behavior only as a comparison variant.

### Macro C — Reflex execution framework

A reflex event is data-defined by:

```text
triggering action
telegraph class
valid responses
required body/tool source
reach/position requirements
timing window profile
result grades
state mutation per grade
source commitment/exposure
failure consequence
```

First-prototype response: **Block**.

Block contract:

- the incoming action must be blockable and sufficiently telegraphed;
- the chosen blocking source must be usable, reachable, and not incompatibly committed;
- an unprepared block has a narrower opportunity and weaker/less safe result;
- a prepared Guard-type Main action provides a broader opportunity or stronger result;
- a successful block does not automatically erase all danger: the attack definition
  may reduce damage, redirect it into the blocking source, prevent a secondary effect,
  or create attacker exposure;
- a miss resolves the original legal attack without a hidden rescue;
- exact milliseconds and percentages are configuration/test values, not product
  decisions in this report.

Possible later response modules—add only after Block proves value:

- evade/step using Legs and range;
- counter using a prepared offensive source;
- catch/parry using a specific limb/tool;
- timed extraction or treatment execution.

These use the same reflex-event contract; they are not separate bespoke minigames.

#### Provisional defense roles

Owner amendment, 2026-08-14: document 31 supersedes the provisional status of this
table with the approved layered automatic defense contract. Reflex defense is a
transient event automatically surfaced from the incoming action and current build,
not a manually played Response card. The table remains useful role context; document
31 owns final preparation, automatic-event, passive-stacking, and consequence rules.

| Mechanic | Default role | Primary trade-off |
|---|---|---|
| Guard Flesh | Prepared direct-damage defense; improves Block and commits/exposes the guarding arm | Main-action tempo, Blood, and source availability |
| Brace | Prepared Knockdown defense, not general damage prevention | Main-action tempo and usable Legs |
| Braced Legs | One automatic Knockdown-prevention charge | Build/limb opportunity cost; no direct damage block |
| Cover It | Enemy prepared protection of a selected valued limb for one round | Enemy Main action and commitment/exposure of the covering source |
| Range-producing response | Avoid or change reach through an authored defense/card/reflex result | Its action opportunity, source, execution, and exposure; no universal movement command |

These roles are now architecture-level approved through document 31, while exact
success calculation, mitigation, exposure values, reflex inputs, readiness, and
runtime implementation remain deferred.

### Macro D — Body consequences and tactical conflict

The required causal chain remains:

```text
action and execution grade
→ integrity/wound/position mutation
→ Blood and functional consequence where approved
→ available actions and reflex responses change
→ objective and encounter viability change
```

The central extraction conflict should frequently be:

> The limb I want is also dangerous, protects something important, or is difficult to
> preserve. Destroying it makes the present safer but weakens or removes my reward.

General target-response evaluation uses:

- value of the limb to the actor's objective;
- action/defense/movement capabilities sourced by the limb;
- remaining substitute sources;
- ability and hope to repair or replace it;
- opponent's apparent intention to destroy, disable, sever, or bargain for it;
- survival pressure and expected continuation cost;
- documented motivation and traits such as desperation, honor, preservation, or rage.

Possible responses—protect, heal, substitute, counterpressure, sacrifice, bargain,
surrender, escape, or deceive—must remain legal under current state.

The wound classes and qualitative physical-consequence meanings were approved by the
2026-08-13 owner amendment in document 27. Numeric Blood, repair, treatment, and rescue
timing remain a later subordinate package. Select those values only after the hybrid
turn cadence can be played, because timing, mitigation, and attack frequency determine
viable numbers.

### Macro E — Encounter resolution and body-build payoff

Core combat needs only a minimum resolution vocabulary initially:

- continue conflict;
- objective completion;
- Blood-0 death after prevention checks;
- offensive incapacity;
- surrender offered/accepted/refused;
- bounded asset-based bargain;
- escape/disengagement;
- unresolved if an unapproved rule is required.

The full negotiation minigame, detailed psychology, boss taxonomies, and final outcome
presentation are subordinate systems. For the first hybrid prototype, use only current
assets and a small number of inspectable motivation inputs.

Combat must feed Body as Build:

```text
fight for a body/resource objective
→ preserve, ruin, trade, or extract it
→ graft/repair/integrate/refuse
→ gain and lose concrete capabilities
→ face a later pressure that makes the changed body matter
```

A full map or meta-progression system is not required to prove this. One short chain of
two contrasting encounters plus one maintenance decision is sufficient.

## 5. Minor questions absorbed under the macros

Do not reopen these as independent owner interviews unless testing finds a P0 conflict:

- exact reflex-window duration and grade thresholds;
- exact damage reduction/redirect percentage per Block grade;
- exact Blood-band display wording;
- exact intent text and dialogue wording;
- exact movement-band names;
- exact repetition penalty in enemy scoring;
- exact mental weights and bargain scores;
- exact wound/Blood numbers after cadence is proven;
- exact number of negotiation exchanges beyond the bounded prototype;
- exact input binding and presentation treatment.

Treat these as data/configuration, UX implementation, or balance-test variables. Surface
them to the owner only when a result would materially change the target experience.

## 6. Four owner-level questions — resolved 2026-08-11

1. **Skill balance:** Strategy leads. Reflex skill usually makes modest improvements,
   while exceptional execution may rarely rescue an extreme but still legally
   recoverable situation. Reflexes cannot repeatedly erase a structurally bad plan.
2. **Reflex frequency:** Reflexes are broadly present in readable physical
   interactions. Most have small effects, prepared or strongly telegraphed moments may
   have material effects, and life-changing effects are rare.
3. **Failure severity:** Ordinary misses apply only the original consequence.
   Additional exposure is legal only for a clearly disclosed and voluntarily selected
   high-risk response.
4. **Body-build proof:** Jeff's grafted Right Arm is both the strongest defensive
   response source against Anna and a body asset put at risk by using it. Damage or
   loss weakens or removes the response.

The smallest testable contract originally derived from these decisions was
`20_H1_HYBRID_COMBAT_SPEC_v0_1.md`. Later owner decisions deferred broader H1/reflex
work and independently approved wound, range, staged-turn, and Attention Slot design
directions. Use documents 24 and 27-29 for the current gate rather than treating this
historical H1 dependency as a blocker.

## 7. First hybrid prototype — H1

### Scope

- one existing bounded opponent setup;
- current six-slot body and Blood model;
- broad/partial/exact intent;
- one Preparation choice and one Main action;
- one reflex type: Block;
- prepared Guard versus unprepared Block comparison;
- source loss cancels attacks/reflexes;
- no new enemy, limb roster, production Stamina system, full negotiation, full
  movement map, art, or engine work.

### Hypothesis

Turn planning plus a short, readable reflex opportunity creates more tension and
personal execution ownership without making body state, intent reading, and Blood
decisions decorative.

### Continue evidence

- players can explain the incoming threat and why Block was or was not available;
- preparing defense changes the reflex opportunity or consequence meaningfully;
- destroying/damaging an action source changes both planned and reflex affordances;
- perfect reflex play does not make Blood, wounds, target choice, and build irrelevant;
- poor reflex execution is recoverable through costly state-legal decisions in some,
  but not all, situations;
- players report both planning and execution as relevant to success;
- action logs distinguish strategic choice, reflex result, and resulting mutation.

### Revise evidence

- reflex prompts feel like unrelated quick-time events;
- every attack is trivially negated;
- prepared defense is never worth its Main action;
- damaged/missing limbs do not change valid reflexes;
- players watch the timing cue and ignore opponent state;
- failure cascades without a readable recovery choice;
- reflex timing overwhelms extraction and body-build decisions.

### Kill/pivot evidence

- repeated tests show that reflex execution and turn planning consistently undermine
  rather than reinforce one another;
- the hybrid loop requires so many special exceptions that state-derived rules stop
  being inspectable;
- the reflex layer is enjoyable only when body, Blood, and extraction consequences are
  removed.

## 8. Modifiability contract

Future implementation should keep these concepts separate even if names change:

```text
TurnPlan            strategic Preparation/Main commitments
ActionDefinition    source, target, reach, cost, telegraph and base effects
TelegraphProfile    public information and reflex eligibility
ReflexOpportunity   valid responses, timing profile and required source
ExecutionGrade      outcome class, not direct victory
StateMutation       body/Blood/wound/item/position changes
CapabilityView      recomputed legal actions and responses
ResolutionCheck     state-derived continuation/outcome evaluation
```

Timing values, valid response sets, mitigation rules, information clarity, and range
requirements must be configurable. Reflex processing must not print, decide narrative,
restore broken sources, or bypass the shared consequence loop.

## 9. Risks

| Risk | Control |
|---|---|
| Reflex becomes QTE decoration | Every reflex requires a state-valid source and produces an explicit mutation |
| Reflex invalidates strategy | Prepared state, source condition, reach, and original action still constrain success |
| Strategy invalidates reflex | Reflex grades must materially change at least one meaningful consequence |
| Combat becomes a stat-menu loop | Require the body to change tactical opportunities, require reflexes to affect committed resolution, and reject packages whose main activity is repeated attack selection |
| Space dominates cards and bodies | Prohibit universal reposition; range changes only through meaningful action/defense/reflex outcomes and settles when unmaintained |
| Card presentation is cosmetic | A changed or unusable body must alter available or legal tactical options, not only displayed damage numbers |
| Defense dominates offense | Prepared defense consumes Main tempo; unprepared response is weaker/riskier |
| Motor skill blocks the game | Timing profiles must support configurable tolerance and non-single-channel telegraphs |
| System explodes into exceptions | One reflex-event contract; add response modules only after Block passes |
| More questions replace fewer | Treat section 6 as resolved; escalate only a P0 contradiction found by H1 |

## 10. New-conversation starting instruction

Use this document for macro direction and
`20_H1_HYBRID_COMBAT_SPEC_v0_1.md` for the research contract, then read
`21_H1_IMPLEMENTATION_RECORD_v0_1.md` for the current evidence. The four owner
questions in section 6 are resolved and the bounded fidelity implementation is
complete. Use `23_REFLEX_INTERACTION_TAXONOMY_AND_DIAGNOSTIC_REVISION_v0_1.md` for the
diagnostic correction, `24_CURRENT_DEVELOPMENT_LEAD_BRIEF_2026-08-12.md` for current
cross-discipline status, and `25_VISUAL_INTERACTION_LAB_RECORD_v0_1.md` for the
preserved lab result and deferred gate. Do not restart the archived question-by-question
interview, promote provisional values before human testing, or expand content or
presentation.

Suggested opening request:

> Read `docs/19_CORE_GAMEPLAY_DIRECTION_AND_HANDOFF_2026-08-01.md`,
> `docs/20_H1_HYBRID_COMBAT_SPEC_v0_1.md`,
> `docs/21_H1_IMPLEMENTATION_RECORD_v0_1.md`,
> `docs/23_REFLEX_INTERACTION_TAXONOMY_AND_DIAGNOSTIC_REVISION_v0_1.md`,
> `docs/24_CURRENT_DEVELOPMENT_LEAD_BRIEF_2026-08-12.md`,
> `docs/25_VISUAL_INTERACTION_LAB_RECORD_v0_1.md`, and the mandatory repository skill files.
> Treat the four owner decisions as resolved, the H1 values as configurable research
> variables, the bounded fidelity implementation as complete, and shared readiness as
> approved for lab research planning only. Review the evidence limits and proposed lab
> plan; do not reopen minor questions unless one creates a P0 contradiction.
