# Game att2 — Decisions, Risks, and Open Questions v0.6

## 2026-08-01 owner decision: hybrid strategic/reflex core direction

Combat remains turn-based at the strategic layer and must also contain reflexive
execution moments; timing a block against an incoming strike is the first concrete
example. The reflex layer modifies an already-legal action through body source,
telegraph, reach, timing quality, and state consequence. It must not bypass the
state-derived resolution loop or make Blood, body condition, target choice, and
extraction planning decorative.

At round start the player may know visible limbs and broad limb data, the opponent's
Blood band rather than necessarily exact Blood, and a basic motivation clue. Observation
or dialogue may reveal more. Recovery skill should come from reading intent, sequencing
treatment and denial, changing the opponent's option space, and trading ideal reward
for survival when necessary.

The consolidated new-conversation handoff and reversible defaults are in
`19_CORE_GAMEPLAY_DIRECTION_AND_HANDOFF_2026-08-01.md`. The individual rows in
`18_OPEN_COMBAT_AND_MOBILITY_DECISIONS.md` are now subordinate dependencies rather than
separate owner-level interview questions. No hybrid runtime implementation is approved
by this documentation decision alone.

## 2026-08-01 owner decision: Blood death, sacrifice, defense boundaries, and negotiation

**Physical rules:** Blood 0 is death unless an explicit prevention resolves first.
Limb for Life is that approved tutorial-scope exception: once per run, sacrifice one
seeded-random usable non-Core limb and restore 12 Blood. Sacrifice may be a necessary
cost on a viable victory path but is not itself victory (`C04` resolved at the
framework level; route-specific predicates remain content work). Limb wounds may cause
immediate Blood loss, periodic loss, both, or no Blood loss; the wound mapping,
numbers, functional penalties, and exact Ruined Torso sequence remain open.

**Capability defeat:** Offensive incapacity occurs when an actor has no legal attack
remaining. The game should warn as the final offensive source is endangered and expose
surrender/negotiation before the dead end. Offensive incapacity informs mental defeat
acceptance; it does not automatically author one universal ending.

**Defense:** Cover It lasts one round, expires, and must be selected again on a later
round. Its effect and trade-off remain open. Brace is a manual one-round Main-action
stance; Braced Legs separately provide one automatic Knockdown-prevention charge per
encounter. The final balance among Cover It, Brace, Braced Legs, and Guard Flesh is not
approved.

**Negotiation and mental defeat:** Defeat acceptance is a background mental state
derived from objective viability, recovery hope, desperation, honor, and character
traits. It may lead to negotiation, surrender, resistance, escape, or awaiting mercy.
Either side may open negotiation. The intended design is a bounded multi-exchange
minigame of demands, offered assets, evaluation, counter-offer, acceptance, or exit.
Failure returns to the unchanged combat state; rejection grants no numerical buff or
debuff. A voluntary player surrender may be accepted, priced, converted into another
outcome, or refused according to the opponent's motivation and character.

**Implementation boundary:** Rules v0.5 implements Blood death/Limb for Life semantics,
the Brace/Braced Legs naming distinction, Cover It's one-round data contract, and
no-modifier bargain rejection. Wounds, active Cover It behavior, generalized mental
defeat, and multi-round negotiation remain blocked by the consolidated decision queue
in `18_OPEN_COMBAT_AND_MOBILITY_DECISIONS.md`.

## 2026-07-31 owner decision: general combat motivation and victory framework

**Decision:** Motivation is a general input to encounter behavior, not a Jeff-only
script. Combat remains the game's main mechanic, but an encounter's purpose need not
be killing or defeating the opponent. Player and opponent may both satisfy their
objectives. Capability defeat may lead to bargaining, surrender, mercy, exploitation,
or another state-legal response according to motivation. Victory routes must emerge
from ordinary Blood, body, inventory, capability, and pressure state rather than feel
like detached bonus objectives.

**Prototype implementation:** The runtime now separates motivation, objective route,
resolution, and per-actor outcome. The generic prototype motivation classes are
Restoration, Survival, Control, and Elimination; generic victory routes include Blood
collapse, capability break, surrender, objective completion, and a state-backed
boss-specific extension point. These categories are reversible pending human evidence.

**Jeff survey hypothesis:** Jeff seeks the player's Clotting Cream to repair his Open
Wound Torso while the player seeks his Right Arm. Marking the usable Right Arm while
the cream remains in inventory can produce a bargain. Accepting exchanges those two
existing assets and can make both actors successful; a hostile Main action rejects the
offer and triggers configured escalation. Desperate Swing chooses legal targets from
state and penalizes exact repetition.

