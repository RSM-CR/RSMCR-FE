from fastapi import FastAPI, Request, Response
from xero.auth import obtener_cliente
from dotenv import load_dotenv, set_key
import os
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:8000", "*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

@app.get("/getTenants")
async def getTenants(request: Request) -> Response:
    cliente = await obtener_cliente()
    response = await cliente.get("https://api.xero.com/connections")
    if response.status_code != 200:
        return JSONResponse(content={"error": "No se pudo obtener tenants"}, status_code=response.status_code)
    tenants = response.json()
    return JSONResponse(content=tenants)

class TenantData(BaseModel):
    tenantid: str

@app.post("/postTenants")
async def postTenants(data: TenantData) -> None:
    set_key(".env", "ID_TENANT_XERO", data.tenantid)
    load_dotenv(override=True)
    logger.info("Nuevo tenant: %s", os.getenv("ID_TENANT_XERO"))
    return {"message": "correctly recieved"}