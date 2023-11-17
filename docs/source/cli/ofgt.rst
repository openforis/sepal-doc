OFGT
====

The **Open Foris Geospatial Toolkit (OFGT)** is a collection of prototype command-line utilities for processing geographical data. The tools can be divided into stand-alone programmes and scripts. They have been tested mainly in the Ubuntu Linux environment, although they can be used with other Linux distros, macOS, and Microsoft Windows (Cywgin) as well. Most of the stand-alone programmes use **GDAL libraries** and many of the scripts rely heavily on **GDAL command-line utilities**.

The **OFGT** project started under the Open Foris initiative in an effort to develop, share and support software tools and methods for multipurpose forest assessment, monitoring and reporting (see `Open Foris <http://openforis.org>`__.

The Open Foris initiative develops and supports innovative, easy-to-use tools needed to produce reliable, up-to-date information on the state of forest resources and their uses.

The command-line tools aim to simplify the complex process of transforming raw satellite imagery for automatic image processing to produce valuable information. These tools contain radiometric harmonization, image segmentation and image arithmetic, as well as image statistics, feature extraction and other image processing analysis.

.. note::

    The current version available in SEPAL is :code:`1.25.4`

Available commands
------------------

The complete documentation of the **OFGT** commands can be found in the `OFGT manual <https://www.openforis.org/fileadmin/user_upload/Geospatial_Toolkit/OFGT_usermanual.pdf>`__.


General tools
^^^^^^^^^^^^^

.. code-block:: console

    $ CsvToPolygon.py              # Creates shapefile polygons from a text file.
    $ genericCsvToPolygon.py       # Creates polygons from text files.
    $ genericGEkml2csv.bash        # Converts separate KML files into one CSV file.
    $ GExml2csv.bash               # Converts XML files from the GEE training data collection tool into one .csv file.
    $ oft-addattr.py               # Adds one integer attribute in a shape file.
    $ oft-addpct.py                # Adds pseudo color table to an image.
    $ oft-admin-mask.bash          # Prepares a mask of administrative areas within a satellite image.
    $ oft-bb                       # Is a Bounding Box calculator t.
    $ oft-classvalues-compare.bash # Creates comparison plots of classes based on results of previous script oft-classvalues-plot.bash.
    $ oft-classvalues-plot.bash    # Creates scatterplots of pixels within training classes.
    $ oft-combine-masks.bash       # Combines several masks into one mask file.
    $ oft-compare-overlap.bash     # Compares overlapping areas of two images and produces between-band correlations.
    $ oft-crop.bash                # Crops a raster image to the extent of a certain pixel value.
    $ oft-cuttile.pl               # Cuts image tiles on the basis of a given list of locations.
    $ oft-filter                   # Moving window filters.
    $ oft-gengrid.bash             # Generates a systematic grid over a raster image.
    $ oft-getcorners.bash          # Retrieves coordinates of corners of a raster image or OGR vector layer.
    $ oft-polygonize.bash          # A wrapper for gdal_polygonize.
    $ oft-sample-within-polys.bash # Samples pixels within polygons and generates training data for knn.
    $ oft-shptif.bash              # Rasterizes a shapefile to the resolution of a reference image.
    $ oft-sigshp.bash              # Creates a signature file of an image based on training area polygons.
    $ PointsToSquares.py           # Converts XY-locations into 100 m x 100 m squares in a .kml file.

Image manipulation
^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ multifillerThermal.bash      # Utilizes several Landsat scenes to build a multitemporal image composite using the warmest pixel method.
    $ oft-calc                     # Raster image calculator.
    $ oft-chdet.bash               # Automated change detection.
    $ oft-clip.pl                  # Subsets an input image using the extent, pixel size and projection of a reference image.
    $ oft-combine-images.bash      # Combines two images into one.
    $ oft-gapfill                  # Regression-based gap and cloud filler.
    $ oft-ndvi.bash                # Computes NDVI images.
    $ oft-prepare-images-for-gapfill.bash # Prepares images and masks for oft-gapfill.
    $ oft-reclass                  # A reclassification program.
    $ oft-shrink                   # To be combined with oft-trim.
    $ oft-stack                    # Creates a multiband image stack.
    $ oft-trim                     # Erosion filter producing binary output.
    $ oft-trim-maks.bash           # Makes a 0/1 mask of a 6- or 7-band Landsat image.

Statistics
^^^^^^^^^^

.. code-block:: console

    $ oft-ascstat.awk              # Computes basic statistics for a space-separated text file.
    $ oft-avg                      # Computes zone/segment averages and standard deviations.
    $ oft-countpix.pl              # Counts number of pixels with, below or above a specific value.
    $ oft-crossvalidate            # Computes RMSE and bias estimates for knn via leave-one-out cross-validation.
    $ oft-extr                     # Extracts pixel values from an image into a text file.
    $ oft-his                      # Computes image histogram by segments.
    $ oft-mm                       # Computes minimum and maximum values for each band of the input file.
    $ oft-segstat                  # Output segments shape and spectral statistics in a text file.
    $ oft-stat                     # Computes segment statistics in a text file.

Classification
^^^^^^^^^^^^^^

.. code-block:: console

    $ oft-cluster.bash             # Clusters raster images.
    $ oft-kmeans                   # For k-means clustering.
    $ oft-nn                       # Nearest neighbor classifier.
    $ oft-nn-training-data.bash    # Prepares a training data text file for oft-nn analysis.
    $ oft-normalize.bash           # Prepares a training data text file for oft-nn analysis.
    $ oft-prepare-image-for-nn.bash # Prepares a Landsat image for nn-analysis with oft-nn.
    $ oft-unique-mask-for-nn.bash  # Creates a unique mask for oft-nn analysis.

Segmentation
^^^^^^^^^^^^

.. code-block:: console

    $ oft-clump                    # Connected component labeling.
    $ oft-seg                      # Image segmentation tool.

Projection
^^^^^^^^^^

.. code-block:: console

    $ oft-getproj.bash             # Fetches projection definition files for UTM zones.
