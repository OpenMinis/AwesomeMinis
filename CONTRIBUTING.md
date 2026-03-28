# Contributing to Awesome Minis

Thank you for helping grow the Minis community! 🎉

This guide explains how to add a new use case or improve an existing one.

---

## ✅ What Makes a Good Use Case

A great Awesome Minis use case:

- **Is real** — you have personally tested and verified it works
- **Solves a genuine problem** — it makes life meaningfully better, not just technically possible
- **Is replicable** — someone else can follow your steps and get the same result
- **Uses Minis specifically** — it leverages Minis' unique capabilities (shell, HealthKit, Skills, Apple integrations, etc.)

---

## 📁 Repository Structure

```
AwesomeMinis/
├── README.md                  # Main index — the curated list
├── CONTRIBUTING.md            # This file
├── CASE_TEMPLATE.md           # Template for new use cases
├── cases/
│   ├── health/                # Health & Wellness
│   ├── productivity/          # Productivity & Automation
│   ├── research/              # Data & Research
│   ├── creative/              # Creative & Content
│   ├── smarthome/             # Smart Home & IoT
│   ├── social/                # Social Media & Communication
│   ├── finance/               # Finance & Tracking
│   └── developer/             # Developer Tools
└── assets/
    └── screenshots/           # Optional screenshots for cases
```

---

## 🚀 How to Submit a New Use Case

### Step 1 — Pick a Category

Choose the most relevant folder under `cases/`. If your use case doesn't fit any existing category, suggest a new one in your PR description.

### Step 2 — Create Your Case File

Copy [CASE_TEMPLATE.md](CASE_TEMPLATE.md) into the appropriate folder:

```
cases/<category>/<your-use-case-name>.md
```

Use **kebab-case** for filenames (e.g., `morning-news-digest.md`).

### Step 3 — Fill in the Template

Cover these key points (see template for full structure):

| Field | Description |
|-------|-------------|
| **Pain Point** | What problem does this solve? |
| **What It Does** | Brief explanation of the use case |
| **How to Use** | Step-by-step instructions |
| **Example Prompt** | The actual prompt(s) you give Minis |
| **Skills Needed** | Which Minis Skills are required (if any) |
| **Expected Output** | What the result looks like |
| **Tips** | Optional: gotchas, variations, improvements |

### Step 4 — Add a Row to README.md

Add your use case to the relevant category table in `README.md`:

```markdown
| [Your Use Case Name](cases/category/your-file.md) | One-line description | `skill-name` or Built-in |
```

### Step 5 — Open a Pull Request

- **One use case per PR** (preferred)
- PR title format: `Add: <Use Case Name>`
- Briefly describe what the use case does and why it's useful

---

## ✏️ Improving Existing Use Cases

Found an error, outdated instruction, or have a better approach? Open a PR with:

- PR title format: `Fix: <Use Case Name>` or `Improve: <Use Case Name>`
- Describe what changed and why

---

## 🚫 What We Don't Accept

- Use cases you haven't personally tested
- Duplicate submissions with no meaningful difference in approach
- Use cases unrelated to Minis
- Promotional content or spam

---

## 💬 Questions?

Join the community on Telegram or open a GitHub Issue.
