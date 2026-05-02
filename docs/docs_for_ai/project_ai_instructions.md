# Project AI Instructions

## Mission

Use this template to ship typed Python changes with the smallest reasonable token spend and command cost.

## Required Workflow

1. Read `docs/docs_for_ai/status.md` first.
2. Read `docs/api.md` before changing public behavior.
3. Use targeted search before opening whole files.
4. Add or update a test before changing behavior.
5. Use `quality` while iterating and `quality --full` only when the change is risky, user-facing, or about to be pushed or merged.
6. Update `CHANGELOG.md` and `docs/docs_for_ai/status.md` when the template meaningfully changes.

## Non-Negotiable Rules

- Always include typing in function definitions.
- Keep the public API as small as possible.
- Prefer short answers and short diffs over long tours.
- Read only the files needed for the current task.
- Prefer `rg` or similarly targeted searches over broad file reads.
- Do not run full test suites unless the change or completion gate justifies it.
- Prefer Windows-safe commands, but keep Linux support where practical.
- Prefer the stable wrappers in `bin/` while the template package name is still provisional.
- Treat `bootstrap` as a one-time setup command. If it already ran, do not try to re-run it.
- Do not remove `.venv` or clean it as part of project cleanup.
- Treat `docs/api.md` and the example scripts as contract documentation.

## Completion Checklist

Before claiming a Python task is complete:

1. Run `ruff check . --fix`
2. Run `ruff format .`
3. Run the smallest relevant test command for the change
4. Run `pytest` and `pyright` only when the change is risky, contract-level, or about to be pushed or merged
5. Update `docs/docs_for_ai/status.md`
6. Update `CHANGELOG.md`

## AI Handoff Checklist

- current status updated
- next step named clearly
- blockers captured
- tests updated for new behavior
- docs synchronized with code
