# Lecture 2
# Data and Models

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Thinking in Data

Applied AI starts with data  
Data defines what models can learn  
Understanding data comes before modeling

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## What Data Represents

Data records observations  
Observations approximate reality  
Approximation introduces error

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Measurement Versus Reality

Sensors miss detail  
Surveys reflect framing  
Logs reflect system design

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Data Is Not Neutral

Choices shape collection  
Context shapes meaning  
Values shape outcomes

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Structured and Unstructured Data

Tables store structured data  
Text and images form unstructured data  
Most applied AI still starts with tables

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Tabular Data Dominates

Businesses record transactions  
Systems log events  
Rows and columns remain common

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Rows and Columns

Rows represent cases  
Columns represent attributes  
Consistency enables learning

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Granularity Matters

Daily totals differ from hourly readings  
Aggregation hides variation  
Resolution shapes insight

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Time Appears Everywhere

Events occur in sequence  
Order affects meaning  
Ignoring time causes error

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Cross Sectional Data

Each row stands alone  
No temporal order exists  
Many classic models assume this form

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Longitudinal Data

Observations repeat over time  
Trends emerge  
Dependence appears

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Panel Data Intuition

Multiple entities evolve over time  
Variation appears across units  
Structure grows complex

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Noise in Data

Random variation exists  
Not every pattern matters  
Models must separate signal from noise

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Missing Values

Data gaps occur naturally  
Systems fail  
People skip responses

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Missingness Matters

Missing values distort learning  
Patterns hide inside absence  
Treatment requires care

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Data Errors

Duplicates appear  
Outliers emerge  
Types mismatch

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Human Assumptions in Data

Labels reflect judgment  
Judgment varies  
Models inherit inconsistency

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Bias Enters Early

Sampling excludes groups  
History embeds inequality  
Data preserves both

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Data Exploration Matters

Summaries reveal shape  
Visuals expose issues  
Exploration prevents surprises

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Simple Questions to Ask

What does each column mean  
How was it collected  
What does it miss

![](images/gas_prices (1).gif)

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Applied Lesson

Models cannot fix bad data  
Understanding precedes prediction  
Data thinking anchors applied AI

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Transition to Features

Raw data rarely feeds models directly  
Features transform information  
Next we examine features and targets

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Features and Targets

Models learn relationships  
Those relationships connect inputs to outcomes  
Clear definitions matter

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## The Target Comes First

Every model answers a question  
The target defines that question  
No target means no model

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## What a Target Represents

Targets encode outcomes  
Outcomes reflect decisions  
Decisions create consequences

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Examples of Targets

Customer churn within thirty days  
House price at sale  
Probability of loan default

> Real-world examples help illustrate how these concepts apply in practice. Pay attention to both successes and failures - both teach valuable lessons about what works and what doesn't.
---

## Classification Targets

Targets represent categories  
Categories encode decisions  
Labels must remain consistent

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Regression Targets

Targets represent numeric values  
Precision matters  
Scale affects learning

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Bad Targets Cause Failure

Ambiguous outcomes confuse models  
Changing definitions break learning  
Noise overwhelms signal

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Features Define What the Model Sees

Features describe cases  
Models see only features  
Omitted information disappears

![](images/causal_inference.gif)

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Raw Data Versus Features

Raw data appears messy  
Features impose structure  
Structure guides learning

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Feature Examples

Account age in days  
Average monthly spend  
Sentiment score from text

> Real-world examples help illustrate how these concepts apply in practice. Pay attention to both successes and failures - both teach valuable lessons about what works and what doesn't.
---

## Derived Features Add Signal

Differences reveal change  
Ratios reveal balance  
Aggregates reveal patterns

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Feature Scaling Intuition

Some features dominate magnitude  
Scaling balances influence  
Learning stabilizes

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Categorical Features

Categories encode groups  
Models require numeric form  
Encoding choices matter

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Encoding Categories

One hot encoding separates groups  
Ordinal encoding implies order  
Assumptions must match reality

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Feature Leakage

Features may reveal the answer  
Leakage inflates performance  
Deployment exposes the failure

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Leakage Example

Using post outcome data  
Using future information  
Using human corrections

> Real-world examples help illustrate how these concepts apply in practice. Pay attention to both successes and failures - both teach valuable lessons about what works and what doesn't.
---

## How to Detect Leakage

