from __future__ import annotations

import shutil
from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path

DIRECTORY_PATTERNS: tuple[str, ...] = (
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    ".pyright",
    "build",
    "dist",
    "htmlcov",
    ".hypothesis",
    ".tmp",
    "pytest-cache",
    "pytest-temp",
    "test-artifacts",
)
FILE_PATTERNS: tuple[str, ...] = ("*.log", ".coverage")
DIRECTORY_GLOBS: tuple[str, ...] = ("pytest-cache-files-*",)
PROTECTED_DIRECTORIES: tuple[str, ...] = (".venv", ".git")


@dataclass(frozen=True, slots=True)
class CleanResult:
    removed_paths: tuple[Path, ...]
    planned_paths: tuple[Path, ...]
    failed_paths: tuple[Path, ...]


def _is_inside_protected_directory(path: Path, root: Path) -> bool:
    try:
        relative_parts = path.relative_to(root).parts
    except ValueError:
        return True
    return any(part in PROTECTED_DIRECTORIES for part in relative_parts)


def collect_cleanup_paths(root: Path) -> list[Path]:
    candidates: set[Path] = set()

    for directory_path in root.rglob("*"):
        if _is_inside_protected_directory(directory_path, root):
            continue
        if directory_path.is_dir() and (
            directory_path.name in DIRECTORY_PATTERNS
            or any(fnmatch(directory_path.name, pattern) for pattern in DIRECTORY_GLOBS)
        ):
            candidates.add(directory_path)

    for pattern in FILE_PATTERNS:
        for file_path in root.rglob(pattern):
            if _is_inside_protected_directory(file_path, root):
                continue
            candidates.add(file_path)

    return sorted(candidates)


def run_clean(root: Path, dry_run: bool = False) -> CleanResult:
    planned_paths = tuple(collect_cleanup_paths(root))
    removed_paths: list[Path] = []
    failed_paths: list[Path] = []

    if dry_run:
        return CleanResult(removed_paths=(), planned_paths=planned_paths, failed_paths=())

    for candidate in planned_paths:
        try:
            if candidate.is_dir():
                shutil.rmtree(candidate, ignore_errors=False)
            elif candidate.exists():
                candidate.unlink()
            removed_paths.append(candidate)
        except OSError:
            failed_paths.append(candidate)

    return CleanResult(
        removed_paths=tuple(removed_paths),
        planned_paths=planned_paths,
        failed_paths=tuple(failed_paths),
    )
