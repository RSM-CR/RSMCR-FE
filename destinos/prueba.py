from Abstracciones.Destino import Destino
from factura import Factura

class DestinoPrueba(Destino):
    def __init__(self) -> None:
        pass

    def subir_factura(self, factura: Factura):
        print("Se ha recibido una factura correctamente. A continuación, se muestra su contenido:")
        factura.mostrar_informacion()

    def obtener_documento(self):
        print("Porfa finge como si hubieras recibido un archivo PDF :3")
        print("De momento, obtener_documento() no tiene return porque faltan cositas para implementar eso")