# Game att2 — Development Master File v0.6

Prepared for: Can Yüzbey  
Project: Game att2  
Current stage: hybrid core-gameplay definition after the deterministic simulator
Status: **Turn-based strategy plus reflexive execution is owner-directed; H1 is not yet implemented. Unity remains delayed.**

## 2026-08-01 owner amendment

This amendment supersedes conflicting v0.4 wording without rewriting historical paper
evidence:

- Combat Rules v0.5 is the current simulator rule authority.
- Blood 0 means death unless an explicit death-prevention rule resolves first.
- Limb for Life is the approved once-per-run exception: sacrifice one seeded-random
  usable non-Core limb and restore 12 Blood. It is a costly continuation mechanic,
  not an encounter victory by itself.
- Wounds may create immediate, periodic, combined, or zero Blood loss, but wound
  mappings and values remain open; runtime must not infer them.
- Cover It lasts one round and must be chosen again on later rounds. Its protection
  effect and trade-off are still open, so it remains runtime-deferred.
- Brace is a manual one-round Main-action stance. Braced Legs separately provide one
  automatic Knockdown prevention charge per encounter.
- Movement capability, reachability, and the final main combat/action-economy model
  are now subordinate to the hybrid macro direction in
  `19_CORE_GAMEPLAY_DIRECTION_AND_HANDOFF_2026-08-01.md` and remain unimplemented.
- Strategic combat remains turn-based. Bounded reflexive execution moments—starting
  with a timing-based Block hypothesis—must reinforce body state, intent reading, and
  Blood decisions rather than bypass them.
- `18_OPEN_COMBAT_AND_MOBILITY_DECISIONS.md` is a dependency register, not a sequence
  of independent owner interviews.

---

## 0. Document Purpose

This file consolidates the current validated development state after:

1. Original handoff v0.1.
2. Jeff paper test.
3. Combat Rules v0.3 validation batch.
4. Forced Unstable Graft test.
5. Mini-campaign paper test v0.4: `Jeff → emergency graft → Anna → stabilization/trade → grafting table`.

It defines:

- current confirmed design,
- current temporary combat rules,
- what belongs in the next simulator,
- what must stay excluded,
- which mechanics/items should be added, kept, revised, or cut,
- simulator architecture/spec,
- test coverage plan,
- decision ledger,
- risk register,
- next sprint tasks.

This is not a final GDD. It is the **current product source of truth** for Codex implementation of the simple digital simulator. It supersedes the earlier condensed task, condensed skill, and short project-state files.

---

## 1. Current Project Status

### Encounter 3 paper-research reconciliation — 2026-07-18

The owner approved Encounter 3 as a bounded causal pressure encounter for moderated
paper testing only. Use fixed fixture `E3-PRETABLE-01`, four table options, three
Warden paper target zones, state-aware Policies A/B, bounded combat incapacity, and
an eight-round unresolved cap as defined in
`encounter_3/BOUNDED_CAUSAL_PAPER_SPEC_v0_2.md`.

This may test source damage and capability loss. It does not approve Warden runtime/config, death, harvest, anatomy, organs, penetration, surrender, bargaining, escape, personality, generalized AI, or Unity. Eight valid P01–P08 human sessions are the next evidence gate. `SELF-S01` and `SELF-S02` remain contaminated designer diagnostics.

```text
Current maturity: Level 2.5 — Prototype Plan validated through internal paper tests
Next target: Level 3 candidate — crude playable loop, but only as a simple simulator first
Digital step allowed: Python console simulator or spreadsheet-style simulator
Digital step not yet allowed: Unity graybox
```

### Confirmed gate result

```text
Paper mini-campaign gate: PASS FOR SIMPLE DIGITAL SIMULATOR
Unity graybox gate: NOT PASSED YET
```

### Why simulator is allowed

The core sequence produced meaningful choices:

```text
want limb → pay blood → damage/sever → harvest → emergency graft → suffer instability → stabilize through Anna → integrate at table → end with changed body
```

### Why Unity is still delayed

Unity would force premature decisions about visual UI layout, animation timing, table/action camera switching, asset pipeline, scene structure, input/presentation implementation, and polished combat feedback. Those are not ready.

---

## 2. Current One-Sentence Pitch

**Game att2 is a single-player PC hell-loop limb-grafting roguelike where the player survives ritualized turn-based duels by cutting useful limbs from other beings, spending blood as both health and currency, and rebuilding their body into a desperate combat engine.**

---

## 3. Current Player Fantasy

```text
I wake up broken.
I fight other broken things.
I cut away what I need.
I graft it onto myself.
I become something that can survive the loop.
```

The player is not a hero. The player is a mostly silent self-insert trapped inside a hellish survival economy.

---

## 4. Locked / Approved Decisions

| ID | Decision | Status |
|---|---|---|
| D-001 | Single-player | Locked |
| D-002 | PC target | Locked |
| D-003 | Player mostly silent/self-insert | Locked |
| D-004 | Hell-loop limb-grafting duel roguelike/roguelite | Locked |
| D-005 | Buckshot Roulette is atmosphere influence, not mechanics blueprint | Locked |
| D-006 | Dark/disturbing tone with satirical relief | Locked |
| D-007 | Hybrid presentation: table decisions + side/body action cut-ins | Locked for prototype |
| D-008 | 6 body slots in first demo | Locked |
| D-009 | Emergency grafting + safer grafting table | Locked |
| D-010 | Missing-limb builds are rare/special, not normal default strategy | Locked |
| D-011 | Blood is health + currency + fuel | Locked for prototype, high risk |
| D-012 | Enemies commonly lose limbs but may react differently | Locked |
| D-013 | Limbs are build engine; cards/contracts/tools are intervention layer | Locked |
| D-014 | First goal is small playable demo, expandable later | Locked |
| D-015 | Limb state affects action effectiveness | Approved for prototype |
| D-016 | Plead can trigger from limb loss | Approved for prototype |
| D-017 | Emergency grafting stays in first playable | Approved for prototype |
| D-018 | Basic attacks cannot cleanly harvest limbs alone | Approved for simulator |
| D-019 | Focus is pre-action information | Approved for simulator |
| D-020 | Fast medical item tag exists | Approved for simulator |
| D-021 | Plead Pressure exists | Approved for simulator |
| D-022 | Combat Rules v0.5 are current simulator ruleset | Owner-amended |
| D-023 | Unity remains delayed until simulator results | Recommended |
| D-024 | Anna is correct second encounter after Jeff | Recommended |

