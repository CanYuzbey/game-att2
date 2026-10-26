# V3 Full-Fidelity Master — sequential chunk 11/12

Historical:
- full deck/card system;
- large item roster;
- full run map;
- procedural generation;
- final art;
- animation/cut-ins;
- faction/lore expansion;
- complex NPC dialogue;
- multiplayer;
- Steam achievements/store;
- save/load;
- build pipeline;
- advanced RPG leveling;
- 100-limb expansion.

Important V3 reversal:
full anatomical card/deck system is now active core direction.
Faction/NPC purpose is also active direction in bounded form.
Other exclusions broadly remain downstream.

## 6. V1 item audit

### Keep
Blood Bag
Clotting Cream
Bone Scissors
Hell Saw
Claim the Cut
Black Stitch.

### Blood Bag comparison variants
A: +25 / +15 if Bleeding.
B: +20 / +12 if Bleeding.
C: +25 but cannot exceed 60.

These are research-only history.

### Black Stitch V1 scope
Anna treatment mode:
cost0 as trade reward;
remove Unstable OR stop Bleeding.
No general inventory spell.

### Excluded historical items
Regrowth Vaccine;
Heal Rotten Flesh;
Wrong Recipient;
Sell the Pain;
Promise: Take This Later;
Emergency Tourniquet unless differentiation required.

## 7. V1 mechanic decision audit

Focus — spend Blood for exact info.
Grip Strike — target limb pressure.
Claim the Cut — pay now for later harvest.
Hell Saw — expensive risky sever.
Bone Scissors — setup + precise sever.
Blood Bag — heal now/save.
Clotting — stop bleeding/spend elsewhere.
Emergency graft — power vs risk.
Unstable — volatility management.
Anna trade — loot vs maintenance.
Table — integrate/repair/prepare/save.
Plead — bargain vs greed.
Clean gate — tool commitment vs ruined part.

Historical weak/untested:
Torso vulnerability mostly passive;
Weak Legs not tested until later Minotaur;
Table Loan interesting/untested;
Surge sometimes irrelevant (+2 Blood fallback added).

## 8. V1 resolved ambiguities

### Enemy Blood vs limb integrity
Separate.
Limb damage did not automatically reduce Blood in V1 simulator.

V3: still separate dimensions; exact injury→Blood coupling comes through wounds/effects, not generic limb-damage conversion.

### Disabled vs Severed vs Ruined
Disabled attached unusable.
Severed detached.
Ruined unsuitable for ordinary emergency graft.

Conceptual distinctions retained.

### Jeff free-arm destruction
Could cause incapacity surrender but did not upgrade ruined arms to Clean.

Legacy encounter rule only.

### Round timing
Old Focus + one Fast before Main.
Panic checked immediately on Blood threshold.
Enemy action canceled if source invalidated.

Only atomic/source-cancel lesson remains universal; cadence superseded.

### Item persistence
Blood Bag/Clotting/Claim consumable across old campaign;
Scissors/Saw refreshed per fight.
Legacy.

### Black Stitch
Anna-specific treatment, not general system.
Legacy.

## 9. V1 stop/revise/continue signals

Continue if:
Jeff baseline; no-spend blocked; Anna both routes; meaningful body change; Blood Bag not always optimal; dangerous not absurd collapse; table varies.

Revise if:
same action dominates; spending irrational; too rich/dead; Unstable ignored/hated; Anna always same; table option universal.

Do not proceed if:
logs confusing; body change irrelevant; Blood unstable; harvest/graft automatic; major combat rules still changing.

V3 preserves this style of falsifiable gate, not the old exact scenario dependencies.

---

# SOURCE DOCUMENT: legacy/04_V1_SCENARIO_TEST_AND_MODULE_CONTRACT_LEDGER.md

# V1 Scenario, Test, and Module Contract Ledger

**Status:** LEGACY ENGINEERING EVIDENCE

## Seven scenarios and original purpose

### S1 Jeff Baseline Acquisition
Mark right arm, damage, saw, acquire/bargain, graft.
Pass: clean right-arm possible, complete Blood log, Guard Flesh after graft, positive Blood, seed reproducible.

