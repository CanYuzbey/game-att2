# Game att2

Canonical repository: <https://github.com/CanYuzbey/game-att2>

Game att2 is a single-player hell-loop roguelike concept in which the player's body
is the build and Blood is simultaneously life, currency, and fuel.

## What exists now

- A bounded Underground City mini-game is defined on paper at the D0 decision gate.
- The new mini-game has no approved engine project or verified product runtime.
- A deterministic Python simulator, H1 runner, and visual interaction lab remain as
  frozen legacy/research evidence. They are not the new mini-game.
- Current combat, Blood, Mana, Will, defense, and NPC-purpose decisions live in five
  living design documents.

## Start here

The working package is [Game_att2_Codex_Handoff_v0_6](Game_att2_Codex_Handoff_v0_6/).

1. Read the [AI working contract](Game_att2_Codex_Handoff_v0_6/docs/DEMO_MINIGAME_AI_WORKING_CONTRACT.md)
   for scope and evidence rules.
2. Use the [documentation map](Game_att2_Codex_Handoff_v0_6/docs/README.md) to read
   the five living design documents in order.
3. Use the [package README](Game_att2_Codex_Handoff_v0_6/README.md) for the concise
   repository map and legacy verification commands.

## Current paper direction

- Attacks are body-sourced cards paid with round-growing Mana.
- Incoming Yellow threats allow Block or Parry; Red threats require Evade.
- Block redirects damage into a chosen guarding body part. Precise Parry prevents
  damage and breaks opponent Will.
- Killing grants Blood but loses that opponent's limb opportunity for the day;
  living surrender grants the agreed limb but no kill-Blood.
- NPC intent is derived from faction doctrine, current role, and individual need.
  Strength is independent of purpose, and `NoClaim` is valid when conflict gains the
  NPC nothing.

All of the above is paper design, not proof of implemented gameplay.

## Repository boundary

The root `.agents/` folder contains active collaboration instructions. Project files
belong under `Game_att2_Codex_Handoff_v0_6/`. Historical evidence remains isolated
under that package's `docs/archive/` and does not override current design authority.
