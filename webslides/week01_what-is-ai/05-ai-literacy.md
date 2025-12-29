# AI Literacy for Adult Learners

> This slide explores an important aspect of working with AI systems. Understanding this concept will help you make better decisions when evaluating and deploying AI in your work.
---



Here is a complete 90-minute class outline for adult learners on AI Literacy. It balances high-level math ideas with practical systems and ethical issues

Title  
"Becoming Literate in AI: From Vectors to Values"

Part 1 – Framing AI (10 min)  
Goal: Establish what "AI literacy"means  
Explain that AI is about representing, predicting, and aligning  
Contrast symbolic vs. statistical reasoning  
Show examples learners recognize (ChatGPT, Netflix recommendations, self-driving)

Part 2 – Math Foundations Behind Everyday AI (25 min)  
Vectors and Similarity  
Show text as vectors  
Compute a simple cosine similarity between two short sentences  
Explain intuition: angle = closeness in meaning  
Sketch how vector databases (e.g., FAISS, Chroma) use this to find nearest neighbors fast

Probability and Markov Chains  
Model next-word prediction as a Markov process  
Walk through a two-state chain (Sunny → Rainy)  
Connect to language models predicting next tokens  
Explain transition matrix, stationary distribution, and why memoryless property matters

Matrix Operations in Learning  
Briefly show that multiplying vectors and matrices gives weighted sums  
Tie to how networks learn embeddings

Part 3 – Systems in Practice (25 min)  
Vector Stores and Retrieval-Augmented Generation  
Show pipeline: Document → Chunk → Embedding → Index → Query  
Demonstrate a simple semantic search example  
Explain latency, scaling, and how metadata filtering works

Model Alignment and Reinforcement Learning from Human Feedback (RLHF)  
Describe how models learn preferred answers through reward signals  
Connect to Markov Decision Process structure  
Discuss human feedback loops, reward hacking, and safety guardrails

Edge and Cloud  
Outline where computation happens (on device, in cloud)  
Mention energy, privacy, latency trade-offs

Part 4 – Ethics, Bias, and Societal Impact (15 min)  
Discuss how embeddings can encode bias  
Explain alignment as matching model behavior to human intent  
Introduce transparency (open weights, documentation)  
Prompt reflection: "What values do we want models to learn?”

Part 5 – Hands-On Mini Lab (10 min)  
Use a small web notebook or demo:

Enter two short sentences

Compute cosine similarity

Change words and observe score shift

Show how a retrieval system uses that number to rank results

Part 6 – Wrap-Up and Reflection (5 min)  
Recap three takeaways:  
AI represents information as vectors, predicts with probabilities, and must stay aligned with people  
Assign optional reading: "The Alignment Problem"(Christian) and "Deep Learning Illustrated"(Pearson)  
Invite questions on where learners see AI affecting their own field

Instructor Notes  
Keep tone conversational  
Use board sketches for matrices and vectors  
Avoid long derivations  
Emphasize intuition and application

> AI literacy means understanding what AI can and cannot do, recognizing when AI is being used, and evaluating AI claims critically. This foundational knowledge enables informed participation in discussions about AI deployment.