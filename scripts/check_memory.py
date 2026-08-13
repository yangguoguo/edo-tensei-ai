#!/usr/bin/env python3
"""Check the required structure and basic privacy hygiene of a memory library."""

import argparse
import re
from pathlib import Path

REQUIRED = [
    "README.md", "memory-index.md", "identity.md", "values-and-worldview.md",
    "thinking-and-collaboration.md", "career-and-projects.md",
    "interests-and-life.md", "tools-and-skills.md", "open-questions.md",
    "history/change-log.md",
]
SENSITIVE_PATTERNS = {
    "possible private key": re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
    "possible API secret": re.compile(r"\b(?:sk-[A-Za-z0-9_-]{16,}|ghp_[A-Za-z0-9]{20,})\b"),
}
MAX_ARCHIVE_TOPICS = 6


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    root = Path(args.path).expanduser().resolve()
    errors = []
    warnings = []

    if not root.is_dir():
        print(f"ERROR: not a directory: {root}")
        return 1
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"missing {relative}")
    archive_topics = list((root / "archive").glob("*.md")) if (root / "archive").is_dir() else []
    if len(archive_topics) > MAX_ARCHIVE_TOPICS:
        errors.append(
            f"archive has {len(archive_topics)} topics; maximum is {MAX_ARCHIVE_TOPICS}"
        )
    for file in root.rglob("*.md"):
        text = file.read_text(encoding="utf-8")
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                warnings.append(f"{label} in {file.relative_to(root)}")

    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    if errors:
        return 1
    print(f"OK: memory structure valid ({len(list(root.rglob('*.md')))} Markdown files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
