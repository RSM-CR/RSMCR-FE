# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import subprocess, sys
from pathlib import Path

project = 'GXBridge'
copyright = 'RSM Costa Rica'
author = 'Especialidades de IA y Apps del CTP CIT'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'autodoc2']

templates_path = ['_templates']
exclude_patterns = ['../../docs/*']

myst_enable_extensions = ['fieldlist', 'alert', 'colon_fence']

language = 'es'

subprocess.run([sys.executable, "extraer_svelte.py"], check=True)



# -- Autodoc2 configuration ---------------------------------------------------
# https://sphinx-autodoc2.readthedocs.io/en/latest/config.html
autodoc2_class_docstring = "both"
# Lista de archivos a documentar
autodoc2_packages = [
    "../../abstracciones/destino.py",
    "../../abstracciones/fuente.py",
    "../../xero/auth.py",
    "../../servidor/configurar.py",
    "../../servidor/secretos.py"
    "../../Capa.py",
    "../../factura.py",
    "../../var_a_xml.py"
]

# Procesa todo como Markdown en vez de como .rst
autodoc2_docstring_parser_regexes = [
    (r".*", "myst"),
    (r"autodoc2\..*", "myst"),
]
autodoc2_index_template = """Referencia de la API
====================

Está página contiene la documentación de las APIs disponibles en GXBridge. Esto se genera en base a los comentarions colocados dentro del código a través de `sphinx-autodoc2 <https://github.com/chrisjsewell/sphinx-autodoc2>`_.

.. toctree::
    :titlesonly:
{% for package in top_level %}
    {{ package }}
{%- endfor %}

.."""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
