---
Title: Alignment Details
Draft: False
Date: 2026-03-21
Week: 4
Weight: 03
---

Up to this point, we have talked about alignment as a gap between what a system is asked to do and what people actually want. Now we need to look at how that gap appears in practice. And the most common way it appears is through bias.

Bias is not a rare failure. It is a natural outcome of how systems are built. Because models learn from data, and data reflects history. If that history contains imbalance, exclusion, or inconsistency, the model will absorb those patterns. And then it will reproduce them. Often faster. Often at scale. So bias is not something you add to a system. It is something you have to detect and manage.

Imagine a hiring model trained on past hiring decisions. If those decisions favored a particular group, the model will learn that pattern. It will rank similar candidates higher. Not because the model prefers that group. But because the data does. The math is neutral. The outcome is not. This is an important shift in thinking. The source of bias is rarely the algorithm itself. It is the data and the design choices around it.

Bias can enter at several points. It can appear in sampling—if certain groups are missing or underrepresented, the model cannot learn how to treat them accurately. It can appear in labeling—if human judgments are inconsistent or influenced by assumptions, those judgments become part of the training signal. It can appear in the model itself—certain structures may favor patterns that appear more frequently. And it can appear in deployment—if the system is used in a context different from where it was trained, performance may vary across groups. So bias is not a single event. It is a chain. And each link matters.

Once you recognize that, the question becomes what to do about it. The first step is visibility. You cannot fix what you cannot see. So you test the system across different groups. You compare outcomes. You look for differences in error rates. You examine where the model performs well and where it struggles. Fairness metrics provide a way to quantify those differences. Not to eliminate them entirely, but to understand them.

Once you see those differences, you face a choice. Do you adjust the data? Do you adjust the model? Do you adjust the threshold? Each option has consequences. Removing biased data may reduce performance. Changing thresholds may affect different groups differently. So fairness is not free. It requires tradeoffs. And those tradeoffs must be made explicitly.

Fairness and accuracy are not always aligned. You may improve fairness and see a drop in traditional performance metrics. But at the same time, you increase trust. You reduce harm. So the question becomes what you are optimizing for. And that takes you back to alignment. What does success mean in this system?

If a system produces different outcomes for different groups, people will ask why. And if you cannot explain it, trust breaks down. So transparency is not only about clarity. It is about accountability. You need to show how decisions are made. What inputs matter. What factors influence the outcome. This does not require exposing every detail of the model. But it does require making the system understandable at the level that matters.

When a system causes harm, someone is accountable. It may be the developer. It may be the organization. It may be the operator. But it is not the model. So responsibility cannot be deferred. You have to define who owns the outcome. Who reviews the system. Who has the authority to change or stop it. Without that clarity, problems persist.

Before building a system, you should ask. Could this system create harm? Could it reinforce existing inequalities? Could it affect people who have no control over it? These questions do not prevent you from building. They guide how you build.

Even if you remove explicit sensitive attributes, like race or gender, the model may still infer them through proxies. Location. Education. Income. These variables can correlate with sensitive attributes. So the system can still produce biased outcomes. This is why simply removing certain fields is not enough. You have to examine the relationships within the data.

Bias is not a bug. It is a property of systems that learn from imperfect data. The goal is not to eliminate it completely. The goal is to detect it, reduce it, and explain it. And to make conscious decisions about how much risk is acceptable.

If you do not actively look for bias, you will not find it. And if you do not find it, the system will carry it into every decision it supports. So responsible AI is not passive. It requires attention. Measurement. And willingness to act when problems appear. That is how alignment becomes real. Not in theory. In practice.