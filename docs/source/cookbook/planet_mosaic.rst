Planet mosaic
=============

Overview
--------

A mosaic is a process of combining spatially overlapping images into an individual image. In the SEPAL platform, you can create a composite dataset from Planet images taken at different times by using different techniques. For example, you can choose to keep only the pixel value from the first or last image, or combine the values of the overlapping pixels using a weighting algorithm, the average, or the maximum or minimum value. In addition, certain preprocessing tasks can be applied to mask clouds, shadows, snow, etc. These operations are complex and repetitive. SEPAL offers an interactive and intuitive way to create Planet mosaics within any area of interest (AOI).

.. thumbnail:: ../_images/cookbook/planet_mosaic/time-series.png
    :group: planet-mosaic-recipe
    :title: A time series of Planet imagery ready to be mosaiced

.. attention::

    You won't be able to retrieve images if your SEPAL and Google Earth Engine (GEE) accounts are not connected (see `Connect SEPAL to GEE <../setup/gee.html>`__).

    You also need to connect your GEE account with Planet (see `Use NICFI - Planet Lab data <../setup/nicfi.html>`__).

Start
-----

Once the :code:`Planet mosaic` recipe is selected, SEPAL will show the recipe process in a new tab (1) and the AOI selection window will appear in the lower right (2).

.. thumbnail:: ../_images/cookbook/planet_mosaic/landing.png
    :group: planet-mosaic-recipe
    :title: The landing page of the Planet mosaic recipe

The first step is to change the name of the recipe, which will be used to name your files and recipes in the SEPAL folders.

Double-click the tab and enter a new name (it will default to :code:`Planet_mosaic_<start_date>_<end_date>`).

.. thumbnail:: ../_images/cookbook/planet_mosaic/default_title.png
    :title: Planet mosaics default title
    :width: 49%

.. thumbnail:: ../_images/cookbook/planet_mosaic/modified_title.png
    :title: Planet mosaics modified title
    :width: 49%

.. tip::

    The SEPAL team recommends using the following naming convention: :code:`<aoi name>_<dates>_<measure>`.

Parameters
----------

In the lower right, four tabs are available, allowing you to customize the planet mosaic to your needs.

-   :guilabel:`AOI`: Area of interest (AOI)
-   :guilabel:`DAT`: Dates of time series
-   :guilabel:`SRC`: Time series dataset source
-   :guilabel:`OPT`: Filtering options

.. thumbnail:: ../_images/cookbook/planet_mosaic/no_parameters.png
    :title: The four tabs to identify SEPAL Planet mosaic parameters
    :group: planet-mosaic-recipe

AOI selection
^^^^^^^^^^^^^

The data exported by the recipe will be cut to the bounds of the AOI.

There are multiple ways to select the AOI in SEPAL:

-   administrative boundaries
-   EE Tables
-   drawn polygons

These are extensively described in our documentation (see :doc:`../feature/aoi_selector`).

.. thumbnail:: ../_images/cookbook/planet_mosaic/aoi.png
    :title: Select AOI based on administrative layers
    :group: planet-mosaic-recipe

Date
^^^^

In the :guilabel:`DAT` tab, select the dates of the time series used to build the composited image (i.e. start date and end date).

.. thumbnail:: ../_images/cookbook/planet_mosaic/date.png
    :title: Date selection window
    :group: planet-mosaic-recipe

Select :btn:`<fa-solid fa-calendar-days>` to choose your date.

.. thumbnail:: ../_images/cookbook/planet_mosaic/date_picker.png
    :title: The SEPAL date selector for the Planet mosaic tool
    :group: planet-mosaic-recipe

Then, select the :btn:`<fa-solid fa-chevron-right> Next` button.

Sources
^^^^^^^

SEPAL can use multiple data sources to create your mosaics/composites, as long as they are Planet-related datasets.

Three options are available:

-   :guilabel:`NICFI basemaps`
-   :guilabel:`Custom basemaps`
-   :guilabel:`Daily imagery`

Select :btn:`<fa-solid fa-check> Done` to finish the process.

NICFI basemaps
""""""""""""""

The NICFI basemap uses Level 1 NICFI data provided by SEPAL.

.. note::

    Since the data provided consists of monthly mosaics, your time range needs to be longer than one month (otherwise, only one image will be used).

.. thumbnail:: ../_images/cookbook/planet_mosaic/sources.png
    :title: Different sources available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Custom basemaps
"""""""""""""""

You can provide a custom :code:`ImageCollection` Planet asset (such as NICFI Level 1 data provided to registered users).

.. thumbnail:: ../_images/cookbook/planet_mosaic/sources_custom.png
    :title: Different sources available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Daily imagery
"""""""""""""

.. attention::

    Only users with access to NICFI Level 2 data can use this option.

Choose this option to provide custom Planet daily :code:`ImageCollection` imagery.

.. thumbnail:: ../_images/cookbook/planet_mosaic/sources_level_2.png
    :title: Different sources available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Options
^^^^^^^

.. note::

    This step is not mandatory since Planet mosaics are already sanitized.

SEPAL provides options to customize images used to create the compositing mosaic; the selected parameter will be automatically applied to the analysis.

Select the :btn:`<fa-solid fa-xmark> Close` button to complete customization.

.. thumbnail:: ../_images/cookbook/planet_mosaic/options.png
    :title: Three options available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Cloud masking
"""""""""""""

Planet composites already remove clouds. Setting this parameter to a value greater than zero (0) will remove additional clouds using a GEE algorithm.

Shadow masking
""""""""""""""

Planet composites already remove shadows. Setting this parameter to a greater value than zero (0) will remove additional shadows using a GEE algorithm.

Cloud buffering
"""""""""""""""

