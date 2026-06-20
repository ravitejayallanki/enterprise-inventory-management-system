
from fastapi import FastAPI

app = FastAPI(title="Enterprise Inventory & Procurement Management System")

@app.get("/health")
def health():
    return {"status": "ok"}
