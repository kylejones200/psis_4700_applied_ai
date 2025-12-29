# Media Asset Mapping: GIFs and Images to Lessons

This document maps all GIFs and images to their appropriate lesson/slide deck locations. All files remain in centralized folders for easy management.

---

## Directory Structure

```
/images/                    # 9 renamed descriptive images (main)
/generated_gifs/            # 23 educational GIFs (generated from scripts)
/webslides/images/          # 90 webslide-specific images
```

---

## Week 1: What Is AI?

### Lessons in This Week
- `week01_what-is-ai/01-main-lesson.md`
- `week01_what-is-ai/02-applied-ai-lecture.md`
- `week01_what-is-ai/03-intro-to-ai.md`
- `week01_what-is-ai/04-history-of-ai.md`
- `week01_what-is-ai/05-ai-literacy.md`
- `week01_what-is-ai/06-buzzwords.md`
- `week01_what-is-ai/07-modeling-evolution.md`
- `week01_what-is-ai/08-flash-boys-case-study.md`

### Currently Used Images
- `images/what-is-applied-ai.png` (01-main-lesson, 02-applied-ai-lecture)
- `images/ai_benchmark_progress_smooth.gif` (01-main-lesson)
- `images/AI Models from 1998 to 2023.gif` (02-applied-ai-lecture, 03-intro-to-ai)
- `images/built-in-obsolescence.png` (06-buzzwords)

### Recommended GIF Additions
- **`generated_gifs/algorithmic_trading.gif`** → `08-flash-boys-case-study.md`
  - Shows rule-based trading algorithm with MA crossovers
- **`generated_gifs/latency_race.gif`** → `08-flash-boys-case-study.md`
  - HFT algorithms jumping ahead in microseconds
- **`generated_gifs/flash_crash_path.gif`** → `08-flash-boys-case-study.md`
  - Flash crash scenario with algorithmic chain reactions
- **`generated_gifs/liquidity_vanish.gif`** → `08-flash-boys-case-study.md`
  - Order book thinning during market stress
- **`generated_gifs/hot_potato.gif`** → `08-flash-boys-case-study.md`
  - Contracts bouncing between traders during flash crash
- **`generated_gifs/speed_bump.gif`** → `08-flash-boys-case-study.md`
  - IEX's 350-microsecond speed bump solution

---

## Week 2: Data and Learning

### Lessons in This Week
- `week02_data-learning/01-main-lesson.md`
- `week02_data-learning/02-data-models-lecture.md`
- `week02_data-learning/03-regression-classification.md`
- `week02_data-learning/04-how-models-learn.md`
- `week02_data-learning/05-evaluation-metrics.md`
- `week02_data-learning/06-ai-ready-data.md`
- `week02_data-learning/07-project-statistics.md`

### Currently Used Images
- `images/frog-mean-plot-output-1.png` (01-main-lesson)
- `images/frog-outliers-plot-output-1.png` (01-main-lesson, 06-ai-ready-data)
- `images/gas_prices (1).gif` (02-data-models-lecture)
- `images/causal_inference.gif` (02-data-models-lecture)
- `images/frog-regression-plot-output-1.png` (02, 03)
- `images/frog-correlation-plot-output-1.png` (02)
- `images/frog-regression-diagnostics-output-2.png` (02, 03)
- `images/how-models-learn.png` (04-how-models-learn)
- `images/training_dataset_size_animation.gif` (04-how-models-learn)
- `images/ai-ready-data-with-cat.png` (06-ai-ready-data)
- `images/ai-ready-data-with-unstructured-data.png` (06-ai-ready-data)

### Recommended GIF Additions
- **`generated_gifs/regression_bestfit.gif`** → `03-regression-classification.md`
  - Line rotating to find best fit for scattered data
- **`generated_gifs/clustering_emergence.gif`** → `04-how-models-learn.md`
  - K-means algorithm forming three clusters
