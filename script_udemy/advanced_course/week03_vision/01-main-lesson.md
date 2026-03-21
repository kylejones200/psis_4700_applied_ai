---
Title: Main Lesson
Draft: False
Date: 2026-03-21
Week: 3
Weight: 01
---

Let's begin with a simple idea. Humans understand images instantly—you look at a picture and recognize objects, context, and relationships in a fraction of a second. Computers do not see that way. A computer sees an image as a grid of numbers, where each number represents a pixel value with no inherent meaning and no concept of "cat" or "car" or "person." Computer vision is the process of turning that grid of numbers into meaning.

The key shift in modern vision systems mirrors what you saw in NLP: we moved from handcrafted rules to learned representations. This week focuses on how that learning happens and how we can take models that already understand images and adapt them to our own problems. In practice, you rarely start from scratch; you start from something that already sees.

To understand the field, it helps to separate the main types of problems. The simplest task is classification—you take an image and ask what is in it, producing a single label. More complex is detection, where you ask where the objects are and need bounding boxes, locations, and multiple outputs. More detailed still is segmentation, where you ask which pixels belong to which object and gain pixel-level understanding. Each step increases complexity and requires a different kind of model output, so when you approach a problem, the first question is not which model to use but what kind of output you need, because that defines everything that follows.

Let's ground this in how images are represented. An image is a grid where each cell is a pixel, and each pixel has values—usually three for color (red, green, and blue)—so an image becomes a three-dimensional array of width, height, and channels. Before feeding this into a model, you often normalize it by scaling pixel values into a standard range. This matters because models are sensitive to scale: if inputs vary widely, training becomes unstable, and normalization ensures consistency. This is one of those small steps that has a large impact.

One of the most powerful ideas in vision is data augmentation. Instead of collecting more data, you create variations of existing data by flipping, rotating, cropping, and adjusting colors. These transformations simulate new examples and help the model generalize. If a model only sees a cat facing one direction, it may struggle when the cat is rotated; augmentation exposes the model to those variations so it learns the concept of "cat" rather than a specific orientation. This becomes especially important when you have limited data, because augmentation effectively expands your dataset.

Now we move into how models actually learn from images. Convolutional neural networks, or CNNs, are the foundation: they use filters to scan across the image, and each filter detects patterns—edges, textures, shapes. Early layers detect simple patterns, and deeper layers combine those into more complex features; a shape becomes a face, a texture becomes fur. This hierarchy allows the model to build meaning step by step. Pooling layers reduce the size of the representation while keeping important information and reducing complexity. Together, these layers transform raw pixels into structured features, and that is how the model learns to see.

As models became deeper, a problem appeared: training became difficult and performance degraded as networks grew. ResNet solved this with a simple idea—skip connections. Instead of forcing each layer to learn from scratch, the model allows information to flow directly across layers, which stabilizes training and allows much deeper networks that capture more complex patterns. ResNet became a standard because it made depth practical, and many modern models build on this idea.

Now we see a shift similar to NLP: transformers move into vision. Instead of processing images with convolutions, they treat images as sequences. You split the image into patches, each patch becomes a token, and then you apply attention so each patch considers every other patch. This allows the model to capture global relationships, not just local patterns. ViT models perform well, especially with large datasets, but they require more data to learn effectively, so the choice between CNNs and transformers depends on context—data size, compute resources, and problem type.

One of the most practical ideas in vision is transfer learning. Instead of training a model from scratch, you start with a model trained on a large dataset like ImageNet that already understands basic visual features—edges, shapes, textures. You then adapt it to your task, which reduces the amount of data you need, reduces training time, and improves performance. Think of it as starting with someone who already knows how to see and teaching them a new task, rather than teaching vision from scratch.

When using transfer learning, you have a choice. You can freeze the backbone—keep the pretrained layers fixed and only train the final layers—which is called feature extraction. Or you can fine-tune the entire model and update all layers. Feature extraction is safer with small datasets, while fine-tuning can achieve better performance with more data, so the decision depends on how much data you have and how different your task is from the original.

Before training, the dataset must be prepared. You split into training, validation, and test sets, check class balance (because if one class dominates, the model may ignore others), and track metadata such as where images came from and how they were labeled. Poor data preparation creates problems that no model can fix, so this is one of the most important steps.

Once your dataset is prepared, you need a way to feed it into the model efficiently—that is the role of dataloaders. At a simple level, a dataloader batches your data so you process many images at once instead of one at a time, which allows GPUs to work efficiently. But dataloaders also shuffle data during training to prevent the model from learning patterns based on order rather than content, and they apply transformations on the fly so augmentation can happen during loading and each epoch sees slightly different versions of the data. Think of the dataloader as the pipeline between your dataset and your model: if it is inefficient, training slows down; if it is inconsistent, results become unreliable. Even though it feels like infrastructure, it directly affects model performance.

At every training step, the model makes a prediction and the loss function measures how wrong that prediction is. For classification, the most common loss is cross-entropy, which penalizes incorrect predictions more strongly when the model is confident and wrong. That matters because a model that is unsure is less dangerous than one that is confidently incorrect. Different tasks require different loss functions—detection and segmentation use more complex losses because they involve spatial information. The key idea is that the loss function defines what the model cares about; if you choose the wrong loss, the model optimizes the wrong objective, so this is not just a technical detail but a design decision.

