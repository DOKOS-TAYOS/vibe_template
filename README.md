# Project Title Pending

Cheap-first Python template for agent-assisted projects. It keeps a reusable library core and a lightweight CLI, but optimizes the default loop for low token spend, low command cost, and short handoffs.

## Official First Run

This template is intentionally incomplete until bootstrap fills in:

- author name
- initial version
- project scope
- license choice
- final distribution and package names

1. Create and activate `.venv`.
2. Install in editable mode with dev tools: `python -m pip install -e .[dev]`
3. Run `bin\bootstrap.cmd` on Windows or `./bin/bootstrap.sh` on Linux/macOS.
4. Let bootstrap finish its automatic editable reinstall.
5. Run `bin\quality.cmd` on Windows or `./bin/quality.sh` on Linux/macOS.
6. Run `bin\quality.cmd --full` on Windows or `./bin/quality.sh --full` on Linux/macOS when you want the full verification pass.

Bootstrap is a one-time step for a fresh copy of the template. After it finishes, treat the repository as the real project codebase and keep using the stable wrappers when you want the safest entrypoint.

This template repository itself is published under MIT. Bootstrap can keep that choice or replace it for the project you create from the template.

## Cheap-First Workflow

- `quality` runs only the cheap Ruff flow: `ruff check . --fix` and `ruff format .`
- `quality --check-only` runs the same cheap flow without rewriting files
- `quality --full` adds `pytest` and `pyright`
- `quality --full --check-only` is the read-only final gate before push or merge
- Start with targeted searches and the smallest relevant test instead of repo-wide sweeps

## Project Scope

`PROJECT_SCOPE_PENDING`

## What This Template Includes

- `src` layout with a small public API and a CLI entrypoint
- TDD-oriented tests for API, bootstrap, cleanup, CLI, and examples
- cheap-by-default quality commands with an explicit full verification mode
- stable wrappers for bootstrap, quality, and clean
- short human docs plus a low-token AI fast path
- CI on Windows and Ubuntu with Python 3.12, plus a Windows fresh-copy bootstrap smoke run
- Dependabot, dependency review, Python dependency auditing, and GitHub security-setting guidance under `.github`

## Security Defaults

The template ships GitHub security configuration as tracked files, so new projects created from it keep the same baseline:

- `.github/dependabot.yml` keeps Python tooling and GitHub Actions updated.
- `.github/workflows/security.yml` runs dependency review on pull requests and `pip-audit`.
- CodeQL is intentionally left to GitHub's default setup, because advanced CodeQL workflows conflict with repositories where default setup is already enabled.
- CI uses read-only `GITHUB_TOKEN` permissions and disables persisted checkout credentials.
- `SECURITY.md` explains which GitHub repository settings still need to be enabled for each derived project, including GitHub code scanning default setup and secret scanning.

## More Docs

- [Documentation index](docs/README.md)
- [Quick start](docs/quick-start.md)
- [Developer guide](docs/guide.md)
- [Architecture](docs/architecture.md)
- [API overview](docs/api.md)
- [AI user guide](docs/docs_for_ai/guide_for_ai_users.md)
- [AI project instructions](docs/docs_for_ai/project_ai_instructions.md)
