import xml.etree.ElementTree as ET

tree = ET.parse("Prueba.xml") #Aquí agarra el xml brindado y la información
root = tree.getroot()

#encabezado

receptor = root.find(".//{*}Receptor") #el .// es para buscar en todo el documento, no solo en el primer nivel, y Receptor es la etiqueta que quiero encontrar

Encabezado = {} #creo un diccionario para guardar la información del encabezado


if receptor is not None: #si el receptor existe, entonces guardo su información
    Encabezado = {
    "Nombre": receptor.findtext(".//{*}Nombre"),
    "Numero": receptor.findtext(".//{*}Numero"),
    "CorreoElectronico": receptor.findtext(".//{*}CorreoElectronico"),
    "NumTelefono": receptor.findtext(".//{*}NumTelefono"),
    "Provincia": receptor.findtext(".//{*}Provincia"),
    "Canton": receptor.findtext(".//{*}Canton"),
    "Distrito": receptor.findtext(".//{*}Distrito"),
    "OtrasSenas": receptor.findtext(".//{*}OtrasSenas")
    }


#detalles

DetalleServicio = []

for prod in root.findall(".//{*}LineaDetalle"):
    item = {
        "Codigo": prod.findtext(".//{*}Codigo"),
        "Cantidad": prod.findtext(".//{*}Cantidad"),
        "PrecioUnitario": prod.findtext(".//{*}PrecioUnitario"),
        "Detalle": prod.findtext(".//{*}Detalle")
    }
    
    if any(item.values()):
        DetalleServicio.append(item)

#Resultado
data = {
    "Encabezado": Encabezado,
    "DetalleServicio": DetalleServicio
}

print(data)
