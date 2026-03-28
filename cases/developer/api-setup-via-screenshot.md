# 截图 API 控制台让 Minis 自动配置

**Screenshot API Console for Minis to Auto-Configure**

> 💬 *From the Open Minis community — shared by **小渔 黄** on 2026-03-25*

---

## 🎯 痛点 / Pain Point

**中文：** 国内 AI 平台控制台 UI 混乱，找 API Key 和端点配置要花很长时间。

**English:** Chinese AI platform consoles are cluttered — finding API keys and endpoints takes forever.

---

## 💡 做了什么 / What It Does

**中文：** 当 API 控制台文档混乱难以找到配置项时，直接截图发给 Minis，让它识别图中的 API Key、端点等信息并自动完成配置，省去反复查文档的麻烦。

**English:** When an API console is confusing or hard to navigate, screenshot it and send to Minis. It reads the image, extracts the API key and endpoint, and configures everything automatically.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| `built-in (vision)` | — |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
（附上 API 控制台截图）这是我的 API 控制台截图，请识别其中的 API Key、Base URL 和模型名称，帮我配置好环境变量。
```

**English:**
```
(Attach API console screenshot) This is my API console screenshot. Please identify the API key, base URL, and model name, and configure the environment variables for me.
```

---


## 📸 截图 / Screenshots

![Screenshot by 小渔 黄](../../assets/screenshots/api-setup-via-screenshot.jpg)
*📷 Shared by **小渔 黄** · 2026-03-24*

![Screenshot by 小渔 黄](../../assets/screenshots/api-setup-via-screenshot-2.jpg)
*📷 Shared by **小渔 黄** · 2026-03-25* — 我接的API设置了环境变量。可以用。比起本地部署的声音更好。

## ⚙️ 配置要求 / Requirements

- [ ] 无需额外配置，Minis 内置图像识别能力

---

## 🏷 标签 / Tags

`api` `vision` `ocr` `configuration` `productivity`

---

## 👤 贡献者 / Contributor

来自 Open Minis Telegram 社区 / From the Open Minis Telegram community

原始分享者 / Original sharer: **小渔 黄**

---

## 📅 验证时间 / Last Verified

2026-03-25
