---
name: to-spec
description: Synthesize an existing plan or conversation into a bounded, source-traceable specification and acceptance matrix. Preserve unknowns and project gates; default to local documents.
---
# To spec

Codex adaptation informed by [Matt Pocock skills](https://github.com/mattpocock/skills)
and the local Claude `to-spec/SKILL.md`, inspected 2026-09-06.
Use the project's existing authority documents; do not create a parallel design canon.

Read full referenced context and relevant current files. State the user's problem,
one observable target, approved rules, proposed fixture, OPEN choices, and exclusions.
Include only stories needed to cover the behavior; length is not coverage.
Map each requirement to a positive case, a negative case, expected state/output,
evidence class, and dependent decision ID. Prefer externally observable test seams.

Separate source-owned design from technical implementation choices. Cite stable local
authority links; avoiding all file paths would destroy this project's traceability.
Do not invent modules, values, actors, persistence boundaries, or extra layers.

When information is missing, mark its dependent behavior BLOCKED and use grill-me for
a focused decision round if appropriate. Synthesis does not silently decide.
Write the reviewable local artifact under the existing project convention.
Do not publish or mark ready-for-agent without resolved decisions and the required
authorization. A real tracker needs an explicit publication request and destination.
