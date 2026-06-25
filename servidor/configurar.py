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
import subprocess

color_texto = "\033[34m"
color_blanco = "\033[0m"

def verificar_node() -> bool:
    try:
        version =  subprocess.check_output(["node", "-v"], stderr=subprocess.STDOUT, text=True)
        print(f"Se detectó una instalación de Node.js: {version}")
        return True
    except Exception as e:
        print(e)
        print("Hubo un error al comprobar si Node.js está instalado. Descárgalo en tu equipo si no está instalado.")
        return False

def construir_frontend() -> None:
    if not verificar_node():
        return
    
    try:
        print(f"{color_texto}Por favor espera mientras se instalan las dependencias...{color_blanco}")
        subprocess.run(["npm", "install"], cwd="./interfaz", shell=True, check=True)
        print(f"{color_texto}Por favor espera mientras se crea la interfaz de usuario...{color_blanco}")
        subprocess.run(["npm", "run", "build"], cwd="./interfaz", shell=True, check=True)
        print(f"{color_texto}¡Interfaz construida con éxito!{color_blanco}")
    except:
        print("Hubo un error al tratar de generar la interfaz de usuario.")
        raise

# Es muy importante poner los imports justo antes de que se usen
# El órden de inicialización puede causar errores
if __name__ == "__main__":
    print(f"{color_texto}¡Bienvenido! Te ayudaré a configurar el servidor{color_blanco}")
    construir_frontend()

    from servidor.secretos import crear_entorno
    print(f"{color_texto}Ahora, define las variables de entorno{color_blanco}")
    crear_entorno()

    from xero.auth import iniciar_sesion
    print(f"{color_texto}Seguidamente, inicia sesión en Xero{color_blanco}")
    iniciar_sesion()

    print(f"{color_texto}¡Has terminado de configurar el servidor!{color_blanco}")
