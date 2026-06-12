from fastapi import FastAPI, Request, BackgroundTasks
from starlette.middleware.sessions import SessionMiddleware
# from xero_python.api_client import ApiClient
# from xero_python.accounting import AccountingApi
# from authlib.integrations.requests_client import OAuth2Session
from authlib.integrations.starlette_client import OAuth

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="porfa-cambiame-soy-insegura") # No usar SessionMiddleware para la versión final porque le manda las credenciales al usuario

id_cliente = input("Introduce el ID del cliente dado por Xero (este no será almacenado)\n> ")
secreto_cliente = input("Introduce el secreto del cliente dado por Xero (este no será almacenado)\n> ")
id_factura = input("Introduce el identificador de la factura (este no será almacenado)\n> ")

token = None

oauth = OAuth()
oauth.register(
    name="xero",
    client_id=id_cliente,
    client_secret=secreto_cliente,
    access_token_url="https://login.xero.com/identity/connect/token",
    access_token_params=None,
    authorize_url="https://login.xero.com/identity/connect/authorize",
    api_base_url="https://api.xero.com/",
    client_kwargs={'scope': 'app.connections accounting.invoices.read'}, # Añadir 'offline_access' servicios más largos
)

def apagar_servidor():
    print("Se ha recuperado el XML. Apagando servidor...")
    import os, signal
    pid = os.getpid()
    os.kill(pid, signal.SIGINT)

@app.get("/login/xero")
async def login(request: Request):
    print("Iniciando sesión...")
    redirect_uri = request.url_for("auth")
    return await oauth.xero.authorize_redirect(request, redirect_uri)

@app.get("/auth/xero")
async def auth(request: Request, background_tasks: BackgroundTasks):
    print("Autenticándose...")
    global token
    token = await oauth.xero.authorize_access_token(request)
    print("Autenticación completada. Descargando factura como XML...")
    factura = oauth.xero.get(f"/api.xro/2.0/Invoices/{id_factura}")
    factura.raise_for_status()
    background_tasks.add_task(apagar_servidor)
    return factura

if __name__ == "__main__":
    print("\033[32mIniciando servidor...\033[0m")
    print("Espera a que el servidor inicie y abre \033[34mhttp://localhost:8000/login/xero\033[0m")

    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)