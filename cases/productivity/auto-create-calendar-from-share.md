# 分享内容自动创建日历事件

**Auto-Create Calendar Events from Shared Content**

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-26 / appinn.com · 2026-03-28*

---

## 🎯 痛点 / Pain Point

**中文：** 看到一条带有时间、地点、事件的内容（推文、文章、聊天截图），需要手动打开日历 App 逐项填写，繁琐且容易遗漏。

**English:** When you see content with a time, location, and event (tweet, article, screenshot), you have to manually open the Calendar app and fill in each field — tedious and error-prone.

---

## 💡 做了什么 / What It Does

**中文：** 将带有时间、地点、事件信息的任意内容直接分享给 Minis（或通过 iOS 分享按钮转发），Minis 自动解析其中的日期、时间、地点，调用 `apple-calendar` 创建日历事件，无需打开日历 App。

**English:** Share any content containing time, location, and event info directly to Minis (or forward via iOS Share Sheet). Minis parses the date, time, and location, then calls `apple-calendar` to create the event — no need to open the Calendar app.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in (`apple-calendar`) | 创建日历事件 / Create calendar events |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
（分享一条推文或截图）
帮我把这个加到日历里。
```

**English:**
```
(Share a tweet or screenshot)
Add this to my calendar.
```

---

## 💡 Tips

- 直接用 iOS **分享按钮** 把推文/网页转发给 Minis，比复制粘贴更快
- 支持模糊时间表达，如"下周五下午"、"明天 3 点"

---


## 📸 截图 / Screenshots

![Screenshot](../../assets/screenshots/auto-create-calendar-from-share.jpg)

*📷 分享活动信息 → Minis 自动创建日历事件，右侧日历 App 同步显示 · @caizhenghai via appinn.com · 2026-03-26*

## 👤 贡献者 / Contributor

[@wsvn53](https://x.com/wsvn53) · [appinn.com](https://www.appinn.com/iphone-automation-11-real-use-cases/)

## 📅 Last Verified

2026-03-26
