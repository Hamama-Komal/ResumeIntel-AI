from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini")

def summarize_resume(text):
    prompt = PromptTemplate(
        input_variables=["resume"],
        template="""
        Summarize this resume in 10 bullet points:

        {resume}
        """
    )
    return llm.invoke(prompt.format(resume=text)).content
