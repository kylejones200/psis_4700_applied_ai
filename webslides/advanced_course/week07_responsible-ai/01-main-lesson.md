# Week 7 — Responsible and Ethical AI
Focus: SHAP/LIME  
Bias and fairness assessment

> Responsible AI weaves ethics, fairness, transparency, and accountability throughout the AI lifecycle. This advanced treatment examines tools, methods, and frameworks for operationalizing principles.
---

## Why Responsible AI?
Societal impact  
Trust  
Regulation and risk

> Fairness is multifaceted with competing definitions - demographic parity, equalized odds, individual fairness each capture different notions of equity. Choose definitions matching your context and values.
---

## Principles
Fairness, accountability, transparency, privacy, safety

![](images/bias_and_ethics.png)

> Bias sources span data (historical discrimination encoded), labels (annotator prejudices), models (amplifying patterns), and deployment (use in inequitable contexts). Mitigation requires addressing all stages.
---

## Bias Sources
Data, labels, model, deployment context

> Fairness metrics quantify disparities across groups. Test multiple metrics since models can satisfy one fairness constraint while violating others due to mathematical impossibilities of perfect fairness.
---

## Fairness Metrics
Demographic parity, equalized odds, calibration

> Debiasing techniques include preprocessing data (reweighting examples), in-processing (fairness-constrained learning), and postprocessing (threshold adjustments per group).
---

## Interventions
Pre-, in-, post-processing techniques

> Transparency spans model interpretability (understanding internal logic), explainability (explaining specific predictions), and documentation (communicating capabilities and limitations).
---

## Explainability
Local vs global  
Model-agnostic vs specific

> Interpretable models like linear models and shallow decision trees are inherently understandable. Post-hoc explainability methods like SHAP and LIME explain black-box models after training.
---

## LIME
Local linear approximations for instance explanations

> SHAP (SHapley Additive exPlanations) assigns each feature an importance value for a prediction based on game theoretic principles, providing consistent and theoretically grounded explanations.
---

## SHAP
Shapley values for feature contribution

> LIME (Local Interpretable Model-agnostic Explanations) approximates complex models locally with simple interpretable models, explaining individual predictions through local linear approximations.
---

## Limitations of XAI
Approximation errors  
Human misinterpretation

> Model cards document model details, performance across groups, limitations, and intended uses. These standardized fact sheets improve transparency and help users assess appropriateness.
---

## Data Privacy
Minimization  
Anonymization  
Secure storage

> Datasheets for datasets document motivation, composition, collection process, preprocessing, labeling, and distribution. This transparency helps users understand data provenance and limitations.
---

## Human Oversight
Review high-risk cases  
Escalation paths

> Accountability mechanisms establish clear ownership, maintain audit trails, and define escalation paths. When AI makes mistakes, knowing who's responsible and how to remediate is essential.
---

## Documentation
Datasheets, model cards, system cards

> Privacy-preserving techniques include differential privacy (adding calibrated noise), federated learning (training without centralizing data), and homomorphic encryption (computing on encrypted data).
---

## Monitoring in Production
Drift, performance, safety, user feedback

> Differential privacy provides mathematically provable privacy guarantees by adding noise proportional to query sensitivity. The privacy budget parameter epsilon controls the privacy-utility tradeoff.
---

## Red Teaming
Adversarial prompts  
Safety tests  
Incident playbooks

> Adversarial testing (red teaming) probes for failure modes through edge cases, prompt injections, and adversarial examples designed to fool the model. Systematic adversarial evaluation reveals vulnerabilities.
---

## Compliance
NIST AI RMF, OECD, sector-specific rules

> Safety alignment involves RLHF (reinforcement learning from human feedback) to align model behavior with human values and preferences, moving beyond simple accuracy metrics.
---

## Practical Lab Preview
Apply SHAP/LIME  
Compute basic fairness metrics

> Monitoring in production tracks fairness metrics over time, data drift affecting different groups differently, and safety incidents requiring rapid response.
---

## Reflection Prompt
Which fairness metric aligns with your application and why?

> Incident response procedures define detection criteria, triage protocols, communication responsibilities, and postmortem requirements to learn from failures.
---

## Sensitive Attributes
Direct vs proxy features  
Detection and handling

> Regulatory compliance requires understanding evolving frameworks like the EU AI Act, sector-specific rules, and organizational policies that constrain AI deployment.
---

## Dataset Shift and Fairness
Performance parity across time and subgroups

> Ethics review boards and impact assessments evaluate projects before deployment, considering societal implications and stakeholder perspectives beyond just technical metrics.
---

## Causal Perspective
Counterfactual fairness  
Structural causal models

> Stakeholder engagement involves affected communities, domain experts, ethicists, and users in design and evaluation. Diverse perspectives identify risks technical teams might miss.
---

## Fairness-Accuracy Tradeoffs
Clarify objectives  
Multi-objective optimization

> The practical lab implements fairness audits with debiasing techniques and explainability dashboards, demonstrating how to operationalize responsible AI principles.
---

## Documentation Templates
Model cards  
Risk statements  
Change logs

> Reflect on fairness metric tradeoffs in your application. You often can't satisfy all fairness definitions simultaneously - which matters most and why?
---

## Privacy by Design
Minimize data  
Purpose limitation  
Retention

> Model auditing includes testing across demographic groups, geographic regions, and edge cases to find disparate impacts and failure modes.
---

## Differential Privacy
Noise mechanisms  
Privacy budgets (epsilon)

> Fairlearn provides algorithmic fairness tooling including fairness metrics, mitigation algorithms, and interactive dashboards for assessing and addressing disparities.
---

## Federated Learning Basics
Train without centralizing data  
Risks and benefits

> AI Fairness 360 offers comprehensive fairness metrics and algorithms across the pipeline from data preprocessing through postprocessing adjustments.
---

## Human Factors
Avoid over-reliance  
Design for contestability

> Error analysis by subgroups reveals which populations experience higher error rates, guiding targeted improvements and data collection.
---

## Redress Mechanisms
Appeals, corrections, human review processes

> Threshold optimization per group addresses disparate impact by choosing different classification thresholds for different groups to equalize outcomes.
---

## Incident Management
Triage, containment, stakeholder comms, postmortems

> Explainability pitfalls include explanations that are misleading, inconsistent, or highlight spurious correlations. Validate explanations against domain knowledge.
---

## Audits and Assessments
Internal/external audits  
Documentation readiness

> Counterfactual explanations show minimal input changes that would flip predictions, helping users understand decision boundaries and potential recourse.
---

## Regulatory Landscape
EU AI Act, sectoral rules  
Institutional policies

> Human-in-the-loop systems keep humans involved through oversight for high-stakes decisions, active learning for labeling, and feedback loops that improve models.
---

## Reading List
Model Cards  
Datasheets  
NIST AI RMF  
OECD principles

> Privacy-utility tradeoffs mean more privacy (less noise in differential privacy) degrades model utility. Finding acceptable balances requires stakeholder input.
---

## Assignment Brief
Compute fairness metrics  
Propose mitigations and risks

> Federated learning challenges include heterogeneous data distributions across clients, communication costs, and Byzantine robustness against malicious participants.