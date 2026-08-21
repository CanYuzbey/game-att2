# Game att2 - Source-First Modular Integrity Owner Review v0.1

Status date: 2026-08-16

Status: **Package D - Source-First Modular Integrity System is owner-approved as
paper design authority. Runtime, configuration, production effect content, individual
card profiles, exact Integrity Echo thresholds, and final numeric balance remain
unapproved.**

## 1. Decision and authority boundary

Package D replaces the earlier recommended Package A as the complete answer to the
body-state capability-mapping gate. It retains source-owned local capability, permits
bounded card-specific deterioration through shared axes, centralizes reusable effect
families, and adds one capped whole-body consequence called Integrity Echo.

The governing statement is:

> An action is primarily governed by the body source that performs it. Local
> structural damage creates the main capability consequence. Shared effect packages
> provide reusable poison, burn, protection, cleansing, and similar interactions.
> Significant loss of the actor's own coherent body state may create a small,
> bounded, visible Integrity Echo across other actions, but that echo never replaces
> source legality or becomes a dominant universal stat penalty.

This document openly amends the earlier normal separation in which structural state
owned capability and wounds owned Blood/treatment pressure. That separation remains
the default. Integrity Echo is the sole approved derived whole-body micro-layer and
is subject to the hard restrictions below.

This approval does not change the current simulator's `100% / 75% / 50%` impairment
behavior, configuration, tests, content, scenarios, Guard Flesh behavior, reflex
implementation, Encounter 3 runtime boundary, or engine scope.

## 2. Three-layer architecture

```text
Layer 1 - source-owned local capability profiles
Layer 2 - centralized modular effect packages
Layer 3 - bounded derived Integrity Echo
```

Resolution always gives Layer 1 priority. Layer 2 may deliver only through a legal
source/action gate. Layer 3 may alter one micro-axis only after the local profile is
known and may never change legality.

## 3. Layer 1 - source-owned local capability

### 3.1 Structural capability ladder

| Source state | Capability result |
|---|---|
| Intact | Full authored profile |
| Damaged | Strained profile; action remains legal and one visible local axis worsens |
| Critical | Desperate profile only when explicitly defined; otherwise Dormant |
| Disabled, Ruined, Severed, Missing, or otherwise unusable | Offline; dependent opportunities become Invalid |
| Occupied or Reserved | Temporarily unavailable; affected opportunities become Dormant |

The paper architecture supersedes universal numeric scaling as the future design
direction. It does not migrate the current runtime baseline without a separately
approved implementation plan.

### 3.2 Local profile contract

Every voluntary action, preparation, item use, tool use, and automatic reflex route
declares its required physical sources. A local profile may deteriorate through this
bounded shared list:

- effect strength;
- an approved cost;
- exposure or self-risk;
- information clarity;
- range consequence; or
- defense or mitigation quality.

Each action may define Full, Strained, and optionally Desperate profiles. Shared
templates and axes own the meanings. A card may select among them but may not create a
private impairment subsystem.

A Desperate profile preserves agency at a physically credible cost. It may not
secretly outperform Full without a visible additional payment, exposure, source risk,
or signature-action reason. An authored signature override is rare, visible, and
still subject to source legality, timing, commitments, costs, effect delivery,
consequences, and logging.

### 3.3 Source locality

- Damage primarily changes opportunities owned by the damaged source.
- An impaired Right Arm does not weaken a valid Left-Arm action merely because both
  belong to the same actor.
- Missing anatomy present in the actor's coherent starting build creates no global
  comparison penalty.
- An action with several required sources uses the weakest required source profile.
- Optional support improves an action only when its definition says how.
- A source cannot be substituted after intention lock.
- Revalidation after intention lock derives the same action's current profile from
  the current source state. A newly Damaged source uses Strained; a newly Critical
  source uses its Desperate profile or cancels if none exists; an Offline source
  cancels. No replacement action or source is selected.
- A changed execution-time cost is revalidated before payment. Previously paid
  on-lock costs remain governed by document 32.
- Once an atomic action legally begins, it completes before new source state changes
  future capability.
- Player and enemy use the same contract except for visible authored exceptions.

### 3.4 Slot-role safeguards

- **Head:** may source Focus, observation, intent-reading, and authored Head actions.
  Head condition does not change Attention Slot capacity or remove general choice.
- **Arms:** independently source declared attacks, guards, tools, items, treatment,
  extraction, and other arm actions. Multi-arm actions name every required arm.
