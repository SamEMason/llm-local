from fastapi import status
from fastapi.testclient import TestClient
from src.main import app
import os

client = TestClient(app)


def test_root():
    response = client.get("/")
    env = os.getenv("ENV", "undefined")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": f"Running in {env} mode"}
