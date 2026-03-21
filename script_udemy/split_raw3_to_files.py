#!/usr/bin/env python3
"""
Parse raw3.md and split into individual .md files.
Content: Embeddings/RAG, Hallucinations, Problem framing, Tradeoffs, What AI is/does,
Workflow, ROI, Ethics, Explaining AI, AI shapes life, Future of AI, Week 7, Week 8.
"""

from pathlib import Path

RAW_PATH = Path(__file__).parent / "raw3.md"
OUTPUT_BASE = Path(__file__).parent

# (start_line, end_line, folder, filename) - 1-based inclusive
SECTIONS = [
    # ============ Foundational / cross-cutting ============
    (50, 418, "00_foundations", "embeddings-and-rag.md"),
    (1086, 1215, "00_foundations", "what-ai-is.md"),
    (1216, 1419, "00_foundations", "what-ai-does-well.md"),
    (587, 897, "00_foundations", "problem-framing.md"),
    (898, 1085, "00_foundations", "tradeoffs.md"),
    # ============ Week 4 - Ethics ============
    (419, 586, "week04_ethics-policy", "08-hallucinations.md"),
    # ============ Week 5 - Gen/Convo ============
    # Embeddings moved to 00_foundations; RAG detail in 13-rag-details exists
    # ============ Week 6 - Deployment ============
    (1420, 1725, "week06_deployment", "11-applied-workflow.md"),
    # ============ Week 3 - Applications ============
    (1726, 2024, "week03_applications", "10-roi-business-case.md"),
    # ============ Week 4 - Ethics (continued) ============
    (2025, 2457, "week04_ethics-policy", "09-ethics-bias-fairness-privacy.md"),
    # ============ Supplementary ============
    (2458, 2812, "advanced_course/supplementary", "advanced_Explaining-AI-Outputs.md"),
    # ============ Week 1 - What is AI ============
    (2813, 3237, "week01_what-is-ai", "09-ai-shapes-your-life.md"),
    (3238, 3582, "week06_deployment", "12-future-of-ai-trends.md"),
    # ============ Advanced course - Week 7 & 8 ============
    (3607, 4127, "advanced_course/week07_responsible-ai", "01-main-lesson.md"),
    (4128, 4702, "advanced_course/week08_integration", "01-main-lesson.md"),
]


def clean_content(text: str) -> str:
    """Remove meta lines, Slide:/Script: headers, conversation artifacts."""
    lines = text.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("Slide ") and ":" in stripped:
            continue
        if stripped == "Script:":
            continue
        if stripped in ("Source:", "Good.", "continue", "proceed", "ok", "cotinue"):
            continue
        if "Say " in stripped and "continue" in stripped:
            continue
        if stripped.startswith("If you want") or stripped.startswith("Next,"):
            continue
        if "Just tell me" in stripped or "👍" in stripped:
            continue
        if "Same depth." in stripped or "Same flow." in stripped:
            continue
        if stripped.startswith("👉 "):
            continue
        if "Just say continue" in stripped:
            continue
        if "This completes the full instructor script" in stripped:
            continue
        if "Good. I'll continue" in stripped or "Good. We'll go" in stripped:
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
            title = " ".join(w.capitalize() for w in title.split())
            cleaned = f"# {title}\n\n{cleaned}"

        out_path.write_text(cleaned, encoding="utf-8")
        print(f"Wrote {out_path.relative_to(OUTPUT_BASE.parent)}")


if __name__ == "__main__":
    main()
