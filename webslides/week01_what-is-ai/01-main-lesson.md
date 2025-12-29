# Week 1 — What Is AI?
Focus: history, definitions, demos  
Reflection on student domains

![](images/what-is-applied-ai.png)

> This opening slide introduces students to the fundamental question of what artificial intelligence really means. We'll explore how AI has evolved from early rule-based systems to today's powerful learning algorithms that can recognize patterns, make predictions, and even generate creative content.

---

## Course Overview
Outcomes, assessments, weekly rhythm

> This course is structured to build your understanding progressively over eight weeks. You'll complete hands-on projects, participate in discussions, and develop practical AI skills that apply directly to your field of study.

---

## What Is Artificial Intelligence?
Systems that perform tasks requiring human-like intelligence

> AI refers to computer systems that can do things we typically think require human intelligence, like recognizing faces, understanding speech, or making decisions. Rather than being programmed with explicit rules for every situation, AI systems learn patterns from examples and apply that learning to new situations.

---

## AI vs ML vs DL
AI umbrella  
ML learns from data  
DL uses neural nets

> Think of AI as the big umbrella term for any system that mimics intelligence. Machine Learning (ML) is one way to achieve AI by showing computers examples so they can learn patterns. Deep Learning (DL) is a specific type of ML that uses brain-inspired networks and has powered recent breakthroughs like ChatGPT and image generators.

---

## Symbolic, Statistical, Generative
Rule-based, data-driven, generative models

> AI has evolved through three main approaches: symbolic AI (following explicit rules like a recipe), statistical AI (learning patterns from data like recognizing spam), and generative AI (creating new content like writing stories or generating images). Modern systems often combine all three approaches.

---

## Narrow vs General AI
Today: narrow AI  
AGI remains speculative

> All AI systems today are "narrow AI" - they're good at specific tasks like playing chess or recognizing faces, but can't transfer that knowledge to other domains. General AI (AGI) would be a system that could learn and adapt like humans do across any task, but that remains science fiction for now.

---

## Brief History
Dartmouth (1956) → Expert systems → ML era → Modern LLMs

![](images/ai_benchmark_progress_smooth.gif)

> AI research began in 1956 at Dartmouth College with grand ambitions that weren't realized for decades. The field went through cycles of excitement and disappointment ("AI winters") before recent breakthroughs in computing power and data availability enabled today's impressive systems like ChatGPT and image generators.

---

## AI Winters and Hype Cycles
Expectations vs reality  
Funding booms/busts

> The history of AI includes periods of intense excitement followed by disappointment when the technology couldn't deliver on inflated promises. These "AI winters" led to funding cuts and reduced research, teaching us that managing expectations is just as important as technical progress.

---

## Capabilities Today
Language, vision, speech, recommendations, planning

> Modern AI can understand and generate human language, recognize objects and faces in images, convert speech to text, recommend products you might like, and even plan complex sequences of actions. These capabilities are already embedded in everyday tools like your phone's voice assistant, Netflix recommendations, and Google Photos.

---

## Limits and Failure Modes
Bias, brittleness, hallucinations, distribution shift

> Despite impressive capabilities, AI systems can fail in predictable ways: they may inherit biases from their training data, break when encountering situations they haven't seen before, confidently state false information ("hallucinate"), or perform poorly when real-world conditions differ from their training. Understanding these limitations is crucial for responsible deployment.

---

## Core Concepts
Data, features, labels, models, loss, optimization

> AI systems learn from data (examples), extract features (important characteristics), use labels (correct answers for training), build models (mathematical representations), measure loss (how wrong predictions are), and apply optimization (improving over time). These foundational concepts appear throughout all AI applications.

---

## Human-in-the-Loop
Collaboration, oversight, escalation paths

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
Users, operators, subjects, society

> Every AI system affects multiple groups of people: those who use it directly, those who operate and maintain it, those whose data it was trained on or whose lives it affects, and society as a whole. Understanding all these perspectives helps us build more ethical and effective systems.

---

## Terminology
Inference, training, prompt, token, embedding

> Key AI terms you'll hear throughout the course: inference (using a trained model to make predictions), training (teaching the model from data), prompt (instructions you give an AI), token (chunks of text the AI processes), and embedding (numerical representations of meaning). Don't worry if these seem abstract now - they'll become clear through practice.

---

## Data and Learning Preview
Supervised vs unsupervised vs reinforcement

> AI systems learn in different ways: supervised learning uses labeled examples (like teaching with flashcards), unsupervised learning finds patterns without being told what to look for (like organizing your closet by color without instructions), and reinforcement learning improves through trial and error with rewards and penalties (like training a dog).

---

## Metrics at a Glance
Accuracy, precision/recall, F1

> We measure AI performance using metrics like accuracy (overall correctness), precision (when it says yes, is it usually right?), recall (does it find all the important cases?), and F1 (a balance of precision and recall). Different applications require different metrics - missing a fraud case is worse than a false alarm.

---

## Prompting Basics
Clear task, constraints, examples

> Getting good results from AI requires clear instructions: specify exactly what you want, set any constraints or limitations, and provide examples when possible. Think of it like giving directions to someone - the clearer you are, the better the outcome.

---

## Hallucinations
Causes  
Grounding with sources

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
Likelihood × impact  
Mitigations

> Evaluate AI risks by considering both how likely something is to go wrong and how serious the consequences would be. A high-impact but unlikely risk (like a medical diagnosis error) may need more attention than a low-impact but frequent issue (like a minor typo in generated text).

---

## Public Perception
Media narratives  
Realistic expectations

> Media coverage of AI often swings between utopian promises and dystopian fears, neither of which reflects reality. Your role as an informed practitioner is to help others understand AI's real capabilities and limitations, countering both hype and fear with facts.

---

## Careers and Roles
Data, ML, MLE, PM, ethics, domain experts

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
Historic benchmark  
Modern perspectives

> The Turing Test (can a computer fool you into thinking it's human?) was proposed in 1950 as a measure of machine intelligence. While some modern chatbots can pass this test, we now recognize that mimicking human conversation isn't the same as true understanding or intelligence.

---

## Knowledge-based vs Data-driven
Rules vs learning  
Hybrid systems

> Early AI used knowledge-based approaches where experts wrote explicit rules (if this, then that). Modern AI is primarily data-driven, learning patterns from examples rather than following programmed rules. The best systems often combine both approaches, using data to learn patterns while respecting known rules and constraints.

---

## Why Now?
Compute, data, algorithms, tooling ecosystem

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
Pilots without adoption  
Misaligned incentives

> Many AI projects fail not because of technology limitations, but because they were launched for the wrong reasons - chasing hype rather than solving real problems. Successful AI projects start with a genuine business need, have clear success metrics, and align with organizational incentives and workflows.

---

## Evaluating Demos Critically
Inputs, constraints, cherry-picking

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

