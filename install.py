# -*- coding: utf-8 -*-
"""Install/update the skills in this repo into ~/.claude/skills/.

Claude Code only discovers skills that sit DIRECTLY under ~/.claude/skills/
(one folder deep, no symlinks), so this script copies every skill folder in
this repo — plus the shared pyproject.toml/uv.lock — to the right place.

Usage:  uv run install.py     (or: python3 install.py)
Update: git pull && uv run install.py
"""
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
DEST = Path.home() / ".claude" / "skills"
ENV_FILES = ["pyproject.toml", "uv.lock"]

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    skills = sorted(p.parent for p in REPO.glob("*/SKILL.md"))
    if not skills:
        sys.exit("No skill folders (containing SKILL.md) found in this repo.")

    for src in skills:
        dst = DEST / src.name
        if dst.resolve() == src.resolve():
            print(f"= {src.name}: already installed in place, skipped")
            continue
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".venv", "__pycache__"))
        print(f"✓ {src.name} → {dst}")

    for name in ENV_FILES:
        f = REPO / name
        if f.exists() and f.resolve() != (DEST / name).resolve():
            shutil.copy2(f, DEST / name)
            print(f"✓ {name} → {DEST / name}  (shared environment)")

    print("\n完成!請重新啟動 Claude Code / 桌面 App,新視窗即可使用 / 指令。")
    print("Done! Restart Claude Code / the desktop app; new sessions will "
          "show the / commands.")

if __name__ == "__main__":
    main()
