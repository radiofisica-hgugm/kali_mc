# Configuration file for the Sphinx documentation builder.
import sys, os

# -- Project information

project = "Kali MC"
copyright = "2024, Servicio de Dosimetría y Radioprotección , Hospital General Universitario Gregorio Marañón"
author = "Rafael Ayala"

release = "1.3"
version = "1.3.1"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.bibtex",
]

sys.path.insert(0, os.path.abspath(os.path.join("..", "..")))
add_module_names = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

html_logo = "kali_mc.svg"
html_theme_options = {
    "logo_only": False,
    "display_version": True,
}

# -- Options for EPUB output
epub_show_urls = "footnote"

bibtex_bibfiles = [
    "references.bib",
]
