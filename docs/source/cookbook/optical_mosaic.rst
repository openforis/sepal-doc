Optical mosaic
==============

Overview 
--------

A mosaic is a combination or fusion of two or more images. In SEPAL, you can create a single raster dataset from several raster datasets by mosaicing them together.
This can be achieved on both contiguous rasters (left) and overlapping images (right). 

.. thumbnail:: ../_images/cookbook/optical_mosaic/mosaic_contiguous.gif
    :width: 49%
    :group: optical-mosaic-recipe

.. thumbnail:: ../_images/cookbook/optical_mosaic/mosaic_overlay.png
    :width: 49%
    :group: optical-mosaic-recipe

These overlay areas can be managed in various ways. For example, you can choose to keep only the raster data from the first or last dataset, combine the values of the overlay cells using a weighting algorithm, average the values of the overlay cells, or take the maximum or minimum value. In addition, certain corrections can be made to the image to account for clouds, snow, and other factors. These operations are complex and repetitive. SEPAL offers you an interactive and intuitive way to create mosaics in any area of interest (AOI).

.. Note::

    You won't be able to retrieve the images if your SEPAL and Google Earth Engine (GEE) accounts are not connected. Navigate to `Connect SEPAL to GEE <../setup/gee.html>`__ to learn more.


Start
-----

Once the mosaic recipe is selected, SEPAL will display the recipe process in a new tab (1) and the AOI selection window will appear on the lower-right side (2). 

.. thumbnail:: ../_images/cookbook/optical_mosaic/landing.png
    :group: optical-mosaic-recipe
    :title: The landing page of the optical mosaic recipe.

The first step is to change the name of the recipe. This name will be used to identify your files and recipes in SEPAL folders. Use the best-suited convention for your needs. Simply double-click the tab and write a new name. It will default to :code:`Optical_mosaic_<start_date>_<end_date>_<band name>`.

.. thumbnail:: ../_images/cookbook/optical_mosaic/default_title.png
    :title: Optical mosaics default title. 
    :width: 49%

.. thumbnail:: ../_images/cookbook/optical_mosaic/modified_title.png
    :title: Optical mosaics modified title. 
    :width: 49%
    
.. note::

    The SEPAL team recommends using the following naming convention: :code:`<aoi name>_<dates>_<measure>`.


Parameters 
----------

In the lower-right corner, 5 tabs are available. They will allow you to customize the mosaic creation to your needs.

-   :guilabel:`AOI`: area of interest
-   :guilabel:`DAT`: target date of interest for the mosaic/composite
-   :guilabel:`SRC`: source datasets of the mosaic/composite
-   :guilabel:`SCN`: scene selection parameters
-   :guilabel:`CMP`: composition parameters

.. thumbnail:: ../_images/cookbook/optical_mosaic/no_parameters.png
    :title: The 5 tabs to set up SEPAL optical mosaic parameters.
    :group: optical-mosaic-recipe

AOI Selection
^^^^^^^^^^^^^

The data exported by the recipe will be generated from within the bounds of the AOI. There are multiple ways to select the AOI in SEPAL:

-   Administrative boundaries
-   EE Tables
-   Drawn polygons

.. thumbnail:: ../_images/cookbook/optical_mosaic/aoi_landing.png
    :title: The 3 different ways to select an AOI in SEPAL.
    :group: optical-mosaic-recipe

.. tip:: 

    The choice of type made at this step is not definitive. To change it, simply click on :icon:`fa fa-globe` :guilabel:`<the selected method>` in the top of the AOI window and a drop-down menu will allow you to switch between the mentioned methods.

Administrative boundaries
"""""""""""""""""""""""""

You can select administrative layers as an AOI. These geometries are extracted from the `FAO GAUL Level 1 <https://data.apps.fao.org/map/catalog/srv/eng/catalog.search?id=12691#/metadata/9c35ba10-5649-41c8-bdfc-eb78e9e65654>`__ dataset available on `GEE <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1>`__. Choose :guilabel:`Select country/province`. 

