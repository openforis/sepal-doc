# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime
from pathlib import Path
sys.path.insert(0, os.path.abspath('.'))

from _script import environment
from _script import modules


# -- Project information -----------------------------------------------------

project = 'SEPAL'
copyright = f"2020-{datetime.now().year}, the SEPAL development team"
author = 'Pierrick Rambaud'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.graphviz',
    'sphinxcontrib.spelling',
    'sphinxcontrib.images',
    'sphinxcontrib.icon',
    'sphinxcontrib.btn',
    'sphinxcontrib.youtube',
    'sphinx_design',
    'sphinx_togglebutton',
    'notfound.extension',
    '_extentions.line_break',
    '_extentions.custom_edit',
    '_extentions.logos',
]

# spelling options
spelling_lang='en_US'
spelling_show_suggestions=True
spelling_exclude_patterns=['modules/dwn/*.rst']
spelling_filters = ['_filters.Names']
spelling_word_list_filename=[str(Path(__file__).expanduser().parent/'_data'/'spelling'/'en_US.txt')]
spelling_verbose = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["**.ipynb_checkpoints"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_favicon = os.path.abspath('_images/favicon.ico')
html_last_updated_fmt = ''
html_sidebars = {"index": []}
html_theme_options = {
    "logo": {
        "image_light": "sepal_light.png",
        "image_dark": "sepal_dark.png",
    },
    "header_links_before_dropdown": 7,
    "navigation_with_keys": False,
    "show_nav_level": 1,
    "show_prev_next": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/openforis/sepal",
            "icon": "fab fa-github"
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/OpenForis",
            "icon": "fab fa-twitter"
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/open-foris/",
            "icon": "fab fa-linkedin"
        },
        {
            "name": "GIS Stackexchange",
            "url": "https://gis.stackexchange.com/questions/tagged/sepal",
            "icon": "fab fa-stack-exchange"
        },
        {
            "name": "Youtube",
            "url": "https://www.youtube.com/channel/UCtpxScciUj0fjMmhpYsAZbA/featured",
            "icon": "fab fa-youtube"
        },
        {
            "name": "Google forum",
            "url": "https://groups.google.com/g/sepal-users",
            "icon": "fab fa-google"
        },
    ],
    "use_edit_page_button": True,
    "footer_items": ["copyright", "sphinx-version", "licence", "map"]
}

html_context = {
    "github_user": "openforis",
    "github_repo": "sepal-doc",
    "github_version": "master",
    "doc_path": "docs/source",
    "default_mode": "auto",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "css/custom.css",
    "https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
]

html_js_files = [
    "https://unpkg.com/leaflet@1.7.1/dist/leaflet.js",
    "js/custom.js"
]


# -- Options for images -------------------------------------------------------

images_config = {
    "download": False
}

# -- Copy the modules documentation ------------------------------------------

modules.get_index()
modules.get_modules()
modules.get_tags()
    
#  -- copy the requirements of the R and Python environment to data ------------

environment.get_R()
environment.get_python()

# -- Option for Latex output ---------------------------------------------------

# create a custom sphinx output for the youtube and vimeo video
youtube_cmd = r"\newcommand{\sphinxcontribyoutube}[3]{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}" + "\n"
vimeo_cmd = r"\newcommand{\sphinxcontribvimeo}[3]{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}" + "\n"

latex_elements = {"preamble": youtube_cmd + vimeo_cmd}
