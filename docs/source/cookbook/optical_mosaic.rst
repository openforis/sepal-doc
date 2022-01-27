Optical mosaic
==============

Overview 
--------

A mosaic is a combination or fusion of two or more images. In SEPAL, you can create a single raster dataset from several raster datasets by mosaicing them together.
This can be achieved on contiguous rasters (left) but also on overlapping images (right). 

.. thumbnail:: ../_images/cookbook/optical_mosaic/mosaic_contiguous.gif
    :width: 49%
    :group: optical-mosaic-recipe

.. thumbnail:: ../_images/cookbook/optical_mosaic/mosaic_overlay.png
    :width: 49%
    :group: optical-mosaic-recipe

These overlay areas can be managed in various ways. For example, you can choose to keep only the raster data from the first or last dataset, combine the values of the overlay cells using a weighting algorithm, average the values of the overlay cells or take the maximum or minimum value. In addition, certain corrections can be made to the image to correct for clouds, snow etc. These operations are complex and repetitive. SEPAL offers you an interactive and intuitive way to create mosaics on any AOI.

.. warning::

    You won't be able to retrieve the images if your SEPAL and GEE accounts are not connected. Follow `Connect SEPAL to GEE <../setup/gee.html>`__ to know more.


Start
-----

Once the mosaic recipe is selected, SEPAL will show up the recipe process in a new tab (1) and the AOI selection window will open itself on the bottom right side (2). 

.. thumbnail:: ../_images/cookbook/optical_mosaic/landing.png
    :group: optical-mosaic-recipe
    :title: the landing page of the optical mosaic recipe

The first step is to change the name of the recipe. This name will be used to name your files and recipes in the SEPAL folders. Use the best-suited convention for your need. Simply double-click the tab and write a new name. It will default to :code:`Optical_mosaic_<start_date>_<end_date>_<band name>`.

.. thumbnail:: ../_images/cookbook/optical_mosaic/default_title.png
    :title: optical mosaics default title 
    :width: 49%

.. thumbnail:: ../_images/cookbook/optical_mosaic/modified_title.png
    :title: optical mosaics modified title 
    :width: 49%
    
.. note::

    The SEPAL team recommends using the following naming convention: :code:`<aoi name>_<dates>_<measure>`.


Parameters 
----------

On the bottom right corner, 5 tabs are available. They will allow you to customize the time series to your needs.

-   :guilabel:`AOI`: the Area of interest (AOI)
-   :guilabel:`DAT`: the dates of the time series
-   :guilabel:`SRC`: the sources datasets of the time series
-   :guilabel:`SCN`: the scene selection parameters
-   :guilabel:`CMP`: the composition parameters

.. thumbnail:: ../_images/cookbook/optical_mosaic/no_parameters.png
    :title: The 5 tabs to set up SEPAL optical mosaic parameters
    :group: optical-mosaic-recipe

AOI Selection
^^^^^^^^^^^^^

The data exported by the recipe will be cut to the bounds of the AOI. There are multiple ways to select the AOI in SEPAL:

-   Administrative boundaries
-   EE Tables
-   Drawn polygons

.. thumbnail:: ../_images/cookbook/optical_mosaic/aoi_landing.png
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

.. thumbnail:: ../_images/cookbook/time_series/aoi_administrative.png
    :title: Select AOI based on administrative layers
    :group: optical-mosaic-recipe

EE table
""""""""

You can use custom AOI defined by shapes. These shapes need to be ingested in EarthEngine as a :code:`ee.FeatureCollection`. Select :guilabel:`EE table`.

In the first dropdown, provide a completely qualified GEE asset name (e.g. :code:`projects/gtfp-fao/assets/aoi_ecowas`). 

.. warning::

    You must have access to this asset. If that's not the case ask the owner of the asset to modify the sharing parameters.

-   Select :guilabel:`include all` and the whole geometries associated with the features will be used as AOI. 
-   Select :guilabel:`filter` and you will be able to provide a column name and a value to filter within the table. The Aoi will then be reduced to the filtered features of the initial asset. 

A buffer can be applied on these boundaries, define its size using the provided slider (in km). It is by default set to 0 i.e. disabled. 

.. note:: 

    The area of interest and the preview will take longer to show up when buffering is enabled.

