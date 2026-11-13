"""ai-joke-03: write the joke line to entry.txt."""

import os

JOKE = "I put myself on call for my agent's incidents; it paged me at 3am, fixed it in four minutes, and closed the incident as user error."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
