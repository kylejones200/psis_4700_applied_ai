# Week 7
# Evaluation and Metrics

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## How we measure if an AI system works

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## The Core Idea

AI doesn't "work" because it looks smart  
It works when its outputs match a clear standard  
Metrics make performance visible and comparable

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Accuracy

The simplest metric: correct predictions ÷ total predictions  
Good for classification tasks like spam detection  
Bad for uneven datasets (95% "not spam" looks accurate but isn't)

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Precision and Recall

Two sides of correctness:  
Precision: Of what the model said was true, how much was correct?  
Recall: Of all the true items, how many did it find?  
High precision = careful  
High recall = thorough

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## F1 Score

A balance between precision and recall  
F1 = harmonic mean  
Used when you need both quality and completeness

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Regression Metrics

For numeric predictions:  
MAE (Mean Absolute Error): average absolute gap  
RMSE (Root Mean Square Error): penalizes big misses  
R²: how well predictions match observed data

> Evaluation requires metrics aligned with actual goals beyond just technical accuracy. Consider business outcomes, user satisfaction, fairness across groups, and long-term impacts when assessing success.
---

## Classification Metrics

Confusion Matrix: shows true vs. predicted outcomes  
ROC Curve: visual tradeoff between sensitivity and specificity  
AUC (Area Under Curve): higher = better discrimination

> Evaluation requires metrics aligned with actual goals beyond just technical accuracy. Consider business outcomes, user satisfaction, fairness across groups, and long-term impacts when assessing success.
---

## Generative Models

Traditional metrics struggle  
New measures focus on quality and faithfulness:  
BLEU: compares machine text to human text  
ROUGE: measures overlap  
BERTScore: compares meaning

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Human Evaluation

Still essential  
Humans rate clarity, coherence, tone, and trustworthiness  
For open-ended outputs, human judgment beats math

> Evaluation requires metrics aligned with actual goals beyond just technical accuracy. Consider business outcomes, user satisfaction, fairness across groups, and long-term impacts when assessing success.
---

## Safety and Bias Metrics

Toxicity rate — proportion of unsafe content  
Fairness gaps — how often predictions differ by group  
Explainability — how clearly results can be traced

> AI ethics addresses fairness, accountability, transparency, privacy, and societal impact. Bias can enter at every stage from data collection through deployment, requiring active mitigation throughout the lifecycle.
---

## Business Metrics

Models exist to deliver value  
Track:  
Time saved  
Errors reduced  
Customer satisfaction  
ROI  
If metrics don't tie to outcomes, they don't matter

> Evaluation requires metrics aligned with actual goals beyond just technical accuracy. Consider business outcomes, user satisfaction, fairness across groups, and long-term impacts when assessing success.
---

## Summary

Metrics make models accountable  
Accuracy measures correctness  
Precision and recall measure completeness  
Business metrics measure value  
Good AI is measurable AI

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.