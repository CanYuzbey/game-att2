# Research map

Research files do not override the five living design documents and do not prove the
Underground City mini-game exists.

## Current paper comparisons

| Path | Purpose |
|---|---|
| `defense_will_npc_balance_v0_1.md` | Sourced Block, timing, accessibility, Will, Guard, and NPC-purpose comparison; every numeric value is a working hypothesis |
| `defense_will_npc_balance_v0_1_model.py` | Deterministic arithmetic for the DWF-0.1 comparison |
| `wound_numeric/` | Provisional wound/Blood arithmetic supporting current paper discussion |
| `brain_synthesis/` | Deterministic body/deck/Brain ownership comparisons and procedural-persona diagnostics; informed current direction but cannot establish fun or balance |
| `card_scaling_guardrails/` | Owner-approved diagnostic content bounds plus research-only static, atomic-exchange, dominance, and combinatorial-coverage checks |

## Frozen research evidence

| Path | Purpose |
|---|---|
| `h1/` | Completed deterministic H1 fixture and result; not production combat |
| `visual_lab/` | Bounded visual-interaction fixture and source template; not the new mini-game |

Generated interactive-shell diagnostics and contaminated designer self-play were
removed from the active tree during the 2026-08-22 cleanup. They remain recoverable
from Git history. Deterministic shell replay input now lives with other fixtures at
`../examples/legacy_campaign_action_sequence.json`.

## Rule

Create a new research file only for a bounded question, reproducible model/protocol,
raw evidence, or implementation record. Put current design decisions in the relevant
living document instead of growing another parallel design package.