- **Legs:** may source or support Brace, Stand, Dodge/Evade, posture, and authored
  Legs-heavy or range-producing actions. Legs do not automatically change Lead.
- **Torso:** affects actions only when declared as a required/supporting source or
  when the approved Ruined-Torso deadline applies. It creates no second generic health
  penalty.
- **Core:** sources only authored Core actions/passives such as Panic Pulse. Package D
  creates no new automatic Core-death rule beside the existing Blood/death contract.

If unusable Legs prevent Stand, other actions remain available only when their own
posture and source contracts explicitly permit grounded use. If none remain, normal
capability-defeat evaluation applies; the system does not invent a recovery action.

### 3.5 Wounds, treatment, and repair

Structural state remains the main local capability fact. Wound family remains the
owner of Blood pressure, treatment urgency, reopening/escalation, and Major Trauma.

- ordinary use of a wounded but usable source remains legal;
- `WOUND_STRESS` applies only when visibly authored;
- Control or Stabilization does not restore structural capability;
- structural repair may improve a local profile and may reduce derived Integrity
  Echo when it restores coherence;
- wound treatment alone does not reduce Integrity Echo;
- an effect package may invoke a wound, treatment, repair, or Blood operation only by
  calling that existing contract explicitly.

## 4. Layer 2 - centralized modular effect packages

### 4.1 Effect Package Contract

Every approved effect family is defined once in a bounded registry. Its definition
contains at least:

```text
effect_id
public_name
delivery_or_trigger_gate
allowed_resolution_stage
potency_semantics
duration_or_expiry
stack_refresh_escalate_replace_rule
maximum_intensity_or_cap
valid_target_requirements
resistance_or_protection_rule
cleanse_control_or_removal_rule
periodic_timing_if_any
state_mutations_and_capability_consequences
preview_and_event_log_requirements
deterministic_or_injected_randomness_boundary
structural_wound_Blood_defense_redirection_death_interactions
```

The registry is closed by default. A new effect family requires an explicit later
design/content decision. `POISON` and `BURN` are architecture fixtures only; they do
not approve production cards, sources, items, spells, characters, or encounters.

### 4.2 Sparse interaction declarations

Sources and actions reference the registry through sparse declarations:

```yaml
effects:
  apply:
    POISON: 2
  resist:
    BURN: 1
  cleanse: {}
```

- a missing entry means no interaction or potency `0`;
- a positive value declares that interaction and potency;
- `apply`, `resist`, and `cleanse` remain separate verbs;
- rare `immune` is explicit, visible, and authored;
- a source/card never redefines duration, stacking, caps, or standard counters;
- the package owns how declared potency becomes state.

Protection/resistance acts when an incoming effect resolves. Cleansing changes an
effect already present under the package's removal rule. These are never synonyms.

### 4.3 Source-owned payload and delivery

An effect intrinsic to a limb, graft, tool, or item normally lives on that source.
The card declares whether it delivers compatible source payloads.

```text
Venomous Right Arm - illustrative source
  POISON payload: 2
  POISON resistance: 1

Needle Jab - illustrative action
  required source: Right Arm
  delivers compatible source payloads: yes

Guard Flesh
  required source: Right Arm
  delivers offensive source payloads: no
```

The values and names above are non-canonical fixtures. The architectural rule is that
one source payload is not copied into every card definition. A meaningful card-level
override must be visible, previewed, and testable.

### 4.4 Delivery and actual recipient

```text
validate action and source
-> resolve preparation and compatible automatic reflex defense
-> determine whether the effect's delivery gate occurred
-> determine actual final recipient after avoidance, Block, Intercept, Cover It,
   or another approved redirection
-> read incoming potency
-> apply actual recipient's valid protection/resistance
-> send remaining potency to the central effect resolver
-> apply package stacking/duration/state rules at the declared stage
-> recompute capabilities and forced consequences
-> log the chain
```

A contact-delivered effect does not apply when contact was completely avoided. A
non-contact family must define that difference centrally. A redirected effect belongs
to the actual recipient unless its package explicitly and visibly defines another
rule. Original-target ownership is never hidden.

An effect may not duplicate structural damage, wounds, treatment, repair, Blood,
grafting, or death. When it changes one of those channels, its central definition
invokes the existing operation at an explicit causal stage.

## 5. Layer 3 - Integrity Echo

