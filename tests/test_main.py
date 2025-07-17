from fastapi.testclient import TestClient
from run import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola desde FastAPI"}

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"app_requests_total" in response.content
