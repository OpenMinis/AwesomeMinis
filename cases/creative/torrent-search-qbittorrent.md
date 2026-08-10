# Search Torrents & Manage qBittorrent Downloads

> **By [@wsvn53](https://x.com/wsvn53)**

### Pain Point

Downloading a movie means manually visiting torrent sites, comparing versions, copying magnet links, then opening qBittorrent WebUI to paste and add — tedious, and you have to remember each site's URL.

### What It Does

Tell Minis what you want to download in one sentence. It searches across multiple torrent sites, finds the best version, extracts the magnet link, and directly calls the qBittorrent WebUI API to add the task — then reports back the download status in real time.

**Full flow shown in screenshots (55 steps):**

**Screenshot 1 — Search:**
1. "Search online for the latest torrent of Xun Qin Ji, find a 4K version"
2. Loads exa-search skill, searches via Exa
3. Tries nyaa (no results) → retries with English title
4. Switches to Chinese media sites: HDSKY → 1337x → TPB → BTBTT → dmhy → torrentgalaxy
5. Finds result, confirms task added ✅ 55/55

**Screenshot 2 — Select version + add to qBittorrent:**
- Version list found, recommends Dolby Vision high-bitrate:
  - ⭐ Dolby Vision HQ (recommended): 2160p HQ.WEB-DL H265 DV DTS5.1
  - 60fps HQ: 2160p H265 60fps DTS5.1
  - 120fps: 2160p H265 120fps
  - HDR Standard: 2160p WEB-DL H265 HDR DTS5.1
- Outputs magnet link
- Re-tests connection → network OK (403 = not logged in, normal)
- Adds magnet to qBittorrent ✅
- Confirms download started:
- **Quest for Qin [Dolby Vision][HQ]** Back.to.the.Past.2025 2160p HQ.WEB-DL H265 DV DTS5.1
  - Size: 22.6 GB
  - Status: ⬇️ Downloading, 58.3 KB/s (connecting to peers)

### Skills Used

| Skill | Purpose |
|-------|---------|
| `qbt-hub` | Add the magnet link and monitor the qBittorrent task |
| `exa-search` *(optional)* | Search the web for candidate releases |

### Example Prompt

```
Search for the latest 4K Dolby Vision torrent of Xun Qin Ji and download it
```

### Requirements

- [ ] `qbt-hub` skill installed; it targets qBittorrent WebUI API v5.0+
- [ ] qBittorrent WebUI enabled and reachable from the phone through LAN, VPN, or Tailscale
- [ ] `QBT_HOST`, `QBT_USER`, and `QBT_PASS` configured in Minis environment variables
- [ ] Optional: `exa-search` for cross-site web retrieval; `EXA_API_KEY` is optional for basic use

---

## 📸 Screenshots

![Minis searches 7 torrent sites for 4K version of Xun Qin Ji in 55 steps](../../assets/screenshots/torrent-search-qbittorrent-1.jpg)

![Version comparison table, magnet link extracted, added to qBittorrent — 22.6GB downloading at 58.3 KB/s](../../assets/screenshots/torrent-search-qbittorrent-2.jpg)

📷 Shared by [@wsvn53](https://x.com/wsvn53)

---

**Last Verified:** 2026-03-31
**Category:** Creative & Content
**Contributor:** [@wsvn53](https://x.com/wsvn53)