Once you have a loss, you need a way to reduce it—that is the role of the optimizer. Optimizers adjust the model's weights to minimize the loss, and two common choices are SGD and Adam: SGD is simple and stable, while Adam adapts learning rates automatically. Both work well in practice, but the learning rate matters as much as the optimizer. If it is too high, training becomes unstable; if it is too low, training becomes slow, so learning rate schedules are used—you start higher, then reduce over time, which allows fast progress early and fine adjustments later.

Returning to evaluation in the context of vision, accuracy is the simplest metric but does not tell the full story. Top-k accuracy is often used: instead of asking if the top prediction is correct, you ask if the correct answer appears in the top k predictions, which is useful when there are many classes. Precision and recall per class become important when classes are imbalanced, because some categories may perform well while others perform poorly, so evaluation must go beyond a single number. The confusion matrix becomes a powerful diagnostic tool: it shows how often each class is predicted as each other class, so if cats are often predicted as dogs, you know the model struggles to distinguish them. That insight leads to action—you may collect more data for those classes, improve labeling, or adjust the model—and this is where evaluation turns into improvement.

As models become more powerful, they risk overfitting and memorizing training data instead of learning general patterns. Regularization helps prevent this: weight decay penalizes large weights, dropout randomly removes parts of the network during training, and label smoothing reduces overconfidence. Each of these techniques encourages the model to generalize, and that is the goal—not perfect performance on training data but reliable performance on new data.

Training can go too far. At first performance improves, then it plateaus, then it declines as the model overfits. Early stopping monitors validation performance and stops training when it stops improving, which saves time and prevents overfitting. It also highlights an important idea: more training is not always better; better training is better.

Training large models can be slow and memory-intensive, and mixed precision addresses this by using lower precision numbers for most computations, which speeds up training and reduces memory usage. But it introduces risk—lower precision can cause numerical instability, and values may become too large or too small—so you must monitor training carefully for issues like NaNs or unstable loss. This is a tradeoff between efficiency and stability.

Many real-world problems do not have large datasets, so you need strategies for small data. Data augmentation becomes more aggressive, you freeze most of the model and only train a few layers, and few-shot learning techniques help the model generalize from limited examples. The key idea is to maximize what you can learn from limited data and to avoid overfitting at all costs.

Once the model is trained, it must be saved—including weights and architecture—and different formats allow deployment in different environments. ONNX provides portability, TorchScript allows optimization, and the goal is to move from training to production without losing behavior, because a model that cannot be deployed has no value.

Deployment introduces new constraints. Latency matters because users expect fast responses, and batch size affects throughput—larger batches improve efficiency but increase delay. Quantization reduces model size and speeds inference but may reduce accuracy, so you balance performance and cost. This is where engineering meets modeling.

Understanding model decisions builds trust. Grad-CAM highlights regions of the image that influenced the prediction, and saliency maps show which pixels matter. These tools help you verify that the model focuses on relevant features; if a model predicts "cat" based on background rather than the cat itself, that is a problem, and explainability reveals these issues.

Bias in data leads to bias in models. If your dataset lacks diversity, your model will struggle in those conditions—for example, a model trained on well-lit indoor images may fail in low-light environments. Fairness requires representation across demographics, environments, and contexts, and this is not only ethical but practical, because models must work in the real world.

The lab brings these ideas together: you will fine-tune a pretrained model, compare approaches, and analyze errors. This is where concepts become experience. Error analysis is where improvement happens—you look at misclassified images, identify patterns, and ask why. Maybe lighting affects performance; maybe certain angles confuse the model. These insights guide data collection and model changes.

Data issues often hide in plain sight. Duplicate images between splits create leakage, and label noise confuses the model. These problems inflate performance artificially and lead to failure in production, so data must be clean and well-organized.

When would you choose a transformer over a CNN? If you have large datasets and want global relationships, transformers may help; if you have limited data, CNNs may perform better. This is not about trends but about fit. When classes are imbalanced, models ignore rare cases—you can adjust loss functions, use focal loss to emphasize difficult examples, or resample data. Each approach ensures the model pays attention to what matters.

Models learn from labels, so if labels are inconsistent, the model learns inconsistency. Clear guidelines matter, multiple annotators help, and agreement checks ensure quality, because the model cannot learn better than the data it is given.

Data changes over time, and versioning tracks those changes to ensure reproducibility. If you report results, you must be able to reproduce them; otherwise you cannot trust them.

Quantization reduces model size and speeds inference by converting weights to lower precision, which is critical for deployment on constrained devices. But it introduces tradeoffs, so you must evaluate performance carefully. Some systems run on phones, sensors, and embedded systems with limited resources, so models must be optimized—smaller, faster, efficient—and this expands where AI can operate.

Explainability tools are helpful but not perfect. Heatmaps can be misleading and may highlight irrelevant regions, so you must interpret them carefully and use multiple methods when possible.

Mixed precision requires monitoring. Loss scaling helps maintain stability, and you must watch for numerical issues, because speed gains are only useful if results remain correct.

Experiments generate data—metrics, parameters, outputs—and tracking tools like MLflow organize this. They allow comparison across runs and support reproducibility; without tracking, you lose insight.

The reading list connects practice to theory: ResNet explains deep learning in vision, and ViT shows the transformer approach, providing deeper understanding. The assignment brings everything together—you fine-tune a model, test variations, and analyze errors. This is where learning becomes capability.
