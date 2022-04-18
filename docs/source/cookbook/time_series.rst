Time series
===========

Overview 
--------

A Satellite Image Time Series (SITS) is a set of satellite images taken from the same scene at different times. A SITS makes use of different satellite sources to obtain a larger data series with a short time interval between two images. In this case, it is fundamental to observe the spatial resolution and registration constraints.

Satellite observations offer opportunities for understanding how Earth is changing, for determining the causes of these changes, and for predicting future changes. Remotely sensed data, combined with information from ecosystem models, offers an opportunity for predicting and understanding the behavior of the Earth's ecosystem. Sensors with high spatial and temporal resolutions make the observation of precise spatio-temporal structures in dynamic scenes more accessible. Temporal components integrated with spectral and spatial dimensions allow the identification of complex patterns concerning applications connected with environmental monitoring and analysis of land-cover dynamics.

Change detection can only provide a "before and after" scenario; a time-series analysis provides an opportunity to study patterns and key changes in the landscape evolution over time.

This SEPAL recipe allows users to create and retrieve SITS based on `Landsat <https://www.usgs.gov/core-science-systems/nli/landsat/data-tools>`__ and `Copernicus <https://www.copernicus.eu/>`__ programs imagery using the Google Earth Engine datacube.  

.. warning::

    You won't be able to retrieve the images if your SEPAL account and GEE account are not connected. Follow `Connect SEPAL to GEE <../setup/gee.html>`__ to know more.

Start
-----

Once the time-series recipe is selected, SEPAL will show up the recipe process in a new tab(1), the base map will change to Google high-resolution imagery and the AOI selection window will open itself on the bottom right side (2). 

.. thumbnail:: ../_images/cookbook/time_series/landing.png
    :group: time-series-recipe
    :title: the landing page of the time series recipe

The first step is to change the name of the recipe. This name will be used to name your files and recipes in the SEPAL folders. Use the best-suited convention for your need. Simply double-click the tab and write a new name. It will default to :code:`Time_series_<start_date>_<end_date>_<band name>`.

.. thumbnail:: ../_images/cookbook/time_series/default_title.png
    :title: time series default title 
    :width: 49%

.. thumbnail:: ../_images/cookbook/time_series/title.png
    :title: time series modified title 
    :width: 49%
    
.. note::

    The SEPAL team recommends using the following naming convention: :code:`<aoi name>_<start-<end>_<measure>_<sensors>`. As an example the following is a satisfying recipe name: :code:`sgp_2012-2018_ndfi_l78`.

Parameters
----------

On the bottom right corner, 4 tabs are available. They will allow you to customize the time series to its needs.

-   :guilabel:`AOI`: the Area of interest (AOI)
-   :guilabel:`DAT`: the dates of the time series
-   :guilabel:`SRC`: the sources datasets of the time series
-   :guilabel:`PRC`: the pre-processing parameters

.. thumbnail:: ../_images/cookbook/time_series/no_parameters.png
    :title: The 4 tabs to set up SEPAL time series parameters
    :group: time-series-recipe

AOI Selection
^^^^^^^^^^^^^

The data exported by the recipe will be cut to the bounds of the AOI. There are multiple ways to select the AOI in SEPAL:

-   Administrative boundaries
-   EE Tables
-   Drawn polygons

.. thumbnail:: ../_images/cookbook/time_series/aoi_landing.png
    :title: The 3 differents ways to select an AOI in SEPAL
    :group: time-series-recipe

.. tip:: 

    The type choice made at this step is not definitive, simply click on :icon:`fa fa-globe` :guilabel:`<the selected method>` on top of the AOI window and a dropdown will allow you to switch between the mentioned methods.

Administrative boundaries
"""""""""""""""""""""""""

