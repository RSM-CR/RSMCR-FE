from gti_implementation.destination import destination as ds
from zeep import AsyncClient
from zeep.transports import AsyncTransport
from zeep.plugins import HistoryPlugin
from lxml import etree
import httpx
from dotenv import load_dotenv
import os

class gti (ds):
        
    async def upload_facture(self):

        with open("Prueba.xml", "r", encoding="utf-8") as f:
            xml_facture = f.read()

        load_dotenv()

        xml_documents = f"""
        <Documentos>
            <FacturaElectronicaXML><![CDATA[
        {xml_facture}
            ]]></FacturaElectronicaXML>
        </Documentos>
        """
        usuario = os.getenv("GTI_USER")
        clave = os.getenv("GTI_PASSWORD")

        history = HistoryPlugin()

        transport = AsyncTransport(client=httpx.AsyncClient())
        client = AsyncClient(
            "https://pruebas.gticr.com/AplicacionFEPruebas/WSCargaFactura/Pruebas/GTICargaFactura.asmx?WSDL",
            transport=transport,
            plugins=[history]
        )

        service = client.bind(
            "GTICargaFactura",
            "GTICargaFacturaSoap12"
        )

        response = await service.InsertarDocumentos(
            pvcDocumentosXML=xml_documents,
            pvcCorreoUsuario=usuario,
            pvcClaveUsuario=clave
        )

        print("\n SOAP ENVIADO")
        print(
            etree.tostring(
                history.last_sent["envelope"],
                pretty_print = True,
                encoding = "unicode"
            )
        )

        print("\n SOAP RECIBIDO")
        print(
            etree.tostring(
                history.last_received["envelope"],
                pretty_print = True,
                encoding = "unicode"
            )
        )

        print(client.service.InsertarDocumentos)
        client.wsdl.dump()

        print("Respuesta: ", repr(response))