#!/usr/bin/env python3
"""
Add YAML frontmatter to script .md files. Replaces # NN title with proper metadata.
"""

import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DATE = "2026-03-21"


def filename_to_title(filename: str) -> str:
    """Convert '05-vision-and-images.md' or 'advanced_RAG-vs-Fine-Tuning.md' to title."""
    stem = Path(filename).stem
    # Remove leading digits and hyphen, or 'advanced_' prefix
    name = re.sub(r"^\d+-", "", stem)
    name = re.sub(r"^advanced_", "", name)
    # Replace hyphens with spaces, title case (lowercase: and, or, the, etc.)
    words = name.replace("-", " ").split()
    minor = {"and", "or", "the", "a", "an", "to", "in", "on", "vs", "with"}
    acronyms = {"ai", "rag", "mcp", "api", "llm", "nlp", "ux", "roi"}
    result = []
    for i, w in enumerate(words):
        if w.lower() in minor and i > 0:
            result.append(w.lower())
        elif w.lower() in acronyms:
            result.append(w.upper())
        else:
            result.append(w.capitalize())
    return " ".join(result)


def folder_to_week(path_str: str) -> int:
    """Convert 'week03_applications' or 'advanced_course/week01_ml-foundations' to week number."""
    m = re.search(r"week(\d+)[_-]", path_str)
    return int(m.group(1)) if m else 0


def filename_to_weight(filename: str) -> str:
    """Extract weight from '05-vision-and-images.md' -> '05'."""
    stem = Path(filename).stem
    m = re.match(r"^(\d+)", stem)
    return m.group(1) if m else "00"


def add_frontmatter(filepath: Path) -> bool:
    """Add or replace frontmatter. Returns True if changed."""
    original = filepath.read_text(encoding="utf-8")
    content = original
    rel = filepath.relative_to(SCRIPT_DIR)
    path_str = str(rel)
    filename = filepath.name

    title = filename_to_title(filename)
    week = folder_to_week(path_str)
    weight = filename_to_weight(filename)

    frontmatter = f"""---
Title: {title}
Draft: False
Date: {DATE}
Week: {week}
Weight: {weight}
---

"""

    # Strip all existing frontmatter blocks (--- ... ---) from start
    while content.strip().startswith("---"):
        idx = content.find("---", 3)  # Find closing ---
        if idx == -1:
            break
        content = content[idx + 3 :].lstrip("\n")
    else:
        # Remove # title line (# NN title or # plain title)
        lines = content.split("\n")
        new_lines = []
        skipped_title = False
        for line in lines:
            stripped = line.strip()
            if not skipped_title and re.match(r"^#\s+(?:\d+[\s-])?.*$", stripped):
                skipped_title = True
                continue
            if not skipped_title and stripped == "":
                continue
            skipped_title = True
            new_lines.append(line)
        content = "\n".join(new_lines).lstrip()

    new_content = frontmatter + content
    if new_content != original:
        filepath.write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    md_files = [f for f in SCRIPT_DIR.rglob("*.md") if f.name not in ("raw.md", "raw2.md")]
    changed = 0
    for f in sorted(md_files):
        if add_frontmatter(f):
            changed += 1
            print(f"Updated: {f.relative_to(SCRIPT_DIR)}")
    print(f"\nUpdated {changed} files.")


if __name__ == "__main__":
    main()