You can select administrative layers as an AOI. These geometries are extracted from the `FAO GAUL Level 1 <https://data.apps.fao.org/map/catalog/srv/eng/catalog.search?id=12691#/metadata/9c35ba10-5649-41c8-bdfc-eb78e9e65654>`__ dataset available on `GEE <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1>`__. Select :guilabel:`Select country/province`. 

.. note::

    As GEE does not support non-latin characters, accents and special characters have been removed from country and provinces names.

In the first dropdown menu, you will be able to select a Country (administrative layer 0) from the country list.  
Optionally one can also select a province (administrative level 1) within the country selected. The dropdown list is updated on the fly according to the country selection. If nothing is selected, the whole country will be considered. 

A buffer can be applied on these boundaries, define its size using the provided slider (in km). It is by default set to 0 i.e. disabled. 

.. note:: 

    The area of interest and preview will take longer to show up when buffering is enabled.

Once all the parameters are selected, the AOI will be previewed in the small map at the bottom of the frame. To validate it click on :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom on the AOI and draw it in grey on the map.

.. thumbnail:: ../_images/cookbook/time_series/aoi_administrative.png
    :title: Select AOI based on administrative layers
    :group: time-series-recipe

EE table
""""""""

The user can use custom AOI defined by shapes. These shapes need to be ingested in EarthEngine as a :code:`ee.FeatureCollection`. Select :guilabel:`EE table`.

in the first dropdown, provide a completely qualified GEE asset name (e.g. :code:`projects/gtfp-fao/assets/aoi_ecowas`). 

.. warning::

    You must have access to this asset. If that's not the case ask the owner of the asset to modify the sharing parameters.

-   Select :guilabel:`include all` and the whole geometries associated with the features will be used as AOI. 
-   Select :guilabel:`filter` and the user will be able to provide a column name and a value to filter within the table. The Aoi will then be reduced to the filtered features of the initial asset. 

A buffer can be applied on these boundaries, define its size using the provided slider (in km). It is by default set to 0 i.e. disabled. 

.. note:: 

    The area of interest and the preview will take longer to show up when buffering is enabled.

Once all the parameters are selected, the AOI will be previewed in the small map at the bottom of the frame. To validate it click on :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom on the AOI and draw it in grey on the map.

.. thumbnail:: ../_images/cookbook/time_series/aoi_table.png
    :title: Select AOI based on EE table
    :group: time-series-recipe

Draw polygon
""""""""""""

The user can use custom AOI defined by a drawn shape. This shape will be converted into a :code:`ee.FeatureCollection` on the fly. Select :guilabel:`draw a polygon` to use this option.

The pointer in the map will be converted into a :icon:`fa fa-plus`. Click successively on the map to draw a polygon.

Once the geometry is closed, the AOI will be previewed in the small map at the bottom of the frame. To validate it click on :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom on the AOI and draw it in grey on the map.

.. thumbnail:: ../_images/cookbook/time_series/aoi_polygon.png
    :title: Select AOI based on drawn polygon
    :group: time-series-recipe

Dates
^^^^^

In the :guilabel:`DAT` tab, you will be asked to select the starting date and the ending date of the time series. Click on the date tex field to open a date picker popup. Click on the :icon:`fa fa-check` :guilabel:`Select` button to validate a date. When both dates are selected click on :icon:`fa fa-check` :guilabel:`apply` button.

.. thumbnail:: ../_images/cookbook/time_series/dates.png
    :title: Select AOI based on EE table
    :width: 49%
    :group: time-series-recipe

.. thumbnail:: ../_images/cookbook/time_series/datepicker.png
    :title: Select AOI based on EE table
    :width: 49%
    :group: time-series-recipe

Sources
^^^^^^^

As mentioned in the introduction, A SITS makes use of different satellite sources to obtain a larger data series with a shorter time interval between the images. To meet this objective, SEPAL allows you to select data from multiple entry points. You can select multiple sources in the following list (click on the link to see the corresponding dataset information):

