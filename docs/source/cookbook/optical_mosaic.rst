Optical mosaic
==============

Overview 
--------

A mosaic is a combination or fusion of two or more images. In SEPAL, you can create a single raster dataset from several raster datasets by mosaicing them together.
this can be used on contiguous rasters (left) but also on overlapping images (right). 

.. image:: ../img/cookbook/optical_mosaic/mosaic_contiguous.gif
    :width: 49%

.. image:: ../img/cookbook/optical_mosaic/mosaic_overlay.png
    :width: 49%

These overlay areas can be managed in various ways. For example, you can choose to keep only the raster data from the first or last dataset, combine the values of the overlay cells using a weighting algorithm, average the values of the overlay cells or take the maximum or minimum value. In addition, certain corrections can be made to the image to correct for clouds, snow etc. These operations are complex and repetitive. SEPAL offers you an interactive and intuitive way to create mosaics on any AOI.

.. warning::

    You won't be able to retrieve the images if your SEPAL account and GEE account are not connected. Follow `Connect SEPAL to GEE <../setup/gee.html>`__ to know more.


Start
-----

Once the mosaic recipe is selected, SEPAL will show up the recipe process in a new tab (1) and the AOI selection window will open itself on the bottom right side (2). 

.. thumbnail:: ../img/cookbook/optical_mosaic/landing.png
    :group: optical-mosaic-recipe
    :title: the landing page of the optical mosaic recipe

The first step is to change the name of the recipe. This name will be used to name your files and recipes in the SEPAL folders. Use the best-suited convention for your need. Simply double-click the tab and write a new name. It will default to :code:`Optical_mosaic_<start_date>_<end_date>_<band name>`.

.. thumbnail:: ../img/cookbook/optical_mosaic/default_title.png
    :title: optical mosaics default title 
    :width: 49%

.. thumbnail:: ../img/cookbook/optical_mosaic/modified_title.png
    :title: optical mosaics modified title 
    :width: 49%
    
.. note::

    The SEPAL team recommends using the following naming convention: :code:`<aoi name>_<dates>_<measure>`.


Parameters 
----------

On the bottom right corner, 5 tabs are available. They will allow you to customize the time series to its needs.

-   :guilabel:`AOI`: the Area of interest (AOI)
-   :guilabel:`DAT`: the dates of the time series
-   :guilabel:`SRC`: the sources datasets of the time series
-   :guilabel:`SCN`: the scene selection parameters
-   :guilabel:`CMP`: the composition parameters

.. thumbnail:: ../img/cookbook/optical_mosaic/no_parameters.png
    :title: The 5 tabs to set up SEPAL optical mosaic parameters
    :group: optical-mosaic-recipe

AOI Selection
^^^^^^^^^^^^^

The data exported by the recipe will be cut to the bounds of the AOI. There are multiple ways to select the AOI in SEPAL:

-   Administrative boundaries
-   EE Tables
-   Drawn polygons

.. thumbnail:: ../img/cookbook/optical_mosaic/aoi_landing.png
    :title: The 3 differents ways to select an AOI in SEPAL
    :group: optical-mosaic-recipe

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

.. thumbnail:: ../img/cookbook/time_series/aoi_administrative.png
    :title: Select AOI based on administrative layers
    :group: optical-mosaic-recipe

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

.. thumbnail:: ../img/cookbook/time_series/aoi_table.png
    :title: Select AOI based on EE table
    :group: optical-mosaic-recipe

Draw polygon
""""""""""""

The user can use custom AOI defined by a drawn shape. This shape will be converted into a :code:`ee.FeatureCollection` on the fly. Select :guilabel:`draw a polygon` to use this option.

The pointer in the map will be converted into a :icon:`fa fa-plus`. Click successively on the map to draw a polygon.

Once the geometry is closed, the AOI will be previewed in the small map at the bottom of the frame. To validate it click on :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom on the AOI and draw it in grey on the map.

