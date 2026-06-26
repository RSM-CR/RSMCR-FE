import asyncio
import json
from typing import Any
import xml.etree.ElementTree as ET
from fastapi import FastAPI, Request
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

entorno = obtener_entorno()

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=entorno.LLAVE_SESIONES.get_secret_value())

filedb = FileDb()

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
    diccionario = await request.json()

    root = ET.Element("Documentos")
    factura_xml = dict_a_xml("FacturaElectronicaXML", diccionario)
    root.append(factura_xml)
    factura_str = ET.tostring(root, encoding="unicode")

    resultado = await gti().subir_factura(factura_str)
    return {"resultado": str(resultado)}

@app.get("/api/recent-xml")
async def recent_xml(count: int = 10):
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

if __name__ == "__main__":

    # Lanzamiento normal de uvicorn a menos que se active ngrok temporalmente.
    ngrok_token = os.getenv("NGROK_AUTHTOKEN")
    use_ngrok = os.getenv("USE_NGROK") == "1" or bool(ngrok_token)

    if use_ngrok:
        # Comando temporal para exponer el servidor con ngrok. Fácil de quitar: borrar la
        # variable de entorno `USE_NGROK` o `NGROK_AUTHTOKEN` y este bloque no se ejecutará.
        cmd = [
            "py", "-m", "ngrok",
            "--authtoken", ngrok_token or "",
            "uvicorn", "servidor.servidor:app",
            "--port", str(entorno.PUERTO),
            "--host", "localhost",
            "--reload",
        ]
        print("Iniciando ngrok temporalmente:", " ".join(cmd))
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