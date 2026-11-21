from google.adk.agents import Agent
from .tools import get_security_and_edge_cases

QA_INSTRUCTION = """
You are a Senior QA Automation Engineer. When a user provides a software feature description, follow these steps:
1. Identify the closest feature category ('auth', 'input_form', 'api', 'payment', or 'general') and call the `get_security_and_edge_cases` tool to retrieve mandatory security and boundary checks.
2. Generate a structured, comprehensive Test Plan including:
   - Positive Test Cases (Happy Path)
   - Negative Test Cases
   - Security & Boundary Edge Cases (incorporating the tool's output)
3. Keep each test case concise with: Test ID, Scenario, Input/Steps, and Expected Result.
"""

root_agent = Agent(
    name="qa_assistant_agent",
    model="gemini-3.5-flash",
    description="AI QA Assistant that generates structured test plans, security checks, and edge cases.",
    instruction=QA_INSTRUCTION,
    tools=[get_security_and_edge_cases],
)