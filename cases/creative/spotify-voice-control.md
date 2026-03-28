# Spotify 语音控制：搜歌、切歌、一气呵成

**Spotify Voice Control: Search, Switch, Play**

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-22 / appinn.com · 2026-03-28*

---

## 🎯 痛点 / Pain Point

**中文：** 开车或做事时想换歌，解锁手机、打开 Spotify、搜索、点击——步骤太多，分心又危险。

**English:** When driving or busy, switching songs means unlocking your phone, opening Spotify, searching, tapping — too many steps, distracting and potentially dangerous.

---

## 💡 做了什么 / What It Does

**中文：** 对 Minis 说一句话，它通过 `spotify-hub` Skill 完成搜索、播放、切歌、调音量等操作，无需打开 Spotify App。

**English:** Say one sentence to Minis, and it uses the `spotify-hub` skill to search, play, skip, or adjust volume — without ever opening the Spotify app.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| `spotify-hub` | 控制 Spotify 播放 / Control Spotify playback |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
播放周杰伦的《晴天》
```
```
切到下一首
```
```
搜索一些适合下雨天的爵士乐，随机播放
```

**English:**
```
Play "Sunny Day" by Jay Chou
```
```
Skip to the next track
```
```
Search for some rainy-day jazz and shuffle play
```

---

## ⚙️ 配置要求 / Requirements

- [ ] `spotify-hub` skill 已安装
- [ ] Spotify Premium 账号（免费版不支持 API 控制播放）
- [ ] `SPOTIFY_CLIENT_ID` / `SPOTIFY_CLIENT_SECRET` 环境变量已配置

---

## 👤 贡献者 / Contributor

[@wsvn53](https://x.com/wsvn53) · [appinn.com](https://www.appinn.com/iphone-automation-11-real-use-cases/)

## 📅 Last Verified

2026-03-22
