import xml.etree.ElementTree as ET
from factura import DatosXero

#cargar los datos
lista_facturas = DatosXero.obtener_datos("prueba.json")

if len(lista_facturas) > 0:

    variables = lista_facturas[0] 
    
    python = ["tipo", "cliente", "estado", "moneda", "lineas"]

    root = ET.Element("traducido")
    for varpy in python:
        valor = getattr(variables, varpy, None)

        if valor is not None:
            sub_elemento = ET.SubElement(root, varpy)
            sub_elemento.text = str(valor)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="   ")
    tree.write("factura.xml", encoding="utf-8", xml_declaration=True)