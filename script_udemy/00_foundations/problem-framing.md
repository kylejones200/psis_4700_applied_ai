---
Title: Problem Framing
Draft: False
Date: 2026-03-21
Week: 0
Weight: 00
---

Let’s shift from models to purpose. Imagine a warehouse that ships orders. Some shipments arrive late. Late deliveries lead to refunds, complaints, and lost trust. The team wants to reduce late shipments. That is the starting point—not the model, not the data, but the problem. Because without a clear problem, everything else becomes disconnected.

The model does not define the problem. The model supports the response to the problem. This sounds obvious, but it is often ignored. Teams start with tools. They ask what the model can do instead of asking what needs to be solved. That leads to solutions without purpose. So always begin with the problem.

Every business problem has three elements: a decision, an outcome, and a cost of being wrong. Someone must choose an action. That action affects an outcome. And mistakes carry consequences. If any of these are missing, the problem is incomplete.

“We want insights” is not a problem. It does not define action. It does not define outcome. A real problem connects prediction to decision. For example, predicting late shipments so the team can intervene. That is actionable.

No solution exists in isolation. Budget matters. Time matters. Skills matter. Regulation matters. A perfect solution that ignores constraints is not useful. So design must reflect reality.

A strong practice is to write the problem in one sentence: who makes the decision, what decision they make, and what happens if they are wrong. Agreement on this sentence aligns the team and allows work to begin.

In our example, the problem is late shipments. The decision is whether to escalate a shipment before failure. Now the problem becomes concrete.

Once the problem is clear, the task follows: estimate the probability that a shipment will arrive late. This connects directly to the decision. A good task has a clear target—a yes or no outcome, a probability, a score, or a rank. Clarity here drives everything else.

The model must only use information available at decision time. Future data creates unrealistic performance. This is a common mistake, and it leads to failure in production.

What are you predicting? A shipment? A customer? A route? The unit defines the structure of the data and the decision. Sometimes the data does not match the problem. Targets may be missing. Time boundaries unclear. Units misaligned. Then the design must change.

Clear tasks define what to build, what to measure, and how results are used. This prevents wasted effort.

Models learn from labels and features. These define the structure of the problem. The label is the outcome: did the shipment arrive late? Each past example has a known result. Features describe the situation at decision time—distance, history, weight, time. They must exist before the outcome. If the model sees the answer in the inputs, it will cheat. Performance looks strong. Reality fails. This is leakage.

Not all features help. Some add noise. Some duplicate information. Good features reflect real mechanisms.

You compare predictions to real outcomes. You study success and failure. You ask if it improves decisions. Problem, task, label, feature, outcome. This chain defines applied AI.
