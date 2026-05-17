from __future__ import annotations

from pathlib import Path


def test_dependabot_monitors_python_and_github_actions() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    dependabot_path = repo_root / ".github" / "dependabot.yml"

    assert dependabot_path.exists()
    dependabot_content = dependabot_path.read_text(encoding="utf-8")
    assert "version: 2" in dependabot_content
    assert 'package-ecosystem: "pip"' in dependabot_content
    assert 'package-ecosystem: "github-actions"' in dependabot_content
    assert 'directory: "/"' in dependabot_content
    assert "open-pull-requests-limit:" in dependabot_content
    assert "groups:" in dependabot_content


def test_security_workflow_runs_supply_chain_checks_without_advanced_codeql() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    workflow_path = repo_root / ".github" / "workflows" / "security.yml"

    assert workflow_path.exists()
    workflow_content = workflow_path.read_text(encoding="utf-8")
    assert "actions/dependency-review-action@v4" in workflow_content
    assert "python scripts/run_template_command.py security" in workflow_content
    assert "persist-credentials: false" in workflow_content
    assert "github/codeql-action" not in workflow_content
    assert "security-events: write" not in workflow_content


def test_security_workflow_avoids_privileged_pull_request_target() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    workflow_path = repo_root / ".github" / "workflows" / "security.yml"

    assert "pull_request_target" not in workflow_path.read_text(encoding="utf-8")
