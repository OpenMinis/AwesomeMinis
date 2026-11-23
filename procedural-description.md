# 案例: Agent-Run Obsidian Vault (Minis + Agentic Dashboard)

## Add: Agent-Run Obsidian Vault (Minis + Agentic Dashboard)

**faizulahasun-cloud** · **Pull Request #11** · OpenMinis/AwesomeMinis

---

### 中文：

本例展示了如何在 iPhone 上使用 Minis 编写任务、日记备忘录和会议记录，然后通过 Agentic Dashboard 插件将这些文件渲染为实时仪表板。Minis 将 Obsidian vault（在 iOS 文件中可见）作为工作空间；代理编写任务、日常备忘录、会议笔记作为纯 Markdown。在 Obsidian 侧，免费社区插件 Agentic Dashboard（无依赖，无 Dataview，桌面 + 移动端）会实时渲染这些文件——任务、日历、统计、会议、最近项目、收件箱——随着 Minis 的写入而自动刷新。

**已在 iPhone 上个人日常使用，另配桌面端使用**  
**案例文件:** cases/productivity/obsidian-vault-agent-dashboard.md（遵循 CASE_TEMPLATE.md）  
**README.md:** 在产品自动化表中添加一行  
**每个 PR 仅一个用例**

#### 提交要求：

1. **截图素材** — 请添加 2–3 张截图展示实际运作情况，例如：Minis 中挂载的 vault、一个代理编写任务/收藏/会议的聊天记录，以及随之而来的 Agentic Dashboard 在 Obsidian 中的渲染效果。将截图放在 assets/screenshots/ 并按照其他案例的模式在案例文件中引用。

2. **双语格式** — 现有案例按中英文逐段交替排版（例如：**中文：** … / **English:** …）。请沿用此风格，参见 cases/productivity/obsidian-notes-mount.md 或 cases/finance/receipt-expense-logging.md 以获取参考。

3. **挂载路径** — 简要提及 Minis 在 /var/minis/mounts/<name>/ 下看到挂载的 vault，这样读者就知道文件最终存放在哪里。

**额外说明（来自用户分享的 PDF，2026-11-23）：**  
- iPhone 上的 Obsidian 备注 normally 存于 files app -> On my iPhone -> obsidian folder -> 您的 vaults 创建在地域上
- 前往 minis app -> settings -> mount external folders/cloud folders -> 选择您的 vault 以便通过 minis agent 操作
- 挂载后：**建议关闭写入选项** 以确保：
  1. 无意外文件删除  
  2. 防止无格式或错误文件目录的写入
  3. 此插件命令确保仅正确格式的触发将在正确目录写入文件
- 无需将文件夹挂载到 minis agent 即可进行写入
- 仅用于阅读备注或确认确切已写入 file vault folder 是否已挂载到 minis agent
- 虽然写入文件完全可行，通过 op=apple-open 读取的备注仅显示格式，不揭示备注内容
- 与其创建额外快捷方式获取内容，将 vault 作为只读文件夹挂载更为容易。即使修改也需要精确命令
- 其他细节由技能和示例命令描述，agent 将自行查明
- 建议先使用 test vault 以获取概念

提交这些内容后，我们将 merge 它。

---

### English:

This use case demonstrates how to use Minis on iPhone to write tasks, daily notes, and meeting notes, which are then rendered as a live dashboard by the Agentic Dashboard plugin. Minis mounts an Obsidian vault (visible in the iOS Files app) as a workspace; the agent writes tasks, daily captures, and meeting notes as plain Markdown. On the Obsidian side, the free community plugin Agentic Dashboard (no dependencies, no Dataview, desktop + mobile) renders those files as a live dashboard — tasks, calendar, stats, meetings, recents, inbox — refreshing automatically as Minis writes.

**Personally tested and in daily use on iPhone (vault mounted in Minis) plus desktop**  
**Case file:** cases/productivity/obsidian-vault-agent-dashboard.md (follows CASE_TEMPLATE.md)  
**README.md:** one row added to the Productivity & Automation table  
**One use case per PR**

#### Submission requirements:

1. **Screenshots** — Please add 2–3 screenshots showing it actually working, e.g. the vault mounted in Minis, a chat where Minis writes a task/capture/meeting note, and the resulting Agentic Dashboard in Obsidian. Put them in assets/screenshots/ and reference them in the case file (see other cases for the pattern).

2. **Bilingual format** — Existing cases alternate Chinese and English paragraph by paragraph (e.g. **Chinese:** … / **English:** …). Please follow that style, see cases/productivity/obsidian-notes-mount.md or cases/finance/receipt-expense-logging.md for reference.

3. **Mount path** — Briefly mention that Minis sees the mounted vault under /var/minis/mounts/<name>/, so readers know where the files end up.

