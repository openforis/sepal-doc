"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup ----------------------------------------------------------------

import os
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.abspath("."))

from _script import environment
from _script import modules

# -- Project information -------------------------------------------------------

project = "SEPAL"
copyright = f"2020-{datetime.now().year}, the SEPAL development team"
author = "Pierrick Rambaud"

# -- General configuration -----------------------------------------------------

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.graphviz",
    "sphinxcontrib.spelling",
    "sphinxcontrib.images",
    "sphinxcontrib.icon",
    "sphinxcontrib.btn",
    "sphinxcontrib.youtube",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx-favicon",
    "notfound.extension",
    "_extentions.line_break",
    "_extentions.custom_edit",
    "_extentions.logos",
]
templates_path = ["_templates"]
exclude_patterns = ["**.ipynb_checkpoints"]
locale_dirs = ["_locale/"]
gettext_compact = False
language = "fr"

# -- Options for HTML output ---------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_last_updated_fmt = ""
html_sidebars = {"index": []}
html_context = {
    "github_user": "openforis",
    "github_repo": "sepal-doc",
    "github_version": "master",
    "doc_path": "docs/source",
    "default_mode": "auto",
}
html_static_path = ["_static"]
html_css_files = ["css/custom.css", "https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"]
html_js_files = ["https://unpkg.com/leaflet@1.7.1/dist/leaflet.js", "js/custom.js"]
html_extra_path = ["browserconfig.xml"]

# -- Option for Latex output ---------------------------------------------------

youtube_cmd = (
    r"\newcommand{\sphinxcontribyoutube}[3]{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}"
    + "\n"
)
vimeo_cmd = (
    r"\newcommand{\sphinxcontribvimeo}[3]{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}"
    + "\n"
)

latex_elements = {"preamble": youtube_cmd + vimeo_cmd}

# -- Option for the pydata-sphinx-theme ----------------------------------------

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
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/OpenForis",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/open-foris/",
            "icon": "fa-brands fa-linkedin",
        },
        {
            "name": "GIS Stackexchange",
            "url": "https://gis.stackexchange.com/questions/tagged/sepal",
            "icon": "fa-brands fa-stack-exchange",
        },
        {
            "name": "Youtube",
            "url": "https://www.youtube.com/channel/UCtpxScciUj0fjMmhpYsAZbA/featured",
            "icon": "fa-brands fa-youtube",
        },
        {
            "name": "Google forum",
            "url": "https://groups.google.com/g/sepal-users",
            "icon": "fa-brands fa-google",
        },
    ],
    "use_edit_page_button": True,
    "footer_items": ["copyright", "sphinx-version", "licence", "map"],
    "left_sidebar_end": ["sidebar-ethical-ads.html"],
}

# -- option for the favicon extention ------------------------------------------

favicons = [
    {
        "rel": "apple-touch-icon",
        "size": "180x180",
        "static-file": "apple-touch-icon.png",
    },
    {
        "rel": "icon",
        "type": "image/png",
        "size": "32x32",
        "static-file": "favicon-32x32.png",
    },
    {
        "rel": "icon",
        "type": "image/png",
        "size": "16x16",
        "static-file": "favicon-16x16.png",
    },
    {"rel": "mask-icon", "static-file": "safari-pinned-tab.svg", "color": "#186691"},
    {"rel": "manifest", "static-file": "/site.webmanifest"},
]

# -- Options for images --------------------------------------------------------

images_config = {"download": False}

# -- spelling options ----------------------------------------------------------

spelling_lang = "en_US"
spelling_show_suggestions = True
spelling_exclude_patterns = ["modules/dwn/*.rst"]
spelling_filters = ["_filters.Names"]
spelling_word_list_filename = [
    str(Path(__file__).expanduser().parent / "_data" / "spelling" / "en_US.txt")
]
spelling_verbose = False

# -- Copy the modules documentation --------------------------------------------

modules.get_index()
modules.get_modules()
modules.get_tags()

# -- copy the requirements of the R and Python environment to data -------------

environment.get_R()
environment.get_python()