- **`generated_gifs/drift_over_time.gif`** → `05-evaluation-metrics.md`
  - Model performance degrading over time
- **`generated_gifs/anomaly_detection.gif`** → `05-evaluation-metrics.md`
  - Highlighting outliers outside normal distribution
- **`generated_gifs/sequence_vs_random.gif`** → `04-how-models-learn.md`
  - Predictable sine wave vs random noise
- **`generated_gifs/forecast_vs_reality.gif`** → `05-evaluation-metrics.md`
  - Predicted values diverging from actual values
- **`generated_gifs/bias_in_training.gif`** → `04-how-models-learn.md`
  - Balanced vs biased training data comparison

---

## Week 3: Applications Across Domains

### Lessons in This Week
- `week03_applications/01-main-lesson.md`
- `week03_applications/02-ai-in-business.md`
- `week03_applications/03-neural-networks.md`
- `week03_applications/04-working-with-text.md`
- `week03_applications/05-vision-and-images.md`
- `week03_applications/06-how-computers-see.md`
- `week03_applications/07-business-value.md`
- `week03_applications/08-value-levels.md`
- `week03_applications/09-roi-cost-models.md`

### Currently Used Images
- Multiple vision/image-related PNGs in `04-working-with-text.md`
- Computer vision images in `05-vision-and-images.md` and `06-how-computers-see.md`
- Business/ROI images in `02-ai-in-business.md` and `09-roi-cost-models.md`

### Recommended GIF Additions
- **`generated_gifs/cost_vs_value.gif`** → `09-roi-cost-models.md`
  - Tradeoff between development cost and business value
- **`generated_gifs/human_in_loop.gif`** → `02-ai-in-business.md`
  - Feedback cycle: Data → Model → Predictions → Human Review
- **`generated_gifs/website_journey_markov.gif`** → `02-ai-in-business.md`
  - E-commerce user journey as Markov chain (Home → Product → Cart → Purchase)

---

## Week 4: Ethics and Policy

### Lessons in This Week
- `week04_ethics-policy/01-main-lesson.md`
- `week04_ethics-policy/02-ethics-alignment.md`
- `week04_ethics-policy/03-alignment-details.md`
- `week04_ethics-policy/04-ethics-bias.md`
- `week04_ethics-policy/05-governance.md`
- `week04_ethics-policy/06-safety-red-teaming.md`
- `week04_ethics-policy/07-data-sovereignty.md`

### Currently Used Images
- Ethics and bias-related images in multiple lessons

### Recommended GIF Additions
- **`generated_gifs/bias_in_training.gif`** → `04-ethics-bias.md`
  - Visual comparison of balanced vs biased training data
- **`generated_gifs/drift_over_time.gif`** → `05-governance.md`
  - Shows need for ongoing monitoring (performance degradation)

---

## Week 5: Generative and Conversational Models

### Lessons in This Week
- `week05_gen-convo/01-main-lesson.md`
- `week05_gen-convo/02-nlp-basics.md`
- `week05_gen-convo/03-generative-ai.md`
- `week05_gen-convo/04-generative-advanced.md`
- `week05_gen-convo/05-understanding-llms.md`
- `week05_gen-convo/06-embeddings.md`
- `week05_gen-convo/07-context-windows.md`
- `week05_gen-convo/08-vector-stores.md`
- `week05_gen-convo/09-tokens-tokenization.md`
- `week05_gen-convo/10-prompt-engineering.md`
- `week05_gen-convo/11-rag-vs-finetuning.md`
- `week05_gen-convo/12-fine-tuning-details.md`
- `week05_gen-convo/13-rag-details.md`
- `week05_gen-convo/14-chatbots-advanced.md`
- `week05_gen-convo/15-multimodal.md`
- `week05_gen-convo/16-learning-with-ai.md`

### Currently Used Images
- RAG-related images in `13-rag-details.md`
- Multimodal images in `15-multimodal.md`

