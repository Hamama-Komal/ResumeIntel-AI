# ⚡ ResumeIntel AI — Advanced AI Resume Analyzer  
A modern AI-powered resume analysis system with executive summaries, ATS scoring, interview Q/A, and a contextual chat assistant using vector search.

Built with **FastAPI**, **Streamlit**, **OpenAI**, **FAISS Vector DB**, and **LangChain**.

---

## 🚀 Features

### 🔹 1. Resume Summary (Executive Summary)
AI extracts key career insights, achievements, skills, and profile details.

### 🔹 2. Interview Q/A Generator
Generates mock interview questions and AI-generated sample answers.

### 🔹 3. ATS Resume Rating
Rates the resume based on a target job role  
(e.g., “Senior Flutter Developer”, “Machine Learning Engineer”).

### 🔹 4. Vector Database + Chat Assistant
Uses FAISS for semantic search.  
Ask questions like:
- “What programming languages does the candidate know?”
- “Does the resume mention React experience?”

### 🔹 5. Premium UI (Streamlit)
Beautiful animated UI with:
- Tabs (acting like a multi-tool dashboard)
- Glassmorphism cards
- Gradient headers
- Smooth animations
- Modern color palette


## 🖼️ Tech Stack

| Component | Technology |
|----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| AI Model | OpenAI GPT |
| Vector DB | FAISS via LangChain |
| Embeddings | OpenAI |
| File Parsing | PyPDF2 / python-docx |
| Styling | Custom HTML + CSS |


## 🔧 Installation

### 1️⃣ Clone Repo

```bash
git clone https://github.com/your-username/resumeintel-ai.git
cd resumeintel-ai
````

### 2️⃣ Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Add API Keys in .env
```
OPENAI_API_KEY=your_openai_key
```

### ▶️ How to Run
👉 Start Backend (FastAPI)
```
uvicorn main:app --reload --port 8000
```

👉 Start Frontend (Streamlit)
```
streamlit run app.py
```

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.
