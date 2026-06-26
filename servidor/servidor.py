import asyncio
import json
import logging
from typing import Any
import xml.etree.ElementTree as ET
from fastapi import FastAPI, Request, Response
from starlette.middleware.sessions import SessionMiddleware
from servidor.filedb import FileDb
from xero.auth import router_auth
from servidor.secretos import obtener_entorno
from gti.gti import gti
from webhooks_and_websockets.websocket import websockets_router
from webhooks_and_websockets.webhooks import webhooks_router
import uvicorn
import os
import subprocess
import logging
import uuid

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

entorno = obtener_entorno()


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=entorno.LLAVE_SESIONES.get_secret_value())

filedb = FileDb()

auth, _ = router_auth("/app")
app.include_router(auth)
app.include_router(websockets_router)
app.include_router(webhooks_router)



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
    try:
        diccionario = await request.json()
    except json.JSONDecodeError:
        return Response(status_code=400, content="JSON inválido")

    resource_id = str(uuid.uuid4)
    if not resource_id:
        return Response(status_code=400, content="Falta el identificador del documento")

    root = ET.Element("Documentos")
    factura_xml = dict_a_xml("FacturaElectronicaXML", diccionario)
    root.append(factura_xml)
    factura_str = ET.tostring(root, encoding="unicode")

    try:
        logger.debug("Se ha recibido el siguiente body: " + str(diccionario))

        root = ET.Element("Documentos")
        factura_xml = dict_a_xml("FacturaElectronicaXML", diccionario)
        root.append(factura_xml)
        factura_str = ET.tostring(root, encoding="unicode")

        logger.debug("Se ha creado el siguiente XML: " + factura_str)

        resultado = await gti().subir_factura(factura_str)
    except Exception as e:
        return {
            Response(status_code=502, content="Error al comunicarse con GTI"),
            logger.error("Error detallado: %s", e)
        }

    try:
        await filedb.crear("gti", resource_id, factura_str)
    except FileExistsError:
        await filedb.actualizar("gti", resource_id, factura_str)

    return {"resultado": str(resultado)}

@app.get("/api/recent-xml")
async def recent_xml(count: int = 10):
    try:
        documentos = await filedb.obtener_recientes("gti", count, None)
        resultados = []
        for documento in documentos:
            contenido = await documento.obtener_contenido()
            resultados.append({
                "name": documento.nombre,
                "id": documento.id,
                "content": contenido,
            })
        return resultados
    except Exception as e:
        logger.error("Error al enviar XMLs recientes al frontend: %s", e)

if __name__ == "__main__":

    # Lanzamiento normal de uvicorn a menos que se active ngrok temporalmente.
    ngrok_token = os.getenv("NGROK_AUTHTOKEN")
    use_ngrok = os.getenv("USE_NGROK") == "1" or bool(ngrok_token)

    if use_ngrok:
        # Comando temporal para exponer el servidor con ngrok.
        # borrar la variable de entorno `USE_NGROK` o `NGROK_AUTHTOKEN` y este bloque no se ejecutará.
        cmd = [
            "py", "-m", "ngrok",
            "--authtoken", ngrok_token or "",
            "uvicorn", "servidor.servidor:app",
            "--port", str(entorno.PUERTO),
            "--host", "localhost",
            "--reload",
        ]
        logger.info("Iniciando ngrok temporalmente:", " ".join(cmd))
        try:
            proc = subprocess.Popen(cmd)
            proc.wait()
        except KeyboardInterrupt:
            proc.terminate()
            proc.wait()
    else:
        config = uvicorn.Config(app, "localhost", port=entorno.PUERTO)
        servidor = uvicorn.Server(config)

        asyncio.run(servidor.serve())