---

## 5. Open Decisions

| Topic | Current State | Needed When |
|---|---|---|
| Final title | Not decided | Later branding |
| Final art style | Stylized/pixel-inspired likely, not locked | Before vertical slice |
| Engine | Unity likely, not locked | After simulator |
| Full run structure | Not designed | After core loop simulator |
| Meta progression | Not designed | After repeated run tests |
| Map/exploration | Delayed | After vertical slice direction |
| Dialogue system | Delayed | After first playable proof |
| Final enemy roster | Not designed | Production stage |
| Final number of limbs | Not designed | After prototype data |
| Steam/store strategy | Future | Release planning |
| Long-term progression/unlocks | Future | After loop validation |

---

## 6. Design Pillars v0.5

### Pillar 1 — Body as Build

The player does not mainly collect weapons. The player becomes the weapon. Every important limb must provide at least one action, passive, tradeoff, economy interaction, grafting consequence, or tactical identity.

### Pillar 2 — Blood as Volatile Bankroll

Blood is survival, currency, ability fuel, debt resource, wager, and bargain material. The player should often think: **“I can afford this, but should I?”**

### Pillar 3 — Combat as Extraction

Winning is not only reducing HP. Combat asks: **“What do I need from this enemy, can I take it cleanly, and can I survive the cost?”**

### Pillar 4 — Desperate Maintenance

Getting a limb is not enough. The player must stabilize, preserve, sell, integrate, repair, cleanse, accept debt, or live with complications.

### Pillar 5 — Ritualized Readability

Every major action must answer:

1. What did I target?
2. What changed?
3. What did it cost?
4. What did I gain?
5. What new risk did I create?

---

## 7. Core Loop v0.5

```text
Player enters fight damaged or incomplete.
Enemy presents body parts, threats, and potential rewards.
Player reads intent.
Player spends blood or preserves blood.
Player damages/disables/severs target limbs.
Enemy reacts through attacks, protection, medical actions, or pleading.
Player wins, bargains, dies, becomes otherwise incapacitated, or retreats.
Player harvests, grafts, sells, preserves, or refuses parts.
Body state changes.
Next encounter tests the consequences.
Grafting table lets player stabilize or specialize.
Loop repeats because the player wants a stronger/weirder body.
```

---

## 8. Current Validated Mini-Campaign

### Sequence

```text
Start: S-001 Torn but Stable, missing Right Arm, 85 blood
Jeff: claim right arm → damage → Hell Saw sever → take both arms by forced bargain
Post-Jeff: emergency graft Right Arm → Unstable → sell spare arm
Anna: unstable graft creates tension → Focus + Guard Flesh matter → accept stabilization instead of more limb greed
Grafting Table: integrate grafted Right Arm
End: 37 blood and changed body
```

### Final state from mini-campaign

```text
Blood: 37
Head: Human Head — Intact
Torso: Damaged Human Torso — Intact
Left Arm: Human Left Arm — Intact
Right Arm: Integrated Grafted Human Right Arm
Legs: Weak Human Legs — Intact
Core: Human Heart — Intact
```

### Design verdict

```text
Continue.
Do not pivot.
Do not move to Unity yet.
Move to simple simulator.
```

---

## 9. Combat Rules v0.5 — Simulator Baseline

### 9.1 Round Order

```text
1. Start-of-round effects: approved bleeding, debt, and unstable graft checks
2. Enemy visible intent
3. Optional Focus: pre-action info, does not consume main action
4. Optional Fast medical item: max 1 per round
5. Player main action
6. Enemy action resolution
7. End-of-round checks: death/incapacity, plea, victory, bargain, temporary states expire
```

### 9.2 Blood Ranges

| Blood | Meaning |
|---:|---|
| 0 | death unless Limb for Life resolves first |
| 1–20 | critical |
| 21–50 | dangerous |
| 51–100 | normal |
| 101–140 | strong |
| 141+ | future unstable/rich design space |

### 9.3 Limb Thresholds

```text
Intact: above 70%
Damaged: 70% to above 35%
Critical: 35% to above 0%
Severed / Destroyed: 0
```

### 9.4 Acting Limb Impairment

```text
Intact source limb: full effect
Damaged source limb: -25% effect
Critical source limb: -50% effect
Disabled / Severed / Missing source limb: action fails or enemy uses fallback
```

### 9.5 Basic Attack Restriction

```text
Grip Strike:
Cost 0 blood.
Deals 10 damage to one limb.
Can damage, disable, ruin, or create pressure.
Cannot create clean graftable severing by itself.
```

If Grip Strike reduces a limb to 0, the result is **Mangled / Disabled / Ruined**, not Clean Harvest, unless a mark/tool/bargain/table rule upgrades it.

### 9.6 Clean Sever Requirements

Clean harvest requires at least one of:

- Claim the Cut,
- Bone Scissors on Critical small/medium limb,
- Hell Saw success on Damaged/Critical large limb,
- special limb ability,
- enemy bargain,
- grafting table procedure.

### 9.7 Harvest Quality

| Quality | Meaning |
|---|---|
| Clean Harvest | full value, best graft stability |
| Stressed Harvest | usable but lower value/stability |
| Ruined Harvest | cannot emergency graft safely; scrap/table/ritual only |

Emergency graft stability:

