import os
from typing import List

import requests
from dotenv import load_dotenv
from pydantic import BaseModel
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# def greet(name: str) -> str:
#     return f"Hello {name}"


# print(greet("Ha"))

load_dotenv()
# JIRA Configuration
JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")
JIRA_AUTH = (os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))

# Slack Configuration
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")

# Initialize Slack client
slack_client = WebClient(token=SLACK_TOKEN)


def fetch_jira_issues() -> list:
    """Fetches issues from Jira project."""
    url = f"https://{JIRA_DOMAIN}/rest/api/3/search"
    params = {
        "jql": f"project={JIRA_PROJECT_KEY} AND created >= -1d",
        "fields": "summary,description,assignee",
    }
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, params=params, auth=JIRA_AUTH)

    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch issues from Jira. Status code: {response.status_code}"
        )

    issues = response.json().get("issues", [])
    return [
        {
            "id": issue["key"],
            "description": issue["fields"].get("description", ""),
            "assignee": issue["fields"]
            .get("assignee", {})
            .get("displayName", "Unassigned"),
        }
        for issue in issues
    ]


def notify_slack(message: str) -> None:
    """Sends a notification to Slack."""
    try:
        slack_client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
    except SlackApiError as e:
        print(f"Error sending to Slack: {e.response['error']}")


def analyze_jira_issue(issue_title: str, issue_description: str) -> str:
    """Analyze a Jira issue and provide a summary with priority suggestion."""
    # You can add logic here or call a model
    return f"Analyzed '{issue_title}' - This issue seems {('critical' if 'crash' in issue_description else 'normal')}."


# Dummy log inspector


def inspect_logs(logs: List[str]) -> str:
    """Inspect logs and find errors or anomalies."""
    errors = [log for log in logs if "ERROR" in log.upper()]
    return f"Found {len(errors)} error(s): {errors}"


# Dummy code debugger


def debug_python_code(code: str) -> str:
    """Analyze a piece of Python code and detect obvious bugs."""
    if "==" in code and "None" in code:
        return "Use `is None` instead of `== None` for checking None in Python."
    return "No obvious bugs found."
