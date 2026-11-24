"""Write one original roast line deterministically, without a trailing newline."""

from pathlib import Path
import os

ENTRY = "My earbuds die after one song; their case lasts a week — the case does all the work and the buds take all the credit."

if "\n" in ENTRY or "\r" in ENTRY or not ENTRY.strip():
    raise ValueError("ENTRY must be a non-empty single line")


def main():
    output_path = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(ENTRY.encode("utf-8"))
    output_path.chmod(0o644)


if __name__ == "__main__":
    main()
