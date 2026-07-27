# Interactive Vacation Photo Map with MapKit + Photos

> Turn scattered vacation photos into a single interactive HTML map artifact — with photo pins on real locations, rendered natively via WKWebView.

---

## 🎯 Pain Point

Photos have location metadata, but there's no easy native way to see "here's everywhere I went on this trip" as a single visual map with actual photo previews pinned to each place — you'd normally need a dedicated travel-journal app.

---

## 💡 What It Does

Minis collects photo highlights from a recent trip (using the Photos CLI + EXIF/location metadata), builds an HTML artifact powered by Apple's MapKit JS, and renders it live inside the app's built-in WKWebView. The result is a scrollable, pannable "trip recap" page: places visited, highlight count, distance traveled, with photos pinned directly on the map — and pins that open directly in the native Apple Maps app.

---

## 🛠 Skills Needed

| Skill | Purpose |
|-------|---------|
| None (built-in) | Uses `apple-photos` CLI + built-in shell/HTML rendering + WKWebView artifact display |

You will need your own MapKit JS developer token (stored securely via Minis' Keychain-backed credential storage, not in plaintext).

---

## 📋 How to Use

1. Ask Minis to identify your recent trip photos (or do this right after the Photos+HealthKit vacation-detective case above).
2. Ask it to build an interactive map artifact using MapKit JS with your highlight photos.
3. Provide your MapKit JS developer token when prompted — it's stored via the native Keychain-backed settings page, not written into any file.
4. Minis renders and opens the HTML artifact automatically.

---

## 💬 Example Prompt

```
Could you create an interactive HTML artifact that uses Apple Maps to put some of these
vacation highlight photos (maybe pictures where we're smiling or landmarks) on a map and
make it interactive?
```

---

## 📤 Expected Output

An interactive "Summer, pinned." trip recap page showing:
- Trip date range and location (e.g. "July 7–15, 2026 · Italy")
- Summary stats: places visited, highlights, total km traveled
- A real embedded map with photo thumbnails pinned at each location
- Tapping a pin opens that exact location in Apple Maps with directions

![Interactive MapKit JS vacation recap: "Summer, pinned" with trip stats and photo pins tappable into native Apple Maps](../../assets/screenshots/mapkit-vacation-photo-map.jpg)

---

## ⚙️ Configuration / Requirements

- [ ] Photos permission granted, with location data present on photos
- [ ] A MapKit JS developer token (from your Apple Developer account) — stored securely when Minis asks
- [ ] Works with any model; the reviewer used Kimi K3 for this specific case

---

## 💡 Tips & Variations

- If you don't want to set up a MapKit JS token, ask Minis to fall back to plain Apple Maps deep links per photo instead of an embedded map.
- Great one-shot demo of Minis' "artifact" capability: HTML/JS generated on the fly and rendered natively, not just returned as a code block.

---

## 👤 Author

Sourced from: [Open Minis Is the iOS Agent I Wish Siri AI Could Be](https://www.macstories.net/reviews/open-minis-is-the-ios-agent-i-wish-siri-ai-could-be/) by Federico Viticci, MacStories (2026-07-20).

---

## 📅 Last Verified

2026-07
