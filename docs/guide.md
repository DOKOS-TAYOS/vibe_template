# Educator Guide

## Core Principles

- Treat `course/` as the main source of truth for the learning experience.
- Keep modules short, explicit, and easy to edit in plain Markdown.
- Prefer small, well-named modules with one responsibility when you add Python code.
- Keep imports relative inside the package so bootstrap renaming stays safe.
- Use tests to define behavior before implementation changes.
- Update human docs and AI docs when architecture or workflow changes.

## Suggested Workflow

1. Activate `.venv`.
2. Install with `python -m pip install -e .[dev]` if the environment is not ready yet.
3. Run bootstrap once for a fresh project and then treat the result as the real codebase.
4. Rewrite the overview and modules in `course/` before adding extra tooling.
5. Write or update a failing test for any behavior change in Python code.
6. Implement the minimal change.
7. Run the smallest relevant test command.
8. Refactor while staying green.
9. Before finishing, run the full quality flow.
10. When dependencies, workflows, or release-facing code change, run the security audit command too.

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
- `course/README.md`: learner path and educator-facing course overview
- `docs/quick-start.md`: exact commands for a fresh project
- `docs/api.md`: public API and CLI contract changes
- `docs/architecture.md`: layer or data-flow changes
- `docs/docs_for_ai/project_ai_instructions.md`: workflow, guardrails, and AI handoff rules
- `docs/docs_for_ai/status.md`: current phase, next step, blockers
