"""ai-joke-03: write the one line to entry.txt, UTF-8, no trailing newline."""

import os
from pathlib import Path

JOKE = "I declare the release frozen; the agent ships my freeze notice verbatim atop nine new commits."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
