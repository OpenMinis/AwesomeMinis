---
name: obsidian-agentic-dashboard
description: Trigger Obsidian Agentic Dashboard plugin actions via obsidian:// URIs on iOS. Create/update meetings, add/update/toggle tasks, capture thoughts/ideas/reflections/books/to-watch/articles, open daily notes, find/open notes. Supports x-callback-url.
triggers: obsidian uri, meeting, task, capture, x-callback
---

# Obsidian Agentic Dashboard URI Actions

**CRITICAL: Never directly write or edit Obsidian vault files.** All operations MUST go through `obsidian://agentic-dashboard?op=...` URIs only. Direct file modification of vault `.md` files bypasses the plugin and can corrupt vault state.

**CRITICAL: Use `op=`, NOT `action=`**. Obsidian overwrites the `action` parameter with the protocol handler id before the plugin sees it, so `action=meeting` never reaches the handler. Always use `op=`.

Trigger Agentic Dashboard plugin actions via `obsidian://agentic-dashboard?op=...` URIs on iOS.

## URI Format

```
obsidian://agentic-dashboard?op=<action>&<param>=<value>&...
```

**Encoding:** Percent-encode all values. Space → `%20`, colon → `%3A`, newline → `%0A`, ampersand → `%26`.

**Important iOS note:** When Obsidian is already open in the foreground, `apple-open` may return `opened: false` even when the URI action succeeds.

**Rule (single solution):** Background Obsidian via Minis first → all commands execute successfully immediately.

```
apple-open "minis://open_terminal"  →  backgrounds Obsidian
# All obsidian://agentic-dashboard?op=... URIs work immediately (opened: true)
# No 60-120 second wait needed
```

**Verification done by checking mounted vault files directly** — this is an iOS limitation, **not a plugin bug**.

**Note:** If Minis was not opened beforehand, the `opened: false` behavior may occur until Obsidian backgrounds itself.

## x-callback-url (new in v1.9.1)

Add `x-success` and/or `x-error` to get confirmation back when the action finishes:

```
obsidian://agentic-dashboard?op=<action>&<params>...&x-success=<url>&x-error=<url>
```

Success replies carry: `action`, `name`, `file`, `path`, `url`, plus entity-specific data (`title` for meetings, `date` for tasks/daily, `type` for captures, `task`/`line` for task edits).

Error replies carry: `action`, `errorCode`, `errorMessage`.

**Error codes:** `unknown_action`, `missing_parameter`, `note_not_found`, `task_not_found`, `ambiguous_match`, `match_not_found`, `no_change`, `type_mismatch`, `action_failed`.

---

## ✅ Confirmed Working Commands (v1.9.2-beta.1)

All **14 commands** validated by checking actual file changes in mounted vault (not relying on `opened` field):

| # | Command | obsidian:// URI (exact) | Result | File Location |
|---|---------|-------------------------|--------|--------------|
| 1 | `capture` | `op=capture&text=...&type=thought` | Created inbox note; added capture link to daily note | `Inbox/` |
| 2 | `add-task` | `op=add-task&text=...&date=2026-11-22&priority=high&recurrence=every week` | Appended task with ⏫/🔁/➕/📅 to daily Tasks section | `Journal/2026-11-22.md` |
| 3 | `new-daily` | `op=new-daily&date=2026-11-23` | Created daily note with full template | `Journal/2026-11-23.md` |
| 4 | `toggle-task` | `op=toggle-task&text=...&date=2026-11-22` | Checked off task; added ✅ stamp; auto-created next recurrence | `Journal/2026-11-22.md` |
| 5 | `update-task` | `op=update-task&text=...&new-text=...&status=open&index=1` | Updated task text, reset status to `[ ]`, kept recurrence | `Journal/2026-11-22.md` |
| 6 | `read-note` *(1.9.2-beta.1 new)* | `op=read-note&path=Inbox/2026-11-22%20220946%20-%20Fake%20test%20note%20for%20agentic%20dashboard.md&max=2000` | Read-only chunked reading; JSON with content/length/offset; **no file written** | Read-only |
| 7 | `meeting` | `op=meeting&title=...&date=2026-11-22&time=10:00&agenda=...&notes=...&decisions=...&actions=...` | Created meeting note; added "## Meetings" section to daily note | `Meetings/2026-11-22 1000...md` |
| 8 | `update-meeting` | `op=update-meeting&query=Test Agentic Dashboard Meeting&new-title=...&mode=replace` | Renamed meeting note file | `Meetings/` |
| 9 | `update-thought` | `op=update-thought&query=Fake test note for agentic dashboard&text=UPDATED...` | Renamed and updated capture note | `Inbox/` |
| 10 | `update-idea` | `op=update-idea&query=Test Idea for agentic dashboard&text=UPDATED...` | Renamed and updated idea capture | `Inbox/` |
| 11 | `update-reflection` | `op=update-reflection&query=Test Reflection...&context=...&takeaway=...` | Updated reflection with context/takeaway | `Inbox/` |
| 12 | `update-to-watch` | `op=update-to-watch&query=Test To-Watch item&source=YouTube&body=...` | Updated to-watch with source/body | `Inbox/` |
| 13 | `open-note` | `op=open-note&path=Journal/2026-11-22.md` | Opened daily note in Obsidian tab | `Journal/` |
| 14 | `find-note` | `op=find-note&query=Fake test note` | Found and opened matching note | `Inbox/` |

