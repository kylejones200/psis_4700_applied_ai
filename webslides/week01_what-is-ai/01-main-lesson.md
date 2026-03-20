# Week 1 — What Is AI?
- History of AI: from symbolic systems to generative models
- Core definitions: AI, ML, DL, and key terminology
- Current capabilities and limits; demos of chatbots and image generation
- Reflection: where can AI add value—or risk—in your field?

![](images/what-is-applied-ai.png)

> This opening slide introduces students to the fundamental question of what artificial intelligence really means. We'll explore how AI has evolved from early rule-based systems to today's powerful learning algorithms that can recognize patterns, make predictions, and even generate creative content.


---

## What Is Artificial Intelligence?
Computer systems that perform tasks we typically associate with human intelligence:
- Recognizing patterns (faces, speech, handwriting)
- Making decisions or predictions (recommendations, risk scores)
- Understanding and generating language
- Adapting to new situations based on experience

Rather than being programmed with explicit rules for every case, modern AI learns from examples.

> AI refers to computer systems that can do things we typically think require human intelligence, like recognizing faces, understanding speech, or making decisions. Rather than being programmed with explicit rules for every situation, AI systems learn patterns from examples and apply that learning to new situations.

---

## AI vs ML vs DL
- **AI** — The umbrella term for any system that performs tasks requiring human-like intelligence
- **ML (Machine Learning)** — A subset of AI: systems that learn patterns from data rather than being explicitly programmed for every situation
- **DL (Deep Learning)** — A subset of ML that uses layered "neural networks" inspired by the brain; powers ChatGPT, image generators, and speech recognition

> Think of AI as the big umbrella term for any system that mimics intelligence. Machine Learning (ML) is one way to achieve AI by showing computers examples so they can learn patterns. Deep Learning (DL) is a specific type of ML that uses brain-inspired networks and has powered recent breakthroughs like ChatGPT and image generators.

---

## Symbolic, Statistical, Generative
AI has evolved through three main paradigms:
- **Symbolic** — Explicit rules and logic (if-then); expert systems that encoded human knowledge
- **Statistical** — Learns patterns from data; spam filters, recommendations, prediction models
- **Generative** — Creates new content (text, images, code); ChatGPT, DALL·E, Copilot

> AI has evolved through three main approaches: symbolic AI (following explicit rules like a recipe), statistical AI (learning patterns from data like recognizing spam), and generative AI (creating new content like writing stories or generating images). Modern systems often combine all three approaches.

---

## Narrow vs General AI
- **Narrow AI** — What we have today: systems excelling at specific tasks (chess, face recognition, translation) but unable to transfer that skill to unrelated domains
- **AGI (General AI)** — Hypothetical system that could learn and adapt across any task, like a human; remains speculative with no clear path or timeline

> All AI systems today are "narrow AI" - they're good at specific tasks like playing chess or recognizing faces, but can't transfer that knowledge to other domains. General AI (AGI) would be a system that could learn and adapt like humans do across any task, but that remains science fiction for now.

---

## Brief History
- **1956** — Dartmouth Conference: AI named as a field; early optimism
- **1980s** — Expert systems: rule-based systems in industry (diagnostics, finance)
- **1990s–2010s** — Machine learning era: statistical methods, neural networks gain traction
- **2020s** — Large language models (LLMs), generative AI; ChatGPT, image generators, coding assistants

![](images/ai_benchmark_progress_smooth.gif)

> AI research began in 1956 at Dartmouth College with grand ambitions that weren't realized for decades. The field went through cycles of excitement and disappointment ("AI winters") before recent breakthroughs in computing power and data availability enabled today's impressive systems like ChatGPT and image generators.

---

## AI Winters and Hype Cycles
- **Expectations vs reality** — Promises often outrun capability; disappointment follows hype
- **Funding booms and busts** — When AI underdelivers, funding dries up; research slows ("AI winters")
- **Lesson** — Managing expectations matters as much as technical progress; today's systems are powerful but still bounded

> The history of AI includes periods of intense excitement followed by disappointment when the technology couldn't deliver on inflated promises. These "AI winters" led to funding cuts and reduced research, teaching us that managing expectations is just as important as technical progress.

---

## Capabilities Today
- **Language** — Understand and generate text; answer questions, summarize, translate, write
- **Vision** — Recognize objects, faces, scenes; describe images; power photo organization and medical imaging
- **Speech** — Transcribe speech to text; text to speech; real-time translation
- **Recommendations** — Suggest content, products, and connections based on behavior
- **Planning** — Sequence actions; route optimization; multi-step task execution

> Modern AI can understand and generate human language, recognize objects and faces in images, convert speech to text, recommend products you might like, and even plan complex sequences of actions. These capabilities are already embedded in everyday tools like your phone's voice assistant, Netflix recommendations, and Google Photos.

