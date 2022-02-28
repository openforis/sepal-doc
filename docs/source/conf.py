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
    'sphinxcontrib.icon',
    'sphinxcontrib.btn',
    'sphinxcontrib.youtube',
    'notfound.extension',
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
html_logo = os.path.abspath('_images/sepal.png') 
html_favicon = os.path.abspath('_images/favicon.ico')
html_last_updated_fmt = ''
html_sidebars = {
    "**": ["search-field", "sidebar-nav-bs"]
}
html_theme_options = {
    "navigation_with_keys": False,
    "show_nav_level": 2,
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
        },
        {
            "name": "Google forum",
            "url": "https://groups.google.com/g/sepal-users",
            "icon": "fab fa-google"
        },
    ],
    "use_edit_page_button": True,
    "footer_items": ["copyright", "sphinx-version", "licence"]
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
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ["css/custom.css"]

# -- Options for images -------------------------------------------------------

images_config = {
    "download": False
}

# -- Copy the modules documentation ------------------------------------------

from urllib.request import urlretrieve
from shutil import copy
import json 

# dirs 
source_dir = Path(__file__).expanduser().parent
module_dir = source_dir/"modules"
dwn_dir = module_dir/"dwn"
template_dir = source_dir/"_templates"

# templates
tag_template = template_dir/"module_tag.rst"
doc_template = template_dir/"no_module.rst"
index_template = template_dir/"index.rst"

# data 
module_json = source_dir/"data"/'modules'/'en.json'
no_module_url = "https://github.com/openforis/sepal-doc/blob/master/docs/source/_templates/no_module.rst"

# flush the modules folder 
[f.unlink() for f in module_dir.glob("*.rst")]

# dst files 
module_index = module_dir/"index.rst"
copy(index_template, module_index)

with module_json.open() as json_file:
    module_list = json.load(json_file)

for name in module_list:
    
    dst = dwn_dir / f'{name}.rst'
    
    file = module_list[name].pop("url", no_module_url)
    if file != no_module_url: 
        urlretrieve (file, dst)
    else:
        copy(doc_template, dst)
        txt = dst.read_text()
        txt = txt.replace("Module_name", name).replace("=", "="*len(name))
        dst.write_text(txt)
        
    with dst.open("a") as f: 
        f.writelines(["", f".. custom-edit:: {file}"])
        
    # create a tag stub file 
    tag = module_list[name].pop("tag", "other")
    tag_file = module_dir/f"{tag}.rst"
    
    if not tag_file.is_file():
        copy(tag_template, tag_file)
        txt = tag_file.read_text()
        txt = txt.replace("module_tag", tag).replace("=", "="*len(tag))
        tag_file.write_text(txt)
        
        with module_index.open("a") as f:
            f.write(f"\n    {tag}")
            
    with tag_file.open('a') as f:
        f.write(f"\n    dwn/{name}")
        
    # prompt for the readthedoc build
    print(f"{name} documentation have been copied to the dwn folder")
    
#  -- copy the requirements of the R and Python environment to data ------------

data_dir = source_dir/"data"

# R environment
print(f"copy R packages from to data folder")
urlretrieve (
    "https://raw.githubusercontent.com/openforis/sepal/master/modules/geospatial-toolkit/script/init_r_packages.sh", 
    data_dir/"r_packages.sh"
)

# Python environment
print(f"copy Python libs from to data folder")
urlretrieve (
    "https://raw.githubusercontent.com/openforis/sepal/master/modules/geospatial-toolkit/config/requirements.txt", 
    data_dir/"python_lib.txt"
)




