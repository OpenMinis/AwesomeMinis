# Photo Every Meal → Auto-Log Nutrition to Apple Health

> 💬 *From [@infinite_Game_](https://x.com/infinite_Game_) · 2026-03-05 (reply to @wsvn53)*

---

## 🎯 Pain Point

Tracking daily nutrition means manually looking up calories, protein, and carbs for every dish and entering them one by one — too tedious to keep up.

---

## 💡 What It Does

Take a photo of each meal and send it to Minis. It identifies the dishes and portions, estimates nutritional content (calories, protein, fat, carbs, etc.), and automatically logs the data to Apple Health via `apple-healthkit`. Three meals a day — just snap and log.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in (Vision) | Identify dishes and portions |
| Built-in (`apple-healthkit`) | Log nutrition data to Health |

---

## 💬 Example Prompt


```
(Attach meal photo)
Log the nutrition data for this meal to Apple Health.
```

---

## ⚙️ Requirements

- [ ] HealthKit write permission has been granted to Minis (nutritional data)

---

## 💡 Tips

- Combined with daily health data analysis, you can observe the relationship between diet, sleep, and exercise recovery
- You can also directly describe: "Record lunch for me: a bowl of rice, braised pork, stir-fried vegetables" without taking a photo
- Use in combination with [Photo-log-caffeine.md] to achieve a complete closed-loop diet tracking

---

## 👤 Contributor

[@infinite_Game_](https://x.com/infinite_Game_) · via [@wsvn53](https://x.com/wsvn53/status/2027237468148511041) thread

## 📅 Last Verified

2026-03-05
