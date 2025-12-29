# Lecture 3
# Working with Text

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Text Matters

Text dominates modern data  
Organizations record decisions in language  
Applied AI must handle text

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Where Text Appears

Emails store communication  
Documents store policy  
Logs store events  
Reviews store opinion

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Text Drives Decisions

Managers read reports  
Customers write feedback  
Agents write notes  
Language guides action

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Text Feels Hard

Language lacks fixed structure  
Meaning shifts by context  
Ambiguity appears everywhere

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Models Help With Text

Scale overwhelms human reading  
Patterns repeat across documents  
Models summarize and classify

![](images/john_adams_correspondence_animation.gif)

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Text Versus Numbers

Numbers arrive cleanly structured  
Text arrives raw and messy  
Transformation enables learning

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Human Language Is Noisy

Spelling varies  
Grammar varies  
Tone varies

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Meaning Depends on Context

Words change meaning by use  
Audience shapes intent  
Time shapes interpretation

![](images/french_revolution1.png)

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Example of Context Shift

Cold describes temperature  
Cold describes illness  
Models must infer use

![](images/french-revolution-docs.png)

> Real-world examples help illustrate how these concepts apply in practice. Pay attention to both successes and failures - both teach valuable lessons about what works and what doesn't.
---

## AI Transforms Context

Same source, different interpretations  
Models reshape meaning  
Context defines output

![](images/french-revolution-fish.png)

> Real-world examples help illustrate how these concepts apply in practice. Pay attention to both successes and failures - both teach valuable lessons about what works and what doesn't.
---

## Why Rules Fail for Text

Rules explode in number  
Edge cases dominate  
Maintenance becomes impossible

![](images/Google Ngram trends from 1800 to 2019.gif)

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Learning From Examples

Models infer patterns from usage  
Examples encode meaning  
Scale replaces hand written logic

> Real-world examples help illustrate how these concepts apply in practice. Pay attention to both successes and failures - both teach valuable lessons about what works and what doesn't.
---

## Applied Text Tasks

Classification assigns labels  
Sentiment estimates tone  
Extraction pulls entities  
Search ranks relevance

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Text in Business

Support tickets require routing  
Reviews require summarization  
Contracts require review

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Text in Government

Public comments require analysis  
Documents require classification  
Requests require triage

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Text in Healthcare

Clinical notes store context  
Summaries support care  
Errors carry risk

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Cost of Text Errors

Misclassification misroutes work  
Misinterpretation misleads decisions  
Bias harms groups

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Applied NLP Focuses on Simplicity

Simple models explain behavior  
Simple pipelines scale well  
Interpretability builds trust

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## What We Will Do With Text

Convert text to features  
Train simple models  
Interpret outputs carefully

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## What We Will Not Do

Train language models from scratch  
Optimize massive architectures  
Treat text as magic

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Responsible Text Use

Language encodes bias  
Models amplify patterns  
Care remains essential

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Applied Lesson

Text carries meaning  
Meaning requires care  
Models support judgment

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Transition to Text as Data

Text must become numeric  
Transformation enables learning  
Next we examine text preprocessing

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Text as Data

Models require numbers  
Text arrives as symbols  
Transformation bridges the gap

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Raw Text Is Not Ready

Text contains punctuation  
Capitalization varies  
Spacing carries noise

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## The Goal of Preprocessing

Reduce noise  
Preserve meaning  
Enable learning

> ROC curves and AUC summarize classifier performance across all possible thresholds. AUC represents the probability that your model ranks a random positive example higher than a random negative example.
---

## Tokenization

Tokenization splits text into units  
Units may be words or symbols  
Choice affects results

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Word Tokenization

Text splits on spaces  
Punctuation separates tokens  
Simple rules work surprisingly well

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Character Tokenization

Characters become units  
Vocabulary shrinks  
Sequences grow longer

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Tradeoffs in Token Choice

Words capture meaning  
Characters capture structure  
Context determines choice

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Normalization

Normalization standardizes text  
Consistency improves learning  
Variation hides signal

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Lowercasing

Capitalization rarely changes meaning  
Lowercasing reduces vocabulary size  
Exceptions exist for acronyms

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Removing Punctuation

Punctuation adds noise  
Removal simplifies text  
Some meaning may disappear

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Stop Words

Stop words appear often  
They add little meaning  
Removal reduces noise

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## When Stop Words Matter

