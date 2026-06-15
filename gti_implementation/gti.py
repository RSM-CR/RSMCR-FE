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

        def xml_cleanup():
            with open("Prueba.xml", "rb") as f:
                xml_facture = f.read()

            root = etree.fromstring(xml_facture)

            for element in root.iter():
                if isinstance(element.tag, str) and element.tag.startswith("{"):
                    element.tag = etree.QName(element).localname

            etree.cleanup_namespaces(root)
            return root

        # xml_documents = f"""
        # <Documentos>
        #     <FacturaElectronicaXML>
        #         {root}
        #     </FacturaElectronicaXML>
        # </Documentos>
        # """

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

        def build_envelop():
            root = xml_cleanup()

            envelope = etree.Element(f"{{{SOAP_NS}}}Envelope", nsmap={"soap": SOAP_NS})
            body = etree.SubElement(envelope, f"{{{SOAP_NS}}}Body")
            operation = etree.SubElement(body, f"{{{SERVICE_NS}}}InsertarDocumentos")
            field1 = etree.SubElement(operation, f"{{{SERVICE_NS}}}pvcDocumentosXML")
            Documentos = etree.SubElement(field1, f"{{{SERVICE_NS}}}Documentos")
            FacturaElectronicaXML = etree.SubElement(Documentos, f"{{{SERVICE_NS}}}FacturaElectronicaXML")
            FacturaElectronicaXML.append(root)
            field2 = etree.SubElement(operation, f"{{{SERVICE_NS}}}pvcCorreoUsuario")
            field2.text = usuario
            field3 = etree.SubElement(operation, f"{{{SERVICE_NS}}}pvcClaveUsuario")
            field3.text = clave
            
            return etree.tostring(envelope, xml_declaration=True, encoding="utf-8")
        
        async def send_xml():
            soap = build_envelop()

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    SEND_ASMX,
                    content=soap,
                    headers={
                        "Content-Type": "text/xml; charset=utf-8",
                        "SOAPAction": SOAP_ACTION
                    }
                )

                print("STATUS:", response.status_code)
                print("HEADERS:", response.headers)
                print("BODY:", response.text)

                response.raise_for_status()

#         # service = client.bind(
#         # "GTICargaFactura",
#         # "GTICargaFacturaSoap12"
# )

        # response = await client.service.InsertarDocumentos(
        #     pvcDocumentosXML=xml_documents,
        #     pvcCorreoUsuario=usuario,
        #     pvcClaveUsuario=clave
        # )

        # print("\n SOAP ENVIADO")
        # print(
        #     etree.tostring(
        #         history.last_sent["envelope"],
        #         pretty_print = True,
        #         encoding = "unicode"
        #     )
        # )

        # print("\n SOAP RECIBIDO")
        # print(
        #     etree.tostring(
        #         history.last_received["envelope"],
        #         pretty_print = True,
        #         encoding = "unicode"
        #     )
        # )

        soap = build_envelop()

        print(
            etree.tostring(
                etree.fromstring(soap),
                pretty_print=True,
                encoding="unicode"
            )
        )

        print(client.service.InsertarDocumentos)
        client.wsdl.dump()

        print("Respuesta: ", repr(response))