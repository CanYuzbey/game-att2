# Game att2 — Decisions, Risks, and Open Questions v0.6

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
- tutorial soft-collapse/low-blood valve;
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
- whether soft collapse survives past prototype.

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
