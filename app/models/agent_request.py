from pydantic import BaseModel


class AgentRequest(BaseModel):
    query: str  # Free-form query for the agent to handle