**Evidence boundary:** This is an instrumented survey hypothesis, not final Jeff canon
or evidence that players understand the system. The full definitions, hypotheses, and
deferred decisions are in `docs/17_COMBAT_MOTIVATION_AND_VICTORY_FRAMEWORK_v0_1.md`.
`Cover It` effect/trade-off, wound mappings, Ruined player-Torso consequences, and
final surrender psychology remain owner decisions.

## 2026-07-23 owner decision: simulator causal-integrity correction

**Decision:** Exactly one successfully committed Main action is permitted per actor per round. Main-action commitment and round-boundary cleanup belong to rules-owned logic. Focus and one Fast item remain pre-Main actions and do not consume Main. Stand consumes Main. Unused Guard Flesh expires at end of round and emits a structured event.

**Implementation:** `RuleEngine` validates action-specific prerequisites before one centralized Main-action commit. A rejected pre-commit action does not consume Main or mutate gameplay state. Grip Strike, Claim the Cut, Bone Scissors, Hell Saw, Guard Flesh, Stand, and Brace use the same commitment path. The Jeff no-spend scenario now advances one round between each successful Grip Strike.

**Evidence:** 81 automated tests pass, including focused commitment, rejection atomicity, Focus/Fast coexistence, Guard lifecycle, source invalidation, and actor-round uniqueness tests. Seed-42 mini-campaign remains 25 Blood; its event count changes from 32 to 39 because six Main commitments and one Guard-consumption event are now explicit.

**Boundary:** No balance value, content definition, Encounter 3 runtime material, Unity
work, or production system was added. Historical results remain preserved under
`archive/results/` and v0.1 is superseded by
`archive/results/Game_att2_Combat_Simulator_Results_v0_2.md`.

## 2026-07-18 owner decision: Encounter 3 bounded causal paper requirements

**Decision:** Encounter 3 is not pure endurance. For paper testing only, it uses fixed fixture `E3-PRETABLE-01`, four table choices (Loan excluded), Warden right-arm/legs/torso target zones, source-derived actions, state-aware Momentum/Butcher policies, bounded combat incapacity, and an eight-round unresolved cap.

**Evidence gate:** Eight real free-choice moderated sessions P01–P08. `SELF-S01`/`SELF-S02` remain contaminated designer diagnostics and do not count.

**Boundary:** No Warden Blood, reward/graft value, horns, organs, penetration, death, surrender, bargaining, escape, personality, generalized AI, runtime configuration/source, simulator scenario, or Unity is approved.

**Reconciliation:** `AGENTS.md` permits owner-approved paper research while retaining the runtime prohibition. Earlier fixed-sequence Minotaur v0.1 materials are historical and superseded for future moderated sessions.

## 2026-07-18 owner decision: state-derived outcomes

**Decision:** Actions change supported runtime state; updated state determines current capabilities, affordances, forced consequences, and legal/rational responses. Actions do not directly select authored endings.

**Boundary:** This approves a design-governance method, not Warden costs, anatomy, organ effects, surrender thresholds, personality, escape rules, or a universal simulator. Unsupported categories remain deferred or require a focused owner decision.

**Implementation status:** Skill governance is upgraded. Designer self-play remains stopped after `SELF-S02`, both sessions remain contaminated diagnostics, and the Encounter 3 paper/runtime gap remains open. Encounter 3 runtime implementation and Unity remain blocked.

## Sprint 0.6 decision record: historical 37 versus deterministic 25

**Decision:** Preserve 37 Blood as historical paper evidence; use deterministic 25 Blood only as the current seed-42 simulator output, not as a balance target.

**Evidence:** The paper record includes a spare-arm sale with no authoritative configured price or rule path. The source-compliant simulator logs 85 start, -10 Claim, -18 Hell Saw, -12 emergency graft, +2 Surge fallback, -3 Focus, -4 Guard Flesh, and -15 integration, ending at 25.

**Reason:** Forcing either record to match would silently add or alter a gameplay transaction.

**What remains flexible:** A future owner-approved bargain/sale rule, its value, and the intended balance target.

**Revisit condition:** Owner provides a source-backed sale/bargain definition or playtest distributions justify a balance revision. Until then, automated tests use current deterministic behavior and neither isolated number determines balance.

Sprint 0.6 is a non-canonical table-consequence probe only. Simulator product evidence remains insufficient for Unity; Unity stays blocked.

## Sprint 0.6.1 decision record: Knockdown and Brace

