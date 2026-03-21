---
Title: RAG Details
Draft: False
Date: 2026-03-21
Week: 5
Weight: 13
---

Up to this point, retrieval has sounded simple. Find relevant information. Add it to the prompt. Generate an answer. And at a high level, that is exactly what happens. But underneath that simplicity, there is a structure that determines whether the system works or fails.

When a user asks a question, the system does not search for exact matches in the way a traditional database would. It transforms the question. It converts the text into an embedding—a vector of numbers that captures meaning. Now that embedding can be compared to other embeddings. Documents are also broken into pieces. Chunks. Each chunk is converted into an embedding. So instead of comparing words, the system compares positions in a numeric space. It looks for chunks that are close to the question. Close means similar in meaning. Not identical in wording. This is what allows the system to find relevant information even when the phrasing is different.

Once those chunks are retrieved, they are inserted into the prompt. The model receives both the question and the supporting context. And it generates a response based on that combined input. So the model is still doing what it always does: predicting tokens. But now it is guided by real data. Not only by what it learned during training.

The quality of the system depends heavily on retrieval. If the right information is found, the answer improves. If the wrong information is retrieved, the model will still produce a fluent answer. But it will be wrong. So retrieval is not a side component. It is central.

Imagine a user asks about a refund policy. The system searches the document store. It finds a section of the policy that discusses refunds. It inserts that text into the prompt. The model reads it. And produces an answer grounded in that text. If the correct section is retrieved, the answer is accurate. If a different section is retrieved, the answer may be incomplete or incorrect. So the entire system hinges on that step.

How do you split documents into chunks? If chunks are too large, they may include irrelevant information. If they are too small, they may lose context. So chunking becomes a balance. You want enough context to be meaningful. But not so much that it dilutes relevance. All those embeddings must be stored in a vector store—a system designed to search based on similarity. That store must be efficient. Because retrieval happens in real time.

You may retrieve several candidate chunks. You need to decide which ones to include. Too many, and you exceed token limits. Too few, and you may miss important context. So ranking matters.

If retrieval fails, the system fails. If the documents are outdated, the answer is outdated. If the chunks are poorly structured, the model becomes confused. So building a RAG system is not only about connecting components. It is about managing these details.

Every retrieved chunk adds tokens. More tokens increase cost. They also increase latency. So you need to be selective. You include what matters. You exclude what does not. This again becomes an exercise in balance.

RAG changes how models behave. It shifts them from relying on memory to using context. From static knowledge to dynamic information. And that shift makes systems more practical. Because most real-world data changes. Policies update. Products evolve. Conditions shift. RAG allows the system to stay current without retraining.

Retrieval is not about making the model smarter. It is about giving the model better information. At the right time. And once you understand that, you stop thinking about models as isolated tools. You start thinking about systems that combine data, search, and generation. And that is what makes modern AI work in practice.