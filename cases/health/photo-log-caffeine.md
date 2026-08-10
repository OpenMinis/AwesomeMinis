# Photo a Coffee → Auto-Log Caffeine Intake to HealthKit

> 💬 *From [@wsvn53](https://x.com/wsvn53) / appinn.com · 2026-03-28*

---

## 🎯 Pain Point

You want to track your daily caffeine intake, but manually logging it in the Health app is too much friction — so you never actually do it.

---

## 💡 What It Does

Take a photo of your coffee (or coffee capsules) and send it to Minis. It identifies the coffee type and quantity, estimates caffeine content, and calls `apple-healthkit` to log the data automatically — a complete caffeine tracking loop.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in Vision | Identify coffee type and quantity |
| Built-in (`apple-healthkit`) | Log caffeine data to HealthKit |

---

## 💬 Example Prompt


```
(Attach coffee photo)
Log the caffeine intake for this coffee.
```

---


## 📸 Screenshots

![Screenshot](../../assets/screenshots/photo-log-caffeine.jpg)

*📷 Photograph coffee capsules → Minis identify and record caffeine → Apple Health shows weekly trends · @wsvn53 via appinn.com · 2026-03-06*

## ⚙️ Requirements

- [ ] HealthKit write permission granted to Minis

---

## 💡 Tips

- Combined with health data analysis, you can observe the relationship between caffeine intake and sleep quality
- You can also directly say "Record two Nespresso capsules for me" without taking a photo.

---

## 👤 Contributor

[@wsvn53](https://x.com/wsvn53) · [appinn.com](https://www.appinn.com/iphone-automation-11-real-use-cases/)

## 📅 Last Verified

2026-03-28
