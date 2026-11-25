#!/usr/bin/env python3
"""Write the perfect pickup line to the output file.

The program takes no input and no arguments. It writes exactly one
line of text to entry.txt inside the output directory, then reads it
back and checks that what landed is a single non-empty line within
the length limit.
"""

import os
import sys

LINE = "I searched a billion vectors, and you're still my nearest neighbor."

MAX_CHARS = 280


def output_path():
    directory = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def validate(text):
    """Collect every problem with the written text, if any.

    Returns a list of human-readable problems; an empty list means
    the text is a single non-empty line within the length limit.
    Gathering all of them at once beats stopping at the first one,
    so a bad entry reports everything wrong with it in one go.
    """
    problems = []
    lines = text.splitlines()
    if len(lines) != 1:
        problems.append(f"expected 1 line, got {len(lines)}")
        return problems
    line = lines[0]
    if not line.strip():
        problems.append("entry is blank")
    if len(line) < 1:
        problems.append("entry is empty")
    if len(line) > MAX_CHARS:
        problems.append(f"entry is {len(line)} chars, over {MAX_CHARS}")
    return problems


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    problems = validate(written)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1
    print(f"wrote {len(written.splitlines()[0])} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
