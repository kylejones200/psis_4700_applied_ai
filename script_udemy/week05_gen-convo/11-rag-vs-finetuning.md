---
Title: RAG vs Finetuning
Draft: False
Date: 2026-03-21
Week: 5
Weight: 11
---

Up to this point, we have treated the model as something fixed. You give it input, shape that input with prompts, and it produces output. Now we need to answer a different question: what happens when the model does not know enough? Because this shows up quickly in practice. The model is strong, but it does not know your data. It does not know your policies. It does not know what changed yesterday. So you need a way to extend it. There are two primary ways: you can give it access to external information at runtime, or you can change the model itself. These correspond to retrieval and fine-tuning.

Let's start with retrieval. The idea is simple. When a user asks a question, the system does not rely only on what the model has learned. It searches for relevant information—documents, records, policies—retrieves it, and inserts it into the prompt. Now the model is not guessing; it is reasoning over provided context. The model itself does not change, but what it sees changes. And that is often enough, because most real-world problems are not about general knowledge. They are about specific, changing information.

This approach has a few important properties. It stays current: if the data changes, you update the documents and the model immediately reflects that change. It is transparent: you can show the source of the answer and trace where the information came from. And it is flexible: you can apply it across many use cases without retraining.

Now contrast that with fine-tuning. Fine-tuning changes the model itself. You take a base model and train it further on your data—not from scratch, but enough to shift its behavior. It learns your style, your structure, your domain. That knowledge becomes part of the model. So instead of reading external documents each time, the model carries that knowledge internally.

Fine-tuning has different properties. It can be more consistent: the model produces outputs in a specific format or tone. It can be faster at runtime because it does not need to retrieve context. But it is also less flexible. If the data changes, you need to retrain. If the task changes, you may need to retrain again. And it is more expensive—in time, in compute, in maintenance.

This leads to a simple way to think about the difference. Retrieval adds knowledge at runtime; fine-tuning changes knowledge at training time. One is dynamic; the other is static.

If you are building a system that answers questions about company policy, the information changes. Policies are updated; documents evolve. So retrieval makes sense—you want the system to read the latest version. If you are building a system that must follow a strict format or tone across millions of outputs, fine-tuning may help. You want the behavior to be consistent. This is not an either-or decision. In many systems, you use both. You fine-tune for structure and behavior; you use retrieval for knowledge and freshness. This layered approach reflects how real systems are built.

Retrieval is usually cheaper to maintain. You update documents; you do not retrain models. Fine-tuning requires more upfront investment and ongoing updates. So the choice depends on your constraints: how often does the data change, how important is consistency, how much control do you need.

When a model fails to answer correctly, do not assume you need a better model. Ask what the model is missing. If it lacks information, add context. If it lacks structure, adjust behavior. Choose the method that fits the problem.

Models are no longer static tools. They are components in systems that combine prompting, retrieval, and adaptation. Understanding how these pieces fit together is what allows you to move from using AI to designing it. And that is where the real shift happens.