# 🛠️ Customer Support Ticket System (CSTS)

The **Customer Support Ticket System (CSTS)** is an advanced, automated customer support solution designed to streamline ticket management. Built with **LangGraph**, **LangChain**, and **FAISS**, this system classifies support tickets, retrieves relevant contextual knowledge, drafts professional responses, conducts quality reviews, and escalates unresolved cases with minimal human intervention. It leverages the **LLaMA3-8B** model via **Groq** for high-quality natural language processing and **SentenceTransformers** for efficient embedding generation.

A demo video is available at:  
**https://drive.google.com/file/d/1pttzWw4gBj0WLTqhZSPphDH3STTimvqa/view?usp=sharing**

## 🧭 Overview

The CSTS follows a structured multi-step workflow:
1. **Input**: Accepts a support ticket with `subject` and `description`.
2. **Classify**: Categorizes tickets into **Billing**, **Technical**, **Security**, or **General**.
3. **Retrieve**: Uses FAISS to fetch relevant context from a local knowledge base.
4. **Draft**: Generates a professional response using the LLM.
5. **Review**: Evaluates the response for clarity, professionalism, and relevance.
6. **Retry or Escalate**: Retries up to 2 times or escalates to a CSV log for human review.

## ⚙️ Tech Stack
- **LangGraph** – Stateful workflow orchestration
- **LangChain** – LLM interfaces and tools
- **FAISS** – Fast similarity-based context retrieval
- **SentenceTransformers** – Embeddings (via `all-MiniLM-L6-v2`)
- **Groq** – High-speed inference with LLaMA3-8B
- **Python 3.10+**

## 🚀 Setup Instructions

Follow these sequential steps to set up and run the CSTS:

### 1. Clone the Repository
```bash
git clone https://github.com/Talha-2/Support-Ticket-Resolution-Agent-with-Multi-Step-Review-Loop-AGENTIC-AI.git
```

### 2. Install `uv` Package Manager
Use `pip` to install the `uv` package manager, a fast alternative for managing Python dependencies:
```bash
pip install uv
uv init
```

### 3. Create a Virtual Environment
Create a virtual environment using `uv` to isolate project dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 4. Install Dependencies
Install all required dependencies listed in `requirements.txt` within the virtual environment:
```bash
uv add -r requirements.txt
```

### 5. Set Up Environment Variables
Create a `.env` file in the root directory and add your Groq and Langsmith API key:
```
GROQ_API_KEY=your_groq_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
```

### 6. Run the Main File
Execute the main script to start the system:
```bash
python -m src.main
```

### 7. Set Up LangGraph CLI (Optional)
To run the agent using the LangGraph CLI, follow these additional steps:

https://github.com/user-attachments/assets/b3bd56d1-4140-46e6-8b72-9ee5bba02160

#### a. Configure Local Server
Refer to the LangGraph local server setup guide:  
**https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/**  
Follow the instructions to set up the local server environment.

#### b. Start the LangGraph Development Server
Launch the server using the LangGraph CLI:
```bash
langgraph dev
```

#### c. Invoke the Agent
Provide a JSON input to invoke the agent. Example input:
```json



{
  "subject": "Refund not received",
  "description": "I canceled my subscription last week but haven’t received a refund yet."
}
```
Send this JSON input via the LangGraph CLI interface to process the ticket.

## 🧪 Testing the Agent

### Sample Test Cases
| Category  | Sample Ticket                       |
|-----------|-------------------------------------|
| Billing   | Why was I charged twice this month? |
| Technical | The app crashes on startup.         |
| Security  | I think my account was hacked.      |
| General   | How do I update my profile?         |

### Check Escalations
If a response fails after 2 retries, it is logged in `escalation_log.csv` with details including:
- Subject
- Description
- Category
- Draft
- Feedback

## 🧠 Design & Architecture
- **LangGraph**: Manages stateful workflows with retry and escalation support.
- **FAISS**: Enables fast local similarity search for context retrieval.
- **SentenceTransformers**: Utilizes `all-MiniLM-L6-v2` for lightweight embeddings.
- **LLaMA3-8B via Groq**: Delivers high-quality NLP with fast inference.
- **TypedDict**: Ensures structured state management.
- **Retry & Escalate**: Implements a 2-retry limit with escalation to `escalation_log.csv`.

## 📦 Dependencies
```
langchain
langchain_community
langchain_groq
faiss-cpu
python-dotenv
ipykernel
sentence_transformers
langgraph-cli
langgraph-cli[inmem]
langchain-huggingface
langgraph
```

## 📈 Potential Improvements
- Update embedding backend to `langchain-huggingface`.
- Integrate a live knowledge base with a DB/API.
- Enhance review with tone, accuracy, and length checks.
- Add timestamps and metadata to logging.
- Scale with Pinecone instead of FAISS.
- Develop a REST API or web frontend.
- Implement unit/integration testing.

## 📂 Project Structure
```
📁 ZIKRA_INFO_TECH
├── src
│   ├── core
│       ├── llm.py
│       ├── prompts.py
│       ├── vector_store.py
│   ├── StateGraph
│       ├── nodes_def.py
│       ├── nodes.py
│       └── retry.py
│       └── ticket_state.py
|   ├── tests
│       ├── test_classify.py
|   ├── init.py
│   ├── CSTS.ipynb
│   ├── main.py
├── .env
├── Assessment Task 
├── escalation_log.csv
├── flow_chart.png
├── langgraph.json
├── README.md
├── requirements.txt
```

