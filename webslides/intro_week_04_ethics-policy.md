# Week 4 — Ethics and Policy
Focus: bias, privacy, transparency  
NIST/OECD excerpts  
Mini-debate

> This week introduces AI ethics and policy frameworks. Ethics isn't a separate topic bolted on at the end - it should guide every decision from initial design through deployment.
---

## Why Ethics Now
Societal impact and trust

![](images/chart_ai_concerns.png)

> AI ethics matters because AI systems affect real people's lives at scale. A biased hiring algorithm or unfair credit system can harm thousands before anyone notices the problem.
---

## Core Principles
Fairness, accountability, transparency, privacy, safety

> Five core principles guide responsible AI: fairness (equal treatment), accountability (clear responsibility), transparency (understandable decisions), privacy (data protection), and safety (preventing harm).
---

## Bias Sources
Data collection, labels, modeling, deployment

> Bias can enter at any stage: biased data reflecting historical inequality, biased labels from human prejudices, biased models from improper training, or biased deployment in inequitable contexts.
---

## Fairness Metrics (Intro)
Parity, equalized odds, calibration

> Fairness metrics help quantify bias. Demographic parity asks if outcomes are equal across groups, equalized odds looks at error rates by group, and calibration checks if predictions mean the same thing for everyone.
---

## Transparency
Explainable outputs  
User understanding

> Transparency means users understand when AI is being used, what data it considers, and how decisions are made. 'Black box' AI erodes trust even when technically accurate.
---

## Privacy
Minimization, consent, retention

> Privacy protection starts with minimization (collect only what's needed), requires informed consent (people choose to participate), and limits retention (delete data when no longer necessary).
---

## Security
Access controls, logging, incident response

> Security and privacy overlap: access controls limit who sees data, logging tracks who accessed what, and incident response plans address breaches quickly when they occur.
---

## NIST AI RMF
Map, measure, manage risks

> The NIST AI Risk Management Framework provides a structured approach: map your context, measure risks and impacts, and manage through controls and monitoring.
---

## OECD Principles
Inclusive growth, human-centered values

> OECD AI Principles emphasize inclusive growth (benefits for all), human-centered values (prioritizing people over profit), and responsible stewardship throughout the AI lifecycle.
---

## Policies in Practice
Organizational guidelines and reviews

> Organizational policies translate principles into practice through guidelines that specify requirements, review processes, and consequences for violations.
---

## Data Governance
Ownership, quality, lineage

> Data governance establishes clear ownership (who's responsible), quality standards (what's acceptable), and lineage tracking (where data comes from and where it goes).
---

## Red Teaming
Adversarial testing to find failures

> Red teaming means intentionally trying to break your AI system or make it behave badly. This adversarial testing finds problems before malicious users or accidents do.
---

## Content Safety
Moderation, guardrails, filters

> Content safety requires moderation of inputs and outputs, guardrails that prevent certain behaviors, and filters that block harmful content before it reaches users.
---

## Accessibility
Design for diverse abilities

> Accessibility ensures AI works for everyone, including people with disabilities. Design with diverse users in mind from the start rather than retrofitting later.
---

## Mini-Debate Setup
Motion, teams, rules, timing

> The mini-debate gives you practice arguing both sides of AI ethics issues. Understanding multiple perspectives helps you make more nuanced decisions in real projects.
---

## Debate Evaluation
Clarity, evidence, ethics reasoning

> Debates are evaluated on clarity of argument, use of evidence, and sophisticated reasoning about ethical tradeoffs. There are no simple right answers in AI ethics.
---

## Reflection Prompt
What safeguards are non-negotiable in your project?

> Identify which safeguards are absolutely non-negotiable for your project. Some requirements (like privacy protections for medical data) cannot be compromised regardless of other benefits.
---

## Sensitive Attributes
Direct vs proxy features  
Detection and handling

> Sensitive attributes like race or gender deserve special attention. Even if you don't collect them directly, other features (proxy variables) might correlate with them and lead to discrimination.
---

## Differential Privacy (Intro)
Noise mechanisms  
Privacy budgets (epsilon)

> Differential privacy adds mathematical noise to protect individuals while still enabling useful analysis. The epsilon parameter controls the privacy-utility tradeoff.
---

## Human Oversight
Escalation paths  
Meaningful human control

> Human oversight means building in escalation paths where uncertain cases go to people, and ensuring humans can override AI decisions when needed. AI should augment human judgment, not replace it.
---

## Documentation Artifacts
Datasheets, model cards, system cards

> Documentation artifacts like datasheets (for datasets) and model cards (for models) force teams to think through and communicate important details about their AI systems.
---

## Monitoring in Production
Drift, performance, safety incidents

> Production monitoring tracks not just accuracy but also performance across different user groups, data drift over time, and safety incidents. Problems often emerge gradually after deployment.
---

## Audit Readiness
Logs, decisions, model versions, approvals

> Audit readiness means keeping detailed logs of decisions, model versions, approvals, and changes. When regulators or lawyers come asking questions, documentation is your friend.
---

## Incident Response
Detection, triage, comms, postmortems

> Incident response requires detection (knowing something went wrong), triage (how bad is it?), communication (telling affected parties), and postmortems (learning from mistakes).
---

## Red Teaming Methods
Prompt attacks, adversarial inputs, stress tests

> Red teaming methods include prompt attacks (malicious instructions), adversarial inputs (carefully crafted to fool the model), and stress tests (extreme or unusual situations).
---

## Accessibility by Design
Inclusive UX  
Alt text  
Keyboard navigation

> Accessibility by design considers all users from the start: screen reader compatibility, keyboard navigation, alternative text for images, and clear simple language.
---

## Legal Landscape (Intro)
EU AI Act, sector rules  
Institutional policy

> The legal landscape is evolving rapidly with new AI-specific regulations like the EU AI Act, plus sector-specific rules for healthcare, finance, and other regulated industries.
---

## Mini-Activity
Draft 3 concrete safeguards for your use-case

> Draft three concrete, actionable safeguards specific to your use case. Vague principles like 'be fair' aren't useful - specify exactly what you'll do and measure.
---

## Reading List
NIST AI RMF, OECD, Model Cards, Datasheets

> The readings include the NIST framework, OECD principles, and academic papers on model cards and datasheets. These are foundational documents that policy makers and practitioners reference.
---

## Assignment Brief
1-page risk assessment + safeguard plan

> Your assignment is a one-page risk assessment with a concrete safeguard plan. Brevity forces you to prioritize what really matters rather than listing every possible consideration.