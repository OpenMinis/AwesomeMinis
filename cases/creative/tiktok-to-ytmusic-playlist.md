# TikTok Song → YouTube Music Playlist in One Step

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-16 / appinn.com · 2026-03-28*

---

## 🎯 Pain Point

You hear a great song on TikTok and want it in your YouTube Music playlist — but there's no direct sync between the two platforms, and manually searching and adding each song is a pain.

---

## 💡 What It Does

Send Minis a screenshot of TikTok comments (which often contain song names), it recognizes the song titles from the image, searches each one on YouTube Music, and batch-adds them to your playlist.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in (Vision OCR) | Recognize song names from screenshot |
| `ytmusic-hub` | Search for tracks and add them to a playlist |

---

## 💬 Example Prompt


```
(Attach TikTok comments screenshot)
Add all these songs to my YouTube Music "Nostalgia" playlist.
```

---


## 📸 Screenshots

![Screenshot](../../assets/screenshots/tiktok-to-ytmusic-playlist.jpg)

*📷 Send a TikTok link → identify 50 Chinese-language soundtrack songs → export a YouTube Music playlist · @wsvn53 via appinn.com · 2026-03-16*

## ⚙️ Requirements

- [ ] `ytmusic-hub` skill installed
- [ ] Sign in at `https://music.youtube.com` in the Minis browser
- [ ] Use `browser_use get_cookies`, then run the skill's `setup_auth.py` to generate `/var/minis/workspace/ytmusic_headers.json`
- [ ] Treat `ytmusic_headers.json` as sensitive login material and do not share it

---

## 👤 Contributor

[@wsvn53](https://x.com/wsvn53) · [appinn.com](https://www.appinn.com/iphone-automation-11-real-use-cases/)

## 📅 Last Verified

2026-03-16
