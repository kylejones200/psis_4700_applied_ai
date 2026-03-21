---
Title: Prompt Engineering
Draft: False
Date: 2026-03-21
Week: 5
Weight: 10
---

Now that you understand how language becomes tokens and how tokens become predictions, the next question becomes practical. How do you control what the model produces? Because the model is capable, but it is not directed on its own. It follows the structure you give it. And that structure comes from the prompt. So prompting is not decoration. It is how you define the task. It is how you shape behavior in real time.

Think of the model as an assistant. A very capable assistant. But also a very literal one. If you give vague instructions, the assistant will interpret them broadly. If you give precise instructions, the assistant will behave more consistently. So the quality of the output depends heavily on the quality of the input. That is the core idea.

If you say "summarize this," the model will produce a summary. But what kind of summary? Short or long. Formal or casual. Focused on key points or narrative flow. The instruction does not say. So the model fills in the gaps based on patterns. If instead you say "summarize this in three sentences, focus on key decisions, and use plain language," the output changes. Not because the model became smarter. Because you constrained the task.

You can assign a role. You tell the model what perspective to take—a policy analyst, a teacher, a support agent. That changes tone and focus. You can provide examples. You show what a good output looks like. The model then matches that pattern. You can also guide reasoning. You can ask the model to work step by step. This often improves consistency for more complex tasks. But these are not tricks. They are ways of specifying the problem more clearly.

The model has learned patterns from data. Those patterns include both good and bad behavior. Prompting steers which patterns are activated. Alignment shapes what patterns are preferred overall. So if the model is not aligned, prompting alone cannot fix it. And if prompting is weak, even an aligned model may produce poor output. The two work together.

You ask the model to write a hiring ad. If the prompt is vague, the model may produce language that reflects biases in the data it learned from. If the model has been aligned, it may avoid some of those patterns. But if you also provide a clear instruction—inclusive tone, neutral language, focus on skills—the output improves further. So structure matters.

Prompting is iterative. You rarely get the best result on the first attempt. You try. You observe. You adjust. You refine. This is not a weakness. It is part of the process. Because you are not only asking a question. You are designing an interaction.

In practice, you do not rely on a single prompt. You create templates. You define slots. You insert variables. This creates consistency. It allows you to scale. Because every request follows the same structure. With different inputs.

If the model can produce harmful or inappropriate content, you need controls. You can filter inputs. You can constrain outputs. You can define rules that the model must follow. This is part of the prompt design. But it also extends beyond it. Into policy and evaluation.

Prompting is the interface between human intent and model behavior. It translates what you want into something the model can act on. And small changes in that translation can have large effects.

If tokens are the foundation, prompting is the control layer. It determines how the model uses what it knows. And learning how to prompt well is not about memorizing patterns. It is about clarity. Being precise about what you want. Being aware of what the model can and cannot do. And shaping the interaction accordingly. Because in the end, the model will do exactly what you ask. The question is whether you asked the right thing.