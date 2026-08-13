---
name: debug-interactive-demo
description: Diagnose and repair local interactive web demos whose page renders but controls, animation, input, startup, or visible feedback fail. Use for HTML/CSS/JavaScript prototypes, Vite demos, file-opened demos, and browser interaction failures; require launch, DOM, event, runtime-error, motion, fallback, and user-visible feedback checks before signoff.
---

# Interactive Demo Debugging

Use this skill to take a prototype from "it looks loaded but does nothing" to a repeatable, understandable interaction test.

## Scope and safety

- Keep a demo distinct from the game runtime, simulator, and rules authority.
- Preserve stated timing, damage, and interaction assumptions unless the task explicitly changes them.
- For one-file or portable demos, prefer dependency-free HTML, CSS, and classic JavaScript. A development server may be optional but must not be the only launch route.
- Do not report a feature as fixed until the documented launch path, the primary button, the associated keyboard control, the success/failure state, and reset path have evidence.

## Triage sequence

1. Reproduce the user's exact launch method first: direct file opening, the documented command, or a local server.
2. Check whether JavaScript executed: look for script-loading, syntax, module/CORS, selector, and console errors.
3. Inventory the interaction chain: button exists, listener binds, state begins, frame/timer runs, visible state changes, input resolves, retry resets.
4. Classify the earliest break: page-only load, unbound handler, motion failure, timing/coordinate failure, no visible feedback, or broken launch instructions.
5. Fix the earliest cause, then add a small user-visible fallback for a failed script or missing required control.

## Advanced situations

- A `file://` launch should not depend on ES module imports or root-relative asset paths. Use relative `./` links and a deferred classic script unless a server is mandatory and clearly started for the user.
- Time the intended contact from the same monotonic clock that drives animation. Resolve the no-input timeout separately from an early or late attempt.
- Calculate movement from live element positions when a responsive layout can change the contact point.
- On startup, fail loudly for missing required elements; retain a readable loading/fallback message if the script never starts.
- Test both pointer and keyboard paths. Ignore repeated input after resolution and cancel pending animation frames during reset.
- Verify server mode using the actual local address and verify portable mode by confirming it has no imports, build-only transforms, or server-root asset paths.

## Required evidence before handoff

- The documented start method launches the intended page.
- "Start" produces a visible attack state and enables the response control.
- The response control gives an explicit timing result; no response gives an explicit miss result.
- Retry returns the exact ready state.
- Reduced-motion and narrow-layout behavior remain legible.
- State whether the page was tested in direct-open mode, local-server mode, or both, and name any browser limitation.

## Handoff

State the root cause in plain language, list the launch route, summarize what was verified, and give one concrete next action for the playtester.
