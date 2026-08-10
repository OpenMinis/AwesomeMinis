# Custom Scheduled Notification with Article Summary

> Ask Minis to fetch a fresh article and ping you with a real, actionable iOS notification — custom title, custom body, delivered on a schedule — using the native Notification framework directly.

---

## 🎯 Pain Point

You want a proactive nudge (not just a chat reply) when a task finishes — e.g. "the article you asked about is ready" — with a real system notification you can act on later, not just a message sitting in a chat thread you might not reopen.

---

## 💡 What It Does

Minis fetches the requested content (e.g. your latest published article), then calls the native `apple-notification` CLI to schedule a real iOS notification with a custom title and body — delivered a moment later on the lock screen / notification center, exactly like a notification from any other app.

---

## 🛠 Skills Needed

None (built-in). Uses Minis' native `apple-notification` CLI directly, plus whatever fetch/scrape method you use to retrieve the source content.

---

## 📋 How to Use

1. Ask Minis to fetch some content and notify you when done.
2. Grant the native Notification permission the first time.
3. The notification arrives with your custom title/body once the task completes.
4. Optionally, ask for a richer follow-up notification (e.g. with a summary) — Minis will tell you honestly if a requested feature (like an image attachment or action button) isn't supported by the native API, and what workaround would be needed (e.g. Pushover or a custom Shortcut).

---

## 💬 Example Prompt

```
Fetch my latest article from [site]. When you're done, send me a notification with the
title and a short summary in the body.
```

---

## 📤 Expected Output

A real native notification appears (visible on the lock screen/Home Screen banner), e.g.:

> **Siri AI and Apple's Trickle-Up Strategy**
> Summary: Siri AI is built for mainstream users—not agent power users. Apple is starting simple, then plans to 'trickle up' through iteration. Tap Minis for the article link.

Note the native notification tool only supports a plain title + body (no images, action buttons, or deep links) — Minis will tell you this honestly rather than pretending otherwise.

![Custom scheduled notification: real iOS lock-screen notification with a custom title and article summary, plus the underlying apple-notification shell call](../../assets/screenshots/scheduled-article-notification.jpg)

---

## ⚙️ Configuration / Requirements

- [ ] Notification permission granted to Minis
- [ ] A way to fetch the source content (browser_use, a scraping skill, etc.)

---

## 💡 Tips & Variations

- Chain this after any long-running task (a video render, a data scrape, a multi-step research task) so you don't have to keep checking back manually.
- If you need richer notifications (images, action buttons, deep links), combine with a Pushover integration or a custom Shortcut — Minis can help you set that up too.

---

## 👤 Author

Sourced from: [Open Minis Is the iOS Agent I Wish Siri AI Could Be](https://www.macstories.net/reviews/open-minis-is-the-ios-agent-i-wish-siri-ai-could-be/) by Federico Viticci, MacStories (2026-07-20).

---

## 📅 Last Verified

2026-07
