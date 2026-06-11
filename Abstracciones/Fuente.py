from abc import ABC, abstractmethod
from typing import Any, Protocol

class CallbackNuevaFactura(Protocol):
    # Falta añadir el tipo de dato de factura pero aún no está
    def __call__(self, factura) -> Any:
        ...

class Fuente(ABC):
    """Representa una fuente de datos que se usará para recibir las facturas. Un ejemplo de una fuente de datos es GTI."""
    def __init__(self) -> None:
        self.callbacks = []

    # Falta el tipo de dato del documento
    @abstractmethod
    def subir_documento(self, documento):
        """Se usa para devolver un documento a la plataforma usada como fuente.
        En el caso de Xero, esto se utiliza para devolver un PDF como archivo adjunto."""
        pass

    @abstractmethod
    def escuchar_nueva_factura(self, funcion: CallbackNuevaFactura) -> None:
        """Añade un callback que se ejecuta cada vez que se detecta una nueva factura.
        El formato de este callback es dictado por [CallbackNuevaFactura](fuente.CallbackNuevaFactura).
        
        :param CallbackNuevaFactura funcion: La función o método que se ejecutará cuando se detecta la creación de una nueva factura"""
        self.callback = funcion

    # Falta añadir el tipo de dato de factura pero aún no está
    def notificar_nueva_factura(self, factura):
        """Se encarga de llamar a todos los callbacks, pasándoles la factura que fue recibida.
        
        :param Factura factura: La factura que será enviada a los callbacks."""
        for callback in self.callbacks:
            callback(factura)