"""Worst Superpower — entry program.

Writes one line, at most 140 characters, inventing the most useless
superpower imaginable, to /output/entry.txt.
"""

import os

ENTRY = "I can talk to fish, but only goldfish, and all they ever want to discuss is the plastic castle."


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
