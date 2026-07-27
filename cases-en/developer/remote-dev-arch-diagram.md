# Remote Dev & Architecture Diagram Generation

> **By @wsvn53 · Feb 27, 2026** · [Original Tweet](https://x.com/wsvn53/status/2027253813992903062)

### Pain Point

Understanding an unfamiliar codebase requires manual exploration or writing custom scripts — slow and tedious.

### What It Does

- SSH into remote server, auto-scan project structure
- Read Swift source files, extract 3-layer architecture model
- Call Nano Banana 2 (Gemini API) to generate architecture diagram

### Example Prompt

```
SSH into my server, scan the ~/MyApp project, read the main Swift files, and generate a 3-layer architecture diagram
```

### Requirements

- SSH key (stored in Minis environment variables)
- Gemini API Key (for Nano Banana image generation)

---

**Last Verified:** 2026-02-27
**Category:** Developer Tools
**Contributor:** [@wsvn53](https://x.com/wsvn53)
