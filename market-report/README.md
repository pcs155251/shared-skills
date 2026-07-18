# market-report

[English](#english) | [繁體中文](#繁體中文)

## English

Turn a Taiwan 實價登錄 pre-sale pricelist export (xlsx) into a polished
PowerPoint deck: 坪數區間 × 建案 statistics, 總價帶 histogram, and per-project
消控表 (sales-control grids) as native editable pptx tables.

**No AI required** — this is a plain Python CLI. AI agents are an optional
enhancement (they refresh the one paragraph of qualitative commentary; see
below).

### Install

Only [uv](https://docs.astral.sh/uv/) is needed — it downloads Python and all
packages itself:

- Mac/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `winget install astral-sh.uv`

### Usage

```
uv run build_deck.py <pricelist.xlsx> <output.pptx> [建案名稱 ...]
```

- Trailing 建案名稱 choose which projects get a 消控表 slide; omit them to
  default to the top-3 by transaction count. Unknown names are warned and
  skipped.
- First run creates the environment automatically (locked by `uv.lock`);
  afterwards it starts instantly.
- Charts need a Traditional-Chinese font: Windows/WSL (JhengHei) and macOS
  (PingFang) work out of the box; on Linux install Noto
  (`sudo apt install fonts-noto-cjk`).

### Updating for a new dataset

Every number on the slides is computed from the xlsx at build time. The only
hand-written text is the `MANUAL` block at the top of `build_deck.py` — the
市場總結 paragraph and three short commentary lines. Rewrite those when the
market picture changes (by hand, or ask any AI); their `{placeholders}` keep
auto-filling from data either way.

The full operating procedure — input validation, dataset-specific rules, and
verification — lives in [`AGENTS.md`](AGENTS.md). It is written to be followed
by any AI coding agent (Claude Code, Codex, Cursor, …) or a human.

### Use as a Claude Code skill

Clone the parent repo anywhere under `~/.claude/skills/` (e.g.
`~/.claude/skills/shared-skills/`) and this folder becomes the `/market-report`
command; `SKILL.md` is the thin adapter that points Claude at `AGENTS.md`.

## 繁體中文

將台灣預售屋實價登錄清冊(xlsx)轉成精美的 PowerPoint 簡報:坪數區間 × 建案
統計表、總價帶直方圖,以及各建案的消控表(以可直接編輯的 pptx 原生表格呈現)。

**不需要 AI** — 這是一個純 Python 命令列工具。AI 是選配的加值功能
(用來改寫唯一一段質性評論文字,見下方說明)。

### 安裝

只需要 [uv](https://docs.astral.sh/uv/) — 它會自行下載 Python 與所有套件:

- Mac/Linux:`curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows:`winget install astral-sh.uv`

### 使用方式

```
uv run build_deck.py <實價登錄.xlsx> <輸出.pptx> [建案名稱 ...]
```

- 結尾的建案名稱指定哪些建案要做消控表;省略時預設取成交筆數前三名。
  不存在的名稱會顯示警告並略過。
- 第一次執行會自動建立環境(版本由 `uv.lock` 鎖定),之後即可秒開。
- 圖表需要繁體中文字型:Windows/WSL(微軟正黑體)與 macOS(蘋方)開箱即用;
  Linux 請安裝 Noto(`sudo apt install fonts-noto-cjk`)。

### 更換新資料集

簡報上所有數字都是建置時從 xlsx 即時計算的。唯一手寫的文字是
`build_deck.py` 開頭的 `MANUAL` 區塊 — 市場總結段落與三行短評。
市場情勢改變時再改寫即可(手動或請任何 AI 代筆);其中的 `{佔位符}`
無論如何都會自動代入最新數據。

完整作業流程 — 輸入檢核、資料集規則、驗證方式 — 收錄於
[`AGENTS.md`](AGENTS.md),任何 AI 程式助理(Claude Code、Codex、Cursor 等)
或人工皆可依其執行。

### 作為 Claude Code 技能使用

將上層 repo clone 到 `~/.claude/skills/` 底下任意路徑(例如
`~/.claude/skills/shared-skills/`),本資料夾就成為 `/market-report` 指令;
`SKILL.md` 是把 Claude 導向 `AGENTS.md` 的輕量轉接層。
