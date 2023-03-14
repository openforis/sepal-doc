Planet mosaic
=============

Overview
--------

A mosaic is a process of combining spatially overlapping images into an individual image. In SEPAL, you can create a composited dataset from Planet images taken at different times. The process can be done using different techniques, for example, you can choose to keep only the pixel value from the first or last image, combine the values of the overlapped pixels using a weighting algorithm, average, or use the maximum or minimum value. In addition, certain preprocessing tasks can be applied to mask clouds/shadows, snow, etc. These operations are complex and repetitive. SEPAL offers you an interactive and intuitive way to create Planet mosaics within any area of interest.

.. thumbnail:: ../_images/cookbook/planet_mosaic/time-series.png
    :group: planet-mosaic-recipe
    :title: a time series of Planet imagery ready to be mosaiced

.. warning::

    You won't be able to retrieve the images if your SEPAL and GEE accounts are not connected. Follow `Connect SEPAL to GEE <../setup/gee.html>`__ to know more.

    You also need to connect your GEE account with Planet. Follow `Use NICFI - Planet Lab data <../setup/nicfi.html>`__.

Start
-----

Once the :code:`planet mosaic` recipe is selected, SEPAL will show up the recipe process in a new tab (1) and the AOI selection window will open itself on the bottom right side (2).

.. thumbnail:: ../_images/cookbook/planet_mosaic/landing.png
    :group: planet-mosaic-recipe
    :title: the landing page of the planet mosaic recipe

The first step is to change the name of the recipe. This name will be used to name your files and recipes in the SEPAL folders. Use the best-suited convention for your need. Simply double-click the tab and write a new name. It will default to :code:`Planet_mosaic_<start_date>_<end_date>`.

.. thumbnail:: ../_images/cookbook/planet_mosaic/default_title.png
    :title: planet mosaics default title
    :width: 49%

.. thumbnail:: ../_images/cookbook/planet_mosaic/modified_title.png
    :title: planet mosaics modified title
    :width: 49%

.. note::

    The SEPAL team recommends using the following naming convention: :code:`<aoi name>_<dates>_<measure>`.

Parameters
----------

On the bottom right corner, 4 tabs are available. They will allow you to customize the planet mosaic to your needs.

-   :guilabel:`AOI`: the Area of interest (AOI)
-   :guilabel:`DAT`: the dates of the time series
-   :guilabel:`SRC`: the time series dataset source
-   :guilabel:`OPT`: the filtering options

.. thumbnail:: ../_images/cookbook/planet_mosaic/no_parameters.png
    :title: The 4 tabs to set up SEPAL planet mosaic parameters
    :group: planet-mosaic-recipe

AOI Selection
^^^^^^^^^^^^^

The data exported by the recipe will be cut to the bounds of the AOI. There are multiple ways to select the AOI in SEPAL:

-   Administrative boundaries
-   EE Tables
-   Drawn polygons

they are extensively described in our documentation. Please read :doc:`../feature/aoi_selector` to know more.

.. thumbnail:: ../_images/cookbook/planet_mosaic/aoi.png
    :title: Select AOI based on administrative layers
    :group: planet-mosaic-recipe

Date
^^^^

In the :guilabel:`DAT` tab, you will be asked to select the dates of the time series used to build the composited image. You need to provide a start and an end date.

.. thumbnail:: ../_images/cookbook/planet_mosaic/date.png
    :title: The date selection window
    :group: planet-mosaic-recipe

Click the :btn:`<fa-solid fa-calendar-days>` to display the Date picker and select your date.

.. thumbnail:: ../_images/cookbook/planet_mosaic/date_picker.png
    :title: The SEPAL datepicker as it is used in the planet mosaic tool
    :group: planet-mosaic-recipe

When the selection is done click :btn:`<fa-solid fa-chevron-right> next` button.

Sources
^^^^^^^

SEPAL can use multiple data sources to create your mosaics/composites as long as they are Planet related datasets.

3 options are available: :guilabel:`NICFI basemaps`, :guilabel:`Custom basemaps`, :guilabel:`Daily imagery`

Once you are finished, click on :btn:`<fa-solid fa-check> done` to finish the process.

NICFI basemaps
""""""""""""""

The NICFI basemap uses the level 1 NICFI data provided by SEPAL.

.. warning::

    provided data are monthly mosaics, which means that your time range needs to be longer than 1 month. Otherwise, only one image will be used.

.. thumbnail:: ../_images/cookbook/planet_mosaic/sources.png
    :title: The different sources available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Custom basemaps
"""""""""""""""

You can provide a custom :code:`ImageCollection` Planet asset (such as NICFI level 1 data provided to registered users).

.. thumbnail:: ../_images/cookbook/planet_mosaic/sources_custom.png
    :title: The different sources available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Daily imagery
"""""""""""""

.. danger::

    Only users with granted access to NICFI level 2 data can use this option.

Choose this option to provide custom Planet daily :code:`ImageCollection` imagery.

.. thumbnail:: ../_images/cookbook/planet_mosaic/sources_level_2.png
    :title: The different sources available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Options
^^^^^^^

.. note::

    This step is not mandatory due to Planet mosaics are already sanitized.

SEPAL provides you with options to customize the images used to create the compositing mosaic. The selected parameter will be automatically applied to the analysis, click the :btn:`<fa-solid fa-xmark> close` button to finish the customization.

.. thumbnail:: ../_images/cookbook/planet_mosaic/options.png
    :title: The 3 options available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Cloud masking
"""""""""""""

Planet composites already remove clouds. Setting this parameter to a value greater than zero (0) will remove additional clouds using a Google Earth Engine (GEE) algorithm.

Shadow masking
""""""""""""""

Planet composites already remove shadows. Setting this parameter to a greater value than zero (0) will remove additional shadows using a GEE algorithm.

Cloud buffering
"""""""""""""""

