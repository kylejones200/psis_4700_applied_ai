#!/usr/bin/env python3
"""
Parse raw2.md and split into individual .md files.
Output: script_udemy/00_foundations/, script_udemy/advanced_course/
"""

from pathlib import Path

RAW_PATH = Path(__file__).parent / "raw2.md"
OUTPUT_BASE = Path(__file__).parent

# (start_line, end_line, folder, filename) - 1-based inclusive
SECTIONS = [
    # ============ 00_foundations ============
    (26, 100, "00_foundations", "ai-as-building-blocks.md"),
    (103, 186, "00_foundations", "ai-dos-and-donts.md"),
    (190, 313, "00_foundations", "software-eats-the-world.md"),
    # ============ Advanced course (instructor scripts - more complete) ============
    (3768, 3974, "advanced_course/week01_ml-foundations", "01-main-lesson.md"),
    (3982, 4681, "advanced_course/week02_nlp", "01-main-lesson.md"),  # includes continued
    (4739, 5520, "advanced_course/week03_vision", "01-main-lesson.md"),  # includes continued
    (786, 1079, "advanced_course/week06_time-series", "01-main-lesson.md"),
    (1087, 1398, "advanced_course/week07_responsible-ai", "01-main-lesson.md"),
    # ============ Supplementary modules ============
    (1712, 1932, "advanced_course/supplementary", "advanced_RAG-vs-Fine-Tuning.md"),
    (1937, 2069, "advanced_course/supplementary", "advanced_Prompt-Engineering-and-Alignment.md"),
    (2071, 2181, "advanced_course/supplementary", "advanced_Data-Sovereignty-and-Localization.md"),
    (2183, 2279, "advanced_course/supplementary", "advanced_AI-Safety-and-Red-Teaming.md"),
    (2281, 2357, "advanced_course/supplementary", "advanced_Cognitive-Load-and-AI-UX.md"),
    (2359, 2461, "advanced_course/supplementary", "advanced_AI-Agents-and-Multi-Agent-Systems.md"),
    (2463, 2526, "advanced_course/supplementary", "advanced_AI-Operating-Model-for-Organizations.md"),
    (2528, 2772, "advanced_course/supplementary", "advanced_The-Future-of-AI-Workflows.md"),
    # AI Alignment standalone
    (1406, 1706, "advanced_course/supplementary", "advanced_AI-Alignment.md"),
    # Instructor scripts (more detailed - use for week04, week05)
    (5536, 6453, "advanced_course/week04_chatbots", "01-main-lesson.md"),
    (6475, 7088, "advanced_course/week05_generative-ai", "01-main-lesson.md"),
]


def clean_content(text: str) -> str:
    """Remove meta lines, Slide:/Script: headers."""
    lines = text.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("Slide ") and ":" in stripped:
            continue
        if stripped == "Script:":
            continue
        if stripped in ("Source:", "Good.", "continue", "proceed", "ok"):
            continue
        if "Say " in stripped and "continue" in stripped:
            continue
        if stripped.startswith("If you want") or stripped.startswith("Next,"):
            continue
        if "Just tell me" in stripped or "👍" in stripped:
            continue
        result.append(line)
    while result and not result[-1].strip():
        result.pop()
    return "\n".join(result).strip()


def extract_section(lines: list[str], start: int, end: int) -> str:
    return "\n".join(lines[start - 1 : end])


def main():
    if not RAW_PATH.exists():
        print(f"Error: {RAW_PATH} not found")
        return

    content = RAW_PATH.read_text(encoding="utf-8")
    lines = content.split("\n")
    total = len(lines)

    for start, end, folder, filename in SECTIONS:
        end = min(end, total)
        extracted = extract_section(lines, start, end)
        cleaned = clean_content(extracted)

        if not cleaned:
            print(f"Skipping empty: {folder}/{filename}")
            continue

        out_dir = OUTPUT_BASE / folder
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / filename

        if not cleaned.strip().startswith("#") and not cleaned.strip().startswith("---"):
            title = filename.replace("advanced_", "").replace("-", " ").replace(".md", "")
            cleaned = f"# {title}\n\n{cleaned}"

        out_path.write_text(cleaned, encoding="utf-8")
        print(f"Wrote {out_path.relative_to(OUTPUT_BASE.parent)}")


if __name__ == "__main__":
    main()
