#!/usr/bin/env python3
"""
Remove non-script content from instructor script files.
Removes: meta conversation, transition directives, Slide:/Script: headers, Optional teaching cues.
"""

import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent


def should_remove_line(line: str) -> bool:
    """Return True if line should be removed (non-script meta content)."""
    s = line.strip()
    if not s:
        return False  # Keep blank lines for now, trim later

    # Meta conversation / transition directives
    if s in ("continue", "proceed", "ok", "coninute"):
        return True
    if re.match(r'^Say ["\']continue["\']', s, re.I):
        return True
    if s.startswith("If you want, I'll do the next one"):
        return True
    if s.startswith("If you want, next I can do "):
        return True
    if s.startswith("If you want, next we can ") and ("turn" in s or "do the Week" in s):
        return True
    if s.startswith("Next, I recommend we go straight into"):
        return True
    if re.match(r"^Next, we (?:should|can) (?:go into|move into) .+, (?:which|that)", s):
        return True
    if re.match(r"^Next, we move into .+, (?:which|where)", s):
        return True
    if s.startswith("If you want, next we can turn all of this into"):
        return True

    return False


def remove_meta_block(lines: list[str], filepath: Path) -> list[str]:
    """Remove known meta blocks (conversation about converting content)."""
    text = "\n".join(lines)
    path_str = str(filepath)

    # 02-applied-ai-lecture: Remove from "are there any left?" through end
    if "02-applied-ai-lecture" in path_str:
        idx = text.find("\n\nare there any left?")
        if idx != -1:
            text = text[:idx].rstrip()

    # 10-future-workflows: Remove from "If you want, next we can turn" through end
    if "10-future-workflows" in path_str:
        idx = text.find('\n\nIf you want, next we can turn all of this into:')
        if idx != -1:
            text = text[:idx].rstrip()

    return text.split("\n")


def clean_file(filepath: Path) -> bool:
    """Clean one file. Returns True if changes were made."""
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")

    # Remove meta blocks first
    lines = remove_meta_block(lines, filepath)

    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]

        stripped = line.strip()

        # Remove Slide: header lines
        if stripped.startswith("Slide:"):
            i += 1
            if i < len(lines) and lines[i].strip() == "Script:":
                i += 1
            continue
        if stripped == "Script:":
            i += 1
            continue

        # Remove Optional teaching cue block
        if stripped == "Optional teaching cue:":
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if not next_line or next_line.startswith("Slide:"):
                    break
                i += 1
            continue

        if should_remove_line(line):
            i += 1
            continue

        # Remove "a full instructor script per week" etc. from 10-future-workflows
        if "or a polished course packet" in line or "or speaker notes aligned" in line:
            i += 1
            continue
        if "Just tell me" in line and "👍" in line:
            i += 1
            continue

        new_lines.append(line)
        i += 1

    # Collapse multiple consecutive blank lines, trim trailing
    result = []
    prev_blank = False
    for line in new_lines:
        is_blank = not line.strip()
        if is_blank and prev_blank:
            continue
        prev_blank = is_blank
        result.append(line)
    while result and not result[-1].strip():
        result.pop()

    new_content = "\n".join(result)
    if new_content != content:
        filepath.write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    md_files = list(SCRIPT_DIR.rglob("*.md"))
    md_files = [f for f in md_files if f.name != "raw.md"]

    changed = 0
    for f in sorted(md_files):
        if clean_file(f):
            changed += 1
            print(f"Cleaned: {f.relative_to(SCRIPT_DIR)}")

    print(f"\nCleaned {changed} files.")


if __name__ == "__main__":
    main()
