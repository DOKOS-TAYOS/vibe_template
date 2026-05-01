# Developer Guide

## Core Principles

- Prefer small, well-named modules with one responsibility.
- Treat the library as the product core and the CLI as a thin entrypoint.
- Keep imports relative inside the package so bootstrap renaming stays safe.
- Use tests to define behavior before implementation changes.
- Update human docs and AI docs when architecture or workflow changes.

## Suggested Workflow

1. Activate `.venv`.
2. Write or update a failing test.
3. Implement the minimal change.
4. Run the smallest relevant test command.
5. Refactor while staying green.
6. Before finishing, run the full quality flow.

## Commands

- `python -m project_name.cli bootstrap`
- `python -m project_name.cli demo`
- `python -m project_name.cli test`
- `python -m project_name.cli quality`
- `python -m project_name.cli clean`
- `python -m project_name.cli licenses`

## When to Touch Which Docs

- `README.md`: project overview or onboarding changes
- `docs/api.md`: public API changes
- `docs/architecture.md`: layer or data-flow changes
- `docs/docs_for_ai/project_ai_instructions.md`: workflow or guardrail changes
- `docs/docs_for_ai/status.md`: current phase, next step, blockers
