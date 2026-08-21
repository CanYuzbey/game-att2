# Game att2 - World, Progression, and Decisions

Status date: 2026-08-21

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

## 2026-08-21 owner direction: one bounded playable demo

`APPROVED DIRECTION`: active production planning now targets a minimal playable demo.
The existing Python campaign is frozen legacy evidence, not the new game's content
plan or engine foundation. Existing H1/visual-lab experiments remain isolated
mechanic evidence. A legacy mechanic is reimplemented only when the new demo's player-
facing contract requires it; no automatic port is implied.

The proposed underground-city fiction and three encounters are a `WORKING
HYPOTHESIS`: intentionally concrete enough to build, but still revisable without
changing the product identity.

## Demo scope box

The first demo includes only:

- one authored, linear escape route through the Rot Market;
- one damaged starting body;
- three encounters with different motivations;
- the minimum hand/deck, body-source, Blood, wound, extraction, graft, and negotiation
  behavior required by those encounters;
- state carried continuously from captivity to the exit tunnel;
- one readable success ending and one explicitly defined failure/restart contract.

The first demo excludes procedural generation, a world map, meta progression, a full
Brain tree/collection, a general dialogue engine, broad inventory, crafting, stealth,
quests, a large body-part roster, final lore revelation, production save architecture,
and reuse of the old simulator campaign as content.

`WORKING HYPOTHESIS`: legacy retirement is staged rather than allowed to consume
production time. Freeze it now; after D1 has its own tests and reproducible build,
preserve a final Git tag and review removal of legacy executable/config/test trees
from the active checkout. Keep only an experimental runner that still answers a named
demo question.

## Level-design working hypothesis

Use a linear **string of rooms**, not an open isometric world:

```text
holding pen / body inspection
-> guard ring
-> Rot Market and merchant stall
-> tunnel gate and Exit Keeper
-> upward escape tunnel
```

- The tunnel or its upward light should act as the persistent destination landmark.
- Each room owns one primary pressure, one body-dependent route, and one irreversible
  carry-forward consequence.
- Encounters resolve in their room; a separate battle arena must earn its existence
  through the interaction test.
- One small optional alcove may test exploration value. More branching is cut until
  the three-encounter line works.

## Art-direction working hypothesis

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

This is a `WORKING HYPOTHESIS`, gated by a two-day interaction spike:

| Need | Recommended tool | Reason |
|---|---|---|
| Runtime | Godot 4 + GDScript | Small PC demo, strong 2D/3D combination, rapid scene/UI iteration, MIT license |
| 3D assets/rig/animation | Blender | One free pipeline for modular bodies, environment, rigging, and animation |
| Concept, cards, UI, textures | Krita | Free commercial-use painting and texture workflow |
| SFX editing | Audacity | Free, sufficient for the first impact/ambience pass |
| Later music/mix, only if needed | REAPER | Add only when multitrack production exceeds the slice's needs |
| Versioning | Git + Git LFS | Already available; use LFS only for binary art/audio assets |

Godot becomes the chosen engine only if the spike can demonstrate in one room:
fixed-camera navigation, a body-part swap, a readable card/intent overlay, one bounded
execution input, deterministic state mutation, and a Windows build. Unity remains a
reasonable fallback only if the actual implementer is materially faster in Unity.
Unreal is rejected for this slice unless the art target changes toward high-fidelity
3D or the team already has strong Unreal production experience.