Once all the parameters are selected, the AOI will be previewed in the small map at the bottom of the frame. To validate it click on :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom on the AOI and draw it in grey on the map.

.. thumbnail:: ../_images/cookbook/time_series/aoi_table.png
    :title: Select AOI based on EE table
    :group: optical-mosaic-recipe

Draw polygon
""""""""""""

You can use custom AOI defined by a drawn shape. This shape will be converted into a :code:`ee.FeatureCollection` on the fly. Select :guilabel:`draw a polygon` to use this option.

The pointer in the map will be converted into a :icon:`fa fa-plus`. Click successively on the map to draw a polygon.

Once the geometry is closed, the AOI will be previewed in the small map at the bottom of the frame. To validate it click on :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom on the AOI and draw it in grey on the map.

.. thumbnail:: ../_images/cookbook/time_series/aoi_polygon.png
    :title: Select AOI based on drawn polygon
    :group: optical-mosaic-recipe

Date
^^^^

Yearly mosaic
"""""""""""""

In the :guilabel:`DAT` tab, you will be asked to select a year. It will define the year which pixels in the mosaic should come from. When the selection is done click on :icon:`fa fa-check` :guilabel:`apply` button.

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_year.png
    :title: The year selection panel
    :group: optical-mosaic-recipe

Seasonal mosaic
"""""""""""""""

Click on :guilabel:`more` in the :guilabel:`DAT` panel to expand the date selection tool. Now instead of selecting a year, you can select a season of interest. 

Click on the :icon:`fa fa-calendar` (1) to open the date selection popup. The selected date will be the target of the mosaic, i.e the date from which pixels in the mosaic should ideally come. 

Now using the main slider (2) define a season around the target date. This season defines the 2 dates in between which SEPAL can retrieve the mosaic images. 

The number of images on one single season of one year may not be enough to produce a correct mosaic. SEPAL provides 2 secondary sliders to increase the pool of images to create the mosaic. Both count the number of seasons SEPAL can retrieve in the past (:code:`past season` - (3)) and in the future (:code:`future season` - (4)). 

When the selection is done click on :icon:`fa fa-check` :guilabel:`apply` button.

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_season.png
    :title: The season selection panel
    :group: optical-mosaic-recipe

Sources
^^^^^^^

As mentioned in the introduction, a mosaic uses different raster datasets and they can be obtained from multiple sources. SEPAL allows you to select data from multiple entry points, below you can find a description of these sources (click on the link to see the corresponding dataset information):

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

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_source.png
    :title: The source selection panel
    :group: optical-mosaic-recipe

To validate your selection, click on :icon:`fa fa-check` :guilabel:`Apply` button.

Scenes
^^^^^^

.. warning:: 

    If Sentinel and Landsat data have been selected, you will be forced to use all scenes. As the tilling system from Sentinel and Landsat data are different, it's impossible to select scenes using the tool presented in the next sections.

You can use multiple options to select the best scenes for your mosaic. The most simple is to use every image available based on the date parameters. Click :guilabel:`use all scenes` and all the images will be integrated into the mosaic. 

Select :guilabel:`select scenes` and 3 new selection options will become available. SEPAL is sorting the images available for each tile, three :code:`priority` options are available, choose the one that suits your analysis: 

-   :guilabel:`cloud free`: will give priority to images with zero or few clouds. 
-   :guilabel:`target date`: will give priority to images that match with the target date 
-   :guilabel:`balanced`: will give priority to images that maximize both cloud and target date.

To validate your selection, click on :icon:`fa fa-check` :guilabel:`Apply` button.

.. thumbnail:: ../_images/cookbook/optical_mosaic/scene_method.png
    :title: The source selection panel
    :group: optical-mosaic-recipe

Composite
^^^^^^^^^

.. note:: 

    This step is optional, SEPAL provides the folowing options by default: 

    -   **Correction**: :guilabel:`SR`, :guilabel:`BRDF`
    -   **Pixel filters**: no filters
    -   **Cloud detection**: :guilabel:`QA bands`, :guilabel:`Cloud score`
    -   **Cloud masking**: :guilabel:`Moderate`
    -   **Cloud buffering**: :guilabel:`None`
    -   **Snow masking**: :guilabel:`On`
    -   **Composing method**: :guilabel:`medoid`

To create a mosaic, you will need to provide SEPAL with the compositing method to create the final image. Here is a description of all the possible compositing options available. 

.. thumbnail:: ../_images/cookbook/optical_mosaic/composite_options.png
    :title: The panel to select the composite options of your mosaic
    :group: optical-mosaic-recipe

Corrections
"""""""""""

