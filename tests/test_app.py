import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_ask_question_success():
    # Send video_id and question as query parameters, not as JSON
    response = client.post("/ask", params={"video_id": "YZbAW2f7-T0", "question": "summarize the entire content"})
    assert response.status_code == 200  # Expecting 200 for a successful request
    data = response.json()

    # Check if there's an answer or an error message
    if "answer" in data:
        assert isinstance(data["answer"], str)
    elif "error" in data:
        print(f"Error: {data['error']}")
        assert False, "Failed to retrieve a valid answer"
    else:
        assert False, "No 'answer' or 'error' field in the response"
def test_ask_question_missing_video_id():
    response = client.post("/ask", params={"question": "Where is it?"})
    assert response.status_code == 422 

def test_ask_question_missing_question():
    response = client.post("/ask", params={"video_id": "YZbAW2f7-T0"})
    assert response.status_code == 422 