Ask when data appears  
Trace feature sources  
Simulate deployment conditions

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Feature Selection Matters

Too many features add noise  
Too few lose signal  
Balance improves generalization

> Feature engineering - creating informative input variables - often matters more than algorithm choice. Good features that capture relevant patterns can make even simple models perform well.
---

## Human Judgment in Features

Features encode assumptions  
Assumptions guide learning  
Reflection reduces harm

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Features and Ethics

Proxy variables hide bias  
Correlation mimics causation  
Design choices matter

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Applied Lesson

Targets define success  
Features define perception  
Careful design prevents failure

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Transition to Models

With features and targets defined,  
Models can learn relationships  
Next we examine regression

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Regression Deep Dive

Regression predicts numeric outcomes  
Many applied AI systems rely on it  
Understanding regression builds intuition for all models

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## What Regression Answers

How much  
How many  
How often

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Everyday Regression Examples

Predict house prices  
Forecast energy demand  
Estimate delivery time

> Real-world examples help illustrate how these concepts apply in practice. Pay attention to both successes and failures - both teach valuable lessons about what works and what doesn't.
---

## Inputs and Outputs

Inputs describe cases  
Outputs represent quantities  
Models map one to the other

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Linear Regression Intuition

Relationships appear as lines  
Lines summarize trends  
Trends guide prediction

![](images/frog-regression-plot-output-1.png)

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Geometry of Linear Regression

Each feature defines a dimension  
The model fits a surface  
Error measures distance from that surface

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Coefficients as Effects

Coefficients weight features  
Signs indicate direction  
Magnitude indicates influence

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Interpreting Coefficients Carefully

Correlation does not imply cause  
Omitted variables distort meaning  
Context defines interpretation

![](images/frog-correlation-plot-output-1.png)

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## The Role of the Intercept

The intercept sets baseline  
Baselines anchor predictions  
Ignoring them misleads

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Loss Functions

Loss measures error  
Squared error penalizes large mistakes  
Optimization minimizes loss

> Loss functions quantify how wrong predictions are, guiding the learning process. Different tasks require different loss functions - squared error for regression, cross-entropy for classification.
---

## Why Squared Error Appears Often

Large errors matter more  
Gradients behave smoothly  
Optimization remains stable

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Residuals

Residuals measure mistakes  
Patterns reveal problems  
Random residuals suggest good fit

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Residual Diagnostics

Trends signal missing features  
Clusters signal nonlinearity  
Outliers demand attention

![](images/frog-regression-diagnostics-output-2.png)

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Assumptions Behind Linear Regression

Linearity  
Independence  
Constant variance  
Normal error distribution

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## When Assumptions Fail

Nonlinear relationships exist  
Variance changes across scale  
Dependencies distort inference

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Practical Impact of Violations

Predictions degrade  
Uncertainty estimates fail  
Trust erodes

> This hands-on exercise gives you practical experience with the concepts we've discussed. Working through examples yourself builds intuition that lectures alone can't provide.
---

## Regularization Intuition

Complex models overfit  
Regularization penalizes complexity  
Bias trades with variance

> Regularization penalizes model complexity to prevent overfitting. By adding costs for large weights or numerous features, regularization encourages simpler models that generalize better.
---

## Ridge Regression

Shrinks coefficients  
Stabilizes estimates  
Handles correlated features

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Lasso Regression

Encourages sparsity  
Selects features  
Simplifies models

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Choosing Regularization

Data size matters  
Noise level matters  
Evaluation guides choice

> Regularization penalizes model complexity to prevent overfitting. By adding costs for large weights or numerous features, regularization encourages simpler models that generalize better.
---

## Regression Metrics

Mean absolute error  
Mean squared error  
Root mean squared error

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Metric Interpretation

Units matter  
Scale affects perception  
Business context defines acceptability

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Common Regression Mistakes

Predicting outside data range  
Ignoring heteroscedasticity  
Overinterpreting coefficients

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Applied Lesson

Regression balances simplicity and power  
Interpretation requires care  
Evaluation protects against misuse

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Transition to Classification

Some questions require categories  
Regression does not suffice  
Next we study classification

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Classification Deep Dive

Classification predicts categories  
Many applied decisions depend on it  
Boundaries separate outcomes

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## What Classification Answers

Yes or no  
Approve or deny  
Normal or anomalous

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Everyday Classification Examples

Spam detection  
Fraud detection  
Medical diagnosis support

