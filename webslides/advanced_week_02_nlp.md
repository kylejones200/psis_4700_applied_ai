# Week 2 — Natural Language Processing
Focus: embeddings and transformers  
Sentiment and summarization

> Natural Language Processing enables computers to understand, interpret, and generate human language. This week focuses on modern transformer-based approaches that have revolutionized text analysis.
---

## NLP Tasks Overview
Classification, sequence labeling, generation

> NLP tasks span classification (sentiment, topic), sequence labeling (named entities, parts of speech), and generation (summarization, translation). Each requires different model architectures and evaluation approaches.
---

## Text as Data
Tokens, subwords, sentences, documents

> Text becomes data through tokenization - breaking it into manageable pieces like words, subwords, or characters. Modern models use subword tokenization to handle rare words and multiple languages efficiently.
---

## Preprocessing
Lowercasing, normalization, tokenization as needed

> Preprocessing choices like lowercasing and normalization depend on your task. Sentiment analysis might preserve case and punctuation while topic modeling might remove them - context determines the right approach.
---

## Bag-of-Words & TF-IDF
Sparse features  
Strong baselines for many tasks

> Bag-of-words and TF-IDF treat text as collections of word counts, ignoring word order but capturing importance. These sparse representations remain strong baselines despite being decades old.
---

## Word Embeddings
Dense vectors capturing semantics (word2vec, GloVe)

> Word embeddings like word2vec and GloVe represent words as dense vectors where semantic similarity corresponds to geometric proximity. Words with similar meanings cluster together in this vector space.
---

## Contextual Embeddings
Token representations depend on context (BERT-like)

> Contextual embeddings from models like BERT represent each word differently depending on surrounding context. The word 'bank' has different embeddings in 'river bank' versus 'savings bank'.
---

## Transformer Basics
Self-attention  
Positional encoding  
Encoder/decoder

> Transformers use self-attention to weigh the importance of different words when processing each word. Positional encoding adds word order information since attention itself is order-agnostic.
---

## Pretrained Language Models
BERT, RoBERTa, DistilBERT, GPT families

> Pretrained language models like BERT, RoBERTa, and GPT families learned language patterns from massive text corpora. You can fine-tune them for specific tasks with relatively little labeled data.
---

## Fine-Tuning vs Prompting
Update model weights vs steer with instructions

> Fine-tuning updates model weights on your specific task while prompting provides instructions to use the model as-is. Prompting is faster and requires no training data but fine-tuning can achieve better performance.
---

## Sentiment Analysis
Predict polarity  
Use labeled datasets (IMDb, SST)

> Sentiment analysis predicts text polarity (positive, negative, neutral) using labeled datasets like IMDb reviews or Stanford Sentiment Treebank. This is a fundamental NLP task with wide business applications.
---

## Summarization
Extractive vs abstractive  
Length control

> Summarization can be extractive (selecting important sentences) or abstractive (generating new text). Length control and faithfulness to source material are key challenges in both approaches.
---

## Hugging Face Pipelines
Sentiment, NER, QA, summarization ready-to-use

> Hugging Face provides ready-to-use pipelines for sentiment analysis, named entity recognition, question answering, and summarization. These democratize NLP by making powerful models accessible with minimal code.
---

## Tokenization Nuances
Subword methods (BPE/WordPiece) reduce OOV issues

> Tokenization nuances include handling subword methods like Byte-Pair Encoding (BPE) and WordPiece that balance vocabulary size against unknown words. These methods enable efficient multilingual models.
---

## Sequence Length Limits
Truncation/chunking for long documents

> Sequence length limits mean long documents must be truncated or chunked. Strategies include taking first/last portions, sliding windows, or hierarchical summarization to preserve important information.
---

## Evaluation: Classification
Accuracy/F1  
Class balance awareness

> Classification evaluation uses accuracy and F1 scores, but class balance matters. A model predicting mostly negative reviews might achieve high accuracy just by always guessing negative.
---

## Evaluation: Summarization
ROUGE/BLEU  
Human review for faithfulness

