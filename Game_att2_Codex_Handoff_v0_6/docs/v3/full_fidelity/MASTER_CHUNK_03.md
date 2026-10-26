# V3 Full-Fidelity Master — sequential chunk 03/12

Every temporary effect declares expiry.
Historical Guard Flesh bug (persisting across rounds if no attack landed) is a permanent regression category.

## 16. Panic / collapse

V1 Panic Pulse and Limb for Life are legacy mechanics.
V3 preserves the requirement:
involuntary Blood loss can cause collapse/death and survival effects must have explicit causal order.

No V3 numeric threshold yet.

## 17. Anti-stall requirement

A complete round must normally alter at least one finite meaningful fact or consume opportunity so defense/healing cannot recreate the identical whole combat state for free.

Exact implementation OPEN.

## 18. Combat resolution

Actions mutate state; they never directly choose endings.

Possible state-derived stops:
death / physical incapacity / objective completion / surrender / bargain / escape / mutual resolution / unresolved continuation.

## 19. Historical rules explicitly not active by default

- Plead Pressure threshold 2;
- Jeff two-arm special surrender;
- Grip Strike 10;
- Hell Saw 18 + Rage;
- Bone Scissors 6;
- Claim the Cut 10;
- Guard Flesh 4;
- Brace once/fight;
- Panic Pulse below 25;
- one Fast item/round;
- Unstable d6 table;
- Stabilized 4–6 sever check.

All preserved in legacy ledgers.

---

# SOURCE DOCUMENT: docs/04_BODY_SOURCE_CAPABILITY_AND_DAMAGE_V3_FULL.md

# Body, Source, Capability, and Damage V3 — Full

**Status:** BINDING STRUCTURE

## 1. Six-slot sample body

Head / Torso / Left Arm / Right Arm / Legs / Core.

## 2. Minimum source record

```text
source_id
slot
definition/origin
attachment_state
integrity / structural_state
wound
treatment_state
graft/integration
provenance if meaningful
capability_tags
expression_ids
maintenance_profile
composition_tags
reservation/occupation
```

## 3. Structural states

V3 requires at least the semantic distinctions:
- healthy/full;
- degraded/strained;
- critical/desperate;
- offline/disabled;
- ruined;
- severed;
- missing.

Exact enum and thresholds OPEN.

## 4. V1 mapping

V1 exact:
Intact >70%, Damaged <=70% >35%, Critical <=35% >0.

Disposition:
**legacy numeric implementation**.
Useful as a test fixture if needed, not active V3 balance.

## 5. V2 source-local degradation

Inherited:
damage primarily affects actions owned by that source.
Another limb does not become weaker merely because one limb is damaged.

Local profile may alter:
- effect;
- cost;
- exposure;
- information clarity;
- target access;
- defense quality.

This is preferred over one universal effectiveness multiplier.

## 6. Direct capability

Body source must not be meaningful only through cards.

Examples of direct capability classes:
- force/lifting;
- grip/tool manipulation;
- guarding;
- fine manipulation;
- traversal;
- perception;
- physiological regulation.

Exact environmental interactions belong to content design, not generic assumptions.

## 7. Source loss

When source becomes permanently invalid:
- dependent active expressions Invalid;
- direct capability removed;
- automatic/passive capability removed if sourced there;
- multi-source actions revalidate;
- later locked unstarted actions may cancel;
- Attention pool recomputes;
- no replacement card/source invented.

## 8. Temporary source restriction

Reservation/occupation can make an opportunity temporarily Dormant rather than permanently Invalid where restoration is possible.

## 9. Multi-source

All sources identified.
The weakest required source may govern profile only if action definition says so.
No silent regrip/substitution.

## 10. Integrity Echo

V2 proposed a capped whole-body "Integrity Echo" that could not alter legality/actions/Blood/death etc.

V3 disposition:
**NOT ACTIVE**.
Reason: V3 emphasizes source-local causality and composition costs; Echo risks abstract stat overlay.
Keep as research provenance only.

## 11. Missing-limb specialization

