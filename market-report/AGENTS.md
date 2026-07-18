# Pricelist → slides — process guide

Turn a 實價登錄 pricelist export (xlsx) into the 預售屋分析 pptx deck. This file is
the single source of truth for the *process* and works with any AI agent or a
human operator; `build_deck.py` beside it is the single source of truth for all
layout, colors, and slide content — edit it there, never in a one-off script.
No other input files are needed.

**Inputs:** (1) the pricelist xlsx path, from the user; (2) the 建案名稱 that get
a 消控表 — ask the user which projects they want, check each answer exists in
the xlsx's 建案名稱 column, and when a name is absent or the user gives no
answer, default to the **top-3 projects by transaction count** (the script
applies the same fallback on its own). Output pptx defaults to the current
directory.

## Deliverable (the slides)

1. **封面** — 區域/期間/筆數/資料來源 (all parsed from the xlsx).
2. **坪數區間 × 建案 成交統計** — pptx table, rows = 案名, columns = 坪數 bins,
   each project's hottest bin bolded.
3. **總結** — exactly four findings backed by computed numbers:
   哪個建案賣最好(成交最多), 哪個坪數帶賣最多, 哪個坪數帶最難賣, and a
   房地產專家觀點 titled 市場總結.
4. **市場總價帶直方圖** — count on each bar with its 占比 directly beneath, and
   **two** bold headline takeaways above the chart.
5. **消控表** — one slide per requested project (default: top-3 sellers), each a
   **native editable pptx table** (never an image): columns = 戶別/房型, rows =
   樓層; each disclosed deal's cell shows 總價 / 單價 / 成交日期; below the table a
   colored-text legend stating the count of every cell color.

## Steps

1. **Validate the input xlsx.** Real header is on row 2 (`header=1`); strip `\n`
   from column names. Done when these columns are all present: `建案名稱`, `棟及號`,
   `交易日期`, `總價(萬元)`, `單價(萬元/坪)`, `車位總價(萬元)`, `樓別/樓高`, `建物格局`,
   `解約情形` — and numeric columns parse after removing thousands-commas.
2. **Refresh the manual prose.** All factual numbers are computed at build time;
   the only judgment text is the `MANUAL` block at the top of `build_deck.py`
   (市場總結 paragraph, the second histogram headline, two commentary tails).
   Rewrite it for the new dataset — with any AI or by hand; its `{placeholders}`
   stay auto-filled. Skipping this step still yields a numerically correct deck,
   just with possibly outdated interpretation.
3. **Build:** `uv run --project "<dir>" "<dir>/build_deck.py" "<xlsx>" "<out.pptx>" [建案名稱 ...]`
   where `<dir>` is the directory containing this file — trailing args are the
   消控表 projects (omit for the top-3 default; the script warns and skips names
   not in the data). `--project` makes uv use the bundled pyproject.toml/uv.lock
   regardless of the current directory. Done when it prints `saved` and the pptx
   opens cleanly.
4. **Eyeball the output.** Check the histogram for label collisions; verify each
   消控表 legend's counts sum to that grid's filled cells; read the script's
   warnings for unparseable 棟及號 rows.
5. **Deliver** the pptx file to the user.

## Dataset-specific rules (re-derive on new data)

- 權狀坪數 = (總價 − 車位總價) ÷ 單價.
- 坪數 bins: 20坪以下 / 20-30 / 30-40 / 40-50 / 50-70 / 70坪以上; table shows top-10
  projects + 其他 + 合計.
- Histogram bins by city: 台北市 starts <3,000萬 stepping +1,000萬 (tail merged at
  15,000以上); elsewhere starts <1,000萬 stepping +500萬 (add this branch to the
  script when data leaves Taipei).
- 消控表 covers the user-requested projects (fallback: top-3 by count).
  `parse_unit_floor()` handles the known `棟及號` shapes (`A6-14F號`, `15F-A3號`,
  `A棟A5-12F號`, `A3棟3F號`); a new dataset may bring a new shape — the script
  warns and skips unparseable rows, so check its warnings and extend the parser
  when one appears.
- Duplicate project names are the same case spelled differently (e.g. 宏普建設台灣
  川普[建設]瑞閣) — merge before ranking (`案名` replace map in the script).
- 解約 rows stay in every count; the 消控表 marks them red, latest-month deals
  green, other deals blue, undisclosed units gray. A unit sold again after 解約
  shows its newest non-解約 deal.
- 實價登錄 has no 表價/底價 — unsold cells stay blank unless the user supplies list
  prices or asks for floor-trend estimates labeled 推估.
