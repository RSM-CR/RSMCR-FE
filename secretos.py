from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import PydanticUndefined
import logging
import os

class Entorno(BaseSettings):
    # Lee del .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Define todas las configuraciones
    ID_CLIENTE: SecretStr = Field(default=...)
    SECRETO_CLIENTE: SecretStr = Field(default=...)
    USUARIO_GTI: SecretStr = Field(default=...)
    CONTRASENA_GTI: SecretStr = Field(default=...)
    PUERTO: int = 3000

def crear_entorno():
    if os.path.exists(".env"):
        logging.warning("El archivo .env ya existe. ¿Deseas sobreescribirlo? s/N")
        # Operador Walrus (:=): Crea una variable antes de seguir con las comparaciones del if
        if (sobreescribir := input("> ").lower()) != "s" and sobreescribir != "y":
            return
    
    nuevo_entorno = list[str]()

    # Hace un bucle que pregunta por todas las variables definidas en Entorno
    for nombre, info in Entorno.model_fields.items():
        opcional = info.default is not PydanticUndefined

        valor = input(f"Introduce un valor para {nombre}{f" (Opcional. Dejar en blanco para el valor por defecto de {info.default})" if opcional else ""}\n> ").strip()
        if not valor and opcional:
            valor = info.default
        while not valor and not opcional:
            valor = input(f"Especificar {nombre} es obligatorio. Introduce un valor\n> ").strip()
        
        nuevo_entorno.append(f"{nombre}={valor}")

    with open(".env", "w") as env:
        env.write("\n".join(nuevo_entorno) + "\n")

    print("¡Archivo .env generado con éxito!")

if __name__ == "__main__":
    print("Imprimiendo todos los valores del .env...")
    entorno = Entorno()
    print(entorno.model_dump())