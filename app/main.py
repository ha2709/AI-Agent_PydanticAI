from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from app.agent import ai_agent
from app.models.agent_request import AgentRequest
from app.services import summarize_jira_issue
from app.tools import fetch_jira_issues

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/agent/run")
async def run_agent(request: AgentRequest):
    result = await ai_agent.run(request.query)
    return {"result": result}


@app.post("/summarize")
def summarize():
    try:
        issues = fetch_jira_issues()  # Fetch Jira issues
        results = [
            summarize_jira_issue(isuue["id"], isuue["description"]) for isuue in issues
        ]  # Summarize each issue
        return JSONResponse(
            content=[r.dict() for r in results]
        )  # Return summarized issues
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
