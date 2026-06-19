import xml.etree.ElementTree as ET
from factura import DatosXero


lista_facturas = DatosXero.obtener_datos()
"""Carga los datos de Xero convertidos en variables y los transforma en un xml para poder ser leídos por GTI."""

if not lista_facturas:
    raise Exception ("No se encontró ninguna factura") #si no hay datos no se va a generar el XML

info = lista_facturas [0]

root = ET.Element("Documentos")
factura_xml = ET.SubElement (root, "FacturaElectrónicaXML")

encabezado = ET.SubElement(factura_xml, "Encabezado")

#Los datos que no los proporciona Xero serán añadidos de manera manual en el front end
#Eso incluye los métodos de pago, el tipo de documento, la condición de venta, sucursal, terminal, moneda, situación envío, y tipo de identificación del receptor y los datos del emisor

receptor = ET.SubElement(encabezado, "Receptor") #datos del receptor
ET.SubElement(receptor, "NombreReceptor").text = info.nombre
ET.SubElement(receptor, "CorreoElectronicoReceptor").text = info.correo
ET.SubElement(receptor, "IdentificaciónReceptor").text = info.cedula

detalle = ET.SubElement(factura_xml, "Detalle")

for item in lista_facturas:
    linea = ET.SubElement(detalle, "Linea")
    
    ET.SubElement (linea, "Cantidad").text = str(item.cantidad)

    #lo mismo sucede con la unidad de medida

    ET.SubElement(linea, "DetalleMerc").text = item.descripcion
    ET.SubElement(linea, "PrecioUnitario").text = str(item.precio)
    
    montototal=float(item.cantidad) * float(item.precio)
    
    ET.SubElement(linea, "MontoTotal").text = f"{montototal:.2f}"
    ET.SubElement(linea, "SubTotal").text = f"{montototal:.2f}"
    ET.SubElement(linea,"Codigo").text = item.codigo

    #impuestos se ven después con Don Carlos el lunes

    #los totales no van a estar completos hasta el lunes.

total_venta = sum (
        float(x.cantidad) * float(x.precio)
        for x in lista_facturas
        )
    
# total_impuesto = sum (
    # float(x.impuesto)
    #for x in lista_facturas
    #)

totales = ET.SubElement( factura_xml, "Totales")

ET.SubElement( totales, "TotalVenta").text = f"{total_venta:.2f}"
#ET.SubElement(totales, "TotalImpuesto").text = f"{total_impuesto:.2f}
#ET.SubElement(totales, "TotalComprobante").text = f"{total_venta + total_impuesto:.2f}"

extra = ET.SubElement(factura_xml, "Extra")

#ET.SubElement(extra, "EsVersion4_4").text = "true"

tree = ET.ElementTree(root)
ET.indent(tree, space="    ")

tree.write(
    "factura.xml", encoding="utf-8", xml_declaration=True
)