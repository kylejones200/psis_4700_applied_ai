# Modeling Has Changed
# From Building to Inferring

> Modern AI modeling looks different from traditional machine learning. With powerful pretrained models and transfer learning, we spend less time training models from scratch and more time adapting existing ones.
---

## From building models to inferring from pre-trained ones

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The Old World

We once built models from scratch.  
We gathered our own data.  
We tested many specifications.  
We prized parsimony — the simplest model that explained the data

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Why Parsimony Mattered

Data was scarce.  
Computation was expensive.  
Simplicity avoided overfitting.  
Interpretation was the goal

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The Old Workflow

Define question.  
Collect and clean data.  
Select variables.  
Fit regression or classification.  
Interpret coefficients.  
Validate with holdout data.  
Output: a model tailored to one problem

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The New Reality

We now inherit models, not build them.  
Foundation models already encode broad knowledge.  
We infer, adapt, and ground them.  
The focus shifts from fitting to applying

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The Pre-Trained Paradigm

Model weights come pre-learned from vast datasets.  
We no longer estimate parameters.  
We query representations.  
Inference replaces estimation

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Example: Language

Old: train logistic regression on word frequencies.  
New: query embeddings from GPT or BERT.  
The meaning exists in vector space, not in a coefficient table

> Concrete examples illustrate abstract concepts and show how ideas apply in practice. Pay attention to what made these particular cases succeed or fail.
---

## Example: Vision

Old: train CNN on a small labeled dataset.  
New: call an API that recognizes thousands of classes.  
We focus on how to use, not how to train

> Concrete examples illustrate abstract concepts and show how ideas apply in practice. Pay attention to what made these particular cases succeed or fail.
---

## What This Means for Practice

Data ownership shifts.  
Small teams can do advanced work.  
Model choice becomes model orchestration.  
Governance replaces gradient tuning

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The New Skillset

Prompt design replaces feature selection.  
Context curation replaces data cleaning.  
Evaluation focuses on trust, bias, and reproducibility.  
Deployment manages inference cost and latency

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Inference as the New Science

We test the limits of general models.  
We adapt them to domains.  
We design guardrails and alignment layers

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The Role of Data

We still need our own data.  
Not to fit the model, but to ground it.  
Data now provides context and relevance

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The End of Parsimony

Complexity no longer punishes us.  
Gigantic models outperform hand-tuned ones.  
Interpretability moves to explainers and monitoring tools

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The New Modeling Cycle

Select a foundation model.  
Prepare contextual data.  
Query and evaluate outputs.  
Ground with retrieval or fine-tuning.  
Deploy and monitor inference.  
Output: a living system that learns from feedback

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Closing

We no longer build models  
We converse with them
Our task is not simplicity.  
Our task is alignment, context, and judgment

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.