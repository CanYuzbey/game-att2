# Game att2 — Combat Rules v0.5 (Simulator Baseline)

Status: approved for simulator testing, not final balance. Supersedes v0.4.

Owner amendment date: 2026-08-01.

v0.5 locks Blood 0 as death, promotes Limb for Life to an explicit limb-sacrifice
death-prevention rule, distinguishes manual Brace from the Braced Legs automatic
charge, and fixes Cover It duration at one round. Wound-to-Blood mappings and the
actual Cover It protection effect remain unimplemented in runtime and must not be
inferred without a separate implementation gate. Document 31 now supplies the later
owner-approved paper direction without changing this simulator ruleset.
Document 32 supplies the later owner-approved Public Lead and two-lock sequential
resolution direction. Its initiative, revalidation, and cancellation rules are also
paper authority only and do not replace the runtime sequence below.
Document 33 supplies the later owner-approved Source-First Modular Integrity paper
direction. Its Full/Strained/Desperate profiles, effect-package interface, and
Integrity Echo do not replace the runtime `100% / 75% / 50%` impairment rules below.
Document 34 supplies the later owner-approved Readied Inventory card/item boundary.
Its deliberate flexible-slot readiness, one voluntary inventory action per round,
and paper rejection of a free Fast-item rail do not replace the implemented Focus,
Fast-item, and Main sequence below.
Document 35 supplies the later owner-approved Resolution-Bound Range Tenure grammar.
Its execution-bound maintenance classifications, non-stacking counters, and
Lead/Reply range contest do not add runtime range state or change this sequence.

## 1. Round sequence

1. Apply start-of-round effects: bleeding and queued unstable consequences.
2. Resolve each Unstable graft's start-of-round check.
3. Generate and expose enemy visible intent.
4. Player may use Focus once.
5. Player may use at most one Fast item.
6. Player selects and resolves one main action.
7. Resolve enemy action if its source and conditions remain valid.
8. Run end checks: Panic/Limb for Life/death if needed, plea, incapacity surrender, victory, trade/bargain, temporary expiration.

The implementation should model phases explicitly enough for tests to verify timing.

## 2. Body slots

```text
HEAD, TORSO, LEFT_ARM, RIGHT_ARM, LEGS, CORE
```

A slot always has a runtime value, including `Missing` placeholders. Missing or Severed slots cannot source actions.

## 3. Limb model

Recommended representation:

- integrity and maximum integrity;
- one primary state: `INTACT`, `DAMAGED`, `CRITICAL`, `DISABLED`, `SEVERED`, `MISSING`, `RUINED`;
- orthogonal tags: `BLEEDING`, `GRAFTED`, `UNSTABLE`, `INTEGRATED`, `STABILIZED`, `MARKED`, `HANGING`, `PROTECTED`.

Thresholds:

```text
Intact: integrity > 70% max
Damaged: integrity <= 70% and > 35%
Critical: integrity <= 35% and > 0
Zero integrity: outcome is determined by damage/action context
```

Zero integrity does not automatically mean Clean sever.

## 4. Acting-limb impairment

Actions declare a source slot or source tool.

```text
Intact source: 100% effect
Damaged source: 75% effect
Critical source: 50% effect
Disabled/Severed/Missing/Ruined source: action cannot execute
```

For integer damage, round half up unless config states otherwise. Tests should pin the chosen rounding behavior.

If the enemy's declared source becomes unusable before enemy resolution, cancel the action and emit a cancellation event.

## 5. Blood

Blood is health, currency, and action fuel.

```text
0: death unless an explicit death-prevention effect resolves first
1–20: critical
21–50: dangerous
51–100: normal
101–140: strong
141+: future design space only
```

All changes are transactions with reason, before, delta, after, and trigger events.

### Panic Pulse

- Source: Human Heart.
- Once per fight.
- Trigger immediately when blood crosses from 25 or above to below 25, from any source including voluntary spending.
- Gain 10 blood.
- Result cannot exceed 35.

### Death and Limb for Life

At blood <= 0:

- normal outcome is death;
- once per run in the approved tutorial scope, `Limb for Life` may remove one
  seeded-random usable non-Core limb and restore Blood to 12 before death finalizes;
- if no eligible limb exists or Limb for Life was already used, death is final;
- the sacrificed limb is a cost that may keep a victory route viable; the sacrifice
  is not itself a victory or encounter ending. This resolves the earlier `C04`
  question: a designed victory route may require the sacrifice as an intermediate
  mechanic when its explicit route predicate says so.

