---
Title: Chatbots Advanced
Draft: False
Date: 2026-03-21
Week: 5
Weight: 14
---

Up to this point, we have looked at models, prompts, and retrieval as parts of a system. Now we place them inside something people actually use: a conversation. And this changes the design in a subtle but important way. Because a conversation is not a single input and output. It is a sequence. Each step depends on what came before. Each response shapes what comes next. So the system has to maintain context. It has to remember. And it has to decide what matters enough to keep.

When a user sends a message, the system interprets it. What is the user trying to do? What information is required? In traditional systems, this was broken into pieces. Intent detection. Slot filling. Dialogue management. Separate components handled each step. Now, with large language models, much of that is handled by a single system. The model reads the input and produces a response. Understanding and generation happen together. That simplifies the architecture. But it does not remove the need for structure.

Each turn in a conversation adds tokens. The system cannot keep everything forever. There is a limit. So it has to decide. What should be kept. What should be summarized. What can be dropped. This is not only a technical constraint. It affects behavior. If important context is lost, the model may respond incorrectly. If irrelevant context is kept, the model may become confused. So memory design becomes part of the system. You may keep recent turns. You may summarize older ones. You may store key facts separately. Each choice shapes how the conversation unfolds.

In many systems, the model does not rely only on the conversation. It also retrieves external information—policies, documents, records. This grounds the response. It connects the conversation to real data. So the system becomes layered. Conversation history. Retrieved context. Prompt structure. Model output. All working together.

Because the system is interactive, users can push it in unexpected directions. They can ask questions that are unsafe. They can try to manipulate the system. They can provide inputs that contain hidden instructions. So you need guardrails. You filter inputs. You constrain outputs. You define what the system should not do. And you test those constraints. Not once. Continuously.

In a simple model, you measure accuracy. In a conversation, that is not enough. You need to ask. Did the system help the user achieve their goal? Was the response coherent? Was it safe? Was the user satisfied? These are harder to measure. But they matter more. Because the system is judged as an experience. Not a single prediction.

Conversational systems fail in specific ways. They go off topic. They produce inconsistent answers. They hallucinate. They respond in ways that are unsafe. So you need fallback strategies. If the system is unsure, it should ask a clarifying question. If the request is out of scope, it should say so. If the situation requires human judgment, it should escalate. These behaviors are part of the design. Not afterthoughts.

Every turn in a conversation consumes tokens. Long conversations increase cost. So you need to manage that. Summarize when needed. Limit unnecessary context. Choose models that balance capability and efficiency. Because at scale, this becomes significant.

A conversational system is not a model. It is an orchestration. Input handling. Context management. Retrieval. Prompt design. Generation. Safety. Evaluation. Each part contributes. And failure in any part affects the whole.

Conversation is the interface people understand. It feels natural. It feels intuitive. But behind that simplicity is a structured system. One that must manage context, control behavior, and handle uncertainty. And if you design it well, the complexity disappears. The user experiences something that feels simple. Even though it is not. And that is what makes conversational AI effective.