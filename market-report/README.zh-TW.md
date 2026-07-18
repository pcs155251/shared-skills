# market-report

[English](README.md) | **繁體中文**

將台灣預售屋實價登錄清冊(xlsx)轉成精美的 PowerPoint 簡報:坪數區間 × 建案
統計表、總價帶直方圖,以及各建案的消控表(以可直接編輯的 pptx 原生表格呈現)。

**不需要 AI** — 這是一個純 Python 命令列工具。AI 是選配的加值功能
(用來改寫唯一一段質性評論文字,見下方說明)。

## 安裝

只需要 [uv](https://docs.astral.sh/uv/) — 它會自行下載 Python 與所有套件:

- Mac/Linux:`curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows:`winget install astral-sh.uv` — 在 **PowerShell 或 CMD** 執行皆可(winget 為 Windows 10/11 內建)。若沒有 winget,改用 PowerShell:`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

## 使用方式

```
uv run build_deck.py <實價登錄.xlsx> <輸出.pptx> [建案名稱 ...]
```

- 結尾的建案名稱指定哪些建案要做消控表;省略時預設取成交筆數前三名。
  不存在的名稱會顯示警告並略過。
- 第一次執行會自動建立環境(版本由 `uv.lock` 鎖定),之後即可秒開。
- 圖表需要繁體中文字型:Windows/WSL(微軟正黑體)與 macOS(蘋方)開箱即用;
  Linux 請安裝 Noto(`sudo apt install fonts-noto-cjk`)。

## 更換新資料集

簡報上所有數字都是建置時從 xlsx 即時計算的。唯一手寫的文字是
`build_deck.py` 開頭的 `MANUAL` 區塊 — 市場總結段落與三行短評。
市場情勢改變時再改寫即可(手動或請任何 AI 代筆);其中的 `{佔位符}`
無論如何都會自動代入最新數據。

完整作業流程 — 輸入檢核、資料集規則、驗證方式 — 收錄於
[`AGENTS.md`](AGENTS.md),任何 AI 程式助理(Claude Code、Codex、Cursor 等)
或人工皆可依其執行。

## 作為 Claude Code 技能使用

將上層 repo clone 到 `~/.claude/skills/` 底下任意路徑(例如
`~/.claude/skills/shared-skills/`),本資料夾就成為 `/market-report` 指令;
`SKILL.md` 是把 Claude 導向 `AGENTS.md` 的輕量轉接層。
