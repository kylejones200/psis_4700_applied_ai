# Week 2 — Natural Language Processing
# Focus: Embeddings and Transformers, Sentiment and Summarization

> Natural Language Processing enables computers to understand, interpret, and generate human language. This week focuses on modern transformer-based approaches that have revolutionized text analysis.
---

## NLP Tasks Overview

- **Classification:** sentiment, topic
- **Sequence labeling:** named entities, parts of speech
- **Generation:** summarization, translation

> NLP tasks span classification (sentiment, topic), sequence labeling (named entities, parts of speech), and generation (summarization, translation). Each requires different model architectures and evaluation approaches.
---

## Text as Data

- **Tokens** — words, subwords, or characters
- Modern models use subword tokenization for rare words and multilingual efficiency

> Text becomes data through tokenization - breaking it into manageable pieces like words, subwords, or characters. Modern models use subword tokenization to handle rare words and multiple languages efficiently.
---

## Preprocessing

- Lowercasing, normalization, tokenization as needed
- Context determines the right approach — sentiment may preserve case; topic modeling may remove it

> Preprocessing choices like lowercasing and normalization depend on your task. Sentiment analysis might preserve case and punctuation while topic modeling might remove them - context determines the right approach.
---

## Bag-of-Words & TF-IDF

- Sparse features
- Treat text as collections of word counts, ignoring word order
- Strong baselines for many tasks

> Bag-of-words and TF-IDF treat text as collections of word counts, ignoring word order but capturing importance. These sparse representations remain strong baselines despite being decades old.
---

## Word Embeddings

- Dense vectors capturing semantics (word2vec, GloVe)
- Semantic similarity corresponds to geometric proximity

> Word embeddings like word2vec and GloVe represent words as dense vectors where semantic similarity corresponds to geometric proximity. Words with similar meanings cluster together in this vector space.
---

## Contextual Embeddings

- Token representations depend on context (BERT-like)
- "Bank" has different embeddings in "river bank" vs. "savings bank"

> Contextual embeddings from models like BERT represent each word differently depending on surrounding context. The word 'bank' has different embeddings in 'river bank' versus 'savings bank'.
---

## Transformer Basics

- **Self-attention** — weigh importance of different words
- **Positional encoding** — add word order (attention is order-agnostic)
- **Encoder/decoder** architecture

> Transformers use self-attention to weigh the importance of different words when processing each word. Positional encoding adds word order information since attention itself is order-agnostic.
---

## Pretrained Language Models

- BERT, RoBERTa, DistilBERT, GPT families
- Learned from massive text corpora
- Fine-tune for specific tasks with relatively little labeled data

> Pretrained language models like BERT, RoBERTa, and GPT families learned language patterns from massive text corpora. You can fine-tune them for specific tasks with relatively little labeled data.
---

## Fine-Tuning vs. Prompting

- **Fine-tuning:** update model weights on your specific task
- **Prompting:** steer with instructions, use model as-is
- Prompting is faster; fine-tuning can achieve better performance

> Fine-tuning updates model weights on your specific task while prompting provides instructions to use the model as-is. Prompting is faster and requires no training data but fine-tuning can achieve better performance.
---

## Sentiment Analysis

- Predict polarity (positive, negative, neutral)
- Use labeled datasets (IMDb, SST)
- Fundamental NLP task with wide business applications

> Sentiment analysis predicts text polarity (positive, negative, neutral) using labeled datasets like IMDb reviews or Stanford Sentiment Treebank. This is a fundamental NLP task with wide business applications.
---

## Summarization

- **Extractive** — select important sentences
- **Abstractive** — generate new text
- Length control and faithfulness to source are key challenges

> Summarization can be extractive (selecting important sentences) or abstractive (generating new text). Length control and faithfulness to source material are key challenges in both approaches.
---

## Hugging Face Pipelines

- Sentiment, NER, QA, summarization ready-to-use
- Democratize NLP with minimal code

> Hugging Face provides ready-to-use pipelines for sentiment analysis, named entity recognition, question answering, and summarization. These democratize NLP by making powerful models accessible with minimal code.
---

## Tokenization Nuances

- Subword methods (BPE/WordPiece) reduce OOV (out-of-vocabulary) issues
- Balance vocabulary size against unknown words

> Tokenization nuances include handling subword methods like Byte-Pair Encoding (BPE) and WordPiece that balance vocabulary size against unknown words. These methods enable efficient multilingual models.
---

## Sequence Length Limits

- Truncation or chunking for long documents
- Strategies: first/last portions, sliding windows, hierarchical summarization

> Sequence length limits mean long documents must be truncated or chunked. Strategies include taking first/last portions, sliding windows, or hierarchical summarization to preserve important information.
---

## Evaluation: Classification

- Accuracy/F1
- Class balance awareness — a model predicting mostly negative might achieve high accuracy by always guessing negative

> Classification evaluation uses accuracy and F1 scores, but class balance matters. A model predicting mostly negative reviews might achieve high accuracy just by always guessing negative.
---

## Evaluation: Summarization

- ROUGE/BLEU metrics
- Human review for faithfulness (does it accurately reflect the source?)

> Summarization evaluation uses ROUGE and BLEU metrics comparing generated text to reference summaries, but human review remains essential for checking faithfulness (does it accurately reflect the source?).
---

## Handling Domain Shift

- Domain-adapt fine-tuning
- Retrieval augmentation with domain knowledge

> Domain shift occurs when training data differs from deployment data. Domain adaptation through continued training on in-domain text or retrieval augmentation with domain knowledge can help.
---

## Prompt Design

