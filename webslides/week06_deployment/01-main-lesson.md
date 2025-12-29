# Week 6 — Deployment and Integration
Focus: prototypes to workflows  
APIs, cloud, MLOps  
Simple deploy

> Moving from prototype notebooks to production systems requires new skills around packaging, deployment, and monitoring. This week bridges the gap between working code and reliable services.
---

## From Notebook to App
Turning prototypes into services

> Turning notebooks into apps means extracting logic into functions, adding proper error handling, and creating interfaces others can use reliably.
---

## API Design Basics
Endpoints, inputs, outputs, status codes

> API design basics include choosing appropriate endpoints (URLs), defining input/output formats, and using standard HTTP status codes to communicate success or failure.
---

## Packaging Models
Save artifacts  
Versioning

> Model packaging means saving trained models and their preprocessing steps, versioning them clearly, and ensuring they can be loaded reliably in production.
---

## CI/CD Basics
Tests, checks, deploy stages

> CI/CD (Continuous Integration/Continuous Deployment) automates testing, checks, and deployment stages to catch problems before they reach users.
---

## Cloud Options
Serverless, containers, managed platforms

> Cloud deployment options include serverless functions (pay per use), containers (consistent environments), and managed platforms (less infrastructure management).
---

## Monitoring
Performance, errors, drift, cost

> Monitoring tracks performance metrics, error rates, data drift, and costs. Problems in production often emerge gradually rather than catastrophically.
---

## Logging and Telemetry
Structured logs  
Privacy considerations

> Logging and telemetry mean structured logs for debugging and privacy considerations for what information gets recorded.
---

## Security Lite
Secrets, authZ/authN, least privilege

> Security lite covers secrets management (never hardcode passwords), authentication (who are you?), authorization (what can you do?), and least privilege (minimum necessary access).
---

## Integration Patterns
Webhooks, queues, batch jobs

![](images/diagram_integration_approaches.png)

> Integration patterns determine how your AI connects to other systems: webhooks for real-time triggers, queues for asynchronous work, and batch jobs for scheduled processing.
---

## Simple Deployment Exercise
Push a minimal API or notebook to a web endpoint

![](images/how-to-vibe-code-an-app.png)

> This exercise walks you through deploying a minimal API or notebook to a web endpoint so it's accessible beyond your local machine.
---

## Reflection Prompt
What integration path fits your project context?

> Consider which integration pattern best fits your project context. Real-time applications need different architectures than daily batch processing.
---

## Packaging Options
Docker images  
Serverless bundles  
Wheels

> Packaging options include Docker images (complete environments), serverless bundles (cloud-specific packages), and Python wheels (library distribution).
---

## Environment Management
Pin dependencies  
Reproducible builds

> Environment management means pinning dependency versions and using isolated environments to ensure reproducible builds across different machines.
---

## Data Contracts
Schemas, validation, versioning

> Data contracts specify schemas (what fields exist), validation rules (what values are valid), and versioning (how changes are communicated).
---

## Input Validation
Pydantic/JSON Schema  
Reject bad requests

> Input validation using tools like Pydantic or JSON Schema catches bad data early and prevents it from crashing your model or producing garbage outputs.
---

## Observability
Traces, metrics, logs  
Golden signals

> Observability combines traces (request paths), metrics (performance numbers), and logs (detailed events) to understand system behavior. The 'golden signals' are latency, traffic, errors, and saturation.
---

## Canary and Rollbacks
Gradual rollout  
Feature flags  
Quick revert

> Canary deployments and rollbacks mean gradually rolling out new versions while monitoring for problems, with feature flags for quick reversion if issues appear.
---

## Cost Awareness
Egress, GPU hours, autoscaling policies

> Cost awareness includes tracking egress bandwidth charges, GPU compute hours, and autoscaling policies that might spend money when you don't expect it.
---

## Security Checklist
Secrets, IAM least privilege, SBOM

> Security checklists cover secrets in environment variables (not code), IAM with least privilege, and software bill of materials (SBOM) to track dependencies.
---

## Data Privacy in Ops
Retention, access controls, anonymization

> Data privacy in operations includes retention policies (how long to keep data), access controls (who can see what), and anonymization (removing identifying information).
---

## DR and Backups
Snapshots, restore drills, RTO/RPO

> Disaster recovery planning includes backup snapshots, practicing restore procedures, and defining recovery time objectives (RTO) and recovery point objectives (RPO).
---

## Post-Deploy Checks
Health, load, quality gates

> Post-deployment checks include health endpoints (is it running?), load testing (can it handle traffic?), and quality gates (is output good enough?).
---

## Mini-Activity
Draft an API contract and monitoring KPIs

> Draft an API contract specifying endpoints, inputs, outputs, and errors, plus monitoring KPIs defining success.
---

## Assignment Brief
Deploy a minimal endpoint  
Include runbook

> Your assignment is deploying a minimal endpoint with a runbook documenting how to operate it, troubleshoot common issues, and roll back if needed.