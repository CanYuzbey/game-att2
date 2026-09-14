# Game att2 — Deck, Brain, and Actions

Status date: 2026-09-15

**CURRENT LIVING PAPER AUTHORITY — Z48/A fixture v0.1.** Owner controls inclusion
and source/target/risk; Brain modifies a declared access relationship, never chooses
cards or fabricates sources. No runtime or human-play validation.

## P06 — Eight instances, four Attention positions

Z25/B: active deck exactly8, Attention4, equal-weight draw without replacement among
instances not already in Attention. Unplayed positions remain across rounds.
Only Spent/Invalid positions refill. Spent cards return to the eligible deck after
round cleanup, allowing later redraw but no extra same-round action. Permanent
source-invalid cards remain visible in the library and leave the refill pool;
temporary Dormant cards occupy their current Attention positions.

If fewer eligible instances exist, show empty positions without substitution.
No full-hand automatic refresh or one-card retain/discard-all rule applies.
A chosen paid redraw occurs at most once before commitments in a round:
remove a chosen unspent Attention instance, draw uniformly among other eligible
instances outside Attention, then return the removed instance to the deck pool.
No other candidate -> illegal, no charge. Default cost2 Blood; Brain's once-per-
encounter first redraw costs1. It spends no Main/Preparation and cannot create a
second redraw. It cannot refresh a Spent card for another Main that round.

| ID/type | Starting copies | Opportunity | Exact source/minimum | Blood cost | Full/Strained effect | Target/tier |
|---|---:|---|---|---:|---|---|
| P-L Punch | 1 | Main | Exact normal Left Arm, >30%, free CanPunch | 2 | 8/6 structural | One living region/horn, Routine |
| P-R Punch | 1 | Main | Exact normal Right Arm, >30%, free CanPunch | 2 | 8/6 | Same, Routine |
| K-A / K-B Kick | 2 | Main | Legs >30%, free | 3 | 12/9 | Same, Committed |
| H-A / H-B Headbutt | 2 | Main | Head >30%, free | 3 | 10/7 | Same, Critical |
| B Brace | 1 | Preparation | One exact free guarding Arm >30% | 1 | GuardFactor1.00->.80 or .80->.80 for next legal Block | Own named Arm; no damage/Will |
| F Feint | 1 | Preparation | Exact attack-capable Head/Arm/Legs >30% | 1 | Next differently sourced Main at named target +3 structural, once | One named target; no standalone damage |
| G Clamp Grip | 0, one learned swap | Main | Exact free Right CanGrip arm >30% | 2 | No base structural damage; hold named enemy Arm's predeclared same-source ordinary Main through response | Enemy Arm only, Committed; never Charge |

All attacks/Grip expose +2 Open/+4 Major source Wound Stress until Stabilized.
No attack-side QTE. Costs pay when execution begins; a canceled unstarted action
pays nothing. Outgoing technique cue categories for NPC defense are Punch/Headbutt/
Grip Yellow, Kick Red; their tier drives successful NPC Parry loss where legal.
NPC Parry cannot answer Kick's Red. A Brace-block's lower factor does not waive
activation Blood or permit an illegal guarding source.

An NPC's successful Parry against Grip prevents its contact/hold; a miss permits
the declared hold. The witness records that miss explicitly. No automatic Grip
success or source replacement is assumed.

## Continuing deck and Brain ownership

Body owns physical permission, knowledge owns learned possibilities, the player
owns active deck composition, ordinary draw owns imperfect access, and Brain owns
an inspectable deterministic modifier of the current hand/body relationship.
Each future Brain rule must expose trigger, legal condition, affected relationship,
benefit, cost/risk, duration, preview and result. It cannot choose/weight/filter/draw
cards, guarantee access, create unknown techniques, add Main or fabricate a missing
source. Current Bifocal modifies the cost of an already player-chosen redraw only.
Body/wounds, technique knowledge, deck, Brain, attempt/meta and narrative knowledge
remain separate. Instability is state-derived, not an approved new global meter.
Poker ranks, suits and generic hand-score multipliers remain outside the doctrine.

