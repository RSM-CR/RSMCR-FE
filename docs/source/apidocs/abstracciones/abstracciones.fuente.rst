:py:mod:`abstracciones.fuente`
==============================

.. py:module:: abstracciones.fuente

.. autodoc2-docstring:: abstracciones.fuente
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`CallbackNuevaFactura <abstracciones.fuente.CallbackNuevaFactura>`
     -
   * - :py:obj:`Fuente <abstracciones.fuente.Fuente>`
     - .. autodoc2-docstring:: abstracciones.fuente.Fuente
          :parser: myst
          :summary:

API
~~~

.. py:class:: CallbackNuevaFactura
   :canonical: abstracciones.fuente.CallbackNuevaFactura

   Bases: :py:obj:`typing.Protocol`

   .. py:method:: __call__(factura) -> typing.Any
      :canonical: abstracciones.fuente.CallbackNuevaFactura.__call__

      .. autodoc2-docstring:: abstracciones.fuente.CallbackNuevaFactura.__call__
         :parser: myst

.. py:class:: Fuente()
   :canonical: abstracciones.fuente.Fuente

   Bases: :py:obj:`abc.ABC`

   .. autodoc2-docstring:: abstracciones.fuente.Fuente
      :parser: myst

   .. py:method:: __init__() -> None
      :canonical: abstracciones.fuente.Fuente.__init__

      .. autodoc2-docstring:: abstracciones.fuente.Fuente.__init__
         :parser: myst

   .. py:method:: escuchar_nueva_factura(funcion: abstracciones.fuente.CallbackNuevaFactura) -> None
      :canonical: abstracciones.fuente.Fuente.escuchar_nueva_factura

      .. autodoc2-docstring:: abstracciones.fuente.Fuente.escuchar_nueva_factura
         :parser: myst

   .. py:method:: notificar_nueva_factura(factura)
      :canonical: abstracciones.fuente.Fuente.notificar_nueva_factura

      .. autodoc2-docstring:: abstracciones.fuente.Fuente.notificar_nueva_factura
         :parser: myst

   .. py:method:: subir_documento(documento)
      :canonical: abstracciones.fuente.Fuente.subir_documento
      :abstractmethod:

      .. autodoc2-docstring:: abstracciones.fuente.Fuente.subir_documento
         :parser: myst
