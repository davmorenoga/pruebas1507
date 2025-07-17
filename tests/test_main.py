from fastapi.testclient import TestClient
from app.main import app  # asegúrate que main.py esté en app/

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"python_gc_objects_collected_total" in response.content
