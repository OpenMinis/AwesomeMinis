# 个人色彩分析——上传自拍，生成专业诊断报告

**AI Personal Color Analysis — Upload a Selfie, Get a Professional Diagnosis Report**

> 💬 *From **采菇凉滴小蘑菇** · 2026-05-02 (via Open Minis Telegram)*

---

## 🎯 痛点 / Pain Point

**中文：** 想知道自己适合什么颜色、穿什么风格，但专业色彩诊断价格高昂，线下预约也麻烦。

**English:** Want to know what colors and styles suit you best, but professional personal color consultations are expensive and hard to book.

---

## 💡 做了什么 / What It Does

**中文：** 制作了一个完整的个人色彩分析 Skill。上传一张自拍，Minis 从冷暖调、明度、彩度、对比度 4 个维度分析，自动判定 12 季型，生成两张专业图片：

- **色彩诊断卡**：色彩坐标 + 7 档推荐色系（最佳色 / 中性色 / 强调色 / 避雷色等）
- **个人形象诊断总报告**：6 套场景穿搭（通勤 / 休闲 / 社交 / 商务 / 周末 / 度假）、妆容配色（眉型 / 眼影 / 腮红 / 唇色）、发型 + 发色推荐、饰品 / 眼镜 / 美瞳建议

男女通用。

**English:** A complete Personal Color Analysis Skill. Upload a selfie — Minis analyzes it across 4 dimensions (warm/cool tone, lightness, chroma, contrast), determines 1 of 12 seasonal types, and generates two professional images:

- **Color Diagnosis Card**: color coordinates + 7-tier palette (best colors, neutrals, accents, colors to avoid, etc.)
- **Personal Image Report**: 6 outfit scenes (commute / casual / social / business / weekend / vacation), makeup palette (brows / eyeshadow / blush / lips), hairstyle + hair color recommendations, accessories / glasses / contact lens suggestions

Works for all genders.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| `personal-color-analysis` | 色彩季型判定 + 诊断图生成 / Color season analysis + report generation |
| `codex-image` | AI 生成诊断图片 / AI image generation for diagnosis cards |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
（附上自拍）
帮我做个人色彩分析
```

**English:**
```
(Attach a selfie)
Personal color analysis please
```

---

## 📸 截图 / Screenshots

![对话截图 / Chat screenshot](../../assets/screenshots/personal-color-analysis-1.jpg)

![色彩诊断卡 / Color Diagnosis Card](../../assets/screenshots/personal-color-analysis-2.jpg)

![个人形象诊断总报告（上）/ Personal Image Report (part 1)](../../assets/screenshots/personal-color-analysis-3.jpg)

![个人形象诊断总报告（下）/ Personal Image Report (part 2)](../../assets/screenshots/personal-color-analysis-4.jpg)

---

## ⚙️ 配置要求 / Requirements

- [ ] 需安装 `personal-color-analysis` Skill
- [ ] 需配置 `codex-image` Skill（用于生成诊断图片）
- [ ] 自拍建议：正脸、自然光、淡妆或素颜、无眼镜

---

## 💡 Tips

**中文：**
- 12 季型覆盖：浅春 / 亮春 / 柔春 / 浅夏 / 柔夏 / 冷夏 / 柔秋 / 暖秋 / 深秋 / 亮冬 / 冷冬 / 深冬
- 可要求 Minis 重点生成某一部分（如「只要穿搭建议」）

**English:**
- 12 season types: Spring (Light/Bright/Soft) · Summer (Light/Soft/Cool) · Autumn (Soft/Warm/Deep) · Winter (Bright/Cool/Deep)
- You can ask Minis to focus on one part only (e.g. "just the outfit recommendations")

---

## 👤 贡献者 / Contributor

来自 Open Minis Telegram 社区 / From the Open Minis Telegram community

原始分享者 / Original sharer: **采菇凉滴小蘑菇**

---

## 📅 Last Verified

2026-05-02
