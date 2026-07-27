# Push Minis Results to WeChat via openilink-hub

> 💬 *From the Open Minis community — shared by **meng nimen** on 2026-03-25*

---

## 🎯 Pain Point

Minis results are only viewable inside the app. There is no built-in way to proactively push them to everyday messaging tools.

---

## 💡 What It Does

Use the open-source `openilink-hub` middleware to push any Minis output — weather, news, health reports, and more — from an iPad to WeChat on your phone, enabling cross-device information delivery.

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in | Run the task and prepare the output |
| `openilink-hub` *(external middleware)* | Push results to WeChat; not part of `OpenMinis/MinisSkills` |

---

## 💬 Example Prompt

```text
After the task completes, push the result to my WeChat via openilink-hub.
```

---

## 📸 Screenshots

![Screenshot by meng nimen](../../assets/screenshots/wechat-push-via-openilink.jpg)

*📷 Shared by **meng nimen** · 2026-03-25 — WeChat ClawBot skill configuration page.*

---

## ⚙️ Requirements

- [ ] Deploy and review the external `openilink-hub` middleware; it is not part of `OpenMinis/MinisSkills`
- [ ] Configure the WeChat push token according to the middleware's current documentation
- [ ] Store the token as a Minis environment variable rather than embedding it in prompts or files

---

## 🏷 Tags

`wechat` `push` `automation` `cross-device`

---

## 👤 Contributor

From the Open Minis Telegram community

Original sharer: **meng nimen**

---

## 📅 Last Verified

2026-03-25
