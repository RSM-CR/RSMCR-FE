from Abstracciones.Destino import Destino as ds # Importar la clase Destino (ds) desde el módulo Abstracciones.Destino
from lxml import etree # Importar la biblioteca lxml para manejar XML
from zeep import AsyncClient # Importar la clase AsyncClient de la biblioteca zeep para manejar solicitudes SOAP asíncronas
from zeep.transports import AsyncTransport # Importar la clase AsyncTransport de la biblioteca zeep para configurar el transporte asíncrono con httpx
from zeep.plugins import HistoryPlugin # Importar la clase HistoryPlugin de la biblioteca zeep para registrar las solicitudes y respuestas SOAP
import httpx # Importar la biblioteca httpx para manejar conexiones HTTP asíncronas
from dotenv import load_dotenv # Importar la función load_dotenv de la biblioteca dotenv para cargar las variables de entorno desde un archivo .env
import os # Importar la biblioteca os para acceder a las variables de entorno

# Este código implementa una clase gti que hereda de una clase Destino (ds) y tiene un método subir_factura que se encarga de subir una factura electrónica en formato XML a través de un servicio SOAP proporcionado por GTI. El método utiliza la biblioteca zeep para manejar las solicitudes SOAP y httpx para las conexiones HTTP asíncronas. Además, se utilizan variables de entorno para almacenar las credenciales de usuario y contraseña necesarias para autenticarse con el servicio de GTI.
class gti (ds):
    # El método subir_factura toma como argumento un string xml_facture que representa la factura electrónica en formato XML.
    async def subir_factura(self, xml_facture):
        load_dotenv()
        
        # Construir el XML que se enviará al servicio SOAP, incluyendo la factura electrónica dentro de una etiqueta CDATA, el CDATA se utiliza para incluir datos que podrían contener caracteres especiales sin que sean interpretados como parte del XML. El XML se estructura dentro de una etiqueta <Documentos> que contiene una etiqueta <FacturaElectronicaXML> con el contenido de la factura electrónica.
        xml_documents = f"""
        <Documentos>
            <FacturaElectronicaXML><![CDATA[
                {xml_facture}
            ]]></FacturaElectronicaXML>
        </Documentos>
        """

        # Obtener las credenciales de usuario y contraseña desde las variables de entorno
        usuario = os.getenv("GTI_USER") # Obtener el correo del usuario para autenticarse con el servicio de GTI desde la variable de entorno GTI_USER
        clave = os.getenv("GTI_PASSWORD") # Obtener la clave del usuario para autenticarse con el servicio de GTI desde la variable de entorno GTI_PASSWORD

        # Definir las constantes necesarias para la conexión SOAP, incluyendo los namespaces, la acción SOAP, la URL del servicio y la URL del WSDL
        SOAP_NS = "http://schemas.xmlsoap.org/soap/envelope/" # Namespace para el envelope SOAP
        SERVICE_NS = "https://www.facturaelectronica.cr" # Namespace para el servicio SOAP de GTI
        SOAP_ACTION = "https://www.facturaelectronica.cr/InsertarDocumentos" # Acción SOAP para el método InsertarDocumentos del servicio de GTI
        SEND_ASMX = "https://pruebas.gticr.com/AplicacionFEPruebas/WSCargaFactura/Pruebas/GTICargaFactura.asmx" # URL del servicio SOAP de GTI para pruebas
        WDSL_NS = "https://pruebas.gticr.com/AplicacionFEPruebas/WSCargaFactura/Pruebas/GTICargaFactura.asmx?WSDL" # URL del WSDL del servicio SOAP de GTI para pruebas

        # Crear un cliente SOAP utilizando zeep y configurar el transporte asíncrono con httpx. También se utiliza el plugin HistoryPlugin para registrar las solicitudes y respuestas SOAP.
        history = HistoryPlugin() # Plugin para registrar las solicitudes y respuestas SOAP
        transport = AsyncTransport(client=httpx.AsyncClient()) # Configuración del transporte asíncrono con httpx
        client = AsyncClient( # Crear un cliente SOAP utilizando zeep
            WDSL_NS , # URL del WSDL del servicio SOAP
            transport=transport, # Configuración del transporte asíncrono con httpx
            plugins=[history] # Plugin para registrar las solicitudes y respuestas SOAP
        )

        # Se asocio el servicio SOAP con el cliente utilizando el método bind, especificando el nombre del servicio y el puerto.
        service = client.bind( # Asociar el servicio SOAP con el cliente
            "GTICargaFactura", # Nombre del servicio definido en el WSDL
            "GTICargaFacturaSoap12" # Nombre del puerto definido en el WSDL
        )


        # Se realiza la llamada al método InsertarDocumentos del servicio SOAP, pasando como argumentos el XML de la factura electrónica, el correo del usuario y la clave del usuario. La respuesta se imprime en la consola, junto con el XML de la solicitud y respuesta SOAP para fines de depuración.
        response = await service.InsertarDocumentos( # Llamada al método InsertarDocumentos del servicio SOAP
            pvcDocumentosXML=xml_documents, # XML de la factura electrónica en formato XML
            pvcCorreoUsuario=usuario, # Correo del usuario para autenticarse con el servicio de GTI
            pvcClaveUsuario=clave # Clave del usuario para autenticarse con el servicio de GTI
        )

        # Imprimir el XML de la solicitud y respuesta SOAP para fines de depuración
        print("\n SOAP ENVIADO")
        print(
            etree.tostring( # Imprimir el XML de la solicitud SOAP para fines de depuración
                history.last_sent["envelope"], # Acceder al último mensaje SOAP enviado registrado por el plugin HistoryPlugin
                pretty_print = True, # Formatear el XML para que sea más legible
                encoding = "unicode" # Especificar que la salida debe ser una cadena de texto en lugar de bytes
            )
        )

        print("\n SOAP RECIBIDO")
        print(
            etree.tostring( # Imprimir el XML de la respuesta SOAP para fines de depuración
                history.last_received["envelope"], # Acceder al último mensaje SOAP recibido registrado por el plugin HistoryPlugin
                pretty_print = True, # Formatear el XML para que sea más legible
                encoding = "unicode" # Especificar que la salida debe ser una cadena de texto en lugar de bytes
            )
        )

        # Imprimir la información del método InsertarDocumentos y el WSDL para fines de depuración
        print(client.service.InsertarDocumentos) # Imprimir la información del método InsertarDocumentos para fines de depuración
        client.wsdl.dump() # Imprimir la información del WSDL para fines de depuración

        print("Respuesta: ", repr(response)) # Imprimir la respuesta del método InsertarDocumentos para fines de depuración
        return response # Devolver la respuesta del método InsertarDocumentos

    async def obtener_documento(self):
        pass