-   :guilabel:`none`: Only mask clouds. It might leave hazy pixels around masked clouds but will minimize the amount of maxed pixels in the mosaic.
-   :guilabel:`moderate`: Mask an additional 120m around each larger cloud. This helps prevent hazy pixels at the border of clouds to be included in the mosaic.
-   :guilabel:`aggressive`: Mask an additional 600m around each larger cloud. This helps prevent hazy pixels at the border of clouds to be included in the mosaic.

Analysis
--------

Once all the parameters have been set, the mosaic will be rendered on the fly. Multiple color combinations can be displayed, see next figures.

.. thumbnail:: ../_images/cookbook/planet_mosaic/mosaic_rgb.png
    :title: The on-the-fly rendered mosaic displayed using red, blue, green bands
    :group: planet-mosaic-recipe
    :width: 49%

.. thumbnail:: ../_images/cookbook/planet_mosaic/mosaic_nrg.png
    :title: The on-the-fly rendered mosaic displayed using nir, red, green bands
    :group: planet-mosaic-recipe
    :width: 49%

.. thumbnail:: ../_images/cookbook/planet_mosaic/mosaic_ndvi.png
    :title: The on-the-fly rendered mosaic displayed using NDVI in false colors
    :group: planet-mosaic-recipe
    :width: 49%

.. thumbnail:: ../_images/cookbook/planet_mosaic/mosaic_savi.png
    :title: The on-the-fly rendered mosaic displayed using SAVI in false colors
    :group: planet-mosaic-recipe
    :width: 49%

Retrieve
--------

Click the :btn:`<fa-solid fa-cloud-arrow-down>` tab, the retrieve panel will be displayed, you can select which bands or indexes to download, specify the output scale, and destination.

.. thumbnail:: ../_images/cookbook/planet_mosaic/retrieve.png
    :title: the last panel of the planet mosaic: the exportation
    :group: planet-mosaic-recipe


Bands
^^^^^

You need to select the band(s) to export in the mosaic. There is no max number of bands, however, exporting useless bands will only increase the size and the time of the output.

.. tip::

    There is no fixed rule to the band selection. Every index will be more useful to the type of analysis you are performing. The knowledge of the study area, the evolution expected and the careful selection of an adapted band combination will improve the quality of the downstream analysis.

Raw bands
"""""""""

-   :guilabel:`blue`: blue
-   :guilabel:`green`: green
-   :guilabel:`red`: red
-   :guilabel:`nir`: near infrared


Indexes
"""""""

-   :guilabel:`NDVI`: `Normalized difference vegetation index <https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index>`__
-   :guilabel:`NDMI`: `Normalized Difference Moisture Index <http://dx.doi.org/10.1016/S0034-4257(01)00318-2>`__
-   :guilabel:`NDWI`: `Normalized difference water index <https://en.wikipedia.org/wiki/Normalized_difference_water_index>`__
-   :guilabel:`EVI`: `Enhanced vegetation index <doi:10.1016/S0034-4257(02)00096-2>`__
-   :guilabel:`EVI2`: Two-band EVI (Enhanced vegetation index)
-   :guilabel:`SAVI`: `Soil-Adjusted Vegetation Index <http://dx.doi.org/10.1016/0034-4257(88)90106-X>`__

Scale
^^^^^

You can set a custom scale for exportation by changing the value in the :code:`scale` field. Requesting a smaller resolution than the image's native resolution will not improve the quality of the output, just its size so keep in mind that PlanetLab data's native resolution is 3 - 4.1 m (altitude dependent Ground Sample Distance,  `see more info <https://assets.planet.com/docs/Planet_Combined_Imagery_Product_Specs_letter_screen.pdf>`__).

Destination
^^^^^^^^^^^

You can export the mosaic composition to :guilabel:`sepal workspace` or to :guilabel: GEE as an `asset`. The same image will be exported but in the first case you will find it in :code:`.tif` format in the :code:`downloads` SEPAL folder, in the second one the image will be exported to your GEE account asset list.

.. warning::

    If :guilabel:`google earth engine asset` is not displayed, it means that your GEE account is not connected to SEPAL, please refer to `Connect SEPAL to GEE <../setup/gee.html>`__.

Click on :btn:`<fa-solid fa-check> apply` to start the download process.

Access
^^^^^^

Once the download process is done, you can access the data in your SEPAL folders. The data will be stored in the :code:`downloads` folder using the following format:

.. code-block::

    .
    └── downloads/
        └── <PM name>/
            ├── <PM name>_<gee tile id>.tif
            ├── <PM name>_<gee tile id>.tif
            ├── ...
            ├── <PM name>_<gee tile id>.tif
            └── <PM name>_<gee tile id>.vrt

.. danger::

    Understanding how images are stored in a Planet Mosaic is only required if you want to manually use them. The SEPAL applications are bound to this tiling system and can digest this information for you.

The data are stored in a folder using the name of the Planet mosaic as it was set in the first section of this document. As the number of data is spatially too big to be exported at once, the data are cut into small pieces and brought back together in a :code:`<PM name>_<gee tile id>.vrt` file.

.. tip::

    The full folder with a consistent tree hierarchy is required to read the :code:`.vrt`

.. important::

    Now that you have downloaded the Planet Mosaic to your SEPAL or/and GEE account, it can be retrieved to your computer using `FileZilla <../setup.filezilla.html>`__ or used in other SEPAL workflows.
