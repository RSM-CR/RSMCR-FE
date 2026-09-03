:py:mod:`xero.auth`
===================

.. py:module:: xero.auth

.. autodoc2-docstring:: xero.auth
   :parser: myst
   :allowtitles:

Module Contents
---------------

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_adjuntar_headers <xero.auth._adjuntar_headers>`
     - .. autodoc2-docstring:: xero.auth._adjuntar_headers
          :parser: myst
          :summary:
   * - :py:obj:`_al_actualizar_token <xero.auth._al_actualizar_token>`
     - .. autodoc2-docstring:: xero.auth._al_actualizar_token
          :parser: myst
          :summary:
   * - :py:obj:`_iniciar_sesion <xero.auth._iniciar_sesion>`
     - .. autodoc2-docstring:: xero.auth._iniciar_sesion
          :parser: myst
          :summary:
   * - :py:obj:`_router_auth <xero.auth._router_auth>`
     - .. autodoc2-docstring:: xero.auth._router_auth
          :parser: myst
          :summary:
   * - :py:obj:`crear_cliente <xero.auth.crear_cliente>`
     - .. autodoc2-docstring:: xero.auth.crear_cliente
          :parser: myst
          :summary:
   * - :py:obj:`iniciar_sesion <xero.auth.iniciar_sesion>`
     - .. autodoc2-docstring:: xero.auth.iniciar_sesion
          :parser: myst
          :summary:
   * - :py:obj:`obtener_cliente <xero.auth.obtener_cliente>`
     - .. autodoc2-docstring:: xero.auth.obtener_cliente
          :parser: myst
          :summary:
   * - :py:obj:`router_auth <xero.auth.router_auth>`
     - .. autodoc2-docstring:: xero.auth.router_auth
          :parser: myst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`_cliente <xero.auth._cliente>`
     - .. autodoc2-docstring:: xero.auth._cliente
          :parser: myst
          :summary:
   * - :py:obj:`_entorno <xero.auth._entorno>`
     - .. autodoc2-docstring:: xero.auth._entorno
          :parser: myst
          :summary:
   * - :py:obj:`_logger <xero.auth._logger>`
     - .. autodoc2-docstring:: xero.auth._logger
          :parser: myst
          :summary:
   * - :py:obj:`_token_actualizacion <xero.auth._token_actualizacion>`
     - .. autodoc2-docstring:: xero.auth._token_actualizacion
          :parser: myst
          :summary:

API
~~~

.. py:function:: _adjuntar_headers(url, headers, body)
   :canonical: xero.auth._adjuntar_headers

   .. autodoc2-docstring:: xero.auth._adjuntar_headers
      :parser: myst

.. py:function:: _al_actualizar_token(token: dict, refresh_token=None, access_token=None)
   :canonical: xero.auth._al_actualizar_token
   :async:

   .. autodoc2-docstring:: xero.auth._al_actualizar_token
      :parser: myst

.. py:data:: _cliente
   :canonical: xero.auth._cliente
   :type: authlib.integrations.httpx_client.AsyncOAuth2Client | None
   :value: None

   .. autodoc2-docstring:: xero.auth._cliente
      :parser: myst

.. py:data:: _entorno
   :canonical: xero.auth._entorno
   :value: 'obtener_entorno(...)'

   .. autodoc2-docstring:: xero.auth._entorno
      :parser: myst

.. py:function:: _iniciar_sesion() -> None
   :canonical: xero.auth._iniciar_sesion
   :async:

   .. autodoc2-docstring:: xero.auth._iniciar_sesion
      :parser: myst

.. py:data:: _logger
   :canonical: xero.auth._logger
   :value: 'Logger(...)'

   .. autodoc2-docstring:: xero.auth._logger
      :parser: myst

.. py:function:: _router_auth(redirigir_a: str, admin=False) -> tuple[fastapi.APIRouter, authlib.integrations.starlette_client.StarletteOAuth2App]
   :canonical: xero.auth._router_auth

   .. autodoc2-docstring:: xero.auth._router_auth
      :parser: myst

.. py:data:: _token_actualizacion
   :canonical: xero.auth._token_actualizacion
   :value: 'get_secret_value(...)'

   .. autodoc2-docstring:: xero.auth._token_actualizacion
      :parser: myst

.. py:function:: crear_cliente() -> authlib.integrations.httpx_client.AsyncOAuth2Client
   :canonical: xero.auth.crear_cliente
   :async:

   .. autodoc2-docstring:: xero.auth.crear_cliente
      :parser: myst

.. py:function:: iniciar_sesion() -> None
   :canonical: xero.auth.iniciar_sesion

   .. autodoc2-docstring:: xero.auth.iniciar_sesion
      :parser: myst

.. py:function:: obtener_cliente() -> authlib.integrations.httpx_client.AsyncOAuth2Client
   :canonical: xero.auth.obtener_cliente
   :async:

   .. autodoc2-docstring:: xero.auth.obtener_cliente
      :parser: myst

.. py:function:: router_auth(redirigir_a: str) -> tuple[fastapi.APIRouter, authlib.integrations.starlette_client.StarletteOAuth2App]
   :canonical: xero.auth.router_auth

   .. autodoc2-docstring:: xero.auth.router_auth
      :parser: myst
