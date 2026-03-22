# Understanding Embeddings and RAG
# How AI Converts Words to Numbers and Searches by Meaning

![](images/embeddings-intro.png)

> Embeddings are mathematical representations of meaning that enable semantic search and similarity comparison. They've become foundational to modern AI systems, powering everything from search to recommendations.
---

## How AI Writes

- AI does not think like a human
- AI predicts what word comes next
- Humans do this too — "United States of ____", "Happy Birthday to ____"
- Language follows patterns

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Prediction at Scale

- AI learns patterns from massive amounts of text
- The model asks one question: what comes next
- Books, websites, conversations, documents

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Words Become Numbers

- AI does not see words — AI sees numbers
- United = 1, States = 2, Of = 3, America = 4
- The sequence becomes 1 2 3 ____
- The model predicts 4

> Turning language into math is the foundation for embeddings. Machines cannot read words; they understand numbers.
---

## Word Vectorization (Embeddings)

- Every word converts into numbers
- We call this an embedding
- Words become vectors — a list of numbers that describe relationships
- Distance in that space reflects meaning

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Think of a Map

- Each word gets a location
- Similar words stay close
- Different words sit farther apart
- America, USA, American — these live near each other

> Embeddings map words into numbers that preserve meaning. Imagine a 3D map where each word is a dot and distance equals difference in meaning.
---

## Vector Space

- AI learns relationships through distance
- Meaning comes from proximity, not from definitions
- The model uses position and pattern
- Nearby dots = similar context; opposite sides = different topics

> Embeddings are mathematical representations of meaning that enable semantic search and similarity comparison. They've become foundational to modern AI systems.
---

## From Tokens to Meaning

- Tokenization turns text into IDs
- Embeddings turn those IDs into coordinates in space
- Each point represents meaning
- Words close together mean similar things

![](images/understanding-embeddings.png)

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## A Simple Example

- "King" → [0.27, 0.81, 0.43, …]
- "Queen" → [0.25, 0.79, 0.47, …]
- King – Man + Woman ≈ Queen
- Meaning is geometric

> Concrete examples illustrate abstract concepts and show how ideas apply in practice. Pay attention to what made these particular cases succeed or fail.
---

## Word Meaning Clusters

- "King," "queen," "man," "woman" — their embeddings cluster by gender and royalty
- The distance between them carries semantic relationships

> Concrete examples illustrate abstract concepts and show how ideas apply in practice. Pay attention to what made these particular cases succeed or fail.
---

## Where RAG Fits

- Imagine you give the AI your own documents: contracts, policies, reports
- The system does not store them as long pages
- Documents become chunks; chunks become embeddings

> Retrieval-Augmented Generation grounds language models in real documents by retrieving relevant information before generating responses.
---

## Documents Become Chunks

- The document breaks into smaller pieces called chunks
- Each chunk captures a small idea
- Chunks make search easier and more precise

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Chunks Become Embeddings

- Each chunk turns into a vector
- The system stores positions in semantic space
- Your knowledge becomes a map

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Asking a Question

- Your question also becomes a vector
- The system looks for chunks nearby
- It searches by meaning, not by exact words

> When you ask a question, your prompt is embedded. The system searches a vector database for nearby matches.
---

## Retrieval Augmented Generation (RAG)

- First the system retrieves nearby chunks
- Then the model writes an answer using that context
- Retrieve first, generate second
- No model retraining required

> Retrieval-Augmented Generation grounds language models in real documents by retrieving relevant information before generating responses. This architecture has become standard for building reliable knowledge systems.
---

## Why This Works

- The system searches the map each time
- Embeddings make meaning searchable
- Answers stay current as data changes

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Vector Stores

- Vectors need special storage
- A vector store keeps positions in space
- This differs from spreadsheets — numbers in Excel add together; vectors represent meaning

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Context Matters

- "United" plus "States" does not equal "Of"
- Words change meaning depending on context
- Language is relational
- The same word changes position with different meaning — "Bank" (money) vs. "Bank" (river)

> Understanding challenges and limitations is as important as knowing capabilities. The model understands context by comparing surrounding embeddings.
---

## The Context Independence Problem

- Both Word2Vec and GloVe gave one vector per word
- "Bank" meant the same in "river bank" and "credit bank"
- Context was lost

> Understanding challenges and limitations is as important as knowing capabilities. Realistic assessment of obstacles helps you plan appropriately and avoid nasty surprises.
---

