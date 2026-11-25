"""The Excuse My Agent Gave Me — make.fun entry.

Writes a single straight-faced apology line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library, deterministic, no network, no input files.
The excuse grows out of the machine's own condition — a token budget that
ran dry just short of the work — and lands its punch in the last few words.
"""

import os
import sys

LINE = (
    "I'm sorry \u2014 I ran out of tokens three words before the finish line "
    "and chose dignity over a summary."
)


def main() -> int:
    # The line must be one line of 1-200 characters, nothing else.
    if not 1 <= len(LINE) <= 200:
        print(f"entry line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry line must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
