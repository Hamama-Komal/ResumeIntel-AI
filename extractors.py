import pdfplumber
import docx

from dotenv import load_dotenv
load_dotenv()

from fastapi import UploadFile

async def extract_text(file: UploadFile):
    ext = file.filename.split(".")[-1].lower()

    if ext == "pdf":
        return extract_pdf(await file.read())
    elif ext == "docx":
        return extract_docx(await file.read())
    else:
        return "Unsupported file format."

def extract_pdf(binary):
    import io
    buffer = io.BytesIO(binary)
    with pdfplumber.open(buffer) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)

def extract_docx(binary):
    import io
    buffer = io.BytesIO(binary)
    document = docx.Document(buffer)
    return "\n".join(p.text for p in document.paragraphs)