This will apply corrections on the stacked pixels to improve the quality of the mosaic.

-   :guilabel:`SR`: Surface reflectance improves comparison between multiple images over the same region by accounting for atmospheric effects such as aerosol scattering and thin clouds, which can help in the detection and characterization of Earth surface change. Top of atmosphere images are used if not selected.
-   :guilabel:`BRDF`: Uses a Bidirectional reflectance distribution function (BRDF) model to characterize surface reflectance anisotropy. For a given land area, the BRDF is established based on selected multiangular observations of surface reflectance.
-   :guilabel:`calibrate`:  Calibrates Sentinel and Landsat data to make them compatibles
    
    .. note:: 
        
        This option is only available if Landsat and sentinel data are mixed. You also need to unselect the BRDF and SR corrections.

Pixel filters
"""""""""""""

Activating any of the filters will remove some pixels from the stack. Removing pixels improve the quality of the mosaic pixel as they are not taken into account in the median value computation.

.. warning:: 

    Each filter is applied iteratively. Meaning that if NDVI is already filtering all pixels but one, there will be nothing left in the stack to be filtered by day of the year. 
    Note as well that adding filters increase significantly the creation time of the mosaic.

-   **Shadow**: filter the xx% darkest pixels of the stack
-   **Haze**: compute a haze index and filter the xx% highest values
-   **NDVI**: compute the NDVI and only keep the xx% highest values
-   **Day of the year**: compute the distance from target day in days and filter out the xx% farthest.

Cloud detection 
"""""""""""""""

It refers to the algorithm used to detect clouds. 

-   :guilabel:`QA bands`: use QA bands to identify clouds in Sentinel data.
-   :guilabel:`Cloud score`: Use the computed cloud score to identify clouds in Landsat data.
-   :guilabel:`Pino 26`: Use the Pino_26 algorithm to identify clouds (`D. Simonetti, 2021 <https://doi.org/10.1016/j.dib.2021.107488>`__).

    .. warning:: 

        This filter is only available for Sentinel exclusive source and when both :guilabel:`BRDF` and :guilabel:`SR` correction are disabled.

Cloud masking 
"""""""""""""

Controls how clouds will be masked based on the cloud detection algorithm selected. 

-   :guilabel:`off`: Use cloud-free pixels if possible, but don't mask areas without cloud-free pixels.
-   :guilabel:`moderate`: Rely only on image source QA bands for cloud masking. Moderate threshold is used.
-   :guilabel:`aggressive`: Rely on image source QA bands and a cloud scoring algorithm for cloud masking with an aggressive threshold. This will probably mask out some built-up areas and other bright features.

Cloud buffering
"""""""""""""""

When pixels are identified as clouds, SEPAL can remove pixels in a small buffer around it to prevent hazy pixels at the border of clouds to be included in the mosaic. 

.. note::

    Buffering is done pixel-wised so using this option will increase significantly the creation time of the mosaic.

-   :guilabel:`none`: Don't use cloud buffering
-   :guilabel:`moderate`: Mask an additional **120m** around each larger cloud. 
-   :guilabel:`aggressive`: Mask an additional 600m around each larger cloud. 

Snow masking
""""""""""""

Define how snowy pixels will be masked.

-   :guilabel:`on`: Mask snow. This tends to leave some pixels with shadowy snow.
-   :guilabel:`off`: Don't mask snow. Note that some clouds might get misclassified as snow, and because of this, disabling snow masking might lead to cloud artifacts.

