from __future__ import annotations

import sys
from pathlib import Path

from project_name.app.tooling_service import (
    build_bootstrap_resync_command,
    build_license_command,
    build_quality_commands,
    build_test_command,
)


def test_quality_commands_default_to_cheap_fixing_flow() -> None:
    commands = build_quality_commands()

    assert commands == [
        [sys.executable, "-m", "ruff", "check", ".", "--fix"],
        [sys.executable, "-m", "ruff", "format", "."],
    ]


def test_quality_commands_check_only_use_non_mutating_cheap_flow() -> None:
    commands = build_quality_commands(check_only=True)

    assert commands == [
        [sys.executable, "-m", "ruff", "check", "."],
        [sys.executable, "-m", "ruff", "format", ".", "--check"],
    ]


def test_quality_commands_full_mode_extends_cheap_flow_with_test_and_typecheck() -> None:
    commands = build_quality_commands(full=True)

    assert commands == [
        [sys.executable, "-m", "ruff", "check", ".", "--fix"],
        [sys.executable, "-m", "ruff", "format", "."],
        [sys.executable, "-m", "pytest"],
        [sys.executable, "-m", "pyright"],
    ]


def test_quality_commands_full_check_only_mode_is_non_mutating() -> None:
    commands = build_quality_commands(check_only=True, full=True)

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