---

## Limits and Failure Modes
- **Bias** — Models inherit and amplify biases in training data; can disadvantage certain groups
- **Brittleness** — Small changes in input can cause unexpected failures; no true "understanding"
- **Hallucinations** — Confidently stating false or made-up information, especially in LLMs
- **Distribution shift** — Performance degrades when real-world data differs from training data

> Despite impressive capabilities, AI systems can fail in predictable ways: they may inherit biases from their training data, break when encountering situations they haven't seen before, confidently state false information ("hallucinate"), or perform poorly when real-world conditions differ from their training. Understanding these limitations is crucial for responsible deployment.

---

## Core Concepts
- **Data** — Examples the system learns from (text, images, sensor readings, etc.)
- **Features** — Measurable characteristics extracted from data (e.g., word frequency, pixel values)
- **Labels** — Correct answers used during training (e.g., "spam" or "not spam")
- **Model** — Mathematical representation that maps inputs to outputs
- **Loss** — Measure of how wrong predictions are; drives improvement
- **Optimization** — Process of adjusting the model to minimize loss over training

> AI systems learn from data (examples), extract features (important characteristics), use labels (correct answers for training), build models (mathematical representations), measure loss (how wrong predictions are), and apply optimization (improving over time). These foundational concepts appear throughout all AI applications.

---

## Human-in-the-Loop
Effective AI systems augment humans rather than replace them:
- **Collaboration** — AI handles routine or high-volume tasks; humans focus on edge cases and judgment
- **Oversight** — Humans review AI outputs before high-stakes decisions (loans, diagnoses, hiring)
- **Escalation paths** — When confidence is low or results seem wrong, the system routes to a human

> The best AI systems work alongside humans rather than replacing them entirely. This means building systems where humans can review AI decisions, override them when needed, and handle cases the AI isn't confident about - creating a partnership that leverages both human judgment and machine efficiency.

---

## Demo: Chatbot
Example Q&A with citations

> We'll explore a chatbot that can answer questions and provide sources for its information. This demonstrates how modern language models can retrieve relevant information and present it conversationally, while showing where they got their answers from to build trust.

---

## Demo: Image Generation
Text-to-image prompt and safety filter

> Image generation AI can create pictures from text descriptions, showing how computers can now be creative in ways previously only humans could. We'll also examine the safety filters that prevent these tools from generating harmful or inappropriate content.

---

## Responsible Use Preview
Fairness, privacy, transparency principles

> Using AI responsibly means ensuring systems treat all people fairly regardless of background, protect personal information and privacy, and operate in ways we can understand and explain. These principles will guide all the work we do in this course.

---

## AI in Your Field
Brainstorm realistic use-cases

> Take a moment to think about how AI could be applied in your major or field of interest. The goal is to identify practical, realistic applications rather than science fiction scenarios - things that could actually be built and deployed with today's technology.

---

## Stakeholders and Impact
Every AI system affects multiple groups:
- **Users** — People who interact with the system directly (employees, customers, patients)
- **Operators** — Those who deploy, monitor, and maintain the system
- **Subjects** — People whose data trains the model or whose lives are affected by its outputs
- **Society** — Broader impacts: employment, inequality, trust in institutions

> Every AI system affects multiple groups of people: those who use it directly, those who operate and maintain it, those whose data it was trained on or whose lives it affects, and society as a whole. Understanding all these perspectives helps us build more ethical and effective systems.

---

## Terminology
- **Inference** — Using a trained model to make predictions on new inputs
- **Training** — Teaching the model from data; adjusting parameters to minimize error
- **Prompt** — The instruction or input you give an AI (e.g., "Summarize this article in 3 bullet points")
- **Token** — Chunks of text (words or subwords) that models process; roughly 4 chars ≈ 1 token in English
- **Embedding** — A numerical vector representing meaning; similar concepts have similar vectors

> Key AI terms you'll hear throughout the course: inference (using a trained model to make predictions), training (teaching the model from data), prompt (instructions you give an AI), token (chunks of text the AI processes), and embedding (numerical representations of meaning). Don't worry if these seem abstract now - they'll become clear through practice.

---

## Data and Learning Preview
- **Supervised** — Labeled examples (input → correct output); e.g., spam detection, image classification
- **Unsupervised** — No labels; find structure in data; e.g., clustering, anomaly detection
- **Reinforcement** — Learn from rewards/penalties through trial and error; e.g., game-playing, robotics

> AI systems learn in different ways: supervised learning uses labeled examples (like teaching with flashcards), unsupervised learning finds patterns without being told what to look for (like organizing your closet by color without instructions), and reinforcement learning improves through trial and error with rewards and penalties (like training a dog).

