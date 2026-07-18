# Game att2 Encounter 3 Bounded Causal Paper Specification v0.2

Status: current owner-approved moderated paper-test specification. Non-canonical evidence only. Runtime and Unity blocked.

## Purpose and scope

Test whether the Jeff → graft → Anna → table body changes legal or effective responses to Knockdown and direct pressure; whether source damage immediately changes Warden capabilities; whether more than one strategy remains viable; and whether facilitators can resolve from state without narrative invention.

Not tested: loot, grafting Warden zones, species anatomy, organs, penetration, death, surrender, bargaining, escape, personality, final balance/AI/pacing, or production content.

## Fixture and table

Use `E3-PRETABLE-01` exactly as recorded in `Game_att2_Encounter_3_Owner_Decision_Reconciliation_v0_1.md`. Offer only Integrate (25 Blood), Repair (22), Strengthen (28), or Leave (40). Table Loan and all medical items are unavailable. Strengthened legs gain the paper-only Anchored rule; Brace remains a once-per-fight main action and protects its round.

## Warden target zones

| Zone | Maximum integrity | Sources | Paper role |
|---|---:|---|---|
| Right arm | 30 | Butcher Strike | Offensive source |
| Legs | 40 | Charge; Hoof Follow-up | Offensive source |
| Torso | 60 | none | Structural incapacity target |

These are mechanical target zones, not complete anatomy. Horns, individual hooves, organs, arteries, hidden weak points, separate weapon targeting, supernatural durability, and biological permissions are absent.

## Source-state rules

Apply existing effectiveness: Intact 100%, Damaged 75%, Critical 50%, and Disabled/Ruined/Severed unavailable. Use the existing threshold model and rounding convention.

After every mutation: recalculate the zone; recalculate capabilities; revalidate declared intent; cancel an invalid intent with no same-phase replacement; log the cancellation and lost capability; then recalculate encounter viability. Drama and assigned policy never override invalid state.

## Player interactions

- **Grip Strike:** normal damage; never Clean Harvest; zero integrity becomes Disabled/Ruined and immediately removes sourced actions.
- **Hell Saw:** existing cost, validation, and success roll; right arm and legs are Large for this test; successful sever removes sourced actions and logs `Severed — Non-Harvest Test Outcome`; no reward.
- **Bone Scissors:** visible but has no valid Warden target; explain through existing size rules.
- **Guard Flesh:** existing rule against the next limb-targeting Warden damage; never prevents Knockdown by itself.
- **Focus:** reveals the current exact Warden action source and player target; never future priority decisions.

## Knockdown

Successful Knockdown adds Knocked Down. Focus remains legal on the next player turn; no Fast item exists in this fixture. The next main action must be Stand, which removes Knocked Down and cannot also attack, use a tool, Guard, or Brace. Knockdown is prevented by active Brace, unused Anchored, disabling Warden legs before resolution, or a later explicitly approved effect. No movement/positioning system follows.

## Warden actions

| Action | Source | Base damage | Target/requirement | Resolution |
|---|---|---:|---|---|
| Charge | Legs | 12 | Player legs | Validate source; scale damage; resolve Brace/Anchored; apply remaining damage; apply Knockdown if unprevented; recompute capabilities |
| Hoof Follow-up | Legs | 14 | Player torso; player must be Knocked Down | Illegal unless Knocked Down and legs usable; scale/apply damage; recompute |
| Butcher Strike | Right arm | 12 | Damaged torso, else lowest-integrity usable arm, else torso | Derive target from state; scale/apply damage; Guard may reduce limb-targeting damage; recompute |

No action adds Bleeding in v0.2.

## State-aware policies

**A — Momentum:** if player is Knocked Down and legs usable, Hoof Follow-up; else if legs usable, Charge; else if right arm usable, Butcher Strike; else combat-incapacitated.

**B — Butcher:** if right arm usable, Butcher Strike; else if player is Knocked Down and legs usable, Hoof Follow-up; else if legs usable, Charge; else combat-incapacitated.

At each Warden response, derive intent from current state, expose visible intent, allow the player action window under the approved round procedure, and revalidate after player mutations. A canceled intent receives no same-phase replacement.

## Resolution

- **Player collapse:** existing Blood/collapse rules, with no hidden rescue.
- **Warden combat incapacity:** torso is Disabled/Ruined/Severed, or both legs and right arm are unusable. This is bounded inability to continue, not death.
- **Unresolved:** stop after eight completed rounds and record `UNRESOLVED — ROUND CAP`; this is an operational boundary, not victory.

No surrender, plea, escape, retreat, bargain, reward, execution, death confirmation, or irrational resistance is represented.

## Conditions and matrix

Known receives the approved pre-table statement and capability summary in the participant cards. Unknown receives only its approved statement until table choice; normal visible intent is never hidden after combat begins.

| Participant | Threat | Policy |
|---|---|---|
| P01 | Known | A |
| P02 | Known | A |
| P03 | Known | B |
| P04 | Known | B |
| P05 | Unknown | A |
| P06 | Unknown | A |
| P07 | Unknown | B |
| P08 | Unknown | B |

Use complete state/capability logs. A material deviation is `CONTAMINATED — DO NOT INCLUDE IN AGGREGATE CONCLUSION` but remains diagnostic evidence.