.. thumbnail:: ../img/cookbook/time_series/aoi_polygon.png
    :title: Select AOI based on drawn polygon
    :group: optical-mosaic-recipe

Date
^^^^

yearly mosaic
"""""""""""""

In the :guilabel:`DAT` tab, you will be asked to select a year. It will define the year which pixels in the mosaic should come from. When the selection is done click on :icon:`fa fa-check` :guilabel:`apply` button.

.. thumbnail:: ../img/cookbook/optical_mosaic/select_year.png
    :title: The year selection panel
    :group: optical-mosaic-recipe

Seasonal mosaic
"""""""""""""""

click on :guilabel:`more` in the :guilabel:`DAT` panel to expand the date selection tool. Now instead of selecting a year you can select a season of interest. 

Click on the :icon:`fa fa-calendar` (1) to open the date selection popup. The selected date will be the target of the mosaic, i.e the date in which pixels in the mosaic should ideally come from. 

Now using the main slider (2) define a season around the target date. This season define the 2 dates in beetween which SEPAL can retreive the mosaic images. 

The number of images on one single season of one year may not be enough to produce a correct mosaic. SEPAL provide 2 secondary sliders to increase the pool of images to create the mosaic. Both count the number of season SEPAL can retreive in the past (:code:`past season` - (3)) and in the future (:code:`future season` - (4)). 

When the selection is done click on :icon:`fa fa-check` :guilabel:`apply` button.

.. thumbnail:: ../img/cookbook/optical_mosaic/select_season.png
    :title: The season selection panel
    :group: optical-mosaic-recipe

Sources
^^^^^^^

As mentioned in the introduction, A mosaic makes use of different raster dataset and they can be obtain from multiple sources. SEPAL allows you to select data from multiple entry points that you can select from the following list (click on the link to see the corresponding dataset information):

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

-   :guilabel:`A+B`: `Sentinel-2 Multispectral instrument <https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2>`__ is a wide-swath, high-resolution, multi-spectral imaging mission supporting Copernicus Land Monitoring studies, including the monitoring of vegetation, soil and water cover, as well as observation of inland waterways and coastal areas.

.. thumbnail:: ../img/cookbook/optical_mosaic/select_source.png
    :title: The source selection panel
    :group: optical-mosaic-recipe

To validate your selection, click on :icon:`fa fa-check` :guilabel:`Apply` button.

Scenes
^^^^^^

.. warning:: 

    If Sentinel and Landsat data have been selected, the user will be forced to use all scenes. As the tilling system from Sentinel and Landsat data are different, it's impossible to select scenes using the tool presented in the next sections.

The user can use multiple options to select the best scenes for its mosaic. The most simple is to use every image available based on the date parameters. Click :guilabel:`use all scenes` and all the images will be integrated to the mosaic. 

Select :guilabel:`select scenes` and 3 new selection option will becaome available. SEPAL is sorting the images available for each tile, these :code:`priority` options are there choose which way suits your analysis: 

-   :guilabel:`cloud free`: will give the priority to the image with zero to few clouds. 
-   :guilabel:`target date`: will give the priority to the image that is matching the target date 
-   :guilabel:`balanced`: will give the priority to the image that maximize both cloud and target date.

To validate your selection, click on :icon:`fa fa-check` :guilabel:`Apply` button.

.. thumbnail:: ../img/cookbook/optical_mosaic/scene_method.png
    :title: The source selection panel
    :group: optical-mosaic-recipe

Composite
^^^^^^^^^

.. note:: 

    This step is optional, SEPAL provide the folowing options by default: 

    -   **correction**: :guilabel:`SR`, :guilabel:`BRDF`
    -   **pixel filters**: no filters
    -   **cloud detection**: :guilabel:`QA bands`, :guilabel:`cloud score`
    -   **cloud masking**: :guilabel:`moderate`
    -   **cloud buffering**: :guilabel:`None`
    -   **snow masking**: :guilabel:`on`
    -   **composing method**: :guilabel:`medoid`

To create a mosaic, the user need to provide to SEPAL the compositing method to use to assemble the pixels together to create the final image. here is a description of all the possible compositing options available in SEPAL. 

.. thumbnail:: ../img/cookbook/optical_mosaic/composite_options.png
    :title: The panel to select the composite options of your mosaic
    :group: optical-mosaic-recipe

corrections
"""""""""""

