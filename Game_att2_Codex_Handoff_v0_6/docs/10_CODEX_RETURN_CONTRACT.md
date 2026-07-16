# Game att2 — Codex Completion and Return Contract

Codex must return a final report with these sections.

## 1. Executive summary

- What was implemented.
- Whether the simulator acceptance gate passed.
- Merge recommendation: merge / revise / do not merge.

## 2. Changed files

For each file:

- purpose;
- meaningful changes;
- whether generated or authored.

## 3. Requirements traceability

Table:

```text
Requirement ID
Implementation module/file
Test(s)
Result
Notes/deviation
```

Cover at least RQ-001 through RQ-021 from the Development Master.

## 4. Commands run

Include installation, formatting/linting, type checking, tests, scenarios, and batch runs with exit status.

## 5. Test results

- unit/integration totals;
- failing/skipped tests and reasons;
- deterministic reproduction example;
- coverage if generated.

## 6. Scenario results

Summarize S1–S7 and link/report output. Distinguish implementation correctness from balance observations.

## 7. Batch metrics

Report each strategy and note anomalies. Do not claim fun or market validation.

## 8. Design ambiguities and assumptions

List every rule that required interpretation:

- source files consulted;
- chosen interpretation;
- reversibility;
- risk;
- suggested owner decision.

## 9. Scope audit

Explicitly state whether any out-of-scope system, content, dependency, or unrelated refactor was added. If yes, explain and recommend removal.

## 10. Hostile self-review

List architecture violations, hidden dependencies, untested branches, maintainability issues, rule drift, and likely bugs by severity.

## 11. Known limitations

Include simulator-only compromises and anything blocking the next gate.

## 12. Recommended next step

Choose one:

- revise rules/config and rerun;
- improve simulator coverage;
- build tiny interactive text prototype;
- prepare Unity graybox proposal;
- stop/pivot.

Do not begin the next step without owner approval.
