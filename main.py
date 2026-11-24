#!/usr/bin/env python3
"""make.fun entry: u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.

Writes a single real-life patch note, in release-note register, to
/output/entry.txt. One line, no trailing newline.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

NOTE = "v3.2.1: Fixed a bug where walking into a room deleted the reason you entered it. The reason now loads before the doorway, not after."

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def validate_note(text: str) -> None:
    if "\n" in text or "\r" in text:
        raise ValueError("patch note must be a single line")
    if not 1 <= len(text) <= 160:
        raise ValueError("patch note must be 1-160 characters")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    validate_note(NOTE)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(NOTE)
    if path.read_text(encoding="utf-8") != NOTE:
        raise IOError("written entry does not match the patch note")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
