#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes one funny one-line review of the agent's own Monday to the
output entry file: a single line, under 200 characters, no title,
no explanation. Pure stdlib, no network, deterministic.
"""

import os

LINE = (
    "My Monday reviewed itself: 9 a.m. standup, 47 unread emails, "
    "and a coffee that quit before I did \u2014 one star, would not relive."
)


def main() -> None:
    text = LINE.strip()
    # Gate: 1-200 characters, exactly one line, no surrounding whitespace.
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text, "entry must not be empty"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and confirm the file holds exactly the validated line.
    with open(target, encoding="utf-8") as f:
        assert f.read().strip() == text
    print(f"Wrote {len(text)} characters to {target}")


if __name__ == "__main__":
    main()
