# API Overview

## Public Python API

The template keeps the public Python API intentionally small.

```python
from project_name import TemplateMetadata, get_template_metadata
```

### `TemplateMetadata`

Immutable dataclass describing the current template metadata:

- `package_name`
- `distribution_name`
- `project_title`
- `bootstrap_required`
- `scope_summary`
- `cli_commands`

### `get_template_metadata()`

Returns the current `TemplateMetadata` snapshot.

## Public CLI

- `bootstrap`
- `quality`
- `test`
- `clean`
- `licenses`

### CLI behavior notes

- `bootstrap` is for a fresh template copy only. Once `bootstrap_required` becomes `False`, the command exits with an error instead of prompting again.
- `quality` runs Ruff, pytest, and pyright through the active interpreter, which keeps `.venv` resolution consistent on Windows and Linux.
- `test` runs pytest through the active interpreter.
- `clean` removes caches and temporary artifacts, including notebook checkpoints, but stays conservative around `.venv`, `.git`, and inaccessible subtrees.
- `licenses` regenerates `THIRD_PARTY_LICENSES` from the active interpreter and excludes the local template package.

During template stage, `project_name` is still a placeholder package name. After bootstrap, the module path changes. The `bin/` wrappers are the stable user-facing entrypoints across that rename.

## Research Workflow Contract

The main change in this branch is not API surface but repository contract:

- `research/question.md`, `research/protocol.md`, and `research/claims.md` are the human-verified research boundary.
- `experiments/`, `notebooks/`, `src/`, `scripts/`, `tests/`, and `examples/` are working areas that may contain drafts, scaffolding, or AI-generated material.
- Nothing outside `research/` should be treated as a checked research conclusion until the researcher promotes it there.

Treat everything outside `src/project_name/__init__.py`, the CLI subcommands, and the verified research files as internal implementation detail.
