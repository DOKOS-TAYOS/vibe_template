# Developer Guide

## Core Principles

- Keep checked research decisions and conclusions in `research/` only.
- Use `experiments/` and `notebooks/` as working areas, not as verified truth.
- Prefer small, well-named modules with one responsibility.
- Treat the research workflow as the product center and the Python library as support.
- Keep the CLI as a thin entrypoint around stable maintenance commands.
- Keep imports relative inside the package so bootstrap renaming stays safe.
- Use tests to define behavior before implementation changes.
- Update human docs and AI docs when architecture or workflow changes.

## Suggested Workflow

1. Activate `.venv`.
2. Install with `python -m pip install -e .[dev]` if the environment is not ready yet.
3. Run bootstrap once for a fresh project and then treat the result as the real codebase.
4. Confirm the problem statement in `research/question.md`.
5. Confirm the methodology and evaluation rules in `research/protocol.md`.
6. Write or update a failing test before changing behavior in code.
7. Implement the minimal change.
8. Run the smallest relevant test command.
9. Refactor while staying green.
10. Before finishing, run the full quality flow.
11. Promote only researcher-checked conclusions to `research/claims.md`.

## Stable Entry Points

- `bin\bootstrap.cmd` or `./bin/bootstrap.sh`
- `bin\quality.cmd` or `./bin/quality.sh`
- `bin\clean.cmd` or `./bin/clean.sh`

Use direct `python -m <package>.cli ...` commands when you specifically want the module-level entrypoint after bootstrap.

## Documentation Responsibilities

- `research/question.md`: human-verified research question and success criteria
- `research/protocol.md`: human-verified methodology and evaluation rules
- `research/claims.md`: human-verified claims and supporting evidence register
- `README.md`: overview and first-run expectations
- `docs/quick-start.md`: exact commands for a fresh project
- `docs/api.md`: public API and CLI contract changes
- `docs/architecture.md`: layer or data-flow changes
- `docs/docs_for_ai/project_ai_instructions.md`: workflow, guardrails, and AI handoff rules
- `docs/docs_for_ai/status.md`: current phase, next step, blockers
