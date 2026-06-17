"""Ejecuta este módulo para configurar las variables de entorno que
el servidor necesita para funcionar. Para esto, navega al directorio
base del proyecto, ejecuta el siguiente comando:
```
python -m servidor.configurar
```
O, alternativamente:
```
py -m servidor.configurar
```
A continuación, deberás suministrar los datos solicitados y seguir las
instrucciones dadas por el módulo.

Revisa la documentación del módulo [secretos](secretos._Entorno) para ver información
sobre todas las variables de entorno disponibles.
"""
# Es muy importante poner los imports justo antes de que se usen
# El órden de inicialización puede causar errores
if __name__ == "__main__":
    from servidor.secretos import crear_entorno
    print("¡Bienvenido! Te ayudaré a configurar el servidor")
    print("Primero, define las variables de entorno")
    crear_entorno()

    from xero.auth import iniciar_sesion
    print("Seguidamente, inicia sesión en Xero")
    iniciar_sesion()

    print("Has terminado de configurar el servidor")
