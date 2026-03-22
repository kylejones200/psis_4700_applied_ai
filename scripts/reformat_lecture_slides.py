#!/usr/bin/env python3
"""Convert lecture slide body text to bullets. Keeps ##, >, ![], --- as-is."""

import re
import sys
from pathlib import Path


def convert_slide(slide: str) -> str:
    """Convert a single slide's body text to bullets."""
    lines = slide.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Keep ## headers as-is
        if line.startswith("## "):
            result.append(line)
            result.append("")  # blank line after header
            i += 1
            continue

        # Keep images
        if line.strip().startswith("![]("):
            result.append(line)
            i += 1
            continue

        # Keep block quotes
        if line.strip().startswith(">"):
            result.append("")
            result.append(line)
            i += 1
            continue

        # Skip leading blank lines before body
        if not result or result[-1] == "":
            if not line.strip():
                i += 1
                continue

        # Keep single # title lines (e.g. # AAI 3013)
        if re.match(r"^# [^#]", line):
            result.append(line)
            i += 1
            continue

        # Body text: convert to bullets (but not ## or # lines or blank)
        if line.strip() and not line.startswith("##") and not re.match(r"^# ", line):
            # Handle multi-line phrases (e.g. "Lecture 1  \nCourse Framing")
            stripped = line.strip()
            if stripped:
                result.append("- " + stripped)
            i += 1
            continue

        # Blank lines
        if not line.strip():
            result.append(line)
            i += 1
            continue

        # Fallback
        result.append(line)
        i += 1

    return "\n".join(result).rstrip()


def process_file(path: Path) -> None:
    content = path.read_text()
    slides = re.split(r"\n---\n", content)

    output = []
    for i, slide in enumerate(slides):
        slide = slide.strip()
        if not slide:
            continue
        converted = convert_slide(slide)
        output.append(converted)

    new_content = "\n---\n".join(output)
    # Fix double blank lines before block quotes
    new_content = re.sub(r"\n{3,}>", "\n\n>", new_content)
    # Fix bullet lists that lost blank line before >
    new_content = re.sub(r"^(- .+)\n(> )", r"\1\n\n\2", new_content, flags=re.MULTILINE)
    path.write_text(new_content)
    print(f"Processed {path.name}")


def main():
    base = Path(__file__).parent.parent / "webslides" / "lectures_full"
    for name in sys.argv[1:] or [
        "lecture1_What-Is-Applied-AI.md",
        "lecture2_Data-and-Models.md",
        "lecture3_Working-with-Text.md",
        "lecture4_Vision-and-Images.md",
        "lecture5_AI-in-Business.md",
    ]:
        path = base / name
        if path.exists():
            process_file(path)
        else:
            print(f"Skip {name} (not found)")


if __name__ == "__main__":
    main()
