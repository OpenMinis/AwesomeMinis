# Tweet Fact-Check: Verify Health Claims with Minis

> **By [@wsvn53](https://x.com/wsvn53) · Apr 6, 2026** · [Original Tweet](https://x.com/wsvn53/status/2041181979308347818)

---

## 🎯 Pain Point

Social media is full of health claims. Some are exaggerated or misleading, but without a medical background it is hard to tell fact from fiction. People often end up either believing everything or dismissing everything.

---

## 💡 What It Does

After seeing a tweet claiming that “elevated homocysteine (Hcy) is a hidden cardiovascular killer linked to sudden death,” @wsvn53 sent the tweet link to Minis for fact-checking.

Minis automatically completed the workflow in 4 steps:

1. Load the `twitter-x-hub` skill
2. Navigate to X.com and get authentication cookies
3. Fetch the original tweet content
4. Perform a medical-literature-based fact-check

## ⚠️ Historical Example

The Hcy verdicts below are retained as the contributor's 2026 example. They were not independently revalidated during the 2026-07-27 MinisSkills catalog update. Re-run the literature search before relying on them for a current medical decision.

**Fact-check result:**

| Claim | Verdict |
|-------|---------|
| Elevated Hcy correlates with cardiovascular risk | ✅ Supported by epidemiological evidence |
| Hcy is a “hidden killer” | ✅ Mostly reasonable phrasing |
| Hcy significantly increases stroke risk | ✅ Good evidence; each +5 μmol/L is associated with roughly +20–30% stroke risk |
| Hcy significantly increases heart attack risk | ⚠️ Association is controversial; lowering Hcy does not necessarily reduce heart attack risk |
| Hcy is directly linked to sudden death | ❌ Insufficient evidence; exaggerated |

**Key correction:**

- Multiple RCTs such as HOPE-2, NORVIT, and VISP show that folate/B12 supplementation lowered Hcy but **did not significantly reduce heart attacks or death**. Hcy may be a biomarker rather than a direct cause.
- The “directly linked to sudden death” claim is weakly supported and likely overstated.

**Conclusion:** The general direction is reasonable, but the claim is somewhat exaggerated, especially around sudden death. It can be treated as a health reminder, but there is no need to panic.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| `twitter-x-hub` | Retrieve the original post and thread |
| Current web/literature search | Verify the claims against primary medical sources |

---

## 💬 Example Prompt

```text
https://x.com/someone/status/xxx — Is this claim accurate?
```

---

## ⚙️ Requirements

- [ ] `twitter-x-hub` skill installed
- [ ] Sign in to X in the Minis browser, use `browser_use get_cookies`, and load `auth_token` / `ct0` as `TWITTER_AUTH_TOKEN` / `TWITTER_CT0`
- [ ] Verify medical claims against current primary literature and clinical guidance; the historical example verdict is not a substitute for a fresh review

---

## 📸 Screenshots

![Minis fetches tweet and performs structured medical fact-check on Hcy claims](../../assets/screenshots/tweet-fact-check-1.jpg)

![Full evaluation table: stroke risk, heart attack, sudden death — conclusion: exaggerated](../../assets/screenshots/tweet-fact-check-2.jpg)

📷 Shared by [@wsvn53](https://x.com/wsvn53) · 2026-04-06

---

**Last Verified:** 2026-04-06
**Category:** Research
**Contributor:** [@wsvn53](https://x.com/wsvn53)
