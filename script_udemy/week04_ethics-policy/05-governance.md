---
Title: Governance
Draft: False
Date: 2026-03-21
Week: 4
Weight: 05
---

Up to this point, we have talked about designing systems, evaluating them, and putting structure around them. Now we need to take a different stance. Instead of asking whether the system works, we ask how it fails. Because every system fails. The only question is when, and how visible that failure will be. Safety begins with that assumption. You do not wait for problems to appear in production. You try to find them in advance. Deliberately. Systematically. That is what red teaming is.

Red teaming means you treat your own system as a target. You try to make it behave badly. You try to expose weaknesses. You look for ways it can produce harmful, incorrect, or unintended outputs. Not because you expect users to behave that way. But because some will. And because accidents will happen. So the goal is not to prove that the system works. It is to prove that it fails in ways you understand and can control.

You start by defining risk scenarios. What could go wrong? Could the system reveal private data? Could it produce biased output? Could it be manipulated into ignoring safeguards? These scenarios become your test cases. Then you act. You attempt to exploit the system. You provide inputs designed to confuse it. You try to bypass its constraints. You push it into edge cases. And you observe what happens. Every failure is recorded. Not as a problem to hide. As information to use. Because each failure tells you something about the system. Where it is brittle. Where assumptions break. Where controls are weak. Then you fix. You adjust the model. You add guardrails. You refine prompts or constraints. And then you test again. This cycle repeats. Because safety is not a one-time check. It is an ongoing process.

One common risk is prompt manipulation. If a system takes instructions from users, those instructions can be crafted to override intended behavior. Another is data leakage. The system may expose information that should remain private. Especially if it has access to sensitive data. Another is what people call jailbreaking. Users find ways to bypass restrictions and force the system into prohibited behavior. And then there is harmful content—outputs that are toxic, misleading, or unsafe. Each of these risks reflects the same underlying issue. The system is operating based on patterns, not understanding. So it can be guided into behavior that was not intended.

If alignment defines what the system should do, red teaming tests whether it actually does that under pressure. If governance defines structure, red teaming tests whether that structure holds. If evaluation measures performance, red teaming measures resilience. So this is not separate work. It is part of the same system.

You deploy a model that answers questions based on internal documents. In normal use, it performs well. It retrieves relevant information and produces useful responses. But a red team tests it differently. They ask questions designed to extract sensitive information. They phrase inputs in ways that confuse retrieval. They combine instructions to override constraints. And they discover that, under certain conditions, the system reveals data it should not. That is a failure. But it is also an opportunity. Because finding that failure before deployment prevents a larger problem later.

Safety work can feel uncomfortable. It focuses on what can go wrong. It challenges assumptions. It exposes weaknesses. But that discomfort is the point. Because systems that are only tested under ideal conditions are not ready for the real world.

Red teaming should be built into the lifecycle. During design, you anticipate risks. During development, you test for them. During deployment, you monitor for new ones. And after deployment, you continue to probe. Because users change. Environments change. And new failure modes emerge.

Safety is quality assurance for AI systems. Not in the sense of checking whether the system works. In the sense of checking whether it works under stress. Whether it behaves within acceptable bounds. Whether it fails in ways you can manage. Because in the end, trust is not built on perfect performance. It is built on predictable behavior. Knowing how the system will respond. Even when things go wrong. And that is what red teaming gives you. Not confidence that the system will never fail. Confidence that you understand its limits.