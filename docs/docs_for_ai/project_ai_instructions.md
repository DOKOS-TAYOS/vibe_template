# Project AI Instructions

## Non-Negotiable Rules

- Always include typing in function definitions.
- Keep the public API as small as possible.
- Use TDD for behavior changes.
- Update `CHANGELOG.md` when adding, fixing, or changing something meaningful.
- Do not remove `.venv` or clean it as part of project cleanup.
- Prefer Windows-safe commands, but keep Linux support where practical.

## Completion Checklist

Before claiming a Python task is complete:

1. Run `ruff check . --fix`
2. Run `ruff format .`
3. Run `pytest`
4. Run `pyright`
5. Update `docs/docs_for_ai/status.md`
6. Update `CHANGELOG.md`

## Architecture Expectations

- library core first
- thin CLI or adapters on top
- explicit layering
- no unnecessary public exports

## Bootstrap Expectations

When the project is still in template state, bootstrap must happen before publishing or long-term development.
