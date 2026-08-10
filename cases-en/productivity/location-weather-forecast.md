# Location-Aware Detailed Weather Forecast

> Ask for the weather where you actually are — Minis grabs your live location via native Location Services and pulls a detailed native Apple Weather forecast, hour by hour, with a practical human-readable takeaway.

---

## 🎯 Pain Point

Getting a genuinely detailed forecast (hourly breakdown, UV index, "feels like" temperature, practical advice on when to avoid going outside) usually means opening a separate weather app and reading through several screens — not something you'd get from a quick assistant query.

---

## 💡 What It Does

Minis reads your current device location (with permission), calls the native Apple Weather CLI, and returns a structured report: current conditions, today's high/low, wind, UV index, sunset time, visibility, an hour-by-hour table for the rest of the day, and a plain-language "practical take" (e.g. when to avoid strenuous outdoor activity).

---

## 🛠 Skills Needed

None (built-in). Uses Minis' native `apple-weather` CLI plus native Location Services — no third-party weather skill required.

---

## 📋 How to Use

1. Ask Minis for a detailed weather forecast.
2. Grant the native Location permission prompt the first time.
3. Review the structured report, including the hourly table and practical summary.

---

## 💬 Example Prompt

```
Access my location and give me a detailed weather forecast for today.
```

---

## 📤 Expected Output

A structured report like:

> **Hot, sunny, and dry. A yellow high-temperature warning is active.**
> - Now: 35.8°C, feels like 37.4°C
> - Today's high: 36.2°C · Overnight low: 24.9°C
> - Conditions: Clear to mostly clear · Rain: 0%
> - UV index: 9 — very high · Sunset: 8:40 PM
>
> **Rest of the day** (hourly table: time / temperature / feels like)
>
> **Practical take:** avoid strenuous outdoor activity until after 6 PM. UV and heat are both severe in the early afternoon — use shade, sunscreen, and plenty of water.

![Location-aware detailed weather forecast: current conditions, hourly breakdown table, and a practical human-readable takeaway](../../assets/screenshots/location-weather-forecast.jpg)

---

## ⚙️ Configuration / Requirements

- [ ] Location Services permission granted to Minis

---

## 💡 Tips & Variations

- Ask it to compare against tomorrow's forecast, or to flag specific hours best suited for outdoor plans.
- Combine with a Calendar-reading prompt to also check locations of upcoming events, so Minis can forecast for a destination rather than just your current spot.

---

## 👤 Author

Sourced from: [Open Minis Is the iOS Agent I Wish Siri AI Could Be](https://www.macstories.net/reviews/open-minis-is-the-ios-agent-i-wish-siri-ai-could-be/) by Federico Viticci, MacStories (2026-07-20).

---

## 📅 Last Verified

2026-07