### 5.1 Meaning and non-goals

Integrity Echo represents a small derived disruption when the actor's current body
departs from its own coherent encounter baseline. It may fictionally communicate
acute pain, coordination loss, or awareness of bodily breakdown, but it is not a
psychology, morale, shock, trauma, or pain simulation.

Integrity Echo has three visible bands:

- **Coherent**;
- **Shaken**;
- **Fractured**.

The exact state-transition weights and modifier values remain tunable. Structural
state transitions, not each integrity point, are the preferred inputs. Fractured is a
hard maximum; pressure cannot accumulate beyond it.

### 5.2 Coherent-body baseline

The baseline is the actor's own stabilized structural build at encounter start. It
records the slot identities/presence and structural states that actor actually begins
with; it is not an ideal human anatomy.

Therefore:

- an actor who begins with one arm may be Coherent;
- a strange but stabilized graft build may be Coherent;
- beginning Damaged or Critical affects local profiles but does not itself create
  Echo;
- later in-encounter structural deterioration may create Shaken or Fractured;
- structural repair toward the recorded baseline may reduce Echo;
- improvement beyond the baseline cannot create a bonus stronger than Coherent;
- wound treatment without structural repair does not change Echo.

The encounter-start snapshot is the approved default comparison boundary. A future
in-encounter graft or explicit recalibration action is `DEFERRED`; no active-encounter
action silently rewrites the baseline. Existing between-encounter graft/table flow is
eligible to establish the next encounter's baseline through its normal authority.

### 5.3 Sensitivity and collision-only fallback

Each voluntary action or automatic response declares exactly one primary sensitivity:

- `EFFECT`;
- `EXPOSURE`;
- `DEFENSE`;
- `INFORMATION`; or
- rare, explicitly justified `NONE`.

An action may additionally name one **collision-only fallback axis** from the same
allowed set. It must differ from the primary axis. This does not create a second
modifier: it is considered only when the primary Echo axis is already the axis
worsened by the local source profile.

Resolution:

1. derive the local source profile and its degradation axis;
2. if Coherent or sensitivity is justified `NONE`, apply no Echo modifier;
3. if the primary Echo axis differs from the local degradation axis, apply the one
   central modifier there;
4. if they collide and a valid fallback exists and does not also match the current
   local degradation axis, apply the one modifier to the fallback;
5. otherwise suppress Echo for that action and show the collision reason.

At most one Echo micro-modifier can apply to an action. It may never stack onto the
same axis as local degradation.

### 5.4 Hard restrictions

Integrity Echo may slightly alter effect quality, exposure, final defense/mitigation,
or information clarity through the central band table.

It may not:

- make a Ready card Dormant or Invalid;
- restore, invalidate, or substitute a physical source;
- remove an otherwise legal automatic reflex-defense route;
- change Attention Slot capacity;
- grant or remove Preparation or Main opportunities;
- automatically seize, retain, or lose Lead;
- create hidden initiative or Speed;
- directly create a wound, Blood transaction, death, surrender, capability defeat,
  success, failure, victory, or defeat;
- become stronger than the local source consequence;
- use hidden or card-specific formulas.

## 6. Shared action/card definition

```text
Action/Card
- required_sources
- supporting_sources
- timing
- target_requirements
- range_profiles
- Full profile
- Strained profile
- optional Desperate profile
- local_degradation_axis
- deliver_compatible_source_payloads
- direct effect apply/resist/cleanse declarations
- integrity_echo_primary_sensitivity
- optional integrity_echo_collision_fallback
- physical commitments and occupied sources
- costs and previewed self-risk
- optional visible authored override
```

Empty fields are not shown to the player. The current preview must answer:

- what source or item enables the action;
- what changed because that source is impaired;
- what effect is applied/resisted/cleansed and at what shown potency;
- whether Integrity Echo changes this action and on which axis;
- why the action is Ready, Dormant, Invalid, or Desperate; and
- what is committed, exposed, spent, or risked.

## 7. Complete causal order