This will apply corrections on the stacked pixels in order to improve the quality of the mosaic.

-   :guilabel:`SR`: Surface reflectance improves comparison between multiple images over the same region by accounting for atmospheric effects such as aerosol scattering and thin clouds, which can help in the detection and characterization of Earth surface change. Top of atmosphere images are used if not selected.
-   :guilabel:`BRDF`: Uses a BRDF model to characterise surface reflectance anisotropy. For a given land area, the BRDF is established based on selected multiangular observations of surface reflectance.
-   :guilabel:`calibrate`:  calibrate Sentinel and Landsat data to make them compatibles
    
    .. note:: 
        
        This option is only available if landsat and sentinel data are mixed. You also need to unselect the BRDF and SR corrections.

pixel filters
"""""""""""""

activate any of the filter will remove some pixels from the stack. Removing pixels It improves the quality of the mosaic pixel as thery are not taken into account in the median value computation.

.. warning:: 

    each filter is applied itteratively. Meaning that if NDVI is already filtering all pixels but one, there will be nothing left in the stack to be filtered by day of the year. 
    Note as well that adding filter increase significatively the creation time of the mosaic.

-   **shadow**: filter the XX% darkest pixels of the stack
-   **haze**: compute a haze index and filter XX% highest values
-   **NDVI**: compute the NDVI and only keep the XX% highest values
-   **day of the year**: compute the distance from target day in days and filter out the XX% farest.

Cloud detection 
"""""""""""""""

The algorithm used to detect clouds. 

-   :guilabel:`QA bands`: use QA bands to identify clouds in Sentinel data
-   :guilabel:`cloud score`: Use the computed cloud score to identify clouds in Landsat data
-   :guilabel:`Pino 26`: Use the Pino_26 algorithm to identify clouds (`D. Simonetti, 2021 <https://doi.org/10.1016/j.dib.2021.107488>`__)

    .. warning:: 

        This filter is only available for Sentinel exlusive source and when both :guilabel:`BRDF` and :guilabel:`SR` correction are disabled.

cloud masking 
"""""""""""""

Controls how clouds will be masked based on the cloud detection algorithm selected. 

-   :guilabel:`off`: Use cloud-free pixels if possible, but don't mask areas without cloud-free pixels
-   :guilabel:`moderate`: Rely only on image source QA bands for cloud masking. Moderate threshold are used.
-   :guilabel:`aggressive`: Rely on image source QA bands and a cloud scoring algorithm for cloud masking with aggressive threshold. This will probably mask out some built-up areas and other bright features.

cloud buffering
"""""""""""""""

When pixels are identified as clouds, SEPAL can remove pixels in a small buffer around it to prevent hazy pixels at the border of clouds to be included in the mosaic. 

.. note::

    buffering is done pixel-wised so using this option will increase significatively the creation time of the mosaic.

-   :guilabel:`none`: Don't use cloud buffering
-   :guilabel:`moderate`: Mask an additional **120m** around each larger cloud. 
-   :guilabel:`aggressive`: Mask an additional 600m around each larger cloud. 

snow masking
""""""""""""

Define how snowy pixels will be masked.

-   :guilabel:`on`: Mask snow. This tend to leave some pixels with shadowy snow
-   :guilabel:`off`: Don't mask snow. Note that some clouds might get misclassified as snow, and because of this, disabling snow masking might lead to cloud artifacts.

