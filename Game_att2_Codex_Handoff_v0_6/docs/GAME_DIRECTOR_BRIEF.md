# Game att2 - Game Director Brief

Status date: 2026-08-22

Status: **CURRENT LIVING GAME-DESIGN AUTHORITY. PAPER DIRECTION ONLY; NOT RUNTIME,
CONTENT, FINAL UI, ENGINE, OR PRODUCTION APPROVAL.**

This is the first of five living game-design documents. Historical design packets are
preserved under `archive/design_history_2026-08-21/`; they provide provenance but do
not override this living set. Simulator authority remains in documents 02-06 and
validated configuration.

## Product intent

- The current production target is one bounded, playable PC mini-game rather than
  another general-purpose simulator, a content-complete vertical slice, or a miniature
  version of the full game.
- The demo must prove the distinctive interaction: read a pressure, use a body-sourced
  technique, accept bodily/Blood consequences, rebuild, and carry the altered body
  into the next encounter.
- A contained single-player PC game, provisionally finishable in one weekend and
  roughly 10-12 hours.
- USD 8-12 remains a commercial hypothesis, not market evidence or a store decision.
- The target is sustained entertainment plus a distinctive, strange aftertaste, not
  a claim that this must be the player's best game ever.
- The desired player memory is: **"Kendimi yeniden inşa ettiğim bir oyundu."**

The mini-game must prove this player-facing arc:

```text
I was trapped and bargained from weakness
-> I became free at a bodily price
-> I found options in a one-versus-one duel through cards and anatomy
-> I survived by forcing or accepting a living bargain
-> death returned me to the same day with memory but not the same flesh
```

## Identity

> You are not collecting weapons. You are becoming the weapon, piece by piece, using
> your own blood as money.

The player damages, extracts, grafts, stabilizes, integrates, and risks body parts.
Blood is health, currency, and ability fuel. Body construction must materially change
what the player can do, what they can lose, and which problems they can solve.

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
- Cards, body state, Blood, wounds, and short reflex moments must form one causal
  interaction rather than unrelated minigames.
- Dialogue is an instrument for pressure, leverage, character, and route selection.
  It supports card combat and non-combat solutions; deep dialogue-tree authorship is
  not the demo's core production burden.

## Design pillars

1. **Body as Build** - important parts create actions, passives, tradeoffs, economy,
   or tactical identity.
2. **Blood as Volatile Bankroll** - spending power is also spending survival.
3. **Combat as Extraction** - success may concern what can be preserved or taken,
   not only reducing health.
4. **Desperate Maintenance** - every useful transformation can create treatment,
   repair, integration, preservation, or debt pressure.
5. **Ritualized Readability** - source, target, cost, expected result, and new risk
   are inspectable before commitment.

## Guardrails

- The game must not become upgraded stat-menu dueling.
- The body cannot be cosmetic eligibility for generic cards.
- The reflex layer cannot become an unrelated skill game.
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

## Living design set

Read in this order:

1. `GAME_DIRECTOR_BRIEF.md`
2. `CORE_LOOP_ENCOUNTER_AND_RUN.md`
3. `COMBAT_BODY_AND_BLOOD.md`
4. `DECK_BRAIN_AND_ACTIONS.md`
5. `WORLD_PROGRESSION_AND_DECISIONS.md`

Only these five files form the active game-director reading surface. Engineering,
test, evidence, governance, and research documents remain separate and protected.