```text
Clean Harvest: 1d6; 1 = Unstable, 2–6 = Stable
Stressed Harvest: 1d6; 1–2 = Unstable, 3–6 = Stable
Ruined: cannot emergency graft without special salvage
```

### 9.8 Plead Pressure

```text
Plead Pressure starts at 0.
+1 major limb cleanly severed
+1 enemy blood below 20
+1 core exposed
+1 personality-specific fear trigger
Basic enemy pleads at 2 Plead Pressure.
Jeff pleads immediately if both arms are lost.
```

### 9.9 Focus

```text
Focus:
Cost 3 blood.
Requires usable Head.
Timing: before main action.
Effect: reveal exact enemy acting limb and target.
Limit: once per round.
Does not consume main action.
```

Head condition modifier:

```text
Intact Head: works normally
Damaged Head: +2 blood cost
Critical Head: 50% incomplete information
Disabled/Missing/Severed Head: unavailable
```

### 9.10 Fast Medical Items

```text
Fast:
Can be used before the main action.
Max 1 Fast item per round.
Usually consumable.
Cannot be used retroactively after enemy hit unless item has Reaction tag.
```

Current Fast items:

- Blood Bag,
- Clotting Cream,
- Emergency Tourniquet later only if needed.

### 9.11 Bleeding

```text
Basic Bleeding: -5 blood at start of round
Severe Bleeding: -8 blood at start of round
Bleeding cap: maximum -20 blood per round
```

Simulator must log projected next-round blood and critical warning if projected blood is below 25.

### 9.12 Panic Pulse

```text
Human Heart passive.
Once per fight.
Triggers when blood drops below 25 from any source.
Gain 10 blood.
Cannot raise blood above 35.
```

### 9.13 Unstable Graft v0.4

At start of round, roll 1d6:

| Roll | Result |
|---:|---|
| 1 | Twitch: limb action costs +3 blood this round; if unpaid, limb Disabled this round |
| 2–4 | Works normally |
| 5 | Ache: limb works; if used this round, roll stress after action |
| 6 | Surge: action with limb costs 2 less blood, or gain +2 blood if not using it |

Ache stress roll:

```text
If unstable limb is used for blood-cost action during Ache:
1d6
1–2 = limb Disabled next round
3–6 = no extra effect
```

### 9.14 Stabilized Limb

```text
Stabilized:
Next sever attempt requires success roll.
If success: sever normally.
If fail: limb becomes Disabled/Hanging, Stabilized removed, next sever attempt easier.
```

### 9.15 Marked Emergency Salvage

If a marked limb becomes Ruined/Hanging/Disabled before clean sever:

```text
Marked Emergency Salvage:
Cost 8 blood.
Roll 1d6.
1–2 = unusable
3–5 = Stressed Harvest
6 = Clean but Unstable
```

Unmarked ruined salvage:

```text
Emergency Salvage:
Cost 15 blood.
Roll 1d6.
1–3 = unusable
4–5 = Stressed Harvest
6 = Unstable graftable limb
```

### 9.16 Low-Blood Escape Valve

If player ends a fight below 15 blood, offer at least one:

- sell harvested part,
- accept blood debt,
- take bargain blood,
- consume medical reward,
- emergency table loan.

This is not a full debt economy yet. It is a prototype soft-loss valve.

---

## 10. Core Content for Simulator v0.1

### 10.1 Starting Body: S-001 — Torn but Stable

```yaml
id: S-001
name: Torn but Stable
blood: 85
slots:
  head: Human Head
  torso: Damaged Human Torso
  left_arm: Human Left Arm
  right_arm: Missing
  legs: Weak Human Legs
  core: Human Heart
conditions: []
purpose: tutorial baseline
```

### 10.2 Player Limb Set

```yaml
Human Head:
  slot: head
  action: Focus, cost 3 blood, pre-action reveal
Damaged Human Torso:
  slot: torso
  passive: extra bleeding vulnerability
Human Left Arm:
  slot: left_arm
  action: Grip Strike, cost 0, 10 limb damage, cannot clean harvest alone
Grafted Human Right Arm:
  slot: right_arm
  action: Guard Flesh, cost 4, reduce next incoming limb damage by 50%
Weak Human Legs:
  slot: legs
  action: Brace, prevent Knockdown once
Human Heart:
  slot: core
  passive: Panic Pulse once per fight
```

### 10.3 Tools / Contracts

```yaml
Blood Bag:
  timing: Fast
  uses: consumable
  effect: gain 25 blood, or 15 if Bleeding
  risk: may be too strong
Clotting Cream:
  timing: Fast
  cost: 8 blood
  uses: consumable
  effect: stop one Bleeding effect
Bone Scissors:
  timing: main action
  cost: 6 blood
  uses: 1 per fight
  effect: clean sever Critical small/medium limb; or 8 surgical damage to Damaged limb
Hell Saw:
  timing: main action
  cost: 18 blood
  uses: 1 per fight
  effect: 18 saw damage; if Damaged/Critical target, 4–6 sever, 1–3 fail and enemy gains Rage
Claim the Cut:
  timing: main action
  cost: 10 blood
  uses: consumable
  effect: mark enemy limb; if severed this fight, guaranteed Clean Harvest
```

### 10.4 Enemies

#### Jeff v0.4

```yaml
id: E-001
name: Jeff
role: tutorial limb-acquisition enemy
blood: 70
body:
  head: 25
  torso: 45
  left_arm: 20
  right_arm: 30
  legs: 35
  core: 35
actions:
  desperate_swing:
    uses: arm
    damage: 10
    targets: player arm or torso
  cover_it:
    protects: threatened limb
  plead:
    trigger: two arms lost or 2 Plead Pressure or blood below 20
purpose: teach limb desire, marking, severing, bargain
```

#### Anna v0.4

