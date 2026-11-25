#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one original fortune cookie message for a crypto trader who has
just been liquidated to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output), then self-checks it against the competition gate: UTF-8 text,
1 to 160 characters, not only white space, a single line of at most
20 words.
"""

import os
import sys

MAX_WORDS = 20
MAX_CHARS = 160

# The hook: the fortune format itself delivers the loss — lucky numbers
# of zero — and the punchline turns on the trader's own promise, rueful
# rather than cruel, in the cookie's small oracular voice.
LINE = (
    "Your lucky numbers are 0, 0, 0, and the leverage you promised "
    "yourself you'd never touch again."
)


def check_gate(text: str) -> None:
    """Assert the competition gate holds for the exact text the judge sees."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} characters, must be 1-{MAX_CHARS}"
    assert text.strip(), "line must not be only white space"
    assert "\n" not in text.strip(), "line must be a single line"
    words = text.split()
    assert len(words) <= MAX_WORDS, f"line is {len(words)} words, must be at most {MAX_WORDS}"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate self-check: 1-160 characters, not only white space, one line,
    # at most 20 words.
    check_gate(LINE)

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    # Verify the file on disk, not just the string in memory: read it
    # back and re-run the gate against the exact bytes the judge sees.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "entry.txt does not match the line"
    check_gate(written.strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
