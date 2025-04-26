import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_ask_question_missing_video_id():
    response = client.post("/ask", params={"question": "Where is it?"})
    assert response.status_code == 422 

def test_ask_question_missing_question():
    response = client.post("/ask", params={"video_id": "YZbAW2f7-T0"})
    assert response.status_code == 422 

