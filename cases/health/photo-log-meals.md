# 拍三餐自动记录营养数据

**Photo Every Meal → Auto-Log Nutrition to Apple Health**

> 💬 *From [@infinite_Game_](https://x.com/infinite_Game_) · 2026-03-05 (reply to @wsvn53)*

---

## 🎯 痛点 / Pain Point

**中文：** 想追踪每天的饮食营养，但手动查询每道菜的热量、蛋白质、碳水化合物并逐项输入健康 App 极其繁琐，坚持不下去。

**English:** Tracking daily nutrition means manually looking up calories, protein, and carbs for every dish and entering them one by one — too tedious to keep up.

---

## 💡 做了什么 / What It Does

**中文：** 每餐拍一张照片发给 Minis，它识别菜品种类和份量，估算各项营养成分（热量、蛋白质、脂肪、碳水化合物等），自动调用 `apple-healthkit` 写入 Apple Health，形成完整的饮食追踪记录。一天三餐，拍照即记录。

**English:** Take a photo of each meal and send it to Minis. It identifies the dishes and portions, estimates nutritional content (calories, protein, fat, carbs, etc.), and automatically logs the data to Apple Health via `apple-healthkit`. Three meals a day — just snap and log.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in (Vision) | 识别菜品种类和份量 / Identify dishes and portions |
| Built-in (`apple-healthkit`) | 写入营养数据 / Log nutrition data to Health |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
（附上餐食照片）
帮我记录这顿饭的营养数据到健康 App。
```

**English:**
```
(Attach meal photo)
Log the nutrition data for this meal to Apple Health.
```

---

## ⚙️ 配置要求 / Requirements

- [ ] HealthKit 写入权限已授予 Minis（营养类数据）

---

## 💡 Tips

- 结合每日健康数据分析，可以观察饮食与睡眠、运动恢复的关联
- 也可以直接描述："帮我记录午餐：一碗米饭、红烧肉、炒青菜"，无需拍照
- 与 [拍咖啡记录咖啡因](photo-log-caffeine.md) 组合使用，实现完整的饮食追踪闭环

---

## 👤 贡献者 / Contributor

[@infinite_Game_](https://x.com/infinite_Game_) · via [@wsvn53](https://x.com/wsvn53/status/2027237468148511041) thread

## 📅 Last Verified

2026-03-05
