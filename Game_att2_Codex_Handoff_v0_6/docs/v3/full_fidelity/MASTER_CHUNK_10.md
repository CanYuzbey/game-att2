# V3 Full-Fidelity Master — sequential chunk 10/12

| Topic | V1 | V2 | V3 |
|---|---|---|---|
| Action cadence | Focus + Fast + Main | Prep + Main | Prep + Main; bounded Attention steering |
| Cards | excluded from simulator | core anatomical deck | core, body-subordinate |
| Brain | none | weighted Attention / evolving doctrines | Brain Architecture + Attention + downstream Parts |
| Tactical class guarantee | n/a | diagnostic no-guarantee | permitted/desired |
| Focus | exact enemy intent info | concept shifted by card system | source/family Attention bias candidate |
| Fast item | free pre-Main rail | removed; item uses Prep/Main | no third rail |
| Inventory | direct simulator items | Readied Item separate lane | retained |
| Surrender | Plead Pressure / encounter rules | Will + claims | Will + claims |
| Clean extraction | tools/quality | no corpse limb; living surrender transfer | legacy quality family + living transfer; exact tools open |
| Blood reward | broad simulator transactions | kill-specific opponent reward | kill-specific sample reward |
| Wounds | BLEEDING tags | 4-family wound model | 4-family downstream, minimal subset early |
| Sacrifice | soft random Limb for Life | explicit Package A archived | pillar #1, exact content open |
| Graft instability | d6 Unstable | broader body/instability work | multi-channel transformation cost |
| Range | minimal/none | explicitly removed | removed active sample |
| Body state | global percentage impairment | source-local profiles | source-local + Attention effect |
| Concept vocabulary | no deck | known from start | retained |
| Death card unlock | none | explicitly no Memory Card | retained no Memory Card |
| Concept progression | none | achievement persistent | retained downstream |
| Brain progression | none | boss persistent | retained downstream, separate from base Brain |
| NPC | scripts | Goal/Need/Claim | bounded purpose contract |
| Engine | Unity blocked | Unity working-hypothesis spike | engine open until V3-1 vehicle |
| Sample | Jeff/Anna/table simulator | Underground City | Underground City after staged combat proof |

---

# SOURCE DOCUMENT: legacy/00_LEGACY_MECHANICS_AND_FIXTURES_LEDGER.md

# Legacy Mechanics and Fixtures Ledger

Purpose: preserve detailed V1/V2 material without making it V3 canon.

## V1 S-001 Torn but Stable

Historical:
Blood 85; Human Head; Damaged Human Torso; Human Left Arm; Missing Right Arm; Weak Human Legs; Human Heart.

## V1 player actions/passives

Focus — cost3, Head, pre-action exact intent, once/round.
Grip Strike — Left Arm, cost0, 10 limb damage, no clean harvest.
Guard Flesh — grafted Right Arm, cost4, next limb damage -50%.
Brace — Weak Legs, prevent one Knockdown/fight.
Panic Pulse — Human Heart, once/fight, crossing below25 gives +10 capped35.

All legacy.

## V1 items/tools

Blood Bag — Fast, +25 or +15 if Bleeding.
Clotting Cream — Fast, cost8, stop Bleeding.
Bone Scissors — Main, cost6, once/fight, Critical clean sever / Damaged 8 surgical.
Hell Saw — Main cost18 once/fight; 18 saw; damaged/critical large 4–6 sever, 1–3 fail + Rage.
Claim the Cut — Main cost10 consumable; mark, later sever Clean.
Black Stitch — Anna treatment; remove Unstable or stop Bleeding in old scope.

## V1 Jeff

Blood70; Head25 Torso45 LArm20 RArm30 Legs35 Core35.
Desperate Swing / Cover It / Plead.
Both arms lost → immediate plead.
Both arms unusable → combat incapacity surrender.
Legacy tutorial acquisition actor.

## V1 Anna

Blood80.
Dazed Head / Stitched Torso / Human LArm / Crude Graft RArm / Human Legs / Leaking Heart.
Surgical Jab 8 with old bleeding roll.
Black Stitch.
Trade offer.
Calm Guard.
Legacy maintenance actor.

## V1 harvest

Clean / Stressed / Ruined.
Old emergency stability:
Clean d6 1 unstable;
Stressed d6 1–2 unstable;
Ruined no normal emergency graft.

## V1 salvage