.. note::

    As GEE does not support non-Latin characters, accents and special characters have been removed from country and province names.

In the first drop-down menu, you will be able to select a country (administrative layer 0) from the Country list.  
If desired, you can also select a province (Administrative level 1) within the selected country. The drop-down list is updated on the fly according to the country selection. If nothing is selected, the whole country will be considered.

A buffer can be applied on these boundaries. Define its size in kilometers (km) by using the provided slider. It is set to 0 by default (buffer disabled).

.. note:: 

    The AOI and preview will take longer to display when buffering is enabled.

Once all the parameters are selected, the AOI will be previewed in the small map at the bottom of the frame. To validate it, click on the :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom into the AOI, which will be outlined in gray.

.. thumbnail:: ../_images/cookbook/time_series/aoi_administrative.png
    :title: Select AOI based on administrative layers.
    :group: optical-mosaic-recipe

EE table
""""""""

You can use custom AOI defined by shapes. These shapes need to be ingested in EarthEngine as a :code:`ee.FeatureCollection`. Select :guilabel:`EE table`.

In the first drop-down menu, provide a completely qualified GEE asset name (e.g. :code:`projects/gtfp-fao/assets/aoi_ecowas`). 

.. Note::

    You must have access to this asset. If you don't, ask the asset's owner to modify the sharing settings to grant you access.

-   Select :guilabel:`Include all` and the geometries associated with the features will be used as AOI. 
-   Select :guilabel:`Filter` and you will be able to provide a column name and a value to filter within the table. The AOI will then be reduced to the filtered features of the initial asset. 

A buffer can be applied on these boundaries. Define its size (in km) by using the provided slider. It is set to 0 by default (buffer disabled). 

.. note:: 

    The AOI and the preview will take longer to show up when buffering is enabled.

Once all the parameters are selected, the AOI will be previewed in the small map at the bottom of the frame. To validate it, click on the :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom in on the AOI, which will be outlined in gray.

.. thumbnail:: ../_images/cookbook/time_series/aoi_table.png
    :title: Select AOI based on EE table.
    :group: optical-mosaic-recipe

Draw polygon
""""""""""""

You can use custom AOI defined by a drawn shape. This shape will be converted into a :code:`ee.FeatureCollection` on the fly. Select :guilabel:`Draw a polygon` to use this option.

The pointer in the map will be converted into a :icon:`fa fa-plus`. Click successively on the map to draw a polygon.

Once the shape is complete, the AOI will be previewed in the small map at the bottom of the frame. To validate it, click on :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom in on the AOI, which will be outlined in gray.

.. thumbnail:: ../_images/cookbook/time_series/aoi_polygon.png
    :title: Select AOI based on drawn polygon.
    :group: optical-mosaic-recipe

Date
^^^^

Yearly mosaic
"""""""""""""

In the :guilabel:`DAT` tab, you will be asked to select a year. It will define the year which pixels in the mosaic should come from. When the selection is done, click on the :icon:`fa fa-check` :guilabel:`Apply` button.

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_year.png
    :title: The year selection panel.
    :group: optical-mosaic-recipe