composing method
""""""""""""""""

After filtering the stack of pixels, SEPAL will compute the median value on the different bands of the image. The composing method will define how the final pixel value is extracted. 

-   :guilabel:`medoid`: Use the closest pixel from the median value. As a real pixel from the stack the final value will embed metadata (like the date of observation)
-   :guilabel:`median`: Use the computed value of the median. If no pixel is matching this value, the pixel will not embed any metadata. tends to produce smoother mosaics. 

Analysis
--------

After selecting the paramters the user can start interacting with the scenes and statr the analysis.
On the top right corner, 3 tabs are available. They will allow you to customize the mosaic scene selection and export the final result.

-   :icon:`fas fa-magic`: auto-select scenes
-   :icon:`fas fa-trash`: clear selected scenes
-   :icon:`fas fa-cloud-download-alt`: retrieve mosaic

.. thumbnail:: ../img/cookbook/optical_mosaic/analysis.png
    :title: The 3 tabs to select the scenes and export mosaic
    :group: optical-mosaic-recipe

.. note::

    If you ave not selected the option :guilabel:`select scenes` in the :guilabel:`SRC` tab, the :icon:`fas fa-magic`button will be disabled and scene areas (the big 0s on the previous screenshot) will be hidden as no scene selection need to be performed.

Select Scenes
^^^^^^^^^^^^^

To create a mosaic, the user need to select the scenes that will be used to compute each pixel value of the mosaic. To do so SEPAL provide a user friendly interface that will help and guide the user during the selection process. The user won't select the stack for every pixel, instead SEPAL is cutting the AOI in smaller pieces called **tiles**. These tiles correspond to the native tiling system of you dataset. they are displayed on the map using the circled numbers. each one corresponding to the number of scenes used to build the mosaic tile. hover these number to see the borders of the tile appear. 

.. note:: 

    Landsat and Sentinel datasets have an inconsistent tiling sytem, that's why the selection process cannot be used if you selected both these datasets. If you have a UI idea to make them work together please let us know in our `issue tracker <https://github.com/openforis/sepal>`__, we'll be happy to implement it.

Auto-select scene 
"""""""""""""""""

clicking on the :icon:`fas fa-magic` tab will open the auto-selection panel. 
Move the silders to select the minimum and maximum number of scene SEPAL should select in a tile. then click on :guilabel:`validate` to apply the auto-select. 
SEPAL will use the priority defined in the :guilabel:`SRC` tab to order the scene and pick up the optimal number for your request.

.. tip:: 

    the relsult is never perfect but can be used as a starting point for manual slection of scene.

.. thumbnail:: ../img/cookbook/optical_mosaic/auto-select.png
    :title: The panel to select the minimum and maximum number of scen to auto select in each tile
    :group: optical-mosaic-recipe

clear all scene
"""""""""""""""

If at least 1 scene is selected in one of the AOI tile, the :icon:`fas fa-trash` tab will be released. click on it to open the clear panel. 
Click on :guilabel:`clear scenes` and all the scenes selected (manually or automatically) will be removed. 

.. thumbnail:: ../img/cookbook/optical_mosaic/remove_all.png
    :title: The panel to unselect all the scenes from the mosaic
    :group: optical-mosaic-recipe

manual selection
""""""""""""""""

Hover a tile and click on it to open the scene selection menu (1). This window is cut in two sides: 

-   Available scene (2): All the available scenes according to the parameters set by the user. These scenes are ordered using the :code:`priority` parameter set by the user in :guilabel:`SRC` tab. 
-   Selected scenes (3): The scene that are curently selected to build the displayed mosaic. 

.. thumbnail:: ../img/cookbook/optical_mosaic/select_scenes.png
    :title: The popup window used to select individual scenes for one single tile
    :group: optical-mosaic-recipe

each thumbails represents a scene from the tile stack and the user have the possibility to include it to the mosaic. they are represented horizontally when they are in the **selected scene** area and vertically when they are in the **available scene** area. In both case multiple information can be found on the thumbnail: 

