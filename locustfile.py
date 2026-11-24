import random
import uuid
from locust import HttpUser, task, between


class QAAssistantUser(HttpUser):
    wait_time = between(2, 5)

    def on_start(self):
        self.user_id = f"load_user_{uuid.uuid4().hex[:8]}"
        response = self.client.post(
            f"/apps/qa_agent/users/{self.user_id}/sessions",
            json={}
        )
        if response.status_code == 200:
            self.session_id = response.json().get("id")
        else:
            self.session_id = None

    @task
    def generate_test_plan(self):
        if not self.session_id:
            return

        prompts = [
            "Create a QA test plan for a user login endpoint",
            "Test a payment checkout API with edge cases",
            "Generate security test cases for a user registration form",
            "Write API test scenarios for a search filter endpoint"
        ]

        payload = {
            "app_name": "qa_agent",
            "user_id": self.user_id,
            "session_id": self.session_id,
            "new_message": {
                "role": "user",
                "parts": [{"text": random.choice(prompts)}]
            }
        }

        with self.client.post(
            "/run",
            json=payload,
            name="/run (QA Agent)",
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Status {response.status_code}: {response.text}")