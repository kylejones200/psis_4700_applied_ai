# Generated GIF Visualizations

All visualizations have been generated from the Python scripts in `/scripts/`. This document provides an index of all GIFs with descriptions.

---

## Flash Boys & Algorithmic Trading (6 GIFs)

### 1. `latency_race.gif`
**Source:** `flash_boys_gifs.py`  
**Description:** Shows how HFT (High-Frequency Trading) algorithms can see investor orders and jump ahead in microseconds. Demonstrates the race between a regular investor order and an HFT order that exploits latency advantages.

### 2. `liquidity_vanish.gif`
**Source:** `flash_boys_gifs.py`  
**Description:** Visualizes how order book depth can thin out rapidly during market stress. Shows bids near the mid-price vanishing during a large sell event, then gradually recovering.

### 3. `flash_crash_path.gif`
**Source:** `flash_boys_gifs.py`  
**Description:** Animated marker following the index price path during a flash crash scenario. Shows how a normal market can turn into a cliff and then snap back, demonstrating algorithmic chain reactions.

### 4. `hot_potato.gif`
**Source:** `flash_boys_gifs.py`  
**Description:** Illustrates how futures contracts bounce between mutual funds, HFT firms, and the rest of the market during a flash crash. Shows the "hot potato" effect where algorithms pass risk back and forth.

### 5. `speed_bump.gif`
**Source:** `flash_boys_gifs.py`  
**Description:** Demonstrates IEX's 350-microsecond speed bump solution. First half shows the baseline race where fast traders win; second half shows how the speed bump equalizes the playing field.

### 6. `algorithmic_trading.gif`
**Source:** `algorithmic_trading_gif.py`  
**Description:** Shows a rule-based trading algorithm using moving averages. Displays buy signals (upward triangles) when price crosses above MA, and sell signals (downward triangles) when price crosses below MA.

---

## Markov Chains & Language Models (7 GIFs)

### 7. `stage_dependent_markov.gif`
**Source:** `markov_chains_learning.py`  
**Description:** Shows how state probabilities evolve in a stage-dependent Markov chain. Three states (S0, S1, S2) with changing transition matrices across different stages. Includes the transition matrix display on the right.

### 8. `markov_stage_cloze.gif`
**Source:** `markov_chains_learning.py`  
**Description:** Fill-in-the-blank examples showing language prediction:
- "Mary had a little ____" → **lamb**
- "United States of ____" → **America**
- "Happy birthday to ____" → **you**

The missing word appears in orange after a pause.

### 9. `text_prediction_chain.gif`
**Source:** `markov_chains_learning.py`  
**Description:** Visualizes next-word prediction as a Markov chain. Shows probability bars for three candidate words (tea, coffee, water) for the phrase "I would like a cup of ____". Probabilities shift toward "coffee" as the chain gains confidence.

### 10. `health_states_markov.gif`
**Source:** `health_and_website_markov.py`  
**Description:** Health state transitions (Healthy → Sick → Recovered) modeled as a Markov process. Shows probability distribution evolving over time with stage-dependent transition matrices favoring recovery in later stages.

### 11. `website_journey_markov.gif`
**Source:** `health_and_website_markov.py`  
**Description:** E-commerce user journey as a Markov chain. A dot moves through states: Home → Product → Cart → Purchase → Exit. Traces the path of a single simulated user session with a line showing the full journey.

### 12. `gpt_translation_meaning.gif`
**Source:** `gpt_translation_meaning.py`  
**Description:** Illustrates GPT-style translation through meaning space. Shows English sentence → Meaning cloud (embeddings) → Spanish sentence. An orange dot travels through the three stages, demonstrating how models convert to semantic representations before generating output.

### 13. `ngrams_context_chunks.gif`
**Source:** `ngrams_context_chunks.py`  
**Description:** Three-phase visualization showing evolution from simple to complex context:
1. **Next-word prediction:** Shows probability bars for candidate words
2. **N-gram context:** Sliding 3-word window highlights context used for prediction
3. **Paragraph chunking:** Demonstrates how models use larger text chunks for understanding topic and meaning

---

## Usage in Slides

All these GIFs can be embedded in your WebSlides presentations:

```markdown
![Description](../generated_gifs/filename.gif)
```

Or in HTML:

```html
<img src="../generated_gifs/filename.gif" alt="Description" style="max-width: 80%;">
```

---

## Regenerating GIFs

To regenerate any GIF, run the corresponding Python script from the `/scripts/` directory:

```bash
cd /path/to/psis_4700_applied_ai/generated_gifs
python ../scripts/script_name.py
```

---

---

## AI Educational Concepts (10 GIFs)

### 14. `prompt_refinement.gif`
**Source:** `ai_educational_gifs.py`  
**Description:** Shows how prompts improve iteratively from basic to detailed, with corresponding quality improvements.

### 15. `drift_over_time.gif`
**Source:** `ai_educational_gifs.py`  
**Description:** Demonstrates model performance degrading over time, crossing below acceptable threshold.

### 16. `clustering_emergence.gif`
**Source:** `ai_educational_gifs.py`  
**Description:** Shows data points forming three distinct clusters with K-means algorithm.

### 17. `regression_bestfit.gif`
**Source:** `ai_educational_gifs.py`  
**Description:** Animates a line rotating to find the best fit for scattered data points.

### 18. `anomaly_detection.gif`
**Source:** `ai_educational_gifs.py`  
**Description:** Highlights outliers outside the normal distribution boundary.

### 19. `sequence_vs_random.gif`
**Source:** `ai_educational_gifs.py`  
**Description:** Compares predictable sine wave pattern against random noise.

### 20. `forecast_vs_reality.gif`
**Source:** `ai_educational_gifs.py`  
**Description:** Shows predicted values diverging from actual values over time.

### 21. `bias_in_training.gif`
**Source:** `ai_educational_gifs.py`  
**Description:** Side-by-side comparison of balanced (50/50) vs biased (80/20) training data.

### 22. `human_in_loop.gif`
**Source:** `ai_educational_gifs.py`  
**Description:** Illustrates the feedback cycle: Data → Model → Predictions → Human Review → Data.

### 23. `cost_vs_value.gif`
**Source:** `ai_educational_gifs.py`  
**Description:** Shows the tradeoff between development cost and business value, highlighting the optimal complexity point.

---

**Total GIFs:** 23  
**Generated:** December 29, 2025
