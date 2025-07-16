

---

# 🛠️Customer Support Ticket System (STS)

The **Customer Support Ticket System (CSTS)** is an automated customer support solution built using **LangGraph**, **LangChain**, and **FAISS**. It classifies support tickets, retrieves contextual knowledge, drafts professional responses, performs quality reviews, and escalates unresolved cases — all with minimal human intervention.

Powered by the **LLaMA3-8B** model via **Groq** and **SentenceTransformers** for embedding generation.

---
### Demo Video Drive Link :
**https://drive.google.com/file/d/1xnnTyuUsIyb9Lj2RPe0dOlkYBsWNsNJo/view?usp=sharing**
## 🧭 Overview

The CSTS processes tickets via a multi-step workflow:

1. **Input**: Accepts a support ticket with `subject` and `description`.
2. **Classify**: Categorizes ticket as **Billing**, **Technical**, **Security**, or **General**.
3. **Retrieve**: Uses FAISS to fetch relevant context from a local knowledge base.
4. **Draft**: Generates a professional response using the LLM.
5. **Review**: Evaluates response clarity, professionalism, and relevance.
6. **Retry or Escalate**: Retries up to 2 times or escalates to CSV for human review.

---

## ⚙️ Tech Stack

* **LangGraph** – Stateful workflow orchestration
* **LangChain** – LLM interfaces and tools
* **FAISS** – Fast similarity-based context retrieval
* **SentenceTransformers** – Embeddings (via `all-MiniLM-L6-v2`)
* **Groq** – High-speed inference with LLaMA3-8B
* **Python 3.10+**

---

## 🚀 Setup Instructions

### ✅ Prerequisites

* Python 3.10+
* [`uv`](https://github.com/astral-sh/uv) (fast Python package manager)
* Groq API Key

---

### 1. Install `uv`

```bash
pip install uv
```

---

### 2. Create Virtual Environment

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
  uv pip install 
  langgraph 
  langchain 
  langchain-community 
  langchain-groq 
  sentence-transformers 
  faiss-cpu 
  python-dotenv 
  jupyter 
  ipython
```

Optional (for faster HuggingFace downloads):

```bash
uv pip install hf_xet
```

---

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual key.

---

### 5. Run Jupyter Notebook

```bash
uv run jupyter notebook
```

Open `STS.ipynb` and run all cells.

---

## ▶️ Running the Agent

### ✅ In Jupyter Notebook

Example:

```python
test_ticket = {
    "subject": "Refund not received",
    "description": "I canceled my subscription last week but haven’t received a refund yet."
}
result = run_agent(test_ticket)
```

The notebook will print the state at each node and display the final response.

---

### ✅ In Python Script

Create a `sts.py` file and include your logic.

Run:

```bash
uv run python sts.py
```

Ensure `.env` is present in the same directory.

---

## 🧪 Testing the Agent

### 🔁 Modify Ticket

```python
test_ticket = {
    "subject": "Login error",
    "description": "I keep getting an Error 403 when trying to log in."
}
result = run_agent(test_ticket)
```

---

### 📄 Check Escalations

If a response fails after 2 retries, it's logged in `escalation_log.csv` with:

* Subject
* Description
* Category
* Draft
* Feedback

---

### ✅ Sample Test Cases

| Category  | Sample Ticket                       |
| --------- | ----------------------------------- |
| Billing   | Why was I charged twice this month? |
| Technical | The app crashes on startup.         |
| Security  | I think my account was hacked.      |
| General   | How do I update my profile?         |

---

## 🧠 Design & Architecture

### 1. **LangGraph** for Workflow

* **Why**: Explicit state management with retry/escalation support.
* **Alt**: LangChain `AgentExecutor`.

### 2. **FAISS** for Context Retrieval

* **Why**: Fast local similarity search.
* **Alt**: Pinecone or Elasticsearch for scale.

### 3. **SentenceTransformers**

* **Model**: `all-MiniLM-L6-v2`
* **Why**: Lightweight, efficient for short text.
* **Note**: Consider migrating to `langchain-huggingface`.

### 4. **LLaMA3-8B via Groq**

* **Why**: High-quality NLP with fast inference.
* **Alt**: Local HF models (tradeoff: performance vs dependency).

### 5. **TypedDict for State**

* Enforces structure and improves maintainability.

### 6. **Retry & Escalate**

* 2 retry limit for draft review.
* Escalates to `escalation_log.csv`.

### 7. **Mock Knowledge Base**

* Hardcoded for demonstration.
* Future: Use a real DB or API.

### 8. **Structured JSON Output**

* Improves validation and parsing robustness.

### 9. **Error Handling**

* Fallbacks to `"General"` category or escalates on critical failure.

---

## 📦 Dependencies

```
langgraph
langchain
langchain-community
langchain-groq
sentence-transformers
faiss-cpu
python-dotenv
jupyter
ipython
```

---

## 📈 Potential Improvements

* 🔁 **Update Embedding Backend**: Use `langchain-huggingface`
* 🧠 **Live Knowledge Base**: Integrate DB/API for dynamic context
* 🔍 **Advanced Review**: Add tone, accuracy, and length checks
* 🗃️ **Improved Logging**: Add timestamps and metadata
* ☁️ **Scalability**: Swap FAISS for Pinecone
* 🌐 **API/UI**: Build REST API or Web Frontend
* 🧪 **Tests**: Add unit/integration testing framework

---

## 📂 Project Structure 

```
📁 sts-project/
├── .env
├── STS.ipynb
├── sts.py
├── escalation_log.csv
├── requirements.txt
└── README.md
```

---

