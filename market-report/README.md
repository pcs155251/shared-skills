# market-report

Turn a Taiwan 實價登錄 pre-sale pricelist export (xlsx) into a polished
PowerPoint deck: 坪數區間 × 建案 statistics, 總價帶 histogram, and per-project
消控表 (sales-control grids) as native editable pptx tables.

**No AI required** — this is a plain Python CLI. AI agents are an optional
enhancement (they refresh the one paragraph of qualitative commentary; see
below).

## Install

Only [uv](https://docs.astral.sh/uv/) is needed — it downloads Python and all
packages itself:

- Mac/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `winget install astral-sh.uv`

## Usage

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

## Updating for a new dataset

Every number on the slides is computed from the xlsx at build time. The only
hand-written text is the `MANUAL` block at the top of `build_deck.py` — the
市場總結 paragraph and three short commentary lines. Rewrite those when the
market picture changes (by hand, or ask any AI); their `{placeholders}` keep
auto-filling from data either way.

The full operating procedure — input validation, dataset-specific rules, and
verification — lives in [`AGENTS.md`](AGENTS.md). It is written to be followed
by any AI coding agent (Claude Code, Codex, Cursor, …) or a human.

## Use as a Claude Code skill

Clone this folder anywhere under `~/.claude/skills/` (e.g.
`~/.claude/skills/shared-skills/market-report/`) and it becomes the `/market-report`
command; `SKILL.md` is the thin adapter that points Claude at `AGENTS.md`.