```yaml
id: E-002
name: Anna
role: medical/stabilization enemy
blood: 80
body:
  head: Dazed Human Head
  torso: Stitched Torso
  left_arm: Human Left Arm
  right_arm: Crude Graft Arm
  legs: Human Legs
  core: Leaking Heart
actions:
  surgical_jab:
    uses: Crude Graft Arm
    damage: 8
    bleeding_roll: 5-6 normally, 4-6 if target already damaged
  black_stitch:
    stabilizes one damaged limb
  trade_offer:
    offers stabilization/medical item if player is bleeding, low blood, or threatening graft arm
  calm_guard:
    protects medically valuable limb
purpose: teach that body maintenance can be more valuable than more loot
```

---

## 11. Grafting Table v0.2

### Problem found in v0.1

The first table had one obvious best choice: **Properly seat the grafted arm**. That was emotionally satisfying but not strategically competitive enough.

### Table design goal

The table should force a meaningful choice between:

- securing current body,
- repairing vulnerability,
- buying future power,
- preserving blood,
- accepting debt.

### Table v0.2 Options

| Option | Cost/Gain | Effect | Purpose |
|---|---:|---|---|
| Properly Seat Grafted Arm | -15 blood | Stable Grafted Arm → Integrated Grafted Arm | lock in Jeff arc |
| Repair Damaged Human Torso | -18 blood | Damaged Human Torso → Human Torso | remove bleeding vulnerability |
| Strengthen Weak Legs | -12 blood | Weak Human Legs → Braced Human Legs | prepare for leg/knockdown enemy |
| Table Loan | +20 blood now, owe 30 after next fight | low-blood escape | prototype debt only |
| Leave Unchanged | 0 | preserve blood | conservative choice |

For simulator v0.1, exclude full shop, random inventory, favors, rituals, and large economy.

---

## 12. Mechanics / Logic / Item Scope Audit

### 12.1 Keep / Include Now

These directly protect or test the core loop.

| Feature | Classification | Reason |
|---|---|---|
| 6 body slots | Core MVP | Identity-defining, locked |
| Blood as health/currency/fuel | Core MVP | Central risk/reward |
| Limb integrity/states | Core MVP | Combat readability |
| Acting limb impairment | Core MVP | Makes limb targeting tactical |
| Clean sever gating | Core MVP | Prevents blood-hoarding exploit |
| Harvest quality | Core MVP | Makes how you cut matter |
| Emergency grafting | Core MVP | Completes fantasy quickly |
| Grafting table | Core MVP | Safer long-term body management |
| Focus | Core MVP | Supports readable intent/counterplay |
| Fast medical item tag | Core MVP | Prevents healing from wasting full turn |
| Plead Pressure | Core MVP | Makes body loss matter beyond HP |
| Unstable graft v0.4 | Core MVP | Gives emergency grafting consequence |
| Low-blood escape valve | Prototype-only core | Prevents unfair post-fight dead ends |
| Turn/event log | Core MVP for simulator | Required for test visibility |
| Seeded randomness | Core MVP for simulator | Reproducible test cases |
| Jeff | Core MVP | Teaches acquisition |
| Anna | Core MVP | Teaches maintenance |
| Grafting table choices | Core MVP | Tests post-fight economy |

### 12.2 Add Now

These are missing or underdefined and should be included in the next simulator because they directly support test quality.

#### A) Intent Clarity Level

```yaml
intent_clarity:
  vague: "enemy seems aggressive"
  partial: "enemy will use right arm"
  exact: "enemy will use right arm against your torso"
```

Reason: Focus, perception limbs, and UI readability need a measurable information state.

#### B) Action Source Tag

```yaml
action_source:
  body_slot: left_arm
  tool: Bone Scissors
  requires_limb_state: usable
```

Reason: acting limb impairment cannot work if actions do not know which limb/tool performs them.

#### C) Test Metrics Output

```yaml
metrics:
  final_blood
  blood_spent
  blood_gained
  limbs_clean_harvested
  limbs_stressed_harvested
  limbs_ruined
  player_limb_state_changes
  death_count
  panic_pulse_used
  fast_items_used
  focus_used
  plea_triggered
  graft_result
  table_choice
```

Reason: we need evidence, not vibes.

#### D) Body Change Summary

At the end of each fight/table, log:

```text
What changed about the player's body?
What new action/passive did they gain or lose?
What problem remains?
```

Reason: the central promise is body transformation.

#### E) Limb for Life

For simulator v0.1, include only one soft-loss valve:

```text
Limb for Life:
If Blood reaches 0 once during the approved tutorial scope,
sacrifice one seeded-random usable non-Core limb and survive at 12 Blood.
Then mark "Limb for Life used". Without an eligible sacrifice, Blood 0 is death.
```

Reason: death spiral was a major risk. The sacrifice makes continuation costly and
may be necessary to preserve a victory route without making Blood 0 non-lethal.

#### F) Tool Availability Reset Rule

```text
Bone Scissors and Hell Saw are 1 use per fight.
Consumables are consumed permanently.
```

Reason: without this, tools are ambiguous and balance results are invalid.

### 12.3 Add Later, Not Now

| Feature | Classification | Reason to delay |
|---|---|---|
| Curses | Important later | Too much complexity before base loop |
| Rotten flesh | Important later | Needs cleansing economy and visual language |
| Celestial judgment | Later content | Advanced risk/reward, not base test |
| Mechanical malfunction | Later content | Similar role to Unstable; avoid duplicate complexity |
| Multiple starting bodies | Later simulator v0.2 | First simulator should stabilize one baseline |
| Bone-Minotaur | Later test | Needs leg/torso counterplay after base simulator |
| Many-Eyed Flesh | Later enemy | Too many abnormal rules |
| Contracts beyond Claim the Cut | Later | Body/tool rules must stabilize first |
| Regrowth Vaccine | Later | Missing-limb strategy too advanced |
| Sell the Pain | Later | Might distort blood economy before baseline |
| Wrong Recipient | Later | Reaction timing not ready |
| Promise debt system | Later | Keep only Table Loan prototype debt |
| Table Favor | Later | Adds meta economy too early |
| Full shop inventory | Later | Scope creep |
| Dialogue system | Later | Use simple trade prompts for now |
| Meta progression | Later | Need first-run loop first |
| Procedural enemy order | Later | Use scripted sequence for validation |
| Random loot table | Later | Use deterministic rewards first |