The current seeded-random selection is retained from the approved prototype. Whether
the final player chooses the sacrificed limb remains an open decision.

### Wounds and Blood-loss direction

Owner-approved design direction, amended 2026-08-13:

- wound families are Closed Trauma, Open Wound, Major Wound, and Severed Stump;
- one body slot holds one dominant active wound; a stronger result escalates it rather
  than stacking duplicate wound records;
- treatment states are Untreated, Controlled, Stabilized, and Resolved;
- integrity/limb state owns normal capability, while wound state owns Blood pressure,
  treatment urgency, and repeat-Major tracking;
- immediate and periodic Blood loss are separate transactions; Closed Trauma normally
  has neither;
- the first qualifying Major result on an arm or Legs records Major Trauma 1/2;
- a second qualifying Major result before wound resolution sets that attached slot to
  0 Integrity and Ruined, making all slot-sourced actions illegal without creating
  Severed or Clean harvest;
- Field Repair may restore attached Damaged/Critical parts but cannot revive Ruined;
- rare Reconstructive Repair may restore an attached Ruined part only to Critical;
- Severed/Missing parts require grafting rather than repair;
- integrity repair, wound treatment, Blood restoration, and grafting are separate
  effects unless an action explicitly combines and logs them;
- clean severance produces lower donor stump pressure than violent severance, but both
  create a Severed Stump; harvest quality remains a separate record;
- player and enemy follow the same wound rules except for explicit visible exceptions;
- a basic attack that Ruins a limb creates Major Wound pressure but still cannot
  create Clean harvest;
- Ruined Torso uses conditional fatality with one explicit rescue window rather than
  ordinary nonfatal treatment or unexplained immediate death.

The complete approved meaning, causal order, invariants, and acceptance requirements
are in `27_AIMED_WOUND_SYSTEM_DIRECTION_AND_OWNER_REVIEW_v0_1.md`.

Document 30 and Development Master Amendment 36 now provide owner-approved provisional
paper values for wound thresholds, Blood pressure, repair, treatment duration,
Wound Stress, and Ruined-Torso rescue. Exact numbers remain tunable after connected
systems are defined. They are still deferred for runtime: configuration migration,
replacement of the current `BLEEDING` tag, deterministic tests, exploit validation,
and a separate implementation gate are required. Until then, ordinary runtime limb
damage does not automatically create the new wound-to-Blood behavior.

## 6. Player actions

### Focus

- Timing: Focus phase before Fast/main action.
- Base cost: 3 blood.
- Requires usable Head.
- Does not consume main action.
- Reveals exact enemy acting source and target.
- Once per round.

Head modifiers:

- Damaged: +2 cost.
- Critical: 50% chance of incomplete information through RNG.
- Unusable: unavailable.

### Grip Strike

- Source: Human Left Arm.
- Cost: 0.
- Damage: 10 to one target limb.
- Purpose: setup, impairment, disable, pressure.
- Never grants Clean Harvest by itself.

### Guard Flesh

- Source: Grafted Human Right Arm.
- Cost: 4.
- Reduce the next incoming limb-targeting damage by 50% for the round.
- The source arm is committed and cannot source another main action that round.

### Downed and Stand

An unresolved Knockdown applies `Downed`. While Downed, attacks, Focus, Guard Flesh, tools, and other normal actions are illegal. Fast medical items remain legal.

At the next action opportunity, the character must spend their normal action to `Stand`. Stand removes Downed, deals no damage, creates no harvest, does not clear other conditions, and does not permit another normal action that turn.

### Brace

Two distinct mechanics share related language and must remain visibly separate:

- **Brace — Manual Stance:** a player-selected Main action sourced by usable Legs;
  protects only the current round against one otherwise-successful Knockdown; expires
  unused at round end; limited to once per encounter in the current prototype.
- **Braced Legs automatic charge:** Strengthened/Braced Human Legs provide one passive
  automatic prevention per encounter; it requires usable legs and does not consume
  the manual Brace opportunity.

The automatic charge does not trigger on failed attempts or while already Downed and
refreshes at encounter start. The final trade-off between manual Brace, Braced Legs,
Guard Flesh, and Cover It remains unimplemented in this simulator baseline. Its later
paper architecture is approved in document 31.

## 7. Fast items

At most one Fast item before the main action. Fast items are not reactions unless explicitly tagged.

### Blood Bag

- consumable;
- gain 25 blood;
- if currently Bleeding, gain 15 instead;
- balance-watch item; do not nerf silently.

### Clotting Cream

- consumable;
- cost 8 blood;
- remove one selected Bleeding tag/effect.

