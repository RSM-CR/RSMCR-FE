from abc import ABC, abstractmethod
from typing import Any, Protocol

class CallbackNuevaFactura(Protocol):
    # Falta añadir el tipo de dato de factura pero aún no está
    def __call__(self, factura) -> Any:
        ...

class Fuente(ABC):
    def __init__(self):
        self.callbacks = []

    # Falta el tipo de dato del documento
    @abstractmethod
    def subir_documento(self, documento):
        pass

    @abstractmethod
    def escuchar_nueva_factura(self, funcion: CallbackNuevaFactura):
        self.callback = funcion

    # Falta añadir el tipo de dato de factura pero aún no está
    def notificar_nueva_factura(self, factura):
        for callback in self.callbacks:
            callback(factura)