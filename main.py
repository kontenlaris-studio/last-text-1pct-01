"""Last Text at One Percent entry: autocorrect's final act at 1% battery."""

import os

JOKE = (
    "Autocorrect's final act at 1%: it changed my goodbye text to my boss "
    'from "see you Monday" to "see you in court," and honestly, the battery '
    "died proud."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