Composing method
""""""""""""""""

After filtering the stack of pixels, SEPAL will compute the median value on the different bands of the image. The composing method will define how the final pixel value is extracted. 

-   :guilabel:`medoid`: Use the closest pixel from the median value. As a real pixel from the stack the final value will embed metadata (like the date of observation)
-   :guilabel:`median`: Use the computed value of the median. If no pixel is matching this value, the pixel will not embed any metadata. It tends to produce smoother mosaics. 

Analysis
--------

After selecting the parameters you can start interacting with the scenes and start the analysis.
On the top right corner, three tabs are available. They will allow you to customize the mosaic scene selection and export the final result.

-   :icon:`fas fa-magic`: auto-select scenes
-   :icon:`fas fa-trash`: clear selected scenes
-   :icon:`fas fa-cloud-download-alt`: retrieve mosaic

.. thumbnail:: ../_images/cookbook/optical_mosaic/analysis.png
    :title: The 3 tabs to select the scenes and export mosaic
    :group: optical-mosaic-recipe

.. note::

    If you have not selected the option :guilabel:`select scenes` in the :guilabel:`SCN` tab, the :icon:`fas fa-magic` button will be disabled and the scene areas (these with a number in a circle on the previous screenshot) will be hidden as no scene selection needs to be performed.
    If you can't see the image scene area, you probably have selected a small area of interest, zoom out the map and you will see the number of available images in the circles.

Select Scenes
^^^^^^^^^^^^^

To create a mosaic, you need to select the scenes that will be used to compute each pixel value of the mosaic. To do so, SEPAL provides a user-friendly interface that will help and guide you during the selection process. You don't have to select the stack for every pixel, instead, SEPAL will clip the AOI in smaller pieces called **tiles**. These tiles correspond to the native tiling system of your dataset and are displayed on the map with circled numbers in their centroid. Each number corresponds to the number of scenes available to build the mosaic tile: hover these circles to see the tile boundaries appear. 

.. note:: 

    Landsat and Sentinel datasets have a different grid system, that's why the selection process cannot be used if you have selected both of these datasets. If you have an UI idea to make them work together please let us know in our `issue tracker <https://github.com/openforis/sepal>`__, we'll be happy to implement it.

Auto-select scene 
"""""""""""""""""

Clicking on the :icon:`fas fa-magic` tab will open the auto-selection panel. 
Move the sliders to select the minimum and the maximum number of scenes SEPAL should select in a tile, then click on the :guilabel:`validate` button to apply the auto-select method. 
SEPAL will use the priority defined in the :guilabel:`SCN` tab to order the scene and pick up the optimal number for your request.

.. tip:: 

    The result is never perfect but can be used as a starting point for manual selection of scenes.

.. thumbnail:: ../_images/cookbook/optical_mosaic/auto-select.png
    :title: Panel to select the minimum and maximum number of scenes to auto select in each tile
    :group: optical-mosaic-recipe

Clear all scene
"""""""""""""""

If at least 1 scene is selected, the :icon:`fas fa-trash` tab will be available. Click on it to open the clear panel. 
Click on :guilabel:`clear scenes` and all the scenes selected (manually or automatically) will be removed. 

.. thumbnail:: ../_images/cookbook/optical_mosaic/remove_all.png
    :title: The panel to unselect all the scenes from the mosaic
    :group: optical-mosaic-recipe

Manual selection
""""""""""""""""

Hover a tile circled-number and click on it to open the scene selection menu (1). This window is divided in two sections: 

-   Available scene (2): All the available scenes according to the parameters you selected. These scenes are ordered using the :code:`priority` parameter you set in :guilabel:`SCN` tab. 
-   Selected scenes (3): The scenes that are currently selected. 

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_scenes.png
    :title: The popup window used to select individual scenes for one single tile
    :group: optical-mosaic-recipe

Each thumbnail represents a scene of the tile stack and you have the option to include them in the mosaic. The scenes located on the left side are the **available scenes** and the **available scene** are on the right side. In both cases multiple information can be found on the thumbnail: 

-   A small preview of the scene in the *red, blue, green* band combination
-   The exact date in yyyy-mm-dd of the scene
-   The satellite name :icon:`fas fa-satellite-dish`
-   The cloud coverage of the scene in % and its position in the stack values :icon:`fas fa-cloud`: 
-   The distance from target day in days within the season and its position in the stack values :icon:`fas fa-calendar-check`: 

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_available.png
    :width: 24%
    :title: the thumbnail of a scene when it's in the available scene area
    :group: optical-mosaic-recipe

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_selected.png
    :width: 74%
    :title: the thumbnail of a scene when it's in the selected scene area
    :group: optical-mosaic-recipe

