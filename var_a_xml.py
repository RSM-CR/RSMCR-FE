import xml.etree.ElementTree as ET
from factura import DatosXero

#cargar los datos
lista_facturas = DatosXero.obtener_datos("prueba.json")

if len(lista_facturas) > 0: #esto hace que el bloque de código se ejecute si hay cierta cantidad de elementos específica

    variables = lista_facturas[0]  #hace que en la lista se cuente desde el primer objeto, el 0
    
    python = ["nombre", "cedula", "correo", "telefono", "provincia", "canton", "distrito", "otras_senas", "codigo", "cantidad", "descripcion", "precio", "total"] #la lista de lo que se extrae de las variables de Datos Xero

    root = ET.Element("traducido") #le da el nombre a la sección donde van a estar los datos
    for varpy in python: #el for hace que se repita paso por paso hasta tener todos los objetos requeridos
        valor = getattr(variables, varpy, None) #se asegura de obtener todo

        if valor is not None: #verifica que se encuentre la información
            sub_elemento = ET.SubElement(root, varpy) #se crea la etiqueta del xml
            sub_elemento.text = str(valor) #mete la información y convierte la variable en un texto plano que es lo que xml puede leer

    tree = ET.ElementTree(root) #toma la estructura de etiquetas creada y las guarda para guardarlas en un archivo real.
    ET.indent(tree, space="   ") #le da el formato estético al XML aplicando los saltos de línea y 3 esácios de sangría a cada etiqueta
    tree.write("factura.xml", encoding="utf-8", xml_declaration=True) #crea y escribe el archivo xml definitivo