Marked: cost8, 1–2 unusable,3–5 Stressed,6 Clean+Unstable.
Unmarked: cost15,1–3 unusable,4–5 Stressed,6 Unstable graftable.

## V1 Unstable v0.4

d6:
1 Twitch +3 cost/decline disabled;
2–4 Works;
5 Ache + stress if Blood-cost action;
6 Surge -2 cost or +2 Blood fallback.
Ache 1–2 disables next round.

## V1 Stabilized

Next sever default 4–6; fail → Hanging/Disabled, remove Stabilized.

## V1 Table v0.2

Integrate arm -15.
Repair torso -18.
Strengthen legs -12.
Loan +20 owe30.
Leave 0.

## V1 Blood bands

0 collapse; 1–20 critical;21–50 dangerous;51–100 normal;101–140 strong.

## V1 soft collapse

Limb for Life historical tutorial: seeded random non-core limb, survive at12.
Later archived Package A replaced this with explicit player choice and more exact rules.

## V1 scenarios

jeff_baseline
jeff_no_spend
failed_hell_saw
anna_stabilization
anna_greed
mini_campaign
blood_bag_balance

## V2 G1

Guard needs Full Right Arm or20 Blood from 70.
Blood →50/full.
Arm →60/Missing Right Arm/Controlled stump after provisional10.

## V2 DWF

See numeric ledger.

## V2 persistent systems

Concept Deck achievement path; Brain Part boss/progression path; no Memory Card.

## Reactivation rule

No legacy mechanic becomes V3 active merely because code already exists.
Need:
proof question + migration spec + V3 rules + tests + owner approval if identity-affecting.

---

# SOURCE DOCUMENT: legacy/01_NUMERIC_HYPOTHESIS_AND_RESULT_LEDGER.md

# Numeric Hypothesis and Result Ledger

All values below are historical/research unless explicitly re-approved.

## V1 July implementation values
Limb thresholds: >70 Intact, <=70>35 Damaged, <=35>0 Critical.
Source effect: 100/75/50%.
Grip Strike10.
Focus3; damaged Head +2.
Bleeding5 / severe8 / cap20.
Panic threshold25, +10, cap35.
Blood Bag25/15.
Clotting8.
Scissors6/8 surgical.
Saw18 cost/damage, Rage+5.
Claim10.
Marked salvage8.
Unmarked salvage15.
Table integrate15, repair18, legs12, loan+20/owe30.
Soft collapse12.

## V1 evidence results
July 23:
63 tests passed; Ruff; strict mypy.
seed42 mini_campaign = 25 Blood.
Historical paper mini-campaign = 37 Blood; unreconciled spare-arm sale difference.
Legacy 500-seed reviewed batches: ~46% completion for several fixed extraction strategies due to 50% saw; Blood Hoarder 0% completion under corrected labeling; no fixed strategy collapsed.

## V2 WNR-0.1
Closed0/0.
Open3 immediate /5 periodic.
Major8/8.
Clean Stump10/8.
Violent Stump15/12.
periodic cap20.
Control8; suppress2 ticks.
Stabilize12.
Field Repair10; +25% max capped70%.
Reconstructive18; Ruined→35%/Critical once/slot/encounter.
Wound Stress Open2 / Major4.

## V2 DWF-0.1
Block = ceil(D*0.75*GuardFactor).
GuardFactor reinforced.80 ordinary1 fragile1.20.
cue min900ms.
Block lock250ms.
Parry ±90ms.
Evade ±180ms.
assist100/140/200%.
speed100/75/50/pause.
Will90.
Parry Will24/30/36.
GoalCritical shock6/9/15; claim unavailable18.

## V2 product comparisons
~30 minute sample planning reference.
~10–12 hour full-game working hypothesis.
USD8–12 commercial comparison.

## V3 numerical status
No final balance values approved.
Any reused number must be explicitly labeled test fixture/research overlay.

---

# SOURCE DOCUMENT: legacy/02_EVIDENCE_AND_TIMELINE_LEDGER.md

# Evidence and Timeline Ledger

## V1 known evidence
- Jeff baseline paper
- no-spend exploit
- failed Hell Saw/death-spiral
- Anna medical
- forced Unstable
- mini-campaign paper
- non-canonical post-table probe
- Knockdown/Brace validation
- deterministic Python simulator
- structured scenario batches
- SELF-S01/S02 contaminated Warden diagnostics
- P01–P08 not completed in July snapshot

