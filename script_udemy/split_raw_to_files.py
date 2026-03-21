#!/usr/bin/env python3
"""
Parse raw.md and split into individual .md files in script_udemy folder.
Content boundaries derived from Source: and Good. markers in raw.md.
"""

from pathlib import Path

RAW_PATH = Path(__file__).parent / "raw.md"
OUTPUT_BASE = Path(__file__).parent  # script_udemy

# (start_line, end_line, folder, filename) - 1-based inclusive
SECTIONS = [
    # ============ WEEK 1 ============
    (221, 540, "week01_what-is-ai", "08-flash-boys-case-study.md"),
    (551, 1107, "week01_what-is-ai", "07-modeling-evolution.md"),
    (1120, 1840, "week01_what-is-ai", "06-buzzwords.md"),
    (1849, 2021, "week01_what-is-ai", "05-ai-literacy.md"),
    (2029, 2211, "week01_what-is-ai", "04-history-of-ai.md"),
    (2220, 2536, "week01_what-is-ai", "02-applied-ai-lecture.md"),
    (2542, 2785, "week01_what-is-ai", "01-main-lesson.md"),
    # ============ WEEK 2 ============
    (2813, 3047, "week02_data-learning", "07-project-statistics.md"),
    (3049, 3193, "week02_data-learning", "06-ai-ready-data.md"),
    (3201, 3381, "week02_data-learning", "04-how-models-learn.md"),
    (3389, 3613, "week02_data-learning", "03-regression-classification.md"),
    (3621, 3847, "week02_data-learning", "05-evaluation-metrics.md"),
    (3853, 4131, "week02_data-learning", "02-data-models-lecture.md"),
    (4137, 4643, "week02_data-learning", "01-main-lesson.md"),
    # ============ WEEK 3 ============
    (4809, 5116, "week03_applications", "01-main-lesson.md"),
    (5123, 5426, "week03_applications", "02-ai-in-business.md"),
    (5432, 5621, "week03_applications", "03-neural-networks.md"),
    (5432, 5621, "week03_applications", "04-working-with-text.md"),
    (5631, 5882, "week03_applications", "05-vision-and-images.md"),
    (5631, 5882, "week03_applications", "06-how-computers-see.md"),
    (5890, 6158, "week03_applications", "07-business-value.md"),
    (6166, 6414, "week03_applications", "08-value-levels.md"),
    (6424, 6670, "week03_applications", "09-roi-cost-models.md"),
    # ============ WEEK 4 ============
    (6881, 7164, "week04_ethics-policy", "01-main-lesson.md"),
    (7175, 7400, "week04_ethics-policy", "02-ethics-alignment.md"),
    (7409, 7648, "week04_ethics-policy", "03-alignment-details.md"),
    (7657, 7906, "week04_ethics-policy", "04-ethics-bias.md"),
    (7915, 8133, "week04_ethics-policy", "05-governance.md"),
    (8153, 8336, "week04_ethics-policy", "06-safety-red-teaming.md"),
    (8342, 8499, "week04_ethics-policy", "07-data-sovereignty.md"),
    # ============ WEEK 5 ============
    (8839, 9094, "week05_gen-convo", "01-main-lesson.md"),
    (9103, 9286, "week05_gen-convo", "09-tokens-tokenization.md"),
    (9295, 9498, "week05_gen-convo", "10-prompt-engineering.md"),
    (9507, 9720, "week05_gen-convo", "11-rag-vs-finetuning.md"),
    (9727, 9934, "week05_gen-convo", "12-fine-tuning-details.md"),
    (9941, 10136, "week05_gen-convo", "13-rag-details.md"),
    (10145, 10400, "week05_gen-convo", "14-chatbots-advanced.md"),
    (10409, 10606, "week05_gen-convo", "15-multimodal.md"),
    (10615, 10843, "week05_gen-convo", "16-learning-with-ai.md"),
    # ============ WEEK 6 ============
    (11069, 11279, "week06_deployment", "01-main-lesson.md"),
    (11287, 11505, "week06_deployment", "02-applied-systems.md"),
    (11513, 11735, "week06_deployment", "03-integration-advanced.md"),
    (11743, 11961, "week06_deployment", "04-ai-lifecycle.md"),
    (11971, 12177, "week06_deployment", "05-edge-private.md"),
    (12185, 12403, "week06_deployment", "06-agents-tools.md"),
    (12413, 12596, "week06_deployment", "07-multi-model.md"),
    (12606, 12800, "week06_deployment", "08-mcp.md"),
    (12812, 13004, "week06_deployment", "09-multi-agent-systems.md"),
    (13012, 13220, "week06_deployment", "10-future-workflows.md"),
    # ============ WEEK 7 ============
    (13240, 13377, "week07_workshop", "01-main-lesson.md"),
    (13380, 13480, "week07_workshop", "02-change-management.md"),
    (13483, 13545, "week07_workshop", "03-maturity-roadmap.md"),
    (13548, 13586, "week07_workshop", "04-org-maturity.md"),
    (13589, 13647, "week07_workshop", "05-human-ai-collab.md"),
    (13650, 13688, "week07_workshop", "06-cognitive-load-ux.md"),
    (13691, 13791, "week07_workshop", "07-operating-model.md"),
]


def clean_content(text: str) -> str:
    """Remove meta/instructional lines from content."""
    lines = text.split("\n")
    result = []
    skip_patterns = (
        "Good.",
        "Source:",
        "proceed",
        "continue",
        "coninute",
        "ok",
        "Say ",
        "If you want,",
        "Next, we ",
        "Next, I recommend",
        "do main lesson one",
        "remember, flow not lists",
    )
    for line in lines:
        stripped = line.strip()
        if any(stripped.startswith(p) or stripped == p for p in skip_patterns):
            if "Source:" in stripped and len(stripped) < 15:
                continue
        if not stripped and not result:
            continue
        result.append(line)
    while result and not result[-1].strip():
        result.pop()
    return "\n".join(result).strip()


def extract_section(lines: list[str], start: int, end: int) -> str:
    """Extract lines start to end (1-based, inclusive)."""
    return "\n".join(lines[start - 1 : end])


def main():
    if not RAW_PATH.exists():
        print(f"Error: {RAW_PATH} not found")
        return

    content = RAW_PATH.read_text(encoding="utf-8")
    lines = content.split("\n")
    total = len(lines)

    written = set()
    for start, end, folder, filename in SECTIONS:
        if (folder, filename) in written:
            continue
        written.add((folder, filename))
        end = min(end, total)
        extracted = extract_section(lines, start, end)
        cleaned = clean_content(extracted)

        if not cleaned:
            print(f"Skipping empty: {folder}/{filename}")
            continue

        out_dir = OUTPUT_BASE / folder
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / filename

        if not cleaned.strip().startswith("#"):
            title = filename.replace("-", " ").replace(".md", "")
            cleaned = f"# {title}\n\n{cleaned}"

        out_path.write_text(cleaned, encoding="utf-8")
        print(f"Wrote {out_path.relative_to(OUTPUT_BASE.parent)}")


if __name__ == "__main__":
    main()
