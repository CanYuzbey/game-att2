# Game att2 — Consolidated Combat and Mobility Decision Queue

Status date: 2026-08-21

Purpose: detailed supporting register of unresolved product questions. Start future
core-gameplay work from `19_CORE_GAMEPLAY_DIRECTION_AND_HANDOFF_2026-08-01.md`; use this
file only to inspect subordinate dependencies. Do not walk every row as an independent
owner interview, and do not implement an item until its blocking macro decision is
approved.

Document 40 completed the earlier cross-system collision audit. Document 41 later
superseded weighted Brain card access and the no-active-deck result: active-deck
authorship is now doctrine, while exact acquisition/deck cadence and embodied-
instability inputs remain open. Inventory separation, instance semantics, and
document organization remain resolved on paper.

## P0 — Wounds, Blood, and physical viability

| ID | Decision required | Why it blocks runtime | Depends on |
|---|---|---|---|
| W-01 — RESOLVED 2026-08-13 | Closed Trauma, Open Wound, Major Wound, and Severed Stump. | Approved minimum wound facts. | — |
| W-02 — RESOLVED 2026-08-13 | Use the qualitative action/result mapping in document 27. | Numeric thresholds remain W-03. | W-01 |
| W-07 — RESOLVED 2026-08-13 | Second qualifying Major result Ruins arms/Legs at 0 Integrity; attached, unusable, non-Clean, not Severed. | Preserves existing state meanings and extraction gate. | W-01, W-02 |
| W-08 — RESOLVED 2026-08-13 | Shared Field/Reconstructive Repair contract; grafting owns Severed/Missing. | Specific sources and values remain later content/balance work. | W-01, W-07 |
| W-03 — PROVISIONAL PAPER DIRECTION RESOLVED 2026-08-14 | WNR-0.1 defines owner-approved tunable immediate/periodic values and retains aggregate cap 20 in document 30. | Runtime configuration and final tuning remain separately gated. | W-01, W-02, W-07 |
| W-04 — PROVISIONAL PAPER DIRECTION RESOLVED 2026-08-14 | WNR-0.1 defines two-tick Control, encounter Stabilization, zero passive worsening chance, repair values, and visible Wound Stress. | Exact values may change after dependency review; runtime remains gated. | W-01–W-03, W-07, W-08 |
| W-05 — PROVISIONAL PAPER DIRECTION RESOLVED 2026-08-14 | WNR-0.1 requires Stabilized/Resolved Torso by the end of the actor's next Main opportunity and preserves a final refusal action. | Catastrophic runtime tests require a separate implementation plan. | W-01–W-04 |
| W-06 — RESOLVED ON PAPER 2026-08-16 | Package D makes Torso affect declared Torso/whole-body sources plus the approved Ruined-Torso deadline; it creates no second global health penalty. | Exact individual action profiles and runtime remain gated. | W-05 |

## P0 — Movement and main combat model

