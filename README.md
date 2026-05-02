# Project Title Pending

Hybrid research-first Python template for computational research. It keeps a reusable Python core and a lightweight CLI, but makes the researcher workflow and the human-vs-AI verification boundary the visible center of the project.

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
6. Start by filling the verified research files in `research/`.

Bootstrap is a one-time step for a fresh copy of the template. After it finishes, treat the repository as the real project codebase and keep using the stable wrappers when you want the safest entrypoint.

This template repository itself is published under MIT. Bootstrap can keep that choice or replace it for the project you create from the template.

## Verified Research Area

These are the first files a researcher should read and edit:

- [Research question](research/question.md)
- [Research protocol](research/protocol.md)
- [Research claims](research/claims.md)

Only files under `research/` count as checked research decisions or conclusions.

- `research/question.md` is the validated problem statement and success criteria.
- `research/protocol.md` is the approved methodology and evaluation contract.
- `research/claims.md` is the claim and evidence register that the researcher must explicitly confirm.

Everything else in the repository is working material.

- `experiments/` holds reproducible runs, scripts, configs, and outputs.
- `notebooks/` is optional and exploratory, never the authoritative source for final claims.
- `src/`, `scripts/`, `tests/`, `examples/`, and `bin/` are the delegable implementation side of the project.

AI can draft code, analyses, plots, summaries, and scaffolding, but nothing outside `research/` should be treated as a checked conclusion until the researcher promotes it there.

## Why the Wrappers Stay Useful

Before bootstrap, the placeholder package is still called `project_name`. After bootstrap, the package name changes. The wrappers in `bin/` stay stable across that rename and prefer the local `.venv` interpreter when it exists.

If you want the raw module entrypoint, use `python -m project_name.cli ...` before bootstrap and the new package name after bootstrap.

## Project Scope

`PROJECT_SCOPE_PENDING`

## What This Template Includes

- verified research files that separate human-checked decisions from AI-delegable work
- `src` layout with a small public API and a CLI entrypoint
- TDD-oriented tests for API, bootstrap, cleanup, CLI, and examples
- stable wrappers for bootstrap, quality, and clean
- documentation for humans plus a short AI fast path
- CI for Windows and Ubuntu with Python 3.11 to 3.13, plus a fresh-copy bootstrap smoke run

## More Docs

- [Research question](research/question.md)
- [Research protocol](research/protocol.md)
- [Research claims](research/claims.md)
- [Documentation index](docs/README.md)
- [Quick start](docs/quick-start.md)
- [Developer guide](docs/guide.md)
- [Architecture](docs/architecture.md)
- [API overview](docs/api.md)
- [AI user guide](docs/docs_for_ai/guide_for_ai_users.md)
- [AI project instructions](docs/docs_for_ai/project_ai_instructions.md)
