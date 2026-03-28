# 😎 Awesome Minis [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated collection of real-world **[Minis](https://minis.app)** use cases, workflows, and creative scenarios — contributed by the community.

**Minis** is an AI-powered assistant running on iOS with a full Linux shell (Alpine Linux), native Apple framework integrations (HealthKit, Calendar, Reminders, HomeKit, etc.), and a rich skill ecosystem. This repository collects the best ways people are actually using it.

---

## 📋 Table of Contents

- [Health & Wellness](#-health--wellness)
- [Productivity & Automation](#-productivity--automation)
- [Data & Research](#-data--research)
- [Creative & Content](#-creative--content)
- [Smart Home & IoT](#-smart-home--iot)
- [Social Media & Communication](#-social-media--communication)
- [Finance & Tracking](#-finance--tracking)
- [Developer Tools](#-developer-tools)
- [Skills](#-skills)
- [Contributing](#-contributing)

---

## 🏥 Health & Wellness

| Name | Description | Skills Used |
|------|-------------|-------------|
| [Apple Watch Heart Health Monitor](cases/health/apple-watch-heart-health.md) | Analyze heart rate, HRV, blood oxygen, and ECG data from HealthKit to detect early warning signs and generate a risk report | `cardiac-health-monitor` |
| [Sleep Quality Analysis](cases/health/sleep-quality-analysis.md) | Deep dive into sleep stages (REM/Deep/Core), blood oxygen during sleep, and HRV trends with weekly summary charts | `health-sleep-analysis` |

## ⚡ Productivity & Automation

| Name | Description | Skills Used |
|------|-------------|-------------|
| [Smart Daily Briefing](cases/productivity/smart-daily-briefing.md) | Every morning: pull calendar events, weather, news headlines, and Reminders into a single spoken briefing | Built-in |
| [Minis Bug Collector](cases/productivity/minis-bug-collector.md) | Sync Telegram group feedback, extract bugs & feature requests, deduplicate against Reminders, and write new tasks automatically | `tg-hub`, `minis-bug-collector` |

## 🔬 Data & Research

| Name | Description | Skills Used |
|------|-------------|-------------|
| [Web Research Deep Dive](cases/research/web-research-deep-dive.md) | Use Exa AI search to research any topic, summarize findings, and export a structured Markdown report | `exa-search` |
| [Bilibili Content Analyzer](cases/research/bilibili-content-analyzer.md) | Fetch video subtitles, AI summaries, and comment sentiment for any Bilibili video | `bilibili-hub` |

## 🎨 Creative & Content

| Name | Description | Skills Used |
|------|-------------|-------------|
| [One-Click PPT Generator](cases/creative/one-click-ppt-generator.md) | Turn a script or outline into a Jobs-style minimal HTML presentation in seconds | `ppt-generator` |
| [AI Image Generation](cases/creative/ai-image-generation.md) | Generate and edit images from text prompts using Pollinations or Nano Banana (Gemini) | `pollinations-image-gen`, `nano-banana` |
| [Humanize AI Writing](cases/creative/humanize-ai-writing.md) | Remove AI writing patterns from any text to make it sound natural and human | `humanizer`, `humanizer-zh` |
| [Text-to-Speech with Doubao](cases/creative/doubao-tts.md) | Convert any text to high-quality speech using ByteDance Doubao TTS with 21+ voice options | `doubao-tts` |

## 🏠 Smart Home & IoT

| Name | Description | Skills Used |
|------|-------------|-------------|
| [HomeKit Scene Automation](cases/smarthome/homekit-scene-automation.md) | Control lights, AC, and scenes across rooms with natural language via HomeKit integration | Built-in |

## 📱 Social Media & Communication

| Name | Description | Skills Used |
|------|-------------|-------------|
| [Twitter/X Timeline Digest](cases/social/twitter-timeline-digest.md) | Fetch your X timeline, filter by topic, and get a daily digest of what matters | `twitter-x-hub` |
| [Weibo Trending Monitor](cases/social/weibo-trending-monitor.md) | Track Weibo hot search trends and keyword mentions in real-time | `weibo-hub` |
| [Maimai Company Insights](cases/social/maimai-company-insights.md) | Read workplace posts from any company's Maimai circle for culture and sentiment insights | `maimai-hub` |

## 💰 Finance & Tracking

| Name | Description | Skills Used |
|------|-------------|-------------|
| [Personal Finance Dashboard](cases/finance/personal-finance-dashboard.md) | Log expenses via chat, visualize spending trends, and get monthly summaries | Built-in |

## 🛠 Developer Tools

| Name | Description | Skills Used |
|------|-------------|-------------|
| [Remote iOS App Dev](cases/developer/remote-ios-app-dev.md) | SSH into a Mac, build and compile an iOS app, run tests, and commit code — all from Minis | `remote-dev-minis-app` |
| [Long Screenshot Stitcher](cases/developer/long-screenshot-stitcher.md) | Automatically stitch multiple iOS screenshots into one seamless long screenshot | `ios-long-screenshot` |

---

## 🧩 Skills

The use cases above leverage **Minis Skills** — reusable instruction sets that extend what Minis can do. Browse the official skill registry:

👉 **[OpenMinis/MinisSkills](https://github.com/OpenMinis/MinisSkills)**

Want to create your own skill? Use the built-in `skill-creator` skill for guided instructions.

---

## 🤝 Contributing

We welcome contributions from the community! Please read **[CONTRIBUTING.md](CONTRIBUTING.md)** before submitting.

**Quick summary:**
- Each use case lives in its own Markdown file under the appropriate `cases/` subfolder
- Use the [case template](CASE_TEMPLATE.md) to structure your submission
- Only submit use cases you have personally tested and verified
- Open a Pull Request — one use case per PR is preferred

---

## 📜 License

[CC0 1.0 Universal](LICENSE) — Public Domain. Use freely, no attribution required.

---

<p align="center">
  Made with ❤️ by the <a href="https://github.com/OpenMinis">OpenMinis</a> community
</p>
