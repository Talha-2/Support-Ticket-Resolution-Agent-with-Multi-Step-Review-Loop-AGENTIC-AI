Support Ticket System (STS)
The Support Ticket System (STS) is an automated customer support ticket processing system built using LangGraph, LangChain, and FAISS. It classifies support tickets, retrieves relevant context from a knowledge base, generates professional responses, reviews them for quality, and escalates unresolved cases for human review. The system leverages the LLaMA3-8B model via Groq for natural language processing and SentenceTransformers for vector-based context retrieval.
Overview
The STS processes customer support tickets through a multi-step workflow:
1.	Input: Accepts a ticket with a subject and description.
2.	Classify: Categorizes the ticket into Billing, Technical, Security, or General using a language model.
3.	Retrieve: Fetches relevant context from a FAISS vector store based on the ticket's category and content.
4.	Draft: Generates a professional response using the ticket and context.
5.	Review: Evaluates the draft for clarity, professionalism, and relevance.
6.	Retry or Escalate: Retries up to two times if the draft fails review, or logs to a CSV for human review.
The system uses LangGraph for stateful workflow orchestration, LangChain for LLM interactions, and FAISS for efficient context retrieval. State persistence is handled via a MemorySaver.
