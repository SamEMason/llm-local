from fastapi.testclient import TestClient
from src.main import app
import os

client = TestClient(app)


def test_root():
    response = client.get("/")
    env = os.getenv("ENV", "undefined")
    assert response.status_code == 200
    assert response.json() == {"message": f"Running in {env} mode"}