---

## Metrics at a Glance
- **Accuracy** — Overall fraction of correct predictions (can be misleading with imbalanced classes)
- **Precision** — When the model says "yes," how often is it right? (reduces false positives)
- **Recall** — Of all true positives, how many did the model find? (reduces missed cases)
- **F1** — Harmonic mean of precision and recall; balances both

> We measure AI performance using metrics like accuracy (overall correctness), precision (when it says yes, is it usually right?), recall (does it find all the important cases?), and F1 (a balance of precision and recall). Different applications require different metrics - missing a fraud case is worse than a false alarm.

---

## Prompting Basics
- **Clear task** — State exactly what you want (e.g., "Summarize in 3 sentences" not "Make it shorter")
- **Constraints** — Specify format, tone, length, or what to avoid
- **Examples** — Show one or more examples of the desired output (few-shot prompting)

> Getting good results from AI requires clear instructions: specify exactly what you want, set any constraints or limitations, and provide examples when possible. Think of it like giving directions to someone - the clearer you are, the better the outcome.

---

## Hallucinations
- **What they are** — Confidently stated false or fabricated information; common in LLMs
- **Causes** — Models predict plausible-sounding text, not verified facts; no built-in "knowledge" check
- **Mitigations** — Ground responses in retrieved documents (RAG); instruct model to say "I don't know"; verify critical claims

> AI systems sometimes confidently state false information, called "hallucinations" - like a student who makes up facts rather than admitting they don't know something. We can reduce this problem by grounding AI responses in real sources and teaching it to say "I don't know" when appropriate.

---

## Privacy and Consent
Minimize data  
Avoid sensitive inputs to third parties

> Protect privacy by only collecting the minimum data necessary and being careful about what information you send to external AI services. Never input sensitive personal information, medical records, or confidential business data into public AI tools without understanding where that data goes.

---

## Accessibility
Clear, concise interfaces  
Multimodal aids

> AI systems should be usable by everyone, including people with disabilities. This means designing clear interfaces, providing text alternatives for images, voice options for those who can't type easily, and considering how people with different abilities will interact with your system.

---

## Risk Assessment
- **Likelihood × impact** — Prioritize by both how often something might fail and how bad the outcome would be
- **Examples** — Medical misdiagnosis: low likelihood, very high impact → needs strong safeguards. Typo in generated email: high likelihood, low impact → less critical
- **Mitigations** — Human review, testing, guardrails, monitoring, and clear escalation paths

> Evaluate AI risks by considering both how likely something is to go wrong and how serious the consequences would be. A high-impact but unlikely risk (like a medical diagnosis error) may need more attention than a low-impact but frequent issue (like a minor typo in generated text).

---

## Public Perception
Media narratives  
Realistic expectations

> Media coverage of AI often swings between utopian promises and dystopian fears, neither of which reflects reality. Your role as an informed practitioner is to help others understand AI's real capabilities and limitations, countering both hype and fear with facts.

---

## Careers and Roles
- **Data scientist** — Analyze data, build models, interpret results
- **ML engineer (MLE)** — Deploy and maintain models in production; infrastructure and scaling
- **Product manager (PM)** — Define problems, prioritize features, align AI with business goals
- **Ethics / governance** — Fairness, privacy, compliance; responsible AI practices
- **Domain experts** — Bring subject-matter knowledge (healthcare, finance, education) to AI projects

> The AI field includes diverse roles beyond just programmers: data scientists who analyze patterns, machine learning engineers who build systems, product managers who guide development, ethics specialists who ensure responsible use, and domain experts who understand the specific problems being solved. There's room for many different skills and backgrounds.

---

## Reading/Watching
Short history pieces  
Primer videos

> The recommended materials provide accessible introductions to AI history and concepts. These readings and videos are designed for general audiences, so don't worry if you don't have a technical background - they'll build your foundation for understanding the technology.

---

## Lab Preview
Try a hosted chatbot and an image generator

> Your first hands-on assignment is to experiment with real AI tools: a chatbot that can answer questions and an image generator that creates pictures from descriptions. The goal is to develop intuition about what these systems can and cannot do through direct experience.

---

## Reflection Prompt
Where can AI add value in your major? What risks?

> Think critically about AI's role in your field of study. Consider both the potential benefits (efficiency, new insights, automation of tedious tasks) and the risks (bias, job displacement, privacy concerns). There are no wrong answers - this is about developing your own informed perspective.

---

## Myths vs Realities
AI is not magic  
Tradeoffs, limits, and costs apply