Seasonal mosaic
"""""""""""""""

Click on :guilabel:`More` in the :guilabel:`DAT` panel to expand the date selection tool. Rather than selecting a year, you can select a season of interest. 

Click on the :icon:`fa fa-calendar` (1) to open the date selection pop-up. The selected date will be the target of the mosaic (the date from which pixels in the mosaic should ideally come). 

Using the main slider (2) define a season around the target date. This season defines two dates: a starting date and an ending date. SEPAL will then retrieve the mosaic images between those dates. 

The number of images in one single season of one year may not be enough to produce a correct mosaic. SEPAL provides two secondary sliders to increase the pool of images to create the mosaic. Both count the number of seasons SEPAL can retrieve in the past (:code:`Past season` - (3)) and in the future (:code:`Future season` - (4)). 

When the selection is done click on the :icon:`fa fa-check` :guilabel:`Apply` button.

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_season.png
    :title: The season selection panel.
    :group: optical-mosaic-recipe

Sources
^^^^^^^

As mentioned in the introduction, a mosaic uses different raster datasets that can be obtained from multiple sources. SEPAL allows you to select data from multiple entry points. Below, you can find a description of these sources (click on the link to see the corresponding dataset information):

-   :guilabel:`L8`: `Landsat 8 Tier 1 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1>`__. Landsat scenes with the highest available data quality are placed into Tier 1 and considered suitable for time-series processing analysis. Tier 1 includes Level-1 Precision Terrain (L1TP) processed data that have well-characterized radiometry and are inter-calibrated across the different Landsat sensors. The geo-registration of Tier 1 scenes will be consistent and within prescribed tolerances (<=12 m root mean square error [RMSE]). All Tier 1 Landsat data can be considered consistent and inter-calibrated (regardless of the sensor used) across the full collection.
    
    .. line-break::

-   :guilabel:`L8 T2`: `Landsat 8 Tier 2 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T2>`__. Scenes not meeting Tier 1 criteria during processing are assigned to Tier 2. This includes Systematic terrain (L1GT) and Systematic (L1GS) processed scenes, as well as any L1TP scenes that do not meet the Tier 1 specifications due to significant cloud cover, insufficient ground control, and other factors. Users interested in Tier 2 scenes can analyze the RMSE and other properties to determine the suitability for use in individual applications and studies.
    
    .. line-break::

-   :guilabel:`L7`: `Landsat 7 Tier 1 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T1>`__. Landsat scenes with the highest available data quality are placed into Tier 1 and are considered suitable for time-series processing analysis. Tier 1 includes Level-1 Precision Terrain (L1TP) processed data that have well-characterized radiometry and are inter-calibrated across the different Landsat sensors. The geo-registration of Tier 1 scenes will be consistent and within prescribed tolerances (<=12 m RMSE). All Tier 1 Landsat data can be considered consistent and inter-calibrated across the full collection (regardless of the sensor used).
    
    .. line-break::

-   :guilabel:`L7 T2`: `Landsat 7 Tier 2 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T2>`__. Scenes not meeting Tier 1 criteria during processing are assigned to Tier 2. This includes Systematic terrain (L1GT) and Systematic (L1GS) processed scenes, as well as any L1TP scenes that do not meet the Tier 1 specifications due to significant cloud cover, insufficient ground control, and other factors. Users interested in Tier 2 scenes can analyze the RMSE and other properties to determine the suitability for use in individual applications and studies.

    .. line-break::

-   :guilabel:`L4-5`: `Landsat 4 Tier 1 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT04_C01_T1>`__ combined with `Landsat 5 Tier 1 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T1>`__. Landsat scenes with the highest available data quality are placed into Tier 1 and are considered suitable for time-series processing analysis. Tier 1 includes Level-1 Precision Terrain (L1TP) processed data that have well-characterized radiometry and are inter-calibrated across the different Landsat sensors. The geo-registration of Tier 1 scenes will be consistent and within prescribed tolerances (<=12m RMSE). All Tier 1 Landsat data can be considered consistent and inter-calibrated across the full collection (regardless of the sensor used).

    .. line-break::

-   :guilabel:`L4-5 T2`: `Landsat 4 TM Tier 2 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT04_C01_T2>`__ combined with `Landsat 5 TM Tier 2 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T2>`__. Scenes not meeting Tier 1 criteria during processing are assigned to Tier 2. This includes Systematic terrain (L1GT) and Systematic (L1GS) processed scenes, as well as any L1TP scenes that do not meet the Tier 1 specifications due to significant cloud cover, insufficient ground control, and other factors. Users interested in Tier 2 scenes can analyze the RMSE and other properties to determine the suitability for use in individual applications and studies.
    
    .. line-break::

-   :guilabel:`A+B`: `Sentinel-2 Multispectral instrument <https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2>`__ is a wide-swath, high-resolution, multi-spectral imaging mission supporting Copernicus Land Monitoring studies, including the monitoring of vegetation, soil and water cover, as well as the observation of inland waterways and coastal areas.

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_source.png
    :title: The source selection panel.
    :group: optical-mosaic-recipe

To validate your selection, click on the :icon:`fa fa-check` :guilabel:`Apply` button.

Scenes
^^^^^^

.. note:: 

    If Sentinel and Landsat data have been selected, you will be forced to use all scenes. As the tilling system from Sentinel and Landsat data are different, it's impossible to select scenes using the tool presented in the following sections.

You can use multiple options to select the best scenes for your mosaic. The most simple is to use every image available based on the date parameters. Click :guilabel:`Use all scenes` and all of the images will be integrated into the mosaic. 

Choose :guilabel:`Select scenes` and 3 new selection options will become available. SEPAL sorts the images available for each tile. Three :code:`Priority` options are available; choose the one that suits your analysis: 

-   :guilabel:`Cloud free`: Prioritizes images with zero or few clouds. 
-   :guilabel:`Target date`: Prioritizes images that match with the target date 
-   :guilabel:`Balanced`: Prioritizes images that maximize both cloud and target date.

To validate your selection, click on the :icon:`fa fa-check` :guilabel:`Apply` button.

.. thumbnail:: ../_images/cookbook/optical_mosaic/scene_method.png
    :title: The source selection panel.
    :group: optical-mosaic-recipe

Composite
^^^^^^^^^

.. note:: 

    This step is optional. SEPAL provides the folowing options by default: 

    -   **Correction**: :guilabel:`SR`, :guilabel:`BRDF`
    -   **Pixel filters**: No filters
    -   **Cloud detection**: :guilabel:`QA bands`, :guilabel:`Cloud score`
    -   **Cloud masking**: :guilabel:`Moderate`
    -   **Cloud buffering**: :guilabel:`None`
    -   **Snow masking**: :guilabel:`On`
    -   **Composing method**: :guilabel:`Medoid`

To create a mosaic, you will need to provide SEPAL with the compositing method to create the final image. Here is a description of all of the possible compositing options available. 

.. thumbnail:: ../_images/cookbook/optical_mosaic/composite_options.png
    :title: The panel to select the composite options of your mosaic.
    :group: optical-mosaic-recipe

Corrections
"""""""""""

