from fastapi import FastAPI
from metrics import setup_metrics

app = FastAPI()

# Configura Prometheus con middleware y endpoint /metrics
setup_metrics(app)

@app.get("/")
def root():
    return {"message": "Hola desde FastAPI"}
