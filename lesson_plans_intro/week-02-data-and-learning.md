# Week 2 — Data and Learning (STEW-style Lesson Plan)

- Audience: Adult undergraduates (hybrid/online)
- Duration: 3 hours contact + 1–2 hours prep

## Overview
Introduce supervised vs unsupervised learning. Build intuition with a tiny classifier via API or scikit-learn. Emphasize evaluation and data ethics.

## Learning Objectives
- Explain supervised vs unsupervised learning with examples.
- Train and evaluate a simple classifier; interpret a confusion matrix.
- Identify and avoid data leakage; choose an appropriate metric.

## Materials & Tools
- Slides: `slides_intro/week-02-data-and-learning.md`
- Python notebook or hosted API for classification demo
- Dataset (small tabular, e.g., UCI sample)

## Key Vocabulary
- Features/labels, train/val/test, accuracy, precision/recall, F1, confusion matrix, class imbalance, leakage

## Prerequisites
- Week 1 concepts; basic spreadsheet or notebook familiarity

## Schedule (3:00)
- 0:00–0:10 Recap & today’s goals
- 0:10–0:30 Supervised vs unsupervised: quick illustrations
- 0:30–0:55 Metrics & confusion matrix
- 0:55–1:10 Break
- 1:10–1:40 Live build: tiny classifier (API or scikit-learn)
- 1:40–2:10 Error analysis & threshold tuning exercise
- 2:10–2:40 Group task: pick metric and justify for a scenario
- 2:40–2:55 Share-outs; instructor synthesis
- 2:55–3:00 Exit ticket

## Warm-Up (10 min)
- Prompt: “What would be worse in your scenario: a false positive or false negative? Why?”

## Core Activities
- Mini-lecture with visuals on supervised/unsupervised.
- Live notebook/API demo to train, predict, and plot confusion matrix.
- Small-group worksheet: calculate precision/recall from a given confusion matrix.

## Differentiation
- Provide a no-code API demo option and a code notebook option.
- Offer optional advanced reading on cross-validation and calibration.

## Assessment
- Formative: Exit ticket naming one metric and why it fits their case.
- Summative: Short lab—train two models and compare metrics; justify threshold.

## Homework/Prep (60–90 min)
- Complete lab; short reflection on leakage risks in their dataset.

## Instructor Notes
- Emphasize baseline first; keep data splits honest.
- Use simple, clean visuals to reduce cognitive load.

## Accessibility & Inclusion
- Provide data tables in accessible formats; ensure chart alt text.

## References
- scikit-learn User Guide (model evaluation); introductory ML primers.
