# Guide for AI Users

## Fast Path

1. Read `docs/docs_for_ai/status.md`.
2. Read `docs/api.md`.
3. Search first, then open only the exact files you need.
4. Open `examples/library_usage.py` or `examples/cli_usage.py` only if usage is still unclear.
5. Use `bin\quality.cmd` or `./bin/quality.sh` for the cheap Ruff pass.
6. Use `bin\quality.cmd --full` or `./bin/quality.sh --full` only for the full verification gate.

## What Not to Assume

- internal modules are not public contracts
- placeholder metadata means bootstrap has not finished
- `bootstrap` is not re-runnable once the project identity has been applied
- `quality` is intentionally cheap by default
- full verification is explicit, not automatic

## Useful Commands

- `bin\bootstrap.cmd` or `./bin/bootstrap.sh`
- `bin\quality.cmd` or `./bin/quality.sh`
- `bin\quality.cmd --full` or `./bin/quality.sh --full`
- `bin\clean.cmd --dry-run` or `./bin/clean.sh --dry-run`
