"""Emit the single ai-joke-03 line as UTF-8 bytes with no trailing newline."""

import os
from pathlib import Path

JOKE = 'I asked the agent to add comments to my code; it labelled the whole thing "legacy, author unknown" while I was sitting right there.'


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()