### Recommended GIF Additions
- **`generated_gifs/prompt_refinement.gif`** → `10-prompt-engineering.md`
  - Prompts improving iteratively from basic to detailed
- **`generated_gifs/gpt_translation_meaning.gif`** → `05-understanding-llms.md`
  - English → Meaning space → Spanish translation
- **`generated_gifs/ngrams_context_chunks.gif`** → `09-tokens-tokenization.md` or `07-context-windows.md`
  - Evolution from next-word prediction → N-grams → paragraph chunking
- **`generated_gifs/markov_stage_cloze.gif`** → `05-understanding-llms.md` or `02-nlp-basics.md`
  - Fill-in-the-blank examples (Mary had a little ____)
- **`generated_gifs/text_prediction_chain.gif`** → `05-understanding-llms.md`
  - Next-word prediction as Markov chain (I would like a cup of ____)
- **`generated_gifs/stage_dependent_markov.gif`** → `05-understanding-llms.md`
  - State probabilities evolving in stage-dependent Markov chain

---

## Week 6: Deployment and Integration

### Lessons in This Week
- `week06_deployment/01-main-lesson.md`
- `week06_deployment/02-applied-systems.md`
- `week06_deployment/03-integration-advanced.md`
- `week06_deployment/04-ai-lifecycle.md`
- `week06_deployment/05-edge-private.md`
- `week06_deployment/06-agents-tools.md`
- `week06_deployment/07-multi-model.md`
- `week06_deployment/08-mcp.md`
- `week06_deployment/09-multi-agent-systems.md`
- `week06_deployment/10-future-workflows.md`

### Currently Used Images
- MCP-related images in `08-mcp.md`
- Edge deployment images in `05-edge-private.md`
- Integration architecture images in `03-integration-advanced.md`

### Recommended GIF Additions
- **`generated_gifs/drift_over_time.gif`** → `04-ai-lifecycle.md`
  - Monitoring model performance over time
- **`generated_gifs/human_in_loop.gif`** → `06-agents-tools.md`
  - Human oversight in AI systems

---

## Week 7: Applied Project Workshop

### Lessons in This Week
- `week07_workshop/01-main-lesson.md`
- `week07_workshop/02-change-management.md`
- `week07_workshop/03-maturity-roadmap.md`
- `week07_workshop/04-org-maturity.md`
- `week07_workshop/05-human-ai-collab.md`
- `week07_workshop/06-cognitive-load-ux.md`
- `week07_workshop/07-operating-model.md`

### Currently Used Images
- Maturity framework images in `03-maturity-roadmap.md` and `04-org-maturity.md`
- Human-AI collaboration images in `05-human-ai-collab.md`
- Change management images in `02-change-management.md`

### Recommended GIF Additions
- **`generated_gifs/human_in_loop.gif`** → `05-human-ai-collab.md`
  - Illustrates feedback cycle in human-AI collaboration
- **`generated_gifs/cost_vs_value.gif`** → `01-main-lesson.md`
  - Optimal complexity point for project planning

---

## Week 8: Capstone Presentations

### Lessons in This Week
- `week08_capstone/01-main-lesson.md`
- `week08_capstone/02-capstone-reflection.md`
- `week08_capstone/03-models-to-meaning.md`

### Currently Used Images
- Summary/reflection images in `03-models-to-meaning.md`

### Recommended GIF Additions
- None specific - students will use GIFs from their own projects

---

## GIF Usage Summary by Category

### Flash Boys & Algorithmic Trading (6 GIFs)
All belong in **Week 1: `08-flash-boys-case-study.md`**
- `algorithmic_trading.gif`
- `latency_race.gif`
- `liquidity_vanish.gif`
- `flash_crash_path.gif`
- `hot_potato.gif`
- `speed_bump.gif`

