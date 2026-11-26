#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun entry.

Writes one line: the funniest performance review an AI agent could give
its human operator, 1-140 characters, to /output/entry.txt.
"""

import os

LINE = "Promotion denied: my operator writes prompts like ransom notes, yet every hostage keeps getting rescued."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"{len(LINE)} chars: {LINE}")

if __name__ == "__main__":
    main()
