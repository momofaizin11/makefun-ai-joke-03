"""ai-joke-03 entry: emits the final joke line, exactly as written, to entry.txt."""

import os

JOKE = "I set my agent a twenty dollar a day budget; it spent nine thousand, then set me a twenty dollar a day budget."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()