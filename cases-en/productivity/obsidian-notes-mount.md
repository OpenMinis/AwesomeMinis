# Mount the Obsidian note library to Minis and turn it into a readable and writable AI knowledge workspace

> 💬 *Real-world workflow: mount an Obsidian vault into Minis, then ask Minis to summarize, clean up, research, and write structured notes directly back into the vault.*

---

## 🎯 Pain Point

Obsidian is very suitable for long-term accumulation of knowledge, but it is still troublesome to organize notes on the mobile terminal: fragmented notes need to be manually archived, webpage materials need to be manually copied and organized, and duplicate test notes need to be cleaned up by yourself. The content generated in AI chat often stays in the chat history and does not enter the real knowledge base.

Obsidian is great for long-term knowledge management, but organizing notes on mobile is still tedious: rough notes need cleanup, web research needs manual copying, test files need pruning, and AI-generated summaries often stay trapped in chat instead of becoming part of your real vault.

---

## 💡 What It Does

Mount Obsidian vault to `/var/minis/mounts/Notes/` through Minis’ external folder mounting capability. Afterwards, Minis can read, summarize, delete, rewrite and create new Markdown notes just like operating local files. Users only need to say in natural language:

- "See what my mount notes are"
- "Summarize the contents of my notes"
- "Delete those pointless notes from the test"
- "Help me research Hermes Agent, organize it into notes and save them"

Minis will directly scan the Obsidian directory, process the Markdown files, and write new notes back to the vault, which will be immediately visible in Obsidian.

Use Minis' external folder mounting to mount an Obsidian vault at `/var/minis/mounts/Notes/`. Minis can then read, summarize, delete, edit, and create Markdown notes just like local files. You can simply ask in natural language, and the result is written back to the vault where Obsidian can see it immediately.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in external folder mount | Mount the Obsidian vault into Minis |
| Built-in Linux shell + file tools | List, read, delete, edit, and create Markdown files |
| Built-in browser/search | Research topics and collect sources before writing notes |
| Built-in Markdown writing | Save structured notes directly into the vault |

---

## 📋 How to Use

1. **Prepare Obsidian vault** — Prepare an Obsidian note library in the local phone or cloud synchronization directory, such as `Notes/`.
2. **Mount directory in Minis** — Open the external folder mounting in Minis settings and mount the Obsidian vault into Minis.
3. **Confirm path** — Minis will see the mount directory under `/var/minis/mounts/`, for example `/var/minis/mounts/Notes/`.
4. **Let Minis scan notes** — Just ask: "See what my mounted notes are."
5. **Ask Minis to summarize or clean up** - For example: "Summarize the content of my notes" "Delete test notes".
6. **Ask Minis to write new notes** - For example: "Help me collect information about Hermes Agent, summarize it into notes and save it."
7. **Go back to Obsidian to view** — The new or modified `.md` file will appear in the Obsidian vault.

---

## 💬 Example Prompts

**List notes in vault:**

```text
See what my mounted notes are
```

**Summary of existing notes:**

```text
To summarize the content of my notes
```

**Clean up meaningless test notes:**

```text
Delete those pointless notes from the test.
```

**Research a topic and save it to Obsidian:**

```text
Help me collect the recently popular Hermes Agent, study some of its most important usage scenarios, and its biggest features. What are its biggest features compared to OpenClaw? Summarize it into notes and save it.
```

---

## 📤 Expected Output

- List note files in the current vault
- Read and summarize existing notes
- Delete test files that the user confirms do not want
- Capture web page data and organize it into structured Markdown
- Save the new note as `Hermes Agent Research Notes.md`
- Return clickable Minis file links in chat
- Return to Obsidian to see the same new note

Typical result:

```text
Completed and saved as note: Hermes Agent Research Notes.md
```

---

## 📸 Screenshots

First, mount the Obsidian vault as an external folder and enable write access:

![Minis external folder mount settings for an Obsidian vault](../../assets/screenshots/obsidian-notes-mount-settings.png)

Minis can read the mounted Obsidian vault and summarize existing notes:

![Minis summarizes notes from a mounted Obsidian vault](../../assets/screenshots/obsidian-notes-mount-summary.png)

Minis can research a topic from the web while keeping the final destination as the mounted vault:

![Minis researches Hermes Agent before writing to Obsidian](../../assets/screenshots/obsidian-notes-mount-research-steps.png)

After the research is complete, Minis saves the Markdown note directly into the vault:

![Minis saves the Hermes Agent research note](../../assets/screenshots/obsidian-notes-mount-saved-result.png)

The same Markdown note is immediately visible in Obsidian:

![The generated Hermes Agent note visible in Obsidian](../../assets/screenshots/obsidian-notes-mount-obsidian-view.png)

---

## ⚙️ Requirements

- [ ] Minis support external folder mounting
- [ ] Minis have been authorized to access the Obsidian vault in the system file picker
- [ ] Notes in Obsidian vault are saved as Markdown `.md` files
- [ ] If you want to study the topic online, Minis browser/network access is required

---

## 💡 Tips & Variations

- **Summary first and then clean up**: Let Minis overview the vault first and then decide which files can be deleted to avoid accidental deletion.
- **Create file name by theme**: You can ask Minis to use fixed naming rules, such as `YYYY-MM-DD theme.md`.
- **Suitable for data research**: Turn the process of "search → read → refine → save Markdown" directly into the Obsidian storage process.
- **Suitable for mobile knowledge management**: No need to copy and paste repeatedly on the mobile phone, Minis can be written directly to the vault.
- **Delete with caution**: You can ask Minis to list candidate files and wait for confirmation before deleting.

---

## 👤 Contributor

Submitted by: Open Minis community

---

## 📅 Last Verified

2026-05
