import asyncio
import json
from typing import Any
import xml.etree.ElementTree as ET
from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from servidor.filedb import FileDb
from xero.auth import router_auth
from servidor.secretos import obtener_entorno
import uvicorn

# Esta función es temporal
# Fue puesto aqui para poder hacer la prueba
def dict_a_xml(tag: str, diccionario: dict[str, Any]) -> ET.Element:
    root = ET.Element(tag)
    for k, v in diccionario.items():
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

    app = FastAPI()
    app.add_middleware(SessionMiddleware, secret_key=entorno.LLAVE_SESIONES.get_secret_value())

    app.frontend("/app", directory="./interfaz/build")

    auth, _ = router_auth("/app")
    app.include_router(auth)

    app.add_middleware(SessionMiddleware,
        secret_key=entorno.LLAVE_SESIONES.get_secret_value(),
        max_age=1800 # 30 minutos, al igual que el access_token de Xero
    )

    # Lugar temporal para recibir el JSON
    # Esto fue puesto aquí para poner a andar una implementación lo más rápido posible
    @app.post("/enviar-json")
    async def recibir_xml(request: Request):
        diccionario = await request.json()

        root = ET.Element("Documentos")
        factura_xml = dict_a_xml("FacturaElectronicaXML", diccionario)
        root.append(factura_xml)
        factura_str = ET.tostring(root, encoding="unicode")

    config = uvicorn.Config(app, "localhost", port=entorno.PUERTO)
    servidor = uvicorn.Server(config)

    asyncio.run(servidor.serve())