### 12.4 Cut / Exclude for Now

| Feature | Reason |
|---|---|
| Full deck/card system | Cards may overpower body system |
| Large item roster | Obscures base mechanics |
| Full run map | Delayed by handoff scope |
| Procedural generation | Not needed to test combat loop |
| Final art/pixel assets | Premature |
| Animation/cut-ins | Unity/presentation later |
| Factions/lore expansion | Lore bloat risk |
| Complex NPC dialogue | Not needed for simulator |
| Multiplayer | Locked out of scope |
| Steam achievements/store systems | Release concern |
| Save/load | Not needed for tiny simulator |
| Build pipeline | Not until engine decision |
| Advanced RPG leveling | Could compete with limb-building |
| 100 limbs/content expansion | Scope explosion risk |

---

## 13. Item Audit

### 13.1 Keep Now

| Item | Status | Reason |
|---|---|---|
| Blood Bag | Keep, watch | Tests blood recovery; may be too strong |
| Clotting Cream | Keep | Tests Fast medical and bleeding |
| Bone Scissors | Keep | Clean precise sever tool |
| Hell Saw | Keep | Expensive dramatic sever tool |
| Claim the Cut | Keep | Creates limb desire and harvest guarantee |
| Black Stitch | Keep as Anna reward/treatment | Stabilization route after unstable graft |

### 13.2 Revise

#### Blood Bag

Current:

```text
Fast.
Gain 25 blood.
If Bleeding, gain only 15.
```

Simulator variants to test:

```text
Variant A: Gain 25 / 15 if bleeding.
Variant B: Gain 20 / 12 if bleeding.
Variant C: Gain 25, but cannot exceed 60 blood.
```

Recommendation: keep current for simulator v0.1, but run balance scenarios.

#### Black Stitch

Current role: stabilize damaged limb or remove Unstable as trade reward.

For simulator v0.1, include only:

```text
Anna treatment mode:
Cost 0 as trade reward.
Effect: remove Unstable OR stop Bleeding.
```

Do not include full combat-use Black Stitch yet.

### 13.3 Exclude for Now

| Item | Reason |
|---|---|
| Regrowth Vaccine | Too advanced; missing-limb builds are rare/special |
| Heal Rotten Flesh | Rot not in simulator |
| Wrong Recipient | Reaction timing not validated |
| Sell the Pain | Blood economy too fragile |
| Promise: Take This Later | Debt system not ready |
| Emergency Tourniquet | Similar to Clotting Cream; add only when arms/legs bleeding need differentiation |

---

## 14. Mechanic Audit by Player Decision

| Mechanic | Decision Created | Keep? |
|---|---|---|
| Focus | Spend blood for exact info? | Yes |
| Grip Strike | Which limb do I pressure? | Yes |
| Claim the Cut | Pay now to secure harvest later? | Yes |
| Hell Saw | Spend big for risky sever? | Yes |
| Bone Scissors | Spend small after setup for precise sever? | Yes |
| Blood Bag | Recover now or save? | Yes, watch |
| Clotting Cream | Stop bleeding or spend blood elsewhere? | Yes |
| Emergency graft | Immediate power vs risk/cost? | Yes |
| Unstable graft | Pay/plan around volatility? | Yes |
| Anna trade | More limbs or stabilize current body? | Yes |
| Grafting table | Integrate/repair/prepare/save blood? | Yes |
| Plead Pressure | Stop for bargain or continue greed? | Yes |
| Clean sever gate | Tool/blood commitment vs ruined part? | Yes |

Mechanics without enough decision right now:

| Mechanic | Problem | Action |
|---|---|---|
| Torso vulnerability | Mostly passive | Add visible bleeding-risk warnings |
| Weak Legs | Not tested yet | Keep but test with Bone-Minotaur later |
| Table Loan | Interesting but untested | Include as low-blood escape only |
| Surge | Can be irrelevant | Keep +2 blood fallback |

---

## 15. Simulator Spec v0.1

### 15.1 Goal

Build a small Python console simulator that can run scripted combat sequences and output readable logs/metrics.

It is not a game. It is a balance and validation tool.

### 15.2 Non-Goals

Do not implement graphics, animation, UI, Unity, save/load, map, procedural generation, full inventory UI, full dialogue, full AI, all enemies, all limbs, or final content.

### 15.3 Required Capabilities

```text
Body slots
Limb integrity/state
Blood
Actions
Tools
Enemy intent scripts
Focus
Fast medical items
Acting limb impairment
Clean sever logic
Harvest quality
Plead Pressure
Emergency graft
Unstable graft
Anna stabilization trade
Grafting table choices
Event logging
Scenario metrics
Seeded randomness
```

### 15.4 Data Model

#### Enum: Slot

```python
HEAD
TORSO
LEFT_ARM
RIGHT_ARM
LEGS
CORE
```

#### Recommended Limb State Model

Use primary state plus tags.

```python
primary_state: INTACT / DAMAGED / CRITICAL / DISABLED / SEVERED / MISSING / RUINED
tags: BLEEDING, GRAFTED, UNSTABLE, INTEGRATED, STABILIZED, MARKED, HANGING
```

#### Class: Limb

```python
id: str
name: str
slot: Slot
max_integrity: int
integrity: int
primary_state: LimbState
tags: set[LimbTag]
actions: list[str]
passives: list[str]
```

#### Class: Body

```python
slots: dict[Slot, Limb]
blood: int
active_effects: list[Effect]
panic_pulse_used: bool
limb_for_life_used: bool
```

