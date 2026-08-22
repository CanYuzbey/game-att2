# Game att2 - World, Progression, and Decisions

Status date: 2026-08-22

Status: **CURRENT LIVING GAME-DESIGN LEDGER. APPROVED, WORKING, EXAMPLE, AND OPEN
ITEMS MUST REMAIN DISTINCT. NO RUNTIME OR CONTENT APPROVAL.**

## Status vocabulary

| Label | Meaning |
|---|---|
| `APPROVED DIRECTION` | Owner accepted the product/design direction; detail may remain open. |
| `PAPER RULE` | Coherent paper contract; runtime migration requires a separate gate. |
| `WORKING HYPOTHESIS` | Worth testing but not proven fun or final. |
| `EXAMPLE ONLY` | Illustration, never canon or implied content. |
| `OPEN` | No answer exists yet; do not fill through convenience. |

## 2026-08-22 owner direction: goal-driven NPCs and reciprocal stakes

`APPROVED DIRECTION`: NPCs must not exist as empty meat containers waiting for the
player. Every consequential actor needs an independent world-facing purpose, something
it needs and wants, something it refuses, and a result it is trying to create. Blood or
a body part matters to that actor only when it can use the asset toward that purpose.
NPC victory may break player Will and pursue a disclosed claim rather than resolving
every loss as death.

`WORKING HYPOTHESIS`: the minimum bounded actor contract is `Goal`, `Need`, `Want`,
`RedLine`, `Leverage`, one primary `Claim`, at most one counterclaim, `Concession`, and
`Fallback`. Claims are authored before the encounter, filtered for legality, then
ordered by Need closure, Goal progress, Want fit, survival benefit, lower Concession
cost, and an authored tie-break. No actor scans the player's body or wallet to invent
the most expensive punishment at Broken Will.

The actor must prove purpose in four observable moments: Goal-related activity before
interaction, a legible Want/Red Line during contact, goal-consistent behavior during
conflict, and a post-result action that advances or revises the Goal. This is the
bounded alternative to a full off-screen life simulator.

`APPROVED DIRECTION`: faction membership supplies a default doctrine and set of world
relationships; it does not overwrite the individual. Encounter intent is derived in
three layers:

```text
Faction doctrine -> current role/duty -> individual Goal, Need, RedLine, and Claim
```

`WORKING HYPOTHESIS`: use the following purpose families for demo authoring tests.
The names are placeholders, not approved lore or final factions.

| Purpose family | World-facing aim | Likely legal encounter results |
|---|---|---|
| Blood accumulators / Houses | Accumulate Blood to service debt, buy treatment, gain status, or fund power | Trade, collect a disclosed Blood debt, threaten, or kill when a kill is the rational Blood route |
| Flesh guilds / grafters | Acquire compatible body functions and preserve valuable tissue | Ask for a specified functional limb, protect it during combat, break Will, and take it through a living transfer |
| Wardens / authorities | Maintain territory, quotas, custody, passage, or institutional order | Demand a toll, compliance, service, access, or custody; kill only when mandate or escalation supports it |
| Hunters / claimants | Complete a bounty, proof, capture, revenge, or named target obligation | Pursue death, capture, proof, or a specific asset rather than generic wealth |
| Free / unaffiliated actors | Survive, travel, heal, exchange information, or avoid larger powers | Trade, flee, cooperate, ignore the player, or carry `NoClaim` when conflict advances nothing |

Faction does not determine aggression, morality, or combat strength. `Capability` and
`RiskTolerance` are separate axes. A weak Blood debtor may bargain, deceive, flee, or
set an ambush; a strong Blood collector may openly demand payment. A powerful free
actor can have no business with the player, while a weak limb-seeker can still protect
the desired part and pursue surrender instead of death. `NoClaim` is a valid authored
result, not missing content.

The minimum NPC decision trace is therefore:

```text
filter actions by physical legality and RedLine
-> prefer survival and current Need closure
-> prefer progress toward individual Goal
-> use faction doctrine and authored priority only to break remaining ties
-> perform the resulting Claim, Concession, Fallback, or NoClaim in the world
```

