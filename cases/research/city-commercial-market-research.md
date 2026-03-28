# 一句话生成城市商业市场研究报告

**One Sentence → Professional City Commercial Market Research Report**

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-02-27 (reply thread)*

---

## 🎯 痛点 / Pain Point

**中文：** 做城市商业研究通常需要：购买仲量联行、戴德梁行、赢商网等机构的专业报告，手动整理多份数据，再用 Excel/Python 绘图——费时费钱，门槛高。

**English:** City commercial research typically requires purchasing reports from JLL, Cushman & Wakefield, Winshang, etc., manually consolidating multiple data sources, then charting in Excel or Python — expensive, time-consuming, and high-barrier.

---

## 💡 做了什么 / What It Does

**中文：** 对 Minis 说一句话，它自动联网检索仲量联行、戴维斯、赢商网等权威数据源，编写分析脚本，生成多维可视化图表，输出包含趋势曲线、商圈对比、业态分化、空置率分布的完整市场报告。

示例：分析成都过去几年门店空置率
- 核心结论：2022 Q4 空置率峰值触顶
- 春熙路/太古里核心商圈长期维持 4–7.5%
- ⚠️ 分化加剧——核心商圈与边缘商圈差距拉大

**English:** Say one sentence to Minis, and it automatically searches authoritative sources (JLL, DTZ, Winshang, etc.), writes analysis scripts, generates multi-dimensional charts, and outputs a complete market report with trend curves, district comparisons, category breakdowns, and vacancy rate distributions.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in (`browser_use`) | 联网检索行业数据源 / Search industry data sources |
| Built-in (shell + Python) | 编写分析脚本、生成图表 / Write scripts, generate charts |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
分析一下成都过去几年门店空置率，
联网检索仲量联行、戴维斯、赢商网等数据，
生成趋势图表和商圈对比报告。
```

**English:**
```
Analyze the retail vacancy rate in Chengdu over the past few years.
Search JLL, DTZ, Winshang and other sources online.
Generate trend charts and a district comparison report.
```

---

## ⚙️ 配置要求 / Requirements

- [ ] 无需额外配置，Minis 内置浏览器检索和 Python 绘图能力

---

## 💡 Tips

- 可替换城市和指标，如"北京写字楼出租率"、"上海零售物业租金走势"
- 生成的图表可直接导出为 PNG 分享或嵌入报告
- 适合房产投资分析、商业选址研究、行业调研等场景

---

## 👤 贡献者 / Contributor

[@wsvn53](https://x.com/wsvn53) · [原始推文](https://x.com/wsvn53/status/2027237468148511041)

## 📅 Last Verified

2026-02-27
