from webhooks_and_websockets.websocket import websockets_router
from webhooks_and_websockets.webhooks import webhooks_router
from fastapi import FastAPI, Request, Response

app = FastAPI()
app.include_router(websockets_router)
app.include_router(webhooks_router)