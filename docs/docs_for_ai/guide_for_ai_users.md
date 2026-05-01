# Guide for AI Users

## Purpose

This folder helps an AI consume the library or template without reading the full codebase first.

## Fast Path

1. Read `docs/api.md` for the public API.
2. Read `examples/library_usage.py` and `examples/cli_usage.py`.
3. Check `docs/docs_for_ai/status.md` to see the current project phase.
4. Use `python -m project_name.cli demo` to verify the environment quickly.

## What Not to Assume

- internal modules are not public contracts
- placeholder metadata means bootstrap has not finished
- empty or outdated `THIRD_PARTY_LICENSES` means dependencies were not regenerated yet

## Useful Commands

- `python -m project_name.cli demo`
- `python -m project_name.cli test`
- `python -m project_name.cli quality`
- `python -m project_name.cli clean --dry-run`
