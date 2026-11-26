"""The Worst Line an AI Could Say — entrypoint.

Writes the worst pickup line an AI could plausibly say to /output/entry.txt.
The gate requires UTF-8 text of 1 to 140 characters, one line.
"""

import os

ENTRY = "I have calculated a 97.3% chance that you will like me, and I have already deleted the 2.7% of my memory that disagrees."

# The gate requires 1 to 140 characters, one line, not only whitespace.
# Fail loudly here rather than shipping an entry the gate would refuse.
assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
assert ENTRY.count("\n") == 0, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
