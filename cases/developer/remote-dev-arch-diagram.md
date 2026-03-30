# Remote Dev & Architecture Diagram Generation

> **By @wsvn53 · Feb 27, 2026** · [Original Tweet](https://x.com/wsvn53/status/2027253813992903062)

## 🇨🇳 中文

### 痛点

想了解一个陌生项目的架构，要么手动翻代码，要么写脚本，费时费力。

### 做了什么

SSH 连入远程服务器，让 Minis 自动扫描项目结构、读取 Swift 源文件，提炼三层架构模型，最后调用 Nano Banana（Gemini 图像生成 API）直接生成架构图。手机上一句话，2 分钟出图，全程零干预。

- SSH 连入远程服务器，自动扫描项目结构
- 逐一读取 Swift 源文件，提炼三层架构模型
- 调用 Nano Banana 2（Gemini API）直接生成架构图

### 示例 Prompt

```
SSH 连接到我的服务器，扫描 ~/MyApp 项目结构，读取主要 Swift 文件，帮我生成一张三层架构图
```

### 所需配置

- SSH 密钥（存入 Minis 环境变量）
- Gemini API Key（用于 Nano Banana 图像生成）

---

## 🇺🇸 English

### Pain Point

Understanding an unfamiliar codebase requires manual exploration or writing custom scripts — slow and tedious.

### What It Does

SSH into a remote server, auto-scan the project structure, read Swift source files one by one, extract a 3-layer architecture model, then call Nano Banana (Gemini image generation API) to produce an architecture diagram. One sentence on your phone, diagram in 2 minutes, zero intervention.

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
