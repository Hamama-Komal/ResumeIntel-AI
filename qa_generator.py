from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini")

def generate_qa(text):
    prompt = f"""
    Generate 10 interview questions and answers based on this resume:

    {text}
    """
    return llm.invoke(prompt).content
