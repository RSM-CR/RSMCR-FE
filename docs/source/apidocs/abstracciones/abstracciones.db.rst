:py:mod:`abstracciones.db`
==========================

.. py:module:: abstracciones.db

.. autodoc2-docstring:: abstracciones.db
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Db <abstracciones.db.Db>`
     -
   * - :py:obj:`Documento <abstracciones.db.Documento>`
     -

API
~~~

.. py:class:: Db
   :canonical: abstracciones.db.Db

   Bases: :py:obj:`abc.ABC`

   .. py:method:: actualizar(tabla: str, id: str, contenido: str)
      :canonical: abstracciones.db.Db.actualizar
      :abstractmethod:
      :async:

      .. autodoc2-docstring:: abstracciones.db.Db.actualizar
         :parser: myst

   .. py:method:: borrar(tabla: str, id: str)
      :canonical: abstracciones.db.Db.borrar
      :abstractmethod:
      :async:

      .. autodoc2-docstring:: abstracciones.db.Db.borrar
         :parser: myst

   .. py:method:: crear(tabla: str, id: str, contenido: str)
      :canonical: abstracciones.db.Db.crear
      :abstractmethod:
      :async:

      .. autodoc2-docstring:: abstracciones.db.Db.crear
         :parser: myst

   .. py:method:: obtener_recientes(tabla: str, cantidad: int, ultimo_id: str | None) -> list[abstracciones.db.Documento]
      :canonical: abstracciones.db.Db.obtener_recientes
      :abstractmethod:
      :async:

      .. autodoc2-docstring:: abstracciones.db.Db.obtener_recientes
         :parser: myst

.. py:class:: Documento(/, **data: typing.Any)
   :canonical: abstracciones.db.Documento

   Bases: :py:obj:`pydantic.BaseModel`

   .. py:attribute:: id
      :canonical: abstracciones.db.Documento.id
      :type: str
      :value: None

      .. autodoc2-docstring:: abstracciones.db.Documento.id
         :parser: myst

   .. py:attribute:: nombre
      :canonical: abstracciones.db.Documento.nombre
      :type: str
      :value: None

      .. autodoc2-docstring:: abstracciones.db.Documento.nombre
         :parser: myst

   .. py:attribute:: obtener_contenido
      :canonical: abstracciones.db.Documento.obtener_contenido
      :type: typing.Callable[[], typing.Awaitable[str]]
      :value: None

      .. autodoc2-docstring:: abstracciones.db.Documento.obtener_contenido
         :parser: myst

   .. py:attribute:: tabla
      :canonical: abstracciones.db.Documento.tabla
      :type: str
      :value: None

      .. autodoc2-docstring:: abstracciones.db.Documento.tabla
         :parser: myst
