---
name: grill-me
description: Stress-test a plan through a dependency-aware owner interview. Use when asked to grill a design, uncover hidden assumptions, or resolve subjective choices before implementation.
---
# Grill me

Codex adaptation of the locally installed Claude grill-me/grilling workflow.
Provenance: [Matt Pocock skills](https://github.com/mattpocock/skills), local source
`~/.claude/skills/grilling/SKILL.md`, inspected 2026-09-06. Instructions below are
project-adapted; no Claude Skill-tool or tracker setup is required.

Read the project's authority and existing decisions first. Build a decision tree:
ID, status, prerequisites, competing options, consequence, recommendation, owner.
Research facts yourself. Use independent factual exploration only when delegation
is available and authorized; otherwise inspect locally.

Ask the smallest useful independent frontier, usually one to three questions.
Use an available asynchronous question tool while continuing independent work.
If none is callable, ask a concise plain-text question using the current conversation
rules; do not invent a tool or stop unrelated authorized paper work.
Explain the recommended option and its cost; allow the owner to reject the frame.
Do not ask a downstream question before its prerequisite is answered.
Already accepted choices are inputs, not questions to reopen by default.

Separate objective facts, reversible technical choices, test hypotheses, and subjective
product decisions. Do not turn a recommendation, silence, or an empty answer into
approval. Record actual answers with date and affected sources/tickets.
Keep unanswered branches OPEN; produce the rest of the requested analysis and plan.

An interview may span turns. Finish a round by stating its unresolved next decision.
Do not claim shared understanding or D0 closure until required choices are settled.
Existing permission to edit planning/skill files remains valid while the interview
continues. An interview answer does not by itself authorize an engine/runtime.
