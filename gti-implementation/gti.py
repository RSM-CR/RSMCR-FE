from destination import destination as ds
from fastapi import FastAPI, Request, Response
from zeep import AsyncClient
from zeep.transports import AsyncTransport
import httpx

class gti (ds):
    app = FastAPI

    @app.get("/get_gti")
    async def get_document(req: Request):
        body = await req.json()
        return body
        
    @app.post("/post_gti")
    async def upload_facture(body: get_document):

        transport = AsyncTransport(client=httpx.AsyncClient)
        client = AsyncClient(
            "https://www.facturaelectronica.cr",
            transport=transport
        )

        await client.service.facturaelectronica(
            space1=body["pvcDocumentosXML"],
            space2=body["pvcCorreoUsuario"],
            space3=body["pvcClaveUsuario"]
        )

        return Response(content='{"ok": true}', media_type="application/json")