This will apply corrections on the stacked pixels to improve the quality of the mosaic.

-   :guilabel:`SR`: Surface reflectance improves comparison between multiple images over the same region by accounting for atmospheric effects such as aerosol scattering and thin clouds, which can help in the detection and characterization of Earth surface change. Top of atmosphere images are used if not selected.
-   :guilabel:`BRDF`: Uses a bidirectional reflectance distribution function model to characterize surface reflectance anisotropy. For a given land area, the BRDF is established based on selected multiangular observations of surface reflectance.
-   :guilabel:`Calibrate`:  Calibrates Sentinel and Landsat data to make them compatible.
    
    .. note:: 
        
        This option is only available if Landsat and Sentinel data are mixed, as well as BRDF and SR corrections are disabled.

Pixel filters
"""""""""""""

Activating any of the filters will remove some pixels from the stack. Removing pixels improves the quality of the mosaic, as they are not taken into account in the median value computation.

.. note:: 

    Each filter is applied iteratively. For example, if the Normalized difference vegetation index (NDVI) is already filtering all pixels but one, there will be nothing left in the stack to be filtered by day of the year. 
    Note as well that adding filters significantly increases the creation time of the mosaic.

-   **Shadow**: Filters the xx% darkest pixels of the stack.
-   **Haze**: Computes a haze index and filter the xx% highest values.
-   **NDVI**: Computes the NDVI and only keeps the xx% highest values.
-   **Day of the year**: Computes the distance from target day in days and filters out the xx% farthest.