> Real-world examples help illustrate how these concepts apply in practice. Pay attention to both successes and failures - both teach valuable lessons about what works and what doesn't.
---

## Inputs and Outputs

Inputs describe cases  
Outputs represent classes  
Probabilities guide decisions

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Binary Classification

Two outcomes exist  
Decisions appear simple  
Consequences vary widely

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Multiclass Classification

More than two categories exist  
Boundaries grow complex  
Interpretation requires care

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Logistic Regression Intuition

Outputs map to probabilities  
Probabilities range from zero to one  
Thresholds convert scores to labels

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Logistic Regression Works Well

Interpretability remains strong  
Training remains stable  
Performance suits many tasks

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Decision Boundaries

Models separate feature space  
Boundaries reflect assumptions  
Data shape determines complexity

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Linear Versus Nonlinear Boundaries

Linear models draw straight lines  
Nonlinear models curve space  
Flexibility trades with stability

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Probabilities Matter More Than Labels

Scores express uncertainty  
Thresholds encode risk tolerance  
Labels hide nuance

> This hands-on exercise gives you practical experience with the concepts we've discussed. Working through examples yourself builds intuition that lectures alone can't provide.
---

## Choosing Thresholds

Default thresholds rarely suffice  
Business cost matters  
Evaluation informs choice

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Confusion Matrix

Predictions meet reality  
Counts summarize outcomes  
Errors reveal tradeoffs

> Confusion matrices break down classification errors into false positives and false negatives. This detailed view reveals exactly how your model fails, guiding targeted improvements.
---

## False Positives

Incorrect positive predictions  
Costs include wasted effort  
Tolerance varies by domain

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## False Negatives

Missed positive cases  
Costs include missed opportunity or harm  
Severity often exceeds false positives

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Accuracy Limits

Class imbalance distorts accuracy  
Trivial models appear strong  
Context matters

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Precision and Recall

Precision measures correctness of positives  
Recall measures coverage of positives  
Tradeoffs appear

> Precision and recall capture different aspects of classifier performance. Precision matters when false alarms are costly, recall matters when misses are dangerous - choose metrics aligned with your actual costs.
---

## Precision Recall Tradeoff

Increasing recall reduces precision  
Increasing precision reduces recall  
Balance depends on stakes

> Precision and recall capture different aspects of classifier performance. Precision matters when false alarms are costly, recall matters when misses are dangerous - choose metrics aligned with your actual costs.
---

## ROC Curves Intuition

Thresholds vary continuously  
Curves summarize discrimination  
Area measures ranking ability

> ROC curves and AUC summarize classifier performance across all possible thresholds. AUC represents the probability that your model ranks a random positive example higher than a random negative example.
---

## Classification Metrics in Practice

No single metric suffices  
Multiple views inform judgment  
Business goals guide selection

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Common Classification Mistakes

Ignoring imbalance  
Using accuracy alone  
Fixating on defaults

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Classification and Bias

Unequal error rates appear  
Groups experience different harm  
Monitoring matters

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Applied Lesson

Classification shapes decisions  
Probabilities deserve attention  
Metrics protect against misuse

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Transition to Evaluation

All models require evaluation  
Evaluation compares choices  
Next we study model evaluation

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Model Evaluation

Models must face reality  
Evaluation tests generalization  
Without evaluation, confidence misleads

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Evaluation Exists

Training performance lies  
Models memorize patterns  
Evaluation reveals truth

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Train Test Split

Data divides into two parts  
Training fits the model  
Testing estimates future performance

> Splitting data into training and test sets is crucial for honest evaluation. Testing on data the model has already seen gives falsely optimistic performance estimates that won't hold in production.
---

## Why Separation Matters

Models remember examples  
Testing on seen data inflates scores  
Separation protects validity

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Common Split Ratios

Seventy thirty appears often  
Eighty twenty appears often  
Data size guides choice

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Random Versus Ordered Splits

Random splits assume independence  
Time ordered data breaks this assumption  
Context determines method

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Cross Validation Intuition

Models train multiple times  
Each fold tests performance  
Averaging stabilizes estimates

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Cross Validation Helps

Single splits vary by chance  
Cross validation reduces noise  
Confidence improves

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Limits of Cross Validation

Time dependence breaks folds  
Large datasets raise cost  
Judgment remains necessary

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Bias and Variance

