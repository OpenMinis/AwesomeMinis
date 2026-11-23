# Agent-Run Obsidian Vault (Minis + Agentic Dashboard)

> 💬 *Real-world workflow: use Minis on iPhone to write tasks, daily captures, and meeting notes as Markdown to an Obsidian vault, then the Agentic Dashboard plugin renders them as a live dashboard — tasks, calendar, stats, meetings, recents, inbox — refreshing automatically as Minis writes.*

---

## 🎯 Pain Point

Managing tasks, daily notes, and meeting records across different apps is fragmented: tasks live in Reminders, notes in Notes, meetings in Calendar. You want a single, local-first Markdown vault that you fully own, accessible on iPhone and desktop, where an AI agent can write structured entries and a dashboard renders them live — without complex databases, sync services, or vendor lock-in.

---

## 💡 What It Does

Mount an Obsidian vault into Minis via the external folder mount. Minis writes tasks, daily captures (thoughts, ideas, reflections, to-watch, books, articles), and meeting notes as plain Markdown using the Agentic Dashboard plugin's `obsidian://agentic-dashboard?op=...` URI commands. The Agentic Dashboard plugin (free, no dependencies, no Dataview, works on desktop + mobile) reads those files and renders a live dashboard: tasks with priority/recurrence, calendar view, statistics, meetings, recent notes, inbox — auto-refreshing as Minis writes.

**Key iOS Discovery:** When Obsidian is in the foreground, `apple-open` returns `opened: false` and URI commands don't execute. **Single Rule:** `apple-open "minis://open_terminal"` backgrounds Obsidian → all subsequent `obsidian://` URIs execute immediately (`opened: true`). No 2-minute wait needed.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| `obsidian-agentic-dashboard` | Execute Agentic Dashboard plugin commands via obsidian:// URIs (capture, add-task, toggle-task, update-task, find-note, open-dashboard, meeting, update-meeting) |
| `plugin-command-tester` | Systematic verification of plugin commands against mounted vault files |

---

## 📋 How to Use

1. **Install Obsidian on iPhone** — Create or open a vault in the Files app (On My iPhone → Obsidian).
2. **Install Agentic Dashboard plugin** — In Obsidian: Settings → Community Plugins → Browse → "Agentic Dashboard" → Install → Enable. Version 1.9.3+ required.
3. **Mount vault in Minis** — Minis Settings → Mount External Folders → choose your Obsidian vault folder. **Recommended: toggle OFF write option** (plugin commands handle writing with correct format).
4. **Install skills in Minis** — Add `obsidian-agentic-dashboard` and `plugin-command-tester` skills (they include the single-rule backgrounding fix).
5. **Write a task** — In Minis chat: "Add a task: Review PR #11 tomorrow high priority every week"
6. **Capture a thought** — "Capture this thought: The single backgrounding rule eliminates all wait scripts"
7. **Create a meeting note** — "Create meeting: Project kickoff tomorrow 10:00, agenda: scope, timeline, owners"
8. **Open dashboard** — "Open the Agentic Dashboard in Obsidian" (or tap the dashboard note in Obsidian)
9. **Verify in Obsidian** — Open Obsidian app → see live dashboard with tasks, calendar, meetings, inbox updating in real time

---

## 💬 Example Prompts

**Add a recurring task:**

```text
Add a task: Review Agentic Dashboard plugin commands, date: tomorrow, priority: high, recurrence: every week
```

**Capture a thought:**

```text
Capture thought: The Minis backgrounding trick backgrounds Obsidian instantly — no more wait loops needed
```

**Capture a reflection with context and takeaway:**

```text
Capture reflection: Testing v1.9.3 commands revealed the single rule. Context: iOS foregrounding blocks URIs. Takeaway: Always background Obsidian via Minis first.
```

**Create a meeting note:**

```text
Create meeting: Weekly sync, date: 2026-11-25, time: 09:00, agenda: Review PR status, blockers, next week priorities
```

**Open the live dashboard:**

```text
Open the Agentic Dashboard in Obsidian
```

**Find a note in the vault:**

```text
Find note: backgrounding rule
```

---

## 📤 Expected Output

- Task appears in daily journal (`Journal/YYYY-MM-DD.md`) with checkbox, priority emoji (⏫/🔼/🔽), recurrence rule (🔁), created date (➕), due date (📅)
- Capture appears in `Inbox/` as timestamped Markdown with frontmatter (`type: inbox`, `tag: thought|idea|reflection|to-watch|book|article`, `date`, `time`, plus type-specific fields)
- Meeting appears in `Meetings/` with agenda, notes, decisions, actions sections; also linked in daily note under `## Meetings`
- Dashboard note (`Agentic dashboard.md`) renders live view: Tasks, Calendar, Stats, Meetings, Recents, Inbox
- All files are plain Markdown — portable, version-controllable, readable in any editor
- Commands execute immediately after `apple-open "minis://open_terminal"` (no 2-min wait)

---

## 📸 Screenshots

**Minis executes capture command — vault file created instantly:**

![Minis capture command execution](assets/screenshots/obsidian-vault-agent-dashboard-capture.jpg)

**Agentic Dashboard live view in Obsidian showing tasks, calendar, meetings, inbox:**

![Agentic Dashboard live view](assets/screenshots/obsidian-vault-agent-dashboard-dashboard.jpg)

**Task toggle and update verified in daily journal Markdown:**

![Task toggle and update in journal](assets/screenshots/obsidian-vault-agent-dashboard-tasks.jpg)

---

## ⚙️ Requirements

- [ ] iPhone with Minis installed
- [ ] iPhone with Obsidian installed
- [ ] Obsidian vault created in Files app (On My iPhone → Obsidian)
- [ ] Agentic Dashboard plugin v1.9.3+ installed and enabled in Obsidian
- [ ] Vault mounted in Minis (Settings → Mount External Folders)
- [ ] `obsidian-agentic-dashboard` skill installed in Minis
- [ ] `plugin-command-tester` skill installed in Minis (for verification)

---

## 💡 Tips & Variations

- **Read-only mount recommended**: Toggle OFF write in Minis mount settings — plugin URI commands write with correct format to the right directories; direct file writes risk wrong format/location.
- **Background first, then command**: Always run `apple-open "minis://open_terminal"` before any `obsidian://agentic-dashboard?op=...` command if Obsidian was recently used.
- **Multiple matching tasks**: Use `index=` parameter (0-based) with `toggle-task` or `update-task` when multiple tasks share the same text.
- **Multi-line values**: Use `%0A` for line breaks in `meeting` command (agenda, notes, decisions, actions).
- **Date/time formats**: Date = `YYYY-MM-DD`, Time = `HH:mm` or `HHmm`.
- **Works on desktop too**: Same vault + plugin works on macOS/Windows/Linux Obsidian — dashboard syncs via vault.

---

## 👤 Contributor

Submitted by: [@faizulahasun-cloud](https://github.com/faizulahasun-cloud)

---

## 📅 Last Verified

2026-11
