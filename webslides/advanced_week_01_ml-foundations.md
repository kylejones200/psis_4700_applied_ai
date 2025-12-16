# Week 1 — Machine Learning Foundations
Focus: scikit-learn on tabular data  
Metrics and evaluation

> This course dives into the technical foundations of machine learning using scikit-learn, focusing on practical implementation with tabular data. You'll learn to build, evaluate, and deploy real ML models using industry-standard tools.
---

## Course Logistics & Goals
8-week accelerated format  
Hands-on labs and reflections

![](images/how-models-learn.png)

> The 8-week accelerated format combines conceptual understanding with hands-on labs. Every week includes practical exercises where you'll write code, train models, and interpret results - learning by doing rather than just reading.
---

## What Is Machine Learning?
Learn patterns from data to make predictions/decisions

> Machine learning is fundamentally about finding patterns in data that let us make predictions or decisions. Instead of programming explicit rules, we show the computer examples and it learns the patterns automatically.
---

## Supervised vs Unsupervised
Supervised: labeled targets  
Unsupervised: structure without labels

> Supervised learning uses labeled data where we know the correct answer, letting the model learn the input-output relationship. Unsupervised learning finds structure in data without predefined labels, useful for discovering natural groupings or patterns.
---

## Typical ML Workflow
Frame problem, gather/clean data, model, evaluate, iterate

> A typical ML workflow follows these steps: clearly define your problem, gather and clean data, choose and train a model, evaluate performance, then iterate to improve. Skipping steps or doing them out of order leads to failed projects.
---

## Tabular Data Focus
Rows=examples  
Columns=features  
Target=label

![](images/training_dataset_size_animation.gif)

