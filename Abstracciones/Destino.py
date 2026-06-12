from abc import ABC, abstractmethod

class Destino(ABC):
    def __init__(self) -> None:
        pass

    # Falta el tipo de dato de factura
    @abstractmethod
    def subir_factura(self, factura):
        pass

    @abstractmethod
    def obtener_documento(self):
        pass