Missing anatomy may:
- narrow card pool;
- improve Attention consistency;
- remove defense/world capability;
- create single-point-of-failure risk.

Valid build pattern.

## 12. Head / Core

May generate cards.
Usually complementary:
Head — perception/control/sensory;
Core — Blood/physiology/regeneration/compatibility.

No rule forbids rare Head/Core-primary builds.

## 13. Readability

Inspect body should expose:
- present state;
- wound/treatment;
- capabilities gained/lost;
- dependent cards;
- maintenance/compatibility;
- provenance only when relevant.

## 14. Zero-integrity rule

Retain V1 causal lesson:
zero integrity outcome depends on damage/action context.
Zero does not automatically mean a clean transferable sever.

---

# SOURCE DOCUMENT: docs/05_WOUNDS_BLOOD_GRAFT_AND_TRANSFORMATION_V3_FULL.md

# Wounds, Blood, Grafting, Sacrifice, and Transformation V3 — Full

**Status:** ACTIVE STRUCTURE / RESEARCH NUMERICS SEPARATE

## 1. Separate state dimensions

Do not conflate:
- integrity;
- structural state;
- wound;
- treatment;
- Blood;
- harvest/transfer quality;
- graft integration;
- composition compatibility.

## 2. V2 wound families — inherited paper model

- Closed Trauma
- Open Wound
- Major Wound
- Severed Stump

One dominant active wound per slot was the V2 paper contract.
A stronger wound escalates; weaker duplicate does not stack.

V3-1 may use a smaller subset if needed; broader model remains active downstream.

## 3. Treatment states

Untreated / Controlled / Stabilized / Resolved.

Treatment does not:
- restore integrity;
- restore Blood;
- repair a ruined structure.

Repair does not treat wounds.
Grafting is not repair.

## 4. V2 WNR-0.1 — research-only exact values

Retained in numeric ledger:
Closed 0/0, Open 3 immediate +5 periodic, Major 8/8, Clean Stump 10/8, Violent Stump 15/12; periodic cap 20; Control 8; Stabilize 12; Field Repair 10→25% capped70%; Reconstructive 18→35% Critical.

These are not V3 balance.

## 5. Ruined Torso

V2 paper model:
Ruined Torso can create pending fatality with one ordinary Main rescue window; Stabilize/Resolve required.

V3 disposition:
**ACTIVE DOWNSTREAM MECHANIC FAMILY, not V3-1 requirement.**
No exact deadline/value implemented until needed.

## 6. Blood identity

Blood = life + economy + selected ability/emergency-control fuel.

Every transaction records:
before / delta / after / reason / source / voluntary vs involuntary.

## 7. Opponent reward

PAPER RULE:
kill → opponent-derived Blood + same-day limb route closes.
living surrender accepted → agreed legal limb + no kill-Blood.

No ordinary corpse extraction in active sample.

## 8. V1 Blood bands

0 collapse, 1–20 critical, 21–50 dangerous, 51–100 normal, 101–140 strong.

Disposition:
legacy UX/balance fixture only.

## 9. V1 Panic Pulse

Exact once/fight below-25 → +10 capped35 is legacy.
Its lesson survives: emergency survival effects need explicit trigger order and Blood ledger.

## 10. V1 low-Blood soft valves

Historical:
- Limb for Life;
- sell part;
- debt;
- bargain Blood;
- medical reward;
- table loan.

V3 does not automatically activate them.
The active principle:
avoid untelegraphed post-fight dead-end traps without erasing consequences.

## 11. Transfer quality

V1 Clean/Stressed/Ruined remains a useful active design family:
quality may affect stability/value/maintenance.

Exact generation rules and dice are OPEN.

## 12. Graft chain

```text
validate part
→ validate target slot
→ validate ownership/access
→ validate procedure/tool/table
→ validate Blood/cost
→ atomic graft
→ create wound/stump/integration state
→ recompute capability
→ reconstruct Anatomical Deck
→ recompute Brain/Attention eligibility
→ log provenance/evidence
```

## 13. Emergency vs controlled graft

Active design family:
emergency faster/riskier; controlled safer.
Exact tiers OPEN.

