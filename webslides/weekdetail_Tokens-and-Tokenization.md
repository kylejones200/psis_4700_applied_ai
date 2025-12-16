# Week 2
# Tokens and Tokenization

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## How text becomes numbers the model can read

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## The Core Idea

Models don't see words.  
They see tokens — small pieces of text turned into numbers.  
Tokenization is how we bridge language and math

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## What Is a Token

A token is a chunk of text.  
It can be a word, part of a word, or even punctuation.  
Example:  
"cats" → "cat", "s"  
"don't" → "do", "n't"

> Clear definitions establish shared understanding and prevent talking past each other. Precise terminology is especially important in AI where marketing hype and technical reality often diverge.
---

## Why Tokens Exist

Computers need fixed units.  
Words vary  
Tokens don't
Tokens let AI models process any language consistently

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## The Conversion

Text → Token IDs → Numbers.  
Each token maps to a numeric ID from the model's vocabulary.  
These IDs are what the neural network actually reads

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Example: "I love cats."

| Text | Token | ID |  
|------|-------|-----|  
| I | I | 41 |  
| love | love | 518 |  
| cats | cat + s | 873 + 220 |

The sentence becomes a sequence of numbers

> Concrete examples illustrate how abstract concepts apply in practice. Studying both successes and failures reveals patterns worth emulating or avoiding.
---

## Why It Matters

Every model has a limit on how many tokens it can handle.  
That limit defines the context window.  
Longer input → more tokens → higher cost

> Understanding why concepts matter helps you apply them appropriately. This context prevents cargo-cult adoption of practices that don't fit your situation.
---

## Tokenization Styles

Word-based (rare today)  
Subword-based (most common)  
Byte-pair encoding (BPE) — merges frequent patterns like "ing," "tion."  
Character-based — used for languages without spaces

> Tokenization breaks text into pieces that language models process. Understanding tokenization matters because costs, context limits, and performance all depend on token counts rather than intuitive measures like words or characters.
---

## Tokenization Across Languages

English uses spaces.  
Chinese or Japanese do not.  
Tokenizers learn each language's structure.  
The goal is always efficient compression of meaning

> Tokenization breaks text into pieces that language models process. Understanding tokenization matters because costs, context limits, and performance all depend on token counts rather than intuitive measures like words or characters.
---

## The Cost of Tokens

Each API call charges per token.  
Prompt + Response = Total tokens.  
Trimming text saves cost and speed

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Visual Summary

Sentence → tokens → numeric IDs → embeddings.  
Embeddings become the input for model reasoning

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Summary

Tokens are how language becomes math.  
Tokenization defines model cost, speed, and capacity.  
Every AI task begins here

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.