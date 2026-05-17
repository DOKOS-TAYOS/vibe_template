from __future__ import annotations

import sys
from pathlib import Path
from subprocess import CompletedProcess

import pytest

import project_name.app.tooling_service as tooling_service
from project_name.app.tooling_service import (
    SECURITY_REQUIREMENTS_PATH,
    build_bootstrap_resync_command,
    build_license_command,
    build_quality_commands,
    build_security_audit_command,
    build_security_commands,
    build_security_freeze_command,
    build_test_command,
    run_security_audit,
)


def test_quality_commands_cover_lint_format_test_and_typecheck() -> None:
    commands = build_quality_commands(include_format_fix=True)

    assert commands == [
        [sys.executable, "-m", "ruff", "check", ".", "--fix"],
        [sys.executable, "-m", "ruff", "format", "."],
        [sys.executable, "-m", "pytest"],
        [sys.executable, "-m", "pyright"],
    ]


def test_quality_check_only_still_runs_full_verification() -> None:
    commands = build_quality_commands(include_format_fix=False)

    assert commands == [
        [sys.executable, "-m", "ruff", "check", "."],
        [sys.executable, "-m", "ruff", "format", ".", "--check"],
        [sys.executable, "-m", "pytest"],
        [sys.executable, "-m", "pyright"],
    ]


def test_license_command_generates_compact_inventory() -> None:
    command = build_license_command(
        output_file=Path("THIRD_PARTY_LICENSES"),
        distribution_name="project-name",
    )

    assert command == [
        sys.executable,
        "-m",
        "piplicenses",
        "--python",
        sys.executable,
        "--format=markdown",
        "--with-urls",
        "--ignore-packages",
        "project-name",
        "--output-file",
        "THIRD_PARTY_LICENSES",
    ]


def test_security_commands_run_dependency_audit() -> None:
    commands = build_security_commands(distribution_name="project-name")

    assert commands == [
        [
            sys.executable,
            "-m",
            "pip",
            "list",
            "--format=freeze",
            "--exclude-editable",
            "--exclude",
            "project-name",
        ],
        [
            sys.executable,
            "-m",
            "pip_audit",
            "--requirement",
            str(SECURITY_REQUIREMENTS_PATH),
            "--strict",
            "--no-deps",
            "--disable-pip",
            "--cache-dir",
            str(Path(".tmp") / "pip-audit-cache"),
            "--progress-spinner",
            "off",
            "--timeout",
            "30",
        ],
    ]


def test_security_freeze_command_excludes_local_distribution() -> None:
    command = build_security_freeze_command(distribution_name="sample-project")

    assert command == [
        sys.executable,
        "-m",
        "pip",
        "list",
        "--format=freeze",
        "--exclude-editable",
        "--exclude",
        "sample-project",
    ]


def test_security_audit_command_uses_generated_requirements_without_dependency_resolution() -> None:
    command = build_security_audit_command(
        requirements_file=Path(".tmp") / "audit-input.txt",
        cache_dir=Path(".tmp") / "audit-cache",
    )

    assert command == [
        sys.executable,
        "-m",
        "pip_audit",
        "--requirement",
        str(Path(".tmp") / "audit-input.txt"),
        "--strict",
        "--no-deps",
        "--disable-pip",
        "--cache-dir",
        str(Path(".tmp") / "audit-cache"),
        "--progress-spinner",
        "off",
        "--timeout",
        "30",
    ]


def test_run_security_audit_excludes_local_distribution_from_generated_requirements(
    temp_dir: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pyproject_path = temp_dir / "pyproject.toml"
    pyproject_path.write_text('[project]\nname = "local-project"\n', encoding="utf-8")
    freeze_output = "pip-audit==2.10.0\nruff==0.15.12\n"
    captured_audit_commands: list[list[str]] = []

    def fake_subprocess_run(
        command: list[str],
        check: bool,
        cwd: Path,
        capture_output: bool,
        text: bool,
    ) -> CompletedProcess[str]:
        assert command == build_security_freeze_command(distribution_name="local-project")
        assert check is False
        assert cwd == temp_dir
        assert capture_output is True
        assert text is True
        return CompletedProcess(args=command, returncode=0, stdout=freeze_output)

    def fake_run_process(command: list[str], root: Path) -> CompletedProcess[bytes]:
        requirements_path = temp_dir / SECURITY_REQUIREMENTS_PATH
        assert root == temp_dir
        assert requirements_path.read_text(encoding="utf-8") == freeze_output
        assert "local-project" not in requirements_path.read_text(encoding="utf-8")
        captured_audit_commands.append(command)
        return CompletedProcess(args=command, returncode=0)

    monkeypatch.setattr(tooling_service.subprocess, "run", fake_subprocess_run)
    monkeypatch.setattr(tooling_service, "run_process", fake_run_process)

    results = run_security_audit(root=temp_dir)

    assert [result.returncode for result in results] == [0, 0]
    assert captured_audit_commands == [
        build_security_audit_command(
            requirements_file=SECURITY_REQUIREMENTS_PATH,
            cache_dir=Path(".tmp") / "pip-audit-cache",
        )
    ]


def test_test_command_uses_active_interpreter() -> None:
    command = build_test_command()

    assert command == [sys.executable, "-m", "pytest"]


def test_bootstrap_resync_command_uses_active_interpreter() -> None:
    command = build_bootstrap_resync_command()

    assert command == [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-e",
        ".[dev]",
    ]
