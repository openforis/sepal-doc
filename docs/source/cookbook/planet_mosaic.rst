Planet mosaic
=============

Overview 
--------

A mosaic is a combination or fusion of two or more images. In SEPAL, you can create a single raster dataset from different time overlay provided provided by Planet. These overlay can be managed in various ways. For example, you can choose to keep only the raster data from the first or last dataset, combine the values of the overlay cells using a weighting algorithm, average the values of the overlay cells or take the maximum or minimum value. In addition, certain corrections can be made to the image to correct for clouds, snow etc. These operations are complex and repetitive. SEPAL offers you an interactive and intuitive way to create Planet mosaics on any AOI.

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
-   :guilabel:`SRC`: the sources datasets of the time series
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

.. thumbnail:: ../_images/cookbook/planet_mosaic/aoi_landing.png
    :title: The 3 differents ways to select an AOI in SEPAL
    :group: planet-mosaic-recipe

.. tip::

    The AOI selection process is fully described in `AOI selection <../feature/aoi_selector.html>`__

Date
^^^^

In the :guilabel:`DAT` tab, you will be asked to select the dates of the time series used to build the mosaic image. You need to provide a start and an end date. 

.. thumbnail:: ../_images/cookbook/planet_mosaic/date.png
    :title: The date selection window
    :group: planet-mosaic-recipe

click on the :btn:`<fas fa-calendar-alt>` to display the Date picker and select your date. 

.. thumbnail:: ../_images/cookbook/planet_mosaic/date_picker.png
    :title: The SEPAL datepicker as it is used in the planet mosaic tool
    :group: planet-mosaic-recipe

When the selection is done click on :btn:`<fa fa-chevron-right> next` button.

Sources
^^^^^^^

SEPAL can use multiple data sources to create your mosaics as long as they are Planet related datasets.

3 options are availables: :guilabel:`NICFI basemaps`, :guilabel:`Custom basemaps`, :guilabel:`Daily imagery`

Once your finished, click on :btn:`<fas fa-check> done` to finish the process. 

NICFI basemaps
""""""""""""""

The NICFI basemap use the level 1 NICFI data provided by SEPAL. 

.. warning::
    
    provided data are montly mosaics so your time range need to be longer than 1 month. If not only one image will be used.

.. thumbnail:: ../_images/cookbook/planet_mosaic/sources.png
    :title: The different sources available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Custom basemaps 
"""""""""""""""

Using this option the user can provide a custom :code:`ImageCollection` asset provided by Planet (such as the NICFI level 1 data provided to registered users).

.. thumbnail:: ../_images/cookbook/planet_mosaic/sources_custom.png
    :title: The different sources available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Daily imagery
"""""""""""""

.. danger::

    Only user granted access with NICFI level 2 data can use this option.

Using this option the user can provide a custom daily :code:`ImageCollection` asset provided by Planet.

.. thumbnail:: ../_images/cookbook/planet_mosaic/sources_level_2.png
    :title: The different sources available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

Options
^^^^^^^

.. note::

    This step is not mandatory as Planet mosaic are already sanitised.

SEPAL provide the user with options to customize the images used to composite the moasic raster.
The selcted parameter will be automatically applied to the analysis so simply click on :btn:`<fas fa-times> close` to finish the customization.

.. thumbnail:: ../_images/cookbook/planet_mosaic/options.png
    :title: The 3 options available in SEPAL to build Planet mosaics
    :group: planet-mosaic-recipe

cloud masking
"""""""""""""

Planet composites already removes clouds. Setting this to a value > 0 will remove additional clouds using GEE algorithm.

Shadow masking
""""""""""""""

Planet composites already removes shadows. Setting this to a value > 0 will remove additional shadows using GEE algorithm.

cloud buffering
"""""""""""""""

-   :guilabel:`none`: Only mask the clouds. It might leave hazy pixels around masked clouds, but will minimize the amount of maxed pixels in the mosaic.
-   :guilabel:`moderate`: Mask an additional 120m around each larger cloud. This helps prevent hazy pixels at the border of clouds to be included in the mosaic.
-   :guilabel:`aggressive`: Mask an additional 600m around each larger cloud. This helps prevent hazy pixels at the border of clouds to be included in the mosaic.

Analysis
--------

Once all the parameter have been set, the mosaic will be rendered on the fliy on screen. Multiple color combination can be displayed such as the one shown in the next figures. 

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

Clicking on the :btn:`<fas fa-cloud-download-alt>` tab will open the retrieve panel where the you can select the exportation parameters.

.. thumbnail:: ../_images/cookbook/planet_mosaic/retrieve.png
    :title: the last panel of the planet mosaic: the exportation
    :group: planet-mosaic-recipe


Bands
^^^^^

You need to select the band to export in the mosaic. There is no max number of bands, however, exporting useless bands will only increase the size and the time of the output. 

.. tip:: 

    There is no fixed rule to the band selection. Each index is more adapted to a set of analyses in a defined biome. The knowledge of the study area, the evolution expected and the careful selection of an adapted band combination will improve the quality of the downstream analysis.

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

You can set a custom scale for exportation by changing the value in the :code:`scale` field. Requesting a smaller resolution than images native resolution will not improve the quality of the output, just its size so keep in mind that PlanetLab data native resolution is 4.7 m.

Destination
^^^^^^^^^^^

You can export the image to :guilabel:`sepal workspace` or to :guilabel:`google earth engine asset`. The same image will be exported but in the first case you will find it in :code:`.tif` format in the :code:`downloads` folder, in the second one the image will be exported to your GEE account asset list. 

.. warning::

    If :guilabel:`google earth engine asset` is not displayed, it means that your GEE account is not connected to SEPAL, please refer to `Connect SEPAL to GEE <../setup/gee.html>`__.

Click on :btn:`<fas fa-check> apply` to start the download process. 

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

    Understanding how images are stored in an Planet Mosaic is only required if you want to manually use them. The SEPAL applications are bound to this tiling system and can digest this information for you.

The data are stored in a folder using the name of the Planet mosaic as it was set in the first section of this document. As the number of data is spatially too big to be exported at once, the data are cut into small pieces and brought back together in a :code:`<PM name>_<gee tile id>.vrt` file. 

.. tip:: 

    The full folder with a consistent tree hierarchy is required to read the `.vrt`

.. important::

    Now that you have downloaded the Planet Mosaic to your SEPAL or/and GEE account, it can be retrieved to your computer using `FileZilla <../setup.filezilla.html>`__ or used in other SEPAL workflows.




