# Auto-Create Calendar Events from Shared Content

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-26 / appinn.com · 2026-03-28*

---

## 🎯 Pain Point

When you see content with a time, location, and event (tweet, article, screenshot), you have to manually open the Calendar app and fill in each field — tedious and error-prone.

---

## 💡 What It Does

Share any content containing time, location, and event info directly to Minis (or forward via iOS Share Sheet). Minis parses the date, time, and location, then calls `apple-calendar` to create the event — no need to open the Calendar app.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in `apple-calendar` | Create calendar events |

---

## 💬 Example Prompt


```
(Share a tweet or screenshot)
Add this to my calendar.
```

---

## 💡 Tips

- Directly use iOS **Share Button** to forward tweets/webpages to Minis, faster than copying and pasting
- Support fuzzy time expressions, such as "next Friday afternoon", "tomorrow 3 o'clock"

---


## 📸 Screenshots

![Screenshot](../../assets/screenshots/auto-create-calendar-from-share.jpg)

*📷 Share event information → Minis automatically creates calendar events, and the calendar app on the right displays them simultaneously · @caizhenghai via appinn.com · 2026-03-26*

## 👤 Contributor

[@wsvn53](https://x.com/wsvn53) · [appinn.com](https://www.appinn.com/iphone-automation-11-real-use-cases/)

## 📅 Last Verified

2026-03-26
