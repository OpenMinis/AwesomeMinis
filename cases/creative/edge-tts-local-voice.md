# Local Lightweight TTS on Old iPhone (edge-tts)

> 💬 *From the Open Minis community — shared by **Xiaoyu Huang** on 2026-03-23*

---

## 🎯 Pain Point

Want to generate speech locally on-device without an API key or when the network is restricted.

---

## 💡 What It Does

On a 64GB iPhone 8 Plus, Minis installs the `edge-tts` Python package and generates speech without requiring the user to supply an API key. The package runs from the local shell, but speech synthesis uses Microsoft's online Edge TTS service and therefore generally requires network access. This is lightweight execution, not fully offline or on-device synthesis.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in shell | Install and run the Python package |
| `edge-tts` *(external Python package)* | Generate speech through Microsoft Edge's online TTS service |

---

## 💬 Example Prompt


```
Install edge-tts for me, then use it to convert the following text to an audio file: [text]
```

---


## 📸 Screenshots

![Screenshot by Xiaoyu Huang](../../assets/screenshots/edge-tts-local-voice-2.jpg)
*📷 Shared by **Xiaoyu Huang** · 2026-03-23* — It’s so difficult for me. Test this voice function in the 64G iPhone 8plus environment. iOS version is limited. Storage capacity is limited. Surprisingly, you can also deploy a lightweight voice TTS locally and test the effect.

## ⚙️ Requirements

- [ ] No API key required
- [ ] Network access to the Microsoft Edge TTS service
- [ ] Install the external package with `pip install edge-tts`; it is not a MinisSkills repository skill

---

## 🏷 Tags

`tts` `edge-tts` `local` `offline` `voice`

---

## 👤 Contributor

From the Open Minis Telegram community

Original sharer: **Xiaoyu Huang**

---

## 📅 Last Verified

2026-03-23
