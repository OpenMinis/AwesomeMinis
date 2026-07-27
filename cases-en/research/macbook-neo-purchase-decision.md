# Before You Buy: Use Minis for Purchase Decision Analysis — MacBook Neo Example

**One Prompt → Full Purchase Decision Report with Benchmark Ladder, Pros/Cons, and Price Research**

---

## 🎯 Pain Point

Before buying a new laptop, you need to watch many review videos, manually check prices across platforms, compare benchmark scores across generations, and understand subsidy-stacking rules. The information is scattered across Bilibili, tech media, Geekbench, and retailer promotion pages, often leaving you more confused than before.

---

## 💡 What It Does

Say one sentence to Minis. It automatically fetches Geekbench 6 scores, tech media reviews, e-commerce prices, and subsidy policies, then generates:

- **CPU benchmark ladder:** single-core and multi-core comparisons, clearly showing which models the target machine matches
- **Deal-breaker list:** structured cons with impact levels for different use cases
- **Use-case analysis:** distinguishes “pure Vibe Coding” from workloads like “compiling apps”
- **China final-price lookup:** official price → after national subsidy → with education discount → lowest trade-in price, all in one table
- **Shareable infographic:** an AI-generated purchase decision visual with a “hype vs. deal-breaker” style

Example: MacBook Neo (A18 Pro, starting at ¥4,599). Minis reached a conclusion in 5 minutes:

- Single-core performance ≈ MacBook Air M3; multi-core only ≈ M1, roughly 2020-level
- ¥3,909 after national subsidy; as low as ¥3,399 with education discount
- Good enough for pure Vibe Coding, but compiling iOS apps is multi-core intensive. After thermal throttling, Neo performance drops by 87%, and large-project compile time is 2x+ compared with M4
- **Verdict: fine as a ¥599 entry device, but not suitable as a primary development machine ❌**

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in `browser_use` | Fetch Geekbench scores, tech media reviews, and e-commerce prices |
| Built-in shell + Python | Aggregate data and run comparison analysis |
| `nano-banana` | Generate a shareable infographic with the Nano Banana 2 model |

---

## 💬 Example Prompts

```text
How does the MacBook Neo's CPU and benchmark scores compare to other MacBook models?
```

```text
What is the MacBook Neo's China price after the national subsidy?
```

```text
Generate an infographic titled “MacBook Neo — From Hype to Deal-Breaker”.
On the left, show the Neo benchmark ladder, comparing single-core and multi-core
scores with other Macs. On the right, list the cons and explain that it may be fine
for pure Vibe Coding, but I need to compile apps.
```

---

## ⚙️ Requirements

- [ ] `nano-banana` skill installed; it currently defaults to Nano Banana 2 (`gemini-3.1-flash-image-preview`)
- [ ] `GEMINI_API_KEY` configured for Gemini image generation
- [ ] No extra configuration for web search and data analysis; Minis built-in capabilities are enough

---

## 💡 Tips

- Replace the target with any digital product, such as “iPhone 17e vs previous iPhone SE models” or “RTX 5080 vs 4090 value comparison.”
- The generated infographic can be screenshotted and shared to Weibo, Xiaohongshu, or WeChat Moments.
- National subsidy policies may change quarterly; include the current month and year when asking for the latest pricing.
- For developers, focus on “multi-core performance” and “thermal throttling,” because these determine compile experience.

---

## 📸 Screenshots

![MacBook Neo — From Hype to Deal-Breaker: CPU ladder + deal-breaker infographic](../../assets/screenshots/macbook-neo-purchase-decision.png)

---

## 👤 Contributor

Internal case · Added 2026-04-09

---

## 📅 Last Verified

2026-04-09