-   Optical datasets: These datasets are based on Optical satellites imagery.

    -   :guilabel:`L8`: `Landsat 8 Tier 1 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1>`__. Landsat scenes with the highest available data quality are placed into Tier 1 and are considered suitable for time-series processing analysis. Tier 1 includes Level-1 Precision Terrain (L1TP) processed data that have well-characterized radiometry and are inter-calibrated across the different Landsat sensors. The geo-registration of Tier 1 scenes will be consistent and within prescribed tolerances [<=12 m root mean square error (RMSE)]. All Tier 1 Landsat data can be considered consistent and inter-calibrated (regardless of the sensor) across the full collection.
        
        .. line-break::

    -   :guilabel:`L8 T2`: `Landsat 8 Tier 2 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T2>`__. Scenes not meeting Tier 1 criteria during processing are assigned to Tier 2. This includes Systematic terrain (L1GT) and Systematic (L1GS) processed scenes, as well as any L1TP scenes that do not meet the Tier 1 specifications due to significant cloud cover, insufficient ground control, and other factors. Users interested in Tier 2 scenes can analyze the RMSE and other properties to determine the suitability for use in individual applications and studies.
        
        .. line-break::

    -   :guilabel:`L7`: `Landsat 7 Tier 1 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T1>`__. Landsat scenes with the highest available data quality are placed into Tier 1 and are considered suitable for time-series processing analysis. Tier 1 includes Level-1 Precision Terrain (L1TP) processed data that have well-characterized radiometry and are inter-calibrated across the different Landsat sensors. The geo-registration of Tier 1 scenes will be consistent and within prescribed tolerances [<=12 m root mean square error (RMSE)]. All Tier 1 Landsat data can be considered consistent and inter-calibrated (regardless of the sensor) across the full collection.
        
        .. line-break::

    -   :guilabel:`L7 T2`: `Landsat 7 Tier 2 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T2>`__. Scenes not meeting Tier 1 criteria during processing are assigned to Tier 2. This includes Systematic terrain (L1GT) and Systematic (L1GS) processed scenes, as well as any L1TP scenes that do not meet the Tier 1 specifications due to significant cloud cover, insufficient ground control, and other factors. Users interested in Tier 2 scenes can analyze the RMSE and other properties to determine the suitability for use in individual applications and studies.

        .. line-break::

    -   :guilabel:`L4-5`: `Landsat 4 Tier 1 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT04_C01_T1>`__ combined with `Landsat 5 Tier 1 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T1>`__. Landsat scenes with the highest available data quality are placed into Tier 1 and are considered suitable for time-series processing analysis. Tier 1 includes Level-1 Precision Terrain (L1TP) processed data that have well-characterized radiometry and are inter-calibrated across the different Landsat sensors. The geo-registration of Tier 1 scenes will be consistent and within prescribed tolerances [<=12 m root mean square error (RMSE)]. All Tier 1 Landsat data can be considered consistent and inter-calibrated (regardless of the sensor) across the full collection.

        .. line-break::

    -   :guilabel:`L4-5 T2`: `Landsat 4 TM Tier 2 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT04_C01_T2>`__ combined with `Landsat 5 TM Tier 2 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T2>`__. Scenes not meeting Tier 1 criteria during processing are assigned to Tier 2. This includes Systematic terrain (L1GT) and Systematic (L1GS) processed scenes, as well as any L1TP scenes that do not meet the Tier 1 specifications due to significant cloud cover, insufficient ground control, and other factors. Users interested in Tier 2 scenes can analyze the RMSE and other properties to determine the suitability for use in individual applications and studies.
        
        .. line-break::

    -   :guilabel:`S2`: `Sentinel-2 Multispectral instrument <https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2>`__ is a wide-swath, high-resolution, multi-spectral imaging mission supporting Copernicus Land Monitoring studies, including the monitoring of vegetation, soil and water cover, as well as observation of inland waterways and coastal areas.        

        .. line-break::

