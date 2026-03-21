#!/usr/bin/env python3
"""
Transform choppy script text into fluent narrative paragraphs.
Joins short lines, creates cohesive paragraphs, preserves meaning.
"""

import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

# Skip these - presenter notes, not narrative
SKIP_LINE_PATTERNS = (
    r"^(Pause and ask|Ask\.|Say\.|Frame this|Trace the|Give \d+ minutes|End with|Repeat the)\b",
)


def is_skip_line(line: str) -> bool:
    return bool(re.match(r"^(" + "|".join(
        "Pause and ask", "Ask\.", "Say\.", "Frame this", "Trace the",
        "Give \d+ minutes", "End with", "Repeat the"
    ).replace(".", r"\.") + ")", line.strip()))


def flow_transform(text: str) -> str:
    """Transform choppy lines into flowing paragraphs."""
    lines = text.split("\n")
    output = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Preserve frontmatter
        if stripped.startswith("---"):
            output.append(line)
            i += 1
            continue

        # Skip blank lines during accumulation
        if not stripped:
            output.append("")
            i += 1
            continue

        # Skip presenter cue lines
        if re.match(r"^(Pause and ask|Ask\.|Say\.|Frame this|Trace the|Give \d+ minutes|End with|Repeat the)\b", stripped):
            i += 1
            continue

        # Accumulate lines into a paragraph
        para_lines = []
        while i < len(lines):
            ln = lines[i]
            st = ln.strip()
            if not st:
                break
            if re.match(r"^(Pause and ask|Ask\.|Say\.|Frame this|Trace the|Give \d+ minutes|End with|Repeat the)\b", st):
                break
            para_lines.append(st)
            i += 1

        if not para_lines:
            continue

        # Merge into flowing paragraph(s)
        merged = merge_to_paragraphs(para_lines)
        output.append(merged)
        output.append("")

    return "\n".join(output).strip()


def merge_to_paragraphs(lines: list[str]) -> str:
    """Merge a list of short lines into one or more fluent paragraphs."""
    if len(lines) == 1:
        return lines[0]

    sentences = []
    current = []

    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        # Single word or very short fragment - attach to prev or next
        words = line.split()
        if len(words) <= 2 and line.endswith(".") and not line[0].islower():
            # "Privacy." or "Costs drop." - might be emphasis
            if current and not current[-1].endswith((".", "!", "?")):
                current.append(line)
            else:
                current.append(line)
            continue

        # Check if this starts a new thought (transition)
        is_transition = (
            line.startswith("Now ") or
            line.startswith("Let's ") or
            (line.startswith("So ") and len(sentences) > 0) or
            (line.startswith("But ") and i > 0 and len(lines) > 3)
        )

        # If we have a good chunk and hit a transition, emit paragraph
        if is_transition and current and len(" ".join(current)) > 150:
            s = join_sentences(current)
            if s:
                sentences.append(s)
            current = [line]
        else:
            current.append(line)

    if current:
        s = join_sentences(current)
        if s:
            sentences.append(s)

    return "\n\n".join(sentences)


def join_sentences(lines: list[str]) -> str:
    """Join lines into coherent sentences and paragraphs."""
    if not lines:
        return ""
    if len(lines) == 1:
        return lines[0]

    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look ahead: can we merge with next?
        if i + 1 < len(lines):
            next_line = lines[i + 1]
            # Fragment (no period, or starts with lowercase) - merge
            if (
                not next_line.endswith((".", "!", "?")) or
                (len(next_line.split()) <= 4 and next_line[0].islower())
            ):
                # Merge current with next
                if line.endswith((".", "!", "?")):
                    combined = line + " " + next_line[0].lower() + next_line[1:] if next_line else line
                else:
                    combined = line + " " + next_line
                result.append(combined)
                i += 2
                continue

            # Short emphatic line - merge with previous or next
            if len(line.split()) <= 3 and line.endswith("."):
                if result and len(result[-1]) < 200:
                    result[-1] = result[-1].rstrip(".") + ", " + line.lower().rstrip(".") + "."
                else:
                    result.append(line)
                i += 1
                continue

        result.append(line)
        i += 1

    # Join sentences with space; break into paras if long
    full = " ".join(result)
    # Clean up double spaces, odd punctuation
    full = re.sub(r"  +", " ", full)
    full = re.sub(r" \.", ".", full)
    full = re.sub(r" ,", ",", full)

    # If very long, split at natural points (~400 chars)
    if len(full) > 500:
        parts = re.split(r"(?<=\.)\s+(?=Now |Let's |So |But )", full)
        if len(parts) > 1:
            return "\n\n".join(p.strip() for p in parts if p.strip())
    return full


SKIP_FILES = {"raw.md", "raw2.md", "raw3.md", "what-ai-is.md", "what-ai-does-well.md", "tradeoffs.md"}


def process_file(filepath: Path) -> bool:
    """Process one file. Returns True if changed."""
    if filepath.name in SKIP_FILES:
        return False
    original = filepath.read_text(encoding="utf-8")

    # Extract frontmatter
    if not original.strip().startswith("---"):
        return False

    parts = original.split("---", 2)
    if len(parts) < 3:
        return False

    frontmatter = "---" + parts[1] + "---"
    body = parts[2].lstrip("\n")

    new_body = flow_transform(frontmatter + "\n\n" + body)
    # Re-extract - flow_transform includes frontmatter in output
    if new_body.startswith("---"):
        idx = new_body.find("---", 3) + 3
        new_body = new_body[idx:].lstrip("\n")

    new_content = frontmatter + "\n\n" + new_body
    if new_content != original:
        filepath.write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    md_files = [f for f in SCRIPT_DIR.rglob("*.md") if f.name not in SKIP_FILES]
    for f in sorted(md_files):
        if process_file(f):
            print(f"Updated: {f.relative_to(SCRIPT_DIR)}")


if __name__ == "__main__":
    main()
