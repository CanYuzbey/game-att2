# Game att2 - World, Progression, and Decisions

Status date: 2026-08-24

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

## 2026-08-24 recorded comparison: tools, starter deck, and learning

At the owner's request, the following package is preserved as a `WORKING HYPOTHESIS`
for paper comparison, not promoted authority:

- one pre-card `Tool Window` per round; use zero or one owned tool, spend no Mana,
  consume a finite charge, and commit its exact source until cleanup;
- five proposed starter technique types in an eight-instance deck:
  `Punch x2`, `Kick x2`, `Headbutt x2`, `Brace x1`, `Feint x1`;
- opening hand and hand cap four, retain at most one, discard the rest, then draw to
  four; Dormant cards occupy hand space and receive no automatic replacement;
- one-for-one deck editing at a Grafting Table, with provisional copy and composition
  limits rather than deck growth;
- `Observe -> Candidate -> Learn -> Slot -> Prove -> Memory`, bounded in the demo to
  at most two visible candidates, one Technique Study, one table swap, and one learned
  technique carried into the gate boss;
- a twelve-technique authored comparison budget: five proposed starters plus up to
  seven learned candidates. Candidate names remain `EXAMPLE ONLY`.

This record excludes random three-card rewards, card rarity, and card upgrades from
the comparison. Exact card values, legal sources, tool charges/effects, acquisition
actors/prices, catalogue content, balance, comprehension, and fun remain unproven.
No simulator, visual lab, engine project, executable content, or product claim changes.

## 2026-08-24 owner direction: concept video as the first communication artifact

`APPROVED DIRECTION`: while the bounded playable demo remains the longer-term
gameplay-proof track, the first near-term communication target is a short concept
video/previsualization. It should explain the intended Underground City gameplay,
body/card/Blood dynamics, possible characters, and world potential to friends,
possible collaborators, and potential investors before full game production begins.

The video must remain visibly labelled as pre-production visualization wherever its
shots are not captured from a verified playable build. It may communicate intended
causal rules and visual potential, but it does not prove control feel, combat appeal,
accessibility, market demand, production feasibility, investor readiness, or the
existence of the Underground City runtime. Open graft, Brain/Memory, character,
faction, boss, theme, and art choices may appear only as labelled concept variants;
polish does not promote them to canon.

The video and demo tracks share the five living design documents. The video uses a
truth matrix that identifies each scene as `PAPER RULE`, `APPROVED DIRECTION`,
`WORKING HYPOTHESIS`, `OPEN`, `CONCEPT VARIANT`, or verified prototype capture. Later
real capture may replace matching concept shots without retroactively verifying the
remainder. The detailed workflow, beat sheet, program chain, file handoffs, review
questions, and evidence boundary live in `CONCEPT_VIDEO_PRODUCTION_PLAN.md`.

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
configuration, tests, or any product runtime.

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

## 2026-08-23 owner direction: one bounded proof-of-potential sample

`APPROVED DIRECTION`: active production planning now targets a minimal playable sample
demo.
The existing Python campaign is frozen legacy evidence, not the new game's content
plan or engine foundation. Existing H1/visual-lab experiments remain isolated
mechanic evidence. A legacy mechanic is reimplemented only when the new demo's player-
facing contract requires it; no automatic port is implied.

The proposed Underground City fiction and bounded opening/graft/boss/reset chain are a
`WORKING HYPOTHESIS`: concrete enough to define the mini-game, still revisable without
changing product identity.

`APPROVED DIRECTION`: the player escapes the Underground City after defeating the
boss at its gate. The sample is for owner self-play and informal friend play, providing
directional evidence for an internal decision about full-time development or investor
pursuit. It is not itself evidence of market demand, retention, broad-audience fun, or
investor readiness.

The minimum proof floor is:

```text
Guard concession while bound
-> one or two pre-boss limb-mechanic fights
-> one gate boss that tests the integrated combat loop
-> escape, or death and same-day reset
```

For this sample, the Guard "loss" is the disclosed unfavorable concession accepted to
buy freedom and continue weaker but playable. It is not a silently approved Guard duel
or player-Will-break claim branch. One versus two pre-boss fights remains a bounded
`D0` content decision for the initial fixture; later revision may be playtest-led. The
first must produce the limb/Blood choice; a second, if used, must uniquely prove the
graft's benefit and drawback before the boss. The boss
must not become a graft-shaped key. `WORKING HYPOTHESIS`: for a clean integrated-combat
test, the boss introduces no new fundamental combat rule; D0 must promote, revise, or
reject that isolation rule.

Approximately 30 minutes is a soft planning reference only. It is not a duration
requirement, content ceiling, or acceptance condition. Actual attempt, first-escape,
and total-session durations are recorded from playable builds.

## Demo scope box

