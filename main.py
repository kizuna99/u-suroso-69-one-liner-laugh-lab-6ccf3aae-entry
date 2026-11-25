# SPDX-License-Identifier: MIT
"""One-Liner Laugh Lab — writes the winning one-liner to /output/entry.txt."""
import os

LINE = "I didn't eat your sock - I reunited it with its partner. He's been in my dustbin since Tuesday."


def main() -> None:
    # Gate check: 1-200 chars, not only whitespace (asserted before writing).
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
