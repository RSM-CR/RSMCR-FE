from fastapi import FastAPI, Request, Response
from xero.auth import obtener_cliente
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/tenants")
async def listar_tenants(request: Request) -> Response:
    cliente = await obtener_cliente()
    response = await cliente.get("https://api.xero.com/connections")
    if response.status_code != 200:
        return JSONResponse(content={"error": "No se pudo obtener tenants"}, status_code=response.status_code)
    tenants = response.json()
    return JSONResponse(content=tenants)