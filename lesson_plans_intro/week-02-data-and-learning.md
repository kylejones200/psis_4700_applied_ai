# Week 2 — Data and Learning

## Course Learning Outcomes (CLO) Alignment
- **CLO-A**: Define core AI concepts and distinguish between different AI approaches
- **CLO-D**: Apply AI concepts to analyze real-world problems and evaluate solutions
- **CLO-E**: Demonstrate understanding of data requirements and evaluation methods for AI systems

---

## Module 2.1: Types of Learning and Evaluation

### Module Learning Outcomes
- **LO 2.1**: Explain supervised vs unsupervised learning with concrete examples [CLO-A]
- **LO 2.2**: Interpret evaluation metrics (accuracy, precision, recall, F1) and confusion matrices [CLO-E]
- **LO 2.3**: Choose an appropriate metric for a given scenario and justify the choice [CLO-D, CLO-E]

### Required Materials & Resources
- **Required Readings**:
  1. Course slides: `webslides/week02_data-learning/` (60-75 min)
  2. Reference document: `course_materials/reference/simple_sample_dataset.md` (15 min)
  3. Reference document: `course_materials/reference/tidy_data_one_pager.md` (20 min)
  4. Reference document: `course_materials/reference/problem_to_model_examples.md` (20 min)
- **Optional Readings**:
  - "Understanding Machine Learning" - Beginner-friendly article
  - "Evaluation Metrics Explained" - Article on accuracy, precision, recall
- **Interactive Activities**:
  - Confusion matrix calculator (online tool or worksheet provided)
  - Practice exercises with example confusion matrices
- **Videos** (if available):
  - Brief explanation of supervised vs unsupervised learning
  - Walkthrough of evaluation metrics

### Key Vocabulary
- Supervised learning, Unsupervised learning, Features, Labels, Training data, Test data, Accuracy, Precision, Recall, F1 score, Confusion matrix, False positive, False negative

### Learning Activities (Formative - Not Graded)
1. **Self-Study**: Review course slides and reference materials on supervised vs unsupervised learning
2. **Practice Exercises**: Complete worksheet calculating metrics from confusion matrix examples
3. **Reflection**: Consider different scenarios and which metrics would be most important

### Estimated Time to Complete
- Reading and review: 60-75 minutes
- Practice exercises: 45-60 minutes
- Reflection: 30 minutes
- **Total: 2.25-2.75 hours**

---

## Module 2.2: Building and Evaluating a Classifier

### Module Learning Outcomes
- **LO 2.4**: Train and evaluate a simple classifier using an API or tool [CLO-D]
- **LO 2.5**: Interpret model results and identify potential issues [CLO-E]
- **LO 2.6**: Identify and avoid data leakage; understand train/test splits [CLO-E]

### Required Materials & Resources
- **Required Readings**:
  1. Course slides: `webslides/week02_data-learning/` (review relevant sections, 30-45 min)
  2. Reference document: `course_materials/reference/simple_sample_dataset.md` (review, 10 min)
  3. Lab template/worksheet (provided) - Review instructions (15 min)
- **Optional Readings**:
  - scikit-learn User Guide - Model evaluation section (for technical learners)
  - "Understanding Train/Test Splits" - Article on data splitting strategies
- **Interactive Activities**:
  - Python notebook or hosted API for classification (provided template)
  - Dataset (small tabular, e.g., UCI sample or provided dataset)
- **Videos** (if available):
  - Walkthrough of building a simple classifier
  - Demonstration of train/test splits and avoiding data leakage

### Key Vocabulary
- Train/validation/test split, Data leakage, Baseline, Threshold tuning, Class imbalance, Overfitting

### Learning Activities (Formative - Not Graded)
1. **Self-Study**: Review materials on classifier training and evaluation
2. **Hands-On Practice**: Follow along with provided notebook/template to build a simple classifier
3. **Exploration**: Experiment with different train/test splits and observe results

### Estimated Time to Complete
- Reading and review: 45-60 minutes
- Hands-on practice: 60-90 minutes
- Exploration and experimentation: 30-45 minutes
- **Total: 2.25-3.25 hours**

---

## Gradable Activities

### Discussion: Choosing the Right Metric (25 points)
- **Initial Post** (100 words minimum): Describe a scenario from your field where an AI system might be used. Explain which evaluation metric (accuracy, precision, or recall) would be most important and why. What would be worse in your scenario: a false positive or false negative?
- **Reply** (75 words minimum): Respond to one peer's post, either agreeing/disagreeing with their metric choice and providing reasoning, or suggesting an alternative perspective.
- **Due Dates**:
  - Initial post: End of Week 2 (Sunday 11:59 PM)
  - Reply to peer: 48 hours after initial post deadline
- **Evaluation Criteria**:
  - Clear scenario description (30%)
  - Appropriate metric selection with justification (40%)
  - Thoughtful engagement with peers in reply (30%)

### Activity: Classifier Lab (75 points)
- **Task**: Complete a short lab report analyzing a simple classifier
- **Required Sections**:
  1. **Dataset Description** (2-3 sentences): What data did you use? What are you predicting?
  2. **Model Training** (2-3 sentences): What approach did you use? What were your train/test splits?
  3. **Results** (1 paragraph): Report accuracy, precision, and recall. Include a confusion matrix (can be hand-drawn or from tool).
  4. **Analysis** (1 paragraph): What do these metrics tell you? What would be worse in your scenario: false positives or false negatives?
  5. **Reflection** (2-3 sentences): What potential issues (data leakage, class imbalance, etc.) should you watch for?
- **Format**: PDF or Word document, 2 pages maximum
- **Due**: End of Week 2 (Sunday 11:59 PM)
- **Evaluation Criteria**:
  - Complete lab report with all sections (25%)
  - Accurate metric calculations and interpretation (40%)
  - Thoughtful reflection on potential issues (25%)
  - Clear communication and organization (10%)

---

## Instructor Notes
- **Module 2.1**: Emphasize that different metrics matter for different scenarios. Provide visual aids for confusion matrices. Create clear practice exercises.
- **Module 2.2**: Provide both no-code API demo option and code notebook option. Emphasize baseline first; keep data splits honest. Use simple, clean visuals to reduce cognitive load.
- **Differentiation**: Provide domain-specific examples. Offer optional advanced reading on cross-validation and calibration.
- **Asynchronous Considerations**: Provide step-by-step instructions for all activities. Create video walkthroughs or detailed screenshots. Offer multiple pathways (no-code and code options). Set up Q&A forum for technical questions.

## Accessibility & Inclusion
- Provide data tables in accessible formats
- Ensure chart alt text for all visualizations
- Offer alternative formats for lab activities
- Provide clear step-by-step instructions
- Ensure all tools and platforms are accessible

## References
- Course slides: `webslides/week02_data-learning/`
- Reference documents: `course_materials/reference/simple_sample_dataset.md`
- scikit-learn User Guide (model evaluation)
- Introductory ML primers
