:py:mod:`servidor.servidor`
===========================

.. py:module:: servidor.servidor

.. autodoc2-docstring:: servidor.servidor
   :parser: myst
   :allowtitles:

Module Contents
---------------

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`dict_a_xml <servidor.servidor.dict_a_xml>`
     - .. autodoc2-docstring:: servidor.servidor.dict_a_xml
          :parser: myst
          :summary:
   * - :py:obj:`recent_xml <servidor.servidor.recent_xml>`
     - .. autodoc2-docstring:: servidor.servidor.recent_xml
          :parser: myst
          :summary:
   * - :py:obj:`recibir_json <servidor.servidor.recibir_json>`
     - .. autodoc2-docstring:: servidor.servidor.recibir_json
          :parser: myst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`app <servidor.servidor.app>`
     - .. autodoc2-docstring:: servidor.servidor.app
          :parser: myst
          :summary:
   * - :py:obj:`entorno <servidor.servidor.entorno>`
     - .. autodoc2-docstring:: servidor.servidor.entorno
          :parser: myst
          :summary:
   * - :py:obj:`filedb <servidor.servidor.filedb>`
     - .. autodoc2-docstring:: servidor.servidor.filedb
          :parser: myst
          :summary:
   * - :py:obj:`logger <servidor.servidor.logger>`
     - .. autodoc2-docstring:: servidor.servidor.logger
          :parser: myst
          :summary:

API
~~~

.. py:data:: app
   :canonical: servidor.servidor.app
   :value: 'FastAPI(...)'

   .. autodoc2-docstring:: servidor.servidor.app
      :parser: myst

.. py:function:: dict_a_xml(tag: str, diccionario: dict[str, typing.Any]) -> xml.etree.ElementTree.Element
   :canonical: servidor.servidor.dict_a_xml

   .. autodoc2-docstring:: servidor.servidor.dict_a_xml
      :parser: myst

.. py:data:: entorno
   :canonical: servidor.servidor.entorno
   :value: 'obtener_entorno(...)'

   .. autodoc2-docstring:: servidor.servidor.entorno
      :parser: myst

.. py:data:: filedb
   :canonical: servidor.servidor.filedb
   :value: 'FileDb(...)'

   .. autodoc2-docstring:: servidor.servidor.filedb
      :parser: myst

.. py:data:: logger
   :canonical: servidor.servidor.logger
   :value: 'getLogger(...)'

   .. autodoc2-docstring:: servidor.servidor.logger
      :parser: myst

.. py:function:: recent_xml(count: int = 10)
   :canonical: servidor.servidor.recent_xml
   :async:

   .. autodoc2-docstring:: servidor.servidor.recent_xml
      :parser: myst

.. py:function:: recibir_json(request: fastapi.Request)
   :canonical: servidor.servidor.recibir_json
   :async:

   .. autodoc2-docstring:: servidor.servidor.recibir_json
      :parser: myst
