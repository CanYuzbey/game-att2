---
name: to-tickets
description: Convert a plan or specification into local, dependency-linked work tickets with observable acceptance and explicit owner/runtime blockers. Use for tracer-bullet implementation planning or paper decision work.
---
# To tickets

Codex adaptation informed by [Matt Pocock skills](https://github.com/mattpocock/skills)
and the local Claude `to-tickets/SKILL.md`, inspected 2026-09-06.
Use the existing project planning location; absent a tracker request, write local
Markdown. No setup wizard, global configuration, or remote publication is required.

Inspect the current spec and authority. Separate paper-decision work from runtime work.
Each runtime ticket delivers one narrow capability across actual input, state,
visible result, and tests. Do not create unused web/API/database layers or speculative
prefactoring. Broad mechanical refactors, when actually needed, may use expand-contract.

Write one file per ticket with:
- ID, title, type, status, responsible role;
- source requirement/decision IDs and authority links;
- player-observable deliverable, why needed now, and scope exclusions;
- blocking ticket IDs with reasons and unresolved owner decisions;
- acceptance cases including failure/rejection and continuation/reset;
- required evidence, implementation gate, and rework/rollback boundary.

Use DRAFT or BLOCKED-OWNER for unsettled work. READY-PAPER is permission for paper
work only. READY-IMPLEMENTATION requires explicit gate authorization, exact touched
rules and verified dependencies. No blockers never means automatic runtime approval.

Order tickets topologically; validate missing IDs, cycles, and uncovered requirements.
Show conditional content branches instead of assuming an answer. Review granularity
through the concrete files; do not stall already-authorized local drafting for a
generic approval ritual. Remote tracker writes require explicit destination/authority
and readback. Never close or mutate a parent issue as an accidental side effect.
