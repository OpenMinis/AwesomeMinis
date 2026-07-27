# Download X/Twitter Videos

> **By @wsvn53 · Feb 27, 2026** · [Original Tweet](https://x.com/wsvn53/status/2027261270542713040)

### Pain Point

X has no official video download button. Third-party sites are full of ads, break frequently, or don't support HD.

### What It Does

Paste an X video link, Minis auto-installs yt-dlp, downloads video and audio streams, merges them with ffmpeg, auto-debugs any errors, and gives you a direct file link when done.

Full flow shown in screenshot:
1. Send X video link: "Help me download this video"
2. Check if yt-dlp is installed
3. Download from X/Twitter (filename error → auto-retry with simpler name)
4. Check ffmpeg availability → list temp files
5. Merge video and audio streams ✅ 6/6

### Example Prompt

```
Help me download this video: https://x.com/xxx/status/xxx
```

---

## 📸 Screenshots

![Minis uses yt-dlp and ffmpeg to download and merge X video](../../assets/screenshots/x-video-download.jpg)

📷 Shared by @wsvn53 · 2026-02-27

---

**Last Verified:** 2026-02-27
**Category:** Creative & Content
**Contributor:** [@wsvn53](https://x.com/wsvn53)
