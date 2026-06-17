# Inducción a Sphinx

En este apartado se detalla todo el proceso de instalación de Sphinx dentro de la computadora y, además, incorporarlo a un proyecto de P.

## Requerimientos

- Tener instalado Python en la PC.

> [!IMPORTANT]
> La versión de Python tiene que ser **3.8 o superior.**
>
> Para verificar la versión instalada, se debe entrar al cmd y escribir en la línea de comandos `python --version`.


Luego de esto, se presentan una serie de pasos sencillos de cómo instalar Sphinx.

## Paso a Paso

### Paso 1: Instalación de Sphinx

Se reitera, en este manual se va a presentar una forma sencilla de cómo instalarlo. 
Para hacerlo, solo se necesita ingresar al símbolo de sistema (cmd) y escribir lo siguiente:

`py -m pip install -r requirements.txt`

### Paso 2: Añadir nuevos archivos (ya sea .md o .py) a un proyecto

Para este momento, ya se debe de tener el Sphinx incorporado por medio del comando ingresado anteriormente.

> [!NOTE]
>Existen varias extensiones que facilitan varios procesos dentro de Sphinx. Se instalan a preferencia. 
>
>En este caso, se usaron `autodoc` y `MyST Markdown`.

En el archivo .py, ingrese a la ruta `docs/source`.
Dentro, deben de estar `index.md` y `conf.py`. El archivo `conf.py` funciona para agregar secciones y subsecciones de un tema.

Es decir:

>- Tema 1
>- Tema 2
>    - Subtema
>    - Subtema
>    - Subtema

Por otro lado, el `index.md` se le puede conocer como el "archvio madre", ya que en este se basa la pantalla principal de la web. Además, su funcionalidad es añadir archivos por aparte sin ningún tipo de ramificación, como "Tema 1" o "Tema 2".

> [!NOTE]
>Es importante aclarar que los `.md` son **únicamente** para la documentación. Por otro lado, los `.py` (sin incluir conf.py), son 