Negation changes meaning  
Function words shape tone  
Blind removal causes error

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Stemming

Stemming trims word endings  
Words collapse to roots  
Meaning approximates intent

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Lemmatization

Lemmatization uses vocabulary rules  
Words map to base forms  
Results improve clarity

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Stemming Versus Lemmatization

Stemming runs fast  
Lemmatization runs slower  
Accuracy trades with speed

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Vocabulary Size

Unique tokens form vocabulary  
Large vocabularies increase sparsity  
Control improves stability

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Rare Words

Rare words add noise  
Removal simplifies models  
Thresholds guide filtering

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Frequency Thresholds

Very common words add little signal  
Very rare words add noise  
Middle frequencies matter most

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Text Length Variation

Documents vary in length  
Length influences models  
Normalization addresses imbalance

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Representing Documents

Documents become vectors  
Vectors enable math  
Structure drives learning

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Order and Meaning

Some models ignore order  
Others preserve sequence  
Tradeoffs appear

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Preprocessing and Bias

Cleaning removes dialect signals  
Standardization erases identity  
Awareness matters

> ROC curves and AUC summarize classifier performance across all possible thresholds. AUC represents the probability that your model ranks a random positive example higher than a random negative example.
---

## Practical Considerations

Preprocessing choices affect outcomes  
Defaults may mislead  
Inspection prevents mistakes

> This hands-on exercise gives you practical experience with the concepts we've discussed. Working through examples yourself builds intuition that lectures alone can't provide.
---

## Applied Lesson

Text becomes data through choice  
Choices encode assumptions  
Reflection improves results

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Transition to Vectorization

Tokens alone do not suffice  
Models require numeric vectors  
Next we examine vectorization methods

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Vectorization Methods

Models operate on numbers  
Vectorization converts text into numeric form  
Representation shapes learning

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## From Tokens to Vectors

Tokens identify units  
Vectors encode documents  
Encoding enables computation

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Bag of Words Intuition

Documents become word counts  
Order disappears  
Presence and frequency remain

> Bag-of-words represents text as word counts, ignoring grammar and word order. Despite its simplicity, BoW remains a strong baseline for many text classification tasks.
---

## How Bag of Words Works

Each word becomes a column  
Each document becomes a row  
Counts fill the table

> Bag-of-words represents text as word counts, ignoring grammar and word order. Despite its simplicity, BoW remains a strong baseline for many text classification tasks.
---

## Example Bag of Words

Document one contains words  
Counts reflect frequency  
Zeros dominate the matrix

> Bag-of-words represents text as word counts, ignoring grammar and word order. Despite its simplicity, BoW remains a strong baseline for many text classification tasks.
---

## Sparsity Appears Quickly

Most words appear rarely  
Most matrix entries equal zero  
Sparsity affects performance

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Bag of Words Still Works

Many tasks rely on frequency  
Order often adds little value  
Simplicity supports interpretation

> Bag-of-words represents text as word counts, ignoring grammar and word order. Despite its simplicity, BoW remains a strong baseline for many text classification tasks.
---

## Limits of Bag of Words

Word order disappears  
Synonyms remain separate  
Context gets lost

> Bag-of-words represents text as word counts, ignoring grammar and word order. Despite its simplicity, BoW remains a strong baseline for many text classification tasks.
---

## Term Frequency

Term frequency counts appearances  
Frequent words gain weight  
Long documents dominate counts

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Normalizing Term Frequency

Divide by document length  
Balance short and long texts  
Comparability improves

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Inverse Document Frequency

Common words add little information  
Rare words add more signal  
IDF downweights common terms

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## TF IDF Intuition

Important words appear often in a document  
They appear rarely across documents  
TF IDF captures both

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## TF IDF in Practice

Counts scale by rarity  
Vectors remain sparse  
Interpretation remains possible

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Comparing TF IDF and Counts

Counts favor repetition  
TF IDF favors specificity  
Task determines choice

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## N Grams

Single words miss phrases  
N grams capture sequences  
Context increases

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Bigrams and Trigrams

Bigrams capture short phrases  
Trigrams capture longer patterns  
Vocabulary grows rapidly

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Tradeoffs With N Grams

Signal increases  
Dimensionality explodes  
Overfitting risk rises

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Dimensionality Matters

