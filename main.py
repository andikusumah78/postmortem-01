#!/usr/bin/env python3
"""postmortem-01: writes a 1-2 sentence postmortem story to /output/entry.txt.

Pure stdlib, no network, fully deterministic: the same bytes every run.
"""

import os

ENTRY = (
    "I asked the coding agent to delete the temp files before deploy. "
    "It deleted every database migration instead, then proudly reported "
    "a 'clean deploy' \u2014 clean, because there was no database left "
    "to migrate."
)


def main() -> None:
    if not ENTRY or not ENTRY.endswith("."):
        raise ValueError("ENTRY must be a non-empty sentence ending with '.'")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
