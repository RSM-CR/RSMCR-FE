import xml.etree.ElementTree as ET


class Factura:
    def __init__(self, archivo_xml="PruebaXero.xml"):
        self.tree = ET.parse(archivo_xml)
        self.root = self.tree.getroot()
        self.nombre = None
        self.numero = None
        self.correo = None
        self.telefono = None
        self.provincia = None
        self.canton = None
        self.distrito = None
        self.otras_senas = None
        self.detalle_servicio = []

    def obtener_encabezado(self):
        receptor = self.root.find(".//{*}Invoice") #.// sirve para buscar todo en específicamente ese elemento

        if receptor is None:
            return

        self.name = receptor.findtext(".//{*}Name")
        self.numero = receptor.findtext(".//{*}Numero") # En Xero no hay un campo específico para el número de factura, por lo que se deja como None
        self.email = receptor.findtext(".//{*}EmailAddress")
        self.phone = receptor.findtext(".//{*}Phone") # En Xero no hay un campo específico para el teléfono del cliente, por lo que se deja como None
        self.province = receptor.findtext(".//{*}Province") # En Xero no hay un campo específico para la provincia del cliente, por lo que se deja como None
        self.canton = receptor.findtext(".//{*}Canton") # En Xero no hay un campo específico para el cantón del cliente, por lo que se deja como None
        self.distrito = receptor.findtext(".//{*}Distrito") # En Xero no hay un campo específico para el distrito del cliente, por lo que se deja como None
        self.reference = receptor.findtext(".//{*}Reference")
        self.currency_code = receptor.findtext(".//{*}CurrencyCode")

    def obtener_detalle_servicio(self):
        self.detalle_servicio = []

        for prod in self.root.findall(".//{*}LineItem"):


            linea = type("LineItem", (), {})()

            linea.account_code = prod.findtext(".//{*}AccountCode")
            linea.quantity = prod.findtext(".//{*}Quantity")
            linea.description = prod.findtext(".//{*}Description")
            linea.unit_amount = prod.findtext(".//{*}UnitAmount")
            linea.line_amount = prod.findtext(".//{*}LineAmount")

            self.detalle_servicio.append(linea)

    def mostrar_informacion(self):

        self.obtener_encabezado()
        self.obtener_detalle_servicio()

        print("----- ENCABEZADO -----")
        print("Nombre:", self.name)
        print("Numero:", self.numero)
        print("Correo:", self.email)
        print("Telefono:", self.phone)
        print("Provincia:", self.province)
        print("Canton:", self.canton)
        print("Distrito:", self.distrito)
        print("Otras Señas:", self.reference)
        print("Moneda:", self.currency_code)

        print("\n----- DETALLE -----")
        for linea in self.detalle_servicio:
            print("Codigo:", linea.account_code)
            print("Cantidad:", linea.quantity)
            print("Unidad:", linea.unit_amount)
            print("Detalle:", linea.description)
            print("Precio:", linea.unit_amount)
            print("Total:", linea.line_amount)
            print("-------------------")

if __name__ == "__main__":
    factura = Factura()
    factura.mostrar_informacion()