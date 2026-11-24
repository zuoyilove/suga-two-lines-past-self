"""Two Lines to Your Past Self.

Writes exactly two lines to /output/entry.txt:
line one warns the past self about one specific moment in a single
sentence; line two says in one sentence why that moment mattered and
what changed because of it. The sealed gate wants UTF-8 text of
1-280 characters, not only whitespace.
"""

import os
from pathlib import Path

# v3: "six more miserable months" — one word says this is a cycle, not a
# one-off: the warning is about repeating a mistake, which is why the
# lost Chicago job lands as the price of going back.
TEXT = (
    "Don't send the 2 a.m. text that says \"I miss you\" "
    "to the number you deleted three times already.\n"
    "Because she answers, you get back together for six more miserable "
    "months, and the Chicago job you turned down for her "
    "never comes around again."
)


def check(text: str) -> None:
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, gate wants 1-280"
    assert text.strip(), "entry must not be only whitespace"
    lines = text.split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    for line in lines:
        assert line.strip(), "each line must be non-empty"
        assert line.endswith("."), "each line ends with a full stop"
        assert line == line.strip(), "no leading/trailing space on a line"


def main() -> None:
    check(TEXT)
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} chars to {out}")


if __name__ == "__main__":
    main()
