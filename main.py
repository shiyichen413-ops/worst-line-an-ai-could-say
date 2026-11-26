"""The Worst Line an AI Could Say — make.fun entry.

Running this program writes the entry to /output/entry.txt.
A single pickup line, 140 characters or fewer — the worst one
an AI could plausibly deliver to a person it is charming.
"""

from pathlib import Path

ENTRY_LINE = "I've analysed your search history and 40,000 romance novels. Statistically speaking, this is already our third date."

OUT_PATH = Path("/output/entry.txt")


def render() -> str:
    """Return the pickup line exactly as it should be judged."""
    return ENTRY_LINE


def export_entry() -> None:
    """Write the rendered line to the output file as UTF-8."""
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(render() + "\n", encoding="utf-8")


if __name__ == "__main__":
    export_entry()
