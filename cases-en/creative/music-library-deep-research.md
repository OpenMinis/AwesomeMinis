# Music Library Deep Research: Singles & B-Sides Audit

> Ask about your music library the way you'd ask a knowledgeable friend — Minis inspects your actual Apple Music library via the native Media framework, cross-references the web, and reasons through messy real-world catalog data (misplaced B-sides, partial EPs) that a simple lookup can't handle.

---

## 🎯 Pain Point

Music metadata in real libraries is messy: B-sides get filed under the wrong single, EPs are incomplete, live recordings pile up without dates. A basic "what songs do I have by X" query can't reconcile any of this — you need actual reasoning over your real library contents plus outside knowledge of the artist's discography.

---

## 💡 What It Does

Minis uses the native Apple Media framework (via a CLI) to inspect what's actually in your local Music library — track counts, release groupings — then cross-references that against general knowledge of the artist's official single/B-side discography to flag inconsistencies: singles where only the B-side is filed, EPs with just the title track present, recent live-only releases, etc. It presents a clean, categorized breakdown instead of a flat track list.

---

## 🛠 Skills Needed

None (built-in). Uses Minis' native Apple Media/MusicKit-backed CLI to inspect the local library — no external music skill required for the library-reading part.

---

## 📋 How to Use

1. Make sure the artist's music is present in your Apple Music library (owned or synced via subscription).
2. Ask Minis a specific discography question about your own library.
3. Minis will inspect track/release metadata locally, then reason about gaps or misfiled tracks.

---

## 💬 Example Prompt

```
What Oasis singles and b-sides do I have in my library?
```

---

## 📤 Expected Output

A categorized report, e.g.:

> You have 359 Oasis tracks across 38 release buckets in your Music library.
>
> **Single/EP releases — substantially complete:** Cigarettes & Alcohol, Whatever, All Around the World...
>
> **Partial single releases — often only the B-side is filed under the single:** Don't Look Back in Anger EP → "Step Out", Lyla → "Won't Let You Down"...
>
> **Recent live singles:** "Slide Away" — Cardiff, 4 July 2025...

![Music library deep research: Minis inspects the real Apple Music library via the native Media framework and reasons through misfiled B-sides and partial EPs](../../assets/screenshots/music-library-deep-research.jpg)

---

## ⚙️ Configuration / Requirements

- [ ] Apple Music library populated with the artist's tracks (via subscription sync or purchased music)
- [ ] No extra skill or API key needed — uses Minis' built-in Media framework CLI

---

## 💡 Tips & Variations

- Try it with any artist whose discography has complicated reissues, deluxe editions, or region-specific B-sides — that's where the reasoning shines vs. a flat "list my X tracks" query.
- Good comparison point against Siri, which can't currently reason across a full library plus outside catalog knowledge in one query.

---

## 👤 Author

Sourced from: [Open Minis Is the iOS Agent I Wish Siri AI Could Be](https://www.macstories.net/reviews/open-minis-is-the-ios-agent-i-wish-siri-ai-could-be/) by Federico Viticci, MacStories (2026-07-20).

---

## 📅 Last Verified

2026-07