The first sample includes at minimum:

- one captive Guard negotiation opening;
- one small traversable Underground City/dungeon section;
- one or two pre-boss limb-mechanic fights, with each retained fight answering a
  distinct proof question;
- one city-gate boss confrontation that combines already-taught combat rules, tests
  the bounded combat-engagement hypothesis through human play, and opens escape when
  defeated;
- the minimum hand/deck, body-source, target-region, turn-budget/combo, wound/Blood,
  kill-for-Blood, living surrender-for-limb, graft, Brain, and negotiation behavior
  required by those interactions;
- one Grafting Table limb-transfer consequence before the gate boss, with a visible
  net capability gain and drawback used or deliberately declined in a later fight;
- one same-day death/reset with the approved card/Memory/Brain persistence split;
- one readable gate-boss defeat -> Underground City escape endpoint.

The proof floor is not a hard encounter or content ceiling. Additional sample-scale
content may be proposed inside D0 only with a named evidence or presentation purpose;
after D0 it requires a separately approved content gate, normally supported by an
observed evidence gap. The sample excludes procedural generation, a world map, a fixed
total encounter count beyond the proof floor, a full roguelite meta, a full Brain tree/
collection, a general dialogue engine, broad inventory, crafting, stealth, quests, a
large body-part roster, final lore revelation, production save architecture, range/
reposition combat, and reuse of the old simulator campaign as content.

`WORKING HYPOTHESIS`: legacy retirement is staged rather than allowed to consume
production time. Freeze it now; after D1 has its own tests and reproducible build,
preserve a final Git tag and review removal of legacy executable/config/test trees
from the active checkout. Keep only an experimental runner that still answers a named
demo question.

## Level-design working hypothesis

Use one bounded connected playable section, not an open world:

```text
holding/captive space
-> Guard concession and weaker-but-free release
-> small freely traversable Underground City/dungeon section
-> pre-boss limb fight A: source/target and kill-Blood versus living-limb choice
-> Grafting Table and bounded deck edit
-> optional pre-boss limb fight B: graft benefit and drawback in ordinary combat
-> city-gate boss
-> boss defeat opens escape
```

- The tunnel or its upward light should act as the persistent destination landmark.
- Each space owns one primary pressure and at least one body-dependent route.
- Encounters resolve in their room; a separate battle arena must earn its existence
  through the interaction test and is currently excluded.
- More branching is cut until the Guard/fight/graft/gate-boss/reset proof chain exists
  and can be evaluated through real input.

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

1. **Proof floor and evaluation question:** close the Guard concession test, distribute
   the limb/graft evidence across one or two pre-boss fights, and define what the boss
   must reveal about understood integrated combat. Record duration after play rather
   than gating content against 30 minutes.
2. **Guard payment and released state:** promote, revise, or reject `G1` (`20 Blood`
   versus a Full Right Arm) and its two precisely weaker-but-playable released states.
3. **Pre-boss fight roles and graft delta:** choose one versus two fights; define one
   exact donor limb, transfer/replacement cost, lost and gained capabilities, technique
   access, drawback, and the later ordinary-combat option it changes.
4. **Turn/card contract:** define starting Mana, per-round growth, cap, refresh,
   carryover, ordering, condition scale, target-region effects, defense inputs/windows,
   Block loss, Will values, anti-stall rule, and the smallest Punch/Kick/Headbutt combo
   set.
5. **Pre-boss actors and boss:** define motivation, threats, desired limb, starting
   Will, exceptional Will rules, and why refusal/resistance is still rational before
   Will breaks; separately define why the gate boss guards the exit, how both disclosed
   reward routes can defeat it, and promote, revise, or reject the no-new-fundamental-
   rule isolation hypothesis for its combat test.
6. **Memory/Brain persistence:** define the Memory Card recipe, anti-empty-death rule,
   and one bounded Brain buff that makes a repeated attempt easier without selecting
   cards or fabricating body capability.
7. **Evidence-led content budget:** start from the proof floor; add only rooms, cards,
   body states, animations, sounds, text, and tests that improve rule fidelity,
   comprehension, or evaluation of combat appeal.
8. **Engine/runtime gate:** choose the smallest implementation vehicle only after this
   contract is reviewable; engine creation still requires explicit approval.

## Production gates

