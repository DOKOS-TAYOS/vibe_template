# Changelog

All notable changes to this template are documented in this file.

## Unreleased

### Added

- Python software template with `src` layout, CLI entrypoint, and bootstrap flow.
- Cleanup, quality, test, and license commands with Windows/Linux wrappers.
- Human documentation, AI documentation, examples, and CI defaults.
- TDD-oriented tests for bootstrap, cleanup, CLI, public API, and examples.
- A reusable `scripts/bootstrap_smoke.py` helper that creates a fresh template copy, bootstraps it non-interactively, and runs the full quality flow.
- Dependabot configuration for Python tooling and GitHub Actions so derived projects keep receiving update pull requests.
- A Security workflow with dependency review and `pip-audit` checks, with CodeQL left to GitHub default setup to avoid advanced-setup conflicts.
- A `security` CLI command for local Python dependency vulnerability audits.

### Fixed

- Bootstrap now removes the template-only test harness self-test from derived projects, avoiding a fragile post-bootstrap test that depended on local temporary directory behavior.
- Security CI no longer uses an advanced CodeQL workflow, so repositories with GitHub CodeQL default setup enabled can process code scanning normally.
- The local `security` command now audits a generated dependency freeze that excludes the local project package, avoiding false CI failures for unpublished template packages.
- Bootstrap now wraps long `scope_summary` metadata into stable multiline Python literals and leaves `THIRD_PARTY_LICENSES` out of identity rewrites, so fresh bootstraps stay Ruff-clean and license inventories only change through the dedicated regeneration flow.
- `THIRD_PARTY_LICENSES` generation now stays compact and uses the active project interpreter instead of expanding full license texts or scanning unrelated global packages.
- Bootstrap now re-syncs the editable install after renaming the package, so the new project state is immediately usable.
- Bootstrap now refuses to run again once the template has already been configured, including dry-run calls.
- Bootstrap no longer rewrites unrelated `MIT` text while changing the project license, which keeps `THIRD_PARTY_LICENSES` stable for a public MIT template.
- Bootstrap no longer rewrites its own internal `bootstrap_required` replacement rules after the first project bootstrap, which keeps fresh-copy smoke validation working on already-bootstrapped copies.
- The license inventory now excludes the local template package and no longer ships `example.invalid` placeholder URLs.
- The wrapper launcher now reads the current package name from `pyproject.toml`, so `bin/bootstrap`, `bin/quality`, and `bin/clean` still work after the template package is renamed.
- Non-interactive bootstrap now derives `package_name` from `distribution_name` automatically, and the exported template metadata flips `bootstrap_required` to `False` after bootstrap.
- `clean` now avoids deleting temporary parent directories when that would also wipe a nested `.venv`.
- `clean` now walks directories conservatively, skips inaccessible subtrees, and no longer relies on fragile recursive globbing.
- Automated tests no longer depend on repo-local `test-artifacts`, which avoids the Windows permission issues seen in temporary workspaces.
- Bootstrap-facing tests and example assertions now stay valid after a fresh-copy smoke bootstrap, instead of assuming the repo is always still in template state.

### Changed

- The template footprint is leaner by default: removed `CITATION.cff`, removed `docs/features.md`, and reduced `bin/` wrappers to bootstrap, quality, and clean.
- The recommended first-run flow now uses stable wrappers in `bin/`, which keep working across the bootstrap package rename and prefer the local `.venv`.
- The public CLI now focuses on `bootstrap`, `quality`, `test`, `clean`, and `licenses`; the old `demo` command was removed in favor of real examples built on safe commands.
- AI documentation was compacted to three files, and the human docs were tightened to reduce overlap between the README, quick start, and guide.
- The redundant `scripts/clean.py` helper was removed, and `hatchling` no longer ships as a direct dev dependency in the template environment.
- `quality` and `test` now invoke tools through `sys.executable -m ...`, which keeps interpreter selection consistent across Windows and Linux.
- Pytest returned to its default cache naming while Ruff cleanup rules were updated for the standard `.pytest_cache` directory.
- CI now includes a dedicated fresh-copy template smoke job on Windows and Ubuntu, using Python 3.12 to validate the real bootstrap-plus-quality flow end to end.
- The template repository now ships with a real MIT license and `Alejandro Mata Ali` as the template author, while still leaving bootstrap in charge of project-specific identity.
- CI workflows now use minimal read-only token permissions, non-persisted checkout credentials, and current official GitHub Actions major versions.
