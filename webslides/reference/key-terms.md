# Vector store
What it is: A database optimized to store and search vectors (numerical representations of text/images)

Why it matters: Enables fast "find similar" lookups for search and RAG

Example: Store document embeddings and retrieve top matches for a user query

> Vector stores are the backbone of modern semantic search and RAG systems. They make it possible to find relevant information based on meaning rather than just keyword matching, fundamentally changing how we build search and question-answering systems.
---

## Cosine similarity
What it is: A score measuring how similar two vectors are by the angle between them (1 = very similar, 0 = unrelated)

Why it matters: Used to rank relevant documents in vector search

Example: Compare a query embedding to document embeddings to pick the top-k

> Cosine similarity measures the angle between vectors regardless of their magnitude, making it perfect for comparing embeddings where scale doesn't matter but direction (meaning) does. This simple geometric concept powers most similarity search systems.
---

## Transfer learning
What it is: Starting from a pre-trained model and adapting it to a new task with limited data

Why it matters: Saves time, cost, and data  
Better results with small datasets

Example: Fine-tune a pretrained vision model on a small product image dataset

> Transfer learning is why small teams can now build state-of-the-art AI systems. Instead of training from scratch (requiring millions of examples and enormous compute), you start with knowledge from large pretrained models and adapt it to your specific task.
---

## Markov chain
What it is: A model where the next state depends only on the current state

Why it matters: Simple way to model sequences and transitions

Example: Predict the next webpage a user visits based on the current page

> Markov chains provide an intuitive framework for modeling sequential processes. The 'memoryless' assumption (only current state matters) simplifies many problems while still capturing essential dynamics.
---

## Alignment
What it is: Ensuring AI behavior follows human values, rules, and goals

Why it matters: Reduces harmful, biased, or off-policy outcomes

Example: Safety policies and refusals built into a chatbot

> Alignment addresses the fundamental challenge of ensuring AI systems pursue goals we actually want. Technical capability means nothing if the system optimizes for the wrong objective or produces harmful outputs.
---

## Large language model (LLM)
What it is: A model trained on lots of text to follow instructions and generate language

Why it matters: Powers chatbots, assistants, writing aids

Example: Ask an LLM to draft an email in a friendly tone

> LLMs represent a paradigm shift in how we interact with computers. Instead of precise programmatic instructions, we can use natural language to describe what we want, democratizing AI access.
---

## Token
What it is: A chunk of text the model reads/writes (pieces of words or characters)

Why it matters: Costs and limits are measured in tokens  
Affects context length

Example: "Assistant" may split into subword tokens like "Assist" + "ant"

> Understanding tokens is crucial for managing costs and context limits. Since pricing and limits are per-token, not per-word, knowing how your text tokenizes directly impacts your budget and architecture choices.
---

## Embedding
What it is: A vector that captures meaning of text or images

Why it matters: Enables similarity search and classification

Example: Represent a sentence as a vector to find similar sentences

> Embeddings convert semantic meaning into mathematical objects we can compute with. They bridge the gap between human language and machine computation, enabling similarity search, classification, and clustering based on meaning.
---

## Prompt
What it is: The instructions or input you give the model

Why it matters: Clear prompts lead to clearer outputs

Example: "Summarize this article in 3 bullet points with a citation."

> Prompt engineering has become a critical skill. The same model produces vastly different results depending on how you ask, so learning to write effective prompts is essential for getting value from LLMs.
---

## Prompt template
What it is: A reusable prompt with placeholders you fill in

Why it matters: Consistent, scalable prompting across many inputs

Example: "You are a helpful tutor. Explain {topic} to a beginner."

> Prompt templates enable scaling from individual experiments to production systems. They ensure consistency, enable version control of prompts, and make it easy to A/B test different instruction strategies.
---

## Context window
What it is: The maximum amount of tokens the model can consider at once

Why it matters: Limits how much history or documents you can include

Example: Long conversations may need summarization to fit the window

