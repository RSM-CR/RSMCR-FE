import asyncio
from secrets import token_hex
from fastapi import FastAPI, Request, BackgroundTasks
from authlib.integrations.starlette_client import OAuth, StarletteOAuth2App
from authlib.integrations.httpx_client import OAuth2Client
from starlette.middleware.sessions import SessionMiddleware
from servidor.secretos import obtener_entorno
from dotenv import set_key
import json
import logging

_entorno = obtener_entorno()
_logger = logging.Logger("XeroAuth")

_token: dict | None = None
_token_actualizacion = _entorno.TOKEN_ACTUALIZACION_XERO.get_secret_value()

async def _iniciar_sesion():
    if _token_actualizacion and _entorno.ID_TENANT_XERO:
        print("Parece que ya has iniciado sesión en Xero antes... ¿Deseas volvera iniciar sesión? s/N")
        if (iniciar_sesion := input("> ").lower()) != "s" and iniciar_sesion != "y":
            return

    app = FastAPI()
    # No se ocupa guardar el secret_key porque la sesión es de un solo uso
    app.add_middleware(SessionMiddleware, secret_key=token_hex(32))

    id_cliente = _entorno.ID_CLIENTE_XERO.get_secret_value()
    secreto_cliente = _entorno.SECRETO_CLIENTE_XERO.get_secret_value()

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

    @app.get("/xero/login")
    async def login(request: Request):
        _logger.info("Iniciando sesión...")
        url_auth = request.url_for("auth")
        return await xero.authorize_redirect(request, url_auth) # Esto devuelve el state pero authlib lo valida automáticamente

    @app.get("/xero/auth")
    async def auth(code: str, request: Request, tasks: BackgroundTasks):
        global _token
        global id_tenant

        _logger.info("Autenticándose...")

        _token = await xero.authorize_access_token(request)

        tenants_disponibles = json.load(await xero.get("https://api.xero.com/connections", token=_token))
        if len(tenants_disponibles) > 1:
            _logger.warning("Hay varios tenants disponibles. Se escogió el primero disponible")

        id_tenant = tenants_disponibles[0]["tenantId"]
        logging.info(f"Estableciendo ID_TENANT_XERO a {id_tenant}")
        set_key(".env", "ID_TENANT_XERO", id_tenant)

        token_actualizacion: str = _token.get("refresh_token") # type: ignore
        logging.info(f"Estableciendo TOKEN_ACTUALIZACION_XERO a {token_actualizacion}")
        set_key(".env", "TOKEN_ACTUALIZACION_XERO", token_actualizacion)

        tasks.add_task(apagar_servidor)

        return "La autenticación fue exitosa."
    
    import uvicorn
    config = uvicorn.Config(app, host="localhost", port=_entorno.PUERTO, loop="asyncio")
    servidor = uvicorn.Server(config)

    def apagar_servidor():
        _logger.info("Apagando servidor. La autenticación con Xero dejará de estar disponible")
        print("La autenticación fue exitosa. Apagando servidor...")
        servidor.should_exit = True

    _logger.info("Iniciando endpoints de autenticación de Xero...")
    print("\033[32mIniciando servidor para la autenticación...\033[0m")
    print("Abre \033[34mhttp://localhost:8000/xero/login\033[0m e inicia sesión en tu cuenta de Xero")
    await servidor.serve()

def iniciar_sesion():
    asyncio.run(_iniciar_sesion())

def _al_actualizar_token(token, refresh_token=None, access_token=None):
    _logger.info("Actualizando token de acceso...")
    global _token_actualizacion
    
    token_actualizacion_nuevo: str = token.get("refresh_token") # type: ignore
    logging.info(f"Estableciendo TOKEN_ACTUALIZACION_XERO a {token_actualizacion_nuevo}")
    set_key(".env", "TOKEN_ACTUALIZACION_XERO", token_actualizacion_nuevo)
    _token_actualizacion = token_actualizacion_nuevo

def crear_cliente() -> OAuth2Client:
    cliente = OAuth2Client(
        client_id=_entorno.ID_CLIENTE_XERO.get_secret_value(),
        client_secret=_entorno.SECRETO_CLIENTE_XERO.get_secret_value(),
        token_endpoint_auth_method="client_secret_post",
        update_token=_al_actualizar_token
    )
    return cliente

def obtener_token() -> dict:
    global _token
    global _token_actualizacion
    if _token is not None:
        return _token

    if not _token_actualizacion:
        e = TypeError("El token de actualización está vacío, por lo que no se puede interactuar con la API de Xero. Ejecuta \"python -m servidor.configurar\" para iniciar sesión en Xero y obtener el token.")
        _logger.critical(e)

    xero = crear_cliente()
    _token = xero.refresh_token("https://login.xero.com/identity/connect/token", refresh_token=_token_actualizacion)

    # OAuth2Client sí tiene un método .close(), pero no está siendo detectado por alguna razón
    xero.close() # type: ignore

    return _token # type: ignore

if __name__ == "__main__":
    iniciar_sesion()
    print(obtener_token())