# Tests

Codex should implement the test matrix in `docs/06_TEST_PLAN_ACCEPTANCE_v0_2.md`.

Recommended organization:

```text
tests/unit/
tests/integration/
tests/scenarios/
```

Use scripted/fake RNG for branch-level unit tests and seeded RNG for reproducibility integration tests.
