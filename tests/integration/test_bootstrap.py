from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from subprocess import CompletedProcess

import pytest

import project_name.cli as cli_module
from project_name.app.bootstrap_service import (
    BootstrapAnswers,
    BootstrapResult,
    PlannedChange,
    bootstrap_template,
)


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
        project_title="Sample Project",
        distribution_name="sample-project",
        package_name="sample_project",
        author_name="Ada Lovelace",
        initial_version="0.1.0",
        project_scope="Tooling library for reliable experiments.",
        license_id="MIT",
    )

    result = bootstrap_template(workspace_root=workspace, answers=answers, dry_run=False)

    assert result.changed is True
    assert (workspace / "src" / "sample_project").is_dir()
    assert not (workspace / "src" / "project_name").exists()

    pyproject_content = (workspace / "pyproject.toml").read_text(encoding="utf-8")
    readme_content = (workspace / "README.md").read_text(encoding="utf-8")
    status_content = (workspace / "docs" / "docs_for_ai" / "status.md").read_text(encoding="utf-8")
    template_metadata_path = (
        workspace / "src" / "sample_project" / "domain" / "template_metadata.py"
    )
    template_metadata_content = template_metadata_path.read_text(encoding="utf-8")

    assert "sample-project" in pyproject_content
    assert "Ada Lovelace" in pyproject_content
    assert "0.1.0" in pyproject_content
    assert "Tooling library for reliable experiments." in readme_content
    assert "License: MIT" in status_content
    assert "example.invalid" not in pyproject_content
    assert "Pending" not in readme_content
    assert "bootstrap_required=False" in template_metadata_content


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


def test_bootstrap_template_rejects_already_bootstrapped_workspace(temp_dir: Path) -> None:
    source_root = Path(__file__).resolve().parents[2]
    workspace = temp_dir / "workspace"
    _copy_template_workspace(source_root, workspace)
    answers = BootstrapAnswers(
        project_title="Stable Project",
        distribution_name="stable-project",
        package_name="stable_project",
        author_name="Margaret Hamilton",
        initial_version="0.4.0",
        project_scope="Reusable template hardening validation.",
        license_id="MIT",
    )

    bootstrap_template(workspace_root=workspace, answers=answers, dry_run=False)

    with pytest.raises(ValueError, match="already been bootstrapped"):
        bootstrap_template(workspace_root=workspace, answers=answers, dry_run=True)


def test_bootstrap_cli_reinstalls_for_the_new_package_name(
    temp_dir: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    workspace = temp_dir / "workspace"
    workspace.mkdir()
    (workspace / "pyproject.toml").write_text(
        """
[tool.vibe_template]
bootstrap_required = true
""".strip(),
        encoding="utf-8",
    )
    planned_change = PlannedChange(
        path=workspace / "src" / "bootstrap_cli_project",
        description="Rename package directory from project_name to bootstrap_cli_project",
    )

    def fake_bootstrap_template(
        workspace_root: Path,
        answers: BootstrapAnswers,
        dry_run: bool,
    ) -> BootstrapResult:
        del workspace_root, answers, dry_run
        return BootstrapResult(changed=True, changes=(planned_change,))

    def fake_run_process(command: list[str], root: Path) -> CompletedProcess[bytes]:
        del root
        return CompletedProcess(args=command, returncode=0)

    monkeypatch.chdir(workspace)
    monkeypatch.setattr(
        cli_module,
        "bootstrap_template",
        fake_bootstrap_template,
    )
    monkeypatch.setattr(
        cli_module,
        "run_process",
        fake_run_process,
    )

    def unexpected_prompt(label: str, default: str | None = None) -> str:
        pytest.fail(f"Unexpected prompt for {label} with {default}")

    monkeypatch.setattr(cli_module, "_prompt", unexpected_prompt)

    args = argparse.Namespace(
        project_title="Bootstrap CLI Project",
        distribution_name="bootstrap-cli-project",
        package_name=None,
        author_name="Katherine Johnson",
        initial_version="0.3.0",
        project_scope="End-to-end bootstrap verification for the template.",
        license_id="MIT",
        dry_run=False,
    )

    return_code = cli_module._handle_bootstrap(args)
    stdout = capsys.readouterr().out

    assert return_code == 0
    assert "bootstrap_cli_project" in stdout
    assert "pip install -e .[dev]" in stdout


def test_bootstrap_cli_fails_without_prompting_when_template_is_already_bootstrapped(
    temp_dir: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    workspace = temp_dir / "workspace"
    workspace.mkdir()
    (workspace / "pyproject.toml").write_text(
        """
[tool.vibe_template]
bootstrap_required = false
""".strip(),
        encoding="utf-8",
    )

    def unexpected_prompt(label: str, default: str | None = None) -> str:
        pytest.fail(f"Unexpected prompt for {label} with {default}")

    monkeypatch.chdir(workspace)
    monkeypatch.setattr(cli_module, "_prompt", unexpected_prompt)

    args = argparse.Namespace(
        project_title=None,
        distribution_name=None,
        package_name=None,
        author_name=None,
        initial_version=None,
        project_scope=None,
        license_id=None,
        dry_run=True,
    )

    return_code = cli_module._handle_bootstrap(args)
    stdout = capsys.readouterr().out

    assert return_code == 1
    assert "already been bootstrapped" in stdout
