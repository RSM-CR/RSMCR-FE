:py:mod:`servidor.secretos`
===========================

.. py:module:: servidor.secretos

.. autodoc2-docstring:: servidor.secretos
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_Entorno <servidor.secretos._Entorno>`
     - .. autodoc2-docstring:: servidor.secretos._Entorno
          :parser: myst
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`crear_entorno <servidor.secretos.crear_entorno>`
     - .. autodoc2-docstring:: servidor.secretos.crear_entorno
          :parser: myst
          :summary:
   * - :py:obj:`obtener_entorno <servidor.secretos.obtener_entorno>`
     - .. autodoc2-docstring:: servidor.secretos.obtener_entorno
          :parser: myst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_entorno <servidor.secretos._entorno>`
     - .. autodoc2-docstring:: servidor.secretos._entorno
          :parser: myst
          :summary:

API
~~~

.. py:class:: _Entorno()
   :canonical: servidor.secretos._Entorno

   Bases: :py:obj:`pydantic_settings.BaseSettings`

   .. autodoc2-docstring:: servidor.secretos._Entorno
      :parser: myst

   .. py:attribute:: CONTRASENA_GTI
      :canonical: servidor.secretos._Entorno.CONTRASENA_GTI
      :type: pydantic.SecretStr
      :value: 'Field(...)'

      .. autodoc2-docstring:: servidor.secretos._Entorno.CONTRASENA_GTI
         :parser: myst

   .. py:attribute:: ID_CLIENTE_XERO
      :canonical: servidor.secretos._Entorno.ID_CLIENTE_XERO
      :type: pydantic.SecretStr
      :value: 'Field(...)'

      .. autodoc2-docstring:: servidor.secretos._Entorno.ID_CLIENTE_XERO
         :parser: myst

   .. py:attribute:: ID_TENANT_XERO
      :canonical: servidor.secretos._Entorno.ID_TENANT_XERO
      :type: str
      :value: <Multiline-String>

      .. autodoc2-docstring:: servidor.secretos._Entorno.ID_TENANT_XERO
         :parser: myst

   .. py:attribute:: LLAVE_JWT
      :canonical: servidor.secretos._Entorno.LLAVE_JWT
      :type: pydantic.SecretStr
      :value: 'SecretStr(...)'

      .. autodoc2-docstring:: servidor.secretos._Entorno.LLAVE_JWT
         :parser: myst

   .. py:attribute:: LLAVE_SESIONES
      :canonical: servidor.secretos._Entorno.LLAVE_SESIONES
      :type: pydantic.SecretStr
      :value: 'SecretStr(...)'

      .. autodoc2-docstring:: servidor.secretos._Entorno.LLAVE_SESIONES
         :parser: myst

   .. py:attribute:: NGROK_AUTHTOKEN
      :canonical: servidor.secretos._Entorno.NGROK_AUTHTOKEN
      :type: pydantic.SecretStr
      :value: 'SecretStr(...)'

      .. autodoc2-docstring:: servidor.secretos._Entorno.NGROK_AUTHTOKEN
         :parser: myst

   .. py:attribute:: PUERTO
      :canonical: servidor.secretos._Entorno.PUERTO
      :type: int
      :value: 8000

      .. autodoc2-docstring:: servidor.secretos._Entorno.PUERTO
         :parser: myst

   .. py:attribute:: SECRETO_CLIENTE_XERO
      :canonical: servidor.secretos._Entorno.SECRETO_CLIENTE_XERO
      :type: pydantic.SecretStr
      :value: 'Field(...)'

      .. autodoc2-docstring:: servidor.secretos._Entorno.SECRETO_CLIENTE_XERO
         :parser: myst

   .. py:attribute:: TOKEN_ACTUALIZACION_XERO
      :canonical: servidor.secretos._Entorno.TOKEN_ACTUALIZACION_XERO
      :type: pydantic.SecretStr
      :value: 'SecretStr(...)'

      .. autodoc2-docstring:: servidor.secretos._Entorno.TOKEN_ACTUALIZACION_XERO
         :parser: myst

   .. py:attribute:: USE_NGROK
      :canonical: servidor.secretos._Entorno.USE_NGROK
      :type: bool
      :value: False

      .. autodoc2-docstring:: servidor.secretos._Entorno.USE_NGROK
         :parser: myst

   .. py:attribute:: USUARIO_GTI
      :canonical: servidor.secretos._Entorno.USUARIO_GTI
      :type: pydantic.SecretStr
      :value: 'Field(...)'

      .. autodoc2-docstring:: servidor.secretos._Entorno.USUARIO_GTI
         :parser: myst

   .. py:attribute:: XERO_WEBHOOK_SECRET
      :canonical: servidor.secretos._Entorno.XERO_WEBHOOK_SECRET
      :type: pydantic.SecretStr
      :value: 'Field(...)'

      .. autodoc2-docstring:: servidor.secretos._Entorno.XERO_WEBHOOK_SECRET
         :parser: myst

   .. py:method:: __init__() -> None
      :canonical: servidor.secretos._Entorno.__init__

   .. py:attribute:: model_config
      :canonical: servidor.secretos._Entorno.model_config
      :value: 'SettingsConfigDict(...)'

      .. autodoc2-docstring:: servidor.secretos._Entorno.model_config
         :parser: myst

.. py:data:: _entorno
   :canonical: servidor.secretos._entorno
   :type: None | servidor.secretos._Entorno
   :value: None

   .. autodoc2-docstring:: servidor.secretos._entorno
      :parser: myst

.. py:function:: crear_entorno() -> None
   :canonical: servidor.secretos.crear_entorno

   .. autodoc2-docstring:: servidor.secretos.crear_entorno
      :parser: myst

.. py:function:: obtener_entorno()
   :canonical: servidor.secretos.obtener_entorno

   .. autodoc2-docstring:: servidor.secretos.obtener_entorno
      :parser: myst
