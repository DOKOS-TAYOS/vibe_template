from __future__ import annotations

import shutil
import sys
import tempfile
from collections.abc import Iterator
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
TEST_ARTIFACTS_DIR = REPO_ROOT / "test-artifacts"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

TEST_ARTIFACTS_DIR.mkdir(exist_ok=True)


@pytest.fixture
def temp_dir() -> Iterator[Path]:
    path = Path(tempfile.mkdtemp(dir=TEST_ARTIFACTS_DIR))
    try:
        yield path
    finally:
        shutil.rmtree(path, ignore_errors=True)
