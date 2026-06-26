import asyncio
import logging

from abstracciones.destino import Destino as ds
from zeep import AsyncClient
from zeep.transports import AsyncTransport
from zeep.plugins import HistoryPlugin
import httpx
from servidor.secretos import obtener_entorno

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

WSDL_URL = "https://pruebas.gticr.com/AplicacionFEPruebas/WSCargaFactura/Pruebas/GTICargaFactura.asmx?WSDL"


class gti(ds):
    _service = None

    @classmethod
    def _get_service(cls):
        if cls._service is None:
            transport = AsyncTransport(client=httpx.AsyncClient())
            client = AsyncClient(WSDL_URL, transport=transport, plugins=[HistoryPlugin()])
            cls._service = client.bind("GTICargaFactura", "GTICargaFacturaSoap12")
        return cls._service

    async def subir_factura(self, xml_facture):
        entorno = obtener_entorno()
        usuario = entorno.USUARIO_GTI.get_secret_value()
        clave = entorno.CONTRASENA_GTI.get_secret_value()

        service = self._get_service()

        response = await service.InsertarDocumentos(
            pvcDocumentosXML=xml_facture,
            pvcCorreoUsuario=usuario,
            pvcClaveUsuario=clave
        )

        logger.debug("Respuesta de GTI: %s", response)
        return response

    async def obtener_documento(self):
        pass