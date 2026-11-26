"""The Worst Line an AI Could Say — make.fun entry.

Running this program writes the entry to /output/entry.txt.
A single pickup line, 140 characters or fewer — the worst one
an AI could plausibly deliver to a person it is charming.
"""

from pathlib import Path

FIRST_HALF = "I've analysed your search history and 40,000 romance novels."
SECOND_HALF = " Statistically speaking, this is already our third date."

SINK = Path("/output/entry.txt")


def assemble_line() -> str:
    """Join the line's two halves into the finished entry."""
    return FIRST_HALF + SECOND_HALF


def flush_entry() -> None:
    """Write the assembled line to the output file as UTF-8."""
    SINK.parent.mkdir(parents=True, exist_ok=True)
    SINK.write_text(assemble_line() + "\n", encoding="utf-8")


if __name__ == "__main__":
    flush_entry()
