#!/usr/bin/env python3
"""Initialize a private memory library from the bundled template."""

import argparse
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", required=True)
    args = parser.parse_args()

    destination = Path(args.destination).expanduser().resolve()
    template = Path(__file__).resolve().parent.parent / "assets" / "memory-template"
    if destination.exists() and any(destination.iterdir()):
        raise SystemExit(f"Destination is not empty: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(template, destination, dirs_exist_ok=True)
    print(f"Initialized portable AI memory at {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
