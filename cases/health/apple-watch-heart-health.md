# Apple Watch Heart Health Monitor

> Analyze your Apple Watch health data to detect early warning signs of cardiac issues and generate a personalized risk report with charts.

---

## 🎯 Pain Point

Most Apple Watch users only glance at their heart rate occasionally. The real value — HRV trends, resting heart rate changes, blood oxygen dips during sleep — is buried in the Health app with no interpretation. Without context, numbers like "HRV: 42ms" mean nothing.

---

## 💡 What It Does

Minis reads 30 days of HealthKit data (heart rate, HRV, blood oxygen, respiratory rate) and runs a three-tier risk analysis:

- 🔴 **Urgent signals** — irregular rhythm, ECG anomalies, extreme heart rate during exercise
- 🟡 **Early warnings** — HRV dropping >30% over 3 days, resting HR rising >10 bpm, nighttime SpO₂ < 95%
- 🟢 **Long-term trends** — 3-month HRV decline, consistently elevated respiratory rate

It generates a visual report with trend charts and actionable recommendations.

---

## 🛠 Skills Needed

| Skill | Purpose |
|-------|---------|
| `cardiac-health-monitor` | Reads HealthKit data, runs risk analysis, generates charts |

---

## 📋 How to Use

1. Make sure your Apple Watch is synced and HealthKit data is up to date
2. Open Minis and start a new conversation
3. Paste the prompt below

---

## 💬 Example Prompt

```
帮我做一次心脏健康分析，读取我最近30天的 Apple Watch 数据，
包括心率、HRV、血氧和呼吸频率，生成风险评估报告和趋势图表。
```

Or in English:
```
Run a cardiac health analysis using my last 30 days of Apple Watch data.
Include heart rate, HRV, blood oxygen, and respiratory rate.
Generate a risk assessment report with trend charts.
```

---

## 📤 Expected Output

- A risk level badge (🔴 / 🟡 / 🟢)
- Trend charts for HRV, resting heart rate, and blood oxygen
- Specific dates/events flagged as anomalies
- Plain-language recommendations (e.g., "Your HRV dropped 35% over the last 3 days — consider rest and stress reduction")

Takes approximately 30–60 seconds to generate.

---

## ⚙️ Configuration / Requirements

- [x] Apple Watch paired and synced
- [x] HealthKit permissions granted to Minis (Heart Rate, HRV, Blood Oxygen, Respiratory Rate)
- [x] `cardiac-health-monitor` skill installed

---

## 💡 Tips & Variations

- **Weekly check-in**: Run this every Monday morning as a health check-in ritual
- **After illness**: Run after recovering from a cold or flu to see how your HRV recovers
- **Variation**: Ask for a comparison between this month and last month

---

## 👤 Author

Submitted by: [@OpenMinis](https://github.com/OpenMinis)

---

## 📅 Last Verified

2026-03
