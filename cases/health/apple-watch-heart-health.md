# Apple Watch Heart Health Analysis

> Analyze recent Apple Watch health data and generate a risk-oriented report with trends and caveats.

---

## 🎯 Pain Point

Apple Watch health data such as HRV, resting heart rate, blood oxygen, and respiratory rate is difficult to interpret without context. Individual readings rarely explain whether a change is meaningful.

---

## 💡 What It Does

Minis reads recent HealthKit data and organizes it into a three-level review:

- 🔴 **Potentially urgent signals:** irregular rhythm notifications, ECG anomalies, or extreme exercise heart rates
- 🟡 **Early warnings:** sharp HRV decline, rising resting heart rate, or repeated low nighttime oxygen readings
- 🟢 **Long-term trends:** sustained changes in HRV, resting heart rate, or respiratory rate

The output can include trend charts, flagged dates, and plain-language recommendations. This is an informational analysis, not a diagnosis. Concerning symptoms or alerts require a qualified clinician.

---

## 🛠 Skills and Capabilities

| Skill or capability | Purpose | Availability |
|---------------------|---------|--------------|
| Built-in `apple-healthkit` | Read heart rate, HRV, oxygen saturation, respiratory rate, ECG, and related HealthKit data | Built into Minis |
| Built-in shell + Python | Aggregate data and generate charts | Built into Minis |
| `cardiac-health-monitor` | Contributor's reusable cardiac analysis workflow | Not currently in the public MinisSkills repository |

The public repository contains `health-sleep-analysis`, but it focuses on sleep and is not an equivalent replacement for `cardiac-health-monitor`.

---

## 📋 How to Use

1. Make sure Apple Watch data has synchronized to Apple Health.
2. Grant Minis read access to the requested HealthKit types.
3. Ask Minis to fetch the data in one `apple-healthkit batch` request and analyze it.

---

## 💬 Example Prompt

```text
Read my last 30 days of Apple Watch data in one HealthKit batch request.
Include heart rate, resting heart rate, HRV, oxygen saturation, respiratory rate,
and any available irregular-rhythm or ECG events. Generate trend charts and a
risk-oriented summary. Clearly distinguish observed data from inference and include
a medical disclaimer.
```

---

## 📤 Expected Output

- A clearly explained risk level
- HRV, resting-heart-rate, and oxygen-saturation trend charts
- Dates and events flagged as anomalies
- Plain-language recommendations and uncertainty
- A reminder that the analysis is not medical diagnosis

---

## ⚙️ Requirements

- [x] Apple Watch paired and synchronized
- [x] HealthKit permissions granted for every requested data type
- [ ] No public `cardiac-health-monitor` installation is required; use built-in `apple-healthkit` and analysis tools
- [ ] Optional: obtain the contributor's custom `cardiac-health-monitor` skill from its original source, if available

---

## 👤 Author

Submitted by [@OpenMinis](https://github.com/OpenMinis)

---

## 📅 Case Last Verified

2026-03

## 🔄 Skill Catalog Check

Checked against `OpenMinis/MinisSkills` commit `3993f5ab0a0ff204d774da7a5cf27ea281e7b021` on 2026-07-27.