### S2 Jeff No-Spend Exploit
Spam free attacks.
Pass: may incapacity-surrender, but no Clean premium harvest without a valid paid/salvage route.

### S3 Failed Hell Saw Spiral
Forced saw failure/Rage/Bleeding.
Pass: failure explicit, critical state visible, Panic/soft-collapse order, no hidden rescue.

### S4 Anna Stabilization
Unstable + Focus/Guard/medical timing, accept treatment.
Pass: trade loot greed for stabilization, nonlethal resolution, Unstable removed/logged.

### S5 Anna Greed
Reject treatment/pursue graft arm.
Pass: Stabilized sever penalty visible, success/failure, risky extraction, no free arm.

### S6 Mini Campaign
S-001→Jeff→graft→Anna→table.
Pass: body change affects later options, final report body/Blood/items/decisions/vulnerability.

### S7 Blood Bag Variants
Config overlay comparisons without selecting winner automatically.

## V1 strategy drivers

Balanced
Blood Hoarder
Limb Greed
Survival First
Reckless Sever

They were deterministic diagnostics, not human behavior models.

## V1 module contracts

### BodySystem
Owned slots/limb references.
Did not own action/enemy/UI.

### LimbStateSystem
Owned integrity→state/tags.

### BloodSystem
Owned transactions, Panic, collapse.

### ActionResolver
Owned source/timing/action effect.

### HarvestSystem
Owned quality/salvage.

### GraftSystem
Owned slot replacement/stability/integration.

### IntentSystem
Owned enemy intent clarity/Focus upgrade.

### EnemyScriptSystem
Owned simple Jeff/Anna choices.

### TableSystem
Owned post-fight transformations.

### Logger/Metrics
Owned inspectability, not rules.

V3 retains the ownership-discipline principle but reorganizes modules around Body/Capability/Concept/Brain/Attention/Inventory/Will.

## V1 CLI contract

Historical:
--scenario
--all-scenarios
--seed
--strategy
--batch
--format text|json|markdown
--output
--verbose

V3 runtime need not expose the same CLI, but evidence tooling should preserve equivalent deterministic fixture selection and machine/human reports.

## V1 errors

ConfigValidationError
IllegalActionError
InvalidTargetError
InsufficientBloodError
InvalidStateTransitionError
ScenarioDefinitionError.

V3 can reuse equivalents.

## V1 performance

A few thousand runs practical; inspectability/correctness over optimization.

Directly retained philosophy for V3 diagnostic harness.

---

# SOURCE DOCUMENT: ops/PRODUCTION_OPERATING_SKILL_V3_FULL.md

# Game att2 — Skeptically Audited Production Operating Skill V3

## Prime directive

Protect the project from hallucinated facts, vague planning, scope creep, weak architecture,
AI-generated mess, untested mechanics, premature content/polish, hidden authority drift,
evidence overclaim, licensing mistakes and context loss.

## Owner authority

Owner decides:
identity, genre/loop, major combat/economy, progression, art/camera, engine, monetization/release, irreversible creative choices.

Agent/team may autonomously resolve:
reversible technical implementation details that cannot materially alter experience.

## Evidence labels

Confirmed fact
Assumption
Inference
Recommendation
Owner-approved decision
Working hypothesis
Open decision
Risk
Legacy evidence

## Work lane

Audit / rules change / implementation / research / human testing / content proposal / documentation / out-of-scope.

State lane before work.

## Gate template

Gate
What locks
Evidence
Continue
Revise
Kill/pivot
Flexible
Risks
Approval.

## Mechanic template

Purpose
Player decision
Skill expression
Risk/reward
State dynamic
Feedback
Failure mode
Prototype
Test
Evidence class.

## Module template

Purpose
Owns / does not own
Inputs
Outputs/events
Dependencies
Public API
Data
Errors
Debug
Tests
Integration.

## Requirement chain

Requirement → design → system → task → acceptance → test → result → status.

## AI quarantine

Inspect:
unrelated changes, authority, dependency, architecture, edge cases, tests, determinism, docs/config, secrets/licenses.

## Systemic hostile review

Reject:
script immortality;
resource theatre;
decorative body damage;
outcome teleportation;
invented anatomy;
Attention substitution;
Concept compensation;
Brain omnipotence;
encounter-specific fake emergence;
hidden rubber-banding.