> Summarization evaluation uses ROUGE and BLEU metrics comparing generated text to reference summaries, but human review remains essential for checking faithfulness (does it accurately reflect the source?).
---

## Handling Domain Shift
Domain-adapt fine-tuning  
Retrieval augmentation

> Domain shift occurs when training data differs from deployment data. Domain adaptation through continued training on in-domain text or retrieval augmentation with domain knowledge can help.
---

## Prompt Design
Clear task, constraints, examples  
Avoid ambiguity

> Prompt design requires clear task specification, appropriate constraints, and sometimes examples. Think of it as giving precise instructions to an intelligent but literal assistant.
---

## Safety & Toxicity
Filter outputs  
Use moderation endpoints

> Safety and toxicity management involves filtering harmful outputs and using moderation endpoints. Unchecked language models can generate offensive or dangerous content.
---

## Data Privacy in NLP
Avoid sending sensitive text to 3rd parties unredacted

> Data privacy in NLP means being careful about sending sensitive text to third-party APIs. Personal information, confidential documents, or proprietary data should be redacted or processed locally.
---

## Multilingual Considerations
Language coverage and tokenization differences

> Multilingual considerations include language coverage in pretrained models and tokenization differences across scripts. Some models handle 100+ languages but with varying quality.
---

## RAG Overview
Retrieve relevant context, then generate grounded answers

> RAG (Retrieval-Augmented Generation) retrieves relevant context from a knowledge base before generating answers. This grounds responses in real information and enables up-to-date knowledge without retraining.
---

## Vector Stores
Store embeddings  
Cosine similarity search

> Vector stores efficiently store and search embeddings using cosine similarity. They enable semantic search where queries match by meaning rather than exact keywords.
---

## Named Entity Recognition
Tag entities  
Label consistency matters

> Named Entity Recognition tags entities like people, organizations, and locations in text. Label consistency is crucial - is 'NYC' tagged the same as 'New York City'?
---

## Text Classification Pipeline
Preprocess, vectorize/encode, model, evaluate

> Text classification pipelines involve preprocessing, vectorizing or encoding text, training a model, and evaluating performance. Each step has choices that significantly impact results.
---

## Error Analysis
Inspect confusion cases  
Refine labels/prompts

> Error analysis means inspecting specific mistakes to find patterns. Maybe your sentiment model struggles with sarcasm or domain-specific slang - these insights guide improvements.
---

## Latency & Cost
Batch requests  
Cache  
Select smaller models when possible

> Latency and cost matter in production. Batch similar requests together, cache common queries, and consider using smaller models when speed matters more than maximum accuracy.
---

## Practical Lab Preview
Sentiment model + summarizer using transformers or API

> The practical lab involves building a sentiment analyzer and summarizer using transformer models or APIs, then conducting error analysis to understand failure modes.
---

## Reflection Prompt
Where does summarization risk hallucinations in your domain?

> Reflect on where summarization risks hallucinations in your domain. Automatic summarization of medical records or legal documents requires extra validation since errors have serious consequences.
---

## Tokenizer Pitfalls
Truncation side-effects  
Special tokens and padding

---

## Long Context Strategies
Sliding windows, hierarchical summaries, retrieval

---

## Few-shot Prompting
Provide labeled examples to guide outputs

---

## Chain-of-Thought
Encourage step-by-step reasoning (use with care)

---

## Citation and Grounding
Require sources  
Highlight retrieved spans

---

## Detoxification
Safety classifiers  
Re-generation strategies

---

## Evaluation Sets
Held-out prompts  
Adversarial and edge cases

---

## Domain Adaptation
Continue pretraining or adapters on domain text

---

## Cost Estimation
Tokens per doc  
Batch sizing  
Caching hits

---

## Latency Budgets
Target p95  
Measure end-to-end, not just model

---

## Data Governance
Redaction, retention windows, access controls

---

## Reading List
Attention Is All You Need  
BERT  
RAG papers

---

## Assignment Brief
Build sentiment + summarizer  
Report error analysis

