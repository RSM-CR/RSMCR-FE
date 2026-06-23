from abc import ABC, abstractmethod

class Db(ABC):
    @abstractmethod
    async def obtener_documentos_recientes(self, cantidad: int, ultimo_id: str | None) -> tuple[list[dict], str]:
        pass

    @abstractmethod
    async def actualizar_documento(self, documento: dict, id: str):
        pass

    @abstractmethod
    async def crear_documento(self, documento: dict) -> str:
        pass

    @abstractmethod 
    async def borrar_documento(self, id: str):
        pass