-   Radar datasets: This dataset is based on Radar satellite imagery.

    -   :guilabel:`S1`: `Sentinel-1 SAR GRD <https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD>`__. The Sentinel-1 mission provides data from a dual-polarization C-band Synthetic Aperture Radar (SAR) instrument at 5.405GHz (C band). This collection includes the S1 Ground Range Detected (GRD) scenes, processed using the Sentinel-1 Toolbox to generate a calibrated, ortho-corrected product. The collection is updated daily. New assets are ingested within two days after they become available.

One can Optionally Select in the last dropdown a classification recipe and apply the classifier to every acquisition in the time-series, transforming the time series into a land cover time series. To know more about the classification recipe got to `Classification <./classification.html>`__.

When all the data are selected click on :icon:`fa fa-check` :guilabel:`apply`.

.. thumbnail:: ../_images/cookbook/time_series/sources.png
    :title: The sources panel to select the different datasets that will be used in the time-series.
    :group: time-series-recipe

Pre-processing
^^^^^^^^^^^^^^

.. warning::

    This section is optional as these parameters are set by default.

    -   correction: :code:`None`
    -   cloud detection: :guilabel:`QA bands`, :guilabel:`Cloud score`
    -   cloud masking: :guilabel:`moderate`
    -   snow masking: :guilabel:`on`

Multiple pre-processing parameters can be set to improve the quality of the provided images. SEPAL has gathered 4 of them in the form of these interactive buttons. If you think others should be added to hesitate to mention it in our `issue tracker <https://github.com/openforis/sepal/issues/new/choose>`__.

**Correction**

-   :guilabel:`surface reflectance`: Use scenes atmospherically corrected surface reflectance.
-   :guilabel:`BRDF correction`: Correct for bidirectional reflectance distribution function (BRDF) effects.

**Cloud detection**

-   :guilabel:`QA bands`: use pre-created QA bands from datasets
-   :guilabel:`Cloud score`: use cloud scoring algorithm

**Cloud masking**

-   :guilabel:`Moderate`: rely only on image source QA bands for cloud masking
-   :guilabel:`Agressive`: rely on image source QA bands and a cloud scoring algorithm for cloud masking. This will probably mask out some built-up areas and other bright features.

**Snow masking**
    
-   :guilabel:`On`: mask snow. This tends to leave some pixels with shadowy snow
-   :guilabel:`Off`: don't mask snow. Note that some clouds might get misclassified as snow, and because of this, disabling snow masking might lead to cloud artifacts.


.. thumbnail:: ../_images/cookbook/time_series/pre_processing.png
    :title: The pre-processing panel to select the extra filtering processes that will improve the quality of the provided images.
    :group: time-series-recipe

Available Bands
^^^^^^^^^^^^^^^

.. note:: 

    The wavelength of each band is dependant on the used satellite.

The time series will use a single observation for each pixel. This observation can be one of the following: 

