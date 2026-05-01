from __future__ import annotations

from project_name import TemplateMetadata, get_template_metadata


def test_public_api_exposes_template_metadata() -> None:
    metadata = get_template_metadata()

    assert isinstance(metadata, TemplateMetadata)
    assert metadata.package_name == "project_name"
    assert metadata.distribution_name == "project-name"
    assert metadata.bootstrap_required is True
    assert "bootstrap" in metadata.cli_commands
