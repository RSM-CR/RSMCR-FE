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