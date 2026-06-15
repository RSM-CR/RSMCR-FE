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
        load_dotenv()

        with open("Prueba.xml", "r") as f:
            xml_facture = f.read()

        xml_documents = f"""
        <Documentos>
            <FacturaElectronicaXML><![CDATA[
                {xml_facture}
            ]]></FacturaElectronicaXML>
        </Documentos>
        """

        usuario = os.getenv("GTI_USER")
        clave = os.getenv("GTI_PASSWORD")

        SOAP_NS = "http://schemas.xmlsoap.org/soap/envelope/"
        SERVICE_NS = "https://www.facturaelectronica.cr"
        SOAP_ACTION = "https://www.facturaelectronica.cr/InsertarDocumentos"
        SEND_ASMX = "https://pruebas.gticr.com/AplicacionFEPruebas/WSCargaFactura/Pruebas/GTICargaFactura.asmx"
        WDSL_NS = "https://pruebas.gticr.com/AplicacionFEPruebas/WSCargaFactura/Pruebas/GTICargaFactura.asmx?WSDL"

        history = HistoryPlugin()

        transport = AsyncTransport(client=httpx.AsyncClient())
        client = AsyncClient(
            WDSL_NS ,
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