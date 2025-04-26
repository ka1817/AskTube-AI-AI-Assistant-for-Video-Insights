import sys
import os

# Ensure we can import from main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app  # ✅ Make sure it's `main.py` not `app.py`

client = TestClient(app)

def test_ask_question_success():
    # Send video_id and question as query parameters, not as JSON
    response = client.post("/ask", params={"video_id": "YZbAW2f7-T0", "question": "summarize the entire content"})
    assert response.status_code == 200  # Expecting 200 for a successful request
    data = response.json()
    assert "answer" in data  # The response should contain an "answer" field
    assert isinstance(data["answer"], str)  # The answer should be a string

def test_ask_question_missing_video_id():
    # Send only the question, which should trigger a 422 response due to missing video_id
    response = client.post("/ask", params={"question": "Where is it?"})
    assert response.status_code == 422  # FastAPI returns 422 for missing fields

def test_ask_question_missing_question():
    # Send only the video_id, which should trigger a 422 response due to missing question
    response = client.post("/ask", params={"video_id": "YZbAW2f7-T0"})
    assert response.status_code == 422  # FastAPI returns 422 for missing fields

