# Game att2 — Combat Rules v0.4 (Simulator Baseline)

Status: approved for simulator testing, not final balance.

## 1. Round sequence

1. Apply start-of-round effects: bleeding and queued unstable consequences.
2. Resolve each Unstable graft's start-of-round check.
3. Generate and expose enemy visible intent.
4. Player may use Focus once.
5. Player may use at most one Fast item.
6. Player selects and resolves one main action.
7. Resolve enemy action if its source and conditions remain valid.
8. Run end checks: Panic/Collapse if needed, plea, incapacity surrender, victory, trade/bargain, temporary expiration.

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
0: collapse
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

### Collapse and tutorial soft collapse

At blood <= 0:

- normal outcome is collapse;
- once in the tutorial mini-campaign, `Limb for Life` may remove a seeded random non-core limb and restore blood to 12;
- if no removable non-core limb exists or the valve was used, the run collapses.

Soft collapse is a test valve, not a final locked game mechanic.

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

- Strengthened/Braced Human Legs grant one automatic Brace charge per encounter.
- On the first otherwise-successful Knockdown, Brace cancels the Knockdown, consumes the charge, and prevents Downed.
- Brace does not trigger on failed attempts, while already Downed, without a charge, or if the legs are unusable.
- The charge refreshes at encounter start. There is no reaction prompt or manual Brace timing.

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
- marked limb causes a configurable protect/use response;
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