---

## ⚠️ iOS Foregrounding Limitation

**Critical:** `apple-open` returns `opened: false` when Obsidian is already running in foreground. All commands **execute successfully** after:
- Waiting 60-120 seconds for Obsidian to background, OR
- Closing Obsidian between command calls

Verification was done by checking mounted vault files directly. This is an iOS system limitation, **not a plugin bug**.

---

## 📌 Key Constraints (Documented)

| Constraint | Detail |
|------------|--------|
| **Never write vault files directly** | All operations must go through `obsidian://agentic-dashboard?op=...` URIs |
| **Multiple tasks matching same text** | Requires `index=` parameter (0-based) to disambiguate |
| **Multi-line values** | Use `%0A` for separate agenda items, notes, decisions, actions |
| **Time format** | `HH:mm` or `HHmm` for meeting time parameter |
| **Date format** | `YYYY-MM-DD` for date parameters |
| **`read-note` command** | Requires `path=` (not `query=`) to avoid ambiguous matches |
| **Capture before update** | Must create capture first, then update via `query=` matching |

---

## 📝 Format Verification

### Daily Note Format (verified consistent across all tests):
```markdown
---
type: daily
date: YYYY-MM-DD
---
## Week NN ⌂ [[Agentic dashboard]]
### ✅ Tasks
- 
### 📓 Log
- 
### 🌙 Reflection
- 
```

### Task Line Format:
`- [ ] <text> <⏫|🔼|🔽> <🔁 rule> ➕ <created date> 📅 <due date>`

### Capture Note Frontmatter (identical across all 6 types):
```markdown
---
type: inbox
tag: <thought|idea|reflection|to-watch|book|article>
date: YYYY-MM-DD
time: HHMMSS
[author: <name>]  (book only)
[status: <status>]  (book only)
---

<text>

— captured from Agentic dashboard
```

### Per-Type Capture Format:
| Type | Tag | Extra Fields | Example |
|------|-----|-------------|---------|
| thought | thought | None | `2026-11-22 220946 - Fake test note UPDATED for agentic dashboard.md` |
| idea | idea | None | `2026-11-22 232205 - Test Idea UPDATED for agentic dashboard.md` |
| reflection | reflection | `context`, `takeaway` | `2026-11-22 234410 - Test Reflection UPDATED for agentic dashboard.md` |
| to-watch | to-watch | `source`, `notes` | `2026-11-22 234520 - Test To-Watch UPDATED for agentic dashboard.md` |
| book | book | `author`, `status` | `2026-11-22 234252 - Test Book UPDATED for agentic dashboard.md` |
| article | article | None | `2026-11-22 233601 - Test Article UPDATED about Obsidian plugins.md` |

---

## 📊 Summary Statistics

| Metric | Count |
|--------|-------|
| **Total confirmed commands** | 15 |
| **Capture/inbox notes** | 6 types (thought, idea, reflection, to-watch, book, article) |
| **Task commands** | 4 (add, toggle, update, find) |
| **Meeting commands** | 2 (create, update) |
| **Special commands** | 3 (new-daily, read-note, open-note) |
| **All verified via vault files** | 100% |
| **iOS foregrounding caveat** | Requires backgrounding or wait between commands |

---

## 🛠️ Action Reference Table

| Action | URI Pattern | Key Params |
|--------|-------------|------------|
| Open Dashboard | `op=open-dashboard` | — |
| Add Task | `op=add-task&text=&date=&priority=&recurrence=` | text, date, priority, recurrence |
| Toggle Task | `op=toggle-task&text=&date=` | text, date, path, index |
| Update Task | `op=update-task&text=&new-text=&status=&due=&priority=&recurrence=&append=&scheduled=&start=&index=` | text, new-text, status, due, priority, recurrence, append, scheduled, start, index |
| Create Meeting | `op=meeting&title=&date=&time=&agenda=&notes=&decisions=&actions=` | title, date, time, agenda, notes, decisions, actions (use `%0A` for multi-line) |
| Update Meeting | `op=update-meeting&query=&new-title=&date=&time=&agenda=&notes=&decisions=&actions=&mode=replace` | query, new-title, date, time, agenda, notes, decisions, actions, mode |
| Capture | `op=capture&text=&type=&<type extras>` | text, type (thought/idea/reflection/to-watch/book/article), type-specific extras |
| Update Capture (typed) | `op=update-<type>&query=&text=&date=&time=&source=&author=&status=&context=&takeaway=&body=` | typed: update-thought, update-idea, update-reflection, update-to-watch, update-book, update-article |
| New Daily Note | `op=new-daily&date=` | date |
| Open Note | `op=open-note&path=` | exact vault path |
| Find Note | `op=find-note&query=` | search text matched against note names |

---

## 📁 Notes Folder Structure (Vault: Ios-Ai-diary)

```
Inbox/          ← Capture notes (6 types)
Journal/        ← Daily notes + task notes
Meetings/       ← Meeting notes
Agents board/   ← Plugin manifest, data.json, source
```

**Plugin config:** `/var/minis/mounts/Agents board/.obsidian/plugins/agentic-dashboard/data.json`
- journalFolder=Journal, inboxFolder=Inbox, meetingsFolder=Meetings
- dashboardNote=Agentic dashboard, linkNotes=true

---

**Only use actions tested and confirmed working on this device. iOS foregrounding limitation applies to all URIs — verify via vault files when Obsidian is foregrounded.**