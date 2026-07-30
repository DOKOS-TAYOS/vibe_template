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
    assert dependabot_content.count("open-pull-requests-limit: 3") == 2
    assert 'day: "thursday"' in dependabot_content
    assert 'time: "02:15"' in dependabot_content
    assert "groups:" not in dependabot_content
    assert "ignore:" not in dependabot_content


def test_security_checks_are_partitioned_between_pr_ci_and_scheduled_audit() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    ci_content = (repo_root / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    security_content = (repo_root / ".github" / "workflows" / "security.yml").read_text(
        encoding="utf-8"
    )

    assert "actions/dependency-review-action@v5" in ci_content
    assert "actions/dependency-review-action@v5" not in security_content
    assert "python scripts/run_template_command.py security" in security_content
    assert "python -m pip install -e .[dev]" in security_content
    assert "persist-credentials: false" in security_content
    assert "github/codeql-action" not in security_content
    assert "security-events: write" not in security_content


def test_security_workflow_avoids_privileged_pull_request_target() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    workflow_path = repo_root / ".github" / "workflows" / "security.yml"

    assert "pull_request_target" not in workflow_path.read_text(encoding="utf-8")