## 8. Extraction tools and contract

### Claim the Cut

- consumable main action;
- cost 10;
- mark one enemy limb;
- if that limb is subsequently severed, quality is upgraded to Clean;
- enemy script may protect or aggressively use it.

### Bone Scissors

- one use per fight;
- main action, cost 6;
- on Critical small/medium limb: Clean sever unless Stabilized modifies the attempt;
- on Damaged valid limb: deal 8 Surgical damage;
- weak/invalid against large limbs.

### Hell Saw

- one use per fight;
- main action, cost 18;
- deal 18 Saw damage;
- against a Damaged/Critical valid large limb, roll d6:
  - 4–6: sever; quality based on target condition/mark;
  - 1–3: no clean sever and enemy gains Rage for next valid attack.
- Rage adds 5 base damage before source-limb impairment.

## 9. Clean, Stressed, and Ruined harvest

### Clean

Created by a mark guarantee, precise surgical sever, controlled bargain, or safe table procedure. Full value and best emergency stability.

### Stressed

Created by a violent sever after substantial damage or rushed extraction. Usable with lower value/stability.

### Ruined

Created by free blunt destruction, overkill, uncontrolled damage, or failed salvage. Not eligible for normal emergency grafting.

Emergency stability:

```text
Clean: d6 1 Unstable, 2–6 Stable
Stressed: d6 1–2 Unstable, 3–6 Stable
Ruined: no normal emergency graft
```

## 10. Salvage

### Marked Emergency Salvage

- cost 8;
- target Marked Ruined/Hanging/Disabled limb;
- d6: 1–2 unusable, 3–5 Stressed, 6 Clean but tagged Unstable for graft purposes.

### Unmarked Emergency Salvage

- cost 15;
- d6: 1–3 unusable, 4–5 Stressed, 6 graftable but Unstable.

## 11. Plead and surrender

Generic Plead Pressure begins at zero:

- +1 major limb Cleanly severed;
- +1 blood below 20;
- +1 core exposed;
- +1 explicit personality fear trigger.

Basic enemy pleads at 2.

Jeff also has special surrender conditions:

- both arms Severed: immediate plead;
- both arms unusable through Disabled/Ruined/Severed: combat-incapacity surrender;
- blood below 20: plead.

Combat-incapacity surrender does not upgrade ruined parts into Clean Harvest.

## 12. Unstable graft v0.4

At start of each round for each Unstable limb, roll d6:

- 1 Twitch: actions sourced by the limb cost +3 this round; player may decline and treat the limb as Disabled for the round.
- 2–4 Works: normal.
- 5 Ache: works; if used for a blood-cost action, make stress roll after resolution.
- 6 Surge: action sourced by limb costs 2 less, or player gains 2 blood if the limb is not used.

Ache stress d6:

- 1–2: limb Disabled next round;
- 3–6: no queued consequence.

An Integrated graft does not make normal Unstable checks.

## 13. Stabilized

The next sever attempt against a Stabilized limb requires the specified success roll (default 4–6 on d6). On failure:

- the limb becomes Hanging/Disabled;
- Stabilized is removed;
- no Clean Harvest is produced;
- a later valid sever attempt may proceed normally.

The required roll must be visible in logs before commitment.

## 14. Encounter-specific rules

### Jeff

- simple intent: Desperate Swing or Cover It;
- Cover It lasts only the round in which it is used and never persists automatically;
- Jeff may choose Cover It again on a later round only by spending another enemy
  action;
- its protected target, damage handling, source requirement, and trade-off against
  Brace are approved on paper in document 31 but remain runtime-deferred, so Cover It
  is not an active runtime intent yet;
- marked limb causes a configurable protect/use response once that effect is approved;
- loss/disable of action arms changes available actions;
- surrender conditions above.

### Anna

- Surgical Jab base 8 using Crude Graft Arm;
- Bleeding on d6 5–6, or 4–6 if target already Damaged;
- Black Stitch applies Stabilized;
- Trade Offer may stabilize player's first Unstable graft and/or stop Bleeding in exchange for sparing her Crude Graft Arm;
- Anna is not required to die.

## 15. Grafting Table v0.2

- Integrate grafted arm: cost 15, Stable Grafted → Integrated.
- Repair damaged torso: cost 18, remove damaged-torso bleeding vulnerability.
- Strengthen weak legs: cost 12, create Braced Human Legs definition for future tests.
- Table Loan: gain 20 now, owe 30 after next fight; store as minimal prototype debt only.
- Leave unchanged: cost 0.

No randomized shop or table favor in v0.1.
