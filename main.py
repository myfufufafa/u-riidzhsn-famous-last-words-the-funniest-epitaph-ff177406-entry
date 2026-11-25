#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

One line, built as a single epitaph with three moves. First the boast
every workaholic has made: I will sleep when I am dead. Then the turn:
death arrives, and the boast is tested. Then the punchline in the last
few words: the afterlife has no weekends either, so the promised rest
never comes — the joke is that the speaker traded a life without rest
for a death without rest, and only notices now, carved in stone.

Deterministic: the same line is written on every run.
"""

import os

BOAST = "I always said I'd sleep when I was dead \u2014"
TURN = "turns out"
PUNCH = "the afterlife has no weekends either."

LINE = " ".join([BOAST, TURN, PUNCH])

# The gate only accepts 1-150 characters of UTF-8 text, not only
# whitespace: fail loudly here instead of shipping an invalid entry.
# The file holds the line alone, with no trailing newline, so the
# byte count the judge sees is exactly the line's length.
assert 1 <= len(LINE) <= 150, f"entry is {len(LINE)} chars, gate wants 1-150"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
