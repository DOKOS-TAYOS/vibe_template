# Troubleshooting

## Bootstrap Fails With Invalid Names

- distribution names should look like `my-project`
- package names should look like `my_project`
- versions should look like `0.1.0`

## `licenses` Command Fails

Make sure dev dependencies are installed in `.venv`:

```bash
python -m pip install -e .[dev]
```

## `quality` Fails on Pyright

- check that `.venv` exists
- confirm the package imports from `src`
- keep function typing explicit

## Cleanup Removed Too Much

The cleanup command should never touch `.venv`. If it does, stop using that version of the script and add a regression test before changing the cleanup rules.
