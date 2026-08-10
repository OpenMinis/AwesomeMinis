# Spotify Voice Control: Search, Switch, Play

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-22 / appinn.com · 2026-03-28*

---

## 🎯 Pain Point

When driving or busy, switching songs means unlocking your phone, opening Spotify, searching, tapping — too many steps, distracting and potentially dangerous.

---

## 💡 What It Does

Say one sentence to Minis, and it uses the `spotify-hub` skill to search, play, skip, or adjust volume — without ever opening the Spotify app.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| `spotify-hub` | Search for music and control Spotify playback |

---

## 💬 Example Prompts

```text
Play "Sunny Day" by Jay Chou.
```

```text
Skip to the next track.
```

```text
Search for rainy-day jazz and start shuffle playback.
```

---


## 📸 Screenshots

![Screenshot](../../assets/screenshots/spotify-voice-control.jpg)

*📷 Say “change the song” → Minis switches to Apink's “Love Me More” · @wsvn53 · 2026-03-22*

## ⚙️ Requirements

- [ ] `spotify-hub` skill installed
- [ ] Spotify Premium account; Web API playback control is unavailable on Free accounts
- [ ] `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI` configured; use `http://127.0.0.1:8888/callback` as the redirect URI
- [ ] Complete the one-time Spotify OAuth authorization flow
- [ ] Keep at least one Spotify playback device active

---

## 👤 Contributor

[@wsvn53](https://x.com/wsvn53) · [appinn.com](https://www.appinn.com/iphone-automation-11-real-use-cases/)

## 📅 Last Verified

2026-03-22
