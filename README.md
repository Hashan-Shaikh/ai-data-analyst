🧠 AI Data Analyst — Natural Language to SQL with LangChain + Groq
This project is an AI-powered data analyst built using FastAPI, LangChain, and Groq’s LLMs. It allows users to ask natural language questions about their database, and intelligently transforms those questions into SQL queries — returning meaningful responses straight from a PostgreSQL database.

🔍 What It Does
Accepts raw natural language queries (e.g., "What are the top 5 most active users?")

Uses LangChain AI Agents to:

Understand the intent

Generate accurate SQL using Groq’s LLM (like LLaMA3)

Execute queries securely against a PostgreSQL database

Returns a clean, AI-generated response to the user

🛠️ Tech Stack
FastAPI — API framework for exposing the AI interface

PostgreSQL — Relational DB storing structured data

LangChain — For building and managing AI agents

Groq + LLaMA3 — High-performance LLM for generating SQL

SQLAlchemy — ORM and DB engine

Docker — Containerized PostgreSQL

dotenv — Manages environment variables

✨ Use Case
Great for dashboards, analytics apps, internal tools — anywhere users need to ask questions about data without writing SQL.

