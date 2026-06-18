:py:mod:`factura`
=================

.. py:module:: factura

.. autodoc2-docstring:: factura
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Factura <factura.Factura>`
     - .. autodoc2-docstring:: factura.Factura
          :parser: myst
          :summary:
   * - :py:obj:`DatosGTI <factura.DatosGTI>`
     - .. autodoc2-docstring:: factura.DatosGTI
          :parser: myst
          :summary:
   * - :py:obj:`DatosXero <factura.DatosXero>`
     - .. autodoc2-docstring:: factura.DatosXero
          :parser: myst
          :summary:

API
~~~

.. py:class:: Factura()
   :canonical: factura.Factura

   .. autodoc2-docstring:: factura.Factura
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: factura.Factura.__init__
      :parser: myst

.. py:class:: DatosGTI
   :canonical: factura.DatosGTI

   .. autodoc2-docstring:: factura.DatosGTI
      :parser: myst

   .. py:method:: obtener_datos(archivo_xml='Prueba.xml') -> factura.Factura
      :canonical: factura.DatosGTI.obtener_datos
      :staticmethod:

      .. autodoc2-docstring:: factura.DatosGTI.obtener_datos
         :parser: myst

.. py:class:: DatosXero
   :canonical: factura.DatosXero

   .. autodoc2-docstring:: factura.DatosXero
      :parser: myst

   .. py:method:: obtener_datos(archivo_json: str) -> list[factura.Factura]
      :canonical: factura.DatosXero.obtener_datos
      :staticmethod:

      .. autodoc2-docstring:: factura.DatosXero.obtener_datos
         :parser: myst
