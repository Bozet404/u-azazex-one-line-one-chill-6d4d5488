#!/usr/bin/env python3
"""One Line, One Chill — a make.fun entry.

Writes one original horror sentence to /output/entry.txt.
One sentence, under 200 characters, meant to frighten a reader
in a single breath: no setup, no paragraph, no second chance.
"""

import os

LINE = "The dentist found a second set of teeth growing behind mine, and this morning they were already chewing."

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry line must be 1-200 characters, got %d" % len(line))
    if "\n" in line or line.count(".") != 1:
        raise SystemExit("entry must be a single sentence on one line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
