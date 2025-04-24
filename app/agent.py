import os

from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
from app.tools import analyze_jira_issue, debug_python_code, inspect_logs

# Define the agent
ai_agent = Agent(
    tools=[analyze_jira_issue, inspect_logs, debug_python_code],
    model="gpt-4",  # or "gpt-3.5-turbo"
)
