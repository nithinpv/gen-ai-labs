from agent.state import AgentState
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), 
               model="llama-3.3-70b-versatile", 
               temperature=0)

def get_help(state: AgentState):

    system = SystemMessage(content="You are ChatMIT, a helpful AI for students. Give practical, kind, actionable advice. Keep responses concise and reference prior context when helpful.")
    messages = [system]

    history = state.get("history", []) if isinstance(state, dict) else []
    for turn in history:
        user_msg = turn.get("user", "")
        ai_msg = turn.get("assistant", "")
        if user_msg:
            messages.append(HumanMessage(content=user_msg))
        if ai_msg:
            messages.append(AIMessage(content=ai_msg))

    messages.append(HumanMessage(content=state.get("question", "")))
   
    ai_msg = llm.invoke(messages)
    return {"response": ai_msg.content}