#### Class: Combatant

```python
id: str
name: str
body: Body
blood: int
inventory: list[Item]
plead_pressure: int
role: player/enemy
```

#### Class: Action

```python
id: str
name: str
source_slot: Optional[Slot]
source_item: Optional[str]
cost_blood: int
timing: FOCUS / FAST / MAIN / REACTION
target_type: limb/self/enemy
effect: function
requires_usable_source: bool
can_clean_sever: bool
```

#### Class: EventLogEntry

```python
round_number: int
phase: str
actor: str
action: str
cost: int
target: str
result: str
blood_before: int
blood_after: int
state_changes: list[str]
tags: list[str]
```

#### Class: ScenarioMetrics

```python
final_blood: int
blood_spent: int
blood_gained: int
rounds_taken: int
focus_used_count: int
fast_items_used_count: int
clean_harvest_count: int
stressed_harvest_count: int
ruined_harvest_count: int
panic_pulse_used: bool
limb_for_life_used: bool
plea_triggered: bool
grafts_attempted: int
unstable_results: int
table_choice: str
final_body_summary: str
```

### 15.5 Core Functions

```python
apply_damage(target_limb, amount, damage_type, can_clean_sever=False)
update_limb_state(limb)
calculate_action_effectiveness(action, source_limb)
spend_blood(combatant, amount, reason)
gain_blood(combatant, amount, reason)
unstable_check(limb, rng)
resolve_focus(player, enemy_intent)
resolve_enemy_intent(enemy, script_state, player_state)
check_plead(enemy)
emergency_graft(player, harvested_limb, target_slot, rng)
apply_table_choice(player, choice)
```

---

## 16. Simulator Scenarios v0.1

| Scenario | Purpose | Pass Condition |
|---|---|---|
| S1 — Jeff Baseline Acquisition | Intended limb acquisition chain | Player ends with grafted arm, blood above 20 |
| S2 — Jeff No-Spend Exploit | Verify free attacks cannot clean harvest | Player may force surrender but gains no clean limb |
| S3 — Failed Hell Saw Spiral | Check death spiral and Limb for Life | Failure is dangerous but readable |
| S4 — Anna Stabilization Path | Test body maintenance | Player sometimes accepts stabilization |
| S5 — Anna Greed Path | Test risky limb greed | Player can get arm with danger; trade remains attractive |
| S6 — Mini-Campaign | Run Jeff → graft → Anna → table | Player ends with changed body and clear next pressure |
| S7 — Blood Bag Balance | Test Blood Bag variants | Blood Bag useful but not automatic best timing |

---

## 17. Acceptance Criteria for Simulator v0.1

The simulator is acceptable only if:

```text
1. Can run Jeff scenario from start to post-fight graft.
2. Can run Anna scenario with stabilization offer.
3. Can run mini-campaign scenario.
4. Logs every blood change.
5. Logs every limb state change.
6. Logs action source and acting limb impairment.
7. Distinguishes Clean/Stressed/Ruined harvest.
8. Supports Unstable v0.4 checks.
9. Supports Grafting Table v0.2.
10. Outputs scenario metrics.
11. Uses deterministic seed for repeatable tests.
12. Has no UI/Unity/art dependencies.
```

---

## 18. Requirements Traceability Matrix

| Requirement ID | Requirement | Source | Priority | Module | Acceptance Criteria | Test |
|---|---|---|---|---|---|---|
| RQ-001 | Player has 6 body slots | Locked design | Critical | BodySystem | slots exist and hold limbs | all |
| RQ-002 | Blood is health/currency/fuel | Locked design | Critical | BloodSystem | Blood can be spent/gained; zero causes death unless Limb for Life resolves | all |
| RQ-003 | Limb damage changes state | Core combat | Critical | LimbStateSystem | thresholds update states | all combat |
| RQ-004 | Acting limb state modifies actions | Paper tests | Critical | ActionResolver | damaged/critical reduce effect | Jeff/Anna |
| RQ-005 | Basic attacks cannot clean harvest | Exploit test | Critical | HarvestSystem | Grip Strike to 0 creates Ruined/Disabled | Jeff exploit |
| RQ-006 | Clean sever requires commitment | Combat rules | Critical | SeverSystem | tools/contracts can clean sever | Jeff baseline |
| RQ-007 | Harvest quality affects grafting | Paper tests | High | HarvestSystem | stability varies by quality | graft tests |
| RQ-008 | Emergency graft can be Unstable | Core grafting | Critical | GraftSystem | stability roll applies | post-Jeff |
| RQ-009 | Unstable v0.4 creates choices | Forced test | High | GraftSystem | Twitch/Ache/Surge resolve | Anna |
| RQ-010 | Focus reveals intent pre-action | Focus revision | High | IntentSystem | focus does not consume main action | Anna |
| RQ-011 | Fast medical items exist | Medical test | High | ItemSystem | 1 Fast item before action | Anna |
| RQ-012 | Plead Pressure triggers bargains | Jeff test | High | EnemyStateSystem | plea at threshold | Jeff |
| RQ-013 | Grafting table offers meaningful choices | Mini-campaign | High | TableSystem | table choices alter body/blood | mini-campaign |
| RQ-014 | Logs support review | Skill requirement | Critical | Logger | readable event log and metrics | all |
| RQ-015 | Seeded randomness | Simulator need | High | RNGService | repeatable outcomes | all |

---

## 19. Module Contracts

### BodySystem

Purpose: own player/enemy body slots and limb references.  
Does not own action resolution, enemy intent, or UI.  
Tests: missing right arm disables right-arm actions; grafting adds Guard Flesh; integrated graft remains stable.

### LimbStateSystem

Purpose: convert integrity and tags into readable limb states.  
Tests: 30 → 20 becomes Damaged; 20 → 10 becomes Critical; basic attack to 0 becomes Ruined/Disabled; clean tool to 0 becomes Severed/Clean.

