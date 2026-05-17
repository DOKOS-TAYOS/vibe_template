from __future__ import annotations

import subprocess
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

from ..infrastructure.process_runner import run_process

PIP_AUDIT_CACHE_DIR = Path(".tmp") / "pip-audit-cache"
SECURITY_REQUIREMENTS_PATH = Path(".tmp") / "pip-audit-requirements.txt"


@dataclass(frozen=True, slots=True)
class CommandExecutionResult:
    command: tuple[str, ...]
    returncode: int


def _build_module_command(module_name: str, *args: str) -> list[str]:
    return [sys.executable, "-m", module_name, *args]


def build_quality_commands(check_only: bool = False, full: bool = False) -> list[list[str]]:
    commands: list[list[str]] = [_build_module_command("ruff", "check", ".")]
    if check_only:
        commands.append(_build_module_command("ruff", "format", ".", "--check"))
    else:
        commands[0].append("--fix")
        commands.append(_build_module_command("ruff", "format", "."))
    if full:
        commands.extend(
            [
                _build_module_command("pytest"),
                _build_module_command("pyright"),
            ]
        )
    return commands


def build_security_freeze_command(distribution_name: str) -> list[str]:
    return _build_module_command(
        "pip",
        "list",
        "--format=freeze",
        "--exclude-editable",
        "--exclude",
        distribution_name,
    )


def build_security_audit_command(
    requirements_file: Path = SECURITY_REQUIREMENTS_PATH,
    cache_dir: Path = PIP_AUDIT_CACHE_DIR,
) -> list[str]:
    return _build_module_command(
        "pip_audit",
        "--requirement",
        str(requirements_file),
        "--strict",
        "--no-deps",
        "--disable-pip",
        "--cache-dir",
        str(cache_dir),
        "--progress-spinner",
        "off",
        "--timeout",
        "30",
    )


def build_security_commands(
    distribution_name: str,
    requirements_file: Path = SECURITY_REQUIREMENTS_PATH,
    cache_dir: Path = PIP_AUDIT_CACHE_DIR,
) -> list[list[str]]:
    return [
        build_security_freeze_command(distribution_name=distribution_name),
        build_security_audit_command(requirements_file=requirements_file, cache_dir=cache_dir),
    ]


def build_test_command() -> list[str]:
    return _build_module_command("pytest")


def build_bootstrap_resync_command() -> list[str]:
    return [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-e",
        ".[dev]",
    ]


def load_distribution_name(project_root: Path) -> str:
    pyproject_data = tomllib.loads((project_root / "pyproject.toml").read_text(encoding="utf-8"))
    return str(pyproject_data["project"]["name"])


def build_license_command(output_file: Path, distribution_name: str) -> list[str]:
    return [
        sys.executable,
        "-m",
        "piplicenses",
        "--python",
        sys.executable,
        "--format=markdown",
        "--with-urls",
        "--ignore-packages",
        distribution_name,
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


def run_security_audit(root: Path) -> list[CommandExecutionResult]:
    distribution_name = load_distribution_name(root)
    freeze_command, audit_command = build_security_commands(distribution_name=distribution_name)
    requirements_path = root / SECURITY_REQUIREMENTS_PATH
    requirements_path.parent.mkdir(parents=True, exist_ok=True)

    freeze_process = subprocess.run(
        freeze_command,
        check=False,
        cwd=root,
        capture_output=True,
        text=True,
    )
    results = [
        CommandExecutionResult(
            command=tuple(freeze_command),
            returncode=freeze_process.returncode,
        )
    ]
    if freeze_process.returncode != 0:
        return results

    requirements_path.write_text(freeze_process.stdout, encoding="utf-8")
    completed_process = run_process(audit_command, root=root)
    results.append(
        CommandExecutionResult(
            command=tuple(audit_command),
            returncode=completed_process.returncode,
        )
    )
    return results
