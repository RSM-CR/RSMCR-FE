from fastapi import FastAPI, WebSocket, APIRouter
from websockets_processor import processor

app = FastAPI()
websockets_router = APIRouter()

@app.websocket("/app")
async def websockets(websocket: WebSocket):
    await processor.connect(websocket)

    try:
        while True:
            await websocket.receive_text
    except Exception:
        processor.disconnect(websocket)