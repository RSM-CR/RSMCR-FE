from secrets import token_hex
from pathlib import Path
from fastapi import FastAPI, Request, BackgroundTasks
from authlib.integrations.starlette_client import OAuth, StarletteOAuth2App
from starlette.middleware.sessions import SessionMiddleware
from servidor.secretos import obtener_entorno
from base64 import b64encode
from dotenv import set_key
import json
import logging

entorno = obtener_entorno()
logger = logging.Logger("XeroAuth")

def iniciar_sesion():
    if entorno.TOKEN_ACTUALIZACION and entorno.ID_TENANT:
        print("Parece que ya has iniciado sesión en Xero antes... ¿Deseas volvera iniciar sesión? s/N")
        if (iniciar_sesion := input("> ").lower()) != "s" and iniciar_sesion != "y":
            return

    app = FastAPI()
    # No se ocupa guardar el secret_key porque la sesión es de un solo uso
    app.add_middleware(SessionMiddleware, secret_key=token_hex(32))

    id_cliente = entorno.ID_CLIENTE.get_secret_value()
    secreto_cliente = entorno.SECRETO_CLIENTE.get_secret_value()

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
        client_kwargs={'scope': 'openid profile email offline_access accounting.invoices.read'}
    )

    def apagar_servidor():
        logger.info("Apagando servidor. La autenticación con Xero dejará de estar disponible")
        print("La autenticación fue exitosa. Apagando servidor...")
        import os, signal
        pid = os.getpid()
        os.kill(pid, signal.SIGINT)

    @app.get("/xero/login")
    async def login(request: Request):
        logger.info("Iniciando sesión...")
        url_auth = request.url_for("auth")
        return await xero.authorize_redirect(request, url_auth) # Esto devuelve el state pero authlib lo valida automáticamente

    @app.get("/xero/auth")
    async def auth(code: str, request: Request, tasks: BackgroundTasks):
        global token
        global id_tenant

        logger.info("Autenticándose...")
        bytes_base64 = b64encode((id_cliente + ":" + secreto_cliente).encode("utf-8"))

        token = await xero.authorize_access_token(request)

        tenants_disponibles = json.load(await xero.get("https://api.xero.com/connections", token=token))
        if len(tenants_disponibles) > 1:
            logger.warning("Hay varios tenants disponibles. Se escogió el primero disponible")

        id_tenant = tenants_disponibles[0]["tenantId"]
        logging.info(f"Estableciendo ID_TENANT a {id_tenant}")
        set_key(".env", "ID_TENANT", id_tenant)

        token_actualizacion: str = token.get("refresh_token") # type: ignore
        logging.info(f"Estableciendo TOKEN_ACTUALIZACION a {token_actualizacion}")
        set_key(".env", "TOKEN_ACTUALIZACION", token_actualizacion)

        tasks.add_task(apagar_servidor)

        return "Autenticación exitosa"
    
    logger.info("Iniciando endpoints de autenticación de Xero...")
    print("\033[32mIniciando servidor para la autenticación...\033[0m")
    print("Espera a que el servidor inicie y abre \033[34mhttp://localhost:8000/xero/login\033[0m")
    import uvicorn
    uvicorn.run(app, host="localhost", port=entorno.PUERTO)

if __name__ == "__main__":
    iniciar_sesion()