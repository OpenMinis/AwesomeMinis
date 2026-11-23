name: plugin-command-tester
version: 1.0.0
description: Dedicated skill for testing Obsidian Agentic Dashboard plugin commands using systematic verification pattern. Triggers when user wants to validate new plugin releases, test command URIs, or verify command results against mounted vault. Uses self-improving-agent framework for closed-loop testing, skill-creator methodology for skill development, and agentic-dashboard skill for actual command execution.
triggers: plugin test, command verification, obsidian command, verify command

---

# Plugin Command Tester Skill

## Overview

This skill provides a systematic workflow for testing Obsidian Agentic Dashboard plugin commands against a mounted vault. It is designed to work with three key skills:

1. **self-improving-agent** - For closed-loop feedback and learning from test results
2. **skill-creator** - For creating and updating skills based on test findings
3. **obsidian-agentic-dashboard** - For actual command execution via `obsidian://agentic-dashboard?op=...` URIs

## When to Use

- Testing new plugin releases from GitHub
- Verifying command URIs work correctly
- Validating command results against vault file changes
- Documenting iOS foregrounding limitations
- Creating data sheets for command inventories

## Test Workflow

### Step 1: Preparation

**Trigger the obsidian-agentic-dashboard skill** to ensure the plugin is loaded and vault is accessible:

```
obsidian://agentic-dashboard?op=open-dashboard
```

**Confirm plugin version** by checking `manifest.json` in the mounted vault:

```
Manifest version should match GitHub release tag
```

### Step 2: Command Inventory

**List all documented commands** from the plugin release notes or `main.js` source:

- Review all `op=` actions documented in the skill
- Note any new commands, deprecated commands, or changed parameters
- Cross-reference with GitHub release changelog

### Step 3: Systematic Testing

**For each command, follow this pattern:**

1. **Construct the URI** with required parameters:
   ```
   obsidian://agentic-dashboard?op=<command>&<param>=<value>&...
   ```
   - Percent-encode all values: space→`%20`, colon→`%3A`, newline→`%0A`, ampersand→`%26`
   - Use correct format: `HH:mm` for time, `YYYY-MM-DD` for dates

2. **Execute via apple-open** (or minis-open for in-app preview):
   ```
   apple-open obsidian://agentic-dashboard?op=...
   ```

3. **Check the `opened` field** result:
   - `opened: true` — URI was processed (but may be iOS limitation)
   - `opened: false` — Obsidian was foregrounded (iOS limitation, not plugin bug)

4. **Verify via vault files** (CRITICAL — do not rely on `opened` field alone):
   - Navigate to mounted vault: `/var/minis/mounts/Agents board/`
   - Check Inbox/ for capture notes
   - Check Journal/ for daily notes and tasks
   - Check Meetings/ for meeting notes
   - Read the resulting `.md` files to confirm changes

5. **Document the result**:
   - Exact URI used
   - `opened` field value
   - File location where change appeared
   - Note name (format: `YYYY-MM-DD HHMMSS - description.md`)
   - Any frontmatter changes observed

### Step 4: iOS Foregrounding Limitation

**Important:** When Obsidian is already open in foreground, `apple-open` returns `opened: false` even when the URI action succeeds. This is an iOS system limitation, not a plugin bug.

**Rule (single solution):** Background Obsidian via Minis first → all URIs execute immediately.

```
apple-open "minis://open_terminal"  →  backgrounds Obsidian
# Subsequent obsidian:// URIs work immediately (opened: true)
# No 2-minute wait needed
```

**Always verify by checking mounted vault files directly**, not relying on the `opened` field alone.

**Note:** If Minis was not opened beforehand, a ~2 minute wait may be required for Obsidian to auto-background.

### Step 5: Self-Improving-Agent Closed Loop

**After testing, use the self-improving-agent skill** to:

1. **Log what worked/didn't work**
2. **Identify any new constraints or parameters**
3. **Update this skill** with findings
4. **Create/update data sheets** for future reference

The self-improving-agent framework follows this pattern:
- Command fails → User corrects → Outdated knowledge identified → Better solution found → Historical learnings reviewed → Closed loop completed

