# Week 5 — Generative and Conversational Models

## Course Learning Outcomes (CLO) Alignment
- **CLO-A**: Define core AI concepts and distinguish between different AI approaches
- **CLO-D**: Apply AI concepts to analyze real-world problems and evaluate solutions
- **CLO-E**: Demonstrate understanding of data requirements and evaluation methods for AI systems

---

## Module 5.1: Understanding LLMs and Prompting

### Module Learning Outcomes
- **LO 5.1**: Explain prompting, context windows, and the idea of grounding [CLO-A]
- **LO 5.2**: Distinguish between different prompting patterns (zero-shot, few-shot, chain-of-thought) [CLO-A]
- **LO 5.3**: Design a simple prompt template for a specific task [CLO-D]

### Required Materials & Resources
- **Required Readings**:
  1. Course slides: `webslides/week05_gen-convo/` (60-75 min)
  2. Course reference: `course_materials/reference/prompt_patterns_workbook.md` (30-45 min)
  3. Course reference: `course_materials/reference/model_family_map.md` (20 min)
- **Optional Readings**:
  - "Prompt Engineering Guide" - Online resource (OpenAI, Anthropic, or Prompt Engineering Institute)
  - "Understanding Large Language Models" - Beginner-friendly explanation
  - Provider safety policies (OpenAI, Anthropic, Google) - Review one provider's approach
- **Videos** (if available):
  - Overview of LLMs and how they work
  - Prompting patterns walkthrough
- **Interactive Activities**:
  - Hosted LLM API or sandbox for experimentation
  - Prompt template worksheet

### Key Vocabulary
- Prompt, Context window, Hallucination, Grounding, Zero-shot, Few-shot, Chain-of-thought, Token, Embedding

### Learning Activities (Formative - Not Graded)
1. **Self-Study**: Review course slides on LLMs and prompting
2. **Interactive Exploration**: Experiment with different prompting patterns using provided API/sandbox
3. **Practice Exercise**: Complete prompt template worksheet for a specific task

### Estimated Time to Complete
- Reading and review: 75-90 minutes
- Interactive exploration: 60-75 minutes
- Practice exercises: 45-60 minutes
- **Total: 3-3.75 hours**

---

## Module 5.2: Building Safe Chatbots and Prompt Pipelines

### Module Learning Outcomes
- **LO 5.4**: Design basic evaluation checks for prompt outputs [CLO-E]
- **LO 5.5**: Build a tiny chatbot/prompt pipeline with safety guardrails [CLO-D, CLO-E]
- **LO 5.6**: Test and refine prompts using an evaluation checklist [CLO-D, CLO-E]

### Required Materials & Resources
- **Readings**:
  - Course slides: `webslides/week05_gen-convo/`
  - Safety guardrails guide (provided)
  - Evaluation checklist template
- **Interactive Activities**:
  - Hosted LLM API or sandbox
  - Starter template for chatbot/pipeline (no-code and code options)
  - Optional: Vector store starter (RAG-lite) for advanced students
- **Videos** (if available):
  - Walkthrough of building a simple chatbot
  - Demonstration of safety checks

### Key Vocabulary
- Moderation, Safety guardrails, Content filtering, Refusal tests, Length limits, Vector store, RAG (Retrieval-Augmented Generation), Cosine similarity, Alignment

### Learning Activities (Formative - Not Graded)
1. **Self-Study**: Review materials on safety guardrails and evaluation
2. **Hands-On Practice**: Follow along with provided template to build a simple chatbot/pipeline
3. **Testing**: Practice running evaluation checklist on example prompts

### Estimated Time to Complete
- Reading and review: 60-75 minutes
- Hands-on practice: 90-120 minutes
- Testing and refinement: 45-60 minutes
- **Total: 3.25-4.25 hours**

---

## Gradable Activities

### Discussion: Prompting and Safety (25 points)
- **Initial Post** (200 words minimum): Write a one-sentence instruction to get a concise, factual answer with a citation from an LLM. Then, describe one safety guardrail you would implement for this prompt and explain why it's important. Share an example of a prompt that might fail your guardrail check.
- **Reply** (75 words minimum): Respond to one peer's post, either suggesting an additional guardrail, testing their prompt, or sharing a similar example.
- **Due Dates**:
  - Initial post: End of Week 5 (Sunday 11:59 PM)
  - Reply to peer: 48 hours after initial post deadline
- **Evaluation Criteria**:
  - Clear prompt design with citation requirement (30%)
  - Appropriate safety guardrail with rationale (40%)
  - Thoughtful engagement with peers in reply (30%)

### Activity: Chatbot/Prompt Pipeline Project (100 points)
- **Task**: Build a tiny chatbot or prompt pipeline and submit with documentation
- **Required Components**:
  1. **Working Chatbot/Pipeline**: Functional system that takes input and produces output
  2. **Safety Guardrails**: Implement at least 3-5 safety checks (e.g., content moderation, length limits, refusal tests)
  3. **Evaluation Results**: Run evaluation checklist and document results
  4. **README** (1-2 pages): Document your system including:
     - What it does
     - How to use it
     - What safety guardrails are implemented
     - Evaluation results and any issues found
     - How to improve it further
- **Format**: 
  - Code/notebook files OR link to hosted system
  - README as PDF or Word document
- **Due**: End of Week 5 (Sunday 11:59 PM)
- **Evaluation Criteria**:
  - Functional chatbot/pipeline (30%)
  - Implementation of 3-5 safety guardrails (30%)
  - Complete evaluation and documentation (25%)
  - Clear README with usage instructions (15%)

---

## Instructor Notes
- **Module 5.1**: Emphasize that prompting is both art and science. Provide clear examples of different patterns. Encourage experimentation.
- **Module 5.2**: Keep scope small; emphasize grounded, safe responses over flashy features. Provide both no-code and code options.
- **Differentiation**: No-code flow for prompt pipelines; code sample for advanced learners. Provide starter guardrail tests; invite advanced students to add more.
- **Asynchronous Considerations**: Provide step-by-step instructions for all activities. Create video walkthroughs or detailed screenshots. Offer multiple pathways (no-code and code options). Set up Q&A forum for technical questions. Provide starter templates to reduce setup time.

## Accessibility & Inclusion
- Ensure UI has clear labels and keyboard navigation
- Provide captions on all videos
- Offer alternative formats for all activities
- Ensure all tools and platforms are accessible
- Provide clear instructions for tool access

## References
- Course slides: `webslides/week05_gen-convo/`
- Prompt engineering primers
- Provider safety policies (OpenAI, Anthropic, etc.)
- RAG introductions (for advanced students)
- Evaluation checklist template: Provided in course materials
