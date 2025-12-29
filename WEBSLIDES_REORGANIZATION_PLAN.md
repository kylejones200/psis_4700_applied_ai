# Webslides Reorganization Plan

## Objective
Reorganize all 77 webslide files to align with the 8-week Introduction to Applied AI framework defined in `lesson_plans_intro/`.

## Current Structure Issues
- Multiple naming conventions (intro_week_, week_, lecture_, weekdetail_, topic_, advanced_)
- Duplicate or overlapping content across different file naming schemes
- No clear hierarchy or grouping

## Proposed New Structure

```
webslides/
├── 00_foundations/          # Pre-course and foundational materials
├── week01_what-is-ai/       # Week 1 materials
├── week02_data-learning/    # Week 2 materials
├── week03_applications/     # Week 3 materials
├── week04_ethics-policy/    # Week 4 materials
├── week05_gen-convo/        # Week 5 materials
├── week06_deployment/       # Week 6 materials
├── week07_workshop/         # Week 7 materials
├── week08_capstone/         # Week 8 materials
├── advanced/                # Advanced topics (post-intro)
├── topics/                  # Standalone deep-dive topics
└── reference/               # Reference materials and glossaries
```

---

## Detailed File Mapping

### Week 1: What Is AI?

**Core Lesson**
- `intro_week_01_what-is-ai.md` → `week01_what-is-ai/01-main-lesson.md`

**Supporting Materials**
- `lecture1_What-Is-Applied-AI.md` → `week01_what-is-ai/02-applied-ai-lecture.md`
- `week1_Introduction-to-AI.md` → `week01_what-is-ai/03-intro-to-ai.md`
- `history-of-ai.md` → `week01_what-is-ai/04-history-of-ai.md`
- `topic_ai_literacy.md` → `week01_what-is-ai/05-ai-literacy.md`
- `topic_AI-Buzzwords-That-Have-Already-Aged.md` → `week01_what-is-ai/06-buzzwords.md`
- `topic_Modeling-Has-Changed.md` → `week01_what-is-ai/07-modeling-evolution.md`
- `flash-boys-and-algorithmic-trading.md` → `week01_what-is-ai/08-flash-boys-case-study.md`

---

### Week 2: Data and Learning

**Core Lesson**
- `intro_week_02_data-and-learning.md` → `week02_data-learning/01-main-lesson.md`

**Supporting Materials**
- `lecture2_Data-and-Models.md` → `week02_data-learning/02-data-models-lecture.md`
- `week2_Regression-and-Classification.md` → `week02_data-learning/03-regression-classification.md`
- `weekdetail_How-Models-Learn.md` → `week02_data-learning/04-how-models-learn.md`
- `weekdetail_Evaluation-and-Metrics.md` → `week02_data-learning/05-evaluation-metrics.md`
- `topic_AI-Ready-Data.md` → `week02_data-learning/06-ai-ready-data.md`
- `topic_The-Statistics-of-AI-Projects.md` → `week02_data-learning/07-project-statistics.md`

---

### Week 3: Applications Across Domains

**Core Lesson**
- `intro_week_03_applications.md` → `week03_applications/01-main-lesson.md`

**Supporting Materials**
- `lecture5_AI-in-Business.md` → `week03_applications/02-ai-in-business.md`
- `week3_Neural-Networks.md` → `week03_applications/03-neural-networks.md`
- `lecture3_Working-with-Text.md` → `week03_applications/04-working-with-text.md`
- `lecture4_Vision-and-Images.md` → `week03_applications/05-vision-and-images.md`
- `topic_How-Computers-See.md` → `week03_applications/06-how-computers-see.md`
- `topic_How-AI-Adds-Value-to-Business.md` → `week03_applications/07-business-value.md`
- `topic_Levels-of-AI-Value.md` → `week03_applications/08-value-levels.md`
- `weekdetail_AI-ROI-and-Cost-Models.md` → `week03_applications/09-roi-cost-models.md`

---

### Week 4: Ethics and Policy

**Core Lesson**
- `intro_week_04_ethics-policy.md` → `week04_ethics-policy/01-main-lesson.md`

**Supporting Materials**
- `week6_AI-Ethics-and-Alignment.md` → `week04_ethics-policy/02-ethics-alignment.md`
- `ai-alignment.md` → `week04_ethics-policy/03-alignment-details.md`
- `weekdetail_Ethics-and-Bias-in-AI.md` → `week04_ethics-policy/04-ethics-bias.md`
- `weekdetail_AI-Governance.md` → `week04_ethics-policy/05-governance.md`
- `advanced_AI-Safety-and-Red-Teaming.md` → `week04_ethics-policy/06-safety-red-teaming.md`
- `advanced_Data-Sovereignty-and-Localization.md` → `week04_ethics-policy/07-data-sovereignty.md`

---

### Week 5: Generative and Conversational Models

**Core Lesson**
- `intro_week_05_gen-convo-models.md` → `week05_gen-convo/01-main-lesson.md`

