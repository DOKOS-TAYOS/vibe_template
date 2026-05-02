from __future__ import annotations

from project_name import get_template_metadata


def main() -> None:
    metadata = get_template_metadata()
    print(f"Research template package: {metadata.package_name}")
    print("Verified research files: research/question.md, research/protocol.md, research/claims.md")
    print(f"Bootstrap required: {metadata.bootstrap_required}")


if __name__ == "__main__":
    main()
