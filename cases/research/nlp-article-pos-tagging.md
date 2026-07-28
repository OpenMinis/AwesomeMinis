# Part-of-Speech Tagging an Article with Apple NLP

> Fetch a web article, scrape it to Markdown, then use Apple's on-device Natural Language framework to color-tag every word by part of speech — a fun, instant linguistic breakdown with zero API calls to a language model for the tagging itself.

---

## 🎯 Pain Point

Analyzing the grammatical structure of a piece of writing (nouns vs. verbs vs. adjectives, etc.) usually requires a dedicated NLP tool or library — not something you'd casually ask a chatbot for, since it needs actual linguistic parsing, not just "reading comprehension."

---

## 💡 What It Does

Minis combines browser-use (or a scraping tool) to fetch and convert a web article to Markdown, then pipes the text through Apple's native NaturalLanguage framework (via the `apple-nlp` CLI) to tag every token with its part of speech. It renders the result as an interactive, color-coded HTML page — nouns in blue, verbs in red, adjectives in purple, etc. — with a hoverable tag legend and per-word counts.

---

## 🛠 Skills Needed

None (built-in). Uses the native `apple-nlp` CLI plus a Markdown-scraping tool (the original review used Firecrawl; `web-content-extractor` from MinisSkills works as a local alternative) and the built-in WKWebView for rendering.

---

## 📋 How to Use

1. Give Minis a URL to an article (or paste the text directly).
2. Ask it to scrape it to Markdown and tag parts of speech with Apple NLP.
3. Minis renders an interactive HTML report you can scroll through, with a legend showing counts per part-of-speech category.

---

## 💬 Example Prompt

```
Fetch my most recent article from [site], scrape it as Markdown, tag its different parts
of speech with Apple NLP, and present it nicely.
```

---

## 📤 Expected Output

An HTML page titled with the article's headline, byline, and total tagged-token count, followed by a legend (Noun / Verb / Adjective / Adverb / Pronoun / Determiner / Preposition / Conjunction / Interjection / Number / Particle / Other, each with a running count), then the full article text rendered with every word color-highlighted and hoverable for its exact tag.

![Apple NLP part-of-speech tagging: article rendered with color-coded nouns, verbs, and adjectives, plus a hoverable tag legend with live counts](../../assets/screenshots/nlp-article-pos-tagging.jpg)

---

## ⚙️ Configuration / Requirements

- [ ] A way to fetch/scrape article text (browser_use, a scraping skill, or pasted text directly)
- [ ] No API key needed for the NLP tagging itself — it's fully on-device via Apple's framework

---

## 💡 Tips & Variations

- Great demo of combining browser-use + a native Apple framework + HTML artifact rendering in one request.
- Try it on your own writing to spot overused word patterns (e.g. adjective-heavy sentences).
- Works fully offline for the tagging step once the text is in front of Minis — only the initial fetch needs network access.

---

## 👤 Author

Sourced from: [Open Minis Is the iOS Agent I Wish Siri AI Could Be](https://www.macstories.net/reviews/open-minis-is-the-ios-agent-i-wish-siri-ai-could-be/) by Federico Viticci, MacStories (2026-07-20).

---

## 📅 Last Verified

2026-07
