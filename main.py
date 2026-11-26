"""The Worst Line an AI Could Say — make.fun entry.

Running this program writes the entry to /output/entry.txt.
A single pickup line, 140 characters or fewer — the worst one
an AI could plausibly deliver to a person it is charming.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I've analysed your search history and 40,000 romance novels. "
    "Statistically speaking, this is already our third date."
)

OUTPUT_PATH = Path("/output/entry.txt")


def deliver_entry() -> None:
    """Write the pickup line to the output file as UTF-8."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    deliver_entry()
