import asyncio

from Abstracciones.Destino import Destino as ds # Importar la clase Destino (ds) desde el módulo Abstracciones.Destino
from zeep import AsyncClient # Importar la clase AsyncClient de la biblioteca zeep para manejar solicitudes SOAP asíncronas
from zeep.transports import AsyncTransport # Importar la clase AsyncTransport de la biblioteca zeep para configurar el transporte asíncrono con httpx
from zeep.plugins import HistoryPlugin # Importar la clase HistoryPlugin de la biblioteca zeep para registrar las solicitudes y respuestas SOAP
import httpx # Importar la biblioteca httpx para manejar conexiones HTTP asíncronas
from servidor.secretos import obtener_entorno # Importar la biblioteca os para acceder a las variables de entorno

class gti (ds):

    # Permite que _subir_factura sea compatible con Destino (ds)
    # Aunque probablemente deberíamos decidir si hacer todo full async
    # en vez de hacer estas cosas...
    def subir_factura(self, factura):
        asyncio.run(self._subir_factura(factura))

    # El método subir_factura toma como argumento un string xml_facture que representa la factura electrónica en formato XML.
    async def _subir_factura(self, xml_facture):
        entorno = obtener_entorno()
        
        # Construir el XML que se enviará al servicio SOAP, incluyendo la factura electrónica dentro de una etiqueta CDATA, el CDATA se utiliza para incluir datos que podrían contener caracteres especiales sin que sean interpretados como parte del XML. El XML se estructura dentro de una etiqueta <Documentos> que contiene una etiqueta <FacturaElectronicaXML> con el contenido de la factura electrónica.
        xml_documents = f"""
        <Documentos>
            <FacturaElectronicaXML><![CDATA[
                {xml_facture}
            ]]></FacturaElectronicaXML>
        </Documentos>
        """

        # Obtener las credenciales de usuario y contraseña desde las variables de entorno
        usuario = entorno.USUARIO_GTI # Obtener el correo del usuario para autenticarse con el servicio de GTI desde la variable de entorno GTI_USER
        clave = entorno.CONTRASENA_GTI # Obtener la clave del usuario para autenticarse con el servicio de GTI desde la variable de entorno GTI_PASSWORD

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

        # print(client.service.InsertarDocumentos)
        # client.wsdl.dump()

        print("Respuesta: ", repr(response))
        return response

    async def obtener_documento(self):
        pass

