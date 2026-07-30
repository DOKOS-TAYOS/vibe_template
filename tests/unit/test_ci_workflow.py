from __future__ import annotations

from pathlib import Path


def test_ci_workflow_runs_fresh_template_smoke_job() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    workflow_content = (repo_root / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")

    assert "template-smoke:" in workflow_content
    assert "os: [ubuntu-latest, windows-latest]" in workflow_content
    assert 'python-version: ["3.12"]' in workflow_content
    assert "python scripts/bootstrap_smoke.py" in workflow_content


def test_ci_workflow_uses_minimal_token_permissions() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    workflow_content = (repo_root / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")

    assert "permissions:" in workflow_content
    assert "contents: read" in workflow_content
    assert "persist-credentials: false" in workflow_content


def test_ci_workflow_exposes_required_gate_for_every_essential_job() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    workflow_content = (repo_root / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")

    assert "paths-ignore:" not in workflow_content
    assert "dependency-review:" in workflow_content
    assert "required-pr-ci:" in workflow_content
    assert "needs: [test, template-smoke, dependency-review]" in workflow_content
    assert "TEST_RESULT: ${{ needs.test.result }}" in workflow_content
    assert "TEMPLATE_SMOKE_RESULT: ${{ needs.template-smoke.result }}" in workflow_content
    assert "DEPENDENCY_REVIEW_RESULT: ${{ needs.dependency-review.result }}" in workflow_content
