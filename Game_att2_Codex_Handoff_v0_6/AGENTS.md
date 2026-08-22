# AGENTS.md — Binding Instructions for Codex

## Mission

Preserve the frozen legacy Python simulator as trustworthy, deterministic evidence.
The active product target is a separate bounded playable demo described by the five
living design documents. Do not expand or port the legacy campaign unless the owner
explicitly approves one isolated mechanic experiment or maintenance task.

For active-demo work, the immediate target is a bounded playable **mini-game**, not
a claim that the full game has been built. Read
`docs/DEMO_MINIGAME_AI_WORKING_CONTRACT.md` before planning or reporting demo work.

## Authority and scope

- Can Yüzbey owns identity-level and product decisions.
- The simulator is legacy rules evidence, not the production game or the new demo's
  content/engine foundation.
- Do not silently change costs, probabilities, thresholds, encounter order, rewards, or meanings.
- When a rule is ambiguous, choose the simplest reversible implementation, make it configurable, and list the ambiguity in the final report.
- Underground-city demo encounters may be defined in the living documents. They must
  not be added to legacy simulator source/configuration. A new engine project requires
  its own explicit implementation gate and scope instructions.
- Do not add runtime enemies, items, systems, lore, UI frameworks, networking, persistence, or engine integrations outside the currently approved simulator implementation scope.

## Required workflow

1. Read the handoff in the order in `README.md`. For owner-led game-design work, read
   the five living documents in `docs/README.md` order and preserve their `APPROVED
   DIRECTION`, `PAPER RULE`, `WORKING HYPOTHESIS`, `EXAMPLE ONLY`, and `OPEN`
   distinctions. The dated packets under
   `docs/archive/design_history_2026-08-21/` are provenance, not current authority.
   None of the five living design documents authorizes runtime.
2. Inspect the repository before modifying it.
3. Produce a short implementation plan mapped to requirements and tests.
4. Implement in small modules with type hints and explicit ownership.
5. Add tests with each behavior, not after all implementation.
6. Run formatter/linter/type checker/tests where available.
7. Run the required deterministic scenarios and save the report.
8. Perform a hostile self-review against scope creep, hidden randomness, and rule drift.
9. Return the completion report defined in `docs/10_CODEX_RETURN_CONTRACT.md`.

## Evidence and claim discipline

- Keep `PAPER RULE`, `WORKING HYPOTHESIS`, `OPEN`, `IMPLEMENTED`, and
  `VERIFIED` separate.
- Documentation never proves runtime existence. A UI image, isolated lab, or scripted
  simulator does not prove the active mini-game is playable.
- Do not report a completion percentage. Do not say the game/demo/feature is ready,
  complete, implemented, or playable unless the claim names the exact artifact and
  includes a fresh command/build, exit status, and player-visible verification.
- Every status report must begin with what actually exists, then what changed, then
  what remains absent or blocked.
- If evidence is missing, say `NOT VERIFIED`; do not infer success from intended code,
  documentation, filenames, passing unrelated tests, or another AI's summary.
- Scope one work item to one observable mini-game capability. Never expand a bounded
  task into the full game, a general framework, final content, or production polish.
- A runnable mock-up is not automatically a playable mini-game. The minimum causal
  chain and its acceptance evidence are defined in the AI working contract.

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
- Blood spending/gaining, Blood-0 death, Panic Pulse, and one tutorial-scope Limb for
  Life death-prevention sacrifice.
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

For active-demo work, use the task-specific gate and evidence in
`docs/DEMO_MINIGAME_AI_WORKING_CONTRACT.md`. The legacy checklist below applies only
when the owner explicitly requests legacy simulator maintenance or verification; it
must never be used to call the new mini-game complete.

A legacy simulator task is done only when:

- the package installs locally;
- all required unit/integration tests pass;
- deterministic scenario runs are reproducible by seed;
- logs show every blood and limb-state change;
- the mini-campaign runs end to end;
- a simulator-results Markdown report is generated;
- no out-of-scope subsystem was added;
- completion report includes changed files, commands, tests, known gaps, and merge recommendation.
