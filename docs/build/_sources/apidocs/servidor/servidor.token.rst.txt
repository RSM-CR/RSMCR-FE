:py:mod:`servidor.token`
========================

.. py:module:: servidor.token

.. autodoc2-docstring:: servidor.token
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Tenant <servidor.token.Tenant>`
     -
   * - :py:obj:`Token <servidor.token.Token>`
     - .. autodoc2-docstring:: servidor.token.Token
          :parser: myst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_entorno <servidor.token._entorno>`
     - .. autodoc2-docstring:: servidor.token._entorno
          :parser: myst
          :summary:
   * - :py:obj:`_llave <servidor.token._llave>`
     - .. autodoc2-docstring:: servidor.token._llave
          :parser: myst
          :summary:

API
~~~

.. py:class:: Tenant(/, **data: typing.Any)
   :canonical: servidor.token.Tenant

   Bases: :py:obj:`pydantic.BaseModel`

   .. py:attribute:: tenantId
      :canonical: servidor.token.Tenant.tenantId
      :type: str
      :value: None

      .. autodoc2-docstring:: servidor.token.Tenant.tenantId
         :parser: myst

   .. py:attribute:: tenantName
      :canonical: servidor.token.Tenant.tenantName
      :type: str
      :value: None

      .. autodoc2-docstring:: servidor.token.Tenant.tenantName
         :parser: myst

.. py:class:: Token(/, **data: typing.Any)
   :canonical: servidor.token.Token

   Bases: :py:obj:`pydantic.BaseModel`

   .. autodoc2-docstring:: servidor.token.Token
      :parser: myst

   .. py:method:: _decodificar_de_jwt(token: str) -> dict
      :canonical: servidor.token.Token._decodificar_de_jwt
      :classmethod:

      .. autodoc2-docstring:: servidor.token.Token._decodificar_de_jwt
         :parser: myst

   .. py:method:: codificar_como_jwt() -> str
      :canonical: servidor.token.Token.codificar_como_jwt

      .. autodoc2-docstring:: servidor.token.Token.codificar_como_jwt
         :parser: myst

   .. py:method:: decodificar_de_jwt(token: str) -> typing.Self
      :canonical: servidor.token.Token.decodificar_de_jwt
      :classmethod:

      .. autodoc2-docstring:: servidor.token.Token.decodificar_de_jwt
         :parser: myst

   .. py:attribute:: exp
      :canonical: servidor.token.Token.exp
      :type: datetime.datetime
      :value: 'Field(...)'

      .. autodoc2-docstring:: servidor.token.Token.exp
         :parser: myst

   .. py:attribute:: sub
      :canonical: servidor.token.Token.sub
      :type: str
      :value: None

      .. autodoc2-docstring:: servidor.token.Token.sub
         :parser: myst

   .. py:attribute:: tenants
      :canonical: servidor.token.Token.tenants
      :type: list[servidor.token.Tenant]
      :value: None

      .. autodoc2-docstring:: servidor.token.Token.tenants
         :parser: myst

.. py:data:: _entorno
   :canonical: servidor.token._entorno
   :value: 'obtener_entorno(...)'

   .. autodoc2-docstring:: servidor.token._entorno
      :parser: myst

.. py:data:: _llave
   :canonical: servidor.token._llave
   :value: 'get_secret_value(...)'

   .. autodoc2-docstring:: servidor.token._llave
      :parser: myst