Cloud detection 
"""""""""""""""

It refers to the algorithm used to detect clouds. 

-   :guilabel:`QA bands`: Uses QA bands to identify clouds in Sentinel data.
-   :guilabel:`Cloud score`: Uses the computed cloud score to identify clouds in Landsat data.
-   :guilabel:`Pino 26`: Uses the Pino_26 algorithm to identify clouds (`D. Simonetti, 2021 <https://doi.org/10.1016/j.dib.2021.107488>`__).

    .. Note:: 

        This filter is only available for Sentinel exclusive source and when both :guilabel:`BRDF` and :guilabel:`SR` correction are disabled.

Cloud masking 
"""""""""""""

Controls how clouds will be masked based on the cloud detection algorithm selected. 

-   :guilabel:`off`: Uses cloud-free pixels if possible, but doesn't mask areas without cloud-free pixels.
-   :guilabel:`moderate`: Relies only on image source QA bands for cloud masking. Moderate threshold is used.
-   :guilabel:`aggressive`: Relies on image source QA bands and a cloud scoring algorithm for cloud masking with an aggressive threshold. This will probably mask out some built-up areas and other bright features.

Cloud buffering
"""""""""""""""

When pixels are identified as clouds, SEPAL can remove pixels in a small buffer around it to prevent hazy pixels at the borders of clouds to be included in the mosaic. 

.. note::

    Buffering is done on the pixel level, so using this option will significantly increase the creation time of the mosaic.

-   :guilabel:`none`: Doesn't use cloud buffering
-   :guilabel:`moderate`: Masks an additional **120 m** around each larger cloud. 
-   :guilabel:`aggressive`: Masks an additional **600 m** around each larger cloud. 

Snow masking
""""""""""""

Define how snowy pixels will be masked.

-   :guilabel:`on`: Masks snow. This tends to leave some pixels with shadowy snow.
-   :guilabel:`off`: Doesn't mask snow. Note that some clouds might get misclassified as snow, and because of this, disabling snow masking might lead to cloud artifacts.

Composing method
""""""""""""""""

After filtering the stack of pixels, SEPAL will compute the median value on the different bands of the image. The composing method will define how the final pixel value is extracted. 

-   :guilabel:`Medoid`: Uses the closest pixel from the median value. As a real pixel from the stack, the final value will embed metadata (e.g. the date of observation).
-   :guilabel:`Median`: Uses the computed value of the median. If no pixel is matching this value, the pixel will not embed any metadata. It tends to produce smoother mosaics. 

Analysis
--------

After selecting the parameters, you can start interacting with the scenes and begin the analysis.
In the upper-right corner, three tabs are available. They will allow you to customize the mosaic scene selection and export the final result.

-   :icon:`fas fa-magic`: auto-select scenes
-   :icon:`fas fa-trash`: clear selected scenes
-   :icon:`fas fa-cloud-download-alt`: retrieve mosaic

.. thumbnail:: ../_images/cookbook/optical_mosaic/analysis.png
    :title: The 3 tabs to select the scenes and export mosaic.
    :group: optical-mosaic-recipe

.. note::

    If you have not selected the option :guilabel:`Select scenes` in the :guilabel:`SCN` tab, the :icon:`fas fa-magic` button will be disabled and the scene areas will be hidden as no scene selection needs to be performed (see those with a number in a circle on the previous screenshot).
    If you can't see the image scene area, you probably have selected a small area of interest. Zoom out on the map and you will see the number of available images in the circles.

Select Scenes
^^^^^^^^^^^^^

To create a mosaic, you need to select the scenes that will be used to compute each pixel value of the mosaic. To do so, SEPAL provides a user-friendly interface that will guide you through the selection process. You don't have to select the stack for every pixel; instead, SEPAL will clip the AOI in smaller pieces called **Tiles**. These tiles correspond to the native tiling system of your dataset and are displayed on the map with circled numbers in their centroid. Each number corresponds to the number of scenes available to build the mosaic tile; hover over these circles to see the tile boundaries appear. 

.. note:: 

    Landsat and Sentinel datasets have a different grid system, which is why the selection process cannot be used if you have selected both of these datasets. If you have an idea related to the user interface (UI) that could make them work together, please let us know in our `issue tracker <https://github.com/openforis/sepal>`__. We would be happy to implement it.

Auto-select scene 
"""""""""""""""""

