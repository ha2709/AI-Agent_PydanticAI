from pydantic import BaseModel


class JiraSummary(BaseModel):
    ticket_id: str
    summary: str
    severity: str
    component: str
    assignee: str
