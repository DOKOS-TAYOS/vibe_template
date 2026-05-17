# Troubleshooting

## Bootstrap Fails With Invalid Names

- distribution names should look like `my-project`
- package names should look like `my_project`
- versions should look like `0.1.0`

## `bootstrap` Says The Template Was Already Bootstrapped

`bootstrap` is a one-time setup step for a fresh copy of the template.

- if you already configured this repository once, keep working in it without running bootstrap again
- if you want a new project, create a fresh copy from the template first

## `licenses` Command Fails

Make sure dev dependencies are installed in `.venv`:

```bash
python -m pip install -e .[dev]
```

The command only lists third-party packages from the active interpreter. If the output looks wrong, confirm you are running it from the intended `.venv`.

## `quality` Fails on Pyright

- check that `.venv` exists
- confirm the package imports from `src`
- keep function typing explicit

## `security` Fails With `CERTIFICATE_VERIFY_FAILED`

The security command contacts the Python vulnerability service over HTTPS. If it fails with `CERTIFICATE_VERIFY_FAILED`, the local Python environment cannot validate the network certificate chain.

- confirm the system date and time are correct
- update Python certificates or corporate proxy trust settings
- if your organization uses a custom CA bundle, set `REQUESTS_CA_BUNDLE` to that certificate file before running the command

Do not bypass certificate validation to make the audit pass. Fix the trust configuration instead.

## Cleanup Removed Too Much

The cleanup command should never touch `.venv`. If it does, stop using that version of the script and add a regression test before changing the cleanup rules.
