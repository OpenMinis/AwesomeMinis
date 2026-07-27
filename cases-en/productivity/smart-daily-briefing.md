# Smart Daily Briefing

> Every morning, get a spoken summary of your day: calendar events, weather, top news, and pending reminders — all in one go.

---

## 🎯 Pain Point

Checking your calendar, then weather app, then news, then reminders is a fragmented morning ritual that fragments your attention before the day even starts. A unified briefing lets you stay informed while getting ready.

---

## 💡 What It Does

Minis pulls together:
- **Today's calendar events** (via Apple Calendar)
- **Current weather** (via Apple Weather framework)
- **Top news headlines** (via web search)
- **Pending reminders** (via Apple Reminders)

...and delivers it as a clean, readable summary. Optionally, use the `doubao-tts` skill to have it read aloud.

---

## 🛠 Skills Needed

| Skill | Purpose |
|-------|---------|
| Built-in | Calendar, Reminders, Weather, Location access |
| `doubao-tts` *(optional)* | Text-to-speech for audio playback |

---

## 📋 How to Use

1. Open Minis in the morning
2. Paste the prompt below
3. Optionally ask Minis to read it aloud

---

## 💬 Example Prompt

```text
Give me a morning briefing:
1. My calendar events for today
2. Current weather and today's forecast
3. Top 3 technology news headlines
4. Pending reminders

End with a one-sentence focus for the day.
```

---

## 📤 Expected Output

A structured summary covering all four sections, ending with a prioritized focus sentence. Takes about 15–20 seconds.

If using TTS, an audio file is generated and plays automatically.

---

## ⚙️ Configuration / Requirements

- [x] Calendar permissions granted to Minis
- [x] Reminders permissions granted to Minis
- [x] Location permissions granted for weather
- [ ] For optional TTS, configure `DOUBAO_TTS_API_KEY`; optionally set `DOUBAO_TTS_RESOURCE_ID`
- [ ] Legacy TTS alternative: configure both `DOUBAO_TTS_APPID` and `DOUBAO_TTS_TOKEN`

---

## 💡 Tips & Variations

- **Automate it**: Set a Shortcut to open Minis with this prompt every morning at 7am
- **Add stocks**: "Also include the current price of AAPL and BTC"
- **Weekly version**: Run on Monday mornings with "this week's" instead of "today's"

---

## 👤 Author

Submitted by: [@OpenMinis](https://github.com/OpenMinis)

---

## 📅 Last Verified

2026-03
