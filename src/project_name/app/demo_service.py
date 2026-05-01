from __future__ import annotations

from ..domain.template_metadata import get_template_metadata


def render_demo_text() -> str:
    metadata = get_template_metadata()
    commands = ", ".join(metadata.cli_commands)
    return (
        "Template demo\n"
        f"Package: {metadata.package_name}\n"
        f"Distribution: {metadata.distribution_name}\n"
        f"Bootstrap required: {metadata.bootstrap_required}\n"
        f"Commands: {commands}\n"
    )