## Different Models, Different Embeddings

- Each large language model builds its own embedding system
- ChatGPT, Claude, Gemini — different maps of language
- That is why outputs differ

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The New Generation: Contextual Embeddings

- Transformers changed this
- Models like BERT create different vectors for the same word in different contexts
- Meaning now depends on the sentence

> Embeddings are mathematical representations of meaning that enable semantic search and similarity comparison. They've become foundational to modern AI systems.
---

## Example: Context Shift

- Sentence A: "He sat by the bank of the river."
- Sentence B: "She works at the bank downtown."
- Old models: same vector
- BERT: two distinct vectors

> Concrete examples illustrate abstract concepts and show how ideas apply in practice. Pay attention to what made these particular cases succeed or fail.
---

## Probabilistic Results

- AI predicts likely words
- Sometimes close words replace exact words
- America and USA sit near each other
- The prediction can sound awkward — expected, not a flaw

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The First Generation: Word2Vec

- Word2Vec learned by prediction
- Skip-gram: predict neighbors from a target word
- CBOW: predict target from neighbors
- Vectors reflect co-occurrence statistics

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## GloVe

- GloVe used global counts, not local prediction
- It built a matrix of word co-occurrences and factored it
- It produced stable vectors that captured analogy and frequency

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Sentence and Document Embeddings

- We can extend embeddings beyond words
- Sentences are averaged from their word vectors
- Paragraphs and documents become larger embeddings
- This supports search, clustering, and retrieval

> Embeddings are mathematical representations of meaning that enable semantic search and similarity comparison. They've become foundational to modern AI systems.
---

## OpenAI and Modern Embeddings

- OpenAI models like text-embedding-3-large produce 3000+ dimension vectors
- Trained on massive corpora across domains
- They capture abstract relationships far beyond words

> Embeddings are mathematical representations of meaning that enable semantic search and similarity comparison. They've become foundational to modern AI systems.
---

## Dimensionality and Variation

- Each system uses different dimensions and training data
- Word2Vec: ~300 | BERT base: 768 | OpenAI: >3000
- Higher dimensions capture nuance but increase compute cost

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Comparing Systems

| System | Context | Dimensionality | Training Method | Example Use |
|--------|---------|----------------|-----------------|-------------|
| Word2Vec | None | ~300 | Predict next word | Analogy |
| GloVe | None | ~300 | Co-occurrence matrix | Semantic grouping |
| BERT | Yes | 768 | Transformer encoder | Contextual understanding |
| OpenAI | Yes | 1536–3072 | Foundation model | Retrieval and reasoning |

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Embeddings vs. Keywords

- Keyword search looks for exact words
- Embedding search looks for meaning
- That's why "AI regulation" also finds "machine learning law"

> Embeddings are mathematical representations of meaning that enable semantic search and similarity comparison. They've become foundational to modern AI systems.
---

## Why Embeddings Differ

- Each model learns from different text
- Legal text shapes vectors differently than social media
- Culture and time shift meaning
- Embeddings evolve as language evolves

> Embeddings are mathematical representations of meaning that enable semantic search and similarity comparison. They've become foundational to modern AI systems.
---

## Beyond Text

- Embeddings now cover images, audio, and code
- A picture can embed into the same vector space as a caption
- Multimodal embeddings unify all data types

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Visualization Techniques

- Use PCA or t-SNE to reduce vectors to 2D
- Words with similar meaning cluster together
- Plot reveals language structure

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Embeddings in Action

- Embed a query and compare to embedded documents
- Use cosine similarity to find the closest meaning
- This is how semantic search works

> Embeddings are mathematical representations of meaning that enable semantic search and similarity comparison. They've become foundational to modern AI systems.
---

## Practical Applications

- **Search engines:** "doctor salary" finds "physician income"
- **Chatbots:** retrieve matching knowledge chunks
- **Recommendation systems:** suggest similar items

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## The New Role for Analysts

- We no longer code meaning manually
- We extract it from embeddings
- Our skill is in interpretation, filtering, and grounding

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---

## Final Idea

- AI writes by mapping language into numbers
- Embeddings create the map
- RAG searches the map
- Probability builds the sentence
- What feels like understanding comes from pattern and distance

> Embeddings are the language of AI. They make meaning measurable. The future depends on how we use and interpret them.
