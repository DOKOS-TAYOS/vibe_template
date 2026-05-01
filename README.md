# Project Title Pending

Stable Python template for software-oriented vibe coding projects. It starts as a reusable library with a lightweight CLI, strong defaults for quality checks, and a documentation split that helps both people and future AI contributors.

## Bootstrap First

This template is intentionally incomplete until the first bootstrap step fills in:

- author name
- initial version
- project scope
- license choice
- final distribution and package names

Run one of these commands after creating your `.venv` and installing the project:

```bash
python -m project_name.cli bootstrap
```

Windows shortcut:

```powershell
bin\bootstrap.cmd
```

Linux or macOS shortcut:

```bash
./bin/bootstrap.sh
```

## What This Template Includes

- `src` layout with a minimal public API and a CLI entrypoint
- TDD-oriented tests for API, bootstrap, cleanup, CLI, and examples
- Windows/Linux-friendly wrappers in `bin/`
- development commands for lint, format, tests, type checking, and license inventory
- documentation for people and dedicated documentation for AI collaborators
- CI for Windows and Ubuntu with Python 3.11 to 3.13

## Recommended Setup

1. Create and activate `.venv`.
2. Install in editable mode with dev tools: `python -m pip install -e .[dev]`
3. Run `python -m project_name.cli bootstrap`
4. Run `python -m project_name.cli quality`

## Project Scope

`PROJECT_SCOPE_PENDING`

## Repository Layout

- `src/project_name`: library code and CLI
- `tests`: unit, integration, and smoke coverage
- `examples`: runnable examples for humans and AI agents
- `docs`: documentation for people
- `docs/docs_for_ai`: operational docs for AI users and AI developers
- `bin`: command wrappers for Windows and POSIX shells
- `scripts`: focused helper scripts, including cleanup

## Documentation Map

- [Documentation index](docs/README.md)
- [Quick start](docs/quick-start.md)
- [Developer guide](docs/guide.md)
- [Architecture](docs/architecture.md)
- [API overview](docs/api.md)
- [AI docs index](docs/docs_for_ai/guide_for_ai_devs.md)
