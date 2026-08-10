# AI Personal Color Analysis — Upload a Selfie, Get a Professional Report

> 💬 *From the Open Minis Telegram community · 2026-05-02*

---

## 🎯 Pain Point

You want to know which colors and styles suit you, but professional personal-color consultations are expensive and inconvenient to book.

---

## 💡 What It Does

Upload a selfie and ask Minis to assess four dimensions: warm/cool undertone, lightness, chroma, and contrast. The workflow classifies one of twelve seasonal types and generates two visual reports:

- **Color Diagnosis Card:** color coordinates plus best colors, neutrals, accents, and colors to avoid
- **Personal Image Report:** outfit recommendations for commute, casual, social, business, weekend, and vacation settings; makeup palette; hairstyle and hair color; accessories, glasses, and contact-lens suggestions

The workflow works for all genders.

---

## 🛠 Skills Used

| Skill | Purpose | Availability |
|-------|---------|--------------|
| `personal-color-analysis` | Analyze the selfie and produce seasonal-color recommendations | Contributor-provided custom skill; not currently in the public MinisSkills repository |
| `codex-image` | Generate the diagnosis cards and visual report | Available in the public MinisSkills repository |

---

## 💬 Example Prompt

```text
(Attach a front-facing selfie taken in natural light.)
Analyze my personal color season and generate a color diagnosis card and style report.
```

---

## 📸 Screenshots

![Chat screenshot](../../assets/screenshots/personal-color-analysis-1.jpg)

![Color Diagnosis Card](../../assets/screenshots/personal-color-analysis-2.jpg)

![Personal Image Report, part 1](../../assets/screenshots/personal-color-analysis-3.jpg)

![Personal Image Report, part 2](../../assets/screenshots/personal-color-analysis-4.jpg)

---

## ⚙️ Requirements

- [ ] Obtain or create the custom `personal-color-analysis` skill; it is not currently published in `OpenMinis/MinisSkills`
- [ ] Install the public `codex-image` skill
- [ ] Sign in to a ChatGPT account in the Minis browser; `codex-image` normally obtains and securely caches authentication automatically, so manual token setup is not required
- [ ] Use a front-facing selfie in natural light, with light or no makeup and no glasses

---

## 💡 Tips

- Twelve-season coverage: Spring (Light/Bright/Soft), Summer (Light/Soft/Cool), Autumn (Soft/Warm/Deep), and Winter (Bright/Cool/Deep).
- Ask Minis to produce only one section, such as outfit recommendations, when you do not need the full report.

---

## 👤 Contributor

From the Open Minis Telegram community

Original sharer: **采菇凉滴小蘑菇**

---

## 📅 Case Last Verified

2026-05-02

## 🔄 Skill Catalog Check

Checked against `OpenMinis/MinisSkills` commit `3993f5ab0a0ff204d774da7a5cf27ea281e7b021` on 2026-07-27.