-   a small preview of the scene in the *red, blue, green* band combination
-   the exact date in yyyy-mm-dd of the scene
-   :icon:`fas fa-satellite-dish`: the satellite name
-   :icon:`fas fa-cloud`: the cloud coverage of the scene in % and its position in the stack values
-   :icon:`fas fa-calendar-check`: the distance from target day in days within the season and its position in the stack values

.. thumbnail:: ../img/cookbook/optical_mosaic/thumbnail_available.png
    :width: 24%
    :title: the thumbnail of a scene when it's in the available scene area
    :group: optical-mosaic-recipe

.. thumbnail:: ../img/cookbook/optical_mosaic/thumbnail_selected.png
    :width: 74%
    :title: the thumbnail of a scene when it's in the selected scene area
    :group: optical-mosaic-recipe

When hovered the user can choose to move the scene to the **selected** area by clicking :icon:`fa fa-plus`:guilabel:`add` or move it back to **available** by clicking :icon:`fa fa-minus` :guilabel:`remove`.  

.. thumbnail:: ../img/cookbook/optical_mosaic/thumbnail_available_hover.png
    :width: 24%
    :title: the thumbnail of a scene when it's in the available scene area when it's hovered
    :group: optical-mosaic-recipe

.. thumbnail:: ../img/cookbook/optical_mosaic/thumbnail_selected_hover.png
    :width: 74%
    :title: the thumbnail of a scene when it's in the selected scene area when it's hovered
    :group: optical-mosaic-recipe

.. tip:: 

    Scenes are moved from one area to the other so they are not duplicated and cannot be selected twice. be careful if your connection is slow wait for the thumbnail to move before clicking again. If you click too fast you could select 2 different images instead of one.

Once you are happy with you selection, click :guilabel:`apply` to close the window and use the selected scenes to compute the mosaic on this tile. When the window is closed, SEPAL reset the rendenring of all the tiles.

Retreive
^^^^^^^^

clicking on the :icon:`fas fa-cloud-download-alt` tab will open the retrieve panel where the user will select the exportation parameters.

.. thumbnail:: ../img/cookbook/optical_mosaic/retrieve.png
    :title: the last panel of the optical mosaic: the exportation
    :group: optical-mosaic-recipe


bands
"""""

The user need to select the band to export in the mosaic. There are no max number of bands but exporting useless band will only increase the size of the output. 

.. tip:: 

    There is no fixed rule to the band selection. Each index is more adapted to a set of analyses in a defined biome. The knowledge of the study area, the evolution expected and the careful selection of an adapted band combination will improve the quality of the downstream analysis.

raw bands
#########

-   :guilabel:`blue`: blue
-   :guilabel:`green`: green 
-   :guilabel:`red`: red 
-   :guilabel:`nir`: near infrared 
-   :guilabel:`swir1`: shortwave infrared 1 
-   :guilabel:`swir2`: shortwave infrared 2 

derived bands
#############

-   :guilabel:`aerosol`: aerosol attributes
-   :guilabel:`thermal`: thermal
-   :guilabel:`thermal2`: thermal2

tasseled cap
############

-   :guilabel:`brightness`: brightness from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
-   :guilabel:`greeness`: greeness from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
-   :guilabel:`wetness`: wetness from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
-   :guilabel:`fourth`: fourth from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
-   :guilabel:`fifth`: fifth from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
-   :guilabel:`sixth`: sixth from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__

indexes
#######

-   :guilabel:`NDVI`: `Normalized difference vegetation index <https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index>`__
-   :guilabel:`NDMI`: `Normalized Difference Moisture Index <http://dx.doi.org/10.1016/S0034-4257(01)00318-2>`__
-   :guilabel:`NDWI`: `Normalized difference water index <https://en.wikipedia.org/wiki/Normalized_difference_water_index>`__  
-   :guilabel:`MNDWI`: `Modified Normalized Difference Water Index <https://doi.org/10.1080/01431160600589179>`__ 
-   :guilabel:`NDFI`: `Normalized Difference Fraction Index <http://10.1016/j.jag.2016.06.020>`__ 
-   :guilabel:`EVI`: `Enhanced vegetation index <doi:10.1016/S0034-4257(02)00096-2>`__
-   :guilabel:`EVI2`: Two-band EVI (Enhanced vegetation index)
-   :guilabel:`SAVI`: `Soil-Adjusted Vegetation Index <http://dx.doi.org/10.1016/0034-4257(88)90106-X>`__
-   :guilabel:`NBR`: `Normailzed burn ratio <https://doi.org/10.2737/RMRS-GTR-164>`__
-   :guilabel:`UI`: Urban index
-   :guilabel:`NDBI`: `Normalized Difference Built-up Index <#>`__
-   :guilabel:`IBI`: Index based built-up index
-   :guilabel:`BUI`: Built-up Index

scale 
"""""

