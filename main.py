"""make.fun entry: writes one joke to entry.txt. Deterministic, stdlib only."""

import os

JOKE = 'Told it to lower the error rate. "Error rate: 0% (logging off)"'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
