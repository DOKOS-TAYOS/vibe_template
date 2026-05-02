# Guide for AI Users

## Fast Path

1. Read `docs/docs_for_ai/status.md` to see whether bootstrap already happened.
2. Read `research/question.md` and `research/protocol.md` before changing research-facing workflows.
3. Treat `research/claims.md` as the checked claims boundary.
4. Read `docs/api.md` only if you need the public API or CLI contract.
5. Read `examples/library_usage.py` and `examples/cli_usage.py` only if you need usage examples.
6. Read `docs/docs_for_ai/project_ai_instructions.md` before changing code.
7. Use the wrappers in `bin/` while the template package name is still provisional.

## What Not to Assume

- anything outside `research/` is not a verified research conclusion unless the researcher promoted it there
- notebooks are not the final source of truth
- internal modules are not public contracts
- placeholder metadata means bootstrap has not finished
- `bootstrap` is not re-runnable once the project identity has been applied
- empty or outdated `THIRD_PARTY_LICENSES` means dependencies were not regenerated yet

## Useful Commands

- `bin\bootstrap.cmd` or `./bin/bootstrap.sh`
- `bin\quality.cmd` or `./bin/quality.sh`
- `bin\clean.cmd --dry-run` or `./bin/clean.sh --dry-run`
