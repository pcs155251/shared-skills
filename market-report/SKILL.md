---
name: market-report
description: Rebuild the 實價登錄 pricelist → 預售屋分析 pptx deck (坪數表格、總價帶直方圖、消控表).
disable-model-invocation: true
---

# Pricelist → slides

Follow **`AGENTS.md` in this skill's base directory** — it holds the entire
process: inputs (pricelist xlsx + which 建案 get a 消控表, top-3 fallback), the
deliverable spec, build/verify steps, and the dataset-specific rules. When it
says `<dir>`, substitute this skill's base directory. Ask the 消控表 question
with AskUserQuestion and deliver the finished pptx with SendUserFile.
