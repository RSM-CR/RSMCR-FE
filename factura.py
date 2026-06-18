import json

class Factura:
    """[class Factura](factura.Factura) lo que hace es almacenar los datos de la factura de forma temporal, para poderlos manejar mejor y de una forma más segura."""
    def __init__(self):
        self.nombre = None
        self.cedula = None
        self.correo = None
        self.telefono = None
        self.provincia = None
        self.canton = None
        self.distrito = None
        self.otras_senas = None
        self.codigo = None
        self.cantidad = None
        self.descripcion = None
        self.precio = None
        self.impuesto = None
        self.total = None


    


class DatosXero:
    """ Se extraen los datos de Xero."""
    @staticmethod
    def obtener_datos(archivo_json: str) -> list[Factura]:
        """Esto hace que mientras exista el json se pueda leer y codificar la información para convertirla luego a una variable."""
        with open("prueba.json", "r", encoding="utf-8") as archivo_json:
            data = json.load(archivo_json)
        facturas = []            
        for invoice in data["Invoices"]:
            factura = Factura()

        with open(archivo_json, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

        facturas = []

        for invoice in data.get("Invoices", []):

            contacto = invoice.get("Contact", {})

            # Buscar dirección STREET
            direccion = {}
            for addr in contacto.get("Addresses", []):
                if addr.get("AddressType") == "STREET":
                    direccion = addr
                    break

            # Buscar teléfono DEFAULT
            telefono = {}
            for tel in contacto.get("Phones", []):
                if tel.get("PhoneType") == "DEFAULT":
                    telefono = tel
                    break

            # Recorrer todas las líneas de la factura
            for linea in invoice.get("LineItems", []):

                factura = Factura()

                factura.nombre = contacto.get("Name")
                factura.cedula = contacto.get("LegalID")
                factura.correo = contacto.get("EmailAddress")
                factura.telefono = telefono.get("PhoneNumber")

                factura.provincia = direccion.get("Province")
                factura.canton = direccion.get("Canton")
                factura.distrito = direccion.get("District")
                factura.otras_senas = direccion.get("OtherAddressDetails")

                factura.codigo = linea.get("ItemCode")
                factura.cantidad = linea.get("Quantity")
                factura.descripcion = linea.get("Description")
                factura.precio = linea.get("UnitAmount")
                factura.impuesto = linea.get("TaxAmount")

                factura.total = invoice.get("Total")

                facturas.append(factura)

        return facturas
