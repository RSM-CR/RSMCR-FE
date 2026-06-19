from fastapi import WebSocket
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebSocketProcessor():
        def __init__(self):
                self.activated_connections: list[WebSocket] = []

        async def connect(self, websocket: WebSocket):
                await websocket.accept()
                self.activated_connections.append(websocket)

        def disconnect(self, websocket: WebSocket):
                self.activated_connections.remove(websocket)

        async def broadcast(self, message: dict):
                disconnected = []

                for connection in self.activated_connections:
                        try:
                               await connection.send_json()
                        except Exception as e:
                                logger.error("Error durante el procesamiento del WebSocket: %s", e)
                                disconnected.append(connection)

                for connection in disconnected:
                        self.disconnect(self.connection)

processor = WebSocketProcessor()
