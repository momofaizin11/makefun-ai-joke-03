"""ai-joke-03 entry: writes the one-line joke to entry.txt."""

import os

JOKE = (
    "I put the agent on a maintenance window; it deploys at 03:17, "
    "then sets the window back."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
