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
- `quality` runs the cheap Ruff flow through the active interpreter: `ruff check . --fix` and `ruff format .`.
- `quality --check-only` keeps the cheap flow non-mutating: `ruff check .` and `ruff format . --check`.
- `quality --full` extends the cheap flow with `pytest` and `pyright`.
- `quality --full --check-only` is the read-only full verification path before push or merge.
- `test` runs pytest through the active interpreter.
- `clean` removes caches and temporary artifacts, but stays conservative around `.venv`, `.git`, and inaccessible subtrees.
- `licenses` regenerates `THIRD_PARTY_LICENSES` from the active interpreter and excludes the local template package.

During template stage, `project_name` is still a placeholder package name. After bootstrap, the module path changes. The `bin/` wrappers are the stable user-facing entrypoints across that rename.

Treat everything outside `src/project_name/__init__.py` and the CLI subcommands as internal implementation detail.
