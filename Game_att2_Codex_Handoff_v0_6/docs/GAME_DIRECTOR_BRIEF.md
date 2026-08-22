# Game att2 - Game Director Brief

Status date: 2026-08-23

Status: **CURRENT LIVING GAME-DESIGN AUTHORITY. PAPER DIRECTION ONLY; NOT RUNTIME,
CONTENT, FINAL UI, ENGINE, OR PRODUCTION APPROVAL.**

This is the first of five living game-design documents. Historical design packets are
preserved under `archive/design_history_2026-08-21/`; they provide provenance but do
not override this living set. Simulator authority remains in documents 02-06 and
validated configuration.

## Product intent

- The current production target is one bounded, playable PC sample demo rather than
  another general-purpose simulator, a content-complete vertical slice, or a miniature
  version of the full game.
- `APPROVED DIRECTION`: the mini-game objective is to escape the Underground City by
  defeating the boss at the city gate. Approximately 30 minutes is a non-binding
  planning reference, not a duration requirement, content ceiling, or acceptance
  condition. Actual attempt and session duration must be observed from the playable
  sample rather than decided by prose.
- `APPROVED DIRECTION`: the minimum proof floor is one captive-Guard concession that
  buys freedom at a real cost, one or two pre-boss fights that expose limb mechanics,
  and one gate boss that exercises the integrated combat loop. Additional sample-scale
  content may be proposed inside D0, or through a later separately approved content
  gate, only when it owns a named evidence or presentation purpose; this floor is not
  a fixed encounter cap or runtime authorization.
- The demo must prove the distinctive interaction: read a pressure, use a body-sourced
  technique, accept bodily/Blood consequences, rebuild, carry the altered body into a
  later fight, and ask whether those known rules remain enjoyable in the gate-boss
  confrontation.
- The intended sample supports owner self-play and informal friend play, then an
  internal go/no-go decision about full-time development or investor pursuit. It does
  not by itself establish market demand, retention, broad-audience fun, or investor
  readiness.
- `FULL-GAME WORKING HYPOTHESIS`: a contained single-player PC game, provisionally
  finishable in one weekend and roughly 10-12 hours. This does not budget the sample.
- `FULL-GAME WORKING HYPOTHESIS`: USD 8-12 remains a commercial comparison, not market
  evidence or a store decision.
- The target is sustained entertainment plus a distinctive, strange aftertaste, not
  a claim that this must be the player's best game ever.
- The desired player memory is: **"Kendimi yeniden inşa ettiğim bir oyundu."**

The mini-game must prove this player-facing arc:

```text
I was trapped and accepted a disclosed loss from weakness
-> I bought freedom at a disclosed meaningful price and continued weaker but playable
-> in limb fight A I learned how cards, targets, and anatomy change one another
-> I chose Blood through death or a limb through a living bargain
-> I grafted and carried the resulting capability change forward
-> when needed, limb fight B exposed the graft's benefit and drawback before the boss
-> if I died, I returned to the same day with memory but not the same flesh
-> I used the known combat language against the gate boss and escaped the Underground City
```

For this sample, the Guard-opening "loss" means accepting a disclosed unfavorable
concession while bound in order to become free. It does not silently approve a full
Guard duel, player-Will break enforcement, or the still-`OPEN` claim-versus-`Defy`
decision.

## Identity

> You are not collecting weapons. You are becoming the weapon, piece by piece, using
> your own blood as money.

The player damages, extracts, grafts, stabilizes, integrates, and risks body parts.
Blood is health, currency, and ability fuel. Body construction must materially change
what the player can do, what they can lose, and which problems they can solve.

For the active demo, combat resolution creates one explicit reward tension: killing
the opponent yields Blood but destroys access to that opponent's limb reward for the
current day; accepting a living surrender yields the agreed limb through the
Grafting Table but no kill-Blood reward. This is a paper rule, not runtime evidence.

## Creative hierarchy

1. **Core play:** the build is a body that acts, commits, becomes wounded, and loses
   capability. Using the built body must be fun; construction alone is insufficient.
2. **Controlled depth:** parts, wounds, techniques, and current choices influence one
   another without becoming an unreadable simulation.
3. **Emotional result:** becoming stronger gradually raises the question of what part
   of the former self has been surrendered.

