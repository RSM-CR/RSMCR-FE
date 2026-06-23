import xml.etree.ElementTree as ET
from abstracciones.fuente import Fuente, CallbackNuevaFactura
from factura import Factura
from typing import Callable

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
