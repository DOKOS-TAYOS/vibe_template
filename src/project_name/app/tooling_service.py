from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from ..infrastructure.process_runner import run_process


@dataclass(frozen=True, slots=True)
class CommandExecutionResult:
    command: tuple[str, ...]
    returncode: int


def build_quality_commands(include_format_fix: bool = True) -> list[list[str]]:
    commands: list[list[str]] = [["ruff", "check", "."]]
    if include_format_fix:
        commands[0].append("--fix")
        commands.append(["ruff", "format", "."])
    else:
        commands.append(["ruff", "format", ".", "--check"])
    commands.extend([["pytest"], ["pyright"]])
    return commands


def build_test_command() -> list[str]:
    return ["pytest"]


def build_license_command(output_file: Path) -> list[str]:
    return [
        sys.executable,
        "-m",
        "piplicenses",
        "--python",
        sys.executable,
        "--format=markdown",
        "--with-urls",
        "--output-file",
        str(output_file),
    ]


def run_commands(commands: list[list[str]], root: Path) -> list[CommandExecutionResult]:
    results: list[CommandExecutionResult] = []
    for command in commands:
        completed_process = run_process(command, root=root)
        results.append(
            CommandExecutionResult(
                command=tuple(command),
                returncode=completed_process.returncode,
            )
        )
        if completed_process.returncode != 0:
            break
    return results