**Additional information (from user-shared PDF, 2026-11-23):**
- iPhone Obsidian notes are normally created at: files app -> On my iPhone -> obsidian folder -> your vaults created locally
- Go to minis app -> settings -> mount external folders/cloud folders -> choose your vault for operating via minis agent
- After mount: **Recommended to toggle off write option** to ensure:
  1. No accidental file deletion
  2. Prevent writing without format or wrong file directory
  3. This plugin commands ensure only correct format trigger will write the file on right directory
- Writing works without mounting the folder on minis agent
- Only For reading notes or making sure exactly what written on file vault folder is mounted on minis agent
- Though write file work exactly, read file via op=apple-open only shows format of the note. Don't reveal content of the note.
- Rather than creating extra shortcut to get the content, it's easier to mount vault as read only folder. Even modifications also need exact command.
- Rest are described with skills and example commands which agent will find out itself.
- Recommended to use a test vault first to get the idea.

Once those are in, we'll merge it.

---

### 📋 Minis Agent Testing Workflow (First-Time Integration)

**由 Minis Agent 使用测试技能验证命令（首次整合）**

**由 Agentic Dashboard 技能更新相应命令**

---

### 中文：

#### Minis Agent 测试技能验证流程

Minis Agent 将使用 **plugin-command-tester** 技能系统测试 Agentic Dashboard v1.9.3 插件的命令，以下是验证步骤：

**Step 1: 技能触发**  
Minis Agent 通过 `plugin test` 或 `command verify` 触发 `plugin-command-tester` 技能。

**Step 2: 插件版本确认**  
检查挂载在 Obsidian 中的插件清单：
- **测试 vault 路径:** `/var/minis/mounts/Plugin testing vault/`
- **参考 vault 路径:** `/var/minis/mounts/Agents board/`
- **manifest.json 版本:** 1.9.3

**Step 3: URI 构造与执行**  
例如测试 `capture` 命令（思维型）：
```
obsidian://agentic-dashboard?op=capture&text=Test%20thought%20v1.9.3&type=thought
```
**关键规则（新规则）：**  
在执行 URI 之前，必须先打开 Minis App 以 background Obsidian：
```
apple-open "minis://open_terminal"
# 然后 URIs 将立即执行 (opened: true)
# 无需等待 2 分钟
```

**Step 4: 验证 vault 文件变更（必不可少）**  
勿仅依赖 `opened` 字段。检查 vault .md 文件的实际变更：
- **收件箱笔记:** `/var/minis/mounts/Plugin testing vault/Inbox/`
- **日志/任务:** `/var/minis/mounts/Plugin testing vault/Journal/`
- **会议笔记:** `/var/minis/mounts/Plugin testing vault/Meetings/`

**Step 5: 数据记录**  
记录结果：精确 URI、`opened` 字段、文件位置、笔记名称。

**Step 6: 技能更新**  
将发现记入 `obsidian-agentic-dashboard` 技能（见下文）。

---

### English:

#### Minis Agent Testing Workflow

Minis Agent will use the **plugin-command-tester** skill to systematically test Agentic Dashboard v1.9.3 plugin commands. Here are the verification steps:

**Step 1: Skill Trigger**  
Minis Agent triggers `plugin-command-tester` via `plugin test` or `command verify`.

**Step 2: Plugin Version Confirmation**  
Check the plugin manifest mounted in Obsidian:
- **Testing vault path:** `/var/minis/mounts/Plugin testing vault/`
- **Reference vault path:** `/var/minis/mounts/Agents board/`
- **manifest.json version:** 1.9.3

**Step 3: URI Construction & Execution**  
Example testing the `capture` command (thought type):
```
obsidian://agentic-dashboard?op=capture&text=Test%20thought%20v1.9.3&type=thought
```
**Critical Rule (new rule):**  
Before executing the URI, Minis App must be opened first to background Obsidian:
```
apple-open "minis://open_terminal"
# Then URIs execute immediately (opened: true)
# No 2-minute wait needed
```

**Step 4: Verify Vault File Changes (CRITICAL)**  
Do NOT rely on the `opened` field alone. Check actual `.md` file changes in vault:
- **Inbox notes:** `/var/minis/mounts/Plugin testing vault/Inbox/`
- **Journal/Tasks:** `/var/minis/mounts/Plugin testing vault/Journal/`
- **Meeting notes:** `/var/minis/mounts/Plugin testing vault/Meetings/`

**Step 5: Result Documentation**  
Record results: exact URI, `opened` field, file location, note name.

**Step 6: Skill Update**  
Update `obsidian-agentic-dashboard` skill (see below).

---

### 📝 Agentic Dashboard Skill Update (Post-Testing)

