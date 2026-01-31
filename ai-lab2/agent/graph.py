from langgraph.graph import StateGraph, START, END
from agent.state import AgentState
from agent.nodes import classify_problem, generate_help

def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("classify", classify_problem)
    graph.add_node("help", generate_help)

    graph.add_edge(START, "classify")
    graph.add_edge("classify", "help")
    graph.add_edge("help", END)

    return graph.compile()
