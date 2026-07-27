# WeRead Skill — Let AI Become Your Reading Companion

> 💬 *From **𝐍𝐢𝐜𝐤𝐢𝐥𝐢𝐬𝐦** · 2026-05-16 via Open Minis Telegram*

---

## 🎯 Pain Point

You may have hundreds of books in your WeRead library, but it is hard to know which books you actually read, how long you spent reading, what you highlighted, and which books are worth continuing — especially without manually organizing everything.

---

## 💡 What It Does

WeRead officially released a Minis Skill: `weread-skills`. After connecting your WeRead account, AI can query your reading records whenever you ask. With one sentence, Minis can:

- 📚 **Browse your bookshelf:** view your library, count e-books, and summarize public/private reading status
- 🔍 **Search books:** search the WeRead store for any book and retrieve title, author, rating, and key information
- 📊 **Analyze reading stats:** summarize reading time, reading days, preferences, and habits
- 📖 **Inspect book details:** view chapter lists, reading progress, and the reading journey for a book
- ✏️ **Review notes and highlights:** view highlights and thoughts, export notes, and revisit your reading reflections
- ⭐ **Recommend books:** suggest books based on your reading preferences

In a real test, Minis analyzed 27 highlights and notes from *Madame Bovary*, identified three reading traits, assessed the user as an “intermediate-advanced literary reader,” and recommended four reading paths.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| `weread-skills` *(external)* | Connect to WeRead and query bookshelf, notes, statistics, and recommendations |

---

## 💬 Example Prompts

```text
Show me an overview of my bookshelf.
```

```text
Check my notes, highlights, and review sources for Madame Bovary.
Assess my reading level and give me reading recommendations.
```

---

## 📸 Screenshots

![WeRead Skill setup page](../../assets/screenshots/weread-skill-1.jpg)

![Minis outputs bookshelf stats](../../assets/screenshots/weread-skill-2.jpg)

![Minis analyzes reading history and recommends books](../../assets/screenshots/weread-skill-3.jpg)

---

## ⚙️ Requirements

- [ ] Install the external official WeRead Skill from [weread.qq.com/r/weread-skills](https://weread.qq.com/r/weread-skills); it is not part of `OpenMinis/MinisSkills`
- [ ] Follow the external setup page to connect your WeRead account
- [ ] Review the external skill and its requested account permissions before installation

---

## 💡 Tips

- Ask natural-language questions like “Find books I have not finished recently” or “What genres do I read most?”
- Combine WeRead data with Minis analysis to generate a deep personal reading report.

---

## 👤 Contributor

From the Open Minis Telegram community

Original sharer: **𝐍𝐢𝐜𝐤𝐢𝐥𝐢𝐬𝐦**

---

## 📅 Last Verified

2026-05-16
