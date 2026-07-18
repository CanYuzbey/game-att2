# Game att2 Encounter 3 Facilitator Policy Cards v0.1

Facilitator-only. Never reveal future priority decisions. Apply the systemic causal loop after every mutation.

## Common validation card

1. Derive intent from assigned policy and current state.
2. Confirm source, requirement, target, and effectiveness.
3. Announce visible intent; Focus may reveal exact source and target.
4. Resolve the player's legal action.
5. Recompute mutated zone states and Warden capabilities.
6. Revalidate intent. If invalid, cancel and log; choose no replacement this phase.
7. If valid, resolve the scaled action and player consequences.
8. Check player collapse, Warden incapacity, and eight-round cap.

Never infer horns, hooves, organs, weapon targeting, Bleeding, surrender, escape, death, or an unpublished fallback.

## Policy A — Momentum Priority

```text
if player is Knocked Down and legs usable: Hoof Follow-up
else if legs usable: Charge
else if right arm usable: Butcher Strike
else: Warden combat-incapacitated
```

## Policy B — Butcher Priority

```text
if right arm usable: Butcher Strike
else if player is Knocked Down and legs usable: Hoof Follow-up
else if legs usable: Charge
else: Warden combat-incapacitated
```

## Action reference

| Action | Source | Base | Target/rule |
|---|---|---:|---|
| Charge | Legs | 12 | Legs; scale damage; Brace/Anchored may prevent Knockdown but not damage |
| Hoof Follow-up | Legs | 14 | Torso; legal only while player Knocked Down |
| Butcher Strike | Right arm | 12 | Damaged torso → lowest-integrity usable arm → torso; Guard only if limb-targeting |

Intact/Damaged/Critical effects are 100%/75%/50%. Unusable sources remove the action. Record each mutation, scaling decision, cancellation, lost capability, and ending check.
