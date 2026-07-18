# Repo-wide conventions (all skills)

These apply to every skill in this repo, on top of each skill's own `AGENTS.md`.

- **Language: 繁體中文.** Users of these skills are Traditional-Chinese
  speakers — conduct all user-facing interaction in 繁體中文: questions,
  progress updates, warnings you relay, and the final summary. Code, commit
  messages, and documentation files stay as written.
- **Environment:** one shared uv environment for the whole repo, defined by the
  root `pyproject.toml`/`uv.lock`. Run skills with `uv run` from inside the
  repo, or `uv run --project <repo-root>` from outside. A skill adding a
  dependency edits the root `pyproject.toml` and runs `uv lock`.
