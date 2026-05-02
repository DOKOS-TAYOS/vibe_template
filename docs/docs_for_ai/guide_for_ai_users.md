# Guide for AI Users

## Strong Workflow

1. Read `docs/docs_for_ai/status.md` to see whether bootstrap already happened.
2. Read `docs/docs_for_ai/project_ai_instructions.md` before changing code.
3. Read `docs/api.md` for the public API and CLI contract.
4. Read `examples/library_usage.py` and `examples/cli_usage.py` only if you need usage examples.
5. Use the wrappers in `bin/` while the template package name is still provisional.

## What Not to Assume

- internal modules are not public contracts
- the strong workflow allows skipping design, TDD, or full verification
- placeholder metadata means bootstrap has not finished
- `bootstrap` is not re-runnable once the project identity has been applied
- empty or outdated `THIRD_PARTY_LICENSES` means dependencies were not regenerated yet

## Useful Commands

- `bin\bootstrap.cmd` or `./bin/bootstrap.sh`
- `bin\quality.cmd` or `./bin/quality.sh` for the full verification gate
- `bin\clean.cmd --dry-run` or `./bin/clean.sh --dry-run`