```text
read prior body, wound, effect, item, range, posture, and commitment state
-> validate actor, action, sources, target, timing, range, and costs
-> derive source-owned Full, Strained, Desperate, Dormant, or Invalid result
-> apply at most one legal Integrity Echo micro-modifier
-> lock or execute under the public-Lead and cancellation contract
-> activate approved preparation and resolve legal automatic reflex defense
-> determine actual recipient and final primary consequence
-> evaluate effect delivery at the package's declared stage
-> apply resistance/protection and centralized effect rules
-> invoke structural, wound, Blood, range, or other shared mutations explicitly
-> recompute source capabilities, card states, effect state, and Integrity Echo
-> evaluate Blood 0, Limb for Life, Torso deadline, incapacity, surrender, and
   encounter viability where already approved
-> emit structured deterministic evidence
```

A renderer, card script, enemy script, or effect package may display or select from
this state. It may not invent a missing state, waive a gate, or choose an ending.

## 8. Paper acceptance cases

All names and numeric values in effect examples are illustrative fixtures.

| ID | Paper case | Required result |
|---|---|---|
| D-PC-01 | One-source arm action at Intact, Damaged, Critical, and Ruined | Full, Strained, explicit Desperate-or-Dormant, then Invalid |
| D-PC-02 | Multi-source action with Full and Strained required sources | Weakest required source selects Strained |
| D-PC-03 | Critical source with authored Desperate profile | Desperate remains legal with visible tradeoff |
| D-PC-04 | Critical source without Desperate profile | Card becomes Dormant, not Invalid |
| D-PC-05 | Reply source degrades or becomes unusable after lock | Same action re-derives Strained/Desperate or cancels under document 32; no substitution |
| D-PC-06 | Illustrative Venomous Right Arm supplies `POISON 2` to compatible Needle Jab | Card inherits source payload once |
| D-PC-07 | Another action from that arm does not deliver offensive payloads | No Poison delivery |
| D-PC-08 | Actual recipient has illustrative `POISON` resistance `1` | Remaining illustrative potency is `1` under the fixture package |
| D-PC-09 | Contact attack is completely avoided | Contact-delivered Poison does not apply |
| D-PC-10 | Cover It/Intercept redirects attack | Primary and effect recipient become covering source |
| D-PC-11 | Illustrative Burn protection uses sparse interface | Central Burn package resolves protection; card contains no duplicate Burn rules |
| D-PC-12 | Actor begins encounter with one coherent arm | Coherent; no global missing-arm penalty; local missing-source actions remain absent |
| D-PC-13 | New in-encounter structural loss crosses illustrative Echo threshold | Derived band becomes Shaken or Fractured according to test mapping |
| D-PC-14 | Unrelated intact limb acts while actor has Echo | Local profile remains Full; at most one Echo micro-axis changes |
| D-PC-15 | Local profile and Echo primary sensitivity share one axis | Use one collision fallback or suppress Echo; never double-stack |
| D-PC-16 | Structural repair restores toward encounter baseline | Local profile improves and derived Echo may reduce; wound remains unchanged |
| D-PC-17 | Wound treatment controls Blood pressure without structural repair | Local profile and Integrity Echo remain unchanged |
| D-PC-18 | Same state is resolved for player and enemy | Identical contract and evidence except visible authored exception |

## 9. Requirements and traceability

| ID | Requirement | Paper cases | Future implementation obligation |
|---|---|---|---|
| SMI-D-001 | Every opportunity declares required physical sources. | 01, 02 | Reject missing/invalid source definitions. |
| SMI-D-002 | Local state derives Full, Strained, Desperate, Dormant, or Invalid. | 01, 03, 04 | Deterministic profile tests for each state. |
| SMI-D-003 | Weakest required source governs a multi-source action. | 02 | Test order independence and no averaging. |
| SMI-D-004 | Critical without Desperate is Dormant; offline is Invalid. | 03, 04 | Distinguish temporary and permanent hand states. |
| SMI-D-005 | Post-lock source change re-derives the same action profile and follows document 32 when canceled. | 05 | Test Strained/Desperate transition, cancellation, costs, and no substitution. |
| SMI-D-006 | Effect interactions use sparse apply/resist/cleanse/immune declarations. | 06-11 | Schema and missing-entry validation. |
| SMI-D-007 | Compatible cards inherit source payload without duplication. | 06, 07 | One payload event and explicit delivery flag. |
| SMI-D-008 | Effect delivery requires the central delivery gate. | 09 | Avoided contact produces no contact effect. |
| SMI-D-009 | Effects belong to the actual final recipient. | 10 | Redirected target and evidence tests. |
| SMI-D-010 | Resistance/protection and cleansing remain separate. | 08, 11 | Test pre-application protection versus later removal. |
| SMI-D-011 | Central package owns stacking, duration, caps, and expiry. | 08, 11 | Cards cannot override package semantics silently. |
| SMI-D-012 | Coherence compares against actor's own encounter-start build. | 12, 13 | Snapshot and unusual-build tests. |
| SMI-D-013 | Echo has Coherent/Shaken/Fractured bands and a hard cap. | 13, 14 | Boundary/cap tests using approved future values. |
| SMI-D-014 | Exactly one active Echo sensitivity axis is allowed. | 14, 15 | Reject multiple active modifiers. |
| SMI-D-015 | Echo never changes legality, slots, plays, Lead, or reflex-route existence. | 04, 05, 14 | Negative tests for every prohibited channel. |
| SMI-D-016 | Local and Echo effects never punish the same axis twice. | 15 | Collision fallback/suppression evidence. |
| SMI-D-017 | Structural repair and wound treatment keep separate effects. | 16, 17 | Assert profile/Echo/wound results independently. |
| SMI-D-018 | Player and enemy use the same contract. | 18 | Symmetric fixture comparison. |
| SMI-D-019 | Every derivation and effect stage emits deterministic evidence. | 01-18 | Seeded replay and structured causal events. |
| SMI-D-020 | Preview exposes only relevant source, profile, effect, Echo, and risk facts. | 01, 06, 14, 15 | Readability contract and disabled reason tests. |

