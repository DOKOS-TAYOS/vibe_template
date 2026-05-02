# Project AI Instructions

## Mission

Use this template to build simple technical courses with a clear learner path, Markdown-first authoring, and a stable Python support layer for bootstrap and maintenance.

## Required Workflow

1. Read `docs/docs_for_ai/status.md` before making changes.
2. Bootstrap a fresh template copy before long-term development.
3. Treat `course/` as the default source of truth for course content.
4. Keep the Python layer small and supportive unless the task clearly needs more.
5. Add or update tests before changing behavior.
6. Update `CHANGELOG.md` for meaningful changes.
7. Update these AI docs when workflow, architecture, or constraints change.

## Non-Negotiable Rules

- Always include typing in function definitions.
- Keep the public API as small as possible.
- Keep the learner path easy to follow and the educator editing surface easy to modify.
- Use TDD for behavior changes.
- Update `CHANGELOG.md` when adding, fixing, or changing something meaningful.
- Do not remove `.venv` or clean it as part of project cleanup.
- Prefer Windows-safe commands, but keep Linux support where practical.
- Prefer the stable wrappers in `bin/` while the template package name is still provisional.
- Treat `bootstrap` as a one-time setup command. If it already ran, do not try to re-run it.
- Treat `docs/api.md` and the example scripts as contract documentation.
- Use AI as backstage support. Do not make the course depend on prompt-heavy flows when plain Markdown is enough.

## Completion Checklist

Before claiming a Python task is complete:

1. Run `ruff check . --fix`
2. Run `ruff format .`
3. Run `pytest`
4. Run `pyright`
5. Update `docs/docs_for_ai/status.md`
6. Update `CHANGELOG.md`

## AI Handoff Checklist

- current status updated
- next step named clearly
- blockers captured
- tests added for new behavior
- docs synchronized with code
