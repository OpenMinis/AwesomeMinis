# 阅读文章后自动生成语音版

**Read Article Then Auto-Generate Audio Version**

> 💬 *From the Open Minis community — shared by **oneasai** on 2026-03-24*

---

## 🎯 痛点 / Pain Point

**中文：** 读完长文后想边做事边听摘要，但手动复制到 TTS 工具很麻烦。

**English:** After reading a long article, you want to listen to the summary while doing something else — but copying to a TTS tool manually is tedious.

---

## 💡 做了什么 / What It Does

**中文：** Minis 完整阅读并总结文章后，自动调用 doubao-tts Skill 生成与文字版一致的语音，音频文件保存到 /var/minis/attachments/ 并在对话末尾自动播放。

**English:** After Minis reads and summarizes an article, it automatically calls the doubao-tts skill to generate an audio version matching the text summary exactly. The audio file is saved and auto-played at the end of the conversation.

---

## 🛠 所用技能 / Skills Used

| Skill | Purpose |
|-------|---------|
| `doubao-tts` | — |

---

## 💬 示例 Prompt / Example Prompt

**中文：**
```
读取这篇文章并总结主要观点，完成后自动用豆包 TTS 生成语音版并播放。
```

**English:**
```
Read this article and summarize the key points. When done, automatically generate an audio version using doubao-tts and play it.
```

---

## ⚙️ 配置要求 / Requirements

- [ ] `doubao-tts` skill 已安装
- [ ] `DOUBAO_TTS_APPID` / `DOUBAO_TTS_TOKEN` 环境变量已设置

---

## 🏷 标签 / Tags

`tts` `audio` `reading` `automation` `doubao`

---

## 👤 贡献者 / Contributor

来自 Open Minis Telegram 社区 / From the Open Minis Telegram community

原始分享者 / Original sharer: **oneasai**

---

## 📅 验证时间 / Last Verified

2026-03-24
