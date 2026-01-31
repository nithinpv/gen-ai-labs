from agent.state import AgentState
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), 
               model="llama-3.3-70b-versatile", 
               temperature=0)

def classify_problem(state: AgentState):
    prompt = f"""
    Classify the following student question into one category:
    - education
    - mental_health
    - financial
    - general

    Question: {state['user_input']}
    """
    category = llm.invoke(prompt).content.strip().lower()
    return {"category": category}

def generate_help(state: AgentState):
    prompt = f"""
    You are a helpful AI for students.

    Category: {state['category']}
    Question: {state['user_input']}

    Give practical, kind, and actionable advice.
    """
    response = llm.invoke(prompt).content
    return {"response": response}
