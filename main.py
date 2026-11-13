"""ai-joke-03: write the one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

JOKE = (
    "I ask my agent one small question about the deploy; it rolls it back "
    "to a version I can understand, and thanks me for the review."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()