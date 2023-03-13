Open Foris Geospatial Toolkit
=============================

OFGT - Open Foris Geospatial Toolkit is a a collection of prototype command-line utilities for processing of geographical data. The tools can be divided into stand-alone programs and scripts and they have been tested mainly in Ubuntu Linux environment although can be used with other linux distros, Mac OS, and MS Windows (Cywgin) as well. Most of the stand-alone programs use GDAL libraries and many of the scripts rely heavily on GDAL command-line utilities.

The OFGT project started under the Open Foris Initiative to develop, share and support software tools and methods for multi-purpose forest assessment, monitoring and reporting http://openforis.org. The Initiative develops and supports innovative, easy-to-use tools needed to produce reliable, timely information on the state of forest resources and their uses. The command-line tools aim to simplify the complex process of transforming raw satellite imagery for automatic image processing to produce valuable information. These tools contain radiometric harmonization, image segmentation and image arithmetic, as well as image statistics, feature extraction and other image processing analysis.

.. note::

    The current version availalble on SEPAL is : :code:`1.25.4`

available commands
------------------

The complete documentation of the GDAL commands can be found on the `OFGT manual <https://www.openforis.org/fileadmin/user_upload/Geospatial_Toolkit/OFGT_usermanual.pdf>`__.


General Tools
^^^^^^^^^^^^^

.. code-block:: console

    $ CsvToPolygon.py              # creates shapefile polygons from a text file.
    $ genericCsvToPolygon.py       # creating polygons from text files
    $ genericGEkml2csv.bash        # converts separate kml files into one CSV file
    $ GExml2csv.bash               # converts xml files from Google Earth training data collection tool into one CSV file
    $ oft-addattr.py               # adds one integer attribute in a shape file
    $ oft-addpct.py                # adds pseudo color table to an image
    $ oft-admin-mask.bash          # prepares a mask of administrative areas within a satellite image
    $ oft-bb                       # is a a bounding box calculator t
    $ oft-classvalues-compare.bash # creates comparison plots of classes based on result of previous script oft-classvalues-plot.bash.
    $ oft-classvalues-plot.bash    # creates scatterplots of pixels within training classes
    $ oft-combine-masks.bash       # combines several masks to one mask file
    $ oft-compare-overlap.bash     # compares overlapping areas of 2 images and produces between-band correlations
    $ oft-crop.bash                # crops a raster image to the extent of a certain pixel value
    $ oft-cuttile.pl               # Cuts image tiles on the basis of a given list of locations
    $ oft-filter                   # moving window filters
    $ oft-gengrid.bash             # generates a systematic grid over a raster image
    $ oft-getcorners.bash          # gets the coordinates of corners of a raster image or OGR vector layer
    $ oft-polygonize.bash          # a wrapper for gdal_polygonize
    $ oft-sample-within-polys.bash # samples pixels within polygons and generates training data for knn
    $ oft-shptif.bash              # Rasterizes a shapefile to the resolution of a reference image
    $ oft-sigshp.bash              # creates a signature file of an image based on training area polygons
    $ PointsToSquares.py           # converts XY-locations into 100 x 100 m squares in a kml-file

Image Manipulation
^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ multifillerThermal.bash      # utilizes several Landsat scenes to build a multi-temporal image composite using the warmest pixel -method
    $ oft-calc                     # raster image calculator
    $ oft-chdet.bash               # automated change detection
    $ oft-clip.pl                  # subsets an input image using the extent, pixels size and projection of a reference image
    $ oft-combine-images.bash      # combines 2 images into one
    $ oft-gapfill                  # regression based gap and cloud filler
    $ oft-ndvi.bash                # computes ndvi images
    $ oft-prepare-images-for-gapfill.bash # prepares images and masks for oft-gapfill
    $ oft-reclass                  # a reclassification program
    $ oft-shrink                   # to be combined with oft-trim
    $ oft-stack                    # Create a multi-band image stack
    $ oft-trim                     # erosion filter producing binary output
    $ oft-trim-maks.bash           # This script makes a 0/1 mask of a 6 or 7 band (Landsat) image

Statistics
^^^^^^^^^^

.. code-block:: console

    $ oft-ascstat.awk              # computes basic statistics for a space separated text file
    $ oft-avg                      # computes zone/segment averages and standard deviations
    $ oft-countpix.pl              # counts number of pixel with, below or above a specific value
    $ oft-crossvalidate            # computes RMSE and bias estimates for knn via leave-one-out cross-validation
    $ oft-extr                     # extracts pixel values from an image into a text file
    $ oft-his                      # computes image histogram by segments
    $ oft-mm                       # computes minimum and maximum values for each band of the input file
    $ oft-segstat                  # output segments shape and spectral statistics in a text file
    $ oft-stat                     # computes segment statistics in a text file

Classification
^^^^^^^^^^^^^^

.. code-block:: console

    $ oft-cluster.bash             # clusters raster images
    $ oft-kmeans                   # for kmeans clustering
    $ oft-nn                       # is a nearest neighbor classifier
    $ oft-nn-training-data.bash    # prepare a training data text file for oft-nn analysis
    $ oft-normalize.bash           # prepare a training data text file for oft-nn analysis
    $ oft-prepare-image-for-nn.bash # prepare a Landsat image for nn-analysis with oft-nn
    $ oft-unique-mask-for-nn.bash  # creates a unique mask for oft-nn analysis

Segmentation
^^^^^^^^^^^^

.. code-block:: console

    $ oft-clump                    # connected component labeling
    $ oft-seg                      # Image segmentation tool

Projection
^^^^^^^^^^

.. code-block:: console

    $ oft-getproj.bash             # fetches projection definition files for UTM zones
