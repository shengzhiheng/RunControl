# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SBC Run Control'
copyright = '2024-2025 SBC'
author = 'Zhiheng Sheng'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

# fake install packages not available in conda/pip
autodoc_mock_imports = [
    "red_caen",     # or whatever the name is for the Python extension that depends on CAENComm
    "CAENComm",     # if you import it in Python
    "CAENDigitizer",
    "CAENVME",
    "CAENUSB",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

root_doc = 'index'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
