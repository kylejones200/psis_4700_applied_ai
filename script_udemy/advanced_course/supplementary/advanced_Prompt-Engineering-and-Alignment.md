---
Title: Prompt Engineering and Alignment
Draft: False
Date: 2026-03-21
Week: 0
Weight: 00
---

At this point, you have seen what models can do. This session shifts to something more practical. How you shape that behavior in real use.

Because the model does not decide what to do on its own. It responds to how you frame the problem. The input you give it becomes the environment it operates in.

That means the quality of your output depends directly on the quality of your prompt.

Think about how you ask a colleague for help. If you say, “Can you take a look at this,” you get one kind of response. If you say, “Can you review this report and focus on clarity and tone for an executive audience,” you get a very different result.

The same principle applies here.

Prompting is not about tricks. It is about clarity. Structure. Intent.

And once you understand that, you stop guessing. You start designing.

Prompt engineering guides the model. Alignment ensures the model behaves in a way that reflects human expectations.

These are related but distinct ideas.

Prompting controls how the model interprets a specific task. Alignment controls how the model behaves across tasks.

You can think of prompting as giving instructions in the moment. Alignment as shaping long-term behavior.

Without prompting, the model may misunderstand what you want. Without alignment, it may produce outputs that are technically correct but inappropriate.

So both are required.

One gives direction. The other gives boundaries.

Let’s make this concrete.

The simplest technique is clear instruction. Say exactly what you want. “Summarize this email.” “Extract key risks.” “Translate to French.”

Clarity reduces ambiguity.

Role prompting adds context. “You are a policy analyst.” “You are a financial advisor.” This helps the model adopt a perspective.

Then there is structured reasoning. You ask the model to work through steps. “Let’s reason step by step.”

This does not change the model’s intelligence. It changes how it organizes its response.

A simple example helps.

If you ask, “What is the best investment?” you get a vague answer.

If you say, “You are a financial advisor. Evaluate three investment options based on risk, return, and time horizon,” the output improves immediately.

The difference is not the model. It is the prompt.

Models learn patterns from data. They do not understand values.

That creates risk.

They may produce biased language. They may generate unsafe content. They may give confident but incorrect answers.

Alignment addresses this.

It shapes behavior so the model reflects human expectations. Ethical standards. safety constraints.

Without alignment, the model follows patterns. With alignment, it follows intent.

And this becomes critical in production systems.

Because the cost of a bad output is not theoretical. It is real.

One of the main methods for alignment is reinforcement learning from human feedback.

Humans review model outputs. They rate them. Good. bad. acceptable. unsafe.

The model learns from those ratings.

Over time, it prefers responses that align with human judgment.

This process does not make the model perfect. It makes it more consistent with expectations.

Think of it as training behavior, not knowledge.

A model may know how to write many types of content. RLHF helps it choose which type is appropriate.

Let’s make this tangible.

You ask the model to write a hiring ad.

An unaligned model may produce biased language. It may include phrasing that excludes certain groups.

An aligned model produces inclusive language. It avoids bias. It reflects compliance requirements.

The difference is not the task. It is the behavior.

That is alignment in action.

Prompting and alignment work together.

Prompting shapes the immediate response.

Alignment shapes long-term behavior.

Together, they define how the system speaks, reasons, and interacts.

And the key insight is simple.

You are not only using the model. You are guiding it.