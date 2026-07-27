# Edit Clash Config Without Touching YAML

> **By @wsvn53 · Feb 27, 2026** · [Original Tweet](https://x.com/wsvn53/status/2027254629344649333)

### Pain Point

Clash config files are hundreds of lines of YAML. Editing DNS settings means hunting for the right section, remembering the syntax, and risking a broken config from a single indentation error.

### What It Does

Drop the Clash config file into Minis, say what you want — Minis reads the config, replaces DNS with DoH/DoT encrypted DNS while preserving China routing rules, then gives you a change summary and the new file. Zero YAML editing required.

Full flow shown in screenshot (7 steps):
1. Share `.yaml` config to Minis
2. "Help me replace DNS with common encrypted DNS"
3. Read Clash config file
4. Copy config to workspace
5. Replace DNS config with encrypted DNS (DoH/DoT)
6. Write & execute DNS replacement script
7. Verify result ✅ 7/7, output `clash-meta-config.yaml`

### Example Prompt

```
Replace the DNS in this Clash config with common encrypted DNS (DoH/DoT), keep the China routing rules intact
```

---

## 📸 Screenshots

![Minis reads Clash config and replaces DNS in 7 automated steps](../../assets/screenshots/clash-config-edit.jpg)

📷 Shared by @wsvn53 · 2026-02-27

---

**Last Verified:** 2026-02-27
**Category:** Productivity & Automation
**Contributor:** [@wsvn53](https://x.com/wsvn53)
