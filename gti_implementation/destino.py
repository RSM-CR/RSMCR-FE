from abc import ABC, abstractmethod

class Destino(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    async def subir_factura(self, facture):
        pass

    @abstractmethod
    async def obtener_documento(self, response):
        pass