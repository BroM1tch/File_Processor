"""
FileProcessor
--------------
Reads a text file and displays its content.

Author: Michel Brochu
Version: 1.0.0
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def read_lines(path: Path) -> list[str]:
    """Read all lines from a text file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()

def count_items(lines: list[str]) -> [str, int]:
    """Count occurrences of each non-empty line (trimmed)."""
    counts: dict[str, int] = {}

    for line in lines:
        item = line.strip()
        if not item:
            continue
        counts[item] = counts.get(item, 0) + 1

    return counts

def write_report(path: Path, counts: dict[str, int]) -> None:
    """Write a sorted report to an output file."""

    with open(path, "w", encoding="utf-8") as f:
        f.write("FileProcessor Report\n")
        f.write("=================\n")
        for item, n in sorted(counts.items()):
            f.write(f"{item}: {n}\n")

def main() -> None:
    input_path = BASE_DIR / "input" / "sample.txt"
    output_path = BASE_DIR / "output" / "report.txt"


    lines = read_lines(input_path)
    counts = count_items(lines)
    write_report(output_path, counts)

    print(f"✅ Report created: {output_path}")

if __name__ == "__main__":
    main()