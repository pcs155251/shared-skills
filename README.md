# shared-skills

[English](#english) | [繁體中文](#繁體中文)

## English

A collection of self-contained, vendor-independent automation skills. Each
skill folder works three ways:

- **As a Claude Code skill** — clone this repo under `~/.claude/skills/` and
  every skill becomes a `/name` slash command.
- **With any AI coding agent** (Codex, Cursor, …) — point the agent at a
  skill's `AGENTS.md`, which holds the full operating procedure.
- **As a plain CLI** — no AI required; each skill is an ordinary
  [uv](https://docs.astral.sh/uv/)-run Python tool documented in its `README.md`.

### Install

```
git clone <this-repo-url> ~/.claude/skills/shared-skills
```

The only prerequisite is uv (it bootstraps Python and all packages itself):

- Mac/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `winget install astral-sh.uv`

### Skills

| Skill | Command | What it does |
|-------|---------|--------------|
| [market-report](market-report/) | `/market-report` | Turn a Taiwan 實價登錄 pre-sale pricelist (xlsx) into a 預售屋分析 PowerPoint deck: 坪數區間 statistics, 總價帶 histogram, and editable per-project 消控表 grids. |

See each skill's own `README.md` for usage and details.

## 繁體中文

一組自成一體、不綁定特定廠商的自動化技能(skills)。每個技能資料夾有三種用法:

- **作為 Claude Code 技能** — 將本 repo clone 到 `~/.claude/skills/` 底下,
  每個技能就成為一個 `/名稱` 斜線指令。
- **搭配任何 AI 程式助理**(Codex、Cursor 等)— 讓 AI 依照各技能的
  `AGENTS.md` 操作,該檔案載有完整的作業流程。
- **作為純命令列工具** — 不需要 AI;每個技能都是一般的
  [uv](https://docs.astral.sh/uv/) Python 工具,用法見各自的 `README.md`。

### 安裝

```
git clone <本repo網址> ~/.claude/skills/shared-skills
```

唯一的前置需求是 uv(它會自行下載 Python 與所有套件):

- Mac/Linux:`curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows:`winget install astral-sh.uv`

### 技能列表

| 技能 | 指令 | 功能 |
|------|------|------|
| [market-report](market-report/) | `/market-report` | 將台灣預售屋實價登錄清冊(xlsx)轉成預售屋分析 PowerPoint 簡報:坪數區間統計、總價帶直方圖,以及可編輯的各建案消控表。 |

各技能的用法與細節請見其資料夾內的 `README.md`。
