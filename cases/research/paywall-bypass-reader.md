# 自动绕过付费墙阅读文章

**Automated Paywall Bypass Article Reader**

> 💬 *From the Open Minis community — shared by **oneasai** on 2026-03-22*

---

## 🎯 痛点 / Pain Point

**中文：** 财新、WSJ 等优质媒体的深度文章需要付费订阅，无法直接阅读。

**English:** Quality long-form articles from Caixin, WSJ, etc. are locked behind paywalls.

---

## 💡 做了什么 / What It Does

**中文：** 将付费墙绕过脚本交给 Minis 分析，让它自动将付费文章链接替换为公开镜像/档案馆链接，实现在对话内直接阅读原本需付费的内容。

**English:** Hands Minis a paywall-bypass script, which then automatically rewrites paywalled article URLs to public archive/mirror links — allowing full article reading directly inside the chat.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| `built-in (browser_use)` | — |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
这篇文章需要付费才能看：[URL]。请帮我找到公开可访问的版本并总结主要观点。
```

**English:**
```
This article is paywalled: [URL]. Find a publicly accessible version and summarize the key points.
```

---

## ⚙️ 配置要求 / Requirements

- [ ] 无需额外配置，Minis 内置浏览器能力
- [ ] 部分内容依赖公开档案馆是否已收录

---

## 🏷 标签 / Tags

`browser` `automation` `reading` `paywall`

---

## 👤 贡献者 / Contributor

来自 Open Minis Telegram 社区 / From the Open Minis Telegram community

原始分享者 / Original sharer: **oneasai**

---

## 📅 验证时间 / Last Verified

2026-03-22
