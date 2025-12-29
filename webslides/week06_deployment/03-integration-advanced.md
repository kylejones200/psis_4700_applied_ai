# Week 8 — Integration, Reflection, and Demonstration
Focus: compare methods  
Mini-project presentations

> Integration week ties together concepts from across the course into production-ready systems. You'll package models, design APIs, and implement robust deployment practices.
---

## Course Integration
Connect NLP, CV, chatbots, GenAI, TS, and RAI

> End-to-end pipeline design connects data ingestion, preprocessing, model inference, postprocessing, and result delivery. Each stage needs error handling and monitoring.
---

## Comparative Methods
When to choose which approach and why

> REST API design uses standard HTTP methods (GET, POST, PUT, DELETE), status codes, and JSON formatting. Clear contracts help consumers integrate reliably.
---

## Project Expectations
Clear problem, method, data, ethics, results

> Schema validation with tools like Pydantic ensures requests match expectations before expensive processing. Failing fast on bad inputs saves resources and prevents crashes.
---

## Demo Checklist
Reproducibility, safety, and clarity

> Versioning strategies including URL versioning (/v1/, /v2/) or header-based versioning allow backwards compatibility while evolving APIs.
---

## Communicating Results
Target audience  
Visuals  
Limitations

> Model versioning tracks which model version served which predictions, enabling A/B testing and rollback when new models underperform.
---

## Failure Analysis
What didn't work and lessons learned

> Containerization with Docker ensures consistent environments from development through production, packaging dependencies, code, and model weights together.
---

## Responsible AI Tie-ins
Risks, mitigations, documentation

> Orchestration with Kubernetes scales services based on load, handles failures gracefully, and manages deployments across many containers.
---

## Next Steps
Roadmap to scale or iterate post-course

> Serverless deployments like AWS Lambda or Google Cloud Functions scale automatically and charge only for actual compute used, reducing operational overhead.
---

## Peer Feedback
Structured reviews  
Action items

> Caching strategies store frequent queries and their results, dramatically reducing latency and costs for repeated requests.
---

## Reflection Prompt
Key takeaways and future applications

> Batch versus online inference trade latency for throughput - batch processing handles large volumes efficiently while online serving responds to individual requests quickly.
---

## Comparative Evaluation Matrix
Criteria: accuracy, cost, latency, safety, maintainability

> Load balancing distributes requests across multiple model instances, preventing any single instance from being overwhelmed and improving availability.
---

## Method Selection Playbook
Heuristics for choosing NLP vs CV vs TS vs RAG

> Health checks and readiness probes let orchestrators know if services are running properly and ready to handle traffic, enabling automatic recovery from failures.
---

## Architecture Patterns
Microservices, event-driven, serverless for AI apps

![](images/diagram_integration_approaches.png)

> Monitoring golden signals include latency (how fast?), traffic (how much?), errors (how many failures?), and saturation (how full?). These indicators reveal system health.
---

## Data Contracts
Schemas, validation, ownership, and SLAs

> Structured logging in JSON format enables efficient parsing and analysis. Include request IDs to trace requests through distributed systems.
---

## Experiment Tracking Rollup
Consolidate metrics/artifacts across weeks

> Distributed tracing follows requests across microservices showing where time is spent and where failures occur. Tools like Jaeger or OpenTelemetry instrument code.
---

## Model Registry
Versioning, stages (staging/prod), approvals

> Cost monitoring tracks compute, storage, and bandwidth expenses. Set budget alerts to avoid surprise bills from autoscaling or unexpected traffic spikes.
---

## CI/CD for ML
Tests, lint, data checks, deployment gates

> Security hardening includes HTTPS, authentication (API keys, OAuth), rate limiting to prevent abuse, and input sanitization against injection attacks.
---

## Monitoring Dashboard
KPIs  
Drift  
Safety incidents  
Cost tracking

> Secrets management stores credentials, API keys, and passwords securely. Never hardcode secrets in code or config files committed to version control.
---

## On-call and Runbooks
Alerts, escalation, rollback, comms templates

> Dependency management pins exact versions in requirements.txt or lockfiles ensuring reproducible builds. Use vulnerability scanning to detect outdated packages with known security issues.
---

## Governance Review
Ethics checklist  
Sign-offs  
Documentation

> CI/CD pipelines automate testing, building, and deployment. Pull requests trigger tests, merges to main trigger deployments, reducing manual errors.
---

## Security Basics
Secrets management  
Least privilege  
Dependency scans

> Gradual rollout strategies like canary deployments route small percentages of traffic to new versions while monitoring for issues before full deployment.
---

## Dataset Lifecycle
Collection, labeling, versions, retention policies

> Feature flags enable toggling functionality without code deployment, allowing quick rollback and gradual feature releases to subsets of users.
---

## Human Factors
UX for AI confidence  
Explanations and controls

> Data validation at input checks ranges, types, and business rules. Reject bad data early before it corrupts predictions or causes crashes.
---

## Demo Storytelling
Problem framing  
Narrative arc  
Evidence and limits

> Output validation ensures predictions are reasonable - if a price prediction is negative or a probability exceeds 1.0, something went wrong.
---

## Feedback Incorporation
Prioritize issues  
Track decisions and tradeoffs

> Database integration for features requires efficient queries, caching layers, and circuit breakers that fail gracefully when databases are slow or down.
---

## Roadmap and Risks
Milestones  
Dependencies  
Risk register

> Message queues like RabbitMQ or Kafka decouple services enabling asynchronous processing. Producers add work to queues, consumers process at their own pace.
---

## Funding and Costing
TCO estimates  
Usage-based budgeting

> Webhook integration triggers workflows when events occur, enabling reactive architectures where AI systems respond to external triggers.
---

## Team Roles
Eng, data, PM, design, legal  
RACI overview

> Rate limiting prevents abuse and manages costs by limiting requests per user or API key over time windows. Return 429 status codes when limits are exceeded.
---

## Capstone Rubric
Functionality, rigor, clarity, ethics, professionalism

> Graceful degradation serves reduced functionality when dependencies fail rather than complete outage - maybe return cached predictions or simple baselines.
---

## Final Submission Checklist
Code, README, video, slides, artifacts, model card

> Backpressure mechanisms slow down request acceptance when systems are overloaded, preventing cascading failures from overwhelming downstream services.