# AGENTS.md — Binding Instructions for Codex

## Mission

Implement the smallest trustworthy Python simulator that reproduces the currently approved paper-prototype rules for Game att2. Preserve design traceability, deterministic behavior, and reviewability. Do not redesign the game or expand content.

## Authority and scope

- Can Yüzbey owns identity-level and product decisions.
- The simulator exists to test rules, not to become a production game.
- Do not silently change costs, probabilities, thresholds, encounter order, rewards, or meanings.
- When a rule is ambiguous, choose the simplest reversible implementation, make it configurable, and list the ambiguity in the final report.
- Do not add enemies, items, systems, lore, UI frameworks, networking, persistence, or engine integrations.

## Required workflow

1. Read the handoff in the order in `README.md`.
2. Inspect the repository before modifying it.
3. Produce a short implementation plan mapped to requirements and tests.
4. Implement in small modules with type hints and explicit ownership.
5. Add tests with each behavior, not after all implementation.
6. Run formatter/linter/type checker/tests where available.
7. Run the required deterministic scenarios and save the report.
8. Perform a hostile self-review against scope creep, hidden randomness, and rule drift.
9. Return the completion report defined in `docs/10_CODEX_RETURN_CONTRACT.md`.

## Repository rules

- Work on a feature branch when Git is available; do not push directly to `main`.
- Do not commit secrets, generated caches, virtual environments, or unrelated files.
- Keep runtime dependencies at zero unless a dependency is explicitly justified and approved.
- Development dependencies may include `pytest`, `pytest-cov`, `ruff`, and `mypy`.
- Use Python 3.11+ features only where they materially improve clarity.

## Architecture rules

- Use `dataclasses`, `Enum`, and typed collections.
- Centralize randomness behind an injected `RNGService`; never call module-global `random.*` from domain systems.
- Centralize tunable numeric values in config/data loading; do not scatter magic numbers.
- Domain systems must not print directly. They emit structured events; the CLI/logger renders them.
- Separate immutable definitions from mutable runtime state.
- Avoid circular dependencies and god classes.
- Every module must have a narrow contract and unit tests.
- Invalid state must fail loudly with a domain-specific exception or validation error.

## Mandatory behaviors

- Six body slots.
- Blood spending/gaining, collapse, Panic Pulse, and one tutorial soft-collapse valve.
- Limb integrity/state transitions and acting-limb impairment.
- Basic attacks cannot create premium Clean Harvest by themselves.
- Clean/Stressed/Ruined harvest quality.
- Focus before the main action.
- At most one Fast item per round.
- Plead Pressure and special Jeff incapacity surrender.
- Emergency grafting and Unstable v0.4.
- Anna stabilization/trade path.
- Grafting Table v0.2.
- Structured event logs, seeded runs, and scenario metrics.

## Forbidden assumptions

Do not infer that:

- enemy blood and limb integrity are the same resource;
- all limb loss reduces blood;
- all disabled limbs are severed;
- all items are reusable;
- combat ends only through blood reaching zero;
- Anna must be killed;
- a clean harvest is guaranteed by dealing enough raw damage;
- Unity is the next step after implementation.

## Definition of done

The task is done only when:

- the package installs locally;
- all required unit/integration tests pass;
- deterministic scenario runs are reproducible by seed;
- logs show every blood and limb-state change;
- the mini-campaign runs end to end;
- a simulator-results Markdown report is generated;
- no out-of-scope subsystem was added;
- completion report includes changed files, commands, tests, known gaps, and merge recommendation.
