SEPAL environment
=================

CLI tools
---------

SEPAL platform includes a variety of useful Command Line Interface utilities to help resolve specific problems, some of them are listed below:
    
-   gdal
-   gdrive
-   gee
-   gwb
-   ofgt
-   otb
    
These tools can be called directly from the terminal or any programming language sending commands to the kernel including R and Python (installed by default on any SEPAL account).

.. thumbnail:: ../_images/cli/index/cli_gdalinfo.gif
    :title: How to use the gdalinfo command in a SEPAL terminal
    
.. note::

    the code executed previously on an existing :code:`example.tif` file.

    .. code-block:: console
        
        gdalinfo example.tif

coding tools
------------

In the app section, you'll find at the top of the list 3 coding tools: 

-   JupyterLab 
-   JupyterNotebook
-   Rstudio

.. thumbnail:: ../_images/cli/index/code_editor.png
    :title: the 3 code editor built-in in the SEPAL environment

They will allow the user to code wokflows in any of the available languages using the coresponding environment built-in in SEPAL. These environments are fully customizables, click on the :code:`Python` or :code:`R` section to know more. 

.. thumbnail:: ../_images/cli/index/jupyter_example.png
    :title: Example of rastreio code running in SEPAL JupyterLab (code extracted from raterio documnetation: https://rasterio.readthedocs.io/en/latest/topics/plotting.html)

.. toctree::
    :hidden:
    :maxdepth: 1

    gdal
    gdrive
    gee
    gwb
    ofgt
    otb
    python
    r