Clicking on the :icon:`fas fa-magic` tab will open the auto-selection panel. 
Move the sliders to select the minimum and the maximum number of scenes SEPAL should select in a tile. Then, click on the :guilabel:`Validate` button to apply the auto-select method. 
SEPAL will use the priority defined in the :guilabel:`SCN` tab to order the scene and collect the optimal number for your request.

.. note:: 

    The result is never perfect but can be used as a starting point for the manual selection of scenes.

.. thumbnail:: ../_images/cookbook/optical_mosaic/auto-select.png
    :title: Panel to select the minimum and maximum number of scenes to auto select in each tile.
    :group: optical-mosaic-recipe

Clear all scene
"""""""""""""""

If at least one scene is selected, the :icon:`fas fa-trash` tab will be available. Click on it to open the clear panel. 
Click on :guilabel:`Clear scenes` and all the scenes selected, either manually or automatically, will be removed. 

.. thumbnail:: ../_images/cookbook/optical_mosaic/remove_all.png
    :title: The panel to unselect all the scenes from the mosaic.
    :group: optical-mosaic-recipe

Manual selection
""""""""""""""""

To open the scene selection menu, hover over a tile circled-number and click on it (1). The window will be divided into two sections: 

-   Available scene (2): All the available scenes according to the parameters you selected. These scenes are ordered using the :code:`priority` parameter you set in :guilabel:`SCN` tab. 
-   Selected scenes (3): The scenes that are currently selected. 

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_scenes.png
    :title: The pop-up window used to select individual scenes for one single tile.
    :group: optical-mosaic-recipe

Each thumbnail represents a scene of the tile stack. You have the option to include them in the mosaic. The scenes located on the left side are the **available scenes**; the **available scene** is on the right side. In both cases, the following information can be found on the thumbnail: 

-   A small preview of the scene in the *red, blue, green* band combination.
-   The exact date in yyyy-mm-dd of the scene.
-   The satellite name :icon:`fas fa-satellite-dish`.
-   The cloud coverage of the scene in % and its position in the stack values :icon:`fas fa-cloud`. 
-   The distance from target day in days within the season and its position in the stack values :icon:`fas fa-calendar-check`.

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_available.png
    :width: 24%
    :title: The thumbnail of a scene when it's in the available scene area.
    :group: optical-mosaic-recipe

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_selected.png
    :width: 74%
    :title: The thumbnail of a scene when it's in the selected scene area
    :group: optical-mosaic-recipe

You can decide to move the scene to the **Selected** area by clicking :icon:`fa fa-plus`:guilabel:`Add` or moving it back to **Available** by clicking :icon:`fa fa-minus` :guilabel:`Remove`.  

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_available_hover.png
    :width: 24%
    :title: The thumbnail of a scene when it's in the available scene area while hovering over it.
    :group: optical-mosaic-recipe

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_selected_hover.png
    :width: 74%
    :title: the thumbnail of a scene when it's in the selected scene area while hovering over it.
    :group: optical-mosaic-recipe

.. tip:: 

    Scenes are moved from one side to the other so they are not duplicated and cannot be selected twice. Be careful if your connection is slow; wait for the thumbnail to move before clicking again (if you click too fast, you could select 2 different images instead of one).

Once you are happy with your selection, click the :guilabel:`Apply` button to close the window and use the selected scenes to compute the mosaic on this tile. When the window is closed, SEPAL resets the rendering of all the tiles.

Retrieve
^^^^^^^^

Clicking on the :icon:`fas fa-cloud-download-alt` tab will open the retrieve panel where the you can select the exportation parameters.

.. thumbnail:: ../_images/cookbook/optical_mosaic/retrieve.png
    :title: The last panel of the optical mosaic: the exportation.
    :group: optical-mosaic-recipe


