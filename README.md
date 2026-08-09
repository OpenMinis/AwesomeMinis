😎 Awesome Minis Awesome
A curated collection of real-world Minis use cases, workflows, and creative scenarios — contributed by the community.

Minis is an AI-powered assistant running on iOS with a full Linux shell (Alpine Linux), native Apple framework integrations (HealthKit, Calendar, Reminders, HomeKit, etc.), and a rich skill ecosystem. This repository collects the best ways people are actually using it.

Minis use cases banner

📋 Table of Contents
English Translations
Health & Wellness
Productivity & Automation
Data & Research
Creative & Content
Finance & Tracking
Smart Home & IoT
Developer Tools
Contributing
🏥 Health & Wellness
Name	Description	By	Skills Used
Apple Watch Heart Health Monitor	Analyze heart rate, HRV, blood oxygen, and ECG data from HealthKit to detect early warning signs and generate a risk report	OpenMinis	cardiac-health-monitor
Photo a Coffee → Auto-Log Caffeine	Take a photo of your coffee, Minis identifies it and automatically logs the caffeine intake to Apple Health	@wsvn53	Built-in
Photo Every Meal → Auto-Log Nutrition	Snap a photo of each meal — Minis identifies dishes, estimates calories/protein/carbs, and logs it all to Apple Health	@infinite_Game_	Built-in
Photo + HealthKit: "How Much Did I Walk That Night?"	Find a vacation photo by description, then auto cross-reference HealthKit steps/distance for that exact date and time window — chaining Photos, memory, and HealthKit in one pass	MacStories (Federico Viticci)	Built-in
⚡ Productivity & Automation
Name	Description	By	Skills Used
Smart Daily Briefing	Every morning: pull calendar events, weather, news headlines, and Reminders into a single spoken briefing	OpenMinis	Built-in
X Timeline Voice Alarm	Replace your morning alarm — Shortcuts auto-fetches your X Timeline, summarizes it, generates TTS audio, and plays it to wake you up	@wsvn53	twitter-x-hub, doubao-tts
Auto-Create Calendar from Shared Content	Share any content with a time and place to Minis via the iOS Share Sheet — it instantly creates the calendar event	@wsvn53	Built-in
Daily Briefing Auto-Push to WeChat	Schedule Minis on iPad to fetch weather + news daily and auto-push to WeChat via openilink-hub	meng nimen	Built-in + openilink-hub
Push Minis Results to WeChat	Use openilink-hub middleware to push any Minis output (reports, alerts, summaries) to WeChat	meng nimen	Built-in + openilink-hub
Group Messages → Auto-Extract to Reminders	Pull Telegram group messages, auto-extract bugs and tasks, deduplicate, and write to Apple Reminders	@wsvn53	tg-hub, Built-in
Web Page → Apple Notes	Send any URL to Minis — it fetches, summarizes, and saves structured notes directly to Apple Notes	@wsvn53	Built-in
Mount Obsidian Vault as a Minis Knowledge Workspace	Mount your Obsidian vault into Minis, then summarize, clean up, research, and write Markdown notes back into the vault	Open Minis community	Built-in
Batch Set Complex Alarms	Describe your entire alarm schedule in one message — Minis creates all of them at once	appinn	Built-in
Convert Notes & Ideas into Dida Tasks	Dump raw notes or brain dumps to Minis — it extracts and polishes them into tasks and writes them to Dida (TickTick)	SI7gen1	Custom (Dida API)
Schedule Minis Tasks via iOS Shortcuts	Use iOS Shortcuts automations to trigger Minis tasks on a schedule — no manual app launch needed	Community	iOS Shortcuts
Edit Clash Config Without Touching YAML	Drop your Clash config into Minis, say what you want changed — it reads, edits, and outputs a new file with a change summary. Zero YAML editing	@wsvn53	Built-in
Remote Control Home Phone to Run Tasks	Remotely trigger Minis tasks on your home phone/iPad from anywhere via SSH or network	朦胧	Built-in (SSH)
Course Creation Assistant	产品经理用 Minis 完成课程设计、代码和逐字稿	@sawyer-wang	project-case-builder, video-script-writer
Taobao Store Management	Built a complete Taobao toolkit from scratch via SSH — order tracking, price comparison, cart management, buyer chat — zero code knowledge required	Da weiwei	Built-in (SSH + shell)
WeRead AI Reading Companion	Connect your WeRead account — browse bookshelf, export highlights, analyze reading habits, and get personalized book recommendations in one conversation	𝐍𝐢𝐜𝐤𝐢𝐥𝐢𝐬𝐦	微信读书
Custom Scheduled Notification with Article Summary	Fetch fresh content, then fire a real iOS notification with a custom title and summary body via the native Notification framework — great for pinging you when a long task finishes	MacStories (Federico Viticci)	Built-in
Location-Aware Detailed Weather Forecast	Grab your live location and pull a detailed native Apple Weather forecast — hourly table, UV index, feels-like temps, and a practical human-readable takeaway	MacStories (Federico Viticci)	Built-in
🔬 Data & Research
Name	Description	By	Skills Used
Automated Paywall Bypass Article Reader	Automatically rewrite paywalled article URLs to public archive links and read full content inside the chat	oneasai	Built-in (browser)
Fetch HK News & Generate Chinese HTML Digest	Fetch Hong Kong news articles, translate and summarize in Chinese, output as a formatted HTML digest	meng nimen	Built-in (browser)
City Commercial Market Research Report	One sentence → Minis searches JLL/Winshang/DTZ, writes analysis scripts, and generates a full market report with charts	@wsvn53	Built-in
Tweet Fact-Check: Verify Health Claims	Paste any tweet link → Minis fetches the content and cross-checks claims against medical literature, outputs a structured verdict table	@wsvn53	twitter-x-hub
Part-of-Speech Tagging with Apple NLP	Fetch a web article, scrape it to Markdown, then use Apple's on-device Natural Language framework to color-tag every word by part of speech in an interactive HTML report	MacStories (Federico Viticci)	Built-in
MacBook Neo Purchase Decision	One prompt → benchmark ladder (single/multi-core vs all MacBook models), deal-breaker analysis, China subsidy price breakdown, and an AI-generated shareable infographic	OpenMinis	Built-in, nano-banana-2
Bilibili Content Analyzer	Extract full subtitles, metadata, search related videos & hot rankings from any Bilibili video	@hanzhe-one	bilibili-hub
🎨 Creative & Content
Name	Description	By	Skills Used
Search Torrents & Manage qBittorrent Downloads	One sentence → Minis searches 7 torrent sites, picks the best version, extracts magnet link, adds to qBittorrent remotely, reports download status	@wsvn53	exa-search
Download X/Twitter Videos	Paste an X video link — Minis auto-installs yt-dlp, downloads video+audio streams, merges with ffmpeg, auto-debugs errors	@wsvn53	Built-in
Local Video Compression with ffmpeg	Drop a 4K video — Minis detects codec/bitrate, picks optimal H.265 settings, compresses locally. 32 MB → 13.5 MB, 58% smaller, no quality loss	@wsvn53	Built-in
One-Click PPT Generator	Turn a script or outline into a Jobs-style minimal HTML presentation in seconds	OpenMinis	ppt-generator
End-to-End Automated Video Production	Research → script → TTS voiceover → image search → ffmpeg edit → upload to Bilibili, all in one session (200+ tool calls)	@wsvn53	bilibili-hub, doubao-tts, ffmpeg
TikTok Song → YouTube Music Playlist	Screenshot TikTok comments with song names, Minis OCRs them and batch-adds all songs to your YouTube Music playlist	@wsvn53	ytmusic-hub
Spotify Voice Control	Search songs, skip tracks, and control Spotify playback with a single sentence — no app needed	@wsvn53	spotify-hub
Read Article Then Auto-Generate Audio	After summarizing an article, automatically generate a matching audio version with doubao-tts and auto-play it	oneasai	doubao-tts
Local Lightweight TTS on Old iPhone	Install edge-tts via Minis shell for free, offline TTS — works even on a 64GB iPhone 8 Plus	小渔 黄	edge-tts (shell)
AI Personal Color Analysis	Upload a selfie — Minis determines your 12-season color type and generates a professional diagnosis report with outfit, makeup, hairstyle, and accessory recommendations	采菇凉滴小蘑菇	personal-color-analysis
Interactive Vacation Photo Map with MapKit	Turn scattered vacation photos into a single interactive HTML map artifact — photo pins on real locations via MapKit JS, rendered natively in WKWebView, tappable into Apple Maps	MacStories (Federico Viticci)	Built-in
Music Library Deep Research	Ask about your Apple Music library the way you'd ask a friend — Minis inspects it via the native Media framework and reasons through misfiled B-sides and partial EPs	MacStories (Federico Viticci)	Built-in
💰 Finance & Tracking
Name	Description	By	Skills Used
Photo a Receipt → Auto-Log Expense	Snap a receipt photo — Minis uses Apple Vision to OCR it, extracts merchant/amount/items, auto-categorizes and logs the expense	Zigzag	Built-in (Vision)
Stock Technical Analysis with Charts	Share a stock ticker — Minis scrapes Futu/Yahoo Finance/TradingView, generates K-line + MACD + RSI charts and a full technical analysis report	@wsvn53	Built-in
🏠 Smart Home & IoT
Name	Description	By	Skills Used
Scan Nearby Bluetooth LE Devices	Ask what's around you — Minis scans real nearby Bluetooth LE devices via the native framework and returns a ranked signal-strength table, no separate scanner app needed	MacStories (Federico Viticci)	Built-in
👨‍💻 Developer Tools
Name	Description	By	Skills Used
Rescue a Crashed OpenClaw via SSH	OpenClaw crashed after an update? SSH in from your iPhone, auto-diagnose and restart the service — no laptop needed	@wsvn53	Built-in (SSH)
Remote Dev & Architecture Diagram Generation	SSH into a remote server, scan Swift source files, extract 3-layer architecture, generate diagram via Nano Banana — 2 min, zero intervention	@wsvn53	Built-in (SSH)
Managing Oracle Free-Tier Servers	Manage multiple Oracle free-tier servers with natural language — check disk, memory, services, run commands	采菇凉滴小蘑菇	Built-in (SSH)
🧩 Skills
The use cases above leverage Minis Skills — reusable instruction sets that extend what Minis can do. Browse the official skill registry:

👉 OpenMinis/MinisSkills

Want to create your own skill? Use the built-in skill-creator skill for guided instructions.

🤝 Contributing
We welcome contributions from the community! Please read CONTRIBUTING.md before submitting.

Quick summary:

Each use case lives in its own Markdown file under the appropriate cases/ subfolder
Use the case template to structure your submission
Only submit use cases you have personally tested and verified
Open a Pull Request — one use case per PR is preferred
📜 License
CC0 1.0 Universal — Public Domain. Use freely, no attribution required.


  Made with ❤️ by the OpenMinis community
