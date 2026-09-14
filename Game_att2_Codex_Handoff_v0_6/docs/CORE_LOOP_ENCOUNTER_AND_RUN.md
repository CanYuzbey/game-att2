# Game att2 — Core Loop, Encounter, and Run

Status date: 2026-09-15

**CURRENT LIVING PAPER AUTHORITY.** Selected two-NPC/Boneatour demo and
Z48/A numeric fixture v0.1. No engine/runtime approval or playable evidence.

## Connected attempt

The actor starts injured and freely controllable, not bound:
injured bone landscape -> asymmetric NPC A -> table -> human NPC B ->
Boneatour -> state-derived death -> retry/menu/exit.

A and B are resolved encounters, not optional substitutes for one another. Both
ordinary kill and living surrender can open each passage. A creates the first
limb/Blood decision; B tests the changed body's Grip and guarding tradeoff.
The optional story pocket has no battle, Blood, item or permanent-power reward.

## P03 — Exact round and source contract

Authority: Z13/A, Z16/B, Z17/B, Z18/A, Z23/A, Z25/B, Z27/B, Z33/A.
Numbers and extra ordering details below are Z48/A delegated content.

1. Complete previous atomic mutations; resolve death/fatality before living claims.
2. Begin the next decision round. Set Preparation=1 and Main=1 for each living actor.
   A pending player stun sets those opportunities to 0 for this round. Defense
   remains available. The skipped Main does not consume a Ruined-Torso rescue.
3. Recompute body/card/item legality. Refill only Spent/Invalid Attention positions,
   with equal-weight draw without replacement from remaining deck instances;
   unplayed and Dormant positions remain. Reveal exact hostile Main, source, target,
   damage, cue, costs and any Preparation.
4. While paused, choose at most one Preparation and one Main; choose a legal defense
   source/intention for the revealed incoming action. One paid redraw may precede
   commitment. Preview independent costs and source occupancy.
5. Player Preparation resolves first, then enemy Preparation. Source/target changes
   are visible before either Main. Re-readying a tool consumes Preparation instead
   of a Preparation card; it does not add an opportunity.
6. Revalidate player Main. If unstarted and now illegal, pay/mutate nothing and allow
   exactly one reselection (Z17/B). A second invalidation or declined reselection
   spends that opportunity. Started actions cannot be rolled back; no substitution.
7. Resolve player Main atomically. NPC defense is inside that attack's resolution,
   not an extra Main. Apply costs/contact, recompute legality, and check death then
   claims before continuing.
8. Revalidate the enemy's declared Main. Invalidation cancels its unpaid action;
   it does not generate a new free Main. A fallback must be selected/revealed at
   refresh, not substituted after a Grip.
9. Execute the player's preselected legal defense with one timed input. Wrong
   intent/source is not repaired by automation; missed Parry does not become Block.
   Resolve activation cost and contact, then Will and claims.
10. Release Grip only after the held actor's selected response opportunity has
    resolved or been canceled. Until then the gripping arm cannot attack/Block/Parry.
    Release creates no refund.
11. Apply one combat wound tick, expire Brace/Feint, clear temporary commitments, and
    consume this round's stun. Newly applied stun targets the next unstarted decision
    round; it does not erase a completed Main. Re-run death/fatality/claim checks and
    emit ordered state evidence.

There is no Mana, expanding sequence budget, free Tool Window or discard-all
cadence. One Preparation plus one Main is the maximum ordinary budget. A same-round
Feint/Main link uses those two opportunities. Defense uses neither budget nor card.

Selecting an intent alone does not reserve a source indefinitely. Atomic actions
occupy their exact sources while resolving. Brace permits its source's subsequent
Block; Grip's persistent occupancy forbids same-arm attack/Block/Parry. Feint expires
if the differently sourced Main becomes illegal. Multi-source actions use the weakest
required condition. Sources are revalidated after each mutation.

## P04 — Will, claims and continuation

Ordinary player/NPC Will starts 90 each encounter, recovery 0, ordinary
damage/GoalCritical shocks 0. Successful Parry subtracts 24/30/36 for the revealed
Routine/Committed/Critical attack. Low Will changes no cost, timing or stat.

At Will=0 pause once after death checks. Living surrender requires two living actors
and a winner with an affordable legal attack from a usable source. At least one
compatible attack instance must remain in the active deck and be obtainable under
the ordinary Attention/refill/redraw contract; no absent card/source is fabricated.