`WORKING HYPOTHESIS G1`: the captive Guard's own guarding arm is failing before a duty
inspection. It primarily wants the player's compatible Full Right Arm and accepts
exactly `20 Blood` only because that amount funds replacement/treatment. Starting from
`70 Blood` and a complete Full body, paying Blood releases the player at `50 Blood`;
giving the arm releases them at `60 Blood`, Missing Right Arm, and a Controlled Clean
Stump after the provisional `10 Blood` procedure consequence. Left-Arm Punch/Block/
Parry, Kick/Evade, and Headbutt remain. This candidate is fully specified for paper
comparison but is not canon until the owner promotes it.

The values, algorithms, source research, playability invariant, and hostile review are
in `../research/defense_will_npc_balance_v0_1.md`. Whether Broken player Will enforces
the disclosed claim or offers one final lethal `Defy` remains `OPEN`.

That open fork means exactly this: under **enforced claim**, a valid pre-disclosed
claim is applied when player Will reaches zero, followed by the NPC's promised
Concession. Under **one Defy**, the game pauses once before transfer; a player who
still has a legal physical action may reject the nonlethal result, permanently close
negotiation for that encounter, and continue under lethal stakes with no second
surrender. Defy is unavailable when the body has no legal continuation. Neither
variant allows the NPC to invent a new punishment or scan for the player's best asset.

## 2026-08-22 owner direction: defense cues, body Block, and Will

`PAPER RULE`: outgoing attack cards resolve without attack-side QTEs. Short timing
input belongs to defense against an incoming attack. A Yellow threat cue allows
`Block` or `Parry`; a Red threat cue requires `Evade` and cannot be Blocked or
Parried. Color must have redundant readable icon/shape, animation, or audio support.

`PAPER RULE`: Block means choosing another legal usable body part and placing it
before the opponent's declared target. The intended target avoids the direct hit,
while the guarding part takes structural pressure, loses Integrity, and may lose
dependent capability. This makes repeated defense consume the current body and
motivates changing, preserving, and grafting parts rather than creating a free stall
loop.

`PAPER RULE`: Parry uses the deliberately difficult precision window. Success causes
no incoming Integrity, wound, or Blood consequence and reduces the attacker's visible
`Will (İrade)`. Failure applies the original attack without an extra hidden miss
penalty. Broken Will triggers the living opponent's surrender/limb bargain while the
actor remains alive, the limb remains transferable, and the player remains a credible
threat. Evade is the required successful answer to Red and creates no distance or
reposition state.

Exact cue duration, input bindings, eligible Block/Parry/Evade sources, Block loss,
Parry and Evade windows, accessibility assistance, Will start/loss/recovery values,
non-Parry Will mutations, and actor exceptions remain `OPEN`. This is paper authority
only; it does not modify or validate the frozen simulator, H1 runner, visual lab,
movement demo, configuration, tests, or any product runtime.

`WORKING HYPOTHESIS DWF-0.1` now supplies one comparison set without closing those
paper-rule decisions: ordinary Full/Strained Arms Block/Parry, Full/Strained Legs
Evade; Block loss `ceil(D * 0.75 * GuardFactor)`; minimum `900 ms` cue; Block lock
`250 ms` before contact; Parry `±90 ms`; Evade `±180 ms`; independent `100/140/200%`
timing assist; bilateral `90 Will` with Parry loss `24/30/36` and zero passive recovery.

## 2026-08-22 owner direction: Mana and kill-for-Blood reward

`PAPER RULE`: the active demo's visible renewable turn/card resource is named `Mana`
and remains separate from Blood. Mana's amount, refresh, carryover, individual card
costs, combo order, and any bounded conversion relationship with Blood remain `OPEN`.
Mana capacity increases as rounds pass so later rounds support larger card sequences;
its starting amount, increment, cap, and refill remain `OPEN`.

`PAPER RULE`: killing the active-demo opponent grants a positive Blood reward sourced
from that opponent and permanently loses that opponent's limb reward for the current
day. Accepting a living, state-derived surrender grants access to the agreed limb
through the Grafting Table but grants no kill-Blood reward. Damage, wounds, incapacity,
or surrender state alone do not award Blood. Exact yield, collection timing and
presentation, wound/yield relationship, and cap behavior remain `OPEN`.
No ordinary active-demo item or objective reward supplies Blood; named internal
emergency effects such as Panic Pulse remain separate from earned encounter rewards.

