import asyncio
import json
import logging
from typing import Any
import xml.etree.ElementTree as ET
from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from servidor.filedb import FileDb
from xero.auth import router_auth
from servidor.secretos import obtener_entorno
from gti.gti import gti
import uvicorn
from webhooks_and_websockets.websocket import websockets_router
from webhooks_and_websockets.webhooks import webhooks_router

# Esta función es temporal
# Fue puesto aqui para poder hacer la prueba
def dict_a_xml(tag: str, diccionario: dict[str, Any]) -> ET.Element:
    root = ET.Element(tag)
    for k, v in diccionario.items():
        if not v:
            continue
        elemento = None
        if type(v) is dict:
            elemento = dict_a_xml(k, v)
        else:
            elemento = ET.Element(k)
            elemento.text = str(v)
        root.append(elemento)
    return root

if __name__ == "__main__":
    entorno = obtener_entorno()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    app = FastAPI()
    app.add_middleware(SessionMiddleware, secret_key=entorno.LLAVE_SESIONES.get_secret_value())

    app.frontend("/app", directory="./interfaz/build")

    auth, _ = router_auth("/app")
    app.include_router(auth)
    app.include_router(websockets_router)
    app.include_router(webhooks_router)

    app.add_middleware(SessionMiddleware,
        secret_key=entorno.LLAVE_SESIONES.get_secret_value(),
        max_age=1800 # 30 minutos, al igual que el access_token de Xero
    )

    # Lugar temporal para recibir el JSON
    # Esto fue puesto aquí para poner a andar una implementación lo más rápido posible
    @app.post("/enviar-json")
    async def recibir_xml(request: Request):
        logger.info("Recibiendo factura JSON del cliente...")
        diccionario = await request.json()

        logger.debug("Se ha recibido el siguiente body: " + str(diccionario))

        root = ET.Element("Documentos")
        factura_xml = dict_a_xml("FacturaElectronicaXML", diccionario)
        root.append(factura_xml)
        factura_str = ET.tostring(root, encoding="unicode")

        logger.debug("Se ha creado el siguiente XML: " + factura_str)

        resultado = await gti().subir_factura(factura_str)
        return {"resultado": str(resultado)}

    config = uvicorn.Config(app, "localhost", port=entorno.PUERTO)
    servidor = uvicorn.Server(config)

    asyncio.run(servidor.serve())