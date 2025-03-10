import os, sys, subprocess

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SBC Run Control'
copyright = '2024-2025 SBC Collaboration'
author = 'Zhiheng Sheng'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    "myst_parser",
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

root_doc = 'index'

# Set each section is a chapter in pdf file
latex_toplevel_sectioning = 'chapter'

sys.path.insert(0, os.path.abspath(".."))
print("Current sys.path:", sys.path)

# Generate .py files from .ui files
ui_dir = os.path.abspath("../ui") 
for ui_file in os.listdir(ui_dir):
    if ui_file.endswith(".ui"):
        ui_path = os.path.join(ui_dir, ui_file)
        py_file = os.path.splitext(ui_file)[0] + ".py"
        py_path = os.path.join(ui_dir, py_file)
        
        # Run pyside6-uic
        try:
            subprocess.run(
                ["pyside6-uic", ui_path, "-o", py_path],
                check=True
            )
            print(f"Successfully generated: {py_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error generating {py_path}: {e}")

# Remove blank pages in pdf file
latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

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
