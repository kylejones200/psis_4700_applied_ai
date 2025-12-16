# Week 6 — Deployment and Integration (STEW-style Lesson Plan)

- Audience: Adult undergraduates (hybrid/online)
- Duration: 3 hours contact + 1–2 hours prep

## Overview
Move from prototypes to simple deployed services. Practice API design, packaging, and lightweight monitoring with attention to cost and security.

## Learning Objectives
- Design a simple API contract and validate inputs.
- Package and deploy a minimal model-backed endpoint.
- Define basic monitoring KPIs and rollback steps.

## Materials & Tools
- Slides: `slides_intro/week-06-deployment-integration.md`
- Minimal API template (FastAPI or equivalent) or notebook-to-web starter
- Example monitoring checklist

## Key Vocabulary
- Endpoint, schema, validation, CI/CD, canary, rollback, observability, SBOM

## Prerequisites
- Weeks 1–5; comfort with simple APIs or notebooks

## Schedule (3:00)
- 0:00–0:10 Recap & goals
- 0:10–0:30 API basics and contract-first design
- 0:30–0:55 Packaging options and env management
- 0:55–1:05 Break
- 1:05–1:35 Live walkthrough: minimal endpoint + validation
- 1:35–2:05 Monitoring & cost: golden signals, budgets
- 2:05–2:35 Group activity: draft API contract + KPIs
- 2:35–2:55 Share-outs; instructor synthesis
- 2:55–3:00 Exit ticket

## Warm-Up (10 min)
- Prompt: “What input would you reject in your app and why?”

## Core Activities
- Contract-first API design; schema validation examples.
- Mini-deploy walkthrough; discuss canary and rollback.
- Group work drafting KPIs and a simple runbook.

## Differentiation
- Provide both a no-code deployment (notebook share) and code template.
- Advanced learners: add a canary step and log sampling.

## Assessment
- Formative: Exit ticket with one KPI and why it matters.
- Summative: Submit a minimal endpoint and a one-page runbook.

## Homework/Prep (60–90 min)
- Polish endpoint; implement one additional validation rule.

## Instructor Notes
- Reinforce privacy and least-privilege in demos.
- Timebox: deployments can run long; pre-stage artifacts.

## Accessibility & Inclusion
- Provide code snippets in accessible text; ensure demo captions.

## References
- FastAPI docs or equivalent; observability primers; CI/CD basics.