The starting six source-valid expressions are Punch-L, Punch-R, Kick, Headbutt,
Brace and Feint across8 instances. G adds one learned expression; no rarity,
upgrade, random reward screen or further technique catalogue is implied.
One-for-one table swaps retain deck8. At least two compatible attack source families
must remain; removing a sole left-arm attack while the Right Arm is incompatible
fails elective deck validation. Lost-body incompatibility remains visible even if it
later violates that elective construction floor.

Cards map physical permissions: clamp has CanGrip/CanGuard/CanParry/CanTool, not
CanPunch. G2 occupancy temporarily prevents same-arm tool handling while held;
there is no G1 permanent fine-tool loss when the clamp is free.
A graft does not teach or auto-slot G; default P-R loses its source permission.
Mara's ordinary arm re-enables P-R but invalidates G. Library knowledge is unchanged.
Known incompatible G may be inspected as Dormant; no illegal G is drawn as a legal
replacement. Exactly one visible table exchange is allowed per resolved ordinary
encounter, tracked across reentry. Reopening a table does not reset it.

## P09 — One Concept and one fixed Brain

**Concept achievement:** successfully Parry one legal Committed Clamp Swipe from
Rusk while both actors live. Show “Grip study unlocked — needs CanGrip Right Arm.”
This achievement is disclosed before the first fight, idempotent across the session,
and can occur before killing or surrendering Rusk. G joins the known candidate
library; study at A's table is free knowledge work, one choice, not a limb reward.
Installing a compatible clamp permits deliberate P-R -> G exchange. Without clamp,
it remains inspectable/source-incompatible and cannot execute. A new person in the
same application session may choose this already-unlocked study at the table but
still needs the physical clamp; knowledge never guarantees draw.

**Starting Brain: Bifocal Node**, the only equipment option, present from attempt1.
Its access benefit is a reduction of the player's first voluntarily chosen ordinary
redraw in each encounter from2 to1 Blood. It changes no candidate weights, chosen
card, source, outcome or draw guarantee. Its visible cost is the first Preparation
card used in that encounter costs one additional Blood (Brace/Feint1->2); re-readying
an item is not that card trigger. Benefit and penalty have separate used flags and
remain used across retreat/reentry. Empty/illegal redraw pays nothing and consumes
no benefit. No Preparation used -> no extra charge, a visible conditional cost.

This fulfills one inspectable access advantage and drawback without inventing Brain
instability, a buff tree or zero-cost defense. Precommit preview shows trigger/used
flags, exact1/2-Blood redraw and the first2-Blood Preparation price.
The fixed starting equipment option remains unlocked while the app is open; the
Concept achievement supplies the earned session-level option. No extra Brain reward
comes from boss loss or death.

## Attempt/session ownership

| Fact | Retry/new person | Application closed/crashed | Disk |
|---|---|---|---|
| Initial body/Blood/wound/world | Restore fixture | Restore fixture | None |
| Deck/Attention, kit/bowl, encounter flags | Restore initial deck and charges | Restore initial | None |
| Grip achievement/known session option | Keep, but source/deck rules still apply | Clear | None |
| Fixed Bifocal option | Present as starting fixture | Present as starting fixture | None |
| Brain benefit/penalty uses | Reset for new encounter/attempt | Reset | None |
| Player-learned route knowledge | Human player remembers | Human may remember | No narrative save |
| New person's memories | No previous person's memories | Same rule | None |
| Controls/accessibility/audio/video settings | Keep | Keep | Versioned settings only |

No Memory Card generation, death-powered buff, previous-person story memory,
permanent gameplay save or unstable meter belongs to this first demo. Full-game
progression delivery, Brain collection, Concept breadth and later persistence remain
OPEN instead of being inferred from the old same-day package.

## Verification boundary and acceptance

The paper calculator checks card damage/cost upper bounds, first-preparation/redraw
cost floors, witness budgets, elective branch affordability and source thresholds.
It does not implement Attention UI, injected draw state, item readiness, NPC timing,
Brain presentation or keyboard/gamepad input. Required runtime negatives include:
G with no clamp, clamp without study/swap, invalidating G after return/ruin,
same-instance redraw with no alternatives, duplicate round redraw, spent same-round
play, illegal source after enemy Preparation, once-only reselection, charged-source
occupation, session unlock without old-person narrative knowledge, settings-only
cold launch, and discount/penalty flags surviving retreat.