.. list-table::
    :header-rows: 1

    *   -   Name
        -   Description
        -   Formula
    *   -   :guilabel:`blue`
        -   blue
        -   
    *   -   :guilabel:`green`
        -   green 
        -
    *   -   :guilabel:`red`
        -    red
        -
    *   -   :guilabel:`nir`
        -   near infrared 
        -
    *   -   :guilabel:`swir1`
        -   shortwave infrared 1 
        -   
    *   -   :guilabel:`swir2`
        -   shortwave infrared 1
        -
    *   -   :guilabel:`aerosol`
        -   aerosol attributes
        -   
    *   -   :guilabel:`pan`
        -   panchromatic band
        -   
    *   -   :guilabel:`cirrus`
        -   cirrus cloud detection
        -   
    *   -   :guilabel:`thermal`
        -   thermal
        -   
    *   -   :guilabel:`thermal2`
        -   thermal2
        -
    *   -   :guilabel:`brightness`
        -   brightness from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
        -   :math:`0.3037 (band 1) + 0.2793 (band 2) + 0.4743 (band 3) + 0.5585 (band 4) + 0.5082 (band 5) + 0.1863 (band 7)`
    *   -   :guilabel:`greeness`
        -   greeness from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
        -   :math:`-0.2848 (band 1) - 0.2435 (band 2) - 0.5436 (band 3) + 0.7243 (band 4) + 0.0840 (band 5) - 0.1800 (band 7)`
    *   -   :guilabel:`wetness`
        -   wetness from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
        -   :math:`0.1509 (band 1) + 0.1973 (band 2) + 0.3279 (band 3) + 0.3406 (band 4) - 0.7112 (band 5) - 0.4572 (band 7)`
    *   -   :guilabel:`fourth`
        -   fourth from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
        -
    *   -   :guilabel:`fifth`
        -   fifth from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
        -
    *   -   :guilabel:`sixth`
        -   sixth from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
        -
    *   -   :guilabel:`NDVI`
        -   `Normalized difference vegetation index <https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index>`__
        -   :math:`((nir - red)/(nir + red))`
    *   -   :guilabel:`NDMI`: 
        -   `Normalized Difference Moisture Index <http://dx.doi.org/10.1016/S0034-4257(01)00318-2>`__ 
        -    :math:`ndmi = (nir - swir1)/(nir + swir1)`
    *   -   :guilabel:`NDWI`
        -   `Normalized difference water index <https://en.wikipedia.org/wiki/Normalized_difference_water_index>`__
        -   
    *   -   :guilabel:`MNDWI`
        -   `Modified Normalized Difference Water Index <https://doi.org/10.1080/01431160600589179>`__ 
        -   :math:`mndwi = (green - swir) / (green + swir)`
    *   -   :guilabel:`NDFI`
        -   `Normalized Difference Fraction Index <http://10.1016/j.jag.2016.06.020>`__ 
        -   :math:`ndfi = (GV_shade - (NPV + soil)/(GV_shade + NPV + soil)`
    *   -   :guilabel:`EVI`
        -   `Enhanced vegetation index <doi:10.1016/S0034-4257(02)00096-2>`__
        -    :math:`evi =G * (nir - red)/(nir + C_1 * red - C_2 * blue + L)`
    *   -   :guilabel:`EVI2`
        -   Two-band EVI (Enhanced vegetation index)
        -   :math:`evi_2 = 2.5 * (nir - red) / (nir + 2.4 * red + 1)`
    *   -   :guilabel:`SAVI`
        -   `Soil-Adjusted Vegetation Index <http://dx.doi.org/10.1016/0034-4257(88)90106-X>`__
        -   :math:`((nir - red) / (nir + red + L)) x (1 + L)`
    *   -   :guilabel:`NBR`
        -   `Normailzed burn ratio <https://doi.org/10.2737/RMRS-GTR-164>`__
        -   :math:`nbr = (nir - swir) / (nir + swir)`
    *   -   :guilabel:`UI`
        -   Urban index
        -   :math:`ui = (swir2 - nir) / (swir2 + nir)`
    *   -   :guilabel:`NDBI`
        -   `Normalized Difference Built-up Index <#>`__
        -   :math:`ndbi = (swir - nir) / (swir + nir)`
    *   -   :guilabel:`IBI`
        -   Index based built-up index
        -   :math:`ibi = (ndbi - (savi + mndwi) / 2) / (ndbi + (savi + mndwi) / 2)`
    *   -   :guilabel:`BUI`
        -   Built-up Index
        -   :math:`bui = (red - swir1) / (red + swir1) + (swir2 - swir1) / (swir2 + swir1)`

Analysis
--------

Once all the parameters are set, you can generate data from the recipe. Some can be directly generated on the fly from the interface, the rest require retrieving the data to SEPAL folders.

The analysis icons can be found in the top right corner of the sepal window: 

- :icon:`fa fa-chart-area`: plot data
- :icon:`fa fa-cloud-download-alt`: retreive data

