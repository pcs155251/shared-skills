# shared-skills

**English** | [繁體中文](README.zh-TW.md)

A collection of self-contained, vendor-independent automation skills. Each
skill folder works three ways:

- **As a Claude Code skill** — clone this repo under `~/.claude/skills/` and
  every skill becomes a `/name` slash command.
- **With any AI coding agent** (Codex, Cursor, …) — point the agent at a
  skill's `AGENTS.md`, which holds the full operating procedure.
- **As a plain CLI** — no AI required; each skill is an ordinary
  [uv](https://docs.astral.sh/uv/)-run Python tool documented in its `README.md`.

## Install

```
git clone <this-repo-url> ~/.claude/skills/shared-skills
```

The only prerequisite is uv (it bootstraps Python and all packages itself):

- Mac/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `winget install astral-sh.uv` — run in **PowerShell or CMD**, either works (winget is built into Windows 10/11). If winget is unavailable, use PowerShell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

## Skills

| Skill | Command | What it does |
|-------|---------|--------------|
| [market-report](market-report/) | `/market-report` | Turn a Taiwan 實價登錄 pre-sale pricelist (xlsx) into a 預售屋分析 PowerPoint deck: 坪數區間 statistics, 總價帶 histogram, and editable per-project 消控表 grids. |

See each skill's own `README.md` for usage and details.
