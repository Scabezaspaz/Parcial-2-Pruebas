from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.recarga import calcular_recarga

app = FastAPI(title="RecargaYa API")


class RecargaRequest(BaseModel):
    monto: float
    premium: bool = False


@app.get("/")
def root():
    return {"mensaje": "RecargaYa API funcionando"}


@app.post("/recarga")
def realizar_recarga(request: RecargaRequest):
    try:
        resultado = calcular_recarga(request.monto, premium=request.premium)
        return resultado
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))