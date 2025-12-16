# Week 6
# AI Agents and Tool Use

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## How models plan, decide, and act

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## The Core Idea

A model predicts text.  
An agent decides what to do next.  
It uses reasoning, planning, and tools to complete tasks

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## What Is an Agent?

An agent is a loop:  
Read the prompt.  
Decide if it needs outside data or action.  
Use a tool or API.  
Return the result and reason about it

> Clear definitions establish shared understanding and prevent talking past each other. Precise terminology is especially important in AI where marketing hype and technical reality often diverge.
---

## The Tools

Agents don't know everything.  
They connect to tools such as:  
Calculators for math.  
Browsers for real-time info.  
Databases or APIs for structured data

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Example

User: "What is the current stock price of Apple?"  
Model: realizes it can't know.  
Agent: calls a financial API.  
Returns: "Apple stock is $181.24."

> Concrete examples illustrate how abstract concepts apply in practice. Studying both successes and failures reveals patterns worth emulating or avoiding.
---

## Planning and Reasoning

Agents break tasks into steps.  
They track what's done and what's next.  
They can call other agents or tools as needed

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Memory and Context

Unlike plain models, agents can store notes between steps.  
This helps them stay consistent in long workflows.  
Still, memory must be designed — it's not automatic

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Chains and Graphs

Earlier systems like LangChain used linear chains.  
Modern systems use graphs — dynamic workflows that adapt as the agent learns what to do next

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Real-World Use

Customer service chatbots.  
Financial report generation.  
IT troubleshooting assistants.  
Data cleaning pipelines

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Limits and Risks

Agents can:  
Loop forever if logic fails.  
Produce nonsense if a tool misfires.  
Leak sensitive data if not sandboxed

> Risk assessment identifies what could go wrong, how likely it is, and how serious the consequences would be. Prioritize mitigations for your highest-impact risks.
---

## The Human Role

Agents don't replace experts.  
They execute decisions within guardrails set by humans.  
Human oversight defines safe and useful autonomy

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.
---

## Summary

Agents extend models with reasoning, planning, and action.  
They connect language to the real world.  
Tools make them capable  
Humans make them responsible

> This slide explores an important concept in applied AI. Understanding this material will help you make better decisions when evaluating opportunities and challenges in your field.