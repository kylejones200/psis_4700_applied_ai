---
Title: Tokens Tokenization
Draft: False
Date: 2026-03-21
Week: 5
Weight: 09
---

Up to this point, we have talked about language models as if they understand text. Now we need to strip that away and look at what actually happens. Because the model does not see words. It sees tokens.

A token is a small piece of text. Sometimes it is a full word. Sometimes it is part of a word. Sometimes it is punctuation. When you type a sentence, the system does not process it as a sentence. It breaks it apart. Into tokens. Each token is then mapped to a number. That number represents the token in the model's vocabulary. So the sentence becomes a sequence of numbers. And that sequence is what the model reads. This may seem like a small detail, but it changes how you think about everything that follows. Because once text becomes numbers, the model can operate on it. It can compare patterns. It can learn relationships. It can predict what comes next. But it is always working at the level of tokens. Not meaning in the human sense.

Take a simple word like "cats." You might think of it as one unit. The model may not. It might split it into "cat" and "s." Each piece becomes a separate token. Each token has its own number. So even basic words can be broken down into parts. This allows the model to handle language more flexibly. It can recognize patterns across variations. "Cat," "cats," "catlike"—all share pieces.

Once the text is converted into tokens and then into numbers, those numbers are transformed again. They become embeddings. An embedding is a vector. A list of numbers that represents the token in a space where similar meanings are closer together. So words that are used in similar contexts end up near each other in that space. That is how the model captures relationships. Not through definitions. Through proximity.

The model does not store language as rules. It stores it as patterns in a numeric space. And when it generates text, it is navigating that space. Choosing the next token based on what is likely given the tokens that came before.

Every token counts. The model has a limit on how many tokens it can process at once. That is the context window. If your input exceeds that limit, the model cannot consider all of it. So you have to decide what to include. What to remove. What to summarize. Because context is not free. It consumes tokens. And tokens cost money. So design becomes an exercise in compression. You want to include enough information to guide the model. But not so much that you waste capacity.

More tokens mean more computation. More computation means slower responses. So there is a tradeoff. More context can improve quality. But it increases cost and time. And that tradeoff appears in every system you build.

You type a sentence. The system breaks it into tokens. Those tokens become numbers. Those numbers become embeddings. The model processes those embeddings through layers. And then it predicts the next token. That token is converted back into text. And you see the result. At every step, the system is working with numbers. Meaning is something that emerges from patterns in those numbers. Not something the model explicitly understands.

If you understand tokens, you understand the foundation of language models. You understand why context matters. Why prompts matter. Why cost matters. Because everything flows through this representation. Language becomes numbers. Numbers become patterns. Patterns become output. And that is the mechanism behind everything you see.