## V3-specific hostile review

- Does Body still own capability?
- Did Brain/Attention fabricate option?
- Did class guarantee hide an impossible source?
- Is source weighting explainable?
- Did recency become hard cooldown accidentally?
- Can specialization exploit remove every downside?
- Did Readied Item create a third action rail?
- Did Brain Part duplicate Brain Architecture?
- Did Concept Deck become second Brain?
- Did persistent progression cover weak combat?
- Did transformation collapse to corruption meter?
- Did boss gain a bespoke graft lock?
- Is same-boss replay evidence contaminated?

## Human evidence

Consent/version/fixture/deviations/raw observations/contamination.
Designer self-play ≠ external evidence.

## Accessibility

Never treat difficult timing as product identity.
Support redundant cues, timing assists, remapping, latency practice, readable feedback.

## External dependencies

Official source/license/maintenance/integration/alternative.

## Completion

Return exact files, verification, evidence boundary, hostile findings, limitations, adoption verdict, one next gate.

## Current gate

V3-1 isolated combat sandbox.

---

# SOURCE DOCUMENT: ops/RETURN_CONTRACT_V3.md

# V3 Return Contract

Every AI/developer return must include:

1. Branch / commit / working-tree state if applicable.
2. Exact requested gate.
3. Files changed.
4. V3 authority references.
5. Behavior changed.
6. Tests and verification.
7. Deterministic seed/replay result where material.
8. Fact / inference / hypothesis / unknown.
9. Hostile-review findings.
10. Scope audit.
11. Known limitations.
12. Adoption verdict:
   - ADOPT
   - ADOPT WITH DEBT
   - REVISE
   - REJECT
   - ARCHIVE / EVIDENCE ONLY
13. One next gate.

Do not say "implemented" without an exact artifact and current verification.
Do not say "playable" without a runnable artifact.
Do not say "validated" without naming the evidence class.

---

# SOURCE DOCUMENT: research/RESEARCH_TEMPLATE_V3.md

# V3 Research Artifact Template

Question:
Hypothesis:
Why this matters:
Authority constraints:
Variables:
Fixed conditions:
Protocol/model:
Instrumentation:
Evidence class:
Contamination risks:
Pass/revise/kill criteria:
Raw outputs:
Result:
What this supports:
What this does NOT support:
Decision:
Next gate:

---

# SOURCE DOCUMENT: research/V3_1_DETERMINISTIC_ARCHITECTURE_EVIDENCE_v0_1.md

# V3-1 Deterministic Architecture Evidence v0.1

Status: AUTOMATED RESEARCH / FIDELITY EVIDENCE

## Implemented invariants

- exact source legality;
- Brain guaranteed/flexible duties;
- weighted exact-expression Attention;
- intrinsic expression weights;
- recency suppression;
- source-state weighting;
- Focus source-family bias;
- without-replacement within refresh;
- duty coverage report;
- shaded unfillable duty;
- no-alternative redraw protection;
- insufficient-Blood redraw rejection with zero mutation;
- exact committed-redraw Blood ledger event;
- persistent held-card lifecycle and explicit Decision Refresh;
- immediate source-invalidation without mid-exchange refill;
- full per-slot weight/rejection/RNG trace;
- Prep/Main and inventory-origin action limits;
- Yellow Block/Parry / Red Evade legality.

## Verification

`pytest`: **26 passed**

Python compile: passed.

A seed-42 balanced fixture produced deterministic structured Attention output.

Lint/type claim: **not made** in this execution environment because Ruff and mypy executables were unavailable.

## Evidence boundary

Supports:
determinism, causal legality, negative cases, architecture consistency.

Does not support:
fun, comprehension, fairness, accessibility, final balance, replay desire.

---

# SOURCE DOCUMENT: research/V3_1_TECHNICAL_HARDENING_REPORT_v0_2.md

# V3-1 Technical Hardening Report v0.2

Status date: 2026-09-04  
Evidence class: deterministic implementation/fidelity evidence

## Scope

Professional/reversible implementation work only. No owner-dependent creative choice was locked.

## Implemented

