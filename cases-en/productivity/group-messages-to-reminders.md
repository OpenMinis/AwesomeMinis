# Auto-Extract Key Info from Group Messages → Reminders

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-11 / appinn.com · 2026-03-28*

---

## 🎯 Pain Point

High-volume group chats bury important bug reports, feature requests, and action items in casual conversation — manually monitoring them is exhausting and unreliable.

---

## 💡 What It Does

Minis uses `tg-hub` to synchronize Telegram group messages into a local SQLite database, identifies bug reports, feature requests, and action items, deduplicates them against existing Reminders, and writes new tasks to the system Reminders app. After fixes are merged, Minis can compare the tasks with the codebase and mark completed items.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| `tg-hub` | Synchronize and query Telegram group messages |
| Built-in (`apple-reminders`) | Write to Reminders |

---

## 💬 Example Prompt


```
Pull the last 24 hours of messages from the Open Minis TG group,
extract bug reports and feature requests,
deduplicate against existing Reminders,
and write new items to the "Minis" reminder list.
```

---


## 📸 Screenshots

![Screenshot](../../assets/screenshots/group-messages-to-reminders.jpg)

*📷 Group messages are pouring in → AI automatically organizes → Write system reminder → Completion against code base mark · @wsvn53 via appinn.com · 2026-03-11*

## ⚙️ Requirements

- [ ] `tg-hub` skill installed
- [ ] Complete the first Telegram account login interactively in Terminal; the session is then persisted
- [ ] Configure your own `TG_API_ID` and `TG_API_HASH` when possible; built-in public credentials are only a fallback
- [ ] Sync or refresh the target group into `tg-hub`'s local SQLite database before running offline searches
- [ ] Reminders permission granted to Minis

---

## 👤 Contributor

[@wsvn53](https://x.com/wsvn53) · [appinn.com](https://www.appinn.com/iphone-automation-11-real-use-cases/)

## 📅 Last Verified

2026-03-11
