from app.agent import ai_agent
from app.models.jira_summary import JiraSummary


def summarize_jira_issue(ticket_id: str, description: str) -> JiraSummary:
    """Summarizes a Jira issue using the AI agent."""
    prompt = (
        f"You are a senior engineering lead. Summarize the following Jira issue in three bullet points.\n"
        f"Include: Cause (if mentioned), Impact, and Resolution steps.\n"
        f"Also suggest a component and urgency level.\n\n"
        f"Issue Description:\n{description}"
    )

    response = ai_agent.run(prompt, output_model=JiraSummary)
    response.ticket_id = ticket_id  # Attach the ticket ID to the result
    return response
