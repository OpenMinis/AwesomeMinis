# One-Click HTML Presentation Generator

> Turn a script, outline, or rough notes into a polished, Jobs-style minimalist HTML presentation.

---

## 🎯 Pain Point

Creating a presentation takes hours of template selection, slide formatting, and layout adjustments. Even with AI tools, you often still need to move elements manually in Keynote or PowerPoint.

---

## 💡 What It Does

Minis can turn a script or outline into one self-contained HTML file styled as a dark, minimalist technology presentation. Each slide is a full-screen section with large typography, one main idea, and smooth transitions.

The result opens in any browser, works offline, can be shared as a file, and can be captured for social media.

---

## 🛠 Skills and Capabilities

| Skill or capability | Purpose | Availability |
|---------------------|---------|--------------|
| Built-in HTML/CSS generation and file tools | Create the self-contained presentation | Built into Minis |
| `ppt-generator` | Contributor's reusable presentation workflow | Not currently in the public MinisSkills repository |

The public `OpenMinis/MinisSkills` repository does not currently contain `ppt-generator`. This case still works without it by asking Minis to generate the HTML directly. Do not describe the missing custom skill as publicly installable unless its source is provided.

---

## 📋 How to Use

1. Prepare a script, outline, bullet list, or rough notes.
2. Ask Minis to create a self-contained HTML presentation.
3. Tap the generated HTML file to preview it in Minis.

---

## 💬 Example Prompt

```text
Turn the following outline into a Jobs-style minimalist presentation.
Create one self-contained HTML file with a dark background, large white type,
one main idea per slide, smooth transitions, and a mobile-friendly vertical layout.
Do not use external dependencies.

[paste your content here]
```

---

## 📤 Expected Output

A single `.html` file with:

- Dark background and large white typography
- One key message per slide
- Smooth CSS transitions
- Mobile-friendly vertical layout
- No external dependencies

---

## ⚙️ Requirements

- [ ] No public repository skill is required; Minis can generate the HTML with built-in file and web capabilities
- [ ] Optional: obtain the contributor's custom `ppt-generator` skill from its original source, if available
- [ ] No API keys or special permissions required

---

## 💡 Tips

- For demos, request a slide with a QR code linking to the demo.
- For social media, ask Minis to capture each slide separately.
- Specify the output language in the prompt.

---

## 👤 Author

Submitted by [@OpenMinis](https://github.com/OpenMinis)

---

## 📅 Case Last Verified

2026-03

## 🔄 Skill Catalog Check

Checked against `OpenMinis/MinisSkills` commit `3993f5ab0a0ff204d774da7a5cf27ea281e7b021` on 2026-07-27.