This creates the approved reward tension:

```text
kill -> Blood, no limb
living surrender accepted -> agreed limb, no kill-Blood reward
```

`APPROVED DIRECTION`: the same-day loop tests routing knowledge, not adaptive reward
denial. A poorly played attempt may leave the player with Blood but no access to the
desired limb, or with the desired limb available but insufficient Blood for the
intended downstream route. After death, the same underlying opportunities return;
the player's remembered knowledge should support a better sequence. The game must
not inspect current Blood and secretly remove, replace, or spawn the desired limb.

`WORKING HYPOTHESIS`: growing Mana and monotonic finite-state pressure prevent an
endless duel. A complete round should change at least one named finite fact—Blood,
integrity, wound severity, finite item/charge, or capability—and defense or healing
must not recreate the same complete state for free. Mana growth is the monotonic fact
before its cap; at or beyond the cap, a non-renewable fact must be consumed or worsened
each full round, and a temporary status cycle is insufficient. Exact recovery limits,
maximum-round handling, and card-level anti-stall rules remain `OPEN`.

This direction changes paper authority only. It does not modify the frozen simulator,
runtime configuration, tests, dependencies, or executable content.

## 2026-08-22 owner direction: same-day playable mini-game

`APPROVED DIRECTION`: the demo is a bounded playable mini-game, not a three-encounter
summary of the future full game. It opens with the player captive and bound. Refusing
the Guard's bargain leaves the player captive; a warned attack while bound can lead to
death; accepting a Guard-favorable trade releases the player weaker but free. The
exact payment remains an owner decision; `G1` above is the current fully specified
comparison package, not an automatically promoted answer.

The freed player traverses one small Underground City/dungeon section and meets an
actor blocking escape or progress. Exploration stays visible during a paused in-world
interaction that combines dialogue, combat choices, cards, body, items, and state.
Combat is one-versus-one and permits multiple legal body-sourced cards/combos within a
turn budget. Cards target body regions. The active demo has no range/distance system.

Body-part transfer occurs only from a living surrendered actor through a coerced
survival bargain and visible Grafting Table transition. No corpse extraction occurs.
Killing the actor loses that part reward for the current day and instead grants the
active-demo kill-Blood reward.

Death repeats the same day for the aware protagonist. The original body and unaware
world/NPCs reset. Default cards persist, attempt-learned cards are lost, exactly one
Memory Card is produced, incompatible Memory Cards remain Dormant, run instability
clears, and already-earned Brain buffs/bonuses remain as visible legal advantages.

This owner direction supersedes the active-demo paper requirements for a fixed Missing
Right Arm/Damaged Torso start, three mandatory encounters, Clinch/Engaged/Distant, one
Main per round, undefined demo failure, and fully open death persistence. It does not
change frozen simulator runtime, configuration, tests, or evidence.

## 2026-08-21 owner direction: one bounded playable demo

`APPROVED DIRECTION`: active production planning now targets a minimal playable demo.
The existing Python campaign is frozen legacy evidence, not the new game's content
plan or engine foundation. Existing H1/visual-lab experiments remain isolated
mechanic evidence. A legacy mechanic is reimplemented only when the new demo's player-
facing contract requires it; no automatic port is implied.

The proposed Underground City fiction and bounded opening/duel/reset chain are a
`WORKING HYPOTHESIS`: concrete enough to define the mini-game, still revisable without
changing product identity.

## Demo scope box

The first mini-game includes only:

- one captive Guard negotiation opening;
- one small traversable Underground City/dungeon section;
- one one-versus-one escape/progress-blocking interaction;
- the minimum hand/deck, body-source, target-region, turn-budget/combo, wound/Blood,
  kill-for-Blood, living surrender-for-limb, graft, and negotiation behavior required
  by that interaction;
- one Grafting Table limb-transfer consequence;
- one same-day death/reset with the approved card/Memory/Brain persistence split;
- one readable success endpoint after the owner defines it.