> Context window size is often the limiting factor in LLM applications. Understanding this constraint shapes architecture decisions around document processing, conversation management, and information retrieval.
---

## Zero-shot prompting
What it is: Asking the model to do a task without examples  
Why it matters: Simple and fast for well-known tasks  
Example: "Classify this review as positive or negative."

> Zero-shot prompting is the simplest approach and often sufficient for well-defined tasks. When models are powerful enough and tasks are standard, you can skip the complexity of providing examples.
---

## Few-shot prompting
What it is: Showing a few labeled examples in the prompt  
Why it matters: Can improve quality and consistency  
Example: Provide 2–3 Q&A examples before asking the model a new question

> Few-shot prompting significantly improves consistency and quality for specific task formats. Those few examples teach the model your exact output format and style preferences better than instructions alone.
---

## Chain-of-thought
What it is: Asking the model to explain steps before the final answer  
Why it matters: Can improve reasoning transparency  
Use carefully
Example: "Think step by step. First outline the steps, then answer."

> Chain-of-thought prompting can improve reasoning on complex problems by forcing step-by-step thinking. However, more tokens mean higher costs and latency, so use strategically when reasoning quality matters most.
---

## Hallucination
What it is: A confident but incorrect or made-up output  
Why it matters: Can mislead users  
Must be managed
Example: The model invents a source that doesn't exist

> Hallucinations are the most frequently mentioned limitation of LLMs. Users must understand that confidence doesn't equal correctness, and verification mechanisms are essential for high-stakes applications.
---

## Grounding
What it is: Tying answers to real sources or data  
Why it matters: Reduces hallucinations and builds trust  
Example: Cite a paragraph from a retrieved document

> Grounding transforms LLMs from creative writers into reliable information systems. By requiring citations and retrieving real sources, you dramatically reduce hallucinations and enable verification.
---

## Retrieval-augmented generation (RAG)
What it is: Retrieve relevant documents, then generate an answer using them  
Why it matters: More accurate, up-to-date, and verifiable responses  
Example: Search a company handbook and answer HR questions with citations

> RAG has become the standard architecture for building knowledge-grounded systems. It combines the flexibility of LLMs with the reliability of traditional search, creating systems that are both conversational and accurate.
---

## Vector database
What it is: A database specialized for storing and querying embeddings  
Why it matters: Scales similarity search across millions of vectors  
Example: Pinecone, FAISS, Weaviate, or Milvus

> Vector databases enable RAG and semantic search at scale. While simple vector search works for thousands of items, specialized databases handle millions or billions of vectors efficiently with approximate nearest neighbor algorithms.
---

## Top-k retrieval
What it is: Returning the k most similar items for a query  
Why it matters: Controls how much context you pass to the model  
Example: Retrieve top-3 relevant passages for a question

> Top-k retrieval controls the precision-recall tradeoff in search. Higher k provides more context but increases noise and costs, while lower k is focused but might miss relevant information.
---

## Confidence score
What it is: A number indicating how sure a system is (varies by method)  
Why it matters: Helps decide when to escalate or ask a human  
Example: Only auto-approve answers with confidence ≥ 0.8

> Confidence scores help systems know what they don't know. By routing low-confidence cases to humans and auto-handling high-confidence ones, you can provide fast automated responses while maintaining quality.
---

## Moderation
What it is: Screening inputs/outputs for unsafe content  
Why it matters: Protects users and meets policy requirements  
Example: Block hate speech or PII before sending to a model

> Moderation is essential for deploying language models responsibly. Without input and output filtering, models will eventually generate harmful content, creating liability and harming users.
---

## Guardrails
What it is: Rules and checks shaping what the model can do or say  
Why it matters: Reduces risk and keeps the app on-policy  
Example: Refuse medical advice  
Limit tools to read-only

> Guardrails are the difference between a demo and a production system. They constrain what the model can do or say, ensuring it behaves appropriately even when users try to misuse it.
---

## Function calling (tools)
What it is: The model outputs a structured request for a tool or function  
Why it matters: Lets the model fetch data or take actions safely  
Example: "get_weather(city='Boston')" returned to your app to run

