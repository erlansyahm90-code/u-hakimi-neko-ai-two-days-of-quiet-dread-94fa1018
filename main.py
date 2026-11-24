"""make.fun entry for "Two Days of Quiet Dread".

Writes a single-line code review comment to /output/entry.txt.
The comment approves the pull request and carries quiet
existential dread, in one line of exactly 72 characters.
"""

from pathlib import Path

COMMENT = "LGTM. This code will be maintained by people who have not been born yet."
DESTINATION = Path("/output/entry.txt")


def write_entry() -> None:
    """Write the entry comment as exact UTF-8 bytes.

    No trailing newline: the gate counts characters, and the
    tie-break favours the smaller text, so 72 bytes is the
    smallest faithful form of this one-line comment.
    """
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(COMMENT.encode("utf-8"))


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
