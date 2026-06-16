"""Capa.py era un boceto para la traducción de json a objetos de python, pero ahora se usa una función de factura.py"""
import json


class App:
    import json 


    def __init__(self, archivo_json="PruebaXero.json"):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            self.data = json.load(archivo)

        self.nombre = None
        self.numero = None
        self.correo = None
        self.telefono = None
        self.provincia = None
        self.canton = None
        self.distrito = None
        self.otras_senas = None
        self.detalle_servicio = []
        """Reorganiza los datos recibidos del json para crealos como una lista, y así administrar mejor los objetos.
        """

    def obtener_encabezado(self):
        """Obtiene el encabezado de la factura desde el JSON por medio de la búsqueda del elemento dentro del json."""
        factura = self.data.get("Invoice", {})

        self.nombre = factura.get("Name")
        self.numero = factura.get("Numero")
        self.correo = factura.get("EmailAddress")
        self.telefono = factura.get("Phone")
        self.provincia = factura.get("Province")
        self.canton = factura.get("Canton")
        self.distrito = factura.get("Distrito")
        self.otras_senas = factura.get("Reference")
        self.moneda = factura.get("CurrencyCode")

    def obtener_detalle_servicio(self):
        """Obtiene el encabezado de la factura desde el JSON por medio de la búsqueda del elemento dentro del json. Por el momento, los datos del json de Xero están incompletos con respecto a los datos que otorga el .xml de GTI."""
        self.detalle_servicio = []

        line_items = self.data.get("Invoice", {}).get("LineItems", [])

        for prod in line_items:

            linea = type("LineItem", (), {})()

            linea.account_code = prod.get("AccountCode")
            linea.quantity = prod.get("Quantity")
            linea.description = prod.get("Description")
            linea.unit_amount = prod.get("UnitAmount")
            linea.line_amount = prod.get("LineAmount")

            self.detalle_servicio.append(linea)

    def mostrar_informacion(self):

        self.obtener_encabezado()
        self.obtener_detalle_servicio()

        print("----- ENCABEZADO -----")
        print("Nombre:", self.nombre)
        print("Número:", self.numero)
        print("Correo:", self.correo)
        print("Teléfono:", self.telefono)
        print("Provincia:", self.provincia)
        print("Cantón:", self.canton)
        print("Distrito:", self.distrito)
        print("Otras Señas:", self.otras_senas)
        print("Moneda:", self.moneda)

        print("\n----- DETALLE -----")
        for linea in self.detalle_servicio:
            print("Código:", linea.account_code)
            print("Cantidad:", linea.quantity)
            print("Detalle:", linea.description)
            print("Precio Unitario:", linea.unit_amount)
            print("Total:", linea.line_amount)
            print("-------------------")
    """Se usa para poder llamar mejor este código a otros archivos, viene todo lo relacionado a las traducciones de json a variables de Python (objetos)."""

class muestra:
    if __name__ == "__main__":
        factura = App() #If para mostrar en termianl los resultados agarrados del JSON (solo para pruebas).
        factura.mostrar_informacion()


