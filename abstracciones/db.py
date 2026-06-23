from abc import ABC, abstractmethod
from typing import Callable, Awaitable
from pydantic import BaseModel

class Documento(BaseModel):
    nombre: str
    id: str
    tabla: str
    obtener_contenido: Callable[[], Awaitable[str]]


class Db(ABC):
    @abstractmethod
    async def obtener_recientes(self, tabla: str, cantidad: int, ultimo_id: str | None) -> list[Documento]:
        pass

    @abstractmethod
    async def actualizar(self, tabla: str, id: str, contenido: str):
        pass

    @abstractmethod
    async def crear(self, tabla: str, id: str, contenido: str):
        pass

    @abstractmethod 
    async def borrar(self, tabla: str, id: str):
        pass