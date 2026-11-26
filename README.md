# QA Assistant Agent (`v2`)

An AI-powered Quality Assurance (QA) engineering assistant built with **Google Agent Development Kit (ADK)**, **FastAPI**, and **Vertex AI (Gemini)**, containerized with **Docker**, deployed serverless on **Google Cloud Run** with full **Cloud Trace** observability, and load-tested using **Locust**.

## Live Deployment

- **Cloud Run Service URL:** https://qa-assistant-agent-230285243293.us-central1.run.app
- **Region:** `us-central1`
- **Observability:** OpenTelemetry + Google Cloud Trace (`TRACE_TO_CLOUD=TRUE`)

## Key Capabilities & Tools

The agent assists QA engineers in generating structured test plans, security checklists, and ready-to-use boundary payloads:

1. **`get_security_and_edge_cases(feature_category)`**
   - Retrieves mandatory security checks (SQLi, XSS, IDOR, Rate Limiting, Replay Attacks) and boundary edge cases tailored to `auth`, `input_form`, `api`, `payment`, or `general` features.
2. **`generate_boundary_test_data(field_type)`** _(Added in v2)_
   - Generates copy-ready test payloads (`valid_boundary`, `invalid_format`, `security_payloads`, and `edge_cases`) for `email`, `password`, `amount`, and `text` input fields.

## Project Architecture

```text
qa-assistant-agent/
├── qa_agent/
│   ├── __init__.py
│   ├── agent.py          # ADK Agent definition & tool bindings
│   └── tools.py          # Custom QA security & boundary data tools
├── server.py             # FastAPI server exposing ADK Web UI & REST endpoints
├── locustfile.py         # Locust concurrent load testing suite
├── Dockerfile            # Container image definition for Cloud Run
├── requirements.txt      # Production Python dependencies
└── .dockerignore         # Build context exclusions
```

## Load Testing Results (Locust)

Tested against the live Cloud Run endpoint with **5 concurrent virtual users** (`ramp-up: 1 user/sec`):

| Endpoint                                  | Requests | Failures | Median Latency | Min Latency |
| :---------------------------------------- | :------: | :------: | :------------: | :---------: |
| `POST /apps/qa_agent/users/{id}/sessions` |    5     |    0%    |    ~285 ms     |   256 ms    |
| `POST /run` (Full Agent + Tool Execution) |    7     |    0%    |   12,000 ms    |  5,892 ms   |
| **Total (`Aggregated`)**                  |  **12**  |  **0%**  |  **9,800 ms**  | **256 ms**  |

## Running Locally

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start local server on port 8080
python server.py
```

## Running Load Tests

```bash
pip install locust
locust --host=https://qa-assistant-agent-230285243293.us-central1.run.app
```