## July 23 automated snapshot
63 pytest passed.
Ruff passed.
strict mypy passed.
Seven scenarios executed.
seed42 mini campaign 25 Blood, 32 structured events.

## Development event dates recorded
2026-07-16 simulator review / post-table probe
2026-07-17 Knockdown/Brace and Warden paper/human-test ops
2026-07-18 self-play protocol/closeout/systemic causal skill/reconciliation
2026-07-23 consolidated audit

## Later known local milestones
Simulator causal integrity correction and interactive research shell are later local engineering milestones.
Treat their exact test counts/results only when their artifacts are directly available in the active repository/session; do not copy stale counts into new reports without verification.

## V2
Living paper docs dated Aug 25.
H1/visual lab = research fixtures, not product runtime.
DWF/WNR/brain/card-scaling = research/paper evidence classes.

## V3
September 4 documentation consolidation only.
No V3-1 runtime/human evidence yet.

---

# SOURCE DOCUMENT: legacy/03_V1_DETAILED_FEATURE_ITEM_SCOPE_LEDGER.md

# V1 Detailed Feature, Item, Scope, and Ambiguity Ledger

**Status:** LEGACY EVIDENCE / DESIGN HISTORY

This file preserves V1 details that are too granular to belong in active V3 specifications but must not disappear.

## 1. V1 locked/approved decision history

Historical V1 decisions included:
- single-player;
- PC;
- mostly silent/self-insert;
- hell-loop limb-grafting duel structure;
- Buckshot Roulette as atmosphere influence rather than mechanics blueprint;
- dark/disturbing tone with satirical relief;
- hybrid table decisions + side/body action cut-ins;
- six body slots;
- emergency graft + safer table;
- missing-limb builds rare/special in that version;
- Blood health/currency/fuel;
- enemies can lose limbs and react differently;
- limbs as build engine, tools/contracts as intervention;
- small expandable demo;
- source impairment;
- Plead;
- no-free-clean-basic-attacks;
- old Focus;
- old Fast medical;
- Plead Pressure;
- Anna after Jeff.

V3 explicitly changes several of these:
missing-limb specialization is more viable; card system is now core; surrender uses Will/claim; Focus and Fast have new meanings/boundaries; presentation is no longer locked.

## 2. V1 mechanics "Keep / Include Now"

Historical classifications:
- six slots;
- Blood;
- limb integrity/state;
- acting-limb impairment;
- clean sever gating;
- harvest quality;
- emergency grafting;
- grafting table;
- Focus;
- Fast medical;
- Plead Pressure;
- Unstable v0.4;
- low-Blood escape;
- event log;
- seeded RNG;
- Jeff;
- Anna;
- table choices.

V3 does not automatically preserve classification; see active specs and legacy ledger.

## 3. V1 "Add Now" details

### Intent Clarity
Historical proposed states:
- vague: enemy seems aggressive;
- partial: enemy will use right arm;
- exact: enemy will use right arm against torso.

V3 retains the need to instrument information clarity, not these exact strings.

### Action Source Tag
Historical fields:
body_slot, tool, requires_limb_state.

V3 expands source ownership to exact source sets, item instances, state-required and automatic origins.

### Test Metrics
Historical list:
final Blood, spent/gained, clean/stressed/ruined, player limb changes, collapse, Panic Pulse, Fast items, Focus, plea, graft result, table choice.

V3 expands these in metrics spec.

### Body Change Summary
Historical required questions:
- what changed in body?
- what action/passive gained/lost?
- what problem remains?

Directly retained as V3 evidence output.

### Soft Collapse
Historical simple rule:
at Blood 0 once during tutorial, random non-core limb removed, restore 12.

Superseded later by explicit-choice Limb for Life paper package, then not automatically activated in V3.

### Tool reset
Bone Scissors / Hell Saw refresh once/fight.
Consumables consumed across mini-campaign.

Retained only as legacy item lifecycle data.

## 4. V1 "Add Later"

Historical deferred:
- curses;
- rotten flesh;
- celestial judgment;
- mechanical malfunction;
- multiple starting bodies;
- Bone-Minotaur;
- Many-Eyed Flesh;
- more contracts;
- Regrowth Vaccine;
- Sell the Pain;
- Wrong Recipient;
- Promise debt;
- Table Favor;
- full shop;
- dialogue;
- meta progression;
- procedural enemy order;
- random loot.

V3 disposition:
none is active solely because it existed.
Potential future content only after named proof need.

## 5. V1 "Cut / Exclude for Now"