You can decide to move the scene to the **selected** area by clicking :icon:`fa fa-plus`:guilabel:`add` or move it back to **available** by clicking :icon:`fa fa-minus` :guilabel:`remove`.  

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_available_hover.png
    :width: 24%
    :title: the thumbnail of a scene when it's in the available scene area when it's hovered
    :group: optical-mosaic-recipe

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_selected_hover.png
    :width: 74%
    :title: the thumbnail of a scene when it's in the selected scene area when it's hovered
    :group: optical-mosaic-recipe

.. tip:: 

    Scenes are moved from one side to the other so they are not duplicated and cannot be selected twice. Be careful if your connection is slow, wait for the thumbnail to move before clicking again. If you click too fast you could select 2 different images instead of one.

Once you are happy with your selection, click the :guilabel:`apply` button to close the window and use the selected scenes to compute the mosaic on this tile. When the window is closed, SEPAL resets the rendering of all the tiles.

Retrieve
^^^^^^^^

Clicking on the :icon:`fas fa-cloud-download-alt` tab will open the retrieve panel where the you can select the exportation parameters.

.. thumbnail:: ../_images/cookbook/optical_mosaic/retrieve.png
    :title: the last panel of the optical mosaic: the exportation
    :group: optical-mosaic-recipe


Bands
"""""

You need to select the band to export in the mosaic. There is no max number of bands, however, exporting useless bands will only increase the size and the time of the output. 

.. tip:: 

    There is no fixed rule to the band selection. Each index is more adapted to a set of analyses in a defined biome. The knowledge of the study area, the evolution expected and the careful selection of an adapted band combination will improve the quality of the downstream analysis.

Raw bands
#########

-   :guilabel:`blue`: blue
-   :guilabel:`green`: green 
-   :guilabel:`red`: red 
-   :guilabel:`nir`: near infrared 
-   :guilabel:`swir1`: shortwave infrared 1 
-   :guilabel:`swir2`: shortwave infrared 2 

Derived bands
#############

-   :guilabel:`aerosol`: aerosol attributes
-   :guilabel:`thermal`: thermal
-   :guilabel:`thermal2`: thermal2

Tasseled cap
############

-   :guilabel:`brightness`: brightness from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
-   :guilabel:`greeness`: greeness from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
-   :guilabel:`wetness`: wetness from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
-   :guilabel:`fourth`: fourth from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
-   :guilabel:`fifth`: fifth from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__
-   :guilabel:`sixth`: sixth from `Tasseled cap bands <https://en.wikipedia.org/wiki/Tasseled_cap_transformation>`__

Indexes
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

Dates
#####

-   :guilabel:`dayofyear`: the julian date (day of the year) 
-   :guilabel:`dayfromtarget`: the distance to the target date within the season in days

Scale 
"""""

You can set a custom scale for exportation by changing the value of the slider (m). Requesting a smaller resolution than images native resolution will not improve the quality of the output, just its size so keep in mind that Sentinel data native resolution is 10 m and Landsat is 30 m. 

Destination
"""""""""""

You can export the image to :guilabel:`sepal workspace` or to ;guilabel:`google earth engine asset`. The same image will be exported but in the first case you will find it in :code:`.tif` format in the :code:`downloads` folder, in the second one the image will be exported to your GEE account asset list. 

.. warning::

    If :guilabel:`google earth engine asset` is not displayed, it means that your GEE account is not connected to SEPAL, please refer to `Connect SEPAL to GEE <../setup/gee.html>`__.

Click on :guilabel:`apply` to start the download process. 

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

Once the download process is done, you can access the data in your SEPAL folders. The data will be stored in the :code:`downloads` folder using the following format:

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

    Understanding how images are stored in an Optical Mosaic is only required if you want to manually use them. The SEPAL applications are bound to this tiling system and can digest this information for you.

The data are stored in a folder using the name of the Optical mosaic as it was set in the first section of this document. As the number of data is spatially too big to be exported at once, the data are cut into small pieces and brought back together in a :code:`<MO name>_<gee tile id>.vrt` file. 

.. tip:: 

    The full folder with a consistent tree folder is required to read the `.vrt`

.. important::

    Now that you have downloaded the MO to your SEPAL or/and GEE account, it can be retrieved to your computer using `FileZilla <../setup.filezilla.html>`__ or used in other SEPAL workflows.