> Tabular data is organized in rows (individual examples or observations) and columns (features or characteristics), with one special column as the target (what we're trying to predict). Most business ML still uses this format.
---

## Train/Validation/Test Split
Hold out data to estimate generalization

> Splitting data into training, validation, and test sets prevents over-optimistic performance estimates. The model never sees test data until final evaluation, ensuring honest assessment of how it will perform on new data.
---

## Baselines First
Simple baselines establish a performance floor

> Always establish a simple baseline first - like predicting the most common class or using a simple rule. This performance floor tells you if your complex model is actually adding value or just wasting effort.
---

## Feature Scaling
Standardize/normalize for some models (e.g., kNN, SVM)

> Feature scaling puts all variables on comparable ranges using standardization or normalization. Some models like k-Nearest Neighbors and Support Vector Machines are sensitive to feature scales and won't work properly without this step.
---

## scikit-learn API Basics
Fit(X, y), predict(X), transform(X)

> Scikit-learn's consistent API means most models use the same commands: fit to train, predict to make predictions, and transform for preprocessing. This consistency makes it easy to swap models and compare approaches.
---

## Pipelines in scikit-learn
Chain preprocessing + model for reproducibility

> Pipelines chain preprocessing steps with your model, ensuring they happen in the correct order and can be saved together. This prevents subtle bugs where preprocessing differs between training and deployment.
---

## Cross-Validation
K-fold CV for robust performance estimates

> Cross-validation trains and evaluates your model multiple times on different data splits, then averages results. This k-fold approach gives more reliable performance estimates than a single train/test split that might get lucky or unlucky.
---

## Classification vs Regression
Classification: categorical targets  
Regression: continuous

> Classification predicts categories (spam/not spam, disease present/absent) while regression predicts continuous numbers (price, temperature, count). The model type and evaluation metrics differ between these two fundamental tasks.
---

## Common Models
Logistic Regression, kNN, Decision Trees, Random Forests

> Common models include logistic regression (linear decision boundaries), k-Nearest Neighbors (voting by similarity), decision trees (series of yes/no questions), and random forests (combining many trees). Each has strengths for different problems.
---

## Bias-Variance Tradeoff
Underfit vs overfit  
Complexity control

> The bias-variance tradeoff balances underfitting (model too simple to capture patterns) against overfitting (model memorizes training data including noise). Managing model complexity through regularization and validation is central to good machine learning.
---

## Model Selection
Compare models via CV metrics and simplicity

> Model selection compares different approaches using cross-validation metrics and favors simpler models when performance is similar. A simple model that works is better than a complex one that's harder to explain and maintain.
---

## Metrics: Accuracy & Error Rate
Accuracy = correct/total  
Error = 1 - accuracy

> Accuracy measures overall correctness but can be misleading with imbalanced classes. Error rate is simply one minus accuracy, showing the fraction of mistakes.
---

## Precision & Recall
Precision: positive correctness  
Recall: positive coverage

> Precision asks 'when I predict positive, how often am I correct?' while recall asks 'of all actual positives, how many do I find?' Different applications prioritize different metrics - spam filters care about precision, medical screening cares about recall.
---

## F1 Score
Harmonic mean of precision and recall

> F1 score is the harmonic mean of precision and recall, useful when you need one number that balances both concerns. It's especially helpful for imbalanced datasets where accuracy alone is misleading.
---

## ROC & AUC
Tradeoff across thresholds  
AUC summarizes ranking

> ROC curves plot true positive rate against false positive rate across different thresholds, with AUC (area under curve) summarizing overall ranking ability. Higher AUC indicates better discrimination between classes.
---

## Confusion Matrix
TP, FP, TN, FN breakdown for classification

> Confusion matrices show counts of true positives, false positives, true negatives, and false negatives. This breakdown reveals exactly how your model fails, guiding improvements.
---

## Regression Metrics
MAE, MSE, RMSE, R^2 for continuous targets

> Regression metrics include MAE (mean absolute error), MSE (mean squared error), RMSE (root mean squared error), and R² (proportion of variance explained). Choose metrics that align with your actual costs of being wrong.
---

## Data Leakage
Prevent test info from contaminating training

> Data leakage occurs when test information accidentally influences training, making performance look artificially good. Common causes include preprocessing on all data before splitting or using features that won't be available at prediction time.
---

## Class Imbalance
Use stratification, resampling, or class weights

> Class imbalance (one class much more common than others) requires special handling through stratified splitting, class weights, or resampling techniques. Otherwise your model might just predict the majority class and still appear accurate.
---

## Hyperparameter Tuning
Grid/Random search or Bayes search over params

> Hyperparameter tuning searches over model settings that aren't learned from data. Grid search tries all combinations, random search samples the space more efficiently, and Bayesian approaches use past results to guide future searches.
---

## Regularization
L1/L2 shrinkage to reduce overfitting

> Regularization adds penalties for model complexity, implementing the principle of Occam's razor. L1 regularization can eliminate features entirely while L2 shrinks all weights, both preventing overfitting by fighting the tendency to memorize noise.
---

## Feature Importance
Trees/ensembles provide importance estimates

> Tree-based models like random forests provide feature importance scores showing which variables most influence predictions. This interpretability helps validate that models use sensible information and builds trust with stakeholders.
---

## Evaluation Protocols
Define clear, realistic evaluation aligned to use-case

> Evaluation protocols must align with how the model will actually be used. If predictions are made monthly, use time-aware splits. If data comes from multiple sources, test generalization across sources.
---

## Reproducibility
Fix seeds  
Pin versions  
Save pipelines

> Reproducibility requires fixing random seeds, pinning library versions, and saving complete pipelines. Your results should be replicable by others, which is both a scientific principle and practical necessity for production systems.
---

## Interpretability Basics
Start with simple models  
Use SHAP/LIME if needed

> Interpretability starts with simple models that are inherently explainable. When complex models are necessary, techniques like SHAP and LIME provide post-hoc explanations of predictions.
---

## Practical Lab Preview
Build a pipeline on a tabular dataset  
Report metrics

> The practical lab has you build a complete pipeline on real tabular data and report proper metrics. This hands-on experience cements the concepts and gives you a template for future projects.
---

## Reflection Prompt
Where could ML add value in your domain? Risks?

> Reflection prompts ask you to think critically about ML applications in your domain. Where could automation add value? What could go wrong? Thoughtful consideration now prevents problems later.
---

## Data Cleaning Priorities
Handle missing values, outliers, inconsistent labels first

> Data cleaning priorities include handling missing values (impute or remove?), outliers (errors or real?), and inconsistent labels (which version is correct?). Clean data matters more than fancy algorithms.
---

## Categorical Encoding
One-hot vs target encoding  
Leakage awareness

> Categorical encoding transforms non-numeric categories into numbers. One-hot encoding creates binary columns for each category, while target encoding uses outcome statistics (but risks leakage if done wrong).
---

## Leakage Case Studies
Future info in features  
Post-split preprocessing

> Leakage case studies show common mistakes: using features known only after the event you're predicting, or preprocessing on all data before train/test split. Always ask 'would I really know this when making a prediction?'
---

## Learning Curves
Diagnose under/overfitting by samples vs score

> Learning curves plot performance against training set size, helping diagnose whether you need more data, a more complex model, or better features. Curves reveal whether problems stem from bias (underfitting) or variance (overfitting).
---

## Class Weights
Adjust loss to address imbalance in classifiers

> Class weights adjust the loss function to penalize mistakes on minority classes more heavily. This helps models learn patterns in rare but important cases like fraud detection or disease diagnosis.
---

## Threshold Tuning
Optimize for business objective, not default 0.5

> Threshold tuning means choosing the probability cutoff that best aligns with business objectives rather than using the default 0.5. If false alarms are cheap but misses are expensive, use a lower threshold.
---

## Calibration
Platt/Isotonic to align probabilities with reality

> Calibration ensures predicted probabilities reflect true likelihood of outcomes. Platt scaling and isotonic regression adjust model outputs so that among cases predicted at 70% confidence, roughly 70% are actually positive.
---

## Cost-Sensitive Evaluation
Confusion costs  
Custom utility metrics

> Cost-sensitive evaluation weights errors by their real-world costs. A misdiagnosed disease might cost much more than a false alarm, so metrics should reflect these actual business or human costs.
---

## Model Cards Lite
Document data, metrics, limitations, ethics

> Model cards lite means documenting what data was used, what metrics were achieved, what limitations exist, and what ethical considerations apply. This documentation lives with the model and informs users.
---

## Deployment Basics
Save pipeline  
Input validation  
Version endpoints

> Deployment basics include saving your complete pipeline, validating inputs to catch bad data, and versioning so you can track which model version made which predictions.
---

## Monitoring
Data/label drift  
Performance alerts  
Rollback plans

> Monitoring in production watches for data drift (are inputs changing?), label drift (are outcomes changing?), performance degradation (is accuracy declining?), and sets up alerts with rollback plans when problems arise.
---

## Reading List
Scikit-learn User Guide  
Bishop PRML chapters 1–3

> The reading list includes scikit-learn's comprehensive user guide and foundational chapters from Bishop's Pattern Recognition and Machine Learning textbook. These resources support both practical implementation and theoretical understanding.