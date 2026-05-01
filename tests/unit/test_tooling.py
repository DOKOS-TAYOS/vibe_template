from __future__ import annotations

import sys
from pathlib import Path

from project_name.app.tooling_service import build_license_command, build_quality_commands


def test_quality_commands_cover_lint_format_test_and_typecheck() -> None:
    commands = build_quality_commands(include_format_fix=True)

    assert commands == [
        ["ruff", "check", ".", "--fix"],
        ["ruff", "format", "."],
        ["pytest"],
        ["pyright"],
    ]


def test_license_command_generates_compact_inventory() -> None:
    command = build_license_command(Path("THIRD_PARTY_LICENSES"))

    assert command == [
        sys.executable,
        "-m",
        "piplicenses",
        "--python",
        sys.executable,
        "--format=markdown",
        "--with-urls",
        "--output-file",
        "THIRD_PARTY_LICENSES",
    ]
