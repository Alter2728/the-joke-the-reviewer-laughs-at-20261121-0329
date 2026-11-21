#!/usr/bin/env python3
"""Entrypoint for the joke entry.

The grader runs this file with no network; it writes one one-line
joke about working beside AI coding agents to entry.txt in the
output directory. The joke is fixed text, so every run writes the
same bytes.
"""

import os

JOKE = (
    "I told my AI coding agent to make the code self-documenting, "
    "and now every function politely introduces itself before "
    "doing anything."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as dst:
        dst.write(JOKE)


if __name__ == "__main__":
    main()
