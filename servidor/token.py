from datetime import datetime, timedelta, timezone
from pydantic import BaseModel, Field
from typing import Self
from servidor.secretos import obtener_entorno
import jwt

_entorno = obtener_entorno()
_llave = _entorno.LLAVE_JWT.get_secret_value()

class Tenant(BaseModel):
    tenantId: str
    tenantName: str

# En teoría, debería haber una clase base por si se quiere añadir algún proveedor de
# identidad que no requiera almacenar los tenants, pero es un cambio fácil de hacer
# en el futuro, por lo que no me preocupa mucho
class Token(BaseModel):
    """Permite identificar que el usuario se ha autenticado con éxito sin depender
    exclusivamente de las APIs de Xero.
    
    > [!NOTE]
    > Si se desea añadir un proveedor de identidad distinto a Xero, esta clase debería ser
    > convertida a una clase base e independiente de tanto Xero y el nuevo proveedor.
    > También se deberían reubicar los campos exclusivos a Xero a una subclase específica."""

    sub: str
    """El identificador único de cada usuario. Es el mismo que utiliza Xero."""
    exp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc) + timedelta(minutes=30))
    """La fecha de expiración del token. Por defecto, es de 30 minutos a partir de su fecha de creación."""
    tenants: list[Tenant]
    """La lista de organizaciones a las cuales el usuario tiene acceso."""

    def codificar_como_jwt(self) -> str:
        return jwt.encode(
            payload=self.model_dump(),
            key=_llave,
            algorithm="HS256"
        )
    
    @classmethod
    def _decodificar_de_jwt(cls, token: str) -> dict:
        return  jwt.decode(
            jwt=token,
            key=_llave,
            algorithms=["HS256"]
        )

    @classmethod
    def decodificar_de_jwt(cls, token: str) -> Self:
        diccionario = cls._decodificar_de_jwt(token)
        return cls.model_validate(diccionario)
    