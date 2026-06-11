from abc import ABC, abstractmethod

class Destino(ABC):
    """Representa el receptor de los datos generados por la [fuente](fuente.Fuente). Estos datos serán subidos al destino para que se sincronicen."""
    def __init__(self) -> None:
        pass

    # Falta el tipo de dato de factura
    @abstractmethod
    def subir_factura(self, factura):
        """Sube la factura a la plataforma relevante. En caso de GTI, primero se hará la conversión a XML.
        
        > [!CAUTION]
        > En caso de que ocurra cualquier error, se va a asumir que la fuente de verdad se encuentra en la [fuente](fuente.Fuente) que haya sido seleccionada. Esto puede causar que se sobreescriban datos en el destino para corregirlos."""
        pass

    @abstractmethod
    def obtener_documento(self):
        """Obtiene un documento para verificar el resultado de la factura subida. En caso de la conexión de GTI a Xero, esto se va a usar para subir un PDF como archivo adjunto."""
        pass