**测试完成后更新 obsidian-agentic-dashboard 技能**

---

### 中文：

#### 更新 obsidian-agentic-dashboard 技能

Minis Agent 将根据测试结果更新 `obsidian-agentic-dashboard` 技能，主要修改如下：

**iOS 前景ighting 限制的单一规则:**  
原有描述："When Obsidian is already open in the foreground, `apple-open` may return `opened: false` even when the URI action succeeds. All commands execute successfully after ~60-120 second waits or after closing Obsidian between calls."

**现已更新为:**  
**Rule (single solution):** Background Obsidian via Minis first → all commands execute successfully immediately.

```
apple-open "minis://open_terminal"  →  backgrounds Obsidian
# All obsidian://agentic-dashboard?op=... URIs work immediately (opened: true)
# No 60-120 second wait needed
```

**Note:** If Minis was not opened beforehand, the `opened: false` behavior may occur until Obsidian backgrounds itself.

**其他约束保持不变:**  
- ✅ 从不直接写入 vault 文件 - 必须通过 `obsidian://agentic-dashboard?op=...` URIs 进行所有操作  
- ✅ 多个与同一文本匹配的任务需要 `index=` 参数（0-based）以消除歧义  
- ✅ 多行值使用 `%0A` 分隔 agenda items, notes, decisions, actions  
- ✅ 时间格式: `HH:mm` 或 `HHmm` 用于 meeting time 参数  
- ✅ 日期格式: `YYYY-MM-DD` 用于 date 参数  
- ✅ `read-note` command 需要 `path=` (而非 `query=`) 以避免模糊匹配  
- ✅ 创建捕获前，必须先创建 capture，然后通过 `query=` 匹配进行更新  

**已验证命令 (v1.9.3):**  
- ✅ capture (6 types: thought, idea, reflection, to-watch, book, article)  
- ✅ add-task, toggle-task, update-task  
- ✅ find-note, open-dashboard  
- ⚠️ meeting / update-meeting - 需要进一步测试  
- ⚠️ new-daily - 需要进一步测试  

**Memory saved:** 测试摘要保存到当前每日日志: `2026-11-23.md`

---

### English:

#### Update obsidian-agentic-dashboard Skill

Minis Agent will update the `obsidian-agentic-dashboard` skill based on testing results, with the following changes:

**iOS Foregrounding Limitation - Single Rule:**  
Original description: "When Obsidian is already open in the foreground, `apple-open` may return `opened: false` even when the URI action succeeds. All commands execute successfully after ~60-120 second waits or after closing Obsidian between calls."

**Updated to:**  
**Rule (single solution):** Background Obsidian via Minis first → all commands execute successfully immediately.

```
apple-open "minis://open_terminal"  →  backgrounds Obsidian
# All obsidian://agentic-dashboard?op=... URIs work immediately (opened: true)
# No 60-120 second wait needed
```

**Note:** If Minis was not opened beforehand, the `opened: false` behavior may occur until Obsidian backgrounds itself.

**Other constraints remain unchanged:**  
- ✅ Never directly write vault files - all operations must go through `obsidian://agentic-dashboard?op=...` URIs  
- ✅ Multiple tasks matching same text require `index=` parameter (0-based) to disambiguate  
- ✅ Multi-line values use `%0A` for separate agenda items, notes, decisions, actions  
- ✅ Time format: `HH:mm` or `HHmm` for meeting time parameter  
- ✅ Date format: `YYYY-MM-DD` for date parameters  
- ✅ `read-note` command requires `path=` (not `query=`) to avoid ambiguous matches  
- ✅ Capture before update - must create capture first, then update via `query=` matching  

**Verified Commands (v1.9.3):**  
- ✅ capture (6 types: thought, idea, reflection, to-watch, book, article)  
- ✅ add-task, toggle-task, update-task  
- ✅ find-note, open-dashboard  
- ⚠️ meeting / update-meeting - needs further testing  
- ⚠️ new-daily - needs further testing  

**Memory saved:** Testing summary saved to today's daily log: `2026-11-23.md`

---

### 📸 Procedure Proof Screenshots (User to Capture)

**用户拍摄的程序证明截图**

---

### 中文：

#### 程序证明截像需求

用户将拍摄以下步骤的截图，作为案例的程序证明：

1. **Minis 挂载 vault 截图**  
   - 展示在 iOS Files 中看到的 Minis vault 挂载
   - 路径: `/var/minis/mounts/Plugin testing vault/`
   - 或 `/var/minis/mounts/Agents board/`

2. **插件清单确认**  
   - 打开 Obsidian → 设置 → 插件
   - 确认 Agentic Dashboard v1.9.3
   - 查看 manifest.json 版本