.. thumbnail:: ../_images/cookbook/time_series/data_analysis.png
    :title: The 2 tabs used to plot or retreive the Time series data
    :group: time-series-recipe

.. tip::

    The download icon is only released when the data parameters are complete. If the button is disabled, check your parameters, some might be missing. 

Plot
^^^^

Click on the :icon:`fa fa-chart-area` button to start the plotting tool. Move the pointer to the main map, the pointer will be transformed into a :icon:`fa fa-plus`. Click anywhere in the AOI to plot data for this specific location in the following popup window. 

The plotting area is dynamic and can be customized by the user.

Using the slider (1), the temporal width displayed can be changed. It cannot exceed the start and/or end date of the time series. 

You can also select the observation feature by selecting one of the available measures in the dropdown selector in the top left corner (2). The available bands are the same as the described previously. 

On the main graph, each point represents one valid (based on the pre-processing filters) observation. Hover on the point to let the tooltip describe the value and date of the observation (3). 

.. tip:: 

    The coordinates of the point are displayed at the top of the chart window.

.. thumbnail:: ../_images/cookbook/time_series/plot.png
    :title: Plot chart popup window providing all the available information on one single pixel alongside the time series.
    :group: time-series-recipe

.. warning:: 

    The plot feature is retrieving information from GEE on the fly and serving it in an interactive window. This operation can take time depending on the number of available observations and the complexity of the selected pre-processing parameters. If the popup window displays a spinning wheel, wait up to 2 min to see the data displayed.

    .. thumbnail:: ../_images/cookbook/time_series/plot_loading.png
        :title: Plot chart popup window providing all the available information on one single pixel alongside the time series. If there are numerous observations and a complex pre-processing, retrieving the data to SEPAL can take up to 2 min 
        :group: time-series-recipe

Export
^^^^^^

The data generated by the recipe can also be used in other workflows but before it needs to be retrieved from GEE to your SEPAL environment. 

