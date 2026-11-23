#!/usr/bin/env python3
"""Copy the entry image to the output directory.

The image is drawn by draw.py (kept out of this repository) and stored
here as entry.png; this program only copies it, so the two grading runs
produce byte-identical output.
"""
import hashlib
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as f:
        data = f.read()
    size = len(data)
    sha = hashlib.sha256(data).hexdigest()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    if size > 1048576:
        print(f"entry.png too large: {size} bytes", file=sys.stderr)
        return 1
    shutil.copyfile(SRC, dst)
    with open(dst, "rb") as f:
        check = hashlib.sha256(f.read()).hexdigest()
    if check != sha:
        print("copy verification failed", file=sys.stderr)
        return 1
    print(f"wrote {dst}: {size} bytes, sha256 {sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
