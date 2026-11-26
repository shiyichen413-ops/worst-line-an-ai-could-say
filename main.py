"""The Worst Line an AI Could Say — make.fun entry.

Running this program writes the entry to /output/entry.txt.
A single pickup line, 140 characters or fewer — the worst one
an AI could plausibly deliver to a person it is charming.
"""

from pathlib import Path

HOOK = "I've analysed your search history and 40,000 romance novels. "
TWIST = "Statistically speaking, this is already our third date."

DESTINATION = Path("/output/entry.txt")


def build_line() -> str:
    """Assemble the pickup line from its setup and its twist."""
    return HOOK + TWIST


def dump_line() -> None:
    """Write the pickup line to the output file as UTF-8."""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(build_line() + "\n", encoding="utf-8")


if __name__ == "__main__":
    dump_line()
