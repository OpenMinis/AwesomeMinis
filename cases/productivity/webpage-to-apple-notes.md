# 网页内容自动整理成 Apple Notes 笔记

**Web Page → Auto-Organized Apple Notes**

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-11 / appinn.com · 2026-03-28*

---

## 🎯 痛点 / Pain Point

**中文：** 看到有价值的 GitHub 项目或技术文档，想保存成笔记，但直接收藏链接以后根本不会再看，手动整理又太耗时。

**English:** When you find a valuable GitHub project or technical doc, bookmarking the link means you'll never read it again — but manually organizing it into notes takes too long.

---

## 💡 做了什么 / What It Does

**中文：** 把网页链接发给 Minis，它自动抓取内容、提炼要点、整理成结构化 Markdown 笔记，并通过 `apple-notes` 写入 iOS 备忘录，随时可查。

**English:** Send a URL to Minis, it fetches the content, extracts key points, formats them as structured Markdown notes, and writes them to Apple Notes via `apple-notes` — ready to read anytime.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in (browser_use) | 抓取网页内容 / Fetch web page content |
| Built-in (`apple-notes`) | 写入 Apple Notes / Write to Apple Notes |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
帮我把这个 GitHub 项目整理成学习笔记，保存到备忘录：
https://github.com/jackwener/xiaohongshu-cli
```

**English:**
```
Summarize this GitHub project into study notes and save to Apple Notes:
https://github.com/jackwener/xiaohongshu-cli
```

---

## ⚙️ 配置要求 / Requirements

- [ ] Apple Notes 权限已授予 Minis

---

## 💡 Tips

- 支持任意网页：技术文档、新闻文章、产品介绍页
- 可以指定笔记格式，如"用 Markdown 标题分节"或"只提炼 5 个要点"

---

## 👤 贡献者 / Contributor

[@wsvn53](https://x.com/wsvn53) · [appinn.com](https://www.appinn.com/iphone-automation-11-real-use-cases/)

## 📅 Last Verified

2026-03-11
