:py:mod:`destino`
=================

.. py:module:: destino

.. autodoc2-docstring:: destino
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Destino <destino.Destino>`
     - .. autodoc2-docstring:: destino.Destino
          :parser: myst
          :summary:

API
~~~

.. py:class:: Destino()
   :canonical: destino.Destino

   Bases: :py:obj:`abc.ABC`

   .. autodoc2-docstring:: destino.Destino
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: destino.Destino.__init__
      :parser: myst

   .. py:method:: subir_factura(factura)
      :canonical: destino.Destino.subir_factura
      :abstractmethod:

      .. autodoc2-docstring:: destino.Destino.subir_factura
         :parser: myst

   .. py:method:: obtener_documento()
      :canonical: destino.Destino.obtener_documento
      :abstractmethod:

      .. autodoc2-docstring:: destino.Destino.obtener_documento
         :parser: myst
