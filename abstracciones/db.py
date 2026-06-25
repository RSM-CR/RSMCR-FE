"""Abstracción que le permite a GXBridge interactuar con cualquier base de datos con
una implementación apropiada."""
from abc import ABC, abstractmethod
from typing import Callable, Awaitable
from pydantic import BaseModel

class Documento(BaseModel):
    nombre: str
    id: str
    tabla: str
    obtener_contenido: Callable[[], Awaitable[str]]
    """Función asincrónica que permite obtener los datos almacenados dentro del documento, archivo o registro."""


class Db(ABC):
    @abstractmethod
    async def obtener_recientes(self, tabla: str, cantidad: int, ultimo_id: str | None) -> list[Documento]:
        """Obtiene los archivos más recientes según el parámetro **cantidad**.
        
        :param str tabla: La tabla o el directorio del que se quieren obtener los documentos más recientes.
        :param int cantidad: La cantidad de elementos que se van a retornar.
        :param str | None ultimo_id: Especifíca un ID de documento para obtener su fecha de creación. Todos los documentos creados
        después de este serán ignorados. El propósito de este parámetro es facilitar la paginación de datos.
        :returns: Una lista con **cantidad** [`Documentos`](db.Documento)."""
        pass

    @abstractmethod
    async def actualizar(self, tabla: str, id: str, contenido: str):
        """Sobrescribe por completo el documento especificado con lo que se especifica en **contenido**.
        
        :param str tabla: La tabla o el directorio del que se quieren obtener los documentos más recientes.
        :param str id: El identificador único del documento, archivo o registro que se quiere sobreescribir.
        :param str contenido: Lo que se escribirá en el archivo después de borrar los datos previos."""
        pass

    @abstractmethod
    async def crear(self, tabla: str, id: str, contenido: str):
        """Crea un archivo completamente nuevo.
        
        :param str tabla: La tabla o el directorio del que se quieren obtener los documentos más recientes.
        :param str id: El nuevo identificador único del documento, archivo o registro que se quiere crear.
        :param str contenido: Lo que se escribirá en el nuevo archivo."""
        pass

    @abstractmethod 
    async def borrar(self, tabla: str, id: str):
        """Borra el archivo especificado.
        
        :param str tabla: La tabla o el directorio donde reside el documento que se quiere borrar.
        :param str id: El identificador único del documento, archivo o registro que se va a borrar."""
        pass