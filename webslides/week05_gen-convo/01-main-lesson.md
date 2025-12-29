# Week 5 — Generative and Conversational Models
Focus: LLMs and image generation  
Build a small chatbot or prompt pipeline

> Generative and conversational AI represent some of the most visible and exciting recent developments in artificial intelligence. This week you'll learn to work with these systems and understand their capabilities and limitations.
---

## Generative Overview
Text, image, audio generation

> Generative AI creates new content (text, images, audio) rather than just analyzing or classifying existing data. This fundamentally changes what's possible with AI, enabling creative applications previously impossible.
---

## LLM Basics
Tokens, prompting, context windows

> Large Language Models (LLMs) process text in chunks called tokens. Context windows limit how much text they can consider at once, affecting applications like long document analysis.
---

## Prompting Patterns
Instructions, examples, constraints

> Effective prompting requires clear instructions, relevant examples, and appropriate constraints. Think of it like delegating to a very capable but literal-minded assistant.
---

## Hallucinations and Grounding
Retrieval augmentation  
Citations

> Hallucinations occur when AI confidently states false information. Retrieval augmentation and citation requirements help ground responses in actual sources rather than fabricated content.
---

## Safety and Moderation
Filter inputs/outputs  
Policies

> Safety and moderation involve filtering both inputs (preventing misuse) and outputs (catching harmful generations). These controls are essential for responsible deployment.
---

## Image Generation Basics
Prompts, seeds, negative prompts

> Text-to-image generation uses prompts to specify desired content, random seeds for reproducibility, and negative prompts to exclude unwanted elements.
---

## Simple Chatbot Plan
Intent, memory, guardrails, UI

> Building a simple chatbot requires planning for intent recognition, maintaining conversation memory, implementing guardrails, and designing a user interface.
---

## Tools and APIs
Provider endpoints  
Rate limits  
Costs

> Commercial APIs provide access to powerful models through endpoints that charge per use. Understanding rate limits and costs helps manage expenses.
---

## Latency and Cost Control
Batching, caching, smaller models

> Control latency through batching requests, caching frequent responses, and choosing smaller models when speed matters more than capability.
---

## Evaluation
Task success, coherence, safety

> Evaluation of conversational systems considers task success (did it help?), coherence (does it make sense?), and safety (did it avoid harmful outputs?).
---

## Demo: Prompt Pipeline
Template + variables + safety checks

> This demo shows how to build a prompt pipeline with variable substitution and safety checks before sending to the model.
---

## Lab Preview
Build a tiny chatbot or prompt pipeline

> Your lab involves building either a small chatbot or a prompt pipeline with clear inputs, processing, and outputs.
---

## Reflection Prompt
What use-case would benefit from a small chatbot?

> Consider what use cases in your field would benefit from conversational AI. Customer service, tutoring, and information lookup are common successful applications.
---

## Prompt Templates
Parameterize slots  
Reuse safely across tasks

> Prompt templates create reusable patterns with placeholders you fill in. This ensures consistency across many similar requests.
---

## Few-shot vs Zero-shot
Trade-offs in quality, tokens, and control

> Zero-shot prompting (no examples) works for common tasks but few-shot prompting (including examples) improves quality and consistency for specific applications.
---

## Function Calling
Structured tool outputs  
Schemas and validation

> Function calling enables structured tool use - the model outputs a specific format you parse to trigger actions like database lookups or API calls.
---

## Memory Design
Short-term context, summaries, user profiles (with consent)

> Memory design choices include short-term context (recent conversation), summaries (compressed history), and user profiles (preferences, but requires consent).
---

## Guardrails
Allow/deny lists  
Regex and classifiers  
Policy tests

> Guardrails include allow/deny lists of topics, regex patterns for filtering, classifiers for content safety, and policy tests that run before deployment.
---

## RAG Lite
Retrieve top-k docs  
Cite sources in answers

> RAG (Retrieval-Augmented Generation) Lite means retrieving the top k most relevant documents and including them in prompts to ground responses in real information.
---

## Evaluation Harness
Golden prompts  
Hallucination/safety checks

> An evaluation harness includes golden test cases with expected outputs, plus specific checks for hallucinations and safety violations.
---

## Image Gen Safety
Filters, blocklists, watermarking

> Image generation safety requires filters for inappropriate content, blocked terms lists, and watermarking to indicate AI-generated content.
---

## Cost Estimation
Tokens per turn  
Monthly budget scenarios

> Estimate costs by calculating tokens per interaction times expected volume per month. Cloud AI services can get expensive at scale.
---

## Latency Budget
P95 targets  
Streaming  
Chunking

> Set latency targets like 'p95 under 2 seconds' (95% of requests complete within 2 seconds), use streaming for immediate feedback, and chunk long outputs.
---

## Mini-Activity
Draft a prompt + 2 test cases  
Define pass criteria

> Draft a prompt and at least two test cases showing desired behavior. Define clear pass/fail criteria so you can evaluate if the system works.
---

## Reading List
Prompt engineering guides  
RAG primers

> Recommended readings cover prompt engineering best practices and RAG system design. These guides come from practitioners at major AI companies.
---

## Assignment Brief
Ship a basic chatbot with 5 guardrail tests

> Ship a basic chatbot with five specific guardrail tests demonstrating it handles edge cases appropriately and avoids prohibited behaviors.