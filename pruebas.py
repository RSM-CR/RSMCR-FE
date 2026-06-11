import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import Callable

CallbackNuevaFactura = Callable[["Factura"], None]


class Factura:
    def __init__(self, archivo_xml="Prueba.xml"):
        self.tree = ET.parse(archivo_xml)
        self.root = self.tree.getroot()

        self.encabezado = {}
        self.detalle_servicio = []

    def obtener_encabezado(self):
        receptor = self.root.find(".//{*}Receptor")

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
        encabezado = self.obtener_encabezado()
        detalle = self.obtener_detalle_servicio()

        print("Encabezado\n")

        print(f"Nombre del cliente: {encabezado.get('Nombre')}")
        print(f"Cédula Jurídica: {encabezado.get('Numero')}")
        print(f"Correo electrónico al que se va a enviar la factura: {encabezado.get('CorreoElectronico')}")
        print(f"Teléfono: {encabezado.get('NumTelefono')}")
        print(f"Provincia: {encabezado.get('Provincia')}")
        print(f"Canton: {encabezado.get('Canton')}")
        print(f"Distrito: {encabezado.get('Distrito')}")
        print(f"Otras Señas: {encabezado.get('OtrasSenas')}")

        print("\nDetalle de la factura\n")

        if not detalle:
            print("No hay datos")
        else:
            for i, item in enumerate(detalle, 1):
                print(f" Línea: {i}")
                print(f"Código: {item.get('Codigo')}")
                print(f"Cantidad: {item.get('Cantidad')}")
                print(f"Precio: {item.get('PrecioUnitario')}")
                print(f"Descripción: {item.get('Detalle')}")
                print(f"Monto Total: {item.get('MontoTotal')}")
                print()


class Fuente(ABC):
    def __init__(self):
        self.callbacks = []

    @abstractmethod
    def subir_documento(self, documento):
        pass

    def escuchar_nueva_factura(self, funcion: CallbackNuevaFactura):
        self.callbacks.append(funcion)

    def notificar_nueva_factura(self, factura):
        contador = 0
        for callback in self.callbacks:
            callback(factura)
            contador += 1

        print(f"Se agregó {contador} factura")


class FuenteXML(Fuente):
    def subir_documento(self, documento):
        factura = Factura(documento)
        self.notificar_nueva_factura(factura)


def procesar_factura(factura):
    factura.mostrar_informacion()


if __name__ == "__main__":
    fuente = FuenteXML()
    fuente.escuchar_nueva_factura(procesar_factura)
    fuente.subir_documento("Prueba.xml")