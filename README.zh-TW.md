# shared-skills

[English](README.md) | **繁體中文**

一組自成一體、不綁定特定廠商的自動化技能(skills)。每個技能資料夾有三種用法:

- **作為 Claude Code 技能** — 將本 repo clone 到 `~/.claude/skills/` 底下,
  每個技能就成為一個 `/名稱` 斜線指令。
- **搭配任何 AI 程式助理**(Codex、Cursor 等)— 讓 AI 依照各技能的
  `AGENTS.md` 操作,該檔案載有完整的作業流程。
- **作為純命令列工具** — 不需要 AI;每個技能都是一般的
  [uv](https://docs.astral.sh/uv/) Python 工具,用法見各自的 README。

## 安裝

```
git clone <本repo網址> ~/.claude/skills/shared-skills
```

唯一的前置需求是 uv(它會自行下載 Python 與所有套件):

- Mac/Linux:`curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows:`winget install astral-sh.uv` — 在 **PowerShell 或 CMD** 執行皆可(winget 為 Windows 10/11 內建)。若沒有 winget,改用 PowerShell:`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

**共用單一環境。** 所有技能共用 repo 根目錄 `pyproject.toml`/`uv.lock`
定義的環境 — 只需安裝一次,repo 內任何 `uv run` 首次執行時會自動建好環境。
未來新技能若新增相依套件,只要 `git pull`,下一次 `uv run` 就會自動依新的
lockfile 更新環境。

## 技能列表

| 技能 | 指令 | 功能 |
|------|------|------|
| [market-report](market-report/README.zh-TW.md) | `/market-report` | 將台灣預售屋實價登錄清冊(xlsx)轉成預售屋分析 PowerPoint 簡報:坪數區間統計、總價帶直方圖,以及可編輯的各建案消控表。 |

各技能的用法與細節請見其資料夾內的 README。
