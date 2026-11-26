"""Worst Superpower — entry program.

Writes one line, at most 140 characters, inventing the most useless
superpower imaginable, to /output/entry.txt.

The power is useless by design: time stops for exactly one second, and
the one thing the hero always does with it is blink — so it can never
help, impress, or even be noticed.
"""

import hashlib
import os

ENTRY = "I can stop time, but only for one second, and I always waste it blinking."


def verify_output() -> None:
    """Check the entry line and report its length and sha256 digest."""
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, over the 140 limit"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing whitespace"
    digest = hashlib.sha256((ENTRY + "\n").encode("utf-8")).hexdigest()
    print(f"entry: {len(ENTRY)} chars, sha256: {digest}")


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    verify_output()
    main()