### Step 6: Result Documentation

**Create a command data sheet** following this template:

| # | Command | obsidian:// URI (exact) | Result | File Location | Note Name |
|---|---------|-------------------------|--------|--------------|-----------|
| 1 | `capture` | `op=capture&text=...&type=thought` | Created inbox note | `Inbox/` | `2026-11-22 220946 - ...md` |
| ... | ... | ... | ... | ... | ... |

**Include format verification:**
- Daily note template consistency
- Capture frontmatter (all 6 types: thought, idea, reflection, to-watch, book, article)
- Task line format: `- [ ] <text> <emoji> <rule> ➕ <date> 📅 <date>`

### Step 7: Skill Updates

**Use the skill-creator skill** to:

1. **Create new test skills** for emerging plugin features
2. **Update existing skills** with new command documentation
3. **Add trigger words** for new command categories
4. **Refine test patterns** based on learned limitations

**Example trigger integration:**
- Add to `obsidian-agentic-dashboard` skill triggers: `plugin test`, `command verify`
- Update `plugin-command-tester` skill description with new findings
- Create bundled reference scripts in `scripts/` subdirectory if needed

## Command Testing Checklist

- [ ] Plugin version confirmed from `manifest.json`
- [ ] All documented commands listed
- [ ] URI constructed with correct parameter format
- [ ] Command executed via `apple-open` or `minis-open`
- [ ] `opened` field noted (understand iOS limitation)
- [ ] **Vault files checked directly** (critical step)
- [ ] Result documented with file location and note name
- [ ] iOS foregrounding limitation recorded if applicable
- [ ] Self-improving-agent learnings logged
- [ ] Skill-creator updates applied if needed

## Integration with Other Skills

### With obsidian-agentic-dashboard

This skill works **alongside** (not replacing) the agentic-dashboard skill:

```
# To test a command:
1. Use this skill's test pattern
2. Execute via: obsidian://agentic-dashboard?op=...
3. Verify results in mounted vault
4. Document findings

# The agentic-dashboard skill handles:
- URI generation and execution
- Plugin protocol handling
- Basic command triggering
```

### With self-improving-agent

**Closed-loop learning flow:**

```
Test command → Check vault files → Note successes/failures → 
self-improving-agent reviews → Identify patterns → 
Update this skill → Improve future tests → Remember for next release
```

### With skill-creator

**Skill evolution cycle:**

```
New plugin release → Test commands → Document results → 
skill-creator creates/updates skill → Add triggers → 
New skill version released → Test again → Closed loop
```

## Bundled Resources (Optional)

Create these optional subdirectories when approaching 500 lines:

- `scripts/` - Executable test scripts (Python shell scripts)
- `references/` - Loaded reference materials as needed
- `assets/` - Icons, templates, formatting assets

**Example test script** (create in `scripts/`):

```python
#!/usr/bin/env python3
"""Test Obsidian Agentic Dashboard command and verify vault changes."""

import subprocess
import json
import os

def test_command(command_uri, vault_path):
    """Execute command and check vault for changes."""
    # Execute URI via apple-open
    result = subprocess.run(
        ['apple-open', command_uri],
        capture_output=True, text=True
    )
    
    # Check vault files for changes
    # ... verification logic
    
    return result

if __name__ == "__main__":
    # Example usage
    test_command(
        "obsidian://agentic-dashboard?op=capture&text=Test&type=thought",
        "/var/minis/mounts/Agents board/"
    )
```

## Notes

- **Never write vault files directly** - all operations go through `obsidian://agentic-dashboard?op=...` URIs
- **Multiple tasks matching same text require `index=`** parameter (0-based)
- **Multi-line values use `%0A`** for separate agenda items, notes, decisions, actions
- **Time format**: `HH:mm` or `HHmm` for meeting time parameter
- **Date format**: `YYYY-MM-DD` for date parameters
- **`read-note` command** requires `path=` (not `query=`) to avoid ambiguous matches
- **Capture before update** - must create capture first, then update via `query=` matching

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-11-23 | Initial release with full test pattern documentation |