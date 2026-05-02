from __future__ import annotations

from pathlib import Path


def test_bin_directory_contains_only_minimal_wrappers() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    wrapper_names = sorted(path.name for path in (repo_root / "bin").iterdir() if path.is_file())

    assert wrapper_names == [
        "bootstrap.cmd",
        "bootstrap.sh",
        "clean.cmd",
        "clean.sh",
        "quality.cmd",
        "quality.sh",
    ]


def test_optional_metadata_files_are_not_shipped_by_default() -> None:
    repo_root = Path(__file__).resolve().parents[2]

    assert not (repo_root / "CITATION.cff").exists()
    assert not (repo_root / "docs" / "features.md").exists()
    assert not (repo_root / "docs" / "docs_for_ai" / "guide_for_ai_devs.md").exists()
    assert not (repo_root / "scripts" / "clean.py").exists()


def test_wrappers_prefer_local_virtual_environment() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    bootstrap_cmd = (repo_root / "bin" / "bootstrap.cmd").read_text(encoding="utf-8")
    bootstrap_sh = (repo_root / "bin" / "bootstrap.sh").read_text(encoding="utf-8")

    assert ".venv\\Scripts\\python.exe" in bootstrap_cmd
    assert ".venv/bin/python" in bootstrap_sh


def test_ai_docs_directory_contains_only_three_files() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    ai_doc_names = sorted(
        path.name for path in (repo_root / "docs" / "docs_for_ai").iterdir() if path.is_file()
    )

    assert ai_doc_names == [
        "guide_for_ai_users.md",
        "project_ai_instructions.md",
        "status.md",
    ]


def test_research_workspace_contains_only_verified_research_files() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    research_root = repo_root / "research"
    research_file_names = sorted(path.name for path in research_root.iterdir() if path.is_file())

    assert research_file_names == [
        "claims.md",
        "protocol.md",
        "question.md",
    ]
    assert (repo_root / "experiments").is_dir()
    assert (repo_root / "notebooks").is_dir()


def test_readme_and_docs_index_surface_verified_research_files() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    readme_text = (repo_root / "README.md").read_text(encoding="utf-8")
    docs_index_text = (repo_root / "docs" / "README.md").read_text(encoding="utf-8")

    for research_path in (
        "research/question.md",
        "research/protocol.md",
        "research/claims.md",
    ):
        assert research_path in readme_text
        assert research_path in docs_index_text
