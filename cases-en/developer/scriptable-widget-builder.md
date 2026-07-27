# Build a Scriptable Widget with AI — No Laptop Needed

> **By @XIN · Apr 14, 2026** · Shared in Open Minis Community

### Pain Point

You want a custom iOS home screen widget, but Scriptable is just a code editor — you still have to write JavaScript yourself, read API docs, handle dark mode, and tune layout sizes. The barrier is real.

### What It Does

Mount the Scriptable folder in Minis, let AI write the widget code, and drop it straight into the directory. Scriptable instantly detects the new script — no laptop, no copy-paste.

Full flow:

1. Mount the Scriptable directory in Minis (path: `/var/minis/mounts/scriptable`)
2. Describe what you want: dual-panel widget with calendar + reminders, all 3 sizes, auto dark mode
3. Minis reads the official Scriptable docs (`docs.scriptable.app`) to understand the API
4. Generates complete JavaScript, writes it directly into the mounted directory
5. Open Scriptable → widget appears immediately, add to home screen and it's live
6. Not happy with the colors? Say "make the calendar title iOS blue and reminders warm orange" — Minis edits the file, re-run to see the update

### Final Result

- Top row: Gregorian date + weekday + Chinese lunar date
- Left panel: upcoming calendar events with name and time
- Right panel: reminders list; overdue items shown in red
- Tap a panel to jump directly into Calendar or Reminders app
- Auto-adapts to small / medium / large widget sizes
- Follows system dark mode automatically

### Example Prompt

```
I want to build a Scriptable widget. Docs at https://docs.scriptable.app/,
file path is /var/minis/mounts/scriptable.

Requirements:
- Auto-adapts to iOS small / medium / large sizes
- Top row: date, weekday, and Chinese lunar calendar
- Left panel: upcoming calendar events (name + time)
- Right panel: reminders (overdue items in red)
- Show only events within the next 2 weeks
- Tapping opens the corresponding app
- Supports auto dark/light mode
```

### Requirements

- Share the Scriptable folder to Minis via iOS Files app (mounted at `/var/minis/mounts/scriptable`)
- Install [Scriptable](https://apps.apple.com/app/scriptable/id1405459188) (free)

---

## 📸 Screenshots

**Step 1 · Describe the requirements, Minis reads the documentation and generates code**

![User describes widget requirements, Minis reads Scriptable docs and starts generating code](../../assets/screenshots/scriptable-widget-builder-prompt.jpg)

**Step 2 · Oral color correction, Minis directly changes the file**

![User asks to tweak colors, Minis edits the JS file with iOS-native blue and warm orange](../../assets/screenshots/scriptable-widget-builder-iterate.jpg)

**Step 3 · Final result: Home screen widget**

![Scriptable widget showing date, calendar events and reminders on iPhone home screen](../../assets/screenshots/scriptable-widget-builder.jpg)

📷 Shared by @XIN · 2026-04-14

---

**Last Verified:** 2026-04-14
**Category:** Developer Tools / Productivity
**Contributor:** [@XIN](https://x.com/XIN)
