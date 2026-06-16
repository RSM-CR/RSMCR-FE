"""
Capa.py era un boceto para la traducción de json a objetos de python, pero ahora se usa una función de factura.py
> [!CAUTION]
> Los datos del json de Xero no incluyen toda la información disponible en el .xml de GTI.
```{deprecated} v0.1
Este módulo está en desuso y puede ser eliminado en versiones futuras. Usa el módulo [factura](factura) en su lugar.
```"""
import json


class App:
    """Esta clase pertenece a todo el código de Capa.py, se metió dentro de una clase para poder manejarlo mejor y transmitirlo a otros archvos."""

    import json 


    def __init__(self, archivo_json="PruebaXero.json"):

        with open(archivo_json, "r", encoding="utf-8") as archivo:
            self.data = json.load(archivo)
        

        self.nombre = None
        """Guarda el nombre del cliente"""
        self.numero = None
        """Guarda el número de la factura"""
        self.correo = None
        """Guarda el correo del cliente"""
        self.telefono = None
        """Guarda el teléfono del cliente"""
        self.provincia = None
        """Guarda la provincia del cliente"""
        self.canton = None
        """Guarda el cantón del cliente"""
        self.distrito = None
        """Guarda el distrito del cliente"""
        self.otras_senas = None
        """Guarda una descripción de la factura"""
        self.detalle_servicio = []

        """Reorganiza los datos recibidos del json para crealos como una lista, y así administrar mejor los objetos.
        > [!NOTE]
        > Los datos se que se le asignan a las variables vienen de PruebaXero.json, que es un archivo de ejemplo.
        """
        

    def obtener_encabezado(self):
        """Obtiene el encabezado de la factura desde el JSON."""
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
        """Obtiene los detalles del servicio de la factura desde el JSON.
        """
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
        """Función para mostrar en la terminal la información obtenida del JSON, organizada en encabezado y detalle.
        Se trabaja junto con [la clase muestra](Capa.muestra).
        """

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

class muestra:
    """Esta clase se usa normalmente para ejectutar [mostrar_informacion](mostrar_informacion()) y así mostrar en terminal los resultados agarrados del JSON (solo para pruebas)."""
    if __name__ == "__main__":
        factura = App() #If para mostrar en termianl los resultados agarrados del JSON (solo para pruebas).
        factura.mostrar_informacion()
