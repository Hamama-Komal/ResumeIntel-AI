from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini")

def rate_resume(text, role):
    prompt = f"""
    Evaluate this resume for the role: {role}.

    Provide:
    1. Score out of 100
    2. Strengths
    3. Weaknesses
    4. Missing keywords
    5. Final improvements

    Resume:
    {text}
    """
    return llm.invoke(prompt).content
