const durationMs = 2200;
const contactAtMs = 1500;
const baseExceptionalMs = 65;
const baseGoodMs = 180;
const elements = {
  arena: document.querySelector("#arena"), jab: document.querySelector("#jab"), cursor: document.querySelector("#cursor"),
  status: document.querySelector("#status"), start: document.querySelector("#start"), block: document.querySelector("#block"),
  retry: document.querySelector("#retry"), outcome: document.querySelector("#outcome"), boot: document.querySelector("#boot-message"),
  bloodState: document.querySelector("#blood-state"), bloodDetail: document.querySelector("#blood-detail"),
  readinessState: document.querySelector("#readiness-state"), readinessDetail: document.querySelector("#readiness-detail"), readinessMeter: document.querySelector("#readiness-meter"),
  armState: document.querySelector("#arm-state"), armDetail: document.querySelector("#arm-detail"), pressureState: document.querySelector("#pressure-state"),
  pressureDetail: document.querySelector("#pressure-detail"), windowCopy: document.querySelector("#window-copy"), safeWindow: document.querySelector("#safe-window"),
  resetPressure: document.querySelector("#reset-pressure"), contact: document.querySelector(".contact"),
};

let frameId = 0;
let startedAt = 0;
let jabTravelPx = 0;
let active = false;
let readiness = 100;
let blockCount = 0;

