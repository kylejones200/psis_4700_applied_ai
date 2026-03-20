# Module 2: Data Reality and Constraints

## Module Overview

This module addresses the limits that real data impose on applied AI projects. Students learn how data availability, quality, and access shape what AI can and cannot do. The module emphasizes judgment and restraint. Students practice deciding when AI fits and when it should not be used.

## Module Learning Objectives

By the end of this module, students can:

1. Evaluate data readiness for applied AI.
2. Identify risks related to data quality, privacy, and access.
3. Decide when AI should not be used.

## Lesson 1: Data Types and Data Limits

### Lesson Objective
This lesson supports the objective of evaluating data readiness for applied AI.

### Lesson Overview
Most workplace data fall short of ideal conditions. This lesson introduces common data types and explains how their limits affect AI design.

### Core Content
Applied AI relies on data that already exist. Structured records, text documents, logs, and time series appear most often. Each type carries constraints that influence model choice and scope.

Quantity matters less than relevance. A small, focused dataset can outperform a large, noisy one. Gaps, bias, and drift reduce reliability.

Labels create friction. Many applied AI systems avoid labeled data by using heuristics, weak signals, or retrieval based approaches.

Good projects begin with an honest inventory of what data exist today.

### Worked Example
A document assistant uses existing reports and emails without labeled examples. Retrieval replaces supervised learning.

### Check for Understanding
Students classify datasets by type and identify likely limitations.

### Required Material
Lesson reading provided in the LMS.

### Optional Enrichment
Sample datasets and exploratory notebooks provided in the course repository.

## Lesson 2: Data Risk and Responsibility

### Lesson Objective
This lesson supports the objective of identifying risks related to data quality, privacy, and access.

### Lesson Overview
Data risk often exceeds model risk. This lesson examines how privacy, security, and access shape applied AI decisions.

### Core Content
Sensitive data introduce legal and ethical obligations. Personal data, regulated records, and proprietary information limit tool choice and deployment options.

Access controls affect feasibility. If data cannot leave a system or cross teams, some approaches fail immediately.

Quality issues hide in plain sight. Missing values, inconsistent definitions, and manual entry errors degrade output.

Responsible applied AI respects data boundaries and designs within them.

### Worked Example
A customer support system masks personal identifiers before processing text. The design reduces exposure and compliance risk.

### Check for Understanding
Students identify data risks in short scenarios and suggest mitigation steps.

### Required Material
Lesson reading provided in the LMS.

### Optional Enrichment
Privacy and governance examples provided in the course repository.

## Lesson 3: When Not to Use AI

### Lesson Objective
This lesson supports the objective of deciding when AI should not be used.

### Lesson Overview
Restraint protects credibility. This lesson teaches students to recognize problems where AI adds cost or risk without benefit.

### Core Content
AI fails when goals lack clarity. It fails when rules already solve the task. It fails when error costs exceed tolerance.

Simple logic often wins. Deterministic systems offer transparency and control. AI adds uncertainty and maintenance overhead.

Saying no reflects professional judgment. Applied AI success includes choosing not to build.

Strong practitioners explain why AI does not fit and propose alternatives.

### Worked Example
A compliance checklist uses rules instead of prediction. The solution remains auditable and stable.

### Check for Understanding
Students evaluate scenarios and decide whether AI fits, explaining their reasoning.

### Required Material
Lesson reading provided in the LMS.

### Optional Enrichment
Decision frameworks and examples provided in the course repository.

## Module 2 Assignment: Data Readiness Assessment

### Assignment Overview
Students assess the data readiness of a proposed applied AI use case. The assignment emphasizes realism and decision quality.

### Assignment Instructions
Students submit a short assessment. The assessment describes available data, identifies gaps and risks, and states whether AI should proceed. If AI does not fit, students propose an alternative approach.

### Assessment Criteria
- Data inventory is accurate and complete.
- Risks related to quality, privacy, and access are clearly identified.
- The recommendation reflects sound judgment.
- The rationale is clear and grounded in constraints.

### Alignment
This assignment assesses Module 2 objectives one and three and Course Learning Outcomes one and two.

## Optional Reading

Selected chapters from *Co-Intelligence* by Ethan Mollick are provided as optional conceptual context. These chapters offer perspectives on how humans and AI work together in practice and are intended to complement, not replace, the applied material in this module.

**Mapped chapter:**
- Chapter 2: Aligning the Alien

**Rationale:** This chapter reinforces the idea that AI behavior reflects training, constraints, and alignment choices. It supports discussion of data quality, limits, and responsibility.

