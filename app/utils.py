from datetime import datetime

from agent import summarize_jira_issue
from apscheduler.schedulers.background import BackgroundScheduler
from tools import fetch_jira_issues, notify_slack


def daily_triage_job() -> None:
    """Job to run daily to triage Jira issues."""
    print(f"Running daily triage at {datetime.now()}")
    try:
        issues = fetch_jira_issues()
        for issue in issues:
            summary = summarize_jira_issue(issue["description"], issue["id"])
            notify_slack(
                f"✅ *{summary['ticket_id']}* summarized\n\n*Summary:* {summary['summary']}\n*Severity:* {summary['severity']}\n*Component:* {summary['component']}\n*Assignee:* {summary['assignee']}"
            )
    except Exception as e:
        print(f"Error during triage job: {e}")


def start_scheduler() -> BackgroundScheduler:
    """Start the background scheduler for daily triage."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_triage_job, "cron", hour=9, minute=0)  # 9:00 AM daily
    scheduler.start()
    return scheduler
