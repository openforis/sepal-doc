CLI tools
=========


SEPAL platform includes a variety of useful Command Line Interface utilities to help resolve specific problems, some of them are listed below

.. toctree::
    :maxdepth: 1
    
    gdal
    gdrive
    gee
    gwb
    ofgt
    otb
    
These tools can be called directly from the terminal or any programming language sending commands to the kernel including R and Python (installed by default on any SEPAL account).

.. thumbnail:: ../_images/cli/index/cli_gdalinfo.gif
    :title: How to use the gdalinfo command in a SEPAL terminal
    
.. note::

    the code executed previously on an existing :code:`example.tif` file.

    .. code-block:: console
        
        gdalinfo example.tif