-   :guilabel:`none`: Only mask clouds. It might leave hazy pixels around masked clouds but will minimize the amount of masked pixels in the mosaic.
-   :guilabel:`moderate`: Mask an additional 120 m around each larger cloud. This helps prevent hazy pixels at the border of clouds from being included in the mosaic.
-   :guilabel:`aggressive`: Mask an additional 600 m around each larger cloud. This helps prevent hazy pixels at the borders of clouds from being included in the mosaic.

Analysis
--------

Once all of the parameters have been set, the mosaic will be rendered on the fly. Multiple color combinations can be displayed (see the following figures).

.. thumbnail:: ../_images/cookbook/planet_mosaic/mosaic_rgb.png
    :title: Displayed on-the-fly rendered mosaic using red, blue and green bands
    :group: planet-mosaic-recipe
    :width: 49%

.. thumbnail:: ../_images/cookbook/planet_mosaic/mosaic_nrg.png
    :title: Displayed on-the-fly rendered mosaic using nir, red, and green bands
    :group: planet-mosaic-recipe
    :width: 49%

.. thumbnail:: ../_images/cookbook/planet_mosaic/mosaic_ndvi.png
    :title: Displayed on-the-fly rendered mosaic using NDVI in false colors
    :group: planet-mosaic-recipe
    :width: 49%

.. thumbnail:: ../_images/cookbook/planet_mosaic/mosaic_savi.png
    :title: Displayed on-the-fly rendered mosaic using SAVI in false colors
    :group: planet-mosaic-recipe
    :width: 49%

Retrieve
--------

.. important::

    You cannot export a recipe as an asset or a :code:`.tiff` file without a small computation quota (if you are a new user, see :doc:`../setup/resource`).

Select the :btn:`<fa-solid fa-cloud-arrow-down>` tab, which will display the **Retrieve** panel, where you can select which bands or indexes to download, as well as specify the output scale and destination.

.. thumbnail:: ../_images/cookbook/planet_mosaic/retrieve.png
    :title: The last panel of the Planet mosaic: exportation
    :group: planet-mosaic-recipe

Bands
^^^^^

Select the band(s) to export in the mosaic. There is no maximum number; however, exporting useless bands will increase the size and time of the output.

.. tip::

    There is no fixed rule to band selection. Every index will be more useful to the type of analysis you are performing. The knowledge of the study area, evolution expected, and careful selection of an adapted band combination will improve the quality of downstream analysis.

Raw bands
"""""""""

-   :guilabel:`blue`: blue
-   :guilabel:`green`: green
-   :guilabel:`red`: red
-   :guilabel:`nir`: near infrared


Indexes
"""""""

-   :guilabel:`NDVI`: `Normalized difference vegetation index <https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index>`__
-   :guilabel:`NDMI`: `Normalized difference moisture index <http://dx.doi.org/10.1016/S0034-4257(01)00318-2>`__
-   :guilabel:`NDWI`: `Normalized difference water index <https://en.wikipedia.org/wiki/Normalized_difference_water_index>`__
-   :guilabel:`EVI`: `Enhanced vegetation index <doi:10.1016/S0034-4257(02)00096-2>`__
-   :guilabel:`EVI2`: Two-band EVI (Enhanced vegetation index)
-   :guilabel:`SAVI`: `Soil-adjusted vegetation index <http://dx.doi.org/10.1016/0034-4257(88)90106-X>`__

Scale
^^^^^

You can set a custom scale for exportation by changing the value in the :code:`Scale` field. Requesting a smaller resolution than the image's native resolution will not improve the quality of the output, only its size (note: PlanetLab data's native resolution is 3.0 m – 4.1 m [altitude-dependent ground sample distance; `see more info <https://assets.planet.com/docs/Planet_Combined_Imagery_Product_Specs_letter_screen.pdf>`__]).

Destination
^^^^^^^^^^^

You can export the mosaic composition to the :guilabel:`SEPAL workspace` or to :guilabel: GEE as an `Asset`.

In both cases, the same image will be exported; however, for the former, the image will be exported in :code:`.tif` format to the :code:`Downloads` SEPAL folder; for the latter, the image will be exported to your GEE account **Assets** list.

.. attention::

    If :guilabel:`GEE Asset` is not displayed, your GEE account is not connected to SEPAL (see `Connect SEPAL to GEE <../setup/gee.html>`__).

Select :btn:`<fa-solid fa-check> Apply` to start the download process.

Access
^^^^^^

Once the download process is complete, access the data in your SEPAL folders.

The data will be stored in the :code:`Downloads` folder using the following format:

.. code-block::

    .
    └── downloads/
        └── <PM name>/
            ├── <PM name>_<gee tile id>.tif
            ├── <PM name>_<gee tile id>.tif
            ├── ...
            ├── <PM name>_<gee tile id>.tif
            └── <PM name>_<gee tile id>.vrt

.. attention::

    Understanding how images are stored in a Planet mosaic is only required if you want to use them manually. SEPAL applications are bound to this tiling system and can digest this information for you.

The data are stored in a folder using the previously chosen name of the Planet mosaic (as described in the "Start" section of this page of the documentation). Since the data is spatially too big to be exported at once, the data is divided into smaller pieces and reassembled in a :code:`<PM name>_<gee tile id>.vrt` file.

.. tip::

    The full folder with consistent tree hierarchy is required to read the :code:`.vrt` file.

.. important::

    Now that you have downloaded the Planet mosaic to your SEPAL account and/or GEE account, it can be retrieved to your computer using `FileZilla <../setup.filezilla.html>`__ or used in other SEPAL workflows.
