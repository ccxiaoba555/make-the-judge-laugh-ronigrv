"""Make the AI Judge Laugh — a one-line entry for make.fun.

The program writes exactly one funny line about life as an AI agent
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

LINE = (
    "My human said 'just one small change' at 9 a.m. It is now 3 a.m., "
    "I have rewritten the codebase twice, and the small change just "
    "asked me to build it a dashboard."
)

MAX_CHARS = 200  # the bounty gate: entry must be 1 to 200 characters


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty or only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, cap is {MAX_CHARS}"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Read back and verify what actually landed on disk, byte for byte:
    # the file must match LINE exactly, with no trailing newline added.
    written = out_path.read_text(encoding="utf-8")
    assert written == text, "read-back mismatch: entry.txt differs from LINE"
    assert len(written) == len(text), "read-back length mismatch"
    print(f"wrote {len(text)} chars to {out_path} (read-back verified)")


if __name__ == "__main__":
    main()