The first mini-game excludes procedural generation, a world map, three mandatory
encounters, a full roguelite meta, a full Brain tree/collection, a general dialogue
engine, broad inventory, crafting, stealth, quests, a large body-part roster, final
lore revelation, production save architecture, range/reposition combat, and reuse of
the old simulator campaign as content.

`WORKING HYPOTHESIS`: legacy retirement is staged rather than allowed to consume
production time. Freeze it now; after D1 has its own tests and reproducible build,
preserve a final Git tag and review removal of legacy executable/config/test trees
from the active checkout. Keep only an experimental runner that still answers a named
demo question.

## Level-design working hypothesis

Use one bounded connected playable section, not an open world:

```text
holding/captive space
-> Guard bargain and release threshold
-> small freely traversable Underground City/dungeon section
-> escape/progress-blocking one-versus-one interaction
-> Grafting Table consequence
-> provisional continuation/success threshold (`OPEN`)
```

- The tunnel or its upward light should act as the persistent destination landmark.
- Each space owns one primary pressure and at least one body-dependent route.
- Encounters resolve in their room; a separate battle arena must earn its existence
  through the interaction test and is currently excluded.
- More branching is cut until the opening/duel/graft/reset chain works.

## Art-direction working hypothesis — pending owner review

The following is preserved from the prior demo proposal. It is not approved for asset
production and must be reviewed during the upcoming general-theme discussion:

- Fixed-angle stylized low-poly 3D for spaces and modular bodies.
- Detachable/swappable body modules use clear silhouettes and a shared attachment
  grammar; readable state outranks anatomical realism.
- 2D illustration is reserved for cards, intent, portraits, and high-value UI.
- A restrained palette separates sick market neutrals, Blood red, and cold tunnel
  light. Gore is graphic design and state feedback, not fidelity competition.
- Pixel art and high-fidelity realistic 3D are both excluded from the first slice:
  the former weakens modular body readability at the intended camera, while the
  latter creates an unaffordable asset/animation burden.

## Engine and program recommendation

Unity is the owner-preferred `WORKING HYPOTHESIS` because its broader production path
currently feels more open. It remains gated by a two-day interaction spike; this
records direction but does not install Unity or create a project.

| Need | Recommended tool | Reason |
|---|---|---|
| Runtime | Unity 6 + C# | Owner-preferred future path; mature 3D, UI, animation, tooling, and asset ecosystem |
| 3D assets/rig/animation | Blender | One free pipeline for modular bodies, environment, rigging, and animation |
| Concept, cards, UI, textures | Krita | Free commercial-use painting and texture workflow |
| SFX editing | Audacity | Free, sufficient for the first impact/ambience pass |
| Later music/mix, only if needed | REAPER | Add only when multitrack production exceeds the slice's needs |
| Versioning | Git + Git LFS | Already available; use LFS only for binary art/audio assets |

Unity becomes the accepted demo engine only if the spike can demonstrate in one room:
fixed-camera navigation, a body-part swap, a readable card/intent overlay, one bounded
execution input, deterministic state mutation, and a Windows build. Godot remains a
fallback only if Unity's iteration or asset overhead materially blocks this bounded
slice. Unreal is rejected unless the art target changes toward high-fidelity 3D or
the team already has strong Unreal production experience.

