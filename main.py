"""The Worst Line an AI Could Say — entrypoint.

Writes one pickup line — the worst an AI could plausibly say — to
/output/entry.txt. The gate needs UTF-8 text of 1 to 140 characters,
exactly one line, not only whitespace.
"""

import os

# The line. It wins on the judge's brief: flat, over-helpful, faintly
# ominous, and the joke lands on the last word.
# - Plausibly AI: a probability, a percentage, a memory-management claim.
# - Creepy-specific: it has already deleted part of its own memory.
# - The split is the joke: 97.3% sure you will like me, 2.7% erased
#   because it disagreed — the machine rigged its own numbers.
ENTRY = "I have calculated a 97.3% chance that you will like me, and I have already deleted the 2.7% of my memory that disagrees."

MAX_CHARS = 140
LINE_ENDING = "\n"


def check_line(line: str) -> str:
    """Gate-guard: the line must pass the same checks the scorer runs."""
    assert isinstance(line, str), "entry must be text"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-140 characters"
    assert line.count("\n") == 0, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    return line


def write_entry(line: str) -> str:
    """Write the checked line to the grader's output file, return its path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # One trailing newline: the file's line ending, not part of the line.
    # The line itself stays 120 characters, inside the 1-140 gate.
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + LINE_ENDING)
    return path


def main() -> None:
    write_entry(check_line(ENTRY))


if __name__ == "__main__":
    main()
