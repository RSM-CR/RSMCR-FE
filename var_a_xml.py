import xml.etree.ElementTree as ET
from factura import DatosXero
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2


endpoint = FastAPI()

#Aquí llegan los datos que vienen del forms en Svelte

class Svelte (BaseModel):
    #IVA

    tipo_iva: str = ""
    tarifa_iva: str = ""
    porcentaje_iva: str = ""
    monto_iva: str = ""

    #resto de cosas

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

    #exoneración

    motivo_exoneracion: str = ""
    num_doc_exo: str = ""
    institucion: str = ""
    fecha_exo: str = ""
    porcentaje_exo: str = ""
    monto_exonerado: str = ""

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

        #impuestos

        if campos.tipo_iva:

            impuestos = ET.SubElement(linea, "Impuestos")
            impuesto = ET.SubElement(impuestos, "Impuesto")

            ET.SubElement(impuesto, "CodigoImpuesto").text = campos.tipo_iva
            ET.SubElement(impuesto, "CodigoTarifa").text = campos.tarifa_iva
            ET.SubElement(impuesto, "PorcentajeImpuesto").text = campos.porcentaje_iva
            ET.SubElement(impuesto, "MontoImpuesto").text = campos.monto_iva

        #Exoneración

        if campos.motivo_exoneracion:

            exoneracion = ET.SubElement(impuesto, "Exoneracion")
            ET.SubElement(exoneracion, "TipoDocumento").text = campos.motivo_exoneracion
            ET.SubElement(exoneracion, "NumeroDocumento").text = campos.num_doc_exo
            ET.SubElement(exoneracion, "NombreInstitucion").text = campos.institucion
            ET.SubElement(exoneracion, "FechaEmision").text = campos.fecha_exo
            ET.SubElement(exoneracion, "PorcentajeExoneracion").text = campos.porcentaje_exo
            ET.SubElement(exoneracion, "MontoExoneracion").text = campos.monto_exonerado

        #XML

        tree = ET.ElementTree(root)
        ET.indent(tree, space = "    ")
        tree.write("factura.xml", encoding="utf-8", xml_declaration=True)

        xml_string = ET.tostring(root,encoding="unicode")
        conn = psycopg2.connect(
            host = "localhost",
            database= "Holi",
            user= "gxbridge",
            password = ""
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO facturas (xml) VALUES (%s)", (xml_string,))
        conn.commit()
        cursor.close()
        conn.close()

        return {"ok": True, "mensaje": "XML generado y guardado correctamente"}