Official references: [Unity Personal](https://unity.com/products/unity-personal/),
[Unity Runtime Fee cancellation](https://unity.com/blog/terms-update-runtime-fee-cancellation),
[Blender features](https://www.blender.org/features/), [Krita
license](https://krita.org/en/about/license/), and [Audacity downloads](https://www.audacityteam.org/download/).

## Demo decision order

Decide in this order; a later decision may not disguise a missing earlier one:

1. **Guard payment and released state:** promote, revise, or reject `G1` (`20 Blood`
   versus a Full Right Arm) and its two precisely weaker-but-playable released states.
2. **Turn/card contract:** define starting Mana, per-round growth, cap, refresh,
   carryover, ordering, condition scale, target-region effects, defense inputs/windows,
   Block loss, Will values, anti-stall rule, and the smallest Punch/Kick/Headbutt combo
   set.
3. **Duel actor and surrender:** define motivation, threats, desired limb, starting
   Will, exceptional Will rules, and why refusal/resistance is still rational before
   Will breaks.
4. **Graft consequence:** define transfer cost, replaced/attached state, and which next
   legal option visibly changes.
5. **Memory/Brain persistence:** define the Memory Card recipe and one bounded Brain
   buff that makes a repeated attempt easier without selecting cards.
6. **Mini-game success:** define the post-graft endpoint and target playtime.
7. **Content budget:** count only the rooms, cards, body states, animations, sounds,
   text, and tests required for the complete loop.
8. **Engine/runtime gate:** choose the smallest implementation vehicle only after this
   contract is reviewable; engine creation still requires explicit approval.

## Production gates

| Gate | Deliverable | Continue criterion |
|---|---|---|
| D0 — current | Closed mini-game paper contract and decision ledger | Every item 1-6 above is decided or explicitly excluded; no AI-invented defaults |
| D1 | Captive Guard opening slice | Refusal remains captivity, attack lethality is legible, and trade causes a verified weaker/free state |
| D2 | One complete in-world card duel | Player can read source, condition, target, cost/combo, expected result, and changed capability without a detached battle scene |
| D3 | Kill/surrender reward split plus Grafting Table | Kill grants Blood with no limb; surrender derives from state/motivation and grants the agreed limb with no kill-Blood; graft changes the next legal option |
| D4 | Same-day death/reset loop | Body/world/default/learned/Memory/instability/Brain persistence all match the paper contract and play can continue |
| D5 | Complete mini-game and external playtest build | Defined success endpoint works in a stable build; no P0/P1 comprehension or progression blocker |

If D1/D2 are not readable or enjoyable, revise the interaction formula before adding
more encounters, art production, or meta systems.

## World and narrative

`APPROVED DIRECTION`: the game may begin as a comparatively ordinary escape,
freedom, or survival story and gradually reveal a larger mystical or ontological
reason behind the repeated bodily experience. The late discovery should materially
recontextualize what the player has been doing.

Simulation, a server, pulling a plug, an open isometric world, AR, and
*Inscryption*-like revelation are `EXAMPLE ONLY`. Exact truth, lore, protagonist,
ending, and full-game topology remain `OPEN`. The demo camera, room string, and
traversal proposal are the bounded `WORKING HYPOTHESIS` above, not full-game canon.

## Progression layers

Keep these responsibilities separate:

- **Body state:** current anatomy, wounds, grafts, integration, capability, and loss.
- **Technique knowledge:** what has been discovered or learned.
- **Active deck:** what compatible knowledge is deliberately prepared.
- **Brain progression:** how the current hand/body relationship is processed.
- **Run/meta state:** what persists across failure or death.
- **Narrative knowledge:** what the player/character understands about the loop.

`APPROVED DIRECTION`: default cards persist through death; technique cards learned in
the attempt do not. Death generates one Memory Card, which remains Dormant when its
body-source requirement is unavailable after reset. Exact acquisition and Memory Card
generation/storage remain `OPEN`.

`APPROVED DIRECTION`: run-derived Brain instability resets on death, while already-
earned persistent Brain buffs/bonuses remain and visibly ease later attempts. Brain
progression delivery—tree, collectible parts, hybrid, or another wrapper—and exact
buff content remain `OPEN`. Permanent Brain Parts are not the only approved form.

## Current compact decision ledger

| Area | Current result | Maturity |
|---|---|---|
| Product memory | "I rebuilt myself" | Approved direction |
| Core emphasis | Using the built body, not construction alone | Approved direction |
| Strategy/execution | Roughly 70/30 compass | Approved direction |
| Combat control | Read, choose source/target/risk, lock, bounded execution, consequences | Approved direction |
| Body capability | Source-first Full/Strained/Desperate/Offline profiles | Paper rule |
| Wounds | Four wound families; treatment/repair/Blood separated | Paper rule |
| Combat range | No range, distance, neutral-settling, or reposition system in active demo | Approved direction |
| Defense cues | Yellow permits Block/Parry; Red requires Evade; redundant non-color cue required | Paper rule; presentation/timing open |
| Block | Protect declared target by redirecting structural pressure into another chosen legal guarding part | Paper rule; eligibility/loss open |
| Parry | Difficult precision response; success takes no incoming damage and reduces enemy Will | Paper rule; window/source/value open |
| Evade | Required response to Red; success prevents consequence without range/reposition | Paper rule; input/source/window open |
| Will / surrender | Successful Parry reduces visible Will; Broken Will triggers a legal living limb bargain | Paper rule; values/exceptions open |
| DWF-0.1 balance set | Body-source tags, Block formula, timing/accessibility grid, bilateral Will `90` and `24/30/36` Parry loss | Working hypothesis; paper comparison only |
| NPC agency | Goal/Need/Want/RedLine/Leverage/Claim/Concession/Fallback; victory may pursue a disclosed claim | Approved direction; exact actors open |
| G1 Guard | Failing guarding arm; accepts Full Right Arm or `20 Blood`; exact `70 -> 60/50` release branches | Working hypothesis; owner promotion open |
| Turn cadence | Visible Mana grows by round and permits larger one-turn sequences/combos | Approved direction; cadence/values open |
| Encounter reward split | Kill grants Blood and loses limb; accepted living surrender grants limb and no kill-Blood reward | Paper rule; yield/presentation open |
| Same-day opportunity learning | Wrong sequencing may separate Blood from desired-limb access; reset restores the same underlying opportunities without wallet-sensitive loot | Approved direction; exact route open |
| Duel anti-stall | Growing Mana plus finite irreversible state pressure; no free full-state loop | Working hypothesis; exact rule open |
| Procedures | Exact-source reservation and atomic started chains | Paper rule |
| Catastrophic Blood survival | Exact eligible limb or death; net 12; no Torso rescue | Paper rule |
| Deck ownership | Player-authored bounded active deck | Approved doctrine |
| Brain | Deterministic current-hand modifier; visible power/control tradeoff | Approved doctrine |
| Encounter outcome | State/motivation-derived, potentially mutual | Direction plus survey prototype |
| Default cards | Punch, Kick, Headbutt; body/condition/target/cost required | Paper rule; values open |
| Demo run | Captivity -> Guard bargain -> traversal -> blocker duel -> living graft/reset -> success endpoint | Direction; ending open |
| Full-game run | Undefined | Open |
| Demo world structure | One bounded connected Underground City/dungeon section | Working hypothesis |
| Full-game world structure | Undefined | Open |
| Demo failure/restart | Same aware protagonist/day; body/world reset; asymmetric card/Memory/Brain persistence | Paper rule |
| Living limb acquisition | Surrender bargain plus Grafting Table; killing selects Blood instead and no corpse-limb extraction occurs | Paper rule |
| Full-game death/persistence | Demo rule approved; full-game expansion undefined | Partly open |
| Final narrative truth | Undefined | Open |

## Full-game open decisions

These remain important but are downstream of the demo decision order above:

1. What constitutes an encounter, and what are its possible end conditions?
2. What constitutes a run, what is its goal, and what connects its pressures?
3. How does the approved demo same-day persistence contract expand across the full game?
4. What world/topology/presentation structure supports that run?
5. What exact deck cadence and embodied-instability model make repeated decisions
   enjoyable rather than administrative?
6. What final narrative truth recontextualizes play without replacing it?

## Scope locks

- The Python S-001 -> Jeff -> Anna campaign is frozen legacy evidence. Do not expand,
  port, or use it as the new demo's content authority.
- Encounter 3 and the Warden remain paper-only.
- VL-WP4, broader reflex work, external pilots, and production integration remain
  deferred until explicitly reopened.
- Underground-city mini-game planning is open. Any engine/runtime spike and content
  production require D0 completion plus explicit owner approval.
- Final UI, final art/audio, full-game world production, and large content expansion
  remain closed.
- Paper directions do not silently change Combat Rules, YAML, simulator code, tests,
  scenarios, or current content.

## Historical provenance

The dated source packets that produced this ledger are preserved under
`archive/design_history_2026-08-21/`. They are read only when provenance, rejected
alternatives, exact provisional tables, or earlier evidence is needed. They are not
part of the ordinary game-director reading order.

## Current design focus

The active product gate is D0: answer the six mini-game decisions in order, then
approve or revise one bounded implementation vehicle. Existing research artifacts,
additional encounters, final theme, and full-game questions do not justify parallel
implementation.
