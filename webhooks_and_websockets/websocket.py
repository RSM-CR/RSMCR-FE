from fastapi import FastAPI, WebSocket, APIRouter
from webhooks_and_websockets.websockets_processor import processor
import logging

websockets_router = APIRouter()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@websockets_router.websocket("/app")
async def websockets(websocket: WebSocket):
    await processor.connect(websocket)

    try:
        while True:
            await websocket.receive_text
    except Exception as e:
        logger.error("Error en el WebSocket: %s", e)
        processor.disconnect(websocket)