> AI is powerful but not magical - it operates through mathematical calculations, not mystical intelligence. Every AI system involves tradeoffs (speed vs accuracy, simplicity vs capability), has real limitations (can only work with data it's been trained on), and costs money to develop and run.

---

## Turing Test and Beyond
- **The test** — Can a machine converse well enough to fool a human into thinking it's human? (Turing, 1950)
- **Status** — Some modern chatbots can pass under limited conditions
- **Limitation** — Mimicking conversation ≠ understanding; we now use task-specific benchmarks instead

> The Turing Test (can a computer fool you into thinking it's human?) was proposed in 1950 as a measure of machine intelligence. While some modern chatbots can pass this test, we now recognize that mimicking human conversation isn't the same as true understanding or intelligence.

---

## Knowledge-based vs Data-driven
- **Knowledge-based** — Experts write explicit rules (if-then); good when logic is well-understood; brittle when rules multiply
- **Data-driven** — Systems learn patterns from examples; flexible but need large datasets; can encode hidden biases
- **Hybrid** — Combine both: use data to learn patterns while enforcing known constraints or safety rules

> Early AI used knowledge-based approaches where experts wrote explicit rules (if this, then that). Modern AI is primarily data-driven, learning patterns from examples rather than following programmed rules. The best systems often combine both approaches, using data to learn patterns while respecting known rules and constraints.

---

## Why Now?
Four factors converged to enable today's AI:
- **Compute** — GPUs and cloud computing make training large models feasible and affordable
- **Data** — The internet and digitization provide massive training corpora
- **Algorithms** — Transformers and related advances unlocked language and multimodal capabilities
- **Tooling** — APIs, open-source libraries, and no-code tools make AI accessible beyond researchers

> AI has exploded recently due to four convergent factors: cheap powerful computers (especially graphics processors), massive amounts of available data (the internet), improved algorithms (like transformers), and excellent tools that make AI accessible to non-experts. This perfect storm has made previously impossible applications routine.

---

## Success Case: Recommendations
Personalization in media/retail

> Recommendation systems are one of AI's biggest success stories, powering Netflix's movie suggestions, Amazon's product recommendations, and Spotify's playlist generation. These systems analyze your past behavior and find patterns with similar users to predict what you might like next.

---

## Success Case: Assistive Tech
Accessibility and productivity boosts

> AI has dramatically improved accessibility and productivity through tools like voice-to-text for people who can't type, image description for the visually impaired, real-time translation for language barriers, and automated transcription for meetings. These applications show AI's potential to genuinely improve people's lives.

---

## Failure Case: Overfitting Hype
- **Pilots without adoption** — Proof-of-concepts that never move to production; no clear path to value
- **Misaligned incentives** — Built to impress leadership, not to solve user problems
- **Lesson** — Start with a real problem, define success metrics, and align with how people actually work

> Many AI projects fail not because of technology limitations, but because they were launched for the wrong reasons - chasing hype rather than solving real problems. Successful AI projects start with a genuine business need, have clear success metrics, and align with organizational incentives and workflows.

---

## Evaluating Demos Critically
- **Inputs** — Were they cherry-picked? Would it work on messy, real-world examples?
- **Constraints** — What guardrails, filters, or human review are hidden from view?
- **Cherry-picking** — Are you seeing the best outcomes while failures are edited out?
- **Takeaway** — Ask what breaks the demo; healthy skepticism reveals true capabilities

> When you see impressive AI demos, ask critical questions: What inputs were carefully chosen to make this work? What constraints or guardrails are hidden from view? Are they showing you only the best results (cherry-picking) while hiding the failures? Healthy skepticism helps you evaluate AI's true capabilities.

---

## Communicating AI Clearly
Avoid jargon  
Explain tradeoffs and risks

> When explaining AI to non-technical audiences, skip the jargon and focus on what the system actually does in plain language. Always discuss tradeoffs (what you gain and what you give up) and be honest about risks and limitations - clear communication builds trust and leads to better decisions.

---

## Ethics Primer
Fairness, privacy, transparency in simple terms

> Ethical AI boils down to three key principles: fairness (treating all people equitably), privacy (protecting personal information), and transparency (being clear about how the system works and when AI is being used). These aren't just nice-to-haves - they're essential for building systems people can trust.

---

## Assignment Brief
Write a one-page concept: use-case, benefit, risk

> Your first assignment asks you to propose an AI application in your field: describe what problem it would solve, who would benefit, what the potential risks are, and why this application makes sense. This exercise helps you think practically about AI while considering both opportunities and responsibilities.

---

## Reading List
Short history of AI  
Beginner-friendly explainers

> The assigned readings provide historical context and accessible explanations of AI concepts. These materials are selected specifically for beginners, so they'll help you build a solid foundation without requiring technical prerequisites.

