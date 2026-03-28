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

| Name | Description | By | Skills Used |
|------|-------------|----|-------------|
| [Apple Watch Heart Health Monitor](cases/health/apple-watch-heart-health.md) | Analyze heart rate, HRV, blood oxygen, and ECG data from HealthKit to detect early warning signs and generate a risk report | OpenMinis | `cardiac-health-monitor` |
| [Sleep Quality Analysis](cases/health/sleep-quality-analysis.md) | Deep dive into sleep stages (REM/Deep/Core), blood oxygen during sleep, and HRV trends with weekly summary charts | 🚧 stub | `health-sleep-analysis` |
| [Explore Comprehensive HealthKit Data](cases/health/health-data-exploration.md) | Ask Minis to autonomously explore all your Apple Watch metrics — heart rate, steps, sleep, SpO₂ — and give you a weekly trend analysis | Alan Chen | Built-in |

## ⚡ Productivity & Automation

| Name | Description | By | Skills Used |
|------|-------------|----|-------------|
| [Smart Daily Briefing](cases/productivity/smart-daily-briefing.md) | Every morning: pull calendar events, weather, news headlines, and Reminders into a single spoken briefing | OpenMinis | Built-in |
| [Daily Briefing Auto-Push to WeChat](cases/productivity/daily-briefing-wechat-push.md) | Schedule Minis on iPad to fetch weather + news daily and auto-push to WeChat via openilink-hub | meng nimen | Built-in + openilink-hub |
| [Push Minis Results to WeChat](cases/productivity/wechat-push-via-openilink.md) | Use openilink-hub middleware to push any Minis output (reports, alerts, summaries) to WeChat | meng nimen | Built-in + openilink-hub |
| [Convert Notes & Ideas into Dida Tasks](cases/productivity/todo-from-notes-dida.md) | Dump raw notes or brain dumps to Minis — it extracts and polishes them into tasks and writes them to Dida (TickTick) | SI7gen1 | Custom (Dida API) |
| [Schedule Minis Tasks via iOS Shortcuts](cases/productivity/shortcuts-scheduled-task.md) | Use iOS Shortcuts automations to trigger Minis tasks on a schedule — no manual app launch needed | Community | iOS Shortcuts |
| [Remote Control Home Phone to Run Tasks](cases/productivity/remote-control-home-phone.md) | Remotely trigger Minis tasks on your home phone/iPad from anywhere via SSH or network | 朦胧 22:36 | Built-in (SSH) |
| [Minis Bug Collector](cases/productivity/minis-bug-collector.md) | Sync Telegram group feedback, extract bugs & feature requests, deduplicate against Reminders, and write new tasks automatically | OpenMinis | `tg-hub`, `minis-bug-collector` |

## 🔬 Data & Research

| Name | Description | By | Skills Used |
|------|-------------|----|-------------|
| [Automated Paywall Bypass Article Reader](cases/research/paywall-bypass-reader.md) | Automatically rewrite paywalled article URLs to public archive links and read full content inside the chat | oneasai | Built-in (browser) |
| [Fetch HK News & Generate Chinese HTML Digest](cases/research/hk-news-html-digest.md) | Fetch Hong Kong news articles, translate and summarize in Chinese, output as a formatted HTML digest | meng nimen | Built-in (browser) |
| [Web Research Deep Dive](cases/research/web-research-deep-dive.md) | Use Exa AI search to research any topic, summarize findings, and export a structured Markdown report | 🚧 stub | `exa-search` |
| [Bilibili Content Analyzer](cases/research/bilibili-content-analyzer.md) | Fetch video subtitles, AI summaries, and comment sentiment for any Bilibili video | 🚧 stub | `bilibili-hub` |

## 🎨 Creative & Content

