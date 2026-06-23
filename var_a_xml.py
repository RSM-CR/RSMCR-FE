import xml.etree.ElementTree as ET
from factura import DatosXero
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2


endpoint = FastAPI()

#Aquí llegan los datos que vienen del forms en Svelte

class Svelte (BaseModel):

    metododepago: int = ""
    tipodoc: int = ""
    condicionventa: int = ""
    terminal: str = ""
    sucursal: str = ""
    moneda: int = ""
    situacionenvio: int = ""
    codigoactividad: int = ""
    tipoidreceptor: int = ""
    numcuentaemisor: int = ""
    unidadmedida: int = ""
    provincia: str = ""
    canton: str = ""
    distrito: str = ""
    otrassenas: str = ""
    numdoc: int = ""

@endpoint.post("/generarxml")

def generar_xml (campos: Svelte):

    lista_facturas = DatosXero.obtener_datos()
    if not lista_facturas:

        raise Exception ("No se encuentró ninguna factura. Intenta de nuevo")
    
    info = lista_facturas[0]

    root = ET.Element("Documentos")
    factura_xml = ET.SubElement (root, "FacturaElectrónicaXML")
    encabezado = ET.SubElement(factura_xml, "Encabezado")

    #Aquí van los datos obtenidos del formulario

    ET.SubElement(encabezado, "TipoDoc").text = campos.tipodoc
    ET.SubElement(encabezado, "NumDoc").text = campos.numdoc
    ET.SubElement(encabezado, "CondicionVenta").text = campos.condicionventa
    ET.SubElement(encabezado, "Sucursal").text = campos.sucursal
    ET.SubElement(encabezado, "Terminal").text = campos.terminal
    ET.SubElement(encabezado, "Moneda").text = campos.moneda
    ET.SubElement(encabezado, "SituacionEnvio").text = campos.situacionenvio
    ET.SubElement(encabezado, "CodigoActividad").text = campos.codigoactividad
    mediopagos= ET.SubElement(encabezado, "MediosPagos")
    ET.SubElement(mediopagos, "TipoMedioPago").text = campos.metododepago

    #Datos Receptor (Xero y Svelte)

    receptor = ET.SubElement(encabezado, "Receptor")
    ET.SubElement(receptor, "TipoIdentificacion").text = campos.tipoidreceptor
    ET.SubElement(receptor, "NombreReceptor").text = info.nombre
    ET.SubElement(receptor, "CorreoElectronicoReceptor").text = info.correo
    ET.SubElement(receptor, "IdentificacionReceptor").text = info.cedula

    #Emisor

    emisor = ET.SubElement(encabezado, "Emisor")
    ET.SubElement(emisor, "NumCuenta").text = campos.numcuentaemisor

    #Ubicación

    ubicacion = ET.SubElement(encabezado, "Ubicacion")
    ET.SubElement(ubicacion, "Provincia").text = campos.provincia
    ET.SubElement(ubicacion, "Canton").text = campos.canton
    ET.SubElement(ubicacion, "Distrito").text = campos.distrito
    ET.SubElement(ubicacion, "OtrasSenas").text = campos.otrassenas

    #Detalle

    detalle = ET.SubElement(factura_xml, "Detalle")
    for item in lista_facturas:
        linea = ET.SubElement(detalle, "Linea")
        ET.SubElement(linea, "Cantidad").text = str(item.cantidad)
        ET.SubElement(linea, "UnidadMedida").text = campos.unidadmedida
        ET.SubElement(linea, "DetalleMerc").text = item.descripcion
        ET.SubElement(linea, "PrecioUnitario").text = str(item.precio)

        montototal = float (item.cantidad) * float (item.precio)

        ET.SubElement(linea, "MontoTotal").text = f"{montototal:.2}"
        ET.SubElement(linea, "SubTotal").text = f"{montototal:.2}"
        ET.SubElement(linea, "Codigo").text = item.codigo

        #totales (Xero)

        total_venta = sum(float(x.cantidad) * float(x.precio) for x in lista_facturas)
        totales= ET.SubElement(factura_xml, "Totales")
        ET.SubElement(totales, "TotalVenta").text = f"{total_venta:.2f}"

        #aún faltan los impuestos, Matheus cuando termine póngalos aquí

        extra = ET.SubElement(factura_xml, "Extra")
        #ET.SubElement(extra, "EsVersion4_4").text = "true" esto aun no sé

        #XML

        tree = ET.ElementTree(root)
        ET.indent(tree, space = "    ")
        tree.write("factura.xml", encoding="utf-8", xml_declaration=True)
        