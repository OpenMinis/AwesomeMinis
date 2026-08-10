# Daily Briefing Auto-Push to WeChat

> 💬 *From the Open Minis community — shared by **meng nimen** on 2026-03-25*

---

## 🎯 Pain Point

Checking weather, news, and calendar separately every morning is fragmented and time-consuming.

---

## 💡 What It Does

Uses Minis on iPad with a scheduled task to fetch weather and news, then pushes the daily briefing to WeChat via the openilink-hub middleware — no manual checking needed.

---

## 🛠 Skills Used

| Platform capability | Purpose |
|---------------------|---------|
| Built-in `apple-weather` | Fetch the local weather and forecast |
| iOS Shortcuts automation *(Apple platform capability, not a MinisSkills skill)* | Trigger the workflow on a schedule |
| `openilink-hub` *(external middleware, not a MinisSkills skill)* | Push the briefing to WeChat |

---

## 💬 Example Prompt


```
Fetch today's weather forecast and top tech news, format as a daily briefing, then push it to my WeChat via openilink-hub.
```

---


## 📸 Screenshots

![Screenshot by meng nimen](../../assets/screenshots/daily-briefing-wechat-push.jpg)

*📷 Shared by **meng nimen** · 2026-03-25* — Send to WeChat ClawBot skill configuration

## ⚙️ Requirements

- [ ] Deploy and review the external `openilink-hub` middleware; it is not part of `OpenMinis/MinisSkills`
- [ ] Store its WeChat push token in a Minis environment variable
- [ ] Configure an iOS Shortcuts time-of-day automation; background shell loops are not reliable when iOS suspends the app
- [ ] Grant location permission for weather

---

## 🏷 Tags

`automation` `wechat` `daily-briefing` `push-notification`

---

## 👤 Contributor

From the Open Minis Telegram community

Original sharer: **meng nimen**

---

## 📅 Last Verified

2026-03-25
