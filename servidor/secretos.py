"""Se encarga de almacenar, cargar y validar los datos privados de la aplicación de un
archivo .env"""
from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import PydanticUndefined
import logging
import os

class _Entorno(BaseSettings):
    """Representa todos los datos que están dentro del archivo `.env`. Si se desea añadir un
    dato adicional, se debe de crear un atributo para este dentro de esta clase."""

    # Lee del .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    """Invoca a [Pydantic](https://pydantic.dev/docs/validation/latest/get-started/) para
    leer y validar las variables de entorno"""

    def __init__(self) -> None:
        """:meta private:"""
        super().__init__()

    # Define todas las configuraciones
    ID_CLIENTE_XERO: SecretStr = Field(default=...)
    """El ID del cliente que genera Xero para la aplicación. Después de crear la aplicación,
    se puede obtener en
    [https://developer.xero.com/app/manage](https://developer.xero.com/app/manage) dentro de
    la pestaña de configuración."""
    SECRETO_CLIENTE_XERO: SecretStr = Field(default=...)
    """El secreto del que genera Xero para la aplicación. Después de crear la aplicación,
    se puede obtener en
    [https://developer.xero.com/app/manage](https://developer.xero.com/app/manage) dentro de
    la pestaña de configuración."""
    USUARIO_GTI: SecretStr = Field(default=...)
    """El nombre de usuario de GTI. Suele ser una cédula jurídica."""
    CONTRASENA_GTI: SecretStr = Field(default=...)
    """La contraseña utilizada para iniciar sesion en GTI."""
    TOKEN_ACTUALIZACION_XERO: SecretStr = SecretStr("")
    """El token de actualización de Xero para mantener acceso a su API. Se recomienda ver la
    documentación del módulo [auth](auth) para obtener más información."""
    ID_TENANT_XERO: str = ""
    """El ID de la organización de Xero. Se recomienda ver la documentación del módulo
    [auth](auth) para obtener más información."""
    PUERTO: int = 8000
    """El puerto de red en el que se va a abrir el servidor. Su valor por defecto es de 8000."""
    XERO_WEBHOOK_SECRET: SecretStr = Field(default=...)
    """El secreto que genera Xero para recibir notificaciones del Webhook. Después de crear
    la aplicación, se puede obtener en
    [https://developer.xero.com/app/manage](https://developer.xero.com/app/manage)."""

def crear_entorno() -> None:
    """Crea un archivo .env en base a los datos suministrados por el usuario. También, da
    la opción de saltarse los parámetros opcionales, que son aquellos que la configuración
    puede generar de forma automática."""
    if os.path.exists(".env"):
        print("El archivo .env ya existe. ¿Deseas sobreescribirlo? s/N")
        # Operador Walrus (:=): Crea una variable antes de seguir con las comparaciones del if
        if (sobreescribir := input("> ").lower()) != "s" and sobreescribir != "y":
            return
    
    print("¿Deseas configurar los parámetros opcionales? s/N")
    configurar_opcionales = (entrada := input("> ").lower()) == "s" or entrada == "y"

    nuevo_entorno = list[str]()

    # Hace un bucle que pregunta por todas las variables definidas en Entorno
    for nombre, info in _Entorno.model_fields.items():
        opcional = info.default is not PydanticUndefined

        if opcional and not configurar_opcionales:
            continue

        valor = input(f"Introduce un valor para {nombre}{f" (Opcional. Dejar en blanco para el valor por defecto de \"{info.default}\")" if opcional else ""}\n> ").strip()
        if not valor and opcional:
            valor = info.default
        while not valor and not opcional:
            valor = input(f"Especificar {nombre} es obligatorio. Introduce un valor\n> ").strip()
        
        nuevo_entorno.append(f"{nombre}={valor}")

    with open(".env", "w") as env:
        env.write("\n".join(nuevo_entorno) + "\n")

    print("¡Archivo .env generado con éxito!")
    logging.info("Se ha generado un nuevo archivo .env")

_entorno: None | _Entorno = None
def obtener_entorno():
    """Instanciar un [_Entorno](secretos._Entorno) directamente puede causar errores al
    importar el módulo. Esta función evita este problema al popular la variable
    [_entorno](secretos._entorno) de forma perezosa. En otras palabras,
    [_entorno](secretos._entorno) comienza con un valor de `None` y cuando la función es
    llamada por primera vez, se crea y se carga el [_Entorno](secretos._Entorno)."""
    global _entorno
    if _entorno is None:
        _entorno = _Entorno()
    return _entorno

if __name__ == "__main__":
    print("Imprimiendo todos los valores del .env...")
    print(obtener_entorno().model_dump())