| ID | Decision required | Why it blocks runtime | Depends on |
|---|---|---|---|
| MOV-01 — RESOLVED 2026-08-13 | One shared action-produced state: Clinch, Engaged, or Distant. No grid, coordinates, blocks, or freely editable movement command. | Exact persistence and card profiles remain open; the representation is fixed. | — |
| MOV-02 — PARTIAL 2026-08-13 | Range changes belong to full tactical action/defense/reflex outcomes; they have no separate generic movement cost. Neutral settling is approved at one later round for Clinch and two for Distant. Exact action/card costs remain open. | Defines the real action economy without creating a locomotion layer. | MOV-01 |
| MOV-03 — RESOLVED ON PAPER 2026-08-16 | Package D makes Legs state affect only declared Legs-sourced/supporting posture, defense, Stand, and range-producing profiles. Legs never alter Lead automatically. | Individual profiles and runtime remain gated. | MOV-01, MOV-02 |
| MOV-04 — RANGE MAINTENANCE RESOLVED ON PAPER 2026-08-17 | Package C classifies profiles as Neutral, Exploit, Maintain, Shift/Create, or Release. Maintenance is execution-bound, non-stacking, source-revalidated, and never implicit; no current production action becomes a maintainer/releaser by implication. Pursuit and escape content remain later gates. | Document 35 resolves maintenance grammar without a universal movement command; individual production profiles and runtime remain gated. | MOV-01–MOV-03, ACT-01–ACT-03 |
| ACT-01 — BRAIN DOCTRINE PARTIAL 2026-08-21 | Zero or one Preparation, then zero or one Main commitment, then automatically surfaced eligible reflex events remain. Document 41 makes the body the source of physical capability, the player the author of a bounded active deck, and the Brain a deterministic modifier of the current hand and visible embodied-instability consequences. Inventory remains outside the hand with its timing/ownership/source safeguards. Exact acquisition, deck cadence, compatibility inputs, progression delivery, content, balance, and runtime remain open. | Establishes ownership and safety boundaries; the minimal paper implementation model is the current gate. | MOV-02 |
| ACT-02 — RESOLVED 2026-08-14 | Chosen preparations may shape defense, while the legal reflex-defense event appears automatically from the incoming action and current build. It is not played from the hand. | Document 31 fixes the layered timing roles; exact reflex execution remains later. | DEF-01–DEF-04 |
| ACT-03 — RESOLVED ON PAPER 2026-08-16 | Public Lead, two intention locks, sequential Lead-first resolution, full recomputation, unchanged Reply revalidation, and explicit cancellation/cost states are approved in document 32. | Runtime, content, exact information display, and special interrupt windows remain gated. | MOV-02, ACT-01 |
| PROC-01 — RESOLVED ON PAPER 2026-08-17 | Package B keeps treatment, Blood restoration, repair, extraction, and grafting separate; assigns Preparation/Main/contextual defaults; reserves exact sources; pays ordinary costs on execution; and makes started procedure chains atomic. | Document 36 resolves architecture only. Production profiles/values, runtime, detailed interruption checkpoints, and post-combat opponent-access predicates remain gated. | W-01–W-08, ACT-01–ACT-03 |

## P0 — Defense trade-offs

Cover It duration is fixed at one round. Brace is manual; Braced Legs is a separate
automatic charge. Document 31 resolves the architecture-level questions:

| ID | Resolved rule | Authority |
|---|---|---|
| DEF-01 — RESOLVED 2026-08-14 | Cover It protects one declared valued limb for one round. | Document 31 |
| DEF-02 — RESOLVED 2026-08-14 | Cover It requires another usable declared covering source; another arm is the default paper hypothesis and other sources require explicit content. | Document 31 |
| DEF-03 — RESOLVED 2026-08-14 | Its automatic Intercept redirects direct structural pressure to the covering source without automatic reduction. | Document 31 |
| DEF-04 — RESOLVED 2026-08-14 | It spends Main tempo, occupies/exposes the covering source, applies actual consequences there, and expires at round end. | Document 31 |
| DEF-05 — RESOLVED 2026-08-14 | Manual Brace is reliable prepared Knockdown prevention; it does not reduce damage and occupies Legs/posture. | Document 31 |
| DEF-06 — RESOLVED 2026-08-14 | Braced Legs preserve Main tempo as a passive fallback and do not spend their charge when an earlier layer already removes Knockdown. | Document 31 |
| DEF-07 — RESOLVED 2026-08-14 | One preparation may shape one automatic reflex route; one compatible passive applies per unresolved consequence type. Duplicate reductions and multiple active routes are prohibited. | Document 31 |

The complete owner-approved contract, acceptance requirements, and runtime boundary
are in `31_STRATEGIC_DEFENSE_CONTRACT_OWNER_REVIEW_v0_1.md`.

## P1 — Limb for Life

| ID | Resolved paper rule | Authority |
|---|---|---|
| LIFE-01 — RESOLVED 2026-08-19 | Player chooses the exact eligible limb; seeded randomness is not final selection. | Document 37 |
| LIFE-02 — RESOLVED 2026-08-19 | The prompt always includes Accept Death. | Document 37 |
| LIFE-03 — RESOLVED 2026-08-19 | Attached usable Left Arm, Right Arm, or Legs is eligible, including grafted/integrated/Critical/objective-critical parts; Head/Torso/Core and unusable/detached parts are excluded. | Document 37 |
| LIFE-04 — RESOLVED 2026-08-19 | Current tutorial player has one visible run-level affordance; other actors require an explicit grant and then use symmetric rules. | Document 37 |
| LIFE-05 — RESOLVED 2026-08-19 | No generic victory route requires sacrifice; future reactions or requirements need separate approved content. | Document 37 |

## P1 — Mental defeat, surrender, and mercy