**Decision:** Can approved Option A, Tempo Loss.

**Owner:** Can Yuzbey.

**Reason:** Strengthen Legs required a minimal, legible downstream consequence without adding movement or a broad status system.

**Rule:** Unresolved Knockdown applies Downed; the next normal action must Stand. Fast medical remains legal before Stand. Braced legs automatically cancel one successful Knockdown per encounter and refresh only at encounter start.

**What remains flexible:** Knockdown prevalence, future limb charge counts, visual presentation, animation, audio feedback, and enemy identity.

**Revisit condition:** Rerun validation shows repeated tempo-lock, no meaningful leg value, or a future encounter requires a different bounded consequence.

## Sprint 0.7 decision record: Minotaur Warden paper encounter

**Status:** Superseded for future moderated testing by the 2026-07-18 bounded causal paper requirements. Preserve the earlier Charge/Cleave/Horn Hook model only as historical walkthrough context; do not use it for P01–P08.

**Decision:** Can approved Minotaur Warden for canonical paper design/testing only.

**Rule:** Charge tests Knockdown/Brace, Cleave tests torso/Bleeding, and Horn Hook tests right-arm/Guard pressure using existing rules only.

**Revisit condition:** Human paper evidence shows unreadable telegraphs, universal table choice, or a need for prohibited mechanics.

## Locked identity/product decisions

- single-player PC target;
- mostly silent self-insert;
- hell-loop limb-grafting duel roguelike/roguelite;
- dark/disturbing tone with satirical relief;
- Buckshot Roulette is atmosphere influence, not copied mechanics;
- limbs are the main build engine;
- blood is health/currency/fuel for prototype;
- six slots for first demo;
- table decision view + side/body action presentation later;
- emergency grafting and safer table grafting;
- missing-limb builds are rare/special;
- small demo first.

## Approved for simulator, still reversible

- acting-limb impairment;
- clean-sever gating;
- Harvest Quality;
- Focus pre-action;
- Fast medical timing;
- Plead Pressure;
- Unstable v0.4;
- tutorial-scope Limb for Life death-prevention sacrifice;
- Jeff first and Anna second;
- Grafting Table v0.2;
- scripted deterministic sequence.

## Open product decisions — Codex must not decide

- final title;
- final engine;
- final art style;
- complete run/map structure;
- meta progression;
- long-term enemy/limb roster;
- dialogue system;
- store/release strategy;
- final debt economy;
- final save/load format;
- final Limb for Life selection/control rules beyond the approved seeded prototype.

## Implementation questions Codex may resolve reversibly

- exact internal class/module names;
- YAML loader versus documented migration to another checked-in data format;
- integer rounding rule, if tested and documented;
- CLI library (standard argparse preferred);
- report formatting details;
- test-fixture organization.

## Active risks

| Risk | Probability | Impact | Simulator warning sign | Control |
|---|---:|---:|---|---|
| Blood hoarding | Medium | Very high | premium body without meaningful spend | no-free-clean-sever scenarios |
| Blood Bag dominance | High | Medium | immediate use nearly universal | variant/config report |
| Death spiral | Medium | Very high | one failed roll makes later actions irrelevant | Panic, Fast items, soft-loss metrics |
| Limb system becomes stats | Medium | Very high | body changes do not change legal actions | final body/action summary |
| Table has one answer | High | Medium | integrate selected almost universally | strategy/batch table rates |
| Unstable hated/ignored | Medium | High | always stabilize or never graft | path and collapse metrics |
| Anna path one-sided | Medium | Medium | offer always accepted/rejected | two integration scenarios |
| Simulator overbuild | Medium | High | frameworks/content unrelated to tests | AGENTS scope gate |
| Rule/config drift | Medium | High | prose and code values diverge | config validation and report versioning |
| Premature Unity | High | Very high | engine work before results review | explicit blocked gate |
| Facilitator preserves policy over state | Medium | Very high | unusable source still acts | mandatory intent revalidation and cancellation log |
| Paper target zones become implied anatomy | Medium | High | moderator invents horns/organs/weak points | mechanical-zone boundary and contamination rule |
| Round cap mistaken for victory | Medium | Medium | cap reported as player success | exact `UNRESOLVED — ROUND CAP` classification |

## Revisit triggers

- Simulator results show a dominant exploit.
- A rule requires repeated special-case code.
- The same mechanic produces contradictory desired outcomes.
- Test logs cannot explain why a run failed.
- External/blind player behavior conflicts with internal simulations.
- Unity architecture would be constrained by a simulator-only convenience.
