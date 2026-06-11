import xml.etree.ElementTree as ET


class Factura:
    def __init__(self, archivo_xml = "Prueba.xml"):
        self.tree = ET.parse(archivo_xml)
        self.root = self.tree.getroot()

        self.encabezado = {}
        self.detalle_servicio = []

    def obtener_encabezado(self):
        receptor = self.root.find(".//{*}Receptor")  # buscar en todo el documento

        if receptor is None:
            return {}

        encabezado = {
            "Nombre": receptor.findtext(".//{*}Nombre"),
            "Numero": receptor.findtext(".//{*}Numero"),
            "CorreoElectronico": receptor.findtext(".//{*}CorreoElectronico"),
            "NumTelefono": receptor.findtext(".//{*}NumTelefono"),
            "Provincia": receptor.findtext(".//{*}Provincia"),
            "Canton": receptor.findtext(".//{*}Canton"),
            "Distrito": receptor.findtext(".//{*}Distrito"),
            "OtrasSenas": receptor.findtext(".//{*}OtrasSenas"),
        }

        self.encabezado = encabezado
        return self.encabezado

    def obtener_detalle_servicio(self):
        self.detalle_servicio = []
        for prod in self.root.findall(".//{*}LineaDetalle"):
            item = {
                "Codigo": prod.findtext(".//{*}Codigo"),
                "Cantidad": prod.findtext(".//{*}Cantidad"),
                "UnidadMedida": prod.findtext(".//{*}UnidadMedida"),
                "Detalle": prod.findtext(".//{*}Detalle"),
                "PrecioUnitario": prod.findtext(".//{*}PrecioUnitario"),
                "MontoTotal": prod.findtext(".//{*}MontoTotal"),
            }
            if any(item.values()):
                self.detalle_servicio.append(item)

        return self.detalle_servicio

    def mostrar_informacion(self):
        return {
            "Encabezado": self.obtener_encabezado(),
            "DetalleServicio": self.obtener_detalle_servicio(),
        }
if __name__ == "__main__":
    factura = Factura()
    info = factura.mostrar_informacion()
    print(info)