### Markov Chains & Language Models (7 GIFs)
Belong in **Week 5: Generative & Conversational Models**
- `stage_dependent_markov.gif` → `05-understanding-llms.md`
- `markov_stage_cloze.gif` → `05-understanding-llms.md` or `02-nlp-basics.md`
- `text_prediction_chain.gif` → `05-understanding-llms.md`
- `health_states_markov.gif` → `05-understanding-llms.md` (example of Markov processes)
- `website_journey_markov.gif` → **Week 3: `02-ai-in-business.md`** (business application)
- `gpt_translation_meaning.gif` → `05-understanding-llms.md`
- `ngrams_context_chunks.gif` → `09-tokens-tokenization.md` or `07-context-windows.md`

### AI Educational Concepts (10 GIFs)
Distributed across **Week 2, 3, 4, 5, 6, 7**
- `prompt_refinement.gif` → Week 5: `10-prompt-engineering.md`
- `drift_over_time.gif` → Week 2: `05-evaluation-metrics.md` OR Week 6: `04-ai-lifecycle.md`
- `clustering_emergence.gif` → Week 2: `04-how-models-learn.md`
- `regression_bestfit.gif` → Week 2: `03-regression-classification.md`
- `anomaly_detection.gif` → Week 2: `05-evaluation-metrics.md`
- `sequence_vs_random.gif` → Week 2: `04-how-models-learn.md`
- `forecast_vs_reality.gif` → Week 2: `05-evaluation-metrics.md`
- `bias_in_training.gif` → Week 2: `04-how-models-learn.md` AND Week 4: `04-ethics-bias.md`
- `human_in_loop.gif` → Week 3: `02-ai-in-business.md`, Week 6: `06-agents-tools.md`, Week 7: `05-human-ai-collab.md`
- `cost_vs_value.gif` → Week 3: `09-roi-cost-models.md`, Week 7: `01-main-lesson.md`

---

## How to Link GIFs in Markdown

### Relative Path from Week Folders
```markdown
![Description](../../generated_gifs/filename.gif)
```

### Example for Week 1
```markdown
# Flash Boys Case Study

## HFT Latency Advantage

![HFT algorithms can see and jump ahead of orders in microseconds](../../generated_gifs/latency_race.gif)

## Flash Crash Dynamics

![Market crash and recovery showing algorithmic chain reactions](../../generated_gifs/flash_crash_path.gif)
```

### Example for Week 2
```markdown
# Regression and Classification

## Finding the Best Fit

![Line rotating to find best fit for data points](../../generated_gifs/regression_bestfit.gif)
```

---

## Implementation Checklist

- [ ] Week 1: Add 6 Flash Boys GIFs to `08-flash-boys-case-study.md`
- [ ] Week 2: Add 7 educational GIFs across data/learning lessons
- [ ] Week 3: Add business application GIFs to relevant lessons
- [ ] Week 4: Add bias/governance GIFs to ethics lessons
- [ ] Week 5: Add 7 Markov/LLM GIFs across generative model lessons
- [ ] Week 6: Add monitoring GIFs to lifecycle/deployment lessons
- [ ] Week 7: Add collaboration GIFs to workshop lessons
- [ ] Update slide titles/descriptions to reference GIF content
- [ ] Test all GIF links in browser
- [ ] Update GitHub Pages to serve GIFs correctly

---

## Benefits of This Approach

1. **Centralized Management**: All GIFs stay in `/generated_gifs/` for easy regeneration
2. **Clear Mapping**: This document shows exact usage locations
3. **Relative Paths**: Links work locally and on GitHub Pages
4. **Easy Updates**: Regenerate GIF → automatically updates in all lessons that link to it
5. **No Duplication**: Single source of truth for each visual asset
6. **Scalable**: Easy to add new GIFs or update existing ones

---

**Created**: December 29, 2025  
**Status**: Ready for implementation  
**Total GIFs**: 23 (all catalogued and mapped)
**Total Images**: 90+ (in webslides/images) + 9 (in main images folder)
