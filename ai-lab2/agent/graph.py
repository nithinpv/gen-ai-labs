from langgraph.graph import StateGraph, START, END
from agent.state import AgentState
from agent.nodes import get_help

def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("help", get_help)
    
    graph.add_edge(START, "help")
    graph.add_edge("help", END)

    return graph.compile()
