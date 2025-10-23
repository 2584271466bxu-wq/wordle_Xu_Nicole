import os, sys
sys.path.insert(0, os.path.abspath("../src"))

project = "wordle_yx3010"
author = "Nicole"
release = "0.1.0"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

html_theme = "furo"