## 14. Identity sacrifice

Binding:
chosen sacrifice is more identity-defining than ordinary loss.

`replacement ≠ undo`.

Possible persistent channels:
- protagonist memory;
- NPC relation;
- body provenance;
- route/opportunity;
- world state.

## 15. Archived Limb for Life package

Historical owner-approved paper package specified:
Blood-0 only, one charge, exact eligible attached Arm/Legs, player chooses, no harvested object, untreated stump, net Blood 12, non-Blood Torso fatality not prevented.

V3 does **not** automatically activate that exact mechanic.
V3 retains:
- exact-choice preview;
- no random sacrifice;
- atomicity;
- no harvested object from self-sacrifice unless authored;
- recomputation/cancellation;
- separate fatality sources.

## 16. Transformation cost channels

- intrinsic;
- composition;
- functional;
- world/social;
- native-body opportunity cost.

No universal corruption score.

## 17. Power ceiling

A transformed body may significantly exceed human raw power.

Balance target is not equal limbs; it is meaningful cost/topology.

## 18. Composition

Potential inputs:
species/organic/mechanical/celestial/demonic tags, neural demands, size/load, Blood maintenance.

Inputs are architecture families, not finalized lore rules.

## 19. Maintenance risks

Watch:
- death spiral;
- maintenance tax becoming mandatory;
- graft always-upgrade behavior;
- composition penalty becoming opaque;
- Blood economy crowding out experimentation.

## 20. Own-limb replacement

Physical graft can restore slot function but does not erase sacrifice provenance.

---

# SOURCE DOCUMENT: docs/06_DECK_CONCEPT_BRAIN_ATTENTION_V3_FULL.md

# Deck, Concept, Brain, and Attention V3 — Full Fidelity

**Status:** BINDING V3 ARCHITECTURE; COUNTS/WEIGHTS OPEN

## 1. Anatomical deckbuilder thesis

> A card states the technique/intention; the body determines the exact physical expression and physical cost.

## 2. Complete abstract vocabulary

INHERITED ACTIVE:
The complete abstract card-concept vocabulary is known from the beginning.

The game is not built around discovering "Punch" as a permanent card after death.

Death generates no Memory Card.

## 3. Ownership table

| Layer | Owns | Cannot own |
|---|---|---|
| Concept vocabulary | abstract intent/techniques | physical source |
| Body | physical capability + source-valid expressions | meta access |
| Concept Deck | specialization/exchanges/bias | missing anatomy |
| Anatomical Deck | current source-valid carried expressions | inventory/reflex |
| Brain Architecture | slot structure, class guarantees/flexible tendencies | physical capability |
| Attention | current weighted access | extra action |
| Brain Part | downstream bounded modifier with tradeoff | source invention |
| Readied Item lane | one deliberate inventory opportunity | random body draw |

## 4. V3 resolution order

```text
known concepts
→ body-valid physical expressions
→ Concept Deck compatibility / atomic exchange
→ Anatomical Deck
→ Brain Architecture slot role
→ legal candidate pool
→ Attention weights
→ selected current access
→ hold/drop/commit
→ Preparation/Main
→ source/reflex/consequence
```

## 5. Concept Deck — inherited + V3 extension

Achievement/non-boss milestone path.

Persists through death.

Contains:
- playstyle promise;
- requirements;
- explicit remove/add exchanges;
- special cards;
- visible sacrifice/gain;
- compatibility/Dormant rule.

Atomic:
validate every sacrificed card/source → validate every gained card/source → validate constraints → mutate all or nothing.

V3 additionally permits bounded probability bias.
It must not dominate Brain or fabricate capability.

## 6. V2 scaling guardrails — retained as research bounds

First bounded catalogue:
- max 5 cards/exact source;
- max 3 functional labels/card;
- max 6 causal mechanic atoms;
- exactly 1 causal signature creativity atom/card;
- max 2 special gains per ordinary Concept exchange;
- max 1 novel engine primitive/card, separately reviewed.

V3 card-count working guidance 2–3 / 3–5 / ~5–6 is compatible.

## 7. Brain-history reconciliation