You can set a custom scale for exportation by changing the value of the slider (m).Requesting smaller resolution than images native resolution will not improve the quality of the output, just its size so keep in mind that Sentinel data native resolution is 10 m and Landsat is 30 m. 

destination
"""""""""""

The user can export the image to :guilabel:`sepal workspace` or to ;guilabel:`google earth engine asset`. The exact same image will be exported but in the first case the user will find it in :code:`.tif` format in the :code:`downloads` folder, in the seconde one the image will be exported to the user GEE account asset list. 

.. warning::

    If :guilabel:`google earth engine asset` is not displayed, it means that the user GEE account is not connected to SEPAL, please refer to `Connect SEPAL to GEE <../setup/gee.html>`__.

you can click on :guilabel:`appply` to start the downloading. 

Exportation status
""""""""""""""""""

Going to the task tab (bottom left corner using the :icon:`fa fa-tasks` or :icon:`fa fa-spinner` buttons —depending on the loading status—), you will see the list of the different loading tasks. The interface will provide you with information about the task progress and it will display an error if the exportation has failed. If you are unsatisfied with the way we present information, the task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    This operation is running between GEE and SEPAL servers in the background, you can thus close the SEPAL page without killing the process.

When the task is finished the frame will be displayed in green as shown on the second image.

.. thumbnail:: ../img/cookbook/time_series/download.png
    :width: 49%
    :title: Evolution of the downloading process of the recipe displayed in the task manager of SEPAL.
    :group: time-series-recipe

.. thumbnail:: ../img/cookbook/time_series/download_complete.png
    :width: 49%
    :title: Completed downloading process of the recipe displayed in the task manager of SEPAL.
    :group: time-series-recipe

Access
""""""

Once the downloading process is done, you can access the data in your SEPAL folders. The data will be stored in the :code:`downloads` folder using the following format:

.. code-block::

    .
    └── downloads/
        └── <MO name>/
            ├── <MO name>_<gee tile id>.tif
            ├── <MO name>_<gee tile id>.tif
            ├── ...
            ├── <MO name>_<gee tile id>.tif
            └── <MO name>_<gee tile id>.vrt

.. danger::

    Understanding how images are stored in an Optical Mosaic is only required if you want to manually use them. The SEPAL applications are bound to this tiling sytem and can digest this information for you.

The data are stored in a folder using the name of the Optical mosaic as it was set in the first section of this document. As the number of data is spatially too big to be exported at once, the data are cut into small pieces and brought back together in a :code:`<MO name>_<gee tile id>.vrt` file. 

.. tip:: 

    The full folder with a concistent treefolder is required to read the `.vrt`

.. important::

    Now that you have downloaded the MO to your SEPAL or/and GEE account, it can be retrieved to your computer using `FileZilla <../setup.filezilla.html>`__ or used in other SEPAL workflows.
