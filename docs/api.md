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
- `demo`

Treat everything outside `src/project_name/__init__.py` and the CLI subcommands as internal implementation detail.
