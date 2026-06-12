from gti_implementation.destination import destination as ds
from zeep import AsyncClient
from zeep.transports import AsyncTransport
import httpx
from dotenv import load_dotenv
import os

class gti (ds):
        
    async def upload_facture(self):

        with open("Prueba.xml", "r", encoding="utf-8") as f:
            xml_factura = f.read()

        load_dotenv()

        documentos_xml = f"""
        <Documentos>
            <FacturaElectronicaXML><![CDATA[
        {xml_factura}
            ]]></FacturaElectronicaXML>
        </Documentos>
        """
        usuario = os.getenv("GTI_USER")
        clave = os.getenv("GTI_PASSWORD")

        transport = AsyncTransport(client=httpx.AsyncClient())
        client = AsyncClient(
            "https://pruebas.gticr.com/AplicacionFEPruebas/WSCargaFactura/Pruebas/GTICargaFactura.asmx?WSDL",
            transport=transport
        )

        response = await client.service.InsertarFacturaPagada(
            pvcDocumentosXML=xml_factura,
            pvcCorreoUsuario=usuario,
            pvcClaveUsuario=clave
        )
        print(client.service.InsertarFacturaPagada)
        client.wsdl.dump()
        print(xml_factura[:10000000000])
        print("Respuesta: ", response)