### BloodSystem

Purpose: track blood as health/currency/fuel.  
Tests: costs reduce Blood; gains increase Blood; Panic Pulse triggers below 25; Limb
for Life may prevent Blood-0 death once; otherwise death finalizes.

### ActionResolver

Purpose: resolve player/enemy actions.  
Tests: damaged acting limb reduces damage; disabled source cancels action; Focus reveals intent before main action; Fast item does not consume main action.

### HarvestSystem

Purpose: determine Clean, Stressed, or Ruined harvest.  
Tests: Claim guarantees Clean if severed; Grip Strike alone cannot Clean; Bone Scissors on Critical creates Clean; ruined marked limb can use discounted salvage.

### GraftSystem

Purpose: apply harvested limbs to player body.  
Tests: Clean Harvest has 1/6 Unstable; Stressed Harvest has 2/6 Unstable; Unstable check resolves Twitch/Ache/Surge; table can integrate graft.

### IntentSystem

Purpose: represent enemy visible intent and Focus upgrades.  
Tests: vague/partial/exact intent; Focus converts to exact; damaged head affects Focus.

### EnemyScriptSystem

Purpose: provide simple scripted enemy behavior for simulator.  
Tests: Jeff protects/uses marked limb; Jeff pleads after arms lost; Anna offers stabilization when player has Unstable/Bleeding.

### TableSystem

Purpose: apply post-fight grafting table options.  
Tests: integrate arm costs 15; repair torso costs 18; strengthen legs costs 12; table loan works as low-blood valve.

### Logger/MetricsSystem

Purpose: make simulations inspectable.  
Tests: every action logs cost/result; every blood change logs before/after; every limb state change logs old/new; scenario summary prints metrics.

---

## 20. Risk Register v0.5

| Risk | Category | Probability | Impact | Warning Signs | Mitigation | Owner | Status |
|---|---|---:|---:|---|---|---|---|
| Blood hoarding returns | Design | Medium | Very High | no-spend wins with good body reward | clean sever gate, simulator exploit tests | Systems | Controlled |
| Blood Bag too strong | Balance | High | Medium | always best early use | variant tests | Systems | Watch |
| Death spiral | Design | Medium | Very High | player dies after one failed roll | Limb for Life, Fast medical, warnings | Systems | Controlled |
| Limb system becomes stat gear | Design | Medium | Very High | limbs only add numbers | every limb needs action/passive/tradeoff | Design | Watch |
| Table choices obvious | Design | High | Medium | always integrate arm | add torso/legs/loan competition | Design | Active |
| Anna path under-tested | Design | Medium | Medium | only stabilization path validated | Anna greed scenario | QA | Open |
| Torso vulnerability invisible | UX | High | Medium | player forgets torso risk | log warnings / future UI | UX | Active |
| Simulator overbuild | Production | Medium | High | starts becoming full game | strict non-goals | Producer | Watch |
| Premature Unity | Production | High | Very High | wants visuals before numbers | simulator gate | Producer | Controlled |
| Scope creep | Production | High | Very High | new enemies/items/lore before simulator | scope audit | Producer | Controlled |

---

## 21. Chain of Proof

### Feature: Emergency Grafting

```text
User requirement: Player can graft harvested limbs after combat.
Design decision: Emergency grafting is immediate but risky.
System/module: GraftSystem.
Implementation task: implement emergency_graft(player, harvested_limb, target_slot).
Acceptance criteria: Clean Harvest costs 12 blood and rolls stability; body slot updates; new action becomes available.
Test case: Jeff baseline acquisition.
Result: Paper test passed. Simulator pending.
Status: Approved for simulator.
```

### Feature: Clean Sever Gating

```text
User requirement: Player should cut useful limbs but blood spending must matter.
Design decision: Basic attacks cannot clean harvest alone.
System/module: HarvestSystem / LimbStateSystem.
Implementation task: differentiate clean sever from ruined disable.
Acceptance criteria: Grip Strike to 0 does not produce Clean Harvest; Bone Scissors / Hell Saw / Claim can.
Test case: Jeff no-spend exploit.
Result: Paper retest passed.
Status: Approved for simulator.
```

### Feature: Anna Medical Trade

```text
User requirement: Not every encounter should be simple butchering.
Design decision: Anna can offer stabilization in exchange for sparing limb.
System/module: EnemyScriptSystem / TradeSystem.
Implementation task: Anna trade triggers when player has Unstable/Bleeding or Anna arm is threatened.
Acceptance criteria: Player can accept stabilization and end fight; player can reject and pursue limb.
Test case: Anna stabilization path and Anna greed path.
Result: Stabilization paper test passed. Greed path still needs simulator/paper test.
Status: Partially validated.
```

---

## 22. Recommended Sprint 0.5 Task List

### Task 0.5.1 — Approve Simulator Spec

Output: Simulator Spec v0.1 approved or revised.  
Acceptance: Scope is Jeff + Anna + Table only. No Unity. No final art. No extra enemies.

### Task 0.5.2 — Implement Data Skeleton

Output: Python files/classes for Body, Limb, Action, Item, Combatant.  
Acceptance: Can instantiate player S-001, Jeff, Anna. No combat required yet.

### Task 0.5.3 — Implement Limb/Blood Systems

Output: Damage thresholds, blood spend/gain, Panic Pulse.  
Acceptance: script tests pass for state changes and blood triggers.

### Task 0.5.4 — Implement Action Resolver

Output: Grip Strike, Focus, Guard Flesh, Fast item timing.  
Acceptance: can resolve one round with logs.

### Task 0.5.5 — Implement Harvest/Graft

Output: Clean/Stressed/Ruined harvest and emergency graft.  
Acceptance: Jeff Right Arm can be harvested and grafted.

### Task 0.5.6 — Implement Enemy Scripts

Output: Jeff and Anna scripted behavior.  
Acceptance: Jeff baseline and Anna stabilization scenario run.

