# Module 5: Deployment and Operations

## Module Overview

This module addresses what happens after an applied AI system moves beyond a prototype. Students learn how cost, performance, and reliability shape real deployments. The module emphasizes operational thinking and long term ownership.

## Module Learning Objectives

By the end of this module, students can:

1. Identify cost and performance tradeoffs in deployed AI systems.
2. Describe monitoring and maintenance needs for applied AI.
3. Assess vendor and platform risk.

## Lesson 1: Cost and Performance Basics

### Lesson Objective
This lesson supports the objective of identifying cost and performance tradeoffs in deployed AI systems.

### Lesson Overview
Applied AI systems incur ongoing costs. This lesson explains where those costs come from and how performance affects user experience.

### Core Content
Cost follows usage. Inference volume, data storage, and API calls drive expense. Poor design multiplies cost quickly.

Performance affects adoption. Latency frustrates users. Throughput limits scale. Consistency matters more than peak speed.

Tradeoffs appear early. Faster responses often cost more. Cheaper systems require limits.

Good teams estimate cost before deployment and revisit estimates regularly.

### Worked Example
A document assistant limits context size to control token usage and response time.

### Check for Understanding
Students identify cost drivers in short scenarios.

### Required Material
Lesson reading provided in the LMS.

### Optional Enrichment
Cost estimation examples provided in the course repository.

## Lesson 2: Monitoring and Maintenance

### Lesson Objective
This lesson supports the objective of describing monitoring and maintenance needs for applied AI.

### Lesson Overview
Deployed AI systems require care. This lesson explains what to monitor and why.

### Core Content
Monitoring begins with inputs and outputs. Data drift, usage spikes, and error rates signal trouble.

Models age. Data change. Vendors update services. Maintenance keeps systems relevant.

Logs support trust. Alerts enable response. Ownership ensures accountability.

Applied AI succeeds when teams plan for upkeep.

### Worked Example
A prediction service tracks input distributions and flags changes that exceed thresholds.

### Check for Understanding
Students select monitoring signals for a given system.

### Required Material
Lesson reading provided in the LMS.

### Optional Enrichment
Monitoring patterns and examples provided in the course repository.

## Lesson 3: Platform and Vendor Risk

### Lesson Objective
This lesson supports the objective of assessing vendor and platform risk.

### Lesson Overview
Most applied AI depends on external platforms. This lesson examines the risks and responsibilities that follow.

### Core Content
Vendors change pricing, behavior, and availability. Lock in increases exposure.

Portability matters. Clear interfaces reduce dependency. Documentation preserves knowledge.

Risk assessment includes exit plans. Teams decide what happens if a service disappears.

Applied AI design includes vendor awareness from the start.

### Worked Example
A workflow abstracts model calls behind a simple interface. Switching providers remains possible.

### Check for Understanding
Students identify vendor risks and propose mitigation steps.

### Required Material
Lesson reading provided in the LMS.

### Optional Enrichment
Platform comparison notes provided in the course repository.

## Module 5 Assignment: Operational Risk Analysis

### Assignment Overview
Students analyze the operational risks of a deployed applied AI system. The assignment emphasizes foresight and responsibility.

### Assignment Instructions
Students submit a short analysis. The analysis identifies cost drivers, monitoring needs, and vendor risks. Students propose mitigation strategies for each area.

### Assessment Criteria
- Cost and performance tradeoffs are accurately identified.
- Monitoring needs are appropriate and complete.
- Vendor risks are clearly described.
- Mitigation strategies reflect sound judgment.

### Alignment
This assignment assesses Module 5 objectives one and three and Course Learning Outcomes two and five.

## Optional Reading

Selected chapters from *Co-Intelligence* by Ethan Mollick are provided as optional conceptual context. These chapters offer perspectives on how humans and AI work together in practice and are intended to complement, not replace, the applied material in this module.

**Mapped chapters:**
- Chapter 6: AI as a Coworker
- Chapter 8: AI as a Coach

**Rationale:** These chapters emphasize ongoing interaction, feedback, and adjustment, which mirrors operational realities after deployment.

