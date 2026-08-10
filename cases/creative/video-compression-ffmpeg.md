# Local Video Compression with ffmpeg

> **By @wsvn53 · Feb 27, 2026** · [Original Tweet](https://x.com/wsvn53/status/2027265760717144263)

### Pain Point

4K videos shot on iPhone 17 Pro are 30–50 MB each. Too big to share on WeChat or upload, but you don't want to lose quality.

### What It Does

Drop the video into Minis, it auto-detects video parameters, picks the optimal compression strategy, and runs ffmpeg locally on your phone. Nothing leaves your device.

Full flow shown in screenshot (5 steps):
1. Send video: "Compress this video while keeping quality as high as possible"
2. Inspect video info (6s): 3840×2160 (4K), 10.6s, ~32 MB, H.264, 24 Mbps
3. Analyze video streams
4. Optimal strategy: H.265 (HEVC) re-encode, CRF 23 slow preset
5. Compare before/after ✅: 32 MB → 13.5 MB, **58% smaller**, 4K quality visually identical

### Example Prompt

```
Compress this video while keeping quality as high as possible
```

---

## 📸 Screenshots

![Minis detects 4K video info and compresses 32MB to 13.5MB with ffmpeg H.265](../../assets/screenshots/video-compression-ffmpeg.jpg)

📷 Shared by @wsvn53 · 2026-02-27

---

**Last Verified:** 2026-02-27
**Category:** Creative & Content
**Contributor:** [@wsvn53](https://x.com/wsvn53)
