"""Este módulo posee una variedad de funciones que permiten autenticarse e interactuar con la API de Xero con facilidad.
**Sobre el token de autenticación**
Para acceder al token de autenticación, se puede usar `obtener_cliente().token`. No obstante, el formato de este no está
muy bien documentado. Por ende, se incluye a continuación:
```
{
    \"id_token\": \"Todos los datos del token de identificación en base64\",
    \"access_token\": \"Todos los datos del token de acceso en base64. Este es el que se usa para acceder a las APIs\",
    \"expires_in\": 1800, # El tiempo en el que expirará el token de acceso. Son 1800 segundos, lo que corresponde a 30 minutos
    \"token_type\": \"Bearer\", # El tipo de token. Para Xero, este debería de ser "Bearer"
    \"refresh_token\": \"El token de actualización, que es válido por más tiempo que el token de acceso. Se usa para obtener nuevos tokens de acceso\",
    \"scope\": \"openid profile email accounting.invoices.read offline_access\", # El scope que se solicitó inicialmente al iniciar sesión
    \"expires_at\": 1781710252 # La fecha cuándo el token de acceso expira
}
```
Este consiste en un diccionario de Python con las llaves que se encuentran arriba."""
import asyncio
from secrets import token_hex
from fastapi import FastAPI, Request, BackgroundTasks
from authlib.integrations.starlette_client import OAuth, StarletteOAuth2App
from authlib.integrations.httpx_client import AsyncOAuth2Client
from starlette.middleware.sessions import SessionMiddleware
from servidor.secretos import obtener_entorno
from dotenv import set_key
import json
import logging
from typing import Any

_entorno = obtener_entorno()
_logger = logging.Logger("XeroAuth")

_token_actualizacion = _entorno.TOKEN_ACTUALIZACION_XERO.get_secret_value()

_cliente: AsyncOAuth2Client | None = None

async def _iniciar_sesion() -> None:
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

def iniciar_sesion() -> None:
    """Abre un servidor y genera un link para iniciar sesión, que es impreso en la consola.
    Luego, espera hasta que el usuario inicie sesión en dicho link y almacena los credenciales
    de forma segura en las variables de entorno. Por último, el servidor se cierra de forma
    automática."""
    asyncio.run(_iniciar_sesion())

async def _al_actualizar_token(token: dict, refresh_token=None, access_token=None):
    """Callback que se ejecuta cada vez que un token se actualiza tanto de forma manual como
    automática. Esta función está diseñada para ser pasada al constructor de
    [OAuth2Client](https://docs.authlib.org/en/stable/oauth2/client/http/api.html#httpx-oauth-2-0). Revisa
    la
    [documentación de Authlib](https://docs.authlib.org/en/stable/oauth2/client/http/index.html#manually-refreshing-tokens)
    para obtener más información"""
    _logger.info("Actualizando token de acceso...")
    global _token_actualizacion
    
    token_actualizacion_nuevo: str = token.get("refresh_token") # type: ignore
    logging.info(f"Estableciendo TOKEN_ACTUALIZACION_XERO a {token_actualizacion_nuevo}")
    set_key(".env", "TOKEN_ACTUALIZACION_XERO", token_actualizacion_nuevo)
    _token_actualizacion = token_actualizacion_nuevo

def _adjuntar_headers(url, headers, body):
    global _entorno
    headers["Accept"] = "application/json"
    headers["Xero-tenant-id"] = _entorno.ID_TENANT_XERO
    return url, headers, body

async def crear_cliente() -> AsyncOAuth2Client:
    """Crea un
    [OAuth2Client](https://docs.authlib.org/en/stable/oauth2/client/http/api.html#httpx-oauth-2-0)
    correctamente configurado para su uso con Xero y HTTPX.
    En la mayoría de los casos, se puede reutilizar el mismo cliente para varias solicitudes. Por ende,
    se recomienda usar [obtener_cliente()](auth.obtener_cliente) a menos que haya una razón específica
    para usar varios clientes"""
    global _token_actualizacion
    if not _token_actualizacion:
        e = TypeError("El token de actualización está vacío, por lo que no se puede interactuar con la API de Xero. Ejecuta \"python -m servidor.configurar\" para iniciar sesión en Xero y obtener el token.")
        _logger.critical(e)

    cliente = AsyncOAuth2Client(
        client_id=_entorno.ID_CLIENTE_XERO.get_secret_value(),
        client_secret=_entorno.SECRETO_CLIENTE_XERO.get_secret_value(),
        token_endpoint_auth_method="client_secret_post",
        update_token=_al_actualizar_token
    )
    cliente.register_compliance_hook("protected_request", _adjuntar_headers)
    await cliente.refresh_token("https://login.xero.com/identity/connect/token", refresh_token=_token_actualizacion)

    _logger.info("Se ha creado un cliente y se ha obtenido la autorización")

    return cliente

async def obtener_cliente() -> AsyncOAuth2Client:
    """Obtiene un cliente compartido que puede ser utilizado en todo el programa. Este es el enfoque
    recomendado para la mayoría de situaciones, a menos de que se requieran clientes distintos por
    alguna razón en concreto"""
    global _cliente
    if _cliente is None:
        _cliente = await crear_cliente()
    return _cliente


if __name__ == "__main__":
    iniciar_sesion()
    print(asyncio.run(crear_cliente()).token)