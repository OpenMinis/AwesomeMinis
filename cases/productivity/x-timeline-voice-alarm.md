# X Timeline Voice Briefing — Replaces Your Morning Alarm

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-12*

---

## 🎯 Pain Point

Every morning, you spend time scrolling X/Twitter to catch up on what happened overnight — and a regular alarm still leaves you groggy.

---

## 💡 What It Does

An iOS Shortcuts automation triggers Minis every morning. Minis uses `twitter-x-hub` to fetch your X Timeline from the past 12 hours, summarizes it into a morning briefing script, generates speech with TTS, and plays it automatically — waking you up with a spoken news briefing instead of a normal alarm.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| `twitter-x-hub` | Fetch X Timeline |
| `doubao-tts` | Generate voice briefing audio |
| iOS Shortcuts | Trigger the workflow on a schedule |

---

## 💬 Example Prompt

```text
Fetch my X Timeline from the past 12 hours, summarize it into a morning briefing,
generate audio with doubao-tts, and play it.
```

---

## 📸 Screenshots

![Screenshot](../../assets/screenshots/x-timeline-voice-alarm.jpg)

*📷 Full X Timeline morning briefing flow: ① set automation ② fetch X data ③ AI generates briefing ④ TTS output · @wsvn53 via appinn.com · 2026-03-12*

---

## ⚙️ Requirements

- [ ] `twitter-x-hub` skill installed
- [ ] Sign in to X in the Minis browser, use `browser_use get_cookies`, and load `auth_token` / `ct0` as `TWITTER_AUTH_TOKEN` / `TWITTER_CT0`
- [ ] `doubao-tts` skill installed with `DOUBAO_TTS_API_KEY`; legacy AppID + Token authentication is also supported
- [ ] iOS Shortcuts morning schedule automation configured

---

## 👤 Contributor

[@wsvn53](https://x.com/wsvn53)

---

## 📅 Last Verified

2026-03-12
