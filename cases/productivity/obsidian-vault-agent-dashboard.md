---
type: usecase
title: Agent-Run Obsidian Vault (Minis + Agentic Dashboard)
version: 1.0.0
status: draft
---

# 案例: Agent-Run Obsidian Vault (Minis + Agentic Dashboard)

**提交者:** faizulahasun-cloud  
**PR:** #11 · OpenMinis/AwesomeMinis  
**日期:** 2026-11-23

## 中文概述

本例展示了如何在 iPhone 上使用 Minis 编写任务、日记备忘录和会议记录，然后通过 Agentic Dashboard 插件将这些文件渲染为实时仪表板。

Minis 将 Obsidian vault（在 iOS 文件中可见）作为工作空间；代理编写任务、日常备忘录、会议笔记作为纯 Markdown。在 Obsidian 侧，免费社区插件 Agentic Dashboard（无依赖，无 Dataview，桌面 + 移动端）会实时渲染这些文件——任务、日历、统计、会议、最近项目、收件箱——随着 Minis 的写入而自动刷新。

**已在 iPhone 上个人日常使用，另配桌面端使用**  
**技能文件:** skills/plugin-command-tester/SKILL.md、skills/obsidian-agentic-dashboard/SKILL.md  
**前置条件:** iPhone 安装 Minis + Obsidian，Agentic Dashboard v1.9.3 插件

## English Overview

This use case demonstrates how to use Minis on iPhone to write tasks, daily notes, and meeting notes, which are then rendered as a live dashboard by the Agentic Dashboard plugin.

Minis mounts an Obsidian vault (visible in the iOS Files app) as a workspace; the agent writes tasks, daily captures, and meeting notes as plain Markdown. On the Obsidian side, the free community plugin Agentic Dashboard (no dependencies, no Dataview, desktop + mobile) renders those files as a live dashboard — tasks, calendar, stats, meetings, recents, inbox — refreshing automatically as Minis writes.

**Personally tested and in daily use on iPhone (vault mounted in Minis) plus desktop**  
**Skill files:** skills/plugin-command-tester/SKILL.md, skills/obsidian-agentic-dashboard/SKILL.md  
**Prerequisites:** iPhone with Minis + Obsidian installed, Agentic Dashboard v1.9.3 plugin
# Agent-Run Obsidian Vault — Minis Writes, the Dashboard Renders

> Mount your Obsidian vault into Minis as a workspace: the agent researches and writes tasks, daily notes and captures as plain Markdown, and the free Agentic Dashboard plugin turns them into a live crystal-glass dashboard — fully working on iPhone.

---

## 🎯 Pain Point

Obsidian vaults are just folders of Markdown files, so agents can write into them — but the result is usually a pile of text you have to open and read. There's no structured "at a glance" view of what the agent did: which tasks it added, what it captured to your inbox, what meetings it created. And if you're an iPhone-only user (no desktop tooling), most agent-vault integrations aren't usable at all.

---

## 💡 What It Does

Minis mounts the Obsidian vault as a normal workspace (it's visible in the iOS Files app). You talk to Minis as usual — "add a task for tomorrow", "research X and file it", "log this idea" — and Minis writes plain Markdown into the vault's folders: daily notes (`YYYY-MM-DD.md`), inbox captures, meeting notes.

On the Obsidian side, the free **Agentic Dashboard** plugin picks those files up automatically and renders them as a live dashboard: today's tasks (with checkboxes you can toggle), a month calendar with dots on days that have daily notes, vault stats, today's meetings, recent notes, and the inbox feed. It updates itself as Minis writes — no Dataview, no Templater, no other plugins, works fully on iPhone.

The end result: you chat with your agent on the phone, and open Obsidian to a polished dashboard that already reflects everything the agent did — or never open the editor at all, because the dashboard is the view.

---

## 🛠 Skills Needed

| Skill | Purpose |
|-------|---------|
| None (built-in) | Minis' file tools write plain Markdown through the mounted vault — no extra skill needed |

---

## 📋 How to Use

1. **Store the vault so Files can see it** — keep the vault on-device (or in iCloud) so the folder appears in the iOS Files app.
2. **Mount it in Minis** — add the vault folder as a workspace in Minis; the agent can now read and write its files like any project folder.
3. **Tell Minis the layout once** — e.g. "my daily notes live in `Journal/` as `YYYY-MM-DD.md`, captures go in `Inbox/`, meetings in `Meetings/`. Append tasks as `- [ ] …` lines."
4. **Use it normally** — ask Minis to add tasks, capture ideas, research topics into notes, or create meeting notes. It writes plain Markdown; no special syntax.
5. **Install the dashboard** — in Obsidian: **Settings → Community plugins → Browse → "Agentic Dashboard" → Install → Enable** (free, no dependencies). Turn on "Open dashboard at startup" in its settings.
6. **Point the folders** — in the plugin settings, set the journal / inbox / meetings folder paths to match your layout. Defaults are sensible.
7. **Optional look** — pair with the free **Hermes Crystal** community theme for the matching crystal-glass aesthetic.

---

## 💬 Example Prompt

```text
My vault is mounted as a workspace. Layout: daily notes in Journal/ named YYYY-MM-DD.md,
quick captures in Inbox/, meetings in Meetings/. Append tasks as "- [ ] …" under a
## Tasks heading in the daily note (create it if missing).

1. Add a task "Reply to the accountant" to today's daily note.
2. Research the new EU accessibility rules, then write a short note in Notes/ and
   capture a one-line summary in Inbox/ with frontmatter: type: article, date: today.
3. Create a meeting note for "Design review" today at 14:30 in Meetings/ with
   frontmatter: date, time, tag.
```

---

## 📤 Expected Output

- In Minis: normal agent replies confirming what it wrote (it can list the files it touched).
- In Obsidian: the Agentic Dashboard refreshes within seconds (it listens to vault file changes) and shows the new task in **Tasks today**, the capture in **Inbox** with its type tag, the meeting in **Meetings today**, and a dot on today in the **Calendar**. New daily notes appear as clickable days.

---

## ⚙️ Configuration / Requirements

- [ ] Vault visible in the iOS Files app (on-device or iCloud vault)
- [ ] [Agentic Dashboard](https://github.com/faizulahasun-cloud/agentic-dashboard) plugin installed and enabled — free, no plugin dependencies, desktop + mobile
- [ ] Vault layout shared with Minis (folder names + daily note format) — the plugin's folder settings must match
- [ ] Optional: [Hermes Crystal](https://github.com/faizulahasun-cloud/hermes-crystal) theme for the matching look

---

## 💡 Tips & Variations

- **Plain Markdown is the contract** — the agent writes normal files; the dashboard reads frontmatter fields (`type`, `date`, `time`, `tag`) and checkbox lines. Keep agent output simple and it just works.
- **Deep links instead of chat** — the plugin registers `obsidian://agentic-dashboard?action=…` URIs, so iOS Shortcuts can add tasks or capture text into the vault without opening any editor (parameters: `action=add-task&text=…&date=…`, `action=capture&text=…&type=idea`, `action=meeting&title=…&time=…`).
- **Desktop agents too** — on desktop, the same vault works with the official Obsidian CLI (`obsidian agentic-dashboard:add-task text="…" vault="MyVault"`), so PC-side agents can drive the same dashboard.
- **Variation**: use Minis for a weekly review — it reads the week's daily notes from the vault, summarizes progress, and writes the summary as an inbox capture that appears right on the dashboard.

---

## 👤 Author

Submitted by: [@faizulahasun-cloud](https://github.com/faizulahasun-cloud)

---

## 📅 Last Verified

2026-11
