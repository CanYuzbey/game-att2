# Game att2 — Simulator Content Catalog v0.1

This file defines only content required for simulator v0.1. YAML is authoritative for tunable values.

## Starting body S-001 — Torn but Stable

- Blood: 85
- Head: Human Head
- Torso: Damaged Human Torso
- Left Arm: Human Left Arm
- Right Arm: Missing Right Arm placeholder
- Legs: Weak Human Legs
- Core: Human Heart

Purpose: immediate desire for Jeff's right arm while retaining enough agency and blood for tutorial decisions.

## Player body parts

### Human Head

- Head, max integrity 25.
- Provides Focus.

### Damaged Human Torso

- Torso, max integrity 45.
- Tag/passive: increased Bleeding susceptibility; simulator should expose the rule in logs.

### Human Left Arm

- Arm, max integrity 30.
- Provides Grip Strike.

### Grafted Human Right Arm

- Arm, max integrity 30.
- Provides Guard Flesh.
- Initially Grafted; may also be Unstable, Stable, or Integrated through tags/state.

### Weak Human Legs

- Legs, max integrity 35.
- Provides `Brace — Manual Stance`, a player-selected one-round Knockdown posture.

### Braced Human Legs

- Retains manual Brace.
- Provides one separate automatic Knockdown-prevention charge per encounter.

### Human Heart

- Core, max integrity 35.
- Provides Panic Pulse.

## Items/tools/contracts

- Blood Bag: Fast consumable, +25 or +15 when Bleeding.
- Clotting Cream: Fast consumable, cost 8, remove one Bleeding.
- Claim the Cut: main consumable, cost 10, mark one limb.
- Bone Scissors: one use per fight, cost 6, precision extraction.
- Hell Saw: one use per fight, cost 18, risky large-limb sever.
- Black Stitch treatment: Anna trade effect only in v0.1.

## Jeff

Role: teach acquisition and action-limb impairment.

- Blood 70.
- Head 25.
- Torso 45.
- Left Arm 20.
- Right Arm 30.
- Legs 35.
- Core 35.

Actions:

- Desperate Swing, source arm, base 10, target player arm or torso.
- Cover It, one-round enemy posture. It must be selected again to recur; protection
  target/effect/source and its trade-off against Brace are approved on paper in
  document 31, but runtime remains deferred, so the current CLI does not execute it.
- Plead/incapacity surrender.

Rewards/path:

- clean desired right arm if extracted correctly;
- lower-quality left arm depending on removal;
- 25 blood offer on plea;
- post-fight graft/preserve/sell decisions.

## Anna

Role: teach maintenance and non-butchering value.

- Blood 80.
- Dazed Human Head 25.
- Stitched Torso 45.
- Human Left Arm 30.
- Crude Graft Arm 30.
- Human Legs 35.
- Leaking Heart 35.

Actions:

- Surgical Jab, source Crude Graft Arm, base 8, Bleeding roll.
- Black Stitch, apply Stabilized.
- Calm Guard, protect medical limb.
- Trade Offer, stabilize player/stop bleeding for sparing arm.

## Grafting Table v0.2

- Integrate Grafted Arm: -15 blood.
- Repair Damaged Torso: -18 blood.
- Strengthen Weak Legs: -12 blood.
- Table Loan: +20 now and record debt 30 after next fight.
- Leave unchanged: 0.

## Excluded content

Bone-Minotaur, Many-Eyed Flesh, Octopus Fingers, Predator Eyes, angelic parts, Rotten Core, Mechanical Heart, curses, rot, Regrowth Vaccine, Wrong Recipient, Sell the Pain, full Promise debt, shops, random loot, meta unlocks.

Document 33's `POISON`, `BURN`, Venomous Right Arm, and Needle Jab are illustrative
architecture fixtures only. They are not additions to this content catalogue.
Document 35's `RANGE_DIAGNOSTIC_MAIN` is also a neutral paper fixture only. It is not
an action, card, item, ability, or addition to this content catalogue.

Document 36 maps existing treatment, Blood-restoration, extraction, salvage, graft,
and table content into Package B timing and atomicity for paper review only. Its
TAC-B fixtures are neutral acceptance cases, not actions, cards, items, abilities,
characters, or additions to this catalogue. Runtime content remains unchanged.

Document 37 maps the existing tutorial-scope Limb for Life affordance into Package A
catastrophic-survival causality for paper review only. Its CIS-A fixtures, evidence
marker examples, and exact-choice prompt are not characters, cards, items, abilities,
wounds, routes, or additions to this catalogue. Runtime content remains unchanged.
