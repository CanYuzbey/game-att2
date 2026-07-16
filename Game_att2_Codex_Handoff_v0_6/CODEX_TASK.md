# Codex Task — Implement Combat Loop Simulator v0.1

## Role

Act as a senior gameplay systems engineer and hostile reviewer. Implement the approved paper prototype faithfully. Prefer transparency and testability over cleverness.

## Primary goal

Create a deterministic Python console simulator for:

```text
S-001 Torn but Stable
→ Jeff encounter
→ plea/bargain and harvest resolution
→ emergency graft
→ Anna encounter
→ stabilization/trade or greed path
→ Grafting Table v0.2
→ final body, blood, metrics, and event-log summary
```

## Required deliverables

1. Installable Python package under `src/game_att2_sim/`.
2. CLI entry point supporting:
   - one named scenario;
   - one seed;
   - all required scenarios;
   - optional batch count;
   - human-readable and JSON report output.
3. Unit tests and integration tests under `tests/`.
4. Config/data loading from `config/*.yaml` or equivalent checked-in data format.
5. Generated `Game_att2_Combat_Simulator_Results_v0_1.md`.
6. Completion report following `docs/10_CODEX_RETURN_CONTRACT.md`.

## Recommended implementation sequence

### Phase 0 — Inspect and plan

- Read all required files.
- Verify config consistency.
- Map requirements `RQ-001` through `RQ-018` to modules and tests.
- Do not implement before identifying contradictions.

### Phase 1 — Project and data skeleton

Implement:

- enums and domain errors;
- immutable definitions and mutable runtime state;
- YAML/data loader with validation;
- injected seeded RNG service;
- structured event and metric models.

### Phase 2 — Core systems

Implement and test:

- body/slot ownership;
- limb thresholds and tags;
- blood transactions, Panic Pulse, collapse, soft collapse;
- action costs, source-limb validation, impairment;
- round phase order;
- Focus and Fast-item timing.

### Phase 3 — Extraction and grafting

Implement and test:

- damage versus clean sever;
- Clean/Stressed/Ruined harvest;
- Claim the Cut;
- Bone Scissors;
- Hell Saw success/failure and Rage;
- emergency salvage;
- emergency graft stability;
- Unstable Twitch/Works/Ache/Surge;
- integration at table.

### Phase 4 — Encounter scripts

Implement only:

- Jeff v0.4;
- Anna v0.4;
- table v0.2;
- scripted and strategy-driven player choices required by scenarios.

Enemy logic should be small, explicit, and inspectable—not a generic AI framework.

### Phase 5 — Scenarios and batch metrics

Implement the seven required scenarios in the test plan. Add at least these simple strategies for batch observation:

- `balanced`;
- `blood_hoarder`;
- `limb_greed`;
- `survival_first`;
- `reckless_sever`.

Strategies are test drivers, not claims about final player behavior.

### Phase 6 — Review and report

- Run deterministic scenario tests.
- Run a small batch, default 100 runs per strategy unless runtime is unreasonable.
- Report distributions without claiming they prove fun.
- Identify balance anomalies, but do not silently rebalance.

## Required CLI examples

```bash
python -m game_att2_sim --scenario jeff_baseline --seed 42
python -m game_att2_sim --scenario mini_campaign --seed 42 --format text
python -m game_att2_sim --all-scenarios --seed 42
python -m game_att2_sim --batch 100 --strategy balanced --seed 42 --format json
```

Equivalent commands through an installed console script are acceptable.

## Mandatory stop conditions

Stop implementation and report a blocker rather than inventing a solution if:

- two binding rules cannot both be satisfied;
- a required data field has no defensible meaning;
- tests require a new gameplay mechanic not present in the docs;
- implementing a requirement would force Unity/UI/save systems;
- the repository contains conflicting newer source-of-truth files.

## Acceptance target

All criteria in `docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md` must pass. Any deliberate deviation must be explained with file/line references, risk, and a proposed reversible fix.