> Function calling bridges LLMs and traditional software. It lets models decide when to use tools while keeping the actual execution under your control, combining reasoning with reliable action-taking.
---

## API rate limit
What it is: The maximum calls you can make per time period  
Why it matters: Prevents overload  
Affects throughput
Example: 60 requests per minute per API key

> Rate limits are your enemy during development and your friend in production. They prevent abuse and manage costs, but require architecting for graceful degradation when limits are hit.
---

## Latency
What it is: The time it takes to get a response  
Why it matters: Affects user experience  
High latency feels slow
Example: Aim for < 1–2 seconds for interactive chat

> Latency directly impacts user experience. Humans perceive sub-second responses as instant, 1-2 seconds as acceptable, and anything longer as slow. Architectural decisions around model size and caching are often driven by latency requirements.
---

## Caching
What it is: Saving results to reuse later  
Why it matters: Cuts cost and latency for repeated queries  
Example: Cache embeddings or model outputs for popular prompts

> Caching is often the easiest performance optimization. Many queries are repeated or similar, so storing results can dramatically reduce both costs and latency with minimal implementation effort.
---

## Prompt injection
What it is: Malicious content that tries to override your instructions  
Why it matters: Can cause data leaks or unsafe actions  
Example: A webpage tells the model to ignore safety rules

> Prompt injection attacks exploit the fact that LLMs don't distinguish between your instructions and user content. Defenses include input filtering, output validation, and structured prompting that separates instructions from data.
---

## Jailbreak
What it is: Tricks to bypass a model's safeguards  
Why it matters: Leads to unsafe or off-policy outputs  
Example: Roleplay prompts that get around refusal policies

> Jailbreaks reveal that safety alignment is difficult. Even well-aligned models can be tricked into inappropriate outputs, requiring layered defenses beyond just model training.
---

## Safety filter
What it is: A check that blocks or rewrites unsafe content  
Why it matters: A core control for production apps  
Example: Classify content before/after generation to block

> Safety filters provide a critical last line of defense. Even when models are trained to refuse harmful requests, filters catch edge cases and protect against evolving attack methods.
---

## Model drift
What it is: Performance changes over time due to data or behavior shifts  
Why it matters: Hidden quality drops can harm users  
Example: New slang reduces intent detection accuracy

> Model drift is an often-overlooked production challenge. Performance degradation happens gradually as language use evolves, requiring monitoring and periodic retraining to maintain quality.
---

## Overfitting
What it is: The model memorizes training data and fails on new data  
Why it matters: Appears great in training but fails in reality  
Example: 99% train accuracy, 60% test accuracy

> Overfitting is the most common mistake in ML projects. Models that achieve perfect training accuracy but fail on new data have memorized rather than learned, requiring more data, simpler models, or regularization.
---

## Underfitting
What it is: The model is too simple to capture the patterns  
Why it matters: Poor performance everywhere  
Example: Linear model for a strongly non-linear problem

> Underfitting indicates your model is too simple for the problem. Before gathering more data or trying complex algorithms, ensure your current model has sufficient capacity to capture the patterns that exist.
---

## Confusion matrix
What it is: A table showing counts of correct/incorrect predictions by class  
Why it matters: Reveals which errors happen  
Example: High false negatives indicate missed positives

> Confusion matrices reveal exactly how your model fails, not just that it fails. Understanding whether you have more false positives or false negatives guides targeted improvements.
---

## Precision
What it is: Of the positives predicted, how many were correct  
Why it matters: Useful when false positives are costly  
Example: Email spam filter avoiding blocking real emails

> Precision matters when false alarms are expensive. If your model flags many cases for review, high precision means human reviewers spend time on real issues rather than chasing false positives.
---

## Recall
What it is: Of the actual positives, how many were found  
Why it matters: Useful when missing positives is costly  
Example: Medical screening where misses are dangerous

> Recall matters when misses are dangerous. In medical screening or fraud detection, missing positive cases has serious consequences, so you accept more false alarms to ensure you find what matters.
---

