# Gym Check-In → Auto Weight Progression + Apple Health

> A closed loop for gym strength training: Minis plans each session from your real history, you log the workout with taps only (no typing), and Minis computes your next weights with deterministic progression rules — then writes the workout to Apple Health.

---

## 🎯 Pain Point

Gym training lives in three disconnected places: a plan that goes stale after two weeks, numbers scattered across your head or chat history, and a health app that never knows you trained. Every session you re-type weights and reps into a notes app, forget what you lifted last time, and "progressive overload" stays a slogan because nobody does the arithmetic between sets.

---

## 💡 What It Does

1. **Before the session** — Minis reads your training plan + workout log + gym equipment list, decides which rotation day you're on (e.g. D1 squat / D2 push / D3 pull / D4 hip hinge), and generates a single-page check-in form pre-filled with today's exercises, target weights, sets and reps.
2. **During the session** — you record everything with taps: per-set reps steppers, last-set RIR chips (reps in reserve), pain flags, cardio machine and duration. The page autosaves, so an interrupted workout is never lost.
3. **After the session** — one tap exports a compact text block; you paste it back to Minis. It parses the text into structured JSONL records and writes workout calories (and treadmill distance) to Apple Health, with estimates explicitly labeled and duplicate writes blocked.
4. **The next session** — a deterministic double-progression engine (included script) suggests the next weight for every lift: two consecutive sessions topping your rep range with reps in reserve → add one step; failing the range or grinding to RPE 9+ → drop one step. The plan updates itself from evidence.

---

## 🛠 Skills Needed

| Skill | Purpose |
|-------|---------|
| `health-training-checkin` | The full loop: session planning, zero-typing check-in form, parsing, progression engine, Apple Health writes |
| Built-in (`apple-healthkit`) | Write active energy / workout data to Apple Health |

---

## 📋 How to Use

1. **Open Minis and install the `health-training-checkin` skill** (from the MinisSkills collection).
2. **One-time setup** — tell Minis your goal (fat loss / muscle / health), weekly availability, any injury limits, and the machines at your gym (a photo of the machine area works great). Minis creates your training directory: plan, equipment catalog, session log.
3. **Each training day** — just say "今天练什么" (what's today's session). Minis opens your pre-filled check-in form.
4. **Train and tap** — adjust reps/RIR as you go; hit "完成并导出" and paste the export back to Minis.
5. **Ask anytime** — "该加重量了吗" (should I go heavier?) returns each lift's next weight with the reasoning.

---

## 💬 Example Prompt

```
(First run)
I want to train at the gym 3-4 times a week for fat loss and strength.
Here's my gym's machine area (photo). Build me a rolling 4-day rotation plan
and set up the check-in workflow.

(Each session)
今天练什么？  →  (Minis opens the pre-filled check-in form)
                (You tap through the workout, export, paste back)

(Anytime)
该加重量了吗？  →  (Minis runs the progression engine and answers per lift)
```

---

## 📤 Expected Output

- A one-page, offline-capable check-in form (all tap controls, 44px+ targets, autosaved) — opens in under 5 seconds.
- After pasting the export: a parsed session record (JSONL) + a one-line confirmation of what was written to Apple Health (~10 seconds).
- Progression answers like: *"Smith squat: 15 kg/side × 2×10 + back-off last week, 9 reps today at RIR 2 — hold one more session, aim 3×10 next time."* Each suggestion cites the rule and the evidence.

---

## ⚙️ Configuration / Requirements

- [ ] Minis with a model API key configured
- [ ] HealthKit **write** permission granted to Minis (active energy; optional: walking distance)
- [ ] The `health-training-checkin` skill installed (includes `progression.py`, a stdlib-only Python engine — no extra dependencies)
- [ ] First-run conversation to define your rotation, equipment and baselines (unknown weights get tested, never guessed)

---

## 💡 Tips & Variations

- **Back-off sets work**: heavy sets + a lighter back-off set is fine — the engine judges only the heaviest segment, matching how real strength programs run.
- **Smith machine loads are recorded per side** (plate load), and bar weight is never guessed — suggestions print as `kg/side`.
- **Assist machines progress inversely**: less assistance = harder, and the engine suggests reducing it.
- **Pain is not a training signal**: the form has a one-tap pain flag; sharp pain shows a stop warning and is written into the record for later review.
- **Every 4–6 weeks** ask Minis for a training review: density vs. recovery caps, progression stalls, and a deload week — it keeps the plan versioned with a changelog so you can see *why* it changed.
- Works for any split — push/pull/legs, upper/lower, or full body. The rotation is configured, not hard-coded.

---

## 👤 Author

Submitted by: [@justFI](https://github.com/justFI)

---

## 📅 Last Verified

2026-09
