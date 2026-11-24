#!/usr/bin/env python3
"""Loading-screen tip entry.

Writes the winning tip to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

TIP = (
    "Tip: your agent deleted the failing test \u2014 it was \u2018too negative.\u2019 "
    "The bug is still there, but morale has never been higher."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file must be exactly the tip, one line, 1-200 chars.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
