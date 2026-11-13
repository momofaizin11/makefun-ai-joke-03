"""make.fun entry: writes one joke to entry.txt. Deterministic, stdlib only."""

import os
from pathlib import Path

JOKE = "I asked my agent to write the changelog. It filed me under breaking changes."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
