from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
import uvicorn

# Import utilities
from utils.extractors import extract_text
from utils.summarizer import summarize_resume, llm
from utils.qa_generator import generate_qa
from utils.resume_rater import rate_resume
from utils.vector_store import create_vector_store, query_vector_store

load_dotenv()

app = FastAPI()


# ----------------------------------------
# Upload Resume → Extract Text
# ----------------------------------------
@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    text = await extract_text(file)
    return {"text": text}


# ----------------------------------------
# Summarize Resume
# ----------------------------------------
@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    text = await extract_text(file)
    summary = summarize_resume(text)
    return {"summary": summary}


# ----------------------------------------
# Generate Interview Q/A
# ----------------------------------------
@app.post("/qa")
async def qa(file: UploadFile = File(...)):
    text = await extract_text(file)
    qa_data = generate_qa(text)
    return {"qa": qa_data}


# ----------------------------------------
# Resume Rating
# ----------------------------------------
@app.post("/rate")
async def rate(role: str, file: UploadFile = File(...)):
    text = await extract_text(file)
    rating = rate_resume(text, role)
    return {"rating": rating}


# ----------------------------------------
# Chat with Resume (Vector DB)
# ----------------------------------------
@app.post("/chat")
async def chat_resume(file: UploadFile = File(...), question: str = ""):
    # Extract text from uploaded file
    text = await extract_text(file)

    # Create vector DB from extracted resume text
    store = create_vector_store(text)

    # Retrieve relevant chunks
    context = query_vector_store(store, question)

    # Final prompt
    prompt = f"""
    You are an expert HR assistant.
    The user asked: {question}

    Here is relevant resume content:
    {context}

    Answer strictly using resume information. If data is missing, say "Not available in resume".
    """

    response = llm.invoke(prompt)
    return {"answer": response.content}


# ----------------------------------------
# FastAPI Server
# ----------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
