SEPAL environment
=================

CLI tools
---------

The SEPAL platform includes a variety of useful command-line interface (CLI) utilities to help resolve specific problems, including, but not limited to:

-   Geospatial Data Abstraction Library (GDAL)
-   Google Drive (Drive)
-   Google Earth Engine (GEE)
-   GuidosToolbox Workbench (GWB)
-   Open Foris Geospatial Toolkit (OFGT)
-   Orfeo Toolbox (OTB)

These tools can be called directly from the terminal or any programming language sending commands to the kernel, including R and Python (installed by default on any SEPAL account).

.. thumbnail:: ../_images/cli/index/cli_gdalinfo.gif
    :title: How to use the gdalinfo command in a SEPAL terminal

.. note::

    The code executed previously on an existing :code:`example.tif` file.

    .. code-block:: console

        gdalinfo example.tif

.. tip::

    If you're running actions from multiple directories or instances, you can open multiple terminal tabs and name them as you see fit.

.. tip::

    If the code you want to execute is taking time, please consider running it in the background using :code:`nohup`.

    .. code-block:: console

        nohup gdalinfo example.tif

    All the console outputs will be redirected to a :code:`nohup.out` in your home directory, but the execution will be running in the background. Thus, you will be able to safely close the terminal or even the browser window without killing your process (for more information about :code:`nohup`, see `here <https://en.wikipedia.org/wiki/Nohup>`__.


Coding tools
------------

In the **App** section, you'll find three coding tools at the top of the list:

-   JupyterLab
-   JupyterNotebook
-   RStudio

.. thumbnail:: ../_images/cli/index/code_editor.png
    :title: The three code editor in the SEPAL environment

They will allow the user to code wokflows in any of the available languages using the coresponding environment in SEPAL. These environments are fully customizable (select the :code:`Python` or :code:`R` section to know more).

.. thumbnail:: ../_images/cli/index/jupyter_example.png
    :title: Example of rasterio code running in SEPAL JupyterLab (code extracted from rasterio documentation: https://rasterio.readthedocs.io/en/latest/topics/plotting.html)

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