Bias reflects model simplicity  
Variance reflects sensitivity to data  
Tradeoffs define performance

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Underfitting

Models miss structure  
Errors stay high  
Predictions oversimplify

> Underfitting happens when models are too simple to capture important patterns in data. The model hasn't learned enough from training examples to make useful predictions on anything.
---

## Overfitting

Models chase noise  
Training error drops  
Test error rises

> Overfitting occurs when models memorize training data including noise, failing to generalize to new examples. It's like a student who memorizes answers without understanding concepts - performs perfectly on practice tests but fails on new questions.
---

## Visualizing Bias Variance

Simple models underfit  
Complex models overfit  
Optimal complexity lies between

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Hyperparameters

Hyperparameters shape behavior  
They are not learned automatically  
Search guides selection

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Hyperparameter Search

Grid search tests combinations  
Random search explores efficiently  
Evaluation guides choice

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Metrics Revisited

Regression uses error magnitude  
Classification uses error types  
Metric choice shapes conclusions

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Comparing Models Fairly

Use the same splits  
Use the same metrics  
Control randomness

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Statistical Noise in Scores

Small differences mislead  
Variance matters  
Repeat evaluation

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## When Better Metrics Mislead

Optimization targets metrics  
Metrics miss context  
Decisions require interpretation

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Human Judgment in Evaluation

Numbers inform choices  
Judgment weighs impact  
Context completes analysis

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Evaluation and Ethics

Unequal errors matter  
Aggregate metrics hide harm  
Disaggregated views reveal risk

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Applied Lesson

Evaluation protects credibility  
Metrics guide but do not decide  
Judgment anchors results

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Transition to Practice

With models evaluated,  
We turn to hands on workflow  
Next we review examples and wrap

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Practical Demo and Wrap

Concepts matter when they run  
Practice reveals gaps  
We connect ideas to code

> This hands-on exercise gives you practical experience with the concepts we've discussed. Working through examples yourself builds intuition that lectures alone can't provide.
---

## Demo Goal

Define a clear question  
Prepare data correctly  
Train and evaluate a model

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## The Problem Framing

Predict an outcome from observed features  
Clarify what success means  
Choose regression or classification

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Inspecting the Dataset

Review rows and columns  
Check data types  
Confirm target definition

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Basic Data Cleaning

Handle missing values  
Remove obvious errors  
Confirm reasonable ranges

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Feature and Target Separation

Isolate the target column  
Select relevant features  
Avoid leakage

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Train Test Split in Practice

Hold out unseen data  
Fix random state  
Protect evaluation integrity

> Splitting data into training and test sets is crucial for honest evaluation. Testing on data the model has already seen gives falsely optimistic performance estimates that won't hold in production.
---

## Model Selection

Start with a simple model  
Avoid premature complexity  
Interpret results first

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Training the Model

Fit the model to training data  
Observe training behavior  
Note any warnings

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Generating Predictions

Apply model to test data  
Store predicted values  
Compare against truth

> Named Entity Recognition identifies and classifies mentions of people, organizations, locations, and other entities in text. This structured information extraction enables downstream applications like knowledge graphs.
---

## Evaluating Results

Compute appropriate metrics  
Interpret scale and magnitude  
Ask if results make sense

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Diagnosing Problems

Check residuals or confusion matrix  
Identify patterns in errors  
Question assumptions

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Iterating Thoughtfully

Adjust features if needed  
Avoid tuning blindly  
Re evaluate consistently

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## What This Demo Shows

Modeling follows structure  
Mistakes appear quickly  
Process matters more than tools

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Common Beginner Pitfalls

Training on all data  
Chasing perfect scores  
Ignoring context

> Named Entity Recognition identifies and classifies mentions of people, organizations, locations, and other entities in text. This structured information extraction enables downstream applications like knowledge graphs.
---

## Connecting Back to Concepts

Targets define learning  
Features define perception  
Evaluation defines trust

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Questions to Reflect On

What decision follows prediction  
What happens when the model fails  
Who bears the cost

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Lecture 2 Summary

Data shapes models  
Models require evaluation  
Judgment completes the loop

> This summary reinforces the key concepts from this section. Reviewing main ideas helps consolidate learning and identify areas that need further study.
---

## Looking Ahead

Next we work with text  
Language becomes data  
New challenges appear

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## End of Lecture 2

Pause  
Review notes  
Prepare for NLP

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.