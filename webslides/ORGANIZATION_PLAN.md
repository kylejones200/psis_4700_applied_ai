# Webslides Organization Plan

## Files to Delete (Exact Duplicates) - 5 files

1. `history-of-ai.md` → duplicate of `week01_what-is-ai/04-history-of-ai.md`
2. `flash-boys-and-algorithmic-trading.md` → duplicate of `week01_what-is-ai/08-flash-boys-case-study.md`
3. `ai-dos-and-donts.md` → duplicate of `00_foundations/ai-dos-and-donts.md`
4. `learning-with-ai.md` → duplicate of `week05_gen-convo/16-learning-with-ai.md`
5. `software-eats-the-world.md` → duplicate of `00_foundations/software-eats-the-world.md`

## Files to Move to Existing Folders - 3 files

### reference/
1. `reference_key-terms.md` → `reference/key-terms.md`

### week08_capstone/
2. `capstone_From-Models-to-Meaning.md` → `week08_capstone/02-from-models-to-meaning.md`

### advanced/ (or week04_ethics-policy/)
3. `ai-alignment.md` → `advanced/ai-alignment.md` (different from week04 alignment files)

## Lecture Series - Create lectures_full/ folder - 5 files

These are formal lecture presentations (appears to be a full semester format):
1. `lecture1_What-Is-Applied-AI.md`
2. `lecture2_Data-and-Models.md`
3. `lecture3_Working-with-Text.md`
4. `lecture4_Vision-and-Images.md`
5. `lecture5_AI-in-Business.md`

**Action:** Create `lectures_full/` folder for formal semester lectures

## Week Series - Create another_course/ or technical_course/ folder - 8 files

These appear to be a third complete course curriculum (more technical):
1. `week1_Introduction-to-AI.md`
2. `week2_Regression-and-Classification.md`
3. `week3_Neural-Networks.md`
4. `week4_Natural-Language-Processing.md`
5. `week5_Generative-AI.md`
6. `week6_AI-Ethics-and-Alignment.md`
7. `week7_Applied-AI-Systems.md`
8. `week8_Capstone-and-Reflection.md`

**Action:** Create `technical_course/` folder for technical week-by-week presentations

## Topic Deep-Dives - Create topics/ folder - 16 files

Supplementary deep-dive presentations:
1. `topic_AI-Buzzwords-That-Have-Already-Aged.md`
2. `topic_AI-Frameworks-for-Organizational-Maturity.md`
3. `topic_AI-Ready-Data.md`
4. `topic_AI-as-Building-Blocks.md`
5. `topic_Context-Windows.md`
6. `topic_Embeddings.md`
7. `topic_Fine-Tuning.md`
8. `topic_How-AI-Adds-Value-to-Business.md`
9. `topic_How-Computers-See.md`
10. `topic_Levels-of-AI-Value.md`
11. `topic_Model-Context-Protocol-MCP.md`
12. `topic_Modeling-Has-Changed.md`
13. `topic_The-Statistics-of-AI-Projects.md`
14. `topic_Understanding-Large-Language-Models.md`
15. `topic_Vector-Stores-Yesterday's-Breakthrough.md`
16. `topic_ai_literacy.md`

**Action:** Create `topics/` folder for modular topic presentations

## Week Details - Create weekdetails/ or integrate into topics/ - 15 files

Detailed supplementary content:
1. `weekdetail_AI-Agents-and-Tool-Use.md`
2. `weekdetail_AI-Change-Management.md`
3. `weekdetail_AI-Governance.md`
4. `weekdetail_AI-Maturity-Roadmap.md`
5. `weekdetail_AI-ROI-and-Cost-Models.md`
6. `weekdetail_Edge-and-Private-Models.md`
7. `weekdetail_Ethics-and-Bias-in-AI.md`
8. `weekdetail_Evaluation-and-Metrics.md`
9. `weekdetail_How-Models-Learn.md`
10. `weekdetail_Human-AI-Collaboration.md`
11. `weekdetail_Multi-Model-AI.md`
12. `weekdetail_Multimodal-AI.md`
13. `weekdetail_Retrieval-Augmented-Generation-RAG.md`
14. `weekdetail_The-AI-Lifecycle.md`
15. `weekdetail_Tokens-and-Tokenization.md`

**Action:** Merge into `topics/` folder (rename to remove `weekdetail_` prefix)

## Summary

**Delete:** 5 exact duplicates
**Move to existing folders:** 3 files
**Create lectures_full/:** 5 lecture files
**Create technical_course/:** 8 week files
**Create topics/:** 31 files (16 topic_* + 15 weekdetail_*)

**Result:** 0 files left in webslides root (except READMEs)

## New Folder Structure

```
webslides/
├── 00_foundations/
├── advanced/
├── advanced_course/
├── lectures_full/         # NEW: Formal semester lectures
├── reference/
├── technical_course/      # NEW: Technical curriculum
├── topics/                # NEW: Modular topic presentations (31 files)
├── week01_what-is-ai/
├── week02_data-learning/
├── week03_applications/
├── week04_ethics-policy/
├── week05_gen-convo/
├── week06_deployment/
├── week07_workshop/
└── week08_capstone/
```