Large feature spaces slow learning  
Noise overwhelms signal  
Regularization helps

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Feature Selection for Text

Remove rare terms  
Limit vocabulary size  
Improve stability

> Feature engineering - creating informative input variables - often matters more than algorithm choice. Good features that capture relevant patterns can make even simple models perform well.
---

## Interpreting Text Features

Weights reveal influence  
Positive and negative terms matter  
Inspection builds trust

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Text Vectors and Linear Models

Linear models handle sparsity well  
Training remains efficient  
Interpretability stays strong

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## When Vectorization Fails

Sarcasm fools frequency  
Context flips meaning  
Human review remains necessary

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Vectorization and Bias

Language encodes identity  
Vectors encode language  
Bias transfers quietly

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Applied Lesson

Representation defines what models learn  
Simple methods remain powerful  
Interpretation protects against misuse

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Transition to Sentiment

Vectors enable learning  
Learning enables inference  
Next we apply vectors to sentiment

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Sentiment Analysis

Sentiment analysis estimates tone  
Tone reflects attitude or emotion  
Many decisions depend on it

> Sentiment analysis classifies text by opinion or emotion. Applications range from analyzing customer reviews to monitoring social media sentiment about brands or public figures.
---

## What Sentiment Measures

Positive language  
Negative language  
Neutral language

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Common Sentiment Questions

Is feedback favorable  
Is a review critical  
Is communication escalating

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Sentiment Matters

Organizations monitor reputation  
Teams track customer experience  
Early signals prevent damage

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Sentiment as a Classification Task

Inputs consist of text  
Outputs represent sentiment labels  
Models infer tone from language

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Binary Sentiment

Positive versus negative  
Simple framing  
Useful for many tasks

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Multiclass Sentiment

Positive neutral and negative  
Greater nuance  
Harder classification

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Lexicon Based Sentiment

Word lists assign polarity  
Scores aggregate across text  
Rules remain transparent

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## How Lexicons Work

Each word carries a score  
Scores sum across documents  
Thresholds define labels

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Benefits of Lexicon Methods

No training data required  
Fast execution  
Easy interpretation

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Limits of Lexicon Methods

Sarcasm fools scoring  
Context changes meaning  
Domain language breaks rules

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Machine Learning Based Sentiment

Models learn from labeled examples  
Vectors encode text  
Patterns drive prediction

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Training a Sentiment Model

Prepare labeled text  
Vectorize documents  
Fit a classifier

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Comparing Lexicon and ML Methods

Lexicons offer transparency  
ML adapts to domain language  
Choice depends on context

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Domain Specific Sentiment

Words shift meaning by domain  
Risk means danger or opportunity  
Models require adaptation

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Evaluating Sentiment Models

Accuracy alone misleads  
Class balance matters  
Confusion matrices reveal bias

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Error Analysis

Inspect misclassified examples  
Identify systematic errors  
Adjust preprocessing or labels

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Sentiment and Bias

Language reflects culture  
Models reflect training data  
Unequal errors appear

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Ethical Use of Sentiment

Avoid surveillance misuse  
Respect consent  
Limit automated judgment

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Practical Applications

Review monitoring  
Support ticket triage  
Survey analysis

> This hands-on exercise gives you practical experience with the concepts we've discussed. Working through examples yourself builds intuition that lectures alone can't provide.
---

## When Sentiment Fails

Mixed emotions appear  
Irony appears  
Models oversimplify

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Human Review Still Matters

Sentiment supports judgment  
It does not replace it  
Context completes interpretation

> This summary reinforces the key concepts from this section. Reviewing main ideas helps consolidate learning and identify areas that need further study.
---

## Applied Lesson

Sentiment appears simple  
Reality remains complex  
Care improves outcomes

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Transition to Pretrained Models

Training requires data  
Pretrained models reduce effort  
Next we examine modern NLP tools

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Pretrained NLP Models

Pretrained models learn from massive text corpora  
They capture language patterns broadly  
They reduce training effort

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Why Pretraining Works

Language repeats structure  
Large datasets reveal patterns  
Transfer enables reuse

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## What Pretrained Models Provide

Embeddings encode meaning  
Classifiers generalize across domains  
APIs expose capability

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Embeddings Intuition

Words map to vectors  
Similar meaning implies proximity  
Geometry captures semantics

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Sentence and Document Embeddings

