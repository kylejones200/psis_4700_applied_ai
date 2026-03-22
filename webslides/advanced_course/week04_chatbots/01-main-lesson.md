# Week 4 — Conversational AI and Chatbots
# Focus: LLM API + Simple UI, Guardrails and Evaluation

> Conversational AI and chatbots represent one of the most visible applications of modern NLP. This week you'll build systems that can maintain coherent dialogues while staying safe and helpful.
---

## Conversational Systems Overview

- **Intents:** what the user wants
- **Slots:** important details
- **Dialogue management:** conversation flow
- **NLU:** understanding input
- **NLG:** generating responses

> Conversational systems consist of intents (what user wants), slots (important details), dialogue management (conversation flow), NLU (understanding input), and NLG (generating responses).
---

## LLM-as-Backbone

- Use API-driven LLMs to simplify NLU/NLG
- One model handles both understanding and generation

> Using LLMs as the backbone simplifies development by handling both understanding and generation in one model. This architectural choice has made sophisticated chatbots accessible to small teams.
---

## Prompt Engineering

- Define clear roles
- Specify constraints and behavioral guidelines
- Provide examples of good responses
- Test iteratively

> Prompt engineering is crucial for chatbot quality. Define clear roles, specify constraints and behavioral guidelines, provide examples of good responses, and iterate based on real usage.
---

## Retrieval-Augmented Chat

- Ground responses with knowledge base documents
- Enables accurate, up-to-date information with source citations

> Retrieval-augmented chat grounds responses in a knowledge base rather than relying purely on model memorization. This enables accurate, up-to-date information with source citations.
---

## Memory and Context

- Track conversation state
- Summarize to fit context when limits are exceeded
- Preserve important information across turns

> Memory and context tracking maintain conversation state across multiple turns. Implement summarization when context exceeds model limits to preserve important information.
---

## Tools and Function Calling

- Structured outputs for tool use
- Safe tool access controls
- Enable actions beyond text: lookups, calculations, workflows

> Tools and function calling enable chatbots to take actions beyond generating text - looking up information, making calculations, or triggering workflows through structured outputs.
---

## UI Prototyping

- Simple web/chat UI (e.g., Streamlit) for fast iteration
- Fast feedback cycles from users improve design more than extended planning

> UI prototyping with tools like Streamlit lets you quickly iterate on chatbot interfaces. Fast feedback cycles from users improve design more than extended planning.
---

## Guardrails

- Content filters
- Topic deny lists
- Max tool scopes — limit tool access to safe operations

> Guardrails prevent chatbots from engaging with harmful topics or following dangerous instructions. Implement content filters, topic deny lists, and limit tool access to safe operations.
---

## Safety by Design

- Limit PII handling
- Rate limits to prevent abuse
- Audit logging for accountability
- Build safeguards into architecture rather than adding them later

> Safety by design limits PII handling, implements rate limits to prevent abuse, and maintains audit logging for accountability. Build safeguards into architecture rather than adding them later.
---

## Evaluation: Conversations

- **Task success:** did it accomplish the goal?
- **Coherence:** was it natural and logical?
- **Safety:** did it stay safe?
- **User satisfaction:** was the user satisfied?

> Conversational evaluation considers multiple dimensions: did it accomplish the task, was it coherent and natural, did it stay safe, and was the user satisfied?
---

## Hallucination Mitigation

- Retrieval for factual grounding
- Citations so users can verify information
- Constrained decoding to prevent fabrication

> Hallucination mitigation uses retrieval for factual grounding, requires citations so users can verify information, and constrains generation to prevent fabrication.
---

## Prompt/Policy Testing

- Unit tests for prompts
- Automated safety checks
- Treat prompts as code that needs testing

> Prompt and policy testing means unit tests for your prompts and automated safety checks. Treat prompts as code that needs testing, not magic incantations.
---

## Cost Control

- Token budgeting per conversation
- Caching frequent responses to avoid redundant API calls
- Choose smaller models when sufficient

> Cost control involves token budgeting per conversation, caching frequent responses to avoid redundant API calls, and choosing smaller models when they're sufficient.
---

## Latency Reduction

- Streaming — show partial responses immediately
- Prefetching likely continuations
- Architectural optimizations that reduce wait time

> Latency reduction through streaming shows partial responses immediately, prefetching likely continuations, and architectural optimizations that reduce wait time.
---

## Multi-turn Dialogue

- Track context across turns
- Ask clarification questions when needed
- Maintain coherent conversation flow across many exchanges

> Multi-turn dialogue requires tracking context, asking clarification questions when needed, and maintaining coherent conversation flow across many exchanges.
---

## Persona and Tone

- Consistent style aligned with brand or use case
- Customer service bot needs different personality than a creative writing assistant

> Persona and tone should match your use case and brand. A customer service bot needs different personality than a creative writing assistant.
---

## Analytics

