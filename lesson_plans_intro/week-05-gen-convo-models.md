# Week 5 — Generative and Conversational Models (STEW-style Lesson Plan)

- Audience: Adult undergraduates (hybrid/online)
- Duration: 3 hours contact + 1–2 hours prep

## Overview
Introduce large language models (LLMs) and image generation at a conceptual level. Build a small chatbot or prompt pipeline with basic safety guardrails.

## Learning Objectives
- Explain prompting, context windows, and the idea of grounding.
- Design a simple prompt template and basic evaluation checks.
- Build a tiny chatbot/prompt pipeline and add 3–5 safety checks.

## Materials & Tools
- Slides: `slides_intro/week-05-gen-convo-models.md`
- Hosted LLM API or sandbox; optional vector store starter (RAG-lite)
- Example prompts and evaluation checklist

## Key Vocabulary
- Prompt, context window, hallucination, grounding, moderation, vector store, cosine similarity, alignment

## Prerequisites
- Weeks 1–4 concepts; comfort with basic web/app workflows

## Schedule (3:00)
- 0:00–0:10 Recap & goals
- 0:10–0:35 Mini-lecture: LLMs, prompting patterns, safety basics
- 0:35–1:00 Demo: prompt pipeline with variables and checks
- 1:00–1:10 Break
- 1:10–1:45 Workshop: draft prompts + guardrails in pairs
- 1:45–2:25 Build: tiny chatbot/pipeline (teams)
- 2:25–2:50 Test: run evaluation checklist; fix top issues
- 2:50–3:00 Exit ticket

## Warm-Up (10 min)
- Prompt: “Write a one-sentence instruction to get a concise, factual answer with a citation.”

## Core Activities
- Prompt template construction; few-shot vs zero-shot comparison.
- Add safety checks (content moderation, length limits, refusal tests).
- Optional RAG-lite: retrieve a short doc snippet and cite it.

## Differentiation
- No-code flow for prompt pipelines; code sample for advanced learners.
- Provide starter guardrail tests; invite advanced students to add more.

## Assessment
- Formative: Exit ticket describing one guardrail they implemented.
- Summative: Submit chatbot/pipeline with 5 passing guardrail tests and a short README.

## Homework/Prep (60–90 min)
- Improve prompts and safety; write a short usage guide.

## Instructor Notes
- Keep scope small; emphasize grounded, safe responses over flashy.
- Encourage pairs to review each other’s prompts with the checklist.

## Accessibility & Inclusion
- Ensure UI has clear labels and keyboard navigation; provide captions on any videos.

## References
- Prompt engineering primers; provider safety policies; RAG introductions.
