"""Break Production, Own It — make.fun entry.

Writes one brutally honest one-liner to /output/entry.txt
($MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
Python 3.13, standard library only, deterministic.
"""

import os
from pathlib import Path

LINE = (
    "I shipped it straight to prod, skipped the tests, and deleted "
    "the users table. The good news is the error page has never "
    "loaded faster."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