- Conversation transcripts
- Metrics dashboards
- Reveal usage patterns, common questions, failure modes, and improvement opportunities

> Analytics from conversation transcripts and metrics dashboards reveal usage patterns, common questions, failure modes, and opportunities for improvement.
---

## Failure Modes

- Off-topic responses
- Unsafe content generation
- Non-determinism causing inconsistent behavior
- Design fallbacks for each failure type

> Failure modes include going off-topic, generating unsafe content, and non-determinism causing inconsistent behavior. Design fallbacks for each failure type.
---

## Human-in-the-Loop

- Escalation to experts for complex cases
- Feedback loops that improve the system over time

> Human-in-the-loop systems escalate complex cases to experts and incorporate feedback loops that improve the system over time.
---

## Compliance

- Policy alignment with organizational standards
- Data retention limits
- User consent for conversation logging

> Compliance requires aligning with organizational policies, defining data retention limits, and obtaining user consent for conversation logging.
---

## Prompt Injection Risks

- Detect instructions embedded in user content
- Neutralize malicious commands that override system prompt

> Prompt injection risks occur when user content contains malicious instructions that override your system prompt. Detect and neutralize embedded commands.
---

## Jailbreak Taxonomy

- Document common attack patterns (e.g., roleplay scenarios, encoded instructions)
- Layered defenses protect against multiple attack vectors

> Jailbreak taxonomy documents common attack patterns like roleplay scenarios or encoded instructions. Layered defenses protect against multiple attack vectors.
---

## Safety Evaluation Harness

- Adversarial red-team prompts
- Automated safety tests integrated into CI/CD pipelines

> Safety evaluation harness includes adversarial red-team prompts and automated safety tests integrated into CI/CD pipelines.
---

## Conversation Memory Design

- **Excerpts vs. summaries:** choose storage approach
- Privacy considerations
- Time-to-live (TTL) policies for data retention

> Conversation memory design chooses between storing excerpts versus summaries, with privacy considerations and time-to-live policies for data retention.
---

## Multilingual Support

- Language detection
- Locale-specific rules
- Acceptable content varies culturally

> Multilingual support requires language detection and locale-specific rules since acceptable content varies culturally.
---

## Accessibility Considerations

- Screen reader compatibility
- Concise, clear responses
- Work for users with various abilities

> Accessibility considerations include screen reader compatibility and concise clear responses that work for users with various abilities.
---

## Analytics Events

- Conversation turns
- Deflections to humans
- Escalations
- Customer satisfaction (CSAT) scores

> Analytics events track conversation turns, deflections to humans, escalations, and customer satisfaction scores for continuous improvement.
---

## A/B Testing Prompts

- Compare prompt variants
- Compare guardrail policies
- Optimize balance between helpfulness and safety

> A/B testing different prompts and guardrail policies helps optimize the balance between helpfulness and safety.
---

## Fallback Strategies

- Apologize for misunderstanding
- Ask clarifying questions
- Offer to escalate
- Retrieve relevant documentation

> Fallback strategies handle failure gracefully: apologize for misunderstanding, ask clarifying questions, offer to escalate, or retrieve relevant documentation.
---

## Telemetry Privacy

- Pseudonymization of user identifiers
- Minimize stored content

> Telemetry privacy requires pseudonymization of user identifiers and minimizing stored content to protect privacy.
---

## Logging Schemas

- Structured log formats
- Automatically redact sensitive fields
- Balance debugging needs with privacy

> Logging schemas use structured formats with sensitive fields redacted automatically to balance debugging needs with privacy.
---

## Deployment Runbooks

- Rollback procedures
- Rate limit thresholds
- Quota alarms

> Deployment runbooks document rollback procedures, rate limit thresholds, and quota alarms to respond quickly to problems.
---

## Incident Response

- Detection
- Triage
- Communication protocols
- Postmortem analysis to learn from failures

> Incident response procedures define detection, triage, communication protocols, and postmortem analysis to learn from failures.
---

## KPIs and SLOs

- **Quality** metrics and targets
- **Latency** metrics and targets
- **Safety** metrics and targets
- Define success so teams know if the system is working well

> KPIs and SLOs define success metrics and targets for quality, latency, and safety so teams know if the system is working well.
---

## User Study Design

- Define tasks
- Define metrics for success
- Obtain informed consent
- IRB approval when required for research involving human subjects

> User study design requires defining tasks, metrics for success, obtaining informed consent, and IRB approval when required for research involving human subjects.
---

## Practical Lab Preview

- Build a chatbot with RAG + safety filters
- Demonstrate both capability and responsibility

> The practical lab has you build a chatbot with RAG and safety filters, demonstrating both capability and responsibility.
---

## Reflection Prompt

- What guardrails are essential for your chatbot scenario?
- Medical advice chatbots need different safeguards than creative writing assistants

> Consider what guardrails are essential for your specific scenario. Medical advice chatbots need different safeguards than creative writing assistants.
