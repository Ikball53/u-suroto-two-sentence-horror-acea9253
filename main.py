#!/usr/bin/env python3
"""Two-Sentence Horror — writes the entry story to /output/entry.txt."""

from pathlib import Path

STORY = (
    "My daughter has counted 47 stuffed animals on her bed "
    "every night since she was four. "
    "Tonight she counted 48, and the new one was holding her hand."
)


def main() -> None:
    # The gate allows 1–400 characters and the brief demands exactly two
    # sentences, so refuse to write anything that breaks either rule.
    sentences = [piece for piece in STORY.split(". ") if piece]
    if len(sentences) != 2 or len(STORY) > 400:
        raise ValueError("story must be exactly two sentences, at most 400 chars")
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(STORY.encode("utf-8"))


if __name__ == "__main__":
    main()
