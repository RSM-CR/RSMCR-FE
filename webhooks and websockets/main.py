from websocket import websockets_router
from webhooks import webhooks_router
from fastapi import FastAPI, Request, Response

app = FastAPI()
app.include_router(websockets_router, webhooks_router)