import os
import uvicorn
from dotenv import load_dotenv
from google.adk.cli.fast_api import get_fast_api_app

load_dotenv()

AGENT_DIR = os.path.dirname(os.path.abspath(__file__))
enable_trace = os.environ.get("TRACE_TO_CLOUD", "false").lower() == "true"

app = get_fast_api_app(
    agents_dir=AGENT_DIR,
    web=True,
    trace_to_cloud=enable_trace,
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)