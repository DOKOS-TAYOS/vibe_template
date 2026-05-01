# Guide for AI Developers

## Mission

Use this template to build software projects with a stable Python core, minimal public APIs, explicit typing, and low-friction maintenance.

## Required Workflow

1. Read `docs/docs_for_ai/status.md` before making changes.
2. Keep the library layer as the center of the system.
3. Add or update tests before changing behavior.
4. Update `CHANGELOG.md` for meaningful changes.
5. Update this AI documentation when architecture, workflows, or constraints change.
6. Before finishing a Python task, run:
   - `ruff check . --fix`
   - `ruff format .`
   - `pytest`
   - `pyright`

## Design Rules

- Prefer focused modules over large utility buckets.
- Keep public exports centralized in `src/project_name/__init__.py`.
- Use relative imports inside the package to keep bootstrap rename-safe.
- Avoid new runtime dependencies unless they buy clear long-term value.
- Treat `docs/api.md` and the example scripts as contract documentation.

## Safe Areas to Extend

- add new use-case services under `app`
- add domain models under `domain`
- add infrastructure adapters when external systems appear
- add demos under `examples`

## AI Handoff Checklist

- current status updated
- next step named clearly
- blockers captured
- tests added for new behavior
- docs synchronized with code
