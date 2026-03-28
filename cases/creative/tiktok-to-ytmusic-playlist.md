# TikTok 好歌一键整理成 YouTube Music 歌单

**TikTok Song → YouTube Music Playlist in One Step**

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-16 / appinn.com · 2026-03-28*

---

## 🎯 痛点 / Pain Point

**中文：** 在 TikTok 刷到好听的歌，想加到 YouTube Music 歌单，但两个平台之间没有直接同步，手动搜歌再添加很麻烦。

**English:** You hear a great song on TikTok and want it in your YouTube Music playlist — but there's no direct sync between the two platforms, and manually searching and adding each song is a pain.

---

## 💡 做了什么 / What It Does

**中文：** 将 TikTok 评论区截图（通常有大量歌名）发给 Minis，它识别图中的歌曲名称，逐一在 YouTube Music 中搜索，批量添加到指定歌单。

**English:** Send Minis a screenshot of TikTok comments (which often contain song names), it recognizes the song titles from the image, searches each one on YouTube Music, and batch-adds them to your playlist.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in (Vision OCR) | 识别截图中的歌名 / Recognize song names from screenshot |
| `ytmusic-hub` | 搜索并添加歌曲到歌单 / Search and add songs to playlist |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
（附上 TikTok 评论截图）
把这些歌都加到我的 YouTube Music「怀旧」歌单里。
```

**English:**
```
(Attach TikTok comments screenshot)
Add all these songs to my YouTube Music "Nostalgia" playlist.
```

---

## ⚙️ 配置要求 / Requirements

- [ ] `ytmusic-hub` skill 已安装，YouTube Music Cookie 已配置

---

## 👤 贡献者 / Contributor

[@wsvn53](https://x.com/wsvn53) · [appinn.com](https://www.appinn.com/iphone-automation-11-real-use-cases/)

## 📅 Last Verified

2026-03-16
