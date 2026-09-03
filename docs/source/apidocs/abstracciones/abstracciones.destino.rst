:py:mod:`abstracciones.destino`
===============================

.. py:module:: abstracciones.destino

.. autodoc2-docstring:: abstracciones.destino
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Destino <abstracciones.destino.Destino>`
     - .. autodoc2-docstring:: abstracciones.destino.Destino
          :parser: myst
          :summary:

API
~~~

.. py:class:: Destino()
   :canonical: abstracciones.destino.Destino

   Bases: :py:obj:`abc.ABC`

   .. autodoc2-docstring:: abstracciones.destino.Destino
      :parser: myst

   .. py:method:: __init__() -> None
      :canonical: abstracciones.destino.Destino.__init__

      .. autodoc2-docstring:: abstracciones.destino.Destino.__init__
         :parser: myst

   .. py:method:: obtener_documento()
      :canonical: abstracciones.destino.Destino.obtener_documento
      :abstractmethod:

      .. autodoc2-docstring:: abstracciones.destino.Destino.obtener_documento
         :parser: myst

   .. py:method:: subir_factura(factura)
      :canonical: abstracciones.destino.Destino.subir_factura
      :abstractmethod:

      .. autodoc2-docstring:: abstracciones.destino.Destino.subir_factura
         :parser: myst
