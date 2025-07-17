from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

from app.metrics import setup_metrics  # <-- importa setup_metrics si está en carpeta app
from app.routes import router  # <-- importa tus rutas si tienes más

app = FastAPI()

setup_metrics(app)  # <-- activa el middleware y el endpoint /metrics

# Rutas base
@app.get("/")
def root():
    return {"message": "Hola desde FastAPI"}

app.include_router(router)  # <-- si usas APIRouter en routes.py