**Supporting Materials**
- `week4_Natural-Language-Processing.md` → `week05_gen-convo/02-nlp-basics.md`
- `week5_Generative-AI.md` → `week05_gen-convo/03-generative-ai.md`
- `advanced_week_05_generative-ai.md` → `week05_gen-convo/04-generative-advanced.md`
- `topic_Understanding-Large-Language-Models.md` → `week05_gen-convo/05-understanding-llms.md`
- `topic_Embeddings.md` → `week05_gen-convo/06-embeddings.md`
- `topic_Context-Windows.md` → `week05_gen-convo/07-context-windows.md`
- `topic_Vector-Stores-Yesterday's-Breakthrough.md` → `week05_gen-convo/08-vector-stores.md`
- `weekdetail_Tokens-and-Tokenization.md` → `week05_gen-convo/09-tokens-tokenization.md`
- `advanced_Prompt-Engineering-and-Alignment.md` → `week05_gen-convo/10-prompt-engineering.md`
- `advanced_RAG-vs-Fine-Tuning.md` → `week05_gen-convo/11-rag-vs-finetuning.md`
- `topic_Fine-Tuning.md` → `week05_gen-convo/12-fine-tuning-details.md`
- `weekdetail_Retrieval-Augmented-Generation-RAG.md` → `week05_gen-convo/13-rag-details.md`
- `advanced_week_04_chatbots.md` → `week05_gen-convo/14-chatbots-advanced.md`
- `weekdetail_Multimodal-AI.md` → `week05_gen-convo/15-multimodal.md`
- `learning-with-ai.md` → `week05_gen-convo/16-learning-with-ai.md`

---

### Week 6: Deployment and Integration

**Core Lesson**
- `intro_week_06_deployment-integration.md` → `week06_deployment/01-main-lesson.md`

**Supporting Materials**
- `week7_Applied-AI-Systems.md` → `week06_deployment/02-applied-systems.md`
- `advanced_week_08_integration.md` → `week06_deployment/03-integration-advanced.md`
- `weekdetail_The-AI-Lifecycle.md` → `week06_deployment/04-ai-lifecycle.md`
- `weekdetail_Edge-and-Private-Models.md` → `week06_deployment/05-edge-private.md`
- `weekdetail_AI-Agents-and-Tool-Use.md` → `week06_deployment/06-agents-tools.md`
- `weekdetail_Multi-Model-AI.md` → `week06_deployment/07-multi-model.md`
- `topic_Model-Context-Protocol-MCP.md` → `week06_deployment/08-mcp.md`
- `advanced_AI-Agents-and-Multi-Agent-Systems.md` → `week06_deployment/09-multi-agent-systems.md`
- `advanced_The-Future-of-AI-Workflows.md` → `week06_deployment/10-future-workflows.md`

---

### Week 7: Applied Project Workshop

**Core Lesson**
- `intro_week_07_project-workshop.md` → `week07_workshop/01-main-lesson.md`

**Supporting Materials**
- `weekdetail_AI-Change-Management.md` → `week07_workshop/02-change-management.md`
- `weekdetail_AI-Maturity-Roadmap.md` → `week07_workshop/03-maturity-roadmap.md`
- `topic_AI-Frameworks-for-Organizational-Maturity.md` → `week07_workshop/04-org-maturity.md`
- `weekdetail_Human-AI-Collaboration.md` → `week07_workshop/05-human-ai-collab.md`
- `advanced_Cognitive-Load-and-AI-UX.md` → `week07_workshop/06-cognitive-load-ux.md`
- `advanced_AI-Operating-Model-for-Organizations.md` → `week07_workshop/07-operating-model.md`

---

### Week 8: Capstone Presentations

**Core Lesson**
- `intro_week_08_capstone.md` → `week08_capstone/01-main-lesson.md`

**Supporting Materials**
- `week8_Capstone-and-Reflection.md` → `week08_capstone/02-capstone-reflection.md`
- `capstone_From-Models-to-Meaning.md` → `week08_capstone/03-models-to-meaning.md`

---

### Foundations (Pre-Course)

**Files**
- `ai-dos-and-donts.md` → `00_foundations/ai-dos-and-donts.md`
- `software-eats-the-world.md` → `00_foundations/software-eats-the-world.md`
- `topic_AI-as-Building-Blocks.md` → `00_foundations/ai-as-building-blocks.md`

---

### Advanced Course Materials

**Advanced Week Files**
- `advanced_week_01_ml-foundations.md` → `advanced/week01_ml-foundations.md`
- `advanced_week_02_nlp.md` → `advanced/week02_nlp.md`
- `advanced_week_03_vision.md` → `advanced/week03_vision.md`
- `advanced_week_06_time-series.md` → `advanced/week06_time-series.md`
- `advanced_week_07_responsible-ai.md` → `advanced/week07_responsible-ai.md`

---

### Reference Materials

**Files**
- `reference_key-terms.md` → `reference/key-terms.md`
- `README.md` → Keep at root level

---

## Implementation Steps

1. **Create new directory structure** (8 week folders + foundations, advanced, reference)
2. **Copy and rename files** according to mapping above
3. **Update internal links** in markdown files to reflect new paths
4. **Update index.html** with new folder structure and navigation
5. **Create README.md in each week folder** explaining contents
6. **Archive old flat structure** files (optional backup)
7. **Test navigation** and links in browser
8. **Update main README** to reference new structure
9. **Commit changes** with clear message

---

## Benefits of New Structure

1. **Clear alignment** with lesson plans
2. **Easier navigation** - week-by-week progression
3. **Better discoverability** - related materials grouped together
4. **Scalable** - easy to add new materials to appropriate weeks
5. **Cleaner separation** - intro vs advanced vs reference vs topics

---

## Notes

- Keep image folder as-is (centralized images work well)
- Some files may fit multiple weeks - use symlinks or cross-references
- Advanced materials remain separate from intro course
- Topics can be referenced from multiple weeks

---

**Status**: Plan created, ready for implementation
**Next**: Begin creating directory structure and moving files
