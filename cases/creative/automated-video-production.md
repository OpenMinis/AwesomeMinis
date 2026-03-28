# 全程自动化视频创作（策划→剪辑→发布）

**End-to-End Automated Video Production**

> 💬 *From [@wsvn53](https://x.com/wsvn53) · 2026-03-18 / appinn.com · 2026-03-28*

---

## 🎯 痛点 / Pain Point

**中文：** 做一期科技视频需要：选题调研、写脚本、录音、找配图、剪辑、加字幕——每一步都耗时，且高度依赖专业工具。

**English:** Producing a tech video requires: topic research, scripting, voice recording, finding images, editing, adding subtitles — each step is time-consuming and requires specialized tools.

---

## 💡 做了什么 / What It Does

**中文：** 全程让 Minis 完成一期科技类视频的创作：分析 B 站 UP 主历史视频和播放量数据 → 策划视频选题和口播脚本 → 调用豆包 TTS 生成语音 → 搜索配图 → 用 ffmpeg 渲染字幕、合成视频。200+ 轮工具调用，最终产出一条完整视频上传 B 站。

**English:** Minis handles an entire tech video production: analyze Bilibili creator history and view data → plan topic and write voiceover script → generate audio with Doubao TTS → search for images → render subtitles and composite video with ffmpeg. 200+ tool calls, resulting in a complete video uploaded to Bilibili.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| `bilibili-hub` | 分析 UP 主数据 / Analyze creator data |
| `doubao-tts` | 生成口播语音 / Generate voiceover audio |
| Built-in (ffmpeg) | 渲染字幕、合成视频 / Render subtitles, composite video |
| `exa-search` | 搜索配图素材 / Search for images |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
帮我做一期科技类视频：
1. 分析 B 站科技区播放量最高的视频，找出共同特性
2. 策划一个选题，写口播脚本
3. 用豆包 TTS 生成语音
4. 搜索相关配图
5. 用 ffmpeg 合成完整视频
```

**English:**
```
Help me produce a tech video:
1. Analyze top-performing tech videos on Bilibili, find common traits
2. Plan a topic and write a voiceover script
3. Generate audio with Doubao TTS
4. Search for relevant images
5. Use ffmpeg to composite the final video
```

---

## ⚙️ 配置要求 / Requirements

- [ ] `bilibili-hub` skill 已安装
- [ ] `doubao-tts` skill 已安装，API 凭证已配置
- [ ] ffmpeg（`apk add ffmpeg`，Minis 可自动安装）

---

## 💡 Tips

- 开车时用豆包语音输入指令，全程解放双手
- 视频成品可直接在 Minis 内预览，满意后再上传

---

## 👤 贡献者 / Contributor

[@wsvn53](https://x.com/wsvn53) · [bilibili.com/video/BV1WpwizcEcq](https://www.bilibili.com/video/BV1WpwizcEcq)

## 📅 Last Verified

2026-03-18
