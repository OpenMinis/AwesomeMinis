# End-to-End Automated Video Production

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-18 / appinn.com · 2026-03-28*

---

## 🎯 Pain Point

Producing a tech video requires: topic research, scripting, voice recording, finding images, editing, adding subtitles — each step is time-consuming and requires specialized tools.

---

## 💡 What It Does

Minis handles an entire tech video production: analyze Bilibili creator history and view data → plan topic and write voiceover script → generate audio with Doubao TTS → search for images → render subtitles and composite video with ffmpeg. 200+ tool calls, resulting in a complete video uploaded to Bilibili.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| `bilibili-hub` | Analyze creator videos and performance data |
| `doubao-tts` | Generate voiceover audio |
| Built-in ffmpeg | Render subtitles and composite the video |
| `exa-search` | Find relevant image material |

---

## 💬 Example Prompt

```text
Help me produce a technology video:
1. Analyze top-performing technology videos on Bilibili and identify common traits
2. Plan a topic and write a voiceover script
3. Generate the voiceover with Doubao TTS
4. Find relevant images
5. Render subtitles and composite the final video with ffmpeg
```

---

## ⚙️ Requirements

- [ ] `bilibili-hub` skill installed
- [ ] Sign in to Bilibili in the Minis browser, then use `browser_use get_cookies`; authenticated access uses `BILI_SESSDATA`, `BILI_JCT`, `BILI_USERID`, and `BILI_BUVID3`
- [ ] `doubao-tts` skill installed with `DOUBAO_TTS_API_KEY`; legacy `DOUBAO_TTS_APPID` + `DOUBAO_TTS_TOKEN` is also supported
- [ ] ffmpeg installed (`apk add ffmpeg`; Minis can install it automatically)
- [ ] `exa-search` available; `EXA_API_KEY` is optional for basic use and recommended for higher limits

---

## 💡 Tips

- Use voice input when your hands are occupied, but do not interact with the workflow while driving unless it is safe and legal.
- Preview the finished video in Minis before uploading it.

---

## 👤 Contributor

[@wsvn53](https://x.com/wsvn53) · [bilibili.com/video/BV1WpwizcEcq](https://www.bilibili.com/video/BV1WpwizcEcq)

## 📅 Last Verified

2026-03-18
