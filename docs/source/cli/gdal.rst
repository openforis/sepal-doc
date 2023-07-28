Geospatial Data Abstraction Library
===================================

GDAL is a translator library for raster and vector geospatial data formats that is released under an  `MIT style license <https://gdal.org/license.html#license>`__ by the `Open Source Geospatial Foundation <http://www.osgeo.org/>`__. As a library, it presents a single raster abstract data model and single vector abstract data model to the calling application for all supported formats. It also comes with a variety of useful command-line utilities for data translation and processing. The `News <https://github.com/OSGeo/gdal/blob/v3.4.0/gdal/NEWS.md>`__ page describes the latest release.

.. note::

    The current version available on SEPAL is : :code:`3.4.3`

Available commands
------------------

The complete documentation of GDAL commands can be found on the `GDAL website <https://gdal.org/programs/index.html>`__.

Raster programmes
^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ gdalinfo           # Lists information about a raster dataset.
    $ gdal_translate     # Converts raster data between different formats.
    $ gdaladdo           # Builds or rebuilds overview images.
    $ gdalwarp           # Image reprojection and warping utility.
    $ gdaltindex         # Builds an OGR-supported dataset as a raster tileindex.
    $ gdalbuildvrt       # Builds a VRT from a list of datasets.
    $ gdal_contour       # Builds vector contour lines from a raster elevation model.
    $ gdaldem            # Tools to analyse and visualize DEMs.
    $ rgb2pct.py         # Convert a 24bit RGB image to 8bit paletted.
    $ pct2rgb.py         # Convert an 8bit paletted image to 24bit RGB.
    $ gdalattachpct.py   # Attach a color table to a raster file from an input file.
    $ gdal_merge.py      # Mosaicks a set of images.
    $ gdal2tiles.py      # Generates directory with TMS tiles, KMLs and simple web viewers.
    $ gdal2xyz.py        # Translates a raster file into xyz format.
    $ gdal_rasterize     # Burns vector geometries into a raster.
    $ gdaltransform      # Transforms coordinates.
    $ nearblack          # Converts nearly black/white borders to black.
    $ gdal_retile.py     # Retiles a set of tiles and/or builds tiled pyramid levels.
    $ gdal_grid          # Creates regular grid from scattered data.
    $ gdal_proximity.py  # Produces a raster proximity map.
    $ gdal_polygonize.py # Produces a polygon feature layer from a raster.
    $ gdal_sieve.py      # Removes small raster polygons.
    $ gdal_fillnodata.py # Fills raster regions by interpolation from edges.
    $ gdallocationinfo   # Raster query tool.
    $ gdalsrsinfo        # Lists info about a given SRS in a number of formats (WKT, PROJ.4, etc.).
    $ gdalmove.py        # Transforms georeferencing of raster file in place.
    $ gdal_edit.py       # Edit in place various information of an existing GDAL dataset.
    $ gdal_calc.py       # Command-line raster calculator with NumPy syntax.
    $ gdal_pansharpen.py # Performs a pansharpen operation.
    $ gdal-config (Unix) # Determines various information about a GDAL installation.
    $ gdalmanage         # Identifies, deletes, renames and copies raster data files.
    $ gdalcompare.py     # Compares two images.
    $ gdal_viewshed      # Computes a visibility mask for a raster.
    $ gdal_create        # Creates a raster file (without source dataset).

Multidimensional raster programmes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ gdalmdiminfo      # Reports structure and content of a multidimensional dataset.
    $ gdalmdimtranslate # Converts multidimensional data between different formats and performs subsetting.

Vector programmes
^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ ogrinfo     # Lists information about an OGR-supported data source.
    $ ogr2ogr     # Converts simple feature data between file formats.
    $ ogrtindex   # Creates a tileindex.
    $ ogrlineref  # Creates linear reference and provides some calculations using it.
    $ ogrmerge.py # Merges several vector datasets into a single one.

Geographic network programmes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ gnmmanage  # Manages networks
    $ gnmanalyse # Analyses networks
