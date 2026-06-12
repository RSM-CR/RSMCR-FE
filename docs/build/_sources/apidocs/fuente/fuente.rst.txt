:py:mod:`fuente`
================

.. py:module:: fuente

.. autodoc2-docstring:: fuente
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`CallbackNuevaFactura <fuente.CallbackNuevaFactura>`
     - .. autodoc2-docstring:: fuente.CallbackNuevaFactura
          :parser: myst
          :summary:
   * - :py:obj:`Fuente <fuente.Fuente>`
     - .. autodoc2-docstring:: fuente.Fuente
          :parser: myst
          :summary:

API
~~~

.. py:class:: CallbackNuevaFactura
   :canonical: fuente.CallbackNuevaFactura

   Bases: :py:obj:`typing.Protocol`

   .. autodoc2-docstring:: fuente.CallbackNuevaFactura
      :parser: myst

   .. py:method:: __call__(factura) -> typing.Any
      :canonical: fuente.CallbackNuevaFactura.__call__

      .. autodoc2-docstring:: fuente.CallbackNuevaFactura.__call__
         :parser: myst

.. py:class:: Fuente()
   :canonical: fuente.Fuente

   Bases: :py:obj:`abc.ABC`

   .. autodoc2-docstring:: fuente.Fuente
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: fuente.Fuente.__init__
      :parser: myst

   .. py:method:: subir_documento(documento)
      :canonical: fuente.Fuente.subir_documento
      :abstractmethod:

      .. autodoc2-docstring:: fuente.Fuente.subir_documento
         :parser: myst

   .. py:method:: escuchar_nueva_factura(funcion: fuente.CallbackNuevaFactura) -> None
      :canonical: fuente.Fuente.escuchar_nueva_factura
      :abstractmethod:

      .. autodoc2-docstring:: fuente.Fuente.escuchar_nueva_factura
         :parser: myst

   .. py:method:: notificar_nueva_factura(factura)
      :canonical: fuente.Fuente.notificar_nueva_factura

      .. autodoc2-docstring:: fuente.Fuente.notificar_nueva_factura
         :parser: myst
