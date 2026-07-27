# Photos + HealthKit Cross-Reference: "How Much Did I Walk That Night?"

> Find a specific vacation photo by description, then automatically cross-reference HealthKit steps for that exact date and time window — no manual date lookup required.

---

## 🎯 Pain Point

You remember a moment ("that night I saw the big ship") but not the exact date. Correlating a photo memory with health data (steps/distance) normally means manually scrolling through Photos, noting the date, then opening the Health app to check that day's activity — three separate apps, real friction.

---

## 💡 What It Does

Minis chains three native Apple frameworks in a single reasoning pass:
1. Checks its own memory system first (already knew the user was recently on vacation from an earlier conversation) to narrow the date range
2. Uses the Photos CLI to build a contact sheet of candidate photos from that period, visually picks the one matching "large ship," and extracts its exact timestamp
3. Calls HealthKit for that specific date/time window and returns steps + distance

All of this runs as deterministic on-device tool calls (not model guessing), so the answer is fast and accurate — down to the exact photo location, time, and step count.

---

## 🛠 Skills Needed

None (built-in). Uses Minis' native `apple-photos` and `apple-healthkit` CLIs plus the built-in memory system — no additional skill install needed.

---

## 📋 How to Use

1. Have a prior conversation where you mentioned a recent trip (optional — helps Minis short-circuit the date search via memory).
2. Ask Minis to find a specific photo by description and correlate it with health data.
3. Review the identified photo + the HealthKit numbers Minis returns.

---

## 💬 Example Prompt

```
Find the photo of when I was on vacation recently and took a picture of a large ship. How much did I walk that night?
```

---

## 📤 Expected Output

Something like:

> This was taken in Gaeta on July 7 at 8:57 PM.
> Between 6 PM and midnight, you walked 6,067 steps — 4.47 km.
> For the entire day: 10,257 steps — 7.62 km.

Plus the actual photo shown inline for confirmation. Total round trip: under a minute, ~30 tool calls under the hood (photo export, HealthKit batch query, memory recall).

![Minis finds the exact vacation photo of a large ship, then correlates it with HealthKit step and distance data for that night](../../assets/screenshots/photos-healthkit-vacation-detective.jpg)

---

## ⚙️ Configuration / Requirements

- [ ] Photos permission granted
- [ ] HealthKit access granted (Apple Watch or iPhone motion data present)
- [ ] Works better if you've discussed the trip with Minis before, so it can use memory to narrow the date range instead of scanning your whole library

---

## 💡 Tips & Variations

- Ask a broader version first: *"Based on my photos, would you say I was recently on vacation?"* — Minis will scan recent photo metadata/EXIF and camera activity patterns to infer travel, distinguishing an actual vacation from, e.g., a concert trip.
- Combine with the MapKit case (see `mapkit-vacation-photo-map.md`) for a full "photo detective" workflow.

---

## 👤 Author

Sourced from: [Open Minis Is the iOS Agent I Wish Siri AI Could Be](https://www.macstories.net/reviews/open-minis-is-the-ios-agent-i-wish-siri-ai-could-be/) by Federico Viticci, MacStories (2026-07-20).

---

## 📅 Last Verified

2026-07
