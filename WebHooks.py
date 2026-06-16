import json
import os
import hmac
import hashlib
import base64
import logging
from fastapi import FastAPI, Request, Response, BackgroundTasks
from dotenv import load_dotenv
from webhooks_processor import process_webhook_events

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

WEBHOOK_KEY = os.getenv("XERO_WEBHOOK_SECRET")
if not WEBHOOK_KEY:
    raise RuntimeError("XERO_WEBHOOK_SECRET no está configurado")

@app.get("/xero/webhooks")
async def xero_webhooks(request: Request, background_tasks: BackgroundTasks):
    body = await request.body()
    signature = request.headers.get("X-Xero-Signature", "")

    computed_signature = base64.b64encode(
        hmac.new(WEBHOOK_KEY.encode(), body, hashlib.sha256).digest()
    ).decode()

    if not hmac.compare_digest(signature, computed_signature):
        logger.error("Firma de webhook inválida")
        return Response(status_code=401)

    payload = json.loads(body)
    background_tasks.add_task(process_webhook_events, payload)
    return Response(status_code=200)

if __name__ == "__main__":
    import uvicorn
    from servidor.secretos import obtener_entorno

    entorno = obtener_entorno()
    uvicorn.run('WebHooks:app', host="127.0.0.1", port=int(entorno.PUERTO), reload=True, log_level="info")