3. **Minis App 背景化 Obsidian**  
   - 操作: `apple-open "minis://open_terminal"`
   - 截图显示 Minis 已打开，Obsidian 进入后台

4. **命令执行截图**  
   - 示例: `apple-open "obsidian://agentic-dashboard?op=capture&text=Test&type=thought"`
   - 截图显示 `opened: true` 返回

5. **Vault .md 文件变更**  
   - 打开对应文件夹查看 .md 文件新增
   - 例如: `/var/minis/mounts/Plugin testing vault/Inbox/` 新增 thought 类型笔记

6. **完整数据表**  
   - 包含所有测试命令的验证结果
   - 包含 file location 和 note name

7. **Vault 挂载设置截图**  
   - Minis app -> settings -> mount external folders
   - 展示 write option 关闭状态

用户将这些截图与技能文件一起打包压缩。

---

### English:

#### Screenshot Proof Procedure

User will capture screenshots of the following steps as procedural proof for the case:

1. **Minis Vault Mount Screenshot**  
   - Show the Minis vault mounted visible in iOS Files
   - Path: `/var/minis/mounts/Plugin testing vault/`
   - Or `/var/minis/mounts/Agents board/`

2. **Plugin Manifest Confirmation**  
   - Open Obsidian → Settings → Plugins
   - Confirm Agentic Dashboard v1.9.3
   - Check manifest.json version

3. **Minis App Backgrounds Obsidian**  
   - Action: `apple-open "minis://open_terminal"`
   - Screenshot shows Minis opened, Obsidian goes to background

4. **Command Execution Screenshot**  
   - Example: `apple-open "obsidian://agentic-dashboard?op=capture&text=Test&type=thought"`
   - Screenshot shows `opened: true` return

5. **Vault .md File Changes**  
   - Open corresponding folder to view newly added .md files
   - Example: New thought-type note in `/var/minis/mounts/Plugin testing vault/Inbox/`

6. **Complete Data Table**  
   - Contains verification results of all tested commands
   - Includes file location and note name

7. **Vault Mounting Settings Screenshot**  
   - Minis app -> settings -> mount external folders
   - Showing write option turned off

User will pack these screenshots with the skill files.

---

### 📦 打包说明 (Packaging Instructions)

**用户将打包以下内容：**

1. **测试技能** (`plugin-command-tester/SKILL.md`) - 已更新的测试规则
2. **仪表板技能** (`obsidian-agentic-dashboard/SKILL.md`) - 已更新的单一规则
3. **程序证明截图** (7 张以上) - Minis vault mounting, plugin manifest, command execution, vault .md changes, mounting settings
4. **案例描述** (本草案) - 中英双语格式
5. **目录结构** - 组织好所有文件

**打包格式:**  
将上述所有文件压缩为 `obsidian-vault-agent-dashboard-case.zip`

**不包含:**  
- 等待脚本相关内容（旧案例，已弃用）
- 任何 2 分钟等待指示
- 与 vault mounting 无关的旧规则

---

### 📁 目录结构 (Directory Structure)

**最终打包的目录应包含:**

```
obsidian-vault-agent-dashboard-case.zip
├── cases/productivity/obsidian-vault-agent-dashboard.md
├── README.md (with row in Productivity & Automation table)
├── assets/screenshots/
│   ├── minis-vault-mounted.png
│   ├── plugin-manifest-confirmed.png
│   ├── minis-backgrounds-obsidian.png
│   ├── command-execution-opened-true.png
│   ├── vault-md-changes-thought.png
│   ├── vault-md-changes-task.png
│   └── vault-mounting-settings.png
├── skills/
│   ├── plugin-command-tester/SKILL.md (updated)
│   └── obsidian-agentic-dashboard/SKILL.md (updated)
└── procedural-description.md (this draft)
```

---

### ✅ 完成标志

**完成标准:**

1. ✅ 中英双语格式符合 cases/productivity/obsidian-notes-mount.md 模式
2. ✅ exact vault paths mentioned: `/var/minis/mounts/Plugin testing vault/`, `/var/minis/mounts/Agents board/`, `/var/minis/mounts/<name>/`
3. ✅ Minis agent testing skill (`plugin-command-tester`) integrated and updated with single rule
4. ✅ Agentic Dashboard skill (`obsidian-agentic-dashboard`) updated with single rule
5. ✅ Procedure proof screenshots captured by user (7+ screenshots including vault mounting settings)
6. ✅ No waiting script mentions (old case, deprecated)
7. ✅ Vault mounting procedures from user PDF incorporated (toggle off write option, etc.)
8. ✅ Reference to PR #11: https://github.com/OpenMinis/AwesomeMinis/pull/11
9. ✅ Testing skill shipped as new integration skill

**准备提交:** 将所有内容打包为 zip 文件并提交至 PR #11。