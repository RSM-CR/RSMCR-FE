import json

class Factura:
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

    @staticmethod
    def obtener_datos(archivo_json: str) -> list[Factura]:

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