# Customer Churn Analysis – Decision-Oriented AI System

An enterprise-style AI system for **customer churn analysis** that accepts natural language queries, detects user intent, conditionally routes logic, analyzes customer and financial data, makes retention decisions, and stores auditable business memory.

This project focuses on **decision-making**, not just prediction.

---

## 📌 Problem Statement

Customer churn is costly for businesses, but traditional churn models only provide predictions.
This system goes a step further by:
- Understanding user intent
- Performing structured analysis
- Making actionable retention decisions
- Persisting decisions for audit and tracking

---

## 🧠 Key Features

- Natural language interface (no SQL exposed to users)
- Intent detection using structured LLM output
- Conditional routing using LangChain `RunnableBranch`
- Parallel analysis using `RunnableParallel`
- Domain-safe SQL tools for enterprise data
- Agent-based decision making for complex churn cases
- Persistent SQLite-based decision memory
- Business-friendly, explainable outputs
- Streamlit-based UI

---

## 🏗️ Architecture

User Query
↓
Intent Detection (analysis / decision / summary)
↓
Conditional Routing
↓
Parallel Analysis (Customer Risk + Financial Exposure)
↓
Decision Agent (Retention Strategy)
↓
SQLite Decision Memory
↓
Final Business Output


---

## 🧩 Tech Stack

- Python
- LangChain
- Streamlit
- SQLite
- GROQ LLM
- Pydantic
- SQL tools

---

## 🚀 How to Run Locally

### 1️⃣ Create virtual environment
```bash
python -m venv .venv

2️⃣ Activate environment
.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file:

GROQ_API_KEY=your_api_key_here

5️⃣ Run the application
python run.py

🔐 Security & Design Principles

API keys stored using environment variables

SQL logic encapsulated inside tools

No direct database access by LLM

Persistent and auditable decision storage

Clear separation of chains, tools, agents, and memory

🎯 Why This Project Is Industry-Level

Focuses on decision workflows, not demos

Avoids unnecessary agent usage for efficiency

Uses conditional routing for scalability

Maintains audit-ready business memory

Designed to mirror real enterprise AI systems

📄 Use Case

Customer retention strategy

Churn risk assessment

Business decision support systems

Enterprise AI workflow design