Official references: [Godot license](https://godotengine.org/license/), [Godot
features](https://godotengine.org/features/), [Blender features](https://www.blender.org/features/),
[Krita license](https://krita.org/en/about/license/), and [Audacity downloads](https://www.audacityteam.org/download/).

## Demo decision order

Decide in this order; a later decision may not disguise a missing earlier one:

1. **Demo contract:** target duration and exact death/capture/restart behavior.
2. **Thirty-second view:** fixed-camera movement, how conflict begins, where the hand
   appears, and how source/target/risk are read.
3. **Guard slice:** minimum cards, source states, wound consequence, disable/kill
   routes, extraction, and graft.
4. **Carry-forward economy:** what Blood, wounds, parts, and cards persist across the
   three rooms; no meta layer.
5. **Merchant grammar:** leverage facts, offers, counteroffers, refusal, mental defeat,
   surrender, and why pure damage cannot simply unlock the tunnel.
6. **Exit Keeper:** motivation and state-derived end routes.
7. **Content budget:** exact parts, cards, animations, sounds, and text required—nothing
   without an encounter responsibility.
8. **Engine acceptance:** keep or reject Godot after the one-room spike.

## Production gates

| Gate | Deliverable | Continue criterion |
|---|---|---|
| D0 — current | One-page demo contract and decision ledger | Failure loop and thirty-second view can be stated without lore filler |
| D1 | Guard-room interaction slice in graybox | A fresh observer can read source, target, cost, expected result, and changed capability |
| D2 | Complete Guard encounter plus graft consequence | The new arm changes the next legal options; damage is not cosmetic |
| D3 | Merchant encounter | Negotiation follows visible leverage/body state rather than a detached dialogue score |
| D4 | Exit Keeper and complete escape line | Prior body/Blood/decision state materially changes climax routes |
| D5 | Art/audio/readability pass and external playtest build | Stable Windows build; no P0/P1 comprehension or progression blocker |

If D1 is not readable or enjoyable, revise the interaction formula before building
the Merchant, final encounter, art production, or meta systems.

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

`WORKING HYPOTHESIS`: techniques may be discovered through embodied experience and
later prepared at maintenance/reconstruction points. Knowledge may persist longer
than flesh. The exact acquisition and persistence model is `OPEN`.

Brain progression delivery—tree, collectible parts, hybrid, or another wrapper—is
`OPEN`. Permanent Brain Parts are no longer the only approved form.

## Current compact decision ledger

| Area | Current result | Maturity |
|---|---|---|
| Product memory | "I rebuilt myself" | Approved direction |
| Core emphasis | Using the built body, not construction alone | Approved direction |
| Strategy/execution | Roughly 70/30 compass | Approved direction |
| Combat control | Read, choose source/target/risk, lock, bounded execution, consequences | Approved direction |
| Body capability | Source-first Full/Strained/Desperate/Offline profiles | Paper rule |
| Wounds | Four wound families; treatment/repair/Blood separated | Paper rule |
| Range | Action-produced Clinch/Engaged/Distant with neutral settling | Paper rule |
| Defense | Preparation -> automatic reflex -> compatible passive | Paper rule |
| Initiative | Public Lead, two locks, Lead-first causal resolution | Paper rule |
| Procedures | Exact-source reservation and atomic started chains | Paper rule |
| Catastrophic Blood survival | Exact eligible limb or death; net 12; no Torso rescue | Paper rule |
| Deck ownership | Player-authored bounded active deck | Approved doctrine |
| Brain | Deterministic current-hand modifier; visible power/control tradeoff | Approved doctrine |
| Encounter outcome | State/motivation-derived, potentially mutual | Direction plus survey prototype |
| Demo run | Captivity -> Guard -> Merchant -> Exit Keeper -> tunnel | Working hypothesis |
| Full-game run | Undefined | Open |
| Demo world structure | Linear underground-market room string | Working hypothesis |
| Full-game world structure | Undefined | Open |
| Demo failure/restart | Undefined | Open — D0 blocker |
| Full-game death/persistence | Undefined | Open |
| Final narrative truth | Undefined | Open |

## Full-game open decisions

These remain important but are downstream of the demo decision order above:

1. What constitutes an encounter, and what are its possible end conditions?
2. What constitutes a run, what is its goal, and what connects its pressures?
3. What happens on failure/death, and which body/knowledge/deck/Brain facts persist?
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
- Underground-city demo planning and definition of a bounded one-room engine spike
  are open. Spike implementation and full content production require D0 completion
  plus explicit owner approval.
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

The active product gate is D0: define the demo failure contract and thirty-second
view, then approve or revise the one-room Guard interaction spike. Existing Brain,
reflex, and full-game questions do not justify parallel implementation.
