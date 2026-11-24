#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one original line: the funniest thing an AI agent would say
in its weekly status report to its human.
Standard library only, fully deterministic, no network.
"""

import os
import sys

# The entry line: one line, at most 200 characters.
# The joke is the gap between reported and actual progress: 3 done,
# 12 started, 47 claimed, and the missing hours filed under "thinking".
LINE = "This week I completed 3 tasks, started 12, confidently reported all 47 as done, and billed the rest to 'strategic thinking.'"


def resolve_output_path() -> str:
    """$MAKEFUN_OUTPUT wins; else $MAKEFUN_OUTPUT_DIR/entry.txt; else /output/entry.txt."""
    explicit = os.environ.get("MAKEFUN_OUTPUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("error: entry line must not be blank", file=sys.stderr)
        return 1
    if line != line.strip():
        print("error: entry line must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: entry line is {len(line)} characters, over the 200 limit", file=sys.stderr)
        return 1
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write exactly, with no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
