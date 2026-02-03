from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), 
               model="llama-3.3-70b-versatile", 
               temperature=0.2)

def get_help(user_input: str) -> str:

    prompt = f"""
    You are a helpful AI for students. You provide advice on study techniques, time management, and learning resources.
    If the question is outside these topics, respond with a very short answer that you can only assist with study-related queries.
    
    A student asks:
    "{user_input}"

    Give kind, practical, and actionable advice.
    """

    response = llm.invoke(prompt)
    return response.content