- Clear task, constraints, examples
- Avoid ambiguity
- Give precise instructions to an intelligent but literal assistant

> Prompt design requires clear task specification, appropriate constraints, and sometimes examples. Think of it as giving precise instructions to an intelligent but literal assistant.
---

## Safety & Toxicity

- Filter outputs
- Use moderation endpoints
- Unchecked models can generate offensive or dangerous content

> Safety and toxicity management involves filtering harmful outputs and using moderation endpoints. Unchecked language models can generate offensive or dangerous content.
---

## Data Privacy in NLP

- Avoid sending sensitive text to 3rd parties unredacted
- Redact personal information, confidential documents, proprietary data

> Data privacy in NLP means being careful about sending sensitive text to third-party APIs. Personal information, confidential documents, or proprietary data should be redacted or processed locally.
---

## Multilingual Considerations

- Language coverage in pretrained models
- Tokenization differences across scripts
- Some models handle 100+ languages with varying quality

> Multilingual considerations include language coverage in pretrained models and tokenization differences across scripts. Some models handle 100+ languages but with varying quality.
---

## RAG Overview

- Retrieve relevant context from knowledge base
- Then generate grounded answers
- Enables up-to-date knowledge without retraining

> RAG (Retrieval-Augmented Generation) retrieves relevant context from a knowledge base before generating answers. This grounds responses in real information and enables up-to-date knowledge without retraining.
---

## Vector Stores

- Store embeddings
- Cosine similarity search
- Semantic search by meaning rather than exact keywords

> Vector stores efficiently store and search embeddings using cosine similarity. They enable semantic search where queries match by meaning rather than exact keywords.
---

## Named Entity Recognition

- Tag entities (people, organizations, locations)
- Label consistency matters — is "NYC" tagged the same as "New York City"?

> Named Entity Recognition tags entities like people, organizations, and locations in text. Label consistency is crucial - is 'NYC' tagged the same as 'New York City'?
---

## Text Classification Pipeline

- Preprocess → vectorize/encode → model → evaluate
- Each step has choices that significantly impact results

> Text classification pipelines involve preprocessing, vectorizing or encoding text, training a model, and evaluating performance. Each step has choices that significantly impact results.
---

## Error Analysis

- Inspect confusion cases
- Find patterns — maybe model struggles with sarcasm or domain slang
- Refine labels/prompts

> Error analysis means inspecting specific mistakes to find patterns. Maybe your sentiment model struggles with sarcasm or domain-specific slang - these insights guide improvements.
---

## Latency & Cost

- Batch similar requests
- Cache common queries
- Select smaller models when speed matters more than maximum accuracy

> Latency and cost matter in production. Batch similar requests together, cache common queries, and consider using smaller models when speed matters more than maximum accuracy.
---

## Tokenizer Pitfalls

- Truncation side-effects
- Special tokens and padding

> Tokenization choices affect model behavior. Watch for truncation cutting important content and ensure special tokens and padding are handled correctly.
---

## Long Context Strategies

- Sliding windows
- Hierarchical summaries
- Retrieval

> Long documents require strategies to fit within model limits. Sliding windows, hierarchical summarization, and retrieval can preserve important information.
---

## Few-Shot Prompting

- Provide labeled examples to guide outputs
- Reduces need for fine-tuning

> Few-shot prompting provides labeled examples in the prompt to guide model behavior. This can achieve task-specific performance without fine-tuning.
---

## Chain-of-Thought

- Encourage step-by-step reasoning
- Use with care — can increase latency and token cost

> Chain-of-thought prompting encourages models to reason step by step. Use with care as it increases latency and token consumption.
---

## Citation and Grounding

- Require sources
- Highlight retrieved spans
- Users can verify information

> Citation and grounding require models to cite sources and highlight retrieved content. This helps users verify information and builds trust.
---

## Detoxification

- Safety classifiers
- Re-generation strategies for flagged content

> Detoxification uses safety classifiers to flag harmful output, then applies re-generation or filtering strategies.
---

## Evaluation Sets

- Held-out prompts
- Adversarial and edge cases

> Evaluation sets should include held-out prompts and adversarial examples to test robustness.
---

## Domain Adaptation

- Continue pretraining on domain text
- Adapters for parameter-efficient adaptation

> Domain adaptation continues pretraining or uses adapters on domain-specific text to improve in-domain performance.
---

## Cost Estimation

- Tokens per document
- Batch sizing
- Caching hits

> Cost estimation considers tokens per document, optimal batch sizes, and expected cache hit rates.
---

## Latency Budgets

- Target p95
- Measure end-to-end, not just model inference

> Latency budgets set targets (e.g., p95) and measure full pipeline latency including preprocessing and retrieval.
---

## Data Governance

- Redaction
- Retention windows
- Access controls

> Data governance defines redaction policies, retention limits, and access controls for NLP data.
---

## Practical Lab Preview

- Build sentiment model + summarizer using transformers or API
- Conduct error analysis to understand failure modes

> The practical lab involves building a sentiment analyzer and summarizer using transformer models or APIs, then conducting error analysis to understand failure modes.
---

## Reflection Prompt

- Where does summarization risk hallucinations in your domain?
- Medical records or legal documents require extra validation

> Reflect on where summarization risks hallucinations in your domain. Automatic summarization of medical records or legal documents requires extra validation since errors have serious consequences.
---

## Reading List

- Attention Is All You Need
- BERT
- RAG papers

> Foundational papers on transformers, BERT, and retrieval-augmented generation support this week's material.
---

## Assignment Brief

- Build sentiment + summarizer
- Report error analysis

> The assignment has you build a sentiment analyzer and summarizer, then report findings from error analysis.
