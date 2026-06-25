import asyncio
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from servidor.secretos import obtener_entorno
import uvicorn

if __name__ == "__main__":
    entorno = obtener_entorno()

    app = FastAPI()

    app.frontend("/app", directory="./interfaz/build")

    app.add_middleware(SessionMiddleware,
        secret_key=entorno.LLAVE_SESIONES.get_secret_value(),
        max_age=1800 # 30 minutos, al igual que el access_token de Xero
    )

    config = uvicorn.Config(app, "localhost", port=entorno.PUERTO)
    servidor = uvicorn.Server(config)

    asyncio.run(servidor.serve())