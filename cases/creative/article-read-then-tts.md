# Read Article Then Auto-Generate Audio Version

> 💬 *From the Open Minis community — shared by **oneasai** on 2026-03-24*

---

## 🎯 Pain Point

After reading a long article, you want to listen to the summary while doing something else — but copying to a TTS tool manually is tedious.

---

## 💡 What It Does

After Minis reads and summarizes an article, it automatically calls the doubao-tts skill to generate an audio version matching the text summary exactly. The audio file is saved and auto-played at the end of the conversation.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| `doubao-tts` | Generate the audio version |

---

## 💬 Example Prompt


```
Read this article and summarize the key points. When done, automatically generate an audio version using doubao-tts and play it.
```

---


## 📸 Screenshots

![Screenshot by oneasai](../../assets/screenshots/article-read-then-tts.jpg)

*📷 Shared by **oneasai** · 2026-03-24* — The audio version is automatically generated and played after the article is summarized

## ⚙️ Requirements

- [ ] `doubao-tts` skill installed
- [ ] `DOUBAO_TTS_API_KEY` configured; optionally set `DOUBAO_TTS_RESOURCE_ID` (defaults to `seed-tts-2.0`)
- [ ] Legacy alternative: configure both `DOUBAO_TTS_APPID` and `DOUBAO_TTS_TOKEN`

---

## 🏷 Tags

`tts` `audio` `reading` `automation` `doubao`

---

## 👤 Contributor

From the Open Minis Telegram community

Original sharer: **oneasai**

---

## 📅 Last Verified

2026-03-24