### Task 0.5.7 — Implement Table

Output: table choices apply blood/body changes.  
Acceptance: mini-campaign reaches table and integrates graft.

### Task 0.5.8 — Run Scenario Batch

Output: Scenario metrics report.  
Acceptance: all 7 scenarios run with deterministic seed.

### Task 0.5.9 — Review Gate

Output: Simulator Results Review v0.1.  
Decision: revise rules, build tiny playable text prototype, or prepare Unity graybox plan.

---

## 23. Stop / Revise / Continue Gate for Simulator

### Continue to tiny playable text prototype if

```text
Jeff baseline succeeds consistently.
No-spend exploit remains blocked.
Anna stabilization and greed paths both work.
Mini-campaign ends with meaningful body change.
Blood Bag is not always optimal.
Death rate is dangerous but not absurd.
Table choices vary across scenarios.
```

### Revise simulator rules if

```text
same action dominates every scenario.
blood spending feels irrational.
player ends too rich or too dead.
Unstable is ignored or hated.
Anna offer is always accepted or always rejected.
table option 1 is always best.
```

### Do not proceed to Unity if

```text
simulator logs are confusing.
body changes do not alter later fights.
blood economy is unstable.
harvest/graft choices feel automatic.
we still need major combat rule changes.
```

---

## 24. Final Inclusion / Exclusion Verdict

### Include in next simulator

```text
Body slots
Blood
Limb integrity and states
Focus
Grip Strike
Guard Flesh
Brace
Panic Pulse
Blood Bag
Clotting Cream
Bone Scissors
Hell Saw
Claim the Cut
Black Stitch as Anna treatment
Jeff
Anna
Grafting Table v0.2
Unstable v0.4
Harvest quality
Plead Pressure
Limb for Life / low-Blood death prevention
Event logs
Metrics
Seeded randomness
```

### Exclude from next simulator

```text
Unity
graphics
animation
final art
map
procedural generation
full card/deck system
large inventory
additional enemies
curses
rot
celestial mechanics
mechanical malfunction
full debt economy
dialogue system
meta progression
save/load
Steam/platform systems
multiplayer
```

---

## 25. Final Producer Recommendation

The project is now ready for **one narrow digital step**:

```text
Build Combat Loop Simulator v0.1.
```

The simulator should answer:

```text
Do these rules survive repeated runs and different player strategies?
```

It should not try to feel like the final game yet.

The next correct file after implementation is:

```text
archive/results/Game_att2_Combat_Simulator_Results_v0_1.md
```

Only after simulator results pass should the project consider:

```text
Unity graybox prototype plan
```

Not before.


---

## 26. Source Precedence and Contradiction Protocol

Codex must use this precedence when implementation sources differ:

```text
AGENTS.md
→ this Development Master v0.6
→ Combat Rules v0.5
→ Simulator Technical Spec v0.2
→ config values
→ Test Plan / Acceptance
→ supporting evidence/history
```

A numeric value in config may override a duplicated tunable value in prose, but it may not change the meaning of a mechanic. Do not silently invent a product decision. Use the most reversible interpretation, preserve configuration, and log the issue.

## 27. Resolved Implementation Ambiguities

### Enemy blood versus limb integrity

They are separate resources, but the owner approved wound-class-driven Blood loss as
the future integration rule. Simulator v0.5 still does not automatically reduce Blood
from ordinary limb damage because wound mappings and values are not approved. Body
loss currently changes action availability, Plead Pressure, or special surrender
conditions. Codex must not invent the missing wound table.

### Disabled versus severed

Disabled means attached but unusable. Severed means detached. Ruined means unsuitable for normal emergency grafting. A free basic attack reducing integrity to zero creates Disabled/Ruined unless a clean-sever enabler applies.

### Jeff surrender after free arm destruction

Jeff has a special **combat incapacity surrender** if both arms are Disabled, Ruined, or Severed. This can end the encounter, but ruined arms remain low-value and do not become Clean Harvest. This is distinct from generic Plead Pressure.

### Round timing

Focus and one Fast item occur before the player's main action. Panic Pulse is checked immediately after any blood transaction or damage that crosses below 25. It may trigger from voluntary spending. Enemy action is canceled if its required source becomes unusable before resolution.

### Item persistence

Blood Bag, Clotting Cream, and Claim the Cut are consumable across the mini-campaign. Bone Scissors and Hell Saw refresh to one use at the start of each fight. This is a simulator rule, not final fiction.

### Black Stitch scope

In simulator v0.1, Black Stitch is implemented primarily as Anna's trade/treatment effect. Do not build a general inventory spell system for it.

## 28. New Requirements for Codex Handoff

| ID | Requirement | Priority |
|---|---|---|
| RQ-016 | All randomness flows through injected seeded RNG | Critical |
| RQ-017 | CLI supports named scenarios and batch strategies | High |
| RQ-018 | Simulator generates human-readable and machine-readable results | High |
| RQ-019 | Config/data validation rejects invalid slots, negative costs, and impossible integrity | High |
| RQ-020 | No domain system prints directly; structured events are rendered separately | High |
| RQ-021 | Completion report maps requirements to tests and results | Critical |

## 29. Codex Implementation Gate

Paper-test approval for Encounter 3 is not an implementation gate. Additional encounter definitions may exist in controlled documentation, but no Warden source, runtime YAML, simulator scenario, production content, or Unity work is authorized before a separate owner-approved runtime gate.

Codex may implement the simulator now. Codex may not:

```text
rebalance values silently
add production UI
choose Unity
add more enemies/items
turn simple scripts into a generic behavior-tree framework
implement full debt/meta-progression/save systems
claim simulator metrics prove fun
```

## 30. Required Output After Codex Work

```text
source code
unit/integration tests
scenario and batch CLI
archive/results/Game_att2_Combat_Simulator_Results_v0_1.md
Codex completion report
known gaps and reversible recommendations
```
