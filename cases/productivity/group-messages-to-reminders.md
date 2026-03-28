# 群消息自动提取重点写入提醒事项

**Auto-Extract Key Info from Group Messages → Reminders**

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-11 / appinn.com · 2026-03-28*

---

## 🎯 痛点 / Pain Point

**中文：** 社群消息量大，重要的 Bug 反馈、需求、待办事项混在闲聊里，需要人工盯着筛选，容易遗漏。

**English:** High-volume group chats bury important bug reports, feature requests, and action items in casual conversation — manually monitoring them is exhausting and unreliable.

---

## 💡 做了什么 / What It Does

**中文：** Minis 通过 `tg-hub` 拉取 Telegram 群消息，自动识别其中的 Bug 反馈、功能需求和待办事项，去重后写入系统提醒事项（Reminders），后续修复完成后还能对照代码库自动标记完成。

**English:** Minis uses `tg-hub` to pull Telegram group messages, automatically identifies bug reports, feature requests, and action items, deduplicates against existing Reminders, and writes new tasks to the system Reminders app. When fixes are merged, it can auto-mark items as done by checking the codebase.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| `tg-hub` | 拉取群消息 / Fetch group messages |
| Built-in (`apple-reminders`) | 写入提醒事项 / Write to Reminders |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
从 Open Minis TG 群拉取最近 24 小时的消息，
提取其中的 Bug 反馈和功能需求，
与现有提醒事项去重后，将新条目写入「Minis」提醒列表。
```

**English:**
```
Pull the last 24 hours of messages from the Open Minis TG group,
extract bug reports and feature requests,
deduplicate against existing Reminders,
and write new items to the "Minis" reminder list.
```

---

## ⚙️ 配置要求 / Requirements

- [ ] `tg-hub` skill 已安装，Telegram 账号已登录
- [ ] Reminders 权限已授予 Minis

---

## 👤 贡献者 / Contributor

[@wsvn53](https://x.com/wsvn53) · [appinn.com](https://www.appinn.com/iphone-automation-11-real-use-cases/)

## 📅 Last Verified

2026-03-11