## F1 score
What it is: A balance between precision and recall in one number  
Why it matters: Good for imbalanced datasets  
Example: Compare models on F1 when positives are rare

> F1 score provides a single metric balancing precision and recall. It's particularly useful for comparing models on imbalanced datasets where accuracy alone is misleading.
---

## Accuracy
What it is: Fraction of predictions that are correct  
Why it matters: Can be misleading with class imbalance  
Example: 95% accuracy when 95% are negative tells little

> Accuracy is intuitive but often misleading. On imbalanced datasets, even a useless model that predicts only the majority class can achieve high accuracy, making precision/recall/F1 more informative.
---

## Bias
What it is: Systematic error that skews results against certain groups  
Why it matters: Unfair outcomes and legal/ethical risks  
Example: Training data underrepresents a demographic

> Bias in AI systems reflects and can amplify societal inequalities. Since models learn from historical data that contains discrimination, active intervention is required to prevent perpetuating unfairness.
---

## Fairness
What it is: Ensuring comparable performance across groups  
Why it matters: Ethical and often required by policy  
Example: Check false negative rates across demographics

> Fairness is not a single mathematical definition but a set of competing concepts. Different stakeholders and contexts require different fairness notions, making this as much a social as technical challenge.
---

## Explainability (XAI)
What it is: Methods to make model decisions understandable  
Why it matters: Builds trust and aids debugging  
Example: Show top features influencing a decision

> Explainability builds trust and enables debugging. When stakeholders understand why a model makes decisions, they can identify when it's using spurious correlations and judge whether to trust its outputs.
---

## SHAP
What it is: A method to explain each feature's contribution to a prediction  
Why it matters: Fine-grained, per-example explanations  
Example: SHAP shows income and age most increased approval odds

> SHAP has become the standard for feature importance explanations. Its game-theoretic foundation provides consistency guarantees and the ability to decompose predictions into individual feature contributions.
---

## LIME
What it is: A method that approximates a complex model locally with a simple one  
Why it matters: Quick, local interpretability  
Example: Explain why one image was classified as a cat

> LIME provides quick local explanations for individual predictions. While less theoretically grounded than SHAP, it's fast and works with any black-box model, making it widely applicable.
---

## Model card
What it is: A short document describing a model, data, metrics, and limits  
Why it matters: Transparent communication and governance  
Example: Include intended use and known failure cases

> Model cards standardize documentation of AI systems. By forcing teams to explicitly state limitations, biases, and intended uses, they promote responsible deployment and help users assess appropriateness.
---

## Datasheet for datasets
What it is: Documentation about how a dataset was collected and used  
Why it matters: Helps assess quality, bias, and fit  
Example: Source, consent, labeling, and caveats

> Datasheets bring similar documentation practices to datasets. Understanding how data was collected, who labeled it, and what biases it contains is essential for judging whether a model trained on it will work for your use case.
---

## Personally identifiable information (PII)
What it is: Data that can identify an individual  
Why it matters: Must be protected by policy and law  
Example: Names, emails, SSNs, exact addresses

> PII protection is both an ethical obligation and a legal requirement. Mishandling personal data can result in massive fines under GDPR, HIPAA, and other regulations beyond the harm to individuals.
---

## Differential privacy
What it is: Techniques that add noise to protect individuals in data  
Why it matters: Share insights while preserving privacy  
Example: Release stats without exposing any one person

> Differential privacy provides mathematical privacy guarantees unlike ad-hoc anonymization. The privacy budget parameter explicitly quantifies the privacy-utility tradeoff, enabling principled decisions.
---

## Watermarking
What it is: Marking generated content to signal its origin  
Why it matters: Transparency and detection of AI content  
Example: Invisible markers in images or text

> Watermarking AI-generated content addresses transparency and authenticity concerns. As AI-generated text and images become indistinguishable from human-created content, marking them becomes essential for trust.
---

