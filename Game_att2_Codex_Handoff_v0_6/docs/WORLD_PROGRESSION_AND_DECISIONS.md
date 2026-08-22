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

## 2026-08-22 owner direction: same-day playable mini-game

`APPROVED DIRECTION`: the demo is a bounded playable mini-game, not a three-encounter
summary of the future full game. It opens with the player captive and bound. Refusing
the Guard's bargain leaves the player captive; a warned attack while bound can lead to
death; accepting a Guard-favorable trade releases the player weaker but free. The
exact payment remains `OPEN`.

The freed player traverses one small Underground City/dungeon section and meets an
actor blocking escape or progress. Exploration stays visible during a paused in-world
interaction that combines dialogue, combat choices, cards, body, items, and state.
Combat is one-versus-one and permits multiple legal body-sourced cards/combos within a
turn budget. Cards target body regions. The active demo has no range/distance system.

Body-part transfer occurs only from a living surrendered actor through a coerced
survival bargain and visible Grafting Table transition. No corpse extraction occurs.
Killing the actor loses that part reward for the current day.

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
  living surrender, graft, and negotiation behavior required by that interaction;
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

1. **Guard payment and released state:** decide what the player gives and precisely why
   release leaves them weaker but able to play.
2. **Turn/card contract:** name and define the budget, refresh, ordering, condition
   scale, target-region effects, and the smallest Punch/Kick/Headbutt combo set.
3. **Duel actor and surrender:** define motivation, threats, desired limb, surrender
   evaluation inputs, and why refusal/resistance is still rational before surrender.
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
| D3 | Living surrender plus Grafting Table | Surrender derives from state/motivation; no corpse extraction; graft changes the next legal option |
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
| Defense | Automatic/source-valid response direction; exact active-demo timing open | Direction/open detail |
| Turn cadence | Multiple legal cards/one-turn combos within visible budget | Approved direction; values open |
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
| Living limb acquisition | Surrender bargain plus Grafting Table; no corpse extraction | Paper rule |
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
