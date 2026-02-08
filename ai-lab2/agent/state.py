from typing import TypedDict, List, Dict

class AgentState(TypedDict, total=False):
    question: str
    response: str
    history: List[Dict[str, str]]
