# Week 4 — Conversational AI and Chatbots
Focus: LLM API + simple UI  
Guardrails and evaluation

> Conversational AI and chatbots represent one of the most visible applications of modern NLP. This week you'll build systems that can maintain coherent dialogues while staying safe and helpful.
---

## Conversational Systems Overview
Intents, slots, dialogue management, NLU/NLG

> Conversational systems consist of intents (what user wants), slots (important details), dialogue management (conversation flow), NLU (understanding input), and NLG (generating responses).
---

## LLM-as-Backbone
Use API-driven LLMs to simplify NLU/NLG

> Using LLMs as the backbone simplifies development by handling both understanding and generation in one model. This architectural choice has made sophisticated chatbots accessible to small teams.
---

## Prompt Engineering
Clear roles, constraints, examples  
Test iteratively

> Prompt engineering is crucial for chatbot quality. Define clear roles, specify constraints and behavioral guidelines, provide examples of good responses, and iterate based on real usage.
---

## Retrieval-Augmented Chat
Ground responses with knowledge base docs

> Retrieval-augmented chat grounds responses in a knowledge base rather than relying purely on model memorization. This enables accurate, up-to-date information with source citations.
---

## Memory and Context
Track conversation state  
Summarize to fit context

> Memory and context tracking maintain conversation state across multiple turns. Implement summarization when context exceeds model limits to preserve important information.
---

## Tools and Function Calling
Structured outputs  
Safe tool access

> Tools and function calling enable chatbots to take actions beyond generating text - looking up information, making calculations, or triggering workflows through structured outputs.
---

## UI Prototyping
Simple web/chat UI (e.g., Streamlit) for fast iteration

> UI prototyping with tools like Streamlit lets you quickly iterate on chatbot interfaces. Fast feedback cycles from users improve design more than extended planning.
---

## Guardrails
Content filters  
Deny lists  
Max tool scopes

> Guardrails prevent chatbots from engaging with harmful topics or following dangerous instructions. Implement content filters, topic deny lists, and limit tool access to safe operations.
---

## Safety by Design
Limit PII handling  
Rate limits  
Audit logging

> Safety by design limits PII handling, implements rate limits to prevent abuse, and maintains audit logging for accountability. Build safeguards into architecture rather than adding them later.
---

## Evaluation: Conversations
Task success, coherence, safety, user satisfaction

> Conversational evaluation considers multiple dimensions: did it accomplish the task, was it coherent and natural, did it stay safe, and was the user satisfied?
---

## Hallucination Mitigation
Retrieval, citations, constrained decoding

> Hallucination mitigation uses retrieval for factual grounding, requires citations so users can verify information, and constrains generation to prevent fabrication.
---

## Prompt/Policy Testing
Unit tests for prompts and safety rules

> Prompt and policy testing means unit tests for your prompts and automated safety checks. Treat prompts as code that needs testing, not magic incantations.
---

## Cost Control
Token budgeting  
Caching  
Smaller models when possible

> Cost control involves token budgeting per conversation, caching frequent responses to avoid redundant API calls, and choosing smaller models when they're sufficient.
---

## Latency Reduction
Streaming, partial responses, prefetching

> Latency reduction through streaming shows partial responses immediately, prefetching likely continuations, and architectural optimizations that reduce wait time.
---

## Multi-turn Dialogue
Turn-taking, clarification questions

> Multi-turn dialogue requires tracking context, asking clarification questions when needed, and maintaining coherent conversation flow across many exchanges.
---

## Persona and Tone
Consistent style aligned with brand or use case

> Persona and tone should match your use case and brand. A customer service bot needs different personality than a creative writing assistant.
---

## Analytics
Conversation transcripts  
Metrics dashboards

> Analytics from conversation transcripts and metrics dashboards reveal usage patterns, common questions, failure modes, and opportunities for improvement.
---

## Failure Modes
Off-topic, unsafe, non-determinism  
Design fallbacks

> Failure modes include going off-topic, generating unsafe content, and non-determinism causing inconsistent behavior. Design fallbacks for each failure type.
---

## Human-in-the-Loop
Escalation to experts  
Feedback loops

> Human-in-the-loop systems escalate complex cases to experts and incorporate feedback loops that improve the system over time.
---

## Compliance
Policy alignment  
Data retention  
User consent

> Compliance requires aligning with organizational policies, defining data retention limits, and obtaining user consent for conversation logging.
---

## Practical Lab Preview
Build a chatbot with RAG + safety filters

> The practical lab has you build a chatbot with RAG and safety filters, demonstrating both capability and responsibility.
---

## Reflection Prompt
What guardrails are essential for your chatbot scenario?

> Consider what guardrails are essential for your specific scenario. Medical advice chatbots need different safeguards than creative writing assistants.
---

## Prompt Injection Risks
Detect and neutralize instructions embedded in content

> Prompt injection risks occur when user content contains malicious instructions that override your system prompt. Detect and neutralize embedded commands.
---

## Jailbreak Taxonomy
Common attack patterns  
Layered defenses

> Jailbreak taxonomy documents common attack patterns like roleplay scenarios or encoded instructions. Layered defenses protect against multiple attack vectors.
---

## Safety Evaluation Harness
Red-team prompts  
Automated tests in CI

> Safety evaluation harness includes adversarial red-team prompts and automated safety tests integrated into CI/CD pipelines.
---

## Conversation Memory Design
Excerpts vs summaries  
Privacy and TTL policies

> Conversation memory design chooses between storing excerpts versus summaries, with privacy considerations and time-to-live policies for data retention.
---

## Multilingual Support
Language detection  
Locale-specific rules

> Multilingual support requires language detection and locale-specific rules since acceptable content varies culturally.
---

## Accessibility Considerations
Screen readers  
Concise, clear responses

> Accessibility considerations include screen reader compatibility and concise clear responses that work for users with various abilities.
---

## Analytics Events
Turns, deflections, escalations, CSAT

> Analytics events track conversation turns, deflections to humans, escalations, and customer satisfaction scores for continuous improvement.
---

## A/B Testing Prompts
Compare prompt variants  
Guardrail policies

> A/B testing different prompts and guardrail policies helps optimize the balance between helpfulness and safety.
---

## Fallback Strategies
Apologize, clarify, escalate or retrieve

> Fallback strategies handle failure gracefully: apologize for misunderstanding, ask clarifying questions, offer to escalate, or retrieve relevant documentation.
---

## Telemetry Privacy
Pseudonymization  
Minimize stored content

> Telemetry privacy requires pseudonymization of user identifiers and minimizing stored content to protect privacy.
---

## Logging Schemas
Structured logs  
Redact sensitive fields

> Logging schemas use structured formats with sensitive fields redacted automatically to balance debugging needs with privacy.
---

## Deployment Runbooks
Rollback plans  
Rate limit and quota alarms

> Deployment runbooks document rollback procedures, rate limit thresholds, and quota alarms to respond quickly to problems.
---

## Incident Response
Detection, triage, comms, postmortems

> Incident response procedures define detection, triage, communication protocols, and postmortem analysis to learn from failures.
---

## KPIs and SLOs
Quality, latency, safety metrics and targets

> KPIs and SLOs define success metrics and targets for quality, latency, and safety so teams know if the system is working well.
---

## User Study Design
Tasks, metrics, consent, IRB if applicable

> User study design requires defining tasks, metrics for success, obtaining informed consent, and IRB approval when required for research involving human subjects.