# Developer Guide

## Core Principles

- Prefer small, well-named modules with one responsibility.
- Treat the library as the product core and the CLI as a thin entrypoint.
- Keep imports relative inside the package so bootstrap renaming stays safe.
- Design non-trivial changes before implementation, especially when AI agents are doing the work.
- Use tests to define behavior before implementation changes.
- Treat the full quality gate as mandatory before claiming work is complete.
- Update human docs and AI docs when architecture or workflow changes.

## Suggested Workflow

1. Activate `.venv`.
2. Install with `python -m pip install -e .[dev]` if the environment is not ready yet.
3. Run bootstrap once for a fresh project and then treat the result as the real codebase.
4. Review `docs/docs_for_ai/status.md`, `docs/api.md`, and any directly affected files.
5. Sketch the approach before implementing non-trivial changes.
6. Write or update a failing test.
7. Implement the minimal change.
8. Run the smallest relevant test command.
9. Refactor while staying green.
10. Before finishing, run the full quality flow.
11. When dependencies, workflows, or release-facing code change, run the security audit command too.
12. Update `CHANGELOG.md` and `docs/docs_for_ai/status.md` when the change is meaningful.

## Stable Entry Points

- `bin\bootstrap.cmd` or `./bin/bootstrap.sh`
- `bin\quality.cmd` or `./bin/quality.sh`
- `bin\clean.cmd` or `./bin/clean.sh`

Use direct `python -m <package>.cli ...` commands when you specifically want the module-level entrypoint after bootstrap.

## Security Maintenance

- Keep `.github/dependabot.yml` in derived projects so Python tooling and GitHub Actions continue receiving update pull requests.
- Keep `.github/workflows/security.yml` unless the project has a stronger organization-level security workflow.
- Run `python scripts\run_template_command.py security` on Windows or `python scripts/run_template_command.py security` on Linux/macOS after dependency changes.
- Keep GitHub repository settings for Dependabot alerts, Dependabot security updates, dependency graph, code scanning, secret scanning, and push protection enabled when available.
- Use GitHub's CodeQL default setup for code scanning. Do not add an advanced CodeQL workflow unless default setup is disabled first.

## Documentation Responsibilities

- `README.md`: overview and first-run expectations
- `docs/quick-start.md`: exact commands for a fresh project
- `docs/api.md`: public API and CLI contract changes
- `docs/architecture.md`: layer or data-flow changes
- `docs/docs_for_ai/project_ai_instructions.md`: workflow, guardrails, and AI handoff rules
- `docs/docs_for_ai/status.md`: current phase, next step, blockers
