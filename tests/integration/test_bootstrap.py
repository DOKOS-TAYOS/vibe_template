from __future__ import annotations

import shutil
from pathlib import Path

from project_name.app.bootstrap_service import BootstrapAnswers, bootstrap_template


def _copy_template_workspace(source_root: Path, workspace: Path) -> None:
    shutil.copytree(
        source_root,
        workspace,
        ignore=shutil.ignore_patterns(
            ".git",
            ".venv",
            "__pycache__",
            ".tmp",
            "pytest-cache",
            "pytest-temp",
            "test-artifacts",
            "pytest-cache-files-*",
        ),
    )


def test_bootstrap_template_updates_metadata_and_package_name(temp_dir: Path) -> None:
    source_root = Path(__file__).resolve().parents[2]
    workspace = temp_dir / "workspace"
    _copy_template_workspace(source_root, workspace)

    answers = BootstrapAnswers(
        project_title="Demo Project",
        distribution_name="demo-project",
        package_name="demo_project",
        author_name="Ada Lovelace",
        initial_version="0.1.0",
        project_scope="Tooling library for reliable experiments.",
        license_id="MIT",
    )

    result = bootstrap_template(workspace_root=workspace, answers=answers, dry_run=False)

    assert result.changed is True
    assert (workspace / "src" / "demo_project").is_dir()
    assert not (workspace / "src" / "project_name").exists()

    pyproject_content = (workspace / "pyproject.toml").read_text(encoding="utf-8")
    readme_content = (workspace / "README.md").read_text(encoding="utf-8")
    status_content = (workspace / "docs" / "docs_for_ai" / "status.md").read_text(encoding="utf-8")

    assert "demo-project" in pyproject_content
    assert "Ada Lovelace" in pyproject_content
    assert "0.1.0" in pyproject_content
    assert "Tooling library for reliable experiments." in readme_content
    assert "License: MIT" in status_content


def test_bootstrap_template_dry_run_leaves_files_unchanged(temp_dir: Path) -> None:
    source_root = Path(__file__).resolve().parents[2]
    workspace = temp_dir / "workspace"
    _copy_template_workspace(source_root, workspace)

    answers = BootstrapAnswers(
        project_title="Dry Run Project",
        distribution_name="dry-run-project",
        package_name="dry_run_project",
        author_name="Grace Hopper",
        initial_version="0.2.0",
        project_scope="Dry run validation for template bootstrap.",
        license_id="Apache-2.0",
    )

    original_pyproject = (workspace / "pyproject.toml").read_text(encoding="utf-8")

    result = bootstrap_template(workspace_root=workspace, answers=answers, dry_run=True)

    assert result.changed is False
    assert (workspace / "src" / "project_name").exists()
    assert (workspace / "pyproject.toml").read_text(encoding="utf-8") == original_pyproject
    assert any("pyproject.toml" in change.path.as_posix() for change in result.changes)
