import os
import sys
from importlib.metadata import version as _version

sys.path.insert(0, os.path.abspath(".."))

project = "TeleAsync"
author = "kazaryanarmen"
copyright = "2026, kazaryanarmen"
release = _version("teleasync")

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "myst_parser",
]

source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
master_doc = "index"
language = "en"

autosummary_generate = True
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}
always_document_param_types = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

myst_enable_extensions = ["colon_fence", "deflist"]

html_theme = "furo"
html_static_path = ["_static"]
html_title = f"{project} {release}"