## Provenance
What it is: The history of data or content creation  
Why it matters: Trust, auditing, and authenticity  
Example: Track what sources fed into an answer

> Provenance tracking creates audit trails showing where information came from. In regulated industries and high-stakes decisions, being able to trace back through the reasoning chain is crucial.
---

## Diffusion model
What it is: An image generator that learns to remove noise step by step  
Why it matters: High-quality images from text prompts  
Example: "A watercolor of a mountain at sunrise."

> Diffusion models have revolutionized image generation through their iterative refinement process. By learning to denoise rather than generate directly, they achieve remarkable quality and controllability.
---

## Inpainting
What it is: Editing or filling in missing parts of an image  
Why it matters: Practical for touch-ups and edits  
Example: Remove an object and refill the background

> Inpainting extends image generation to editing workflows. The ability to selectively modify regions while maintaining coherence with surroundings enables practical tools that augment rather than replace creative work.
---

## Negative prompt
What it is: Terms you want the generator to avoid  
Why it matters: Steers results away from unwanted traits  
Example: "No text, no watermark."

> Negative prompts provide fine-grained control over generation. They're often more effective than trying to specify everything you want, instead explicitly excluding common failure modes.
---

## Seed (random seed)
What it is: A number that makes random processes repeatable  
Why it matters: Lets you reproduce results  
Example: Use the same seed to get similar images each run

> Random seeds enable reproducibility in stochastic processes. For debugging, sharing results, and scientific rigor, being able to exactly reproduce an output is essential.
---

## Multimodal model
What it is: A model that handles more than one kind of data (text, image, audio)  
Why it matters: Richer interactions and capabilities  
Example: Ask about an image and get a text answer

> Multimodal models unify different data types into single systems. This enables richer interactions like visual question answering and reduces the friction of stitching together separate specialized models.
---

## Time series
What it is: Data points ordered in time  
Why it matters: Forecasting and anomaly detection  
Example: Daily sales over a year

> Time series data requires respecting temporal ordering throughout modeling. The sequential nature means standard cross-validation doesn't work, and special care is needed to prevent leaking future information into the past.
---

## Seasonality
What it is: Regular patterns that repeat over time  
Why it matters: Influences forecasts and planning  
Example: Weekly traffic spikes on Mondays

> Seasonality is one of the most important patterns in time series. Identifying and modeling regular fluctuations (daily, weekly, yearly) often matters more than sophisticated forecasting algorithms.
---

## Cross-validation
What it is: A way to estimate performance by training/testing on different splits  
Why it matters: More reliable evaluation than a single split  
Example: 5-fold CV averages scores across 5 runs

> Cross-validation provides more reliable performance estimates than single train-test splits. By averaging across multiple splits, you reduce the risk of lucky or unlucky divisions biasing your assessment.
---

## Pipeline
What it is: A chained sequence of steps: preprocess → model → postprocess  
Why it matters: Reproducible and less error-prone  
Example: Scale features then apply logistic regression

> Pipelines enforce the correct order of operations and ensure preprocessing steps are consistent between training and deployment. Many subtle bugs come from preprocessing differences that pipelines prevent.
---

## Data leakage
What it is: Test information accidentally used during training  
Why it matters: Inflates metrics and fails in production  
Example: Normalizing using the full dataset before splitting

> Data leakage is the silent killer of ML projects. It makes your model look great in development but fail in production because it learned from information that won't be available when making real predictions.
---

## Baseline
What it is: A simple method used to set a performance floor  
Why it matters: Helps judge whether complex models add value  
Example: Majority class classifier as a baseline

> Baselines provide essential context for evaluating complex models. If your sophisticated deep learning system barely beats a simple heuristic, the added complexity probably isn't worth the maintenance cost.
---

## A/B testing
What it is: Comparing two versions (A vs B) with users to see which performs better  
Why it matters: Data-driven decisions in production  
Example: Test two prompts and measure user success

> A/B testing enables data-driven decisions in production. Rather than guessing which approach is better, you measure actual user outcomes, letting empirical evidence guide continuous improvement.