# Week 3 — Computer Vision
Focus: transfer learning with ResNet/ViT on images

![](images/how-computers-see-with-cats.png)

> Computer vision enables machines to interpret and understand visual information. This week focuses on transfer learning with modern architectures like ResNet and Vision Transformers.
---

## CV Tasks Overview
Classification, detection, segmentation

> CV tasks include classification (what's in the image?), detection (where are objects?), and segmentation (which pixels belong to what?). Each requires different model outputs and training approaches.
---

## Image Basics
Channels, resolution, normalization

![](images/computer-matrix-vision.png)

> Images are represented as grids of pixels with channels for color (typically RGB). Normalization puts pixel values in standard ranges that models expect, typically [0,1] or [-1,1].
---

## Data Augmentation
Flips, crops, color jitter to reduce overfitting

> Data augmentation artificially increases training data diversity through random flips, crops, rotations, and color adjustments. This helps models generalize by seeing variations of each image.
---

## CNN Fundamentals
Convolutions, pooling, feature hierarchies

> Convolutional Neural Networks process images through convolution layers that detect features, pooling layers that reduce size, creating hierarchical feature representations from edges to complex patterns.
---

## Residual Networks (ResNet)
Skip connections enable deeper training

> ResNet introduced skip connections that add input directly to output, enabling training of very deep networks without degradation. This architectural innovation was crucial for modern vision models.
---

## Vision Transformers (ViT)
Patch embeddings + transformer encoder

> Vision Transformers treat images as sequences of patches, applying transformer attention mechanisms from NLP. ViT has become competitive with CNNs, especially with large datasets.
---

## Transfer Learning
Start from pretrained weights  
Fine-tune on task

> Transfer learning starts with weights pretrained on ImageNet (millions of labeled images), then fine-tunes on your specific task. This works with thousands rather than millions of training examples.
---

## Feature Extractor vs Full Fine-Tune
Freeze backbone or train all layers

![](images/Sentinel-2_L2A-765644962654613-timelapse.gif)

> Feature extraction freezes the pretrained backbone and only trains new layers for your task. Full fine-tuning updates all weights but requires more data and computation.
---

## Dataset Preparation
Train/val/test split  
Class balance  
Metadata

> Dataset preparation requires splitting into train/validation/test sets, balancing classes, and maintaining metadata. Poor data organization causes more problems than algorithm choices.
---

## Dataloaders
Efficient batching, shuffling, preprocessing

> Dataloaders efficiently batch images, shuffle training data, and apply augmentation on-the-fly. Proper batching enables GPU acceleration and smooth training.
---

## Loss Functions
Cross-entropy for classification  
Others per task

> Loss functions like cross-entropy for classification measure how wrong predictions are, guiding model updates. Different tasks require different loss functions aligned with objectives.
---

## Optimizers
SGD/Adam  
Learning rate schedules

> Optimizers like SGD and Adam adjust model weights to minimize loss. Learning rate schedules gradually reduce step size for fine-grained optimization near convergence.
---

## Evaluation Metrics
Accuracy, top-k  
Precision/recall per class

> Evaluation metrics include accuracy and top-k accuracy (is correct answer in top k predictions), plus precision and recall for each class to identify which categories struggle.
---

## Confusion Matrix in CV
Spot class confusion  
Data issues

> Confusion matrices for vision show which classes are confused with each other. If cats and dogs are often mixed up, you might need more examples distinguishing them.
---

## Regularization
Weight decay, dropout, label smoothing

> Regularization techniques including weight decay, dropout, and label smoothing prevent overfitting. Models that memorize training images won't generalize to new images.
---

## Early Stopping
Monitor val loss/metric to halt overfit

> Early stopping monitors validation performance and halts training when it stops improving. This prevents overfitting while using computational resources efficiently.
---

## Mixed Precision
Speed up training  
Watch for stability

> Mixed precision training uses lower precision numbers (float16) for speed and memory efficiency while maintaining accuracy. Watch for numerical instability in some operations.
---

## Small Data Strategies
Data augmentation  
Freeze backbone  
Few-shot

> Small data strategies include aggressive augmentation, freezing most of the pretrained model, and few-shot learning techniques. You can often achieve good results with hundreds rather than thousands of examples.
---

## Model Export
Save state dict  
Export to ONNX/TorchScript as needed

> Model export saves trained weights for deployment. Formats like ONNX or TorchScript enable deployment on different platforms and optimization for production.
---

## Deployment Considerations
Inference latency, batch size, quantization

> Deployment considerations include inference latency, batch size for throughput, and quantization for smaller models. Production requirements often differ from research settings.
---

## Explainability in CV
Grad-CAM  
Saliency to inspect focus regions

> Explainability in CV uses techniques like Grad-CAM that visualize which image regions influenced predictions. Saliency maps help verify models focus on relevant features.
---

## Fairness in Datasets
Representation across demographics and contexts

> Fairness in datasets requires representation across demographics and contexts. Models trained only on well-lit indoor photos may fail in dark outdoor settings.
---

## Practical Lab Preview
Fine-tune ResNet/ViT for small image classification

> The practical lab involves fine-tuning ResNet or ViT for image classification on a small dataset, comparing approaches, and analyzing errors to understand limitations.
---

## Error Analysis
Misclassified examples  
Augment/collect more data

> Error analysis reveals patterns in mistakes - maybe your model struggles with images taken at night or from certain angles. These insights guide data collection and model improvements.
---

## Data Hygiene
Duplicates/leakage between splits  
Label noise

> Data hygiene catches duplicates between splits (test images that appear in training), leakage, and label noise that confuse the model.
---

## Reflection Prompt
When is ViT preferable to ResNet for your task and why?

> Reflect on when ViT is preferable to ResNet. ViT excels with large datasets and benefits from pretraining, while ResNet works better with limited data and offers stronger inductive biases.
---

## Class Imbalance Strategies
Weighted loss, focal loss, oversampling/undersampling

> Class imbalance strategies include weighted loss, focal loss (emphasizing hard examples), and sampling techniques. Otherwise rare classes get ignored.
---

## Labeling and Quality Control
Clear guidelines  
Inter-annotator agreement checks

> Labeling and quality control require clear guidelines and checking inter-annotator agreement. If humans disagree on labels, models can't learn consistent patterns.
---

## Data Versioning
Track dataset changes  
Ensure experiment reproducibility

> Data versioning tracks dataset changes ensuring reproducible experiments. When you report '92% accuracy', that should be reproducible with the same data version.
---

## Quantization
INT8/PTQ/QAT for faster, smaller inference

> Quantization reduces model size and speeds inference by using 8-bit integers instead of 32-bit floats. Post-training quantization is easy while quantization-aware training achieves better accuracy.
---

## Edge Deployment
Optimize for mobile/embedded  
Memory and power limits

> Edge deployment optimizes models for mobile and embedded devices with limited memory and processing power. Efficient architectures and quantization enable on-device vision.
---

## Grad-CAM Pitfalls
Heatmaps can be misleading  
Use multiple methods

> Grad-CAM pitfalls include heatmaps that are misleading or highlight spurious correlations. Use multiple explanation methods and verify with domain knowledge.
---

## Mixed Precision Caveats
Loss scaling  
Check numerical stability

> Mixed precision caveats include potential numerical instability and need for loss scaling. Monitor for NaN values and adjust scaling factors if needed.
---

## Experiment Tracking
Log metrics, params, artifacts (e.g., MLflow)

> Experiment tracking with tools like MLflow logs metrics, hyperparameters, and artifacts. Systematic tracking is essential for reproducible research and comparing approaches.
---

## Reading List
He et al. (ResNet)  
Dosovitskiy et al. (ViT)

---

## Assignment Brief
Fine-tune a pretrained model  
Report ablations and errors

