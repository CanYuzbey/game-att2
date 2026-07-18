# Game att2 Encounter 3: Minotaur Warden Paper Test v0.1

> **SUPERSEDED FOR FUTURE MODERATED TESTING.** Preserve as historical designer-walkthrough evidence only. Fixed sequences, Bleeding, horns, four-round survival resolution, and its old fixture must not be used for P01–P08. Use `Game_att2_Encounter_3_Bounded_Causal_Paper_Spec_v0_2.md`.

Status: canonical paper-design packet only. This is not Python, Unity, loot, final lore, or final balance.

## Purpose

Test whether the post-Anna table choice changes a readable 3-4 round fight without making one option automatic. The Warden is a heavy, deliberate jailer carrying a butcher's cleaver; its identity is provisional presentation, not finalized lore.

## Player preparation

Use the legal post-table state selected from the seed-42 campaign baseline: S-001 has a grafted right arm, damaged torso, weak legs, Human Heart, one Blood Bag, and one Clotting Cream unless a listed table choice changes that state. Record exact Blood after the table.

| State | Table choice | Blood | Body difference | Classification |
|---|---|---:|---|---|
| 1 | Integrate arm | 25 | Integrated right arm, damaged torso, weak legs | naturally reachable |
| 2 | Repair torso | 22 | grafted arm, repaired torso, weak legs | controlled diagnostic |
| 3 | Strengthen legs | 28 | grafted arm, damaged torso, Braced legs, one Brace | controlled diagnostic |
| 4 | Leave | 40 | grafted arm, damaged torso, weak legs | naturally reachable |
| 5 | Table Loan then Leave | 60, debt 30 | same weaknesses, settlement after fight | controlled diagnostic |

## Warden sheet

| Field | Value |
|---|---|
| Enemy | Minotaur Warden |
| Body/reward | No health, loot, harvest, or limb rules are tested in this packet |
| Fight target | Resolve four Warden attack rounds, then settle Table Loan if present |
| Player victory for this test | Finish four rounds without collapse; no reward is granted |

## Action kit

| Action | Telegraph | Resolution | Encounter-local values and reason |
|---|---|---|---|
| Warden's Charge | lowers horns, stamps once | Roll d6; 4-6 attempts successful Knockdown. Apply approved Brace/Downed/Stand rules. Then deal 6 limb damage to Legs. | `4+`: matches existing d6 success language. `6`: below Jeff's 10 and Anna's 8 because Knockdown is the primary pressure. Revise if Downed is absent or repeated inactivity dominates. |
| Butcher's Cleave | raises visible cleaver toward torso | Deal 8 torso damage. Roll Bleeding using existing rule: 5-6 normally, 4-6 if torso is Damaged/Critical. | `8`: existing Surgical Jab reference. Revise if Repair cannot change Bleeding/medical decisions. |
| Horn Hook | turns horn toward grafted right arm | Deal 8 right-arm damage. Player may use Guard Flesh before resolution. Existing Unstable check still applies before player choice. | `8`: existing attack reference. Revise if Guard is always unaffordable or arm pressure is irrelevant. |

No movement, positioning, bonus damage against Downed, restraint, disarm, armor, new injury, or new status is used.

## Attack scripts

**Script A:** Round 1 Charge, Round 2 Cleave, Round 3 Horn Hook, Round 4: Charge if no Downed occurred; Horn Hook if torso is Bleeding/Critical; otherwise Cleave.

**Script B:** Round 1 Horn Hook, Round 2 Charge, Round 3 Cleave, Round 4: Cleave if torso is Damaged/Critical; otherwise Charge.

Use the same d6 sequence for every matched table path. Suggested matched rolls: `Charge 5, Bleeding 5, Unstable 1 then 5, Charge 5`. Script B shifts the same rolls to its actions. The Known variant reveals pressure categories but never exact numbers/order; Unknown reveals no Warden information until table choice is locked.

## Rules reminders

- Brace automatically cancels the first otherwise-successful Knockdown per encounter.
- Unresolved Knockdown applies Downed. A Fast item may be used; the next normal action must Stand and cannot also attack.
- Damaged/Critical torso is more susceptible to the existing Bleeding roll. Clotting Cream removes one Bleeding tag for 8 Blood. Blood Bag gains 15 while Bleeding, otherwise 25.
- Guard Flesh costs 4 Blood, uses the right arm, and halves the next limb-targeting damage.
- Integrated grafts avoid normal Unstable checks. Do not invent an additional arm rule.

## Log sheets

### Round log

| Round | Telegraph understood? | Warden action | Player Fast | Player normal action | Knockdown/Brace | Bleeding | Blood end | Limb changes | Notes |
|---:|---|---|---|---|---|---|---:|---|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |

### Blood and limb log

| Event | Before | Delta | After | Reason / slot |
|---|---:|---:|---:|---|
| | | | | |

| Slot | Start integrity/state/tags | End integrity/state/tags | Key transition |
|---|---|---|---|
| Torso | | | |
| Right arm | | | |
| Legs | | | |

## Evaluation

Continue to human paper test only when the three telegraphs are distinguishable, each preparation has an observable role, Leave remains defensible under uncertainty, Loan remains distinct after settlement, and the packet resolves in 3-4 primary rounds. Revise if a path is obvious in both information variants, if Stand causes repeated inactivity, or if Cleave overwhelms every other decision. Pivot only if the three dimensions cannot be tested without prohibited systems.
