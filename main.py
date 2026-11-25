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


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    lines = written.splitlines()
    if len(lines) != 1:
        print(f"expected 1 line, got {len(lines)}", file=sys.stderr)
        return 1
    if not lines[0].strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if len(lines[0]) > MAX_CHARS:
        print(f"entry is {len(lines[0])} chars, over {MAX_CHARS}", file=sys.stderr)
        return 1
    print(f"wrote {len(lines[0])} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
