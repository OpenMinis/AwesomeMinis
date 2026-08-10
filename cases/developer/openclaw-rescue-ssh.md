# Rescue a Crashed OpenClaw via SSH

> **By @wsvn53 · Mar 6, 2026** · [Original Tweet](https://x.com/wsvn53/status/2029852301998051847)

### Pain Point

OpenClaw (a.k.a. "the lobster") crashes after every update — Tailscale drops, the service dies, SSH tunnels break. Used to require someone physically on-site or hours of waiting.

### What It Does

SSH into the server from your iPhone via Minis, automatically diagnose the OpenClaw service, and fix it — no laptop needed.

> "OpenClaw keeps dying after updates, just SSH in with Minis to fix it 🤣"

Full flow shown in screenshot:
1. Prompt: "Check the OpenClaw service on this server"
2. Minis auto-runs: check service status → write diagnostic script → execute
3. Output: `openclaw service: ✅ active running`, uptime 9h, 52/52 steps done

### Example Prompt

```
SSH into my server and check the OpenClaw service status. If it's down, restart it.
```

### Requirements

- SSH key or password (stored in Minis environment variables)
- Server IP / hostname

---

## 📸 Screenshots

![Minis SSH into server to rescue crashed OpenClaw service](../../assets/screenshots/openclaw-rescue-ssh.jpg)

📷 Shared by @wsvn53 · 2026-03-06

---

**Last Verified:** 2026-03-06
**Category:** Developer Tools
**Contributor:** [@wsvn53](https://x.com/wsvn53)