function selected(name) { return document.querySelector(`input[name="${name}"]:checked`).value; }
function settings() { return { blood: selected("blood"), initialReadiness: selected("readiness"), guard: selected("guard"), arm: selected("arm"), profile: selected("profile") }; }
function legalBlock() { return settings().arm === "usable"; }
function timing() {
  const current = settings();
  const multiplier = (current.guard === "prepared" ? 1.35 : 1) * (current.profile === "assisted" ? 1.3 : 1);
  return { exceptional: Math.round(baseExceptionalMs * multiplier), good: Math.round(baseGoodMs * multiplier) };
}
function blockCost() {
  const current = settings();
  const repeated = 18 + blockCount * 8;
  return Math.round(repeated * (current.blood === "low" ? 1.25 : 1));
}
function writeOutcome(label, title, text, result = "none") {
  elements.outcome.dataset.result = result;
  elements.outcome.innerHTML = `<p class="outcome-label">${label}</p><h3>${title}</h3><p>${text}</p>`;
}
function updateState() {
  const current = settings();
  const nextCost = blockCost();
  const currentTiming = timing();
  elements.bloodState.textContent = current.blood === "low" ? "Low" : "Steady";
  elements.bloodDetail.textContent = current.blood === "low" ? "Amplifies Block strain by 25%" : "No strain amplifier";
  elements.readinessState.textContent = `${readiness} / 100`;
  elements.readinessMeter.style.width = `${readiness}%`;
  elements.readinessDetail.textContent = readiness > 65 ? "Ready" : readiness > 25 ? "Strained" : "Exhausted";
  elements.armState.textContent = current.arm === "usable" ? "Right Arm" : "Right Arm impaired";
  elements.armDetail.textContent = current.arm === "usable" ? "Usable: Block legal" : "Unusable: Block illegal";
  elements.pressureState.textContent = `${blockCount} Block${blockCount === 1 ? "" : "s"}`;
  elements.pressureDetail.textContent = `Next use: ${nextCost} readiness`;
  elements.windowCopy.textContent = `${current.guard === "prepared" ? "Guard Flesh: " : ""}${current.profile === "assisted" ? "Assisted " : "Standard "}window: ±${currentTiming.good} ms. Perfect: ±${currentTiming.exceptional} ms.`;
  const left = 68.18 - (currentTiming.good / durationMs) * 100;
  const width = (currentTiming.good * 2 / durationMs) * 100;
  elements.safeWindow.style.left = `${left}%`;
  elements.safeWindow.style.width = `${width}%`;
}
function resetAttack() {
  cancelAnimationFrame(frameId);
  active = false;
  elements.arena.dataset.phase = "ready";
  elements.jab.style.transform = "translateX(0)";
  elements.cursor.style.left = "0%";
  elements.status.textContent = "Ready when you are.";
  elements.start.hidden = false;
  elements.start.disabled = false;
  elements.block.disabled = true;
  elements.retry.hidden = true;
  updateState();
  writeOutcome("What happened", "Read the situation first.", "Choose a pressure state, then start Anna's attack.");
}
function resetPressure() {
  readiness = settings().initialReadiness === "fresh" ? 100 : 58;
  blockCount = 0;
  resetAttack();
}
function resolve(offset, noBlock = false, unavailable = false) {
  active = false;
  cancelAnimationFrame(frameId);
  elements.arena.dataset.phase = "resolved";
  elements.block.disabled = true;
  elements.start.hidden = true;
  elements.retry.hidden = false;
  if (unavailable) {
    elements.status.textContent = "Block unavailable.";
    writeOutcome("Source legality", "The jab lands.", "Your Right Arm is unusable, so readiness and timing cannot make Block legal. The original 8 Torso damage lands.", "miss");
    return;
  }
  if (noBlock) {
    readiness = Math.min(100, readiness + 12);
    elements.status.textContent = "The jab lands.";
    updateState();
    writeOutcome("Forgo Block", "The jab lands; pressure eases.", "No Block was attempted, so the original 8 Torso damage lands. After the threat resolved, readiness recovered by 12 and Block repetition did not grow.", "miss");
    return;
  }
  const currentTiming = timing();
  const absoluteOffset = Math.abs(offset);
  const direction = offset < 0 ? "early" : offset > 0 ? "late" : "on time";
  const cost = blockCost();
  readiness = Math.max(0, readiness - cost);
  blockCount += 1;
  updateState();
  if (absoluteOffset <= currentTiming.exceptional) {
    elements.status.textContent = "Exceptional Block.";
    writeOutcome(`You were ${direction}`, "Exceptional Block.", `Signed timing: ${offset} ms. Block used ${cost} readiness; the jab is heavily reduced from 8 to 4 Torso damage. Next Block costs more because repeated Block pressure is visible.`, "exceptional");
  } else if (absoluteOffset <= currentTiming.good) {
    elements.status.textContent = "Solid Block.";
    writeOutcome(`You were ${direction}`, "Solid Block.", `Signed timing: ${offset} ms. Block used ${cost} readiness; the jab is reduced from 8 to 6 Torso damage. Your Right Arm remains the required source.`, "good");
  } else {
    elements.status.textContent = "The jab lands.";
    writeOutcome(`You were ${direction}`, "The jab lands.", `Signed timing: ${offset} ms falls outside the visible window. The original 8 Torso damage lands. This ordinary miss adds no extra source damage.`, "miss");
  }
}
function animate(now) {
  if (!active) return;
  const elapsed = now - startedAt;
  const progress = Math.min(1, elapsed / contactAtMs);
  elements.jab.style.transform = `translateX(${jabTravelPx * progress}px)`;
  elements.cursor.style.left = `${(elapsed / durationMs) * 100}%`;
  if (elapsed >= contactAtMs) { elements.arena.dataset.phase = "contact"; elements.status.textContent = "NOW — Block!"; }
  if (elapsed < durationMs) frameId = requestAnimationFrame(animate);
  else resolve(durationMs - contactAtMs, true, !legalBlock());
}
function begin() {
  const jabBox = elements.jab.getBoundingClientRect();
  const contactBox = elements.contact.getBoundingClientRect();
  jabTravelPx = contactBox.left - jabBox.left;
  active = true;
  elements.arena.dataset.phase = "incoming";
  elements.jab.style.transform = "translateX(0)";
  elements.cursor.style.left = "0%";
  startedAt = performance.now();
  elements.start.disabled = true;
  elements.block.disabled = !legalBlock();
  elements.status.textContent = legalBlock() ? "Watch the blue jab." : "Block is unavailable: Right Arm impaired.";
  writeOutcome("Incoming threat", legalBlock() ? "Block at the red line." : "Source unavailable.", legalBlock() ? `This Block would use ${blockCost()} readiness. ${elements.windowCopy.textContent}` : "The incoming attack still resolves, but no timing input can replace an unusable body source.");
  frameId = requestAnimationFrame(animate);
}
function blockNow() { if (active && legalBlock()) resolve(Math.round(performance.now() - startedAt - contactAtMs)); }

const required = Object.values(elements).every(Boolean);
if (!required) throw new Error("The demo page is missing a required control element.");
document.querySelectorAll("input").forEach((input) => input.addEventListener("change", () => { if (!active) resetPressure(); }));
elements.start.addEventListener("click", begin);
elements.block.addEventListener("click", blockNow);
elements.retry.addEventListener("click", resetAttack);
elements.resetPressure.addEventListener("click", resetPressure);
window.addEventListener("keydown", (event) => { if (event.code === "Space" && active && legalBlock()) { event.preventDefault(); blockNow(); } });
elements.boot.hidden = true;
resetPressure();
