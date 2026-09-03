:py:mod:`servidor.filedb`
=========================

.. py:module:: servidor.filedb

.. autodoc2-docstring:: servidor.filedb
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`FileDb <servidor.filedb.FileDb>`
     -

API
~~~

.. py:class:: FileDb(carpeta: str = './servidor/filedb')
   :canonical: servidor.filedb.FileDb

   Bases: :py:obj:`abstracciones.db.Db`

   .. py:method:: __init__(carpeta: str = './servidor/filedb') -> None
      :canonical: servidor.filedb.FileDb.__init__

      .. autodoc2-docstring:: servidor.filedb.FileDb.__init__
         :parser: myst

   .. py:method:: actualizar(tabla: str, id: str, contenido: str)
      :canonical: servidor.filedb.FileDb.actualizar
      :async:

   .. py:method:: borrar(tabla: str, id: str)
      :canonical: servidor.filedb.FileDb.borrar
      :async:

   .. py:method:: crear(tabla: str, id: str, contenido: str)
      :canonical: servidor.filedb.FileDb.crear
      :async:

   .. py:method:: obtener_recientes(tabla: str, cantidad: int, ultimo_id: str | None = None) -> list[abstracciones.db.Documento]
      :canonical: servidor.filedb.FileDb.obtener_recientes
      :async:
