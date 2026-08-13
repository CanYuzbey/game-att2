# Block Movement Demo

This is a disposable local browser demo for communicating one interaction: watch Anna's
blue Jab and press Block when its tip reaches the red line. It also makes the bounded
research variables visible: Blood band, shared readiness, repeated-Block pressure,
Guard preparation, input profile, and Right-Arm legality. It is not the Game att2
runtime, a production UI, or a rules-authority change.

## Open it now

Double-click `start-demo.bat` in this folder. It opens `index.html` directly in your
default browser; no install or web server is needed.

## Optional local-server mode

From the handoff directory:

```powershell
npm install
npm run demo
```

Open the local address printed in the terminal, normally `http://127.0.0.1:5173`.
Choose a situation, use `Start attack`, then `Block` or Space. `Next attack` retains
the readiness and repeated-Block pressure so their effects can be compared. `Reset
drill pressure` returns to the selected starting state.

## Check it

```powershell
npm.cmd run check:demo
```

The demo uses plain JavaScript and CSS and can run without Vite. Vite is included only
as an optional local-server tool. The demo has no backend, telemetry, external asset,
player data, or game-simulator connection. Its values are visual-study examples only;
they do not alter or establish production combat rules.
