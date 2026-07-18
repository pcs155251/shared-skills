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

前置需求一 — git(若 `git --version` 已可執行則跳過):

- Windows:`winget install Git.Git`(PowerShell 或 CMD 皆可),或到 [git-scm.com](https://git-scm.com/downloads) 下載安裝
- Mac:`xcode-select --install`(或 `brew install git`)
- Linux:`sudo apt install git`(Debian/Ubuntu)

接著 clone 本 repo(任何位置皆可,例如 `~/shared-skills`)— Mac/Linux/WSL:

```
git clone https://github.com/pcs155251/shared-skills.git ~/shared-skills
```

Windows PowerShell(請用 `$HOME`,不要用 `~` — PowerShell 會把 `~` 原樣傳給
git,產生一個名字就叫 `~` 的資料夾):

```
git clone https://github.com/pcs155251/shared-skills.git "$HOME\shared-skills"
```

前置需求二 — uv(它會自行下載 Python 與所有套件):

- Mac/Linux:`curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows:`winget install astral-sh.uv` — 在 **PowerShell 或 CMD** 執行皆可(winget 為 Windows 10/11 內建)。若沒有 winget,改用 PowerShell:`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

最後,在 clone 下來的資料夾內執行安裝程式:

```
cd ~/shared-skills        # Windows:cd "$HOME\shared-skills"
uv run install.py
```

它會把每個技能複製到 `~/.claude/skills/` — Claude Code 只會偵測**直接**放在
該資料夾下的技能(不支援子資料夾或符號連結),所以只 clone 是不夠的。
重新啟動 Claude Code / 桌面 App 後,新視窗就會出現 `/` 指令。

**更新**(新技能、新相依套件,一組指令搞定):

```
git pull && uv run install.py
```

**共用單一環境。** 所有技能共用 `pyproject.toml`/`uv.lock` 定義的環境
(會隨技能一起安裝)— 第一次 `uv run` 自動建好環境,更新後下一次
`uv run` 也會自動依新的 lockfile 重新同步。

## 技能列表

| 技能 | 指令 | 功能 |
|------|------|------|
| [market-report](market-report/README.zh-TW.md) | `/market-report` | 將台灣預售屋實價登錄清冊(xlsx)轉成預售屋分析 PowerPoint 簡報:坪數區間統計、總價帶直方圖,以及可編輯的各建案消控表。 |

各技能的用法與細節請見其資料夾內的 README。
