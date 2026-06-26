"""Implementación de [`Db`](abstracciones.db.Db) que almacena archivos en una carpeta local.
Se recomienda leer [`Db`](abstracciones.db.Db) para conocer más detalles.

Conceptualmente, esta implementación trata a **tabla** como si fuese un directorio. Asimismo,
los parámetros de **id** y **ultimo_id** corresponden al nombre del archivo dentro del directorio."""
from abstracciones.db import Db, Documento
from pathlib import Path
from aiopath import AsyncPath
from os import stat_result
import heapq

class FileDb(Db):
    def __init__(self, carpeta: str ="./servidor/filedb") -> None:
        """:param str carpeta: La carpeta en donde se va a crear la base de datos. De aquí se extraen
        todos los archivos y datos. Por defecto, tiene un valor de `\"./servidor/filedb\"`"""
        carpeta_path = Path(carpeta)
        carpeta_path.mkdir(exist_ok = True)
        self.carpeta: AsyncPath =  AsyncPath(carpeta_path)

    async def obtener_recientes(self, tabla: str, cantidad: int, ultimo_id: str | None = None) -> list[Documento]:
        dir_tabla: AsyncPath = self.carpeta.joinpath(tabla)
        if ultimo_id is not None:
            ultimo_archivo: AsyncPath = dir_tabla.joinpath(ultimo_id)
            ultima_pareja = ((await ultimo_archivo.stat()).st_mtime_ns, ultimo_archivo.name, ultimo_archivo)
        else:
            ultima_pareja = None


        parejas = list[tuple[int, str, AsyncPath]]()
        async for archivo in dir_tabla.iterdir():
            stat: stat_result = await archivo.stat()
            pareja = (stat.st_mtime_ns, archivo.name, archivo)
            if not await archivo.is_file() or (ultima_pareja is not None and pareja >= ultima_pareja):
                continue

            parejas.append(pareja)

        archivos_recientes = heapq.nlargest(cantidad, parejas)

        archivos = []
        for _, nombre, archivo in archivos_recientes:
            datos = await archivo.stat()
            archivos.append(Documento(
                nombre=nombre,
                id=str(archivo.relative_to(self.carpeta)),
                tabla=str(archivo.parent),
                obtener_contenido=archivo.read_text
            ))
        return archivos


    async def actualizar(self, tabla: str, id: str, contenido: str):
        dir_tabla: AsyncPath = self.carpeta.joinpath(tabla)
        await dir_tabla.mkdir(exist_ok=True)
        archivo: AsyncPath = dir_tabla.joinpath(id)

        await archivo.write_text(contenido)

    async def crear(self, tabla: str, id: str, contenido: str):
        dir_tabla: AsyncPath = self.carpeta.joinpath(tabla)
        await dir_tabla.mkdir(exist_ok=True)
        nuevo_archivo: AsyncPath = dir_tabla.joinpath(id)

        if await nuevo_archivo.exists():
            raise FileExistsError("Se intentó crear un archivo que ya existía")

        await nuevo_archivo.write_text(contenido)
    
    async def borrar(self, tabla:str, id: str):
        dir_tabla: AsyncPath = self.carpeta.joinpath(tabla)
        archivo: AsyncPath = dir_tabla.joinpath(id)

        await archivo.unlink()