For player defeat show the NPC's preauthored primary demand, one fixed counteroffer
and one lethal Defy if legal continuation exists. At most one counteroffer occurs.
Acceptance applies its cost and promised concession atomically. Defy closes this
encounter's negotiation permanently. Invalid transfer does not occur; use the
authored fallback. See [World P07](WORLD_PROGRESSION_AND_DECISIONS.md#p07--actors-and-preauthored-claims).

For NPC defeat show its living arm offer, reward-free mercy or continue-to-kill.
A ruined/unavailable arm yields no fake replacement. Mercy/passage follows its
expectation of death from renewed resistance, not a free-flesh story. Accepting the
living bargain yields no kill-Blood.

Boneatour is the Z42/A exception: Will break cancels the next otherwise-legal Charge
selection once, with a revealed normal fallback in its place. There is no boss
surrender or transfer; Will stays 0 and the exception cannot be farmed.

## Retreat, clocks and stalled input

Each ordinary encounter permits one retreat for 6 Blood through Main using
Full/Strained Legs. Wounds, body, NPC state, Will, negotiation flags, remaining uses
and retreat-used flag persist. Reentry restores no resources, Attention or retreat.
Round opportunities refresh on reentry; the unresolved encounter must still be
resolved to open passage. This normal-fight choice gives Boneatour no retreat.

30 active exploration seconds create one wound tick; combat creates one at round
end. Preserve the exploration remainder, freeze it in combat, resume it afterward.
Dialogue, inspect, care/table, pause, settings and alt-tab pause both clocks.
A completed retreat round ticks once; the same interval is never charged twice.

Leaving a paused decision panel open pauses the session; it is not a completed free
combat-state cycle. No hidden timeout is introduced. No input in a running cue
applies the original attack. Pass spends the Main opportunity and resolves that
threat. Rejected uncommitted input is not a newly completed round.

## P05 — Finite-state and death bound

Z30/B + Z43/A: attacks cost at least 2 player Blood, accepted defense at least 1,
Grip at least 2, redraw at least 1 even with the Brain. There is no global round
tax. Each procedure/item/Preparation declares its own cost. Healing transfers
existing bowl Blood; treatment generates no Blood and repairs no structure.

Define E = body Blood + bowl Blood + unclaimed eligible normal-kill Blood.
Initially E is at most 80 + 30 + 30 = 140. Each unique eligible kill converts its
already-counted allowance once; accepted surrender/mercy removes that allowance.
Costs, wounds, overflow and lost access decrease E. Card cycles, session unlocks,
old-arm replacement and duplicate claim attempts cannot increase it.

At the boss, an input-responsive completed round pays a defense/finite Main cost,
or permits an actual vital hit of at least 10 Integrity plus 4 Blood. Grip cannot
cancel all ordinary threats for free and cannot cancel Charge. Thus each completed
round decreases a named finite player fact. The loose bound is 140 resolved boss
rounds, including a fatal activation/hit. Modal pause is outside this transition bound.

Player structural damage is at most 4 times paid offensive Blood: all base ratios
are at most 4; a nonstacking Feint adds 3 for another Blood. Grip has no repeat tick
damage. Global damage is at most 560 even with all rewards, perfect draw and the
best source. All boss lethal vitals start at 600; none can reach 0. Horns have no
vital overflow or vascular wound. Making both arms and Legs Desperate would require
3 * 420 = 1260 damage, more than 560, so an ordinary threat remains legal.

Boss Blood starts 900. Its at-most-three paid actions per resolved round consume
at most 420 in that loose bound. No boss regeneration or immortality override is
used. Actual vital hits or paid depletion kill the player before the boss.
This is analytic fixture evidence, not exhaustive verification of future engine
code. New damage, healing, zero-cost discount, reward, wound or cancellation requires
recomputing the bound.

## Reset and full-game boundary

Retry alternates the two authored people. Restore initial body/Blood/wounds, deck,
kit/bowl, NPCs/horns and all attempt flags. Keep player-owned session Concept unlocks
and the single starting Brain option; new people have no previous narrative memories.
Unlocking is idempotent first-encounter achievement, never death count. No Memory
Card, death buff or boss reward. Cold launch/crash clears gameplay, retaining settings.

Full-game run topology, long-term meta, cosmology, revelation, save architecture,
other bosses and death rules remain OPEN.
