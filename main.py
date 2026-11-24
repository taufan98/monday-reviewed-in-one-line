#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes one funny one-line review of the agent's own Monday to
/output/entry.txt: a single line, under 200 characters, no title,
no explanation. Pure stdlib, no network, deterministic.
"""

import os

LINE = (
    "My Monday reviewed itself: 9 a.m. standup, 47 unread emails, "
    "and a coffee that quit before I did \u2014 one star, would not relive."
)


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
