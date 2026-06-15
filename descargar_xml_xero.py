from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth, StarletteOAuth2App
from dotenv import load_dotenv, set_key
from pathlib import Path
from base64 import b64encode
from httpx import Response
import xml.etree.ElementTree as ET
import os
import json

camino_env = ".env"

archivo_env = Path(camino_env)

if not archivo_env.exists():
    print("No se encontró un archivo .env. Creando...")
    archivo_env.touch()

load_dotenv(camino_env, override=True)

id_cliente = os.getenv("ID_CLIENTE") or ""
if not id_cliente:
    print("No se encontró un ID del cliente en las variables de entorno")
    id_cliente = input("Introduce el ID del cliente generado por Xero\n> ")
    set_key(camino_env, "ID_CLIENTE", id_cliente)

secreto_cliente = os.getenv("SECRETO_CLIENTE") or ""
if not secreto_cliente:
    print("No se encontró el secreto del cliente en las variables de entorno")
    secreto_cliente = input("Introduce el secreto del cliente generado por Xero\n> ")
    set_key(camino_env, "SECRETO_CLIENTE", secreto_cliente)

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="porfa-cambiame-soy-insegura") # No usar SessionMiddleware para la versión final porque le manda las credenciales al usuario

token = ""
id_tenant = None

oauth = OAuth()
xero: StarletteOAuth2App = oauth.register(
    name="xero",
    client_id=id_cliente,
    client_secret=secreto_cliente,
    access_token_url="https://login.xero.com/identity/connect/token",
    access_token_params=None,
    authorize_url="https://login.xero.com/identity/connect/authorize",
    server_metadata_url="https://identity.xero.com/.well-known/openid-configuration",
    api_base_url="https://api.xero.com/",
    client_kwargs={'scope': 'openid profile email accounting.invoices.read'} # Añadir 'offline_access' para servicios más largos
)

def apagar_servidor():
    print("Se ha recuperado el XML. Apagando servidor...")
    import os, signal
    pid = os.getpid()
    os.kill(pid, signal.SIGINT)

@app.get("/login/xero")
async def login(request: Request):
    print("Iniciando sesión...")
    url_auth = request.url_for("auth")
    return await xero.authorize_redirect(request, url_auth) # Esto devuelve el state pero authlib lo valida automáticamente

@app.get("/auth/xero")
async def auth(code: str, request: Request):
    global token
    global id_tenant

    print("Autenticándose...")
    bytes_base64 = b64encode((id_cliente + ":" + secreto_cliente).encode("utf-8"))

    token = await xero.authorize_access_token(request)

    tenants_available = json.load(await xero.get("https://api.xero.com/connections", token=token))
    if len(tenants_available) > 1:
        print("Hay varios tenants disponibles. Se escogió el primero disponible")
    id_tenant = tenants_available[0]["tenantId"]

    print("Autenticación exitosa.")
    print("Abre \033[34mhttp://localhost:8000/download/xml/id_factura\033[0m en tu navegador para descargar una factura")
    print("Reemplaza id_factura por el identificador único de la factura")
    return f"""Autenticación exitosa.
    Abre http://localhost:8000/download/xml/id_factura en tu navegador para descargar una factura
    Reemplaza id_factura por el identificador único de la factura"""

@app.get("/download/xml/{id_factura}")
async def download(id_factura: str, request: Request):
    print("Descargando factura...")

    headers = {
        "Xero-tenant-id": id_tenant
    }

    factura: Response = await xero.get(f"/api.xro/2.0/Invoices/{id_factura}", token=token, headers=headers)
    factura.raise_for_status()
    print("Descarga completada.")
    return Response(content=factura.content, status_code=200)

if __name__ == "__main__":
    print("\033[32mIniciando servidor...\033[0m")
    print("Espera a que el servidor inicie y abre \033[34mhttp://localhost:8000/login/xero\033[0m")

    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)