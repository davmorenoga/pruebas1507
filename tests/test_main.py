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

def test_add_sale_success():
    # Crear cliente
    client_resp = client.post("/clients", json={"name": "Cliente venta"})
    client_id = client_resp.json()["client_id"]

    # Crear producto
    product_resp = client.post("/products", json={"name": "Producto venta", "price": 50.0})
    product_id = product_resp.json()["product_id"]

    # Registrar venta
    sale_resp = client.post("/sales", json={
        "client_id": client_id,
        "product_id": product_id,
        "quantity": 2
    })
    assert sale_resp.status_code == 200
    assert sale_resp.json()["message"] == "Sale recorded"