Transhumanism is therefore a gameplay tension, not a cosmetic theme: transformation
can create power while making the assembled self harder to coordinate or control.
No specific sanity, corruption, or instability meter is approved by this statement.

## Intended play character

- Approximately 70% problem solving and selection / 30% physical application is a
  compass, not a numeric promise.
- The player reads a concrete pressure, finds a body-dependent approach, commits a
  source and risk, then physically applies that decision where appropriate.
- Strategy determines what and why. Execution influences how well the committed
  action resolves, but cannot routinely erase a bad strategic decision.
- Offensive cards carry the strategic commitment without an attack QTE. The short
  execution test belongs to defense: read Yellow as Block/Parry and Red as Evade.
- Block protects one targeted part by sacrificing condition in another chosen part;
  precise Parry protects the defender and breaks enemy Will toward surrender.
- Cards, body state, Blood, wounds, and short reflex moments must form one causal
  interaction rather than unrelated minigames.
- Dialogue is an instrument for pressure, leverage, character, and route selection.
  It supports card combat and non-combat solutions; deep dialogue-tree authorship is
  not the demo's core production burden.
- A consequential NPC has a goal it would pursue without the player, a need/want and
  refusal that explain its trade, and a disclosed claim it may pursue after breaking
  player Will. Blood and limbs are useful to that NPC, not generic score tokens.

## Design pillars

1. **Body as Build** - important parts create actions, passives, tradeoffs, economy,
   or tactical identity.
2. **Blood as Volatile Bankroll** - spending power is also spending survival.
3. **Combat as Extraction** - success may concern what can be preserved or taken,
   not only reducing health. The active demo makes the kill-for-Blood versus
   surrender-for-limb choice explicit.
4. **Desperate Maintenance** - every useful transformation can create treatment,
   repair, integration, preservation, or debt pressure.
5. **Ritualized Readability** - source, target, cost, expected result, and new risk
   are inspectable before commitment.

## Guardrails

- The game must not become upgraded stat-menu dueling.
- The body cannot be cosmetic eligibility for generic cards.
- The reflex layer cannot become an unrelated skill game.
- Yellow/Red threat meaning cannot depend on color alone; it requires redundant
  readable shape/icon, animation, or audio language.
- Space cannot become a walk-forward/attack/walk-back locomotion loop.
- The active mini-game has no combat range/reposition system. Do not hide the removed
  range model inside card tags, camera states, or renamed distance resources.
- Narrative mystery cannot substitute for a playable core.
- More documentation is not progress unless it closes a player-facing decision or
  supports a bounded test.
- Legacy simulator breadth is not a production requirement. A mechanic enters the
  demo only because the demo needs it and a player can encounter its consequence.
- Same-day persistence must create earned familiarity, not erase all consequence:
  flesh and the unaware world reset, while memory-derived progress remains bounded and
  inspectable.
- NPCs cannot be inventory-scanning punishment functions or idle meat containers.
  Their demand must pre-exist the player's failure, their combat choices must protect
  what they want, and their victory/concession must visibly advance or revise a goal.

## Current bounded comparison, not canon

`DWF-0.1` supplies test values for Block source/wear, `±90 ms` Parry, `±180 ms` Evade,
independent accessibility controls, and bilateral `90 Will`. `G1` supplies an exact
Guard comparison: a visibly failing guarding arm motivates a Full Right Arm or
`20 Blood` demand, starting from `70 Blood`; the resulting release is either `50 Blood`
with the full body or `60 Blood` with a Missing Right Arm and Controlled stump. Both
remain `WORKING HYPOTHESIS`, not a final design or implemented behavior. Evidence and
reject criteria live in `../research/defense_will_npc_balance_v0_1.md`.

## Living design set

Read in this order:

1. `GAME_DIRECTOR_BRIEF.md`
2. `CORE_LOOP_ENCOUNTER_AND_RUN.md`
3. `COMBAT_BODY_AND_BLOOD.md`
4. `DECK_BRAIN_AND_ACTIONS.md`
5. `WORLD_PROGRESSION_AND_DECISIONS.md`

Only these five files form the active game-director reading surface. Engineering,
test, evidence, governance, and research documents remain separate and protected.
