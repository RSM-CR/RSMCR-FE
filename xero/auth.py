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
import json
from fastapi import FastAPI, Request, BackgroundTasks, APIRouter, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from authlib.integrations.starlette_client import OAuth, StarletteOAuth2App
from authlib.integrations.httpx_client import AsyncOAuth2Client
from fastapi.staticfiles import StaticFiles
from pydantic import SecretStr
from starlette.middleware.sessions import SessionMiddleware
from servidor.secretos import obtener_entorno
from servidor.token import Tenant, Token
from dotenv import set_key
import logging
from typing import Any

_entorno = obtener_entorno()
_logger = logging.Logger("XeroAuth")

_token_actualizacion = _entorno.TOKEN_ACTUALIZACION_XERO.get_secret_value()

_cliente: AsyncOAuth2Client | None = None

def router_auth(redirigir_a: str) -> tuple[APIRouter, StarletteOAuth2App]:
    """Crea un [`APIRouter`](https://fastapi.tiangolo.com/reference/apirouter/) con todos los
    endpoints necesarios para manejar el inicio de sesión en Xero.
    
    :param str redirigir_a: Especifica el link al cual redirigir al usuario una vez la autenticación se complete con éxito.
    :returns: Una tupla con un [`APIRouter`](https://fastapi.tiangolo.com/reference/apirouter/) y un
    [`StarletteOAuth2App`](https://docs.authlib.org/en/stable/oauth2/client/web/starlette.html)"""
    return _router_auth(redirigir_a)

def _router_auth(redirigir_a: str, admin = False) -> tuple[APIRouter, StarletteOAuth2App]:
    """Crea un [`APIRouter`](https://fastapi.tiangolo.com/reference/apirouter/) con todos los
    endpoints necesarios para manejar el inicio de sesión en Xero.
    
    :param str redirigir_a: Especifica el link al cual redirigir al usuario una vez la autenticación se complete con éxito.
    :param bool admin: Controla si se genera un nuevo token de actualización para `.env`. Esto solo debería ser `True` si se
    trata del flujo de inicio de sesión inicial que sucede cuando se configura el servidor.
    :returns: Una tupla con un [`APIRouter`](https://fastapi.tiangolo.com/reference/apirouter/) y un
    [`StarletteOAuth2App`](https://docs.authlib.org/en/stable/oauth2/client/web/starlette.html)"""
    router = APIRouter(prefix="/xero")

    id_cliente = _entorno.ID_CLIENTE_XERO.get_secret_value()
    secreto_cliente = _entorno.SECRETO_CLIENTE_XERO.get_secret_value()

    token: dict | None = None

    oauth = OAuth()
    kwargs = {'scope': 'openid profile email offline_access accounting.invoices.read'} if admin else {'scope': 'openid profile email accounting.invoices.read'}
    cliente: StarletteOAuth2App = oauth.register(
        name="xero",
        client_id=id_cliente,
        client_secret=secreto_cliente,
        access_token_url="https://login.xero.com/identity/connect/token",
        access_token_params=None,
        authorize_url="https://login.xero.com/identity/connect/authorize",
        server_metadata_url="https://identity.xero.com/.well-known/openid-configuration",
        api_base_url="https://api.xero.com/",
        client_kwargs=kwargs
    )

    @router.get("/login")
    async def login(request: Request):
        _logger.info("Iniciando sesión...")
        url_auth = request.url_for("auth")
        return await cliente.authorize_redirect(request, url_auth) # Esto devuelve el state pero authlib lo valida automáticamente

    @router.get("/auth")
    async def auth(code: str, request: Request):
        _logger.info("Autenticándose...")
        token_xero = await cliente.authorize_access_token(request)

        if admin:
            token_actualizacion: str = token_xero.get("refresh_token") # type: ignore
            _logger.info(f"Estableciendo TOKEN_ACTUALIZACION_XERO a {token_actualizacion}")
            set_key(".env", "TOKEN_ACTUALIZACION_XERO", token_actualizacion)

        token_id: dict[str, str] = await cliente.parse_id_token(token_xero, nonce=None) # type: ignore
        tenants_json: list[dict[str, str]] = json.load(await cliente.get("https://api.xero.com/connections", token=token_xero))

        tenants: list[Tenant] = [Tenant(tenantId=tenant.get("tenantId", ""), tenantName=tenant.get("tenantName", "")) for tenant in tenants_json]

        token = Token(sub=token_id.get("sub", ""), tenants=tenants)

        # HACK: Esto debería ser reemplazado en el futuro cuando tengamos base de datos
        request.session["token"] = jsonable_encoder(token)

        return RedirectResponse(url=redirigir_a)
    
    @router.get("/tenants/get", response_model=Token)
    async def obtener_tenants(request: Request) -> JSONResponse:
        token = request.session.get("token") 
        if token is None:
            return JSONResponse(content={"error": "No tienes autorización. Inicia sesión primero."}, status_code=status.HTTP_403_FORBIDDEN)

        return JSONResponse(token.get("tenants"))

    return router, cliente

async def _iniciar_sesion() -> None:
    if _token_actualizacion and _entorno.ID_TENANT_XERO:
        print("Parece que ya has iniciado sesión en Xero antes... ¿Deseas volvera iniciar sesión? s/N")
        if (iniciar_sesion := input("> ").lower()) != "s" and iniciar_sesion != "y":
            return

    app = FastAPI()
    app.add_middleware(SessionMiddleware, secret_key=_entorno.LLAVE_SESIONES.get_secret_value())

    # Hay que montar el frontend para obtener el JavaScript y el CSS
    app.frontend("/app", directory="./interfaz/build", fallback="index.html")

    router, cliente = _router_auth("/app/tenants/", True)
    app.include_router(router)

    @app.post("/xero/tenants/post/{id}")
    async def establecer_tenant(id: str, request: Request):
        if request.session.get("token") is None:
            return JSONResponse(content={"error": "No tienes autorización."}, status_code=status.HTTP_403_FORBIDDEN)
        
        logging.info(f"Estableciendo ID_TENANT_XERO a {id}")
        set_key(".env", "ID_TENANT_XERO", id)
        _entorno.ID_TENANT_XERO = id
        return "Se ha establecido el ID de tenant con éxito."

    @app.get("/apagar")
    async def endpoint_apagar(request: Request, tasks: BackgroundTasks):
        _logger.info("Apagando servidor. La autenticación con Xero dejará de estar disponible")
        print("La autenticación fue exitosa. Apagando servidor...")
        tasks.add_task(apagar_servidor)
        return f"La autenticación fue exitosa y se ha establecido ID_TENANT_XERO a {_entorno.ID_TENANT_XERO}. Regresa al script de configuración."

    import uvicorn
    config = uvicorn.Config(app, host="localhost", port=_entorno.PUERTO, loop="asyncio")
    servidor = uvicorn.Server(config)

    def apagar_servidor():
        servidor.should_exit = True

    _logger.info("Iniciando endpoints de autenticación de Xero...")
    print("\033[32mIniciando servidor para la autenticación...\033[0m")
    print(f"Abre \033[34mhttp://localhost:{_entorno.PUERTO}/xero/login\033[0m e inicia sesión en tu cuenta de Xero")
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
    _entorno.TOKEN_ACTUALIZACION_XERO = SecretStr(_token_actualizacion)

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