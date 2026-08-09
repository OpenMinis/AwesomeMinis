# Bilibili Content Analyzer

> **By [@hanzhe-one](https://github.com/hanzhe-one) · Aug 9, 2026** · [Original Video](https://www.bilibili.com/video/BV1GJ411x7h7)

## 🇨🇳 中文

### 痛点

想深入分析 B 站视频内容（字幕全文、视频元数据、相关热门趋势、UP 主投稿历史），但手动逐帧看、复制字幕、搜关联视频太慢，且没有现成工具能一次性把这些结构化拿到。

### 做了什么

把一个 B 站视频链接（或 BV 号）发给 Minis，让它用 `bilibili-hub` 技能自动完成（约 10 秒）：

1. **抓取视频完整字幕** —— 包含时间轴的全文文本（中/英/多语言）
2. **提取视频元数据** —— 标题、UP主、分区、时长、播放/点赞/投币/收藏/评论等统计、简介
3. **关键词搜索关联视频** —— 基于视频主题自动搜索同类内容
4. **获取站内热门榜单** —— 对比当前内容热度趋势
5. **可选：拉取 UP 主投稿历史** —— 纵向分析创作者内容风格

**真实输出示例（Rick Astley 官方 MV）：**

```
标题: 【官方 MV】Never Gonna Give You Up - Rick Astley
UP: 索尼音乐中国
时长: 03:33
分区: 音乐
字幕: 完整中文歌词（含时间轴），约 2000 字
```

**搜索 "Python 教程" 返回真实结果：**
- BV1rpWjevEip 【全748集】目前B站最全最细的Python零基础全套教程…
- BV1qW4y1a7fU 黑马程序员python零基础全套教程…

**站内热门前 5（实时）：**
1. 做什么都是个人的话，会不会太自由了 👁 294万
2. 评分8.7！我们奥特曼有救啦！提欧奥特曼开播吐槽！ 👁 37万
3. ...

### 示例 Prompt

```
分析这个 B 站视频：https://www.bilibili.com/video/BV1GJ411x7h7
把字幕全文、视频基本信息、搜同类热门视频、再给我站内热门榜单前 5
```

---

## 🇺🇸 English

### Pain Point

Want to deeply analyze a Bilibili video — full subtitles, metadata, related trending videos, uploader history — but manually watching frame-by-frame, copying subtitles, and searching related content is too slow. No existing tool structures all this in one pass.

### What It Does

Send a Bilibili video link (or BV ID) to Minis, and it uses the `bilibili-hub` skill to automatically (~10 sec):

1. **Extract full subtitles** — complete timestamped transcript (Chinese/English/multi-language)
2. **Fetch video metadata** — title, uploader, category, duration, view/like/coin/favorite/comment stats, description
3. **Search related videos by keyword** — auto-discover similar content based on video topic
4. **Get site-wide hot ranking** — benchmark against current platform trends
5. **Optional: Pull uploader's video history** — longitudinal analysis of creator's content style

**Real output example (Rick Astley Official MV):**

```
Title: 【Official MV】Never Gonna Give You Up - Rick Astley
Uploader: Sony Music China
Duration: 03:33
Category: Music
Subtitles: Full Chinese lyrics (with timestamps), ~2000 chars
```

**Search "Python tutorial" returns real results:**
- BV1rpWjevEip 【748 eps】Most comprehensive Python zero-to-hero course on Bilibili 2026…
- BV1qW4y1a7fU HeiMa Programmer Python zero-to-mastery in 8 days…

**Site-wide hot top 5 (live):**
1. "If everything is personal choice, is it too free?" 👁 2.94M
2. "Rating 8.7! Our Ultraman is saved! Tiga Ultraman premiere roast!" 👁 370K
3. ...

### Example Prompt

```
Analyze this Bilibili video: https://www.bilibili.com/video/BV1GJ411x7h7
Give me full subtitles, video metadata, search similar hot videos, and site-wide hot ranking top 5
```

### Requirements

- `bilibili-hub` skill installed
- Bilibili login cookies available (auto-fetched via browser: SESSDATA, bili_jct, DedeUserID)
  - Navigate to https://www.bilibili.com in Minis browser
  - Skill reads cookies automatically via `browser_use get_cookies`

---

## 📸 Screenshots

![Real Bilibili search results for "Python 教程" fetched live via bilibili-hub](../../assets/screenshots/bilibili-content-analyzer-1.jpg)

*Live screenshot of Bilibili search results — real videos, play counts, and uploaders fetched via the bilibili-hub skill.*

---

**Last Verified:** 2026-08-09
**Category:** Research
**Contributor:** [@hanzhe-one](https://github.com/hanzhe-one)