Parameters 
""""""""""
Click on the :icon:`fa fa-cloud-download-alt` button, it will open the download parameters window. You will be able to select the measure to use on each observation of the time-series. This measure can be selected in the list of available bands presented in a previous section.

.. tip:: 

    There is no fixed rule to the measure selection. Each index is more adapted to a set of analyses in a defined biome. The knowledge of the study area, the evolution expected and the careful selection of an adapted measure will improve the quality of the downstream analysis.

You can set a custom scale for exportation by changing the value of the slider (m). Keep in mind that Sentinel data native resolution is 10 m and Landsat is 30 m.

When all the data is selected click on the :icon:`fa fa-check` :guilabel:`apply` button. Notice that the task tab in the bottom left corner of the screen (1) will change from :icon:`fa fa-tasks` to :icon:`fa fa-spinner` which means that the tasks are loading.

.. thumbnail:: ../_images/cookbook/time_series/export_param.png
    :title: Select the parameter of the exportation process to retreive the data from GEE to SEPAL's folders.
    :group: time-series-recipe


Exportation status
""""""""""""""""""

Going to the task tab (bottom left corner using the :icon:`fa fa-tasks` or :icon:`fa fa-spinner` buttons —depending on the loading status—), you will see the list of the different loading tasks. The interface will provide you with information about the task progress and it will display an error if the exportation has failed. If you are unsatisfied with the way we present information, the task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    This operation is running between GEE and SEPAL servers in the background, you can thus close the SEPAL page without killing the process.

When the task is finished the frame will be displayed in green as shown on the second image.

.. thumbnail:: ../_images/cookbook/time_series/download.png
    :width: 49%
    :title: Evolution of the downloading process of the recipe displayed in the task manager of SEPAL.
    :group: time-series-recipe

.. thumbnail:: ../_images/cookbook/time_series/download_complete.png
    :width: 49%
    :title: Completed downloading process of the recipe displayed in the task manager of SEPAL.
    :group: time-series-recipe

Access
""""""

Once the downloading process is done, you can access the data in your SEPAL folders. The data will be stored in the :code:`downloads` folder using the following format:

.. code-block::

    .
    └── downloads
        └── <TS name>
            ├── <tile number>
            │   ├── chunk-<start date>_<end date>
            │   │   ├── <TS name>_<tile number>_<start_date>_<end date>-<gee tiling id>.tif
            │   │   ├── ...
            │   │   └── <TS name>_<tile number>_<start_date>_<end date>-<gee tiling id>.tif
            │   ├── ...
            │   ├── chunk-<start date>_<end date>
            │   ├── tile-<gee tiling id>
            │   │   └── stack.vrt
            │   ├── ...
            │   ├── tile-<gee tiling id>
            │   ├── dates.csv
            │   └── stack.vrt
            ├── ...
            └── <tile number>

.. danger::

    Understanding how images are stored in a Time Series is only required if you want to manually use them. The SEPAL applications are bound to this tiling sytem and can digest this information for you.

The data are stored in a folder using the name of the time series as it was set in the first section of this document. SEPAL team was forced to use this folder structure as Google Earth Engine is enable to export an :code:`ee.ImageCollection`. As the number of data is spatially too big to be exported at once, the data are cut into small pieces and brought back together in a :code:`stack.vrt` file. 

The AOI provided by the user will be split in multiple SEPAL tiles. The AOI is an :code:`ee.FeatureCollection`, each feature is downloaded in a different tile. if the Tile is bigger than 2°x2° (EPSG:4326) then the feature is split again until all the tiles are smaller than the maximal 2° size. The tiles are identified by their :code:`<tile_number>`.

To limit the size of the downloaded images, in each SEPAL tile, the time period is splitted in chunks of 3 month. they are identified by their :code:`<chunk-<start>_<end>`. Chunks are image folders. As a SEPAL tile is still bigger than what GEE can download at once, the images are splitted in GEE tile. This tiling system uses it's own identification system (000000xxxx-000000xxxx). In consequence chunks contain tile raster images. Each one of these images is composed of 1 band per observation date, with the value of the measure for each pixel. The bands are named with the date. 

To gather all theses raster together a first agregation on time is performed. One :code:`stack.vrt` is created per GEE tile meaning that each :code:`stack.vrt`file contains all the :code:`*<gee tiling id>.tif` contained in each chunk. reconstituting the full time period on the smallest spatial unit: the gee tile. each file is stored in a folder called :code:`tile-<gee tiling id>`.

Finally information are gathered at the spatialy at the SEPAL tile level in the main :code:`stack.vrt` file.

The last file: :code:`date.csv` gather all the observation dates in chronological order.

.. note::

    The dates contained in :code:`date.csv` can differ from one SEPAL tile to another due to data availability and pre-processing filters

.. tip:: 

    The full folder with a concistent treefolder is required to read the `.vrt`

Here is an example of a real TS folder:

.. code-block::

    .
    └── downloads
        └── tutorial_TS
            ├── 1
            │   ├── chunk-2012-01-01_2012-04-01
            │   │   ├── tutorial_TS_1_2012-01-01_2012-04-01-0000000000-0000000000.tif
            │   │   ├── ...
            │   │   └── tutorial_TS_1_2012-01-01_2012-04-01-0000002560-0000001024.tif
            │   ├── ...
            │   ├── chunk-2018-10-01_2018-12-31
            │   ├── tile-0000000000-0000000000
            │   │   └── stack.vrt
            │   ├── ...
            │   ├── tile-0000002560-0000001024
            │   ├── dates.csv
            │   └── stack.vrt
            ├── ...
            └── 3

.. important::

    Now that you have downloaded the TS to your SEPAL account, it can be retrieved to your computer using `FileZilla <../setup.filezilla.html>`__ or used in one of our `time-series analysis module <../modules/time-series.html>`__.
