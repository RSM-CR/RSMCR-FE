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
>Es importante aclarar que los `.md` son **únicamente** para la documentación. Por otro lado, los `.py` (sin incluir conf.py), son propios del proyecto que se está desarrollando por fuera de Sphinx.

#### Cómo vincular un **.py** a Sphinx

1. Se debe de crear el archivo `.py` por fuera de la carpeta `/docs`.
2. Dentro de `conf.py`, debe de aparecer una sección llamada `autodoc2_packages`. En esa lista se ingresan los archivos que se desea que aparezcan dentro de la web. En caso de que los archivos estén dentro de una carpeta previamente creada, se tiene que ingresar el directorio.

#### Cómo vincular un **.md** a Sphinx

1. Se crea un archivo `.md` dentro del directorio `/docs/source`.
2. Dentro de `index.md`, es posible que ya esté creado de forma predeterminada una lista `toctree`, en caso de no estarlo se debe añadir. Ahí se agrega **único y exclusivamente** el nombre del archivo sin su extensión (.md).

### Paso 3: Documentación dentro de archivos .py

El texto básico de documentación para Sphinx se crea por medio de un texto entre triples comillas dobles:

`"""Esto es un texto que comenta un código."""`

Para una mejor organización y más detalles de tipados de texto, se recomienda ingresar a la siguiente página web:

[Basic Syntax | Markdown Guide (Click Aquí)](https://www.markdownguide.org/basic-syntax/)


### Paso 4: Compilación y visualización

1. Para poder "guardar" los cambios se necesita ingresar el siguiente comando dentro de la terminal:

`py -m sphinx.cmd.build -b html .\docs\source .\docs\build`

2. Luego, para ver la página web, se necesita entrar al directorio `/docs/build/index.html`.
3. Al entrar a `index.html`, se debe ejecutar el programa para que se abra dentro de un navegador.