| Name | Description | By | Skills Used |
|------|-------------|----|-------------|
| [One-Click PPT Generator](cases/creative/one-click-ppt-generator.md) | Turn a script or outline into a Jobs-style minimal HTML presentation in seconds | OpenMinis | `ppt-generator` |
| [Read Article Then Auto-Generate Audio](cases/creative/article-read-then-tts.md) | After summarizing an article, automatically generate a matching audio version with doubao-tts and auto-play it | oneasai | `doubao-tts` |
| [Local Lightweight TTS on Old iPhone](cases/creative/edge-tts-local-voice.md) | Install edge-tts via Minis shell for free, offline TTS — works even on a 64GB iPhone 8 Plus | 小渔 黄 | edge-tts (shell) |
| [Reverse-Engineered Doubao TTS](cases/creative/doubao-tts-reverse-engineering.md) | Use an open-source reverse-engineered Doubao TTS client for high-quality Chinese voice — no API tokens needed | oneasai | Custom |
| [AI Image Generation](cases/creative/ai-image-generation.md) | Generate and edit images from text prompts using Pollinations or Nano Banana (Gemini) | 🚧 stub | `pollinations-image-gen`, `nano-banana` |
| [Humanize AI Writing](cases/creative/humanize-ai-writing.md) | Remove AI writing patterns from any text to make it sound natural and human | 🚧 stub | `humanizer`, `humanizer-zh` |
| [Text-to-Speech with Doubao](cases/creative/doubao-tts.md) | Convert any text to high-quality speech using ByteDance Doubao TTS with 21+ voice options | 🚧 stub | `doubao-tts` |

## 🏠 Smart Home & IoT

| Name | Description | By | Skills Used |
|------|-------------|----|-------------|
| [HomeKit Scene Automation](cases/smarthome/homekit-scene-automation.md) | Control lights, AC, and scenes across rooms with natural language via HomeKit integration | 🚧 stub | Built-in |

## 📱 Social Media & Communication

| Name | Description | By | Skills Used |
|------|-------------|----|-------------|
| [Twitter/X Timeline Digest](cases/social/twitter-timeline-digest.md) | Fetch your X timeline, filter by topic, and get a daily digest of what matters | 🚧 stub | `twitter-x-hub` |
| [Weibo Trending Monitor](cases/social/weibo-trending-monitor.md) | Track Weibo hot search trends and keyword mentions in real-time | 🚧 stub | `weibo-hub` |
| [Maimai Company Insights](cases/social/maimai-company-insights.md) | Read workplace posts from any company's Maimai circle for culture and sentiment insights | 🚧 stub | `maimai-hub` |

## 💰 Finance & Tracking

| Name | Description | By | Skills Used |
|------|-------------|----|-------------|
| [Personal Finance Dashboard](cases/finance/personal-finance-dashboard.md) | Log expenses via chat, visualize spending trends, and get monthly summaries | 🚧 stub | Built-in |

## 🛠 Developer Tools

| Name | Description | By | Skills Used |
|------|-------------|----|-------------|
| [Managing Oracle Free-Tier Servers](cases/developer/turtle-oracle-server-management.md) | Manage multiple Oracle free-tier servers with natural language — check disk, memory, services, run commands | 采菇凉滴小蘑菇 | Built-in (SSH) |
| [Screenshot API Console to Auto-Configure](cases/developer/api-setup-via-screenshot.md) | Screenshot a confusing API console and let Minis read it, extract keys, and configure everything automatically | 小渔 黄 | Built-in (vision) |
| [Real-Time Execution Monitor on iPad](cases/developer/realtime-execution-monitor-ipad.md) | Generate a live web dashboard that monitors Minis task execution in real-time, viewable in split-screen on iPad | king 华 | Built-in (shell) |
| [Auto-Copy Skills Between Devices/Agents](cases/developer/skill-copy-between-devices.md) | Let Minis detect and copy all skill configs from another AI agent platform and recreate them | 如幻 | Built-in |
| [Remote iOS App Dev](cases/developer/remote-ios-app-dev.md) | SSH into a Mac, build and compile an iOS app, run tests, and commit code — all from Minis | OpenMinis | `remote-dev-minis-app` |
| [Long Screenshot Stitcher](cases/developer/long-screenshot-stitcher.md) | Automatically stitch multiple iOS screenshots into one seamless long screenshot | OpenMinis | `ios-long-screenshot` |

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