| ID | Decision required | Why needed |
|---|---|---|
| MENT-01 | Define the minimum defeat-acceptance inputs and their representation. | Motivation alone cannot decide surrender. |
| MENT-02 | Define how objective impossibility, offensive incapacity, recovery hope, fear, honor, and desperation combine. | Prevents universal rationality and bespoke endings. |
| MENT-03 | Define which traits are generic and which are character-specific. | Needed for reusable opponents and bosses. |
| MENT-04 | Define the warning threshold before the player loses the final attack source. | Supports informed voluntary surrender. |
| MENT-05 | Define when surrender can be refused and whether an irrational last stand is legal. | Opponent motivation must constrain the answer. |
| MENT-06 | Define mercy as personality, strategy, relationship, or a weighted combination. | Same outward act may have different causes. |

## P1 — Negotiation minigame

| ID | Decision required | Why needed |
|---|---|---|
| NEG-01 | Maximum exchanges and how negotiation ends. | Prevents endless loops. |
| NEG-02 | Whether an exchange consumes combat time and whether Bleeding continues. | Determines the physical cost of talking. |
| NEG-03 | Offer vocabulary: Blood, items, limbs, release, debt, information, future obligation. | Defines legal offer construction. |
| NEG-04 | Opponent evaluation inputs and acceptable uncertainty. | Needed for deterministic, inspectable responses. |
| NEG-05 | Counter-offer construction and concession behavior. | Defines the actual minigame. |
| NEG-06 | Whether either side may attack during negotiation. | Needed for trust and exit behavior. |
| NEG-07 | What memory a rejected offer creates without numerical buffs/debuffs. | Combat resumes unchanged physically but behavior may remember. |
| NEG-08 | How invalid promises or unavailable assets are prevented. | Required causal validation. |

The current Jeff one-click exchange remains a survey shortcut until NEG-01–NEG-08 are
approved.

## P1 — Victory and encounter outcome

| ID | Open question |
|---|---|
| VIC-01 | Is Blood death an available route in every encounter or filtered by motivation/content rating? |
| VIC-02 | When is offensive incapacity partial success, full success, or only negotiation leverage? |
| VIC-03 | When does surrender satisfy the player's actual objective? |
| VIC-04 | How is escape scored for each actor? |
| VIC-05 | How are mutual and multi-route outcomes presented without a binary win screen? |
| VIC-06 | How do boss-specific predicates compose with general routes without hard-coded endings? |
| VIC-07 | Which consequences persist into the next encounter or run? |

## P2 — Motivation, information, and evidence

| ID | Open question |
|---|---|
| MOT-01 | Are Restoration, Survival, Control, and Elimination sufficient as primary classes? |
| MOT-02 | May actors hold primary and secondary motivations simultaneously? |
| MOT-03 | Which state changes may replace or reprioritize a motivation? |
| MOT-04 | What are the final 3–4 reusable ordinary-enemy profiles? |
| INFO-01 | How much motivation is public, inferred, or revealed by Focus? |
| INFO-02 | Is negotiation explicitly offered or discovered through behavior? |
| INFO-03 | Which victory routes are explained before an encounter? |
| TEST-01 | What human-test threshold validates motivation comprehension? |
| TEST-02 | What threshold validates perceived solution breadth and natural resolution? |
| CANON-01 | Is reciprocal-repair Jeff final canon or only the survey instrument? |

## Recommended decision order

```text
Wound meanings, repeated-Major collapse, repair boundary, and Torso direction - RESOLVED
→ movement representation - RESOLVED
→ action economy and cadence - DESIGN DIRECTION RESOLVED
→ wound/Blood/repair/treatment values and exact Torso rescue timing - PROVISIONAL PAPER DIRECTION RESOLVED
→ defense sources/effects/trade-offs - RESOLVED ON PAPER
→ initiative, intention lock, interruption, and simultaneous resolution - RESOLVED ON PAPER
→ body-state capability mapping - RESOLVED ON PAPER (PACKAGE D)
→ remaining card and item boundaries - RESOLVED ON PAPER (PACKAGE A2)
→ range-maintenance action grammar - RESOLVED ON PAPER (PACKAGE C)
→ treatment, repair, extraction, and graft commitment flow - RESOLVED ON PAPER (PACKAGE B)
→ Limb for Life and catastrophic survival - RESOLVED ON PAPER (PACKAGE A)
→ Brain hand modifier plus embodied instability - ACTIVE PAPER IMPLEMENTATION GATE
→ mental defeat, surrender, and mercy - NEXT GATE
→ negotiation timing and offer evaluation
→ victory persistence and presentation
→ information and presentation grammar
→ numeric reconciliation
→ content-readiness gate
→ reflex mechanics only after explicit reopening
```
