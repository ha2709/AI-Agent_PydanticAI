 
#  AI Agent FastAPI Server

This project implements AI-powered agents using `PydanticAI`, `OpenAI`, and `FastAPI` to automate common developer workflows such as:

- ✅ Jira issue analysis  
- ✅ Code debugging  
- ✅ Log inspection

---

## 🚀 Getting Started

### 📦 Installation

```bash
 
# Create and activate virtual environment
python -m venv env
source env/bin/activate  # or `.\env\Scripts\activate` on Windows
```

# Install dependencies

`pip install -r requirements.txt`
 
## Run the Server

``` bash
uvicorn app.main:app --reload
```

The API will be available at:

` http://localhost:8000`

## 📡 API Endpoint

### `POST /agent/run`

Run any supported query through the AI agent.

---

###  Example Inputs

#### Jira Issue Analysis

```json
{
  "query": "Analyze this Jira issue: 'App crash on login', description: 'App crashes when logging in with empty credentials'"
}
```

#### Code Debugging

```json
{
  "query": "Debug this code: if user_input == None: print('bad input')"
}
```

#### Log Inspection
 
 ```json
 {
  "query": "Check these logs: ['INFO: User login', 'ERROR: Null pointer exception', 'WARNING: Timeout']"
}
```


###  POST /summarize

No request body is required.

Returns a list of summarized Jira issues

```json
[
  {
    "ticket_id": "ABC-123",
    "summary": "App crashes on login when credentials are empty",
    "severity": "High",
    "component": "Authentication",
    "assignee": "John Doe"
  }
]
```