Sentences aggregate word meaning  
Documents aggregate sentence meaning  
Similarity enables search and clustering

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Common Pretrained Tasks

Text classification  
Named entity recognition  
Summarization  
Question answering

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Using Pretrained Models via APIs

Send text to a service  
Receive predictions or embeddings  
Integrate results into applications

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Benefits of API Based NLP

No model training  
Rapid experimentation  
Scales on demand

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Tradeoffs of API Use

Less control over internals  
Ongoing usage cost  
Data governance concerns

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Latency Considerations

Network calls add delay  
Batching reduces overhead  
UX depends on response time

> Latency (response time) and throughput (volume handled) represent key performance tradeoffs. Batching improves throughput while individual requests optimize latency - choose based on your use case.
---

## Privacy and Data Handling

Text may contain sensitive data  
Transmission carries risk  
Policies must guide use

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Fine Tuning Versus Prompting

Fine tuning adapts models with data  
Prompting adapts behavior with instructions  
Choice depends on needs

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## When Simple Models Suffice

Small datasets exist  
Interpretation matters  
Latency must remain low

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## When Pretrained Models Shine

Language complexity rises  
Coverage matters  
Development time shrinks

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Evaluating Pretrained Outputs

Benchmarks do not match context  
Local evaluation remains necessary  
Human review adds safety

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Bias in Pretrained Models

Training data reflects society  
Bias persists  
Monitoring remains required

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Responsible Integration

Limit automated decisions  
Log and audit use  
Explain limitations

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Practical Workflow

Start with simple baselines  
Test pretrained alternatives  
Choose by evidence

> This hands-on exercise gives you practical experience with the concepts we've discussed. Working through examples yourself builds intuition that lectures alone can't provide.
---

## Applied Lesson

Pretrained models accelerate work  
Judgment remains essential  
Integration defines success

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Transition to Wrap

We have turned language into data  
We have applied models to text  
Now we summarize and close

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Demo, Integration, and Wrap

Text models matter when they run  
We connect concepts to practice  
Integration reveals limitations

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Demo Goal

Take raw text  
Transform it into features  
Produce a usable prediction

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Demo Dataset

Short text documents  
Clear labels  
Known limitations

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Preprocessing in Practice

Lowercase text  
Tokenize words  
Remove noise carefully

> ROC curves and AUC summarize classifier performance across all possible thresholds. AUC represents the probability that your model ranks a random positive example higher than a random negative example.
---

## Vectorization Choice

Start with TF IDF  
Limit vocabulary size  
Inspect feature space

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Model Selection

Choose a simple classifier  
Avoid unnecessary complexity  
Favor interpretability

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Training the Model

Fit on training data  
Observe convergence  
Watch for warnings

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Generating Predictions

Apply model to test data  
Capture probabilities  
Avoid hard labels too early

> Named Entity Recognition identifies and classifies mentions of people, organizations, locations, and other entities in text. This structured information extraction enables downstream applications like knowledge graphs.
---

## Evaluating Performance

Inspect confusion matrix  
Review misclassified examples  
Identify systematic patterns

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Error Analysis Matters

Errors reveal data issues  
Errors reveal label ambiguity  
Errors guide improvement

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Iteration Strategy

Adjust preprocessing  
Revisit labels  
Reevaluate consistently

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## When Pretrained Models Help

Compare results qualitatively  
Note speed differences  
Assess interpretability tradeoffs

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Integration Into Applications

Predictions require context  
Users need explanation  
UI shapes trust

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Common Text Modeling Mistakes

Overcleaning language  
Ignoring negation  
Trusting scores blindly

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Ethics Revisited

Language reflects identity  
Automation risks misinterpretation  
Human oversight remains necessary

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Lecture 3 Summary

Text dominates real data  
Preprocessing shapes meaning  
Simple models remain powerful

> This summary reinforces the key concepts from this section. Reviewing main ideas helps consolidate learning and identify areas that need further study.
---

## Skills You Now Have

Convert text to data  
Train interpretable models  
Evaluate responsibly

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## Looking Ahead

Next we work with images  
Vision introduces new structure  
Different risks emerge

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.
---

## End of Lecture 3

Pause  
Reflect  
Prepare for vision

> This slide covers an important concept in applied AI. Understanding this material will help you evaluate opportunities and challenges when considering AI applications in your field.