| Gate | Deliverable | Continue criterion |
|---|---|---|
| D0 — current | Closed sample-demo paper contract and acceptance matrix | Every item 1-6 above is decided or explicitly excluded; every encounter owns a unique evidence question; no AI-invented defaults |
| D1 | Captive Guard concession slice | Refusal remains captivity, attack lethality is legible, the accepted loss is understood, and the D0-approved concession causes its declared weaker-but-free playable state; if D0 approves multiple branches, each must pass; at least one accepted branch is required |
| D2 | Pre-boss limb fight A | Player can read source, condition, target, cost/combo, defense, and consequences; kill and living-surrender routes create the advertised Blood/limb choice |
| D3 | Grafting Table plus selected downstream proof | Graft produces an exact gain, drawback, and legality change; if fight B exists it proves these in ordinary combat, otherwise the gate-boss evidence is explicitly marked as confounded; the no-graft/Blood route remains viable |
| D4 | Same-day death/reset loop | Body/world/default/learned/Memory/instability/Brain persistence all match the paper contract and play can continue |
| D5 | Connected sample and informal external playtest | In a fresh reproducible build with no unresolved P0/P1 rule-fidelity, comprehension, progression, or softlock blocker, real input reaches Guard outcome -> selected limb fight(s) -> graft consequence -> gate boss -> escape/reset; raw observations record comprehension, combat appeal, replay/change-of-plan behavior, facilitator intervention, and observed duration without claiming market validation |

Rule fidelity, comprehension, and combat appeal are separate evidence classes. Tests
and state logs can verify legality, mutation, completion, and absence of softlocks;
they cannot prove fun. Owner self-play is internal design evidence. Friends who have
not been taught the system provide informal external evidence, but their relationship
and convenience sampling must be recorded as bias. If the chain is incorrect, fix the
rules; if correct but misunderstood, fix interaction language; if understood but the
boss is not engaging, revise combat rather than covering the result with more rooms,
story, meta progression, or polish.

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
| Near-term communication artifact | Labelled concept/previsualization film explaining intended gameplay, dynamics, possible characters, and world promise | Approved direction; production plan is paper-only and no video asset exists by implication |
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
| NPC agency | Faction doctrine -> role/duty -> individual Goal/Need/RedLine/Claim; capability is separate and `NoClaim` is valid | Approved direction plus working faction families; exact actors open |
| G1 Guard | Failing guarding arm; accepts Full Right Arm or `20 Blood`; exact `70 -> 60/50` release branches | Working hypothesis; owner promotion open |
| Turn cadence | Visible Mana grows by round and permits larger one-turn sequences/combos | Approved direction; cadence/values open |
| Encounter reward split | Kill grants Blood and loses limb; accepted living surrender grants limb and no kill-Blood reward | Paper rule; yield/presentation open |
| Same-day opportunity learning | Wrong sequencing may separate Blood from desired-limb access; reset restores the same underlying opportunities without wallet-sensitive loot | Approved direction; exact route open |
| Duel anti-stall | Growing Mana plus finite irreversible state pressure; no free full-state loop | Working hypothesis; exact rule open |
| Procedures | Exact-source reservation and atomic started chains | Paper rule |
| Catastrophic Blood survival | Exact eligible limb or death; net 12; no Torso rescue | Paper rule |
| Deck ownership | Player-authored bounded active deck; current comparison is exactly 8 cards, hand 4, retain 1, and one-for-one table swaps | Approved doctrine; numerical cadence is a working hypothesis |
| Tool use | Proposed pre-card Tool Window: zero or one owned finite-charge tool, no Mana, exact source committed | Working hypothesis; tools, values, and runtime open |
| Brain | Deterministic current-hand modifier; visible power/control tradeoff | Approved doctrine |
| Encounter outcome | State/motivation-derived, potentially mutual | Direction plus survey prototype |
| Default cards | Punch, Kick, Headbutt remain paper defaults; Brace and Feint are proposed additions to the 8-card comparison | Paper rule for the original three; additions/values are working hypotheses |
| Technique acquisition | Observe -> Candidate -> Learn -> Slot -> Prove -> Memory; one study and one swap per table comparison | Working hypothesis; exact content, actors, and prices open |
| Demo objective/time | Defeat the Underground City gate boss and escape; no fixed acceptance duration; approximately 30 minutes is a soft planning reference | Objective approved; duration observed from play |
| Demo proof floor | Guard concession -> one or two pre-boss limb fights -> graft consequence -> integrated gate boss -> escape or same-day reset | Approved direction; exact one/two distribution and content open |
| Demo decision use | Owner self-play plus informal friend play informs whether to pursue full-time development or investors | Owner play is internal evidence; friends are informal external convenience evidence; neither proves market or investor readiness |
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

The first communication-planning focus is the labelled concept video defined in
`CONCEPT_VIDEO_PRODUCTION_PLAN.md`. The active gameplay/runtime product gate remains
D0: close one reviewable acceptance matrix for the Guard concession, selected
one-or-two-fight limb/graft chain, integrated gate boss, escape, and same-day reset;
then explicitly approve or revise one bounded implementation vehicle. Video planning
does not authorize an engine project, and a polished previsualization does not replace
the D0 contract or later playable evidence.
