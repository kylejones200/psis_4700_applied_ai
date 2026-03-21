---
Title: How Models Learn
Draft: False
Date: 2026-03-21
Week: 2
Weight: 04
---

Now that we have a clear picture of data, we can move to the next question: what does it actually mean for a model to learn?

People often imagine learning as something deliberate—a student studies a concept, understands it, and applies it later. Models do not work that way. They do not understand in the human sense. They adjust. That is the core idea. A model learns by changing numbers. Those numbers determine how strongly different pieces of input influence the output. When you hear terms like weights and bias, that is what they refer to: parameters that shape how the model reacts to what it sees.

At the beginning, those numbers are essentially random. The model has no useful behavior. If you give it an input, its output is little better than a guess. Then the process begins. The model makes a prediction, compares it to the correct answer, and measures how far off it was. That difference is called the error. And then, very slightly, the model adjusts its internal numbers to reduce that error. That is one step. Then it repeats—again and again, thousands of times, millions of times, sometimes billions.

Over time, those small adjustments accumulate into something meaningful. The model begins to respond differently to different inputs. It starts to capture patterns—not because it was told what those patterns are, but because adjusting its parameters in response to error led it there. That is learning. It is not memorization of specific answers. It is a gradual shaping of behavior.

Imagine a very simple task. The model sees the phrase "good morning" and tries to predict the next word. At first, it might produce something random. Then it sees the correct continuation—maybe "everyone" or "sunshine"—and adjusts its parameters so that next time it is slightly more likely to produce something similar. It repeats the process with many examples. Each word shifts the model a little. Over time, the system becomes better at predicting what follows what. And that same process scales up: instead of a few phrases, the model sees massive amounts of text; instead of a few adjustments, it makes billions. But the mechanism stays the same. Prediction, comparison, adjustment—that loop is the engine of learning.

Look more closely at the pieces inside that loop. The weights control how strongly different inputs influence the output. If a feature is important, its weight grows; if it is not useful, its weight shrinks. The bias provides a baseline, shifting the output in a consistent direction independent of the input. Together, weights and bias define how the model interprets what it sees. But they do not adjust themselves automatically. The system needs a way to measure how wrong it is. That is where the loss function comes in.

The loss function takes the model's prediction and the correct answer and produces a number—the error. A larger error means the model is further from the correct behavior; a smaller error means it is closer. Training becomes a process of reducing that number.

Imagine this visually. Picture a landscape of hills and valleys. Each point represents a different set of model parameters; the height represents the error. High points mean large error; low points mean small error. Training is like placing a ball on that landscape and letting it roll downhill. The ball moves in the direction that reduces error. Eventually it settles into a valley where the error is relatively low. That is the state the model reaches after training. This process is often described as gradient descent, but you do not need the math to understand it. You only need the intuition: the model searches for a configuration of parameters that minimizes error.

There is an important constraint in all of this. The model can only learn from the data it sees. If the data is clean, balanced, and representative, the model can learn patterns that generalize to new situations. If the data is noisy, biased, or incomplete, the model learns those problems as well. So the quality of the data sets the ceiling for the model. This connects directly to what we discussed earlier: you cannot fix bad data with a better model.

Suppose you are training a model to distinguish between cats and dogs. At the start, the model guesses randomly. It has no concept of whiskers, ears, or fur. But as it sees more examples, it begins to associate certain visual patterns with the label "cat" and others with "dog." Those associations are encoded in the weights. The model does not know what a whisker is in a human sense, but it learns that certain patterns in the data tend to appear with certain labels. That is enough to make accurate predictions.

A good model does not memorize the training data. It learns patterns that it can apply to new data. This ability is called generalization. If a model only memorizes, it will perform well on the examples it has seen but fail on new ones. If it generalizes, it can handle inputs it has never encountered before. That is what we want.

There is a tradeoff hidden here. A model with very few parameters is simple; it may not capture all the patterns in the data and may underfit. A model with many parameters is flexible and can capture complex patterns, but it may also capture noise and overfit. So learning involves finding a balance—enough capacity to capture real patterns, but not so much that the model chases random variation. This balance shows up again and again in AI, and it connects back to evaluation, which we will cover next.

Before we move on, hold onto a simple mental model. A model is a system that adjusts internal numbers to reduce error on examples. That is all it is. Everything else—the architecture, the scale, the application—builds on that core process. If you understand that loop, you understand how models learn. And that understanding will make everything that follows much easier to reason about.