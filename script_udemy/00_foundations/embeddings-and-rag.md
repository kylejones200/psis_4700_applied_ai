---
Title: Embeddings and RAG
Draft: False
Date: 2026-03-21
Week: 0
Weight: 00
---

A simple but important correction: AI does not write the way people write. When you write, you think about meaning. You form an idea. You choose words to express that idea. AI does something different. It predicts the next word. That is the core mechanism. It looks at what came before and asks one question: what is the most likely next word in this sequence?

This may sound simplistic, but it is powerful. Language has structure. If I say, “United States of…” you already know what comes next. If I say, “Happy Birthday to…” you can complete the sentence. You are using patterns. AI does the same thing, but at scale. It has seen billions of examples. It has learned how words tend to follow each other. So what feels like understanding is actually pattern completion. And that idea will carry through everything we discuss.

Now take that idea and expand it. Instead of learning from a few sentences, the model learns from massive amounts of text—books, websites, conversations, documents. From that data, it builds statistical patterns. Not rules. Not definitions. Patterns. So every time the model generates text, it is not recalling a fact. It is calculating a probability: what word is most likely to come next given everything it has seen before. This happens repeatedly, word by word, sentence by sentence. That is how output is formed. So when you see a response, remember this: it is not retrieved from memory. It is constructed in real time.

Now we need to understand how the model processes language. It does not see words. It sees numbers. Each word is converted into a number or a sequence of numbers. A phrase like “United States of America” becomes a sequence of numeric values. The model processes that sequence and predicts the next number in the sequence, which corresponds to the next word. This conversion is necessary because the model operates mathematically. It cannot process text directly. So everything must become numeric. This is the foundation for embeddings.

Now we move from simple numbers to something more structured: vectors. Instead of assigning a single number to a word, the model assigns a vector—a list of numbers. Each dimension captures some aspect of meaning. You do not interpret each number directly, but together they define the position of the word in a space. This is what we call an embedding. It is a numerical representation of meaning. And this is where things become interesting, because once words are in this space, relationships emerge.

The easiest way to understand embeddings is to think of a map. Each word has a location. Words with similar meanings are close together. Words with different meanings are farther apart. So “America,” “USA,” and “American” cluster together, while unrelated words sit elsewhere. This spatial structure allows the model to reason about similarity—not through definitions, but through distance. That is a shift. Meaning becomes geometry.

In this space, relationships are defined by proximity. Words that appear in similar contexts end up near each other. This allows the model to generalize. If it understands one word, it can often understand related words because they occupy similar positions. So instead of memorizing every case, the model learns structure. And that structure allows it to handle new combinations.

Now we connect this to retrieval. Imagine you provide the system with your own documents—contracts, policies, reports. The system does not store them as text alone. It converts them into embeddings. So your knowledge becomes part of this map, and that allows the system to search by meaning, not by keywords.

Before converting documents, they are broken into chunks. Each chunk represents a small piece of information. Why do this? Because smaller pieces are easier to search. If you search entire documents, results become noisy. Chunks allow precise retrieval. They isolate ideas, and that improves accuracy. Each chunk becomes a vector. Now your documents exist as points in space. This creates a semantic map of your knowledge, and that map is what the system searches.

When you ask a question, it also becomes a vector. The system compares that vector to the stored ones. It finds nearby chunks—not exact matches, but meaning matches. This is the key difference from traditional search.

Now the full process comes together. First, retrieve relevant chunks. Then generate an answer using those chunks. Retrieve first. Generate second. This grounds the response. It connects the model to real data. This approach avoids retraining. You update data, not the model. The system searches dynamically. And embeddings make meaning searchable. That is the power of RAG.

Vectors require specialized storage. A vector store manages positions in space. It enables fast similarity search. This is different from traditional databases because you are not querying exact values. You are querying meaning.

Meaning is not fixed. It depends on context. Words change based on usage. So the system must consider surrounding information. That is why context windows exist. Each model builds its own map. Different embeddings, different relationships. That is why outputs vary across systems.

Because outputs are probabilistic, variation occurs. Similar words may appear. Slight differences in phrasing. This is expected. Not a flaw.

Let’s close this section. AI maps language into numbers. Embeddings create structure. RAG searches that structure. Probability generates output. What feels like understanding is pattern and distance.