## 10. Evidence card

| Field | Record |
|---|---|
| Question | Can local body damage, reusable effects, and a small whole-body echo create physical consequence without returning to universal stat penalties? |
| Mechanic package | Package D: source profiles, central effect registry, coherent-baseline Integrity Echo, one-axis/no-double-punishment safeguards. |
| Expected dynamic | Local injury reshapes source-owned choices; effects combine consistently; acute body loss adds one capped cross-action pressure without changing legality. |
| Desired experience | The player feels the body breaking and adapting while still understanding exactly which source, effect, and derived pressure changed each option. |
| Instrumentation | Baseline snapshot, source states, chosen profile, local axis, effect payload/delivery/recipient/resistance/result, Echo band/sensitivity/collision, card state, and final mutations. |
| Continue criteria | Source consequences dominate; effect rules remain reusable; unusual builds are coherent; Echo is visible but secondary. |
| Revise criteria | Most cards need overrides, Echo is routinely suppressed or dominates choices, or effect timing cannot be explained compactly. |
| Kill criteria | Package requires global legality loss, hidden formulas, duplicate wound/Blood systems, uncapped stacking, or per-card effect engines. |
| Evidence class | Owner-approved paper architecture; no runtime or human-experience evidence. |
| Decision owner | Can Yuzbey. |

## 11. Hostile review

| Risk | Severity | Required safeguard |
|---|---|---|
| Flat stat-menu play returns under new labels | High | Local profiles alter bounded meaningful axes; no global percentage sheet. |
| Every card becomes bespoke | High | Shared profile templates/axes; rare override is visible and review-gated. |
| Effect catalogue explodes | High | Closed bounded registry; each new family requires explicit approval. |
| Poison/Burn logic is duplicated | High | Central package owns all standard behavior; sparse declarations only. |
| Effect timing is hidden | High | Delivery gate and stage are central, previewed, and logged. |
| Effects duplicate wounds or Blood | High | Effect must explicitly invoke the existing shared operation. |
| Redirection applies effect to wrong target | High | Actual final recipient owns delivery after defense/redirection. |
| Local damage and Echo double-punish | Critical | One active Echo axis; collision fallback or suppression; never same-axis stacking. |
| Echo creates a global death spiral | Critical | Three bands, hard cap, micro-values, no legality/tempo effects, weaker than local consequence. |
| Unusual builds are permanently penalized | Critical | Actor-relative encounter-start coherent baseline. |
| Head becomes master attribute | High | Head cannot change Attention Slots or general choice. |
| Torso/Core create second health/death system | Critical | Existing Blood/Torso authority remains exclusive; no generic Package D death rule. |
| Echo removes automatic defense | Critical | Route existence remains source/action-derived; Echo may only micro-modify final defense quality. |
| Echo changes Lead or plays | Critical | Explicit prohibition and future negative tests. |
| AI bypasses physical rules | High | Player/enemy symmetry and visible exceptions only. |
| Hidden randomness enters profiles/effects | High | Deterministic definitions or injected/logged randomness only. |
| Card preview becomes unreadable | High | Show current/relevant fields only; central definitions available on inspection. |
| Examples become content | High | POISON, BURN, Venomous Arm, Needle Jab, and all values remain marked illustrative. |

