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
    'notfound.extension',
    '_extentions.video',
    '_extentions.line_break',
    '_extentions.custom_edit'
]

# spelling options
spelling_lang='en_US'
spelling_show_suggestions=True
spelling_exclude_patterns=['modules/dwn/*.rst']
spelling_filters = ['_filters.Names']
spelling_word_list_filename=[str(Path(__file__).expanduser().parent.joinpath('data', 'spelling', 'en_US.txt'))]
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
html_logo = os.path.abspath('img/sepal.png') 
html_favicon = os.path.abspath('img/favicon.ico')
html_last_updated_fmt = ''
html_sidebars = {
    "**": ["search-field", "sidebar-nav-bs"]
}
html_theme_options = {
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
            "name": "GIS Stackexchange",
            "url": "https://gis.stackexchange.com/questions/tagged/sepal",
            "icon": "fab fa-stack-exchange"
        },
        {
            "name": "Youtube",
            "url": "https://www.youtube.com/channel/UCtpxScciUj0fjMmhpYsAZbA/featured",
            "icon": "fab fa-youtube"
        }
    ],
    "use_edit_page_button": True,
}

html_context = {
    "github_user": "openforis",
    "github_repo": "sepal-doc",
    "github_version": "master",
    "doc_path": "docs/source",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ['css/custom.css']

# -- Options for images-------------------------------------------------------

images_config = {
    "download": False
}

# -- Copy the modules documentation ------------------------------------------

from urllib.request import urlretrieve
import json 

module_dir = Path(__file__).expanduser().parent.joinpath('data', 'modules')
dwn_dir = Path(__file__).expanduser().parent.joinpath('modules', 'dwn')

with module_dir.joinpath('en.json').open() as json_file:
    module_doc = json.load(json_file)

for name in module_doc:
    dst = dwn_dir / f'{name}.rst'
    
    urlretrieve (module_doc[name], dst)
    
    with dst.open("a") as f: 
        f.writelines(["", f".. custom-edit:: {module_doc[name]}"])
                      
    # prompt for the readthedoc build
    print(f"{name} documentation have been copied to the dwn folder")