Bands
"""""

You need to select the band(s) to export with the mosaic. There is no maximum number of bands, but exporting useless bands will only increase the size and time of the output. 

.. tip:: 

    There is no fixed rule to the band selection. Each index is more adapted to a set of analyses in a defined biome. The knowledge of the study area, the evolution expected and the careful selection of an adapted band combination will improve the quality of downstream analysis.

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
-   :guilabel:`NDMI`: `Normalized difference moisture index <http://dx.doi.org/10.1016/S0034-4257(01)00318-2>`__
-   :guilabel:`NDWI`: `Normalized difference water index <https://en.wikipedia.org/wiki/Normalized_difference_water_index>`__  
-   :guilabel:`MNDWI`: `Modified normalized difference water index <https://doi.org/10.1080/01431160600589179>`__ 
-   :guilabel:`NDFI`: `Normalized difference fraction index <http://10.1016/j.jag.2016.06.020>`__ 
-   :guilabel:`EVI`: `Enhanced vegetation index <doi:10.1016/S0034-4257(02)00096-2>`__
-   :guilabel:`EVI2`: Two-band EVI (Enhanced vegetation index)
-   :guilabel:`SAVI`: `Soil-adjusted vegetation index <http://dx.doi.org/10.1016/0034-4257(88)90106-X>`__
-   :guilabel:`NBR`: `Normailzed burn ratio <https://doi.org/10.2737/RMRS-GTR-164>`__
-   :guilabel:`UI`: Urban index
-   :guilabel:`NDBI`: `Normalized difference built-up index <#>`__
-   :guilabel:`IBI`: Index based built-up index
-   :guilabel:`BUI`: Built-up Index

Dates
#####

-   :guilabel:`dayofyear`: The Julian calendar date (day of the year) 
-   :guilabel:`dayfromtarget`: The distance to the target date within the season in days.

Scale 
"""""

You can set a custom scale for exportation by changing the value of the slider in meters (m). (Note: Requesting a smaller resolution than images' native resolution will not improve the quality of the output, just its size, so keep in mind that Sentinel data native resolution is 10 m and Landsat is 30 m.) 

Destination
"""""""""""

You can export the image to the :guilabel:`SEPAL workspace` or to the ;guilabel:`Google Earth Engine Asset` folder. The same image will be exported to both; however, for the former, you will find it in :code:`.tif` format in the :code:`Downloads` folder; for the latter, the image will be exported to your GEE account asset list. 

.. Note::

    If :guilabel:`Google Earth Engine Asset` is not displayed, it means that your GEE account is not connected to SEPAL. Please refer to `Connect SEPAL to GEE <../setup/gee.html>`__.

Click on :guilabel:`Apply` to start the download process. 

Exportation status
""""""""""""""""""

Going to the task tab (lower-left corner using the :icon:`fa fa-tasks` or :icon:`fa fa-spinner` buttons, depending on the loading status), you will see the list of the different loading tasks. The interface will provide you with information about the task progress and it will display an error if the exportation has failed. If you are unsatisfied with the way we present information, the task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    This operation is running between GEE and SEPAL servers in the background. You can close the SEPAL page without stopping the process.

When the task is finished, the frame will be displayed in green, as shown on the second image.

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

Once the download process is complete, you can access the data in your SEPAL folders. The data will be stored in the :code:`Downloads` folder using the following format:

.. code-block::

    .
    └── downloads/
        └── <MO name>/
            ├── <MO name>_<gee tile id>.tif
            ├── <MO name>_<gee tile id>.tif
            ├── ...
            ├── <MO name>_<gee tile id>.tif
            └── <MO name>_<gee tile id>.vrt

.. Note::

    Understanding how images are stored in an optical mosaic is only required if you want to manually use them. The SEPAL applications are bound to this tiling system and can digest this information for you.

The data are stored in a folder using the name of the optical mosaic as it was set in the first section of this documentation. As the number of data is spatially too big to be exported at once, the data are cut into small pieces and brought back together in a :code:`<MO name>_<gee tile id>.vrt` file. 

.. tip:: 

    The full folder with a consistent tree folder is required to read the `.vrt`

.. important::

    Now that you have downloaded the MO to your SEPAL and/or GEE account, it can be downloaded to your computer using `FileZilla <../setup.filezilla.html>`__ or used in other SEPAL workflows.