No P0 or P1 contradiction remains after formalizing the collision-only fallback and
encounter-start baseline. The principal production risk is combinatorial presentation:
source profile, effect delivery, and Echo must be calculated centrally and reduced to
one current preview rather than printed as three parallel rulebooks.

## 12. Approval record and explicit deferrals

On 2026-08-16 the owner approved Package D and authorized optimization,
formalization, reconciliation, and documentation.

Approved paper direction:

- source-first local profiles and weakest-required-source handling;
- bounded Full/Strained/Desperate differentiation through shared axes;
- centralized effect packages and sparse interaction declarations;
- source-owned payloads and actual-recipient delivery;
- actor-relative Coherent/Shaken/Fractured Integrity Echo;
- one active Echo axis with no double punishment;
- deterministic evidence and player/enemy symmetry.

Deferred:

- runtime, configuration, and tests;
- exact local profile values and individual production card profiles;
- exact Echo thresholds, weights, and micro-values;
- any in-encounter baseline recalibration or graft shortcut;
- a production effect catalogue and final Poison/Burn behavior;
- new limbs, items, cards, spells, characters, and encounters;
- final UI, accessibility implementation, balance, Unity, and production claims.

## 13. Recommended next decision

Resolve remaining card and item boundaries as one package: exact item timing classes,
Fast-item limits, item/source cards, retention/expiry, multi-source tools, signature
overrides, and the minimum complete paper card set needed to exercise documents 28
through 33 without opening runtime or production content.

## 14. Later Package A2 resolution (2026-08-16)

Document 34 resolves this decision with one deliberately selected Readied Inventory
opportunity in a flexible Attention Slot, one voluntary inventory-origin action per
round, Preparation/Main timing, inventory-owned lifecycle, weakest-source tools, and
governed signature overrides. It preserves Package D source profiles, effect delivery,
Integrity Echo restrictions, and automatic-defense boundaries. Runtime, content, and
exact values remain gated. At that decision point, the next dependency-safe design
gate was range-maintenance action grammar; the later Package C disposition below
records its resolution.

## 15. Later Package C resolution (2026-08-17)

Document 35 resolves range maintenance under Package D. Full, Strained, and explicit
Desperate profiles declare their own range classification; missing maintenance data
never inherits or infers a refresh. Dormant or Invalid sources cannot maintain, and
multi-source opportunities use their weakest required source. Integrity Echo cannot
create, remove, maintain, shift, or release range. Runtime and production profiles
remain deferred.

## 16. Later Package B reconciliation (2026-08-17)

Document 36 requires every procedure to declare and reserve its exact body, item,
tool, patient, donor, target, harvested-part, and destination sources. Full, Strained,
explicit Desperate, Dormant, Invalid, weakest-source, and no-substitution rules remain
binding through pre-execution revalidation. Treatment, repair, Blood restoration,
extraction, and graft effects invoke their separate owners rather than a generic
effect package. Runtime and production profiles remain deferred.

## 17. Later Package A catastrophic-survival reconciliation (2026-08-19)

Document 37 sacrifices one exact attached body source, then re-derives its local
profile and every dependent source. Full/Strained/explicit Desperate, Dormant,
Invalid, weakest-source, Attention Slot, Integrity Echo, and no-substitution rules
remain binding. A grafted or integrated arm has no immunity, and the sacrifice cause
cannot create an alternative usable source. Runtime and profiles remain unchanged.

## 18. Brain Module reconciliation (2026-08-21)

Document 38 preserves Package D source ownership while allowing one source to
contribute multiple distinct card instances. Full/Strained/explicit Desperate,
Dormant, Invalid, weakest-source, occupied-source, and no-substitution rules apply to
every instance independently and again before commitment. Selection weighting cannot
improve an Offline source or conceal a Strained/Desperate profile.

Integrity Echo still cannot alter Attention Slot capacity, card legality, Brain Part
configuration, redraw availability, or automatic-reflex existence. Brain Parts are a
separate explicit progression owner, not an Integrity Echo effect. Ordinary Head/body
damage cannot permanently destroy Brain Parts; any temporary Stun interaction remains
deferred. Runtime, profiles, Brain content, and values remain unchanged.
