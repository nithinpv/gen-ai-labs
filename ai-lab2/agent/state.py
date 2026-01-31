from typing import TypedDict

class AgentState(TypedDict):
    user_input: str
    category: str
    response: str
