# 探索 HealthKit 综合健康数据

**Explore Comprehensive HealthKit Data**

> 💬 *From the Open Minis community — shared by **Alan Chen / Virile Chen** on 2026-03-27*

---

## 🎯 痛点 / Pain Point

**中文：** HealthKit 数据分散在健康 App 各处，没有统一的综合分析视图。

**English:** HealthKit data is scattered across the Health app with no unified comprehensive analysis view.

---

## 💡 做了什么 / What It Does

**中文：** 直接让 Minis 获取综合健康数据指标，它会自主探索 apple-healthkit 的各项能力，逐步请求权限，汇总心率、步数、睡眠、血氧等数据并给出分析。

**English:** Simply ask Minis to fetch your comprehensive health metrics. It autonomously explores apple-healthkit capabilities, requests permissions incrementally, and aggregates heart rate, steps, sleep, SpO₂, and more into an analysis.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| `built-in (apple-healthkit)` | — |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
帮我获取我的综合健康数据，包括心率、步数、睡眠、血氧，分析近一周的趋势并给出建议。
```

**English:**
```
Fetch my comprehensive health metrics including heart rate, steps, sleep, and blood oxygen. Analyze last week's trends and give me recommendations.
```

---

## ⚙️ 配置要求 / Requirements

- [ ] Apple Watch 已配对
- [ ] HealthKit 权限授予 Minis（首次运行时会自动请求）

---

## 🏷 标签 / Tags

`healthkit` `apple-watch` `health` `analysis`

---

## 👤 贡献者 / Contributor

来自 Open Minis Telegram 社区 / From the Open Minis Telegram community

原始分享者 / Original sharer: **Alan Chen / Virile Chen**

---

## 📅 验证时间 / Last Verified

2026-03-27
