PyEO Forest Alerts System
=========================
*Detect deforestation over time using optical satellite imagery and change detection*

Overview
--------

Standard change detection provides just one "before and after" scenario to assess land-cover change, Python for Earth Observation (PyEO) Forest Alert System (FAS) extends this by assessing change consistency over a monitoring time-series, producing a change report. PyEO is an open-source Python library developed by the University of Leicester (Pacheco-Pascagaza *et al.,* 2022; Roberts *et al.,* 2022; Reading *et al.,* 2024).

With this recipe, SEPAL enables users to easily monitor deforestation from any Area Of Interest (AOI) using optical satellite imagery (`Landsat <https://www.usgs.gov/core-science-systems/nli/landsat/data-tools>`__ and `Sentinel-2 <https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2>`__) from the Google Earth Engine (GEE) archive. This recipe does not currently accept using radar imagery.

This tutorial will guide the user in using PyEO-FAS to monitor deforestation in 2023 across a 30 squared kilometres AOI in the Ashanti region of Ghana, by comparing land-cover against a baseline created from 2022 mosaicked optical imagery. Users can monitor *any* land-cover change (e.g. afforestation, flooding), but this tutorial will focus on detecting deforestation. It is assumed that the baseline represents a stable period of time to compare against.

Pilot Areas
-----------

For the purposes of this tutorial, you can use any of these pilot areas. This tutorial will follow the example for the Ghana pilot below.

Region 1: Ghana
^^^^^^^^^^^^^^^

===================================  =========================================================================================================
Definitions        
===================================  =========================================================================================================
Area of Interest                     Ghana, Ashanti Region
Baseline period                      2022-01-01 to 2023-01-01
Monitoring period                    2023-01-01 to 2024-01-01
Land cover classes                   Forest, Soil, and Disturbed Vegetation
Class transitions                    FROM {Forest} -> TO {Soil, Disturbed Vegetation}
Data sources                         Sentinel-2
Wavebands                            **Blue, Green, Red, NIR, SWIR1, SWIR2, Red-Edge1, Red-Edge2**, Red-Edge3, Red-Edge4, Aerosol, Water Vapor
Imagery corrections applied          Surface Reflectance only
Maximum scene cloud cover            75%
Per-pixel maximum cloud probability  20%
AOI asset path                       projects/aim4forests-499914/assets/Ghana_AOI
Training points asset path           projects/aim4forests-499914/assets/Ghana_trainingPoints
===================================  =========================================================================================================

Region 2: Kenya
^^^^^^^^^^^^^^^

===================================  =========================================================================================================
Definitions        
===================================  =========================================================================================================
Area of Interest                     Kenya, Trans Nzoia County
Baseline period                      2020-01-01 to 2021-01-01
Monitoring period                    2021-01-01 to 2022-01-01
Land cover classes                   Forest, Soil, Grassland and Urban
Class transitions                    FROM {Forest} -> TO {Soil, Grassland, Urban}
Data sources                         Sentinel-2
Wavebands                            **Blue, Green, Red, NIR, SWIR1, SWIR2, Red-Edge1, Red-Edge2**, Red-Edge3, Red-Edge4, Aerosol, Water Vapor
Imagery corrections applied          Surface Reflectance only
Maximum scene cloud cover            75%
Per-pixel maximum cloud probability  30%
AOI asset path                       projects/aim4forests-499914/assets/Kenya_AOI
Training points asset path           projects/aim4forests-499914/assets/Kenya_trainingPoints
===================================  =========================================================================================================

Region 3: Brazil
^^^^^^^^^^^^^^^^

===================================  =========================================================================================================
Definitions        
===================================  =========================================================================================================
Area of Interest                     Brazil, Mato Grosso State
Baseline period                      2019-01-01 to 2020-01-01
Monitoring period                    2020-01-01 to 2021-01-01
Land cover classes                   Forest, Soil, Grassland and Dry Forest
Class transitions                    FROM {Forest, Dry Forest} -> TO {Soil, Grassland}
Data sources                         Sentinel-2
Wavebands                            **Blue, Green, Red, NIR, SWIR1, SWIR2, Red-Edge1, Red-Edge2**, Red-Edge3, Red-Edge4, Aerosol, Water Vapor
Imagery corrections applied          Surface Reflectance only
Maximum scene cloud cover            75%
Per-pixel maximum cloud probability  30%
AOI asset path                       projects/aim4forests-499914/assets/Brazil_AOI
Training points asset path           projects/aim4forests-499914/assets/Brazil_trainingPoints
===================================  =========================================================================================================

.. attention::

    You won't be able to download the change report if your SEPAL and GEE account aren't connected. To learn more, go to `Connect SEPAL to GEE <../setup/gee.html>`__.

Start
-----

Once the **PyEO Forest Alerts System** recipe is selected, SEPAL will open the recipe process in a new tab (see **1** in the figure below). 

.. thumbnail:: ../_images/cookbook/pyeo_fas/landing.png
    :title: The landing page of the PyEO Forest Alerts System recipe.
    :group: pyeo-fas-recipe

The first step is to change the name of the recipe as it defaults to :code:`Forest_alerts_<timestamp>`, which may not be the best-suited convention to organise your recipes within SEPAL folders. Simply click the tab and enter a new name.

.. thumbnail:: ../_images/cookbook/pyeo_fas/default_title.png
    :title: Forest Change Alerts (PYEO) default title
    :width: 49%

.. thumbnail:: ../_images/cookbook/pyeo_fas/title.png
    :title: Forest Change Alerts (PYEO) modified title
    :width: 49%

.. note::

    The SEPAL team recommends using the following naming convention: :code:`Forest_alerts_<aoi_name>_<baseline_year>_<monitoring_year>_<sensor>` (e.g. :code:`Forest_alerts_GhanaAshanti_2022_2023_S2`).

Parameters
----------

In the lower-right corner, five tabs are available, allowing you to customise the Forest Alerts System to your needs:

-   :guilabel:`AOI`: Area Of Interest (AOI).
-   :guilabel:`SRC`: Source datasets of the time series.
-   :guilabel:`DAT`: Dates of the monitoring period.
-   :guilabel:`PRC`: Pre-processing parameters.
-   :guilabel:`OPT`: Change rules to apply.

We will now proceed through these steps in order, starting with :guilabel:`Area Of Interest` (see **1** in the figure below).

.. thumbnail:: ../_images/cookbook/pyeo_fas/parameters.png
    :title: The parameters of the PyEO Forest Alerts System recipe.
    :group: pyeo-fas-recipe


AOI selection
^^^^^^^^^^^^^   

The :guilabel:`AOI` tab specifies the AOI to create a change report over. There are multiple ways to select an AOI in SEPAL:

-   Administrative boundaries (country/province)
-   EE Tables
-   From the AOI of existing EE assets or SEPAL recipes
-   Drawn polygons

For more information, go to :doc:`../feature/aoi_selector`.

.. tip::

    If users wish to follow along to reproduce this workflow, use the public asset for the Ghana AOI: :code:`projects/aim4forests-499914/assets/Ghana_AOI` by following these steps:

    -   Click :guilabel:`Select from EE Table`
    -   Enter the asset path above
    -   Under :code:`Rows`, select :guilabel:`Include All`
    -   Select :btn:`<fa-solid fa-chevron-right>Next`

.. thumbnail:: ../_images/cookbook/pyeo_fas/aoi.png
    :title: Select a custom AOI
    :group: pyeo-fas-recipe

Sources
^^^^^^^

The :guilabel:`SRC` tab comprises the following parameters:

-   Classification recipe (**1**)
-   Optical datasets to use (**2**)
-   Maximum scene cloud cover for each image of the time-series (**3**)
-   From/to classes to monitor changes between (**4**)

.. thumbnail:: ../_images/cookbook/pyeo_fas/sources_tab.png
    :title: The parameters within the Sources tab
    :group: pyeo-fas-recipe

1. Classification recipe
""""""""""""""""""""""""

PyEO-FAS assesses land-cover changes by comparing classification results of images through time against a baseline image, so users need to create the image for the baseline (obtained through the **optical mosaic** recipe) and construct a classifier that will be applied to the baseline and to a monitoring time-series (using the **classification** recipe). So to proceed, users should:

A.  Create an optical mosaic as the baseline. For more information go to the :doc:`optical_mosaic` tutorial, after reading section A below.
B.  Create a machine learning classifier of the baseline. For more information go to the :doc:`classification` tutorial, after reading section B below.

Below, examples of expected outputs are shown to provide the user guidance.

**A. Optical mosaic baseline creation**

For this working example, an optical mosaic spanning 2022 will be used as the baseline and to train the classifier. Refer to the Ghana definition table in the Pilot Areas section above for the parameters needed to create the baseline.

When creating an optical mosaic, it is important to consider the spatial resolution, revisit cycle, monitoring period and wavelength bands of the available satellite programmes (currently Landsat and Sentinel-2), and decide which is most appropriate for the land-cover to monitor.

For this tutorial, Sentinel-2 is appropriate as the 10 m spatial resolution enables small dirt access roads to be identified and the AOI is small enough to not exceed Earth Engine computation timeouts. But, whilst Landsat and Sentinel-2 can both monitor deforestation *now*, only Landsat can monitor deforestation prior to 2017. Additionally, the shorter the desired monitoring period (e.g. 30 days), the greater frequency of observations are needed, so Sentinel-2 is appropriate because of its 5-day revisit time compared to Landsat (every 8 days). 

The more observations, the greater the likelihood of cloud-free imagery. For this example, the maximum cloud cover for a whole image was set to 75% and the per-pixel maximum cloud probability was set to 20%. This combination permits more images for the mosaic recipe to consider whilst still being stringent on cloud likelihood.

When finished creating the optical mosaic, it is advised to follow the instructions to export the mosaic as an EE asset, which will improve the computational speed of the classification stage to follow.

.. thumbnail:: ../_images/cookbook/pyeo_fas/sources_optical_mosaic.png
    :title: The optical mosaic to provide to the classification recipe
    :group: pyeo-fas-recipe

**B. Creating a classifier of the baseline**

.. role:: forest
.. role:: soil
.. role:: disturbed

Below is the classified 2022 optical mosaic that acts as the **baseline** which PyEO-FAS will compare changes against, and the trained classifier that will be applied to the monitoring time-series by PyEO-FAS.

.. tip:: 

    If users wish to follow along to reproduce this workflow, use the public asset for the Ghana training points: :code:`projects/aim4forests-499914/assets/Ghana_trainingPoints` when supplying land cover class training information in the :guilabel:`TRN` tab of the classification recipe.

Here, the colours of the classified baseline (right panel) correspond to :forest:`forest`, :soil:`soil` and :disturbed:`disturbed vegetation`.

.. thumbnail:: ../_images/cookbook/pyeo_fas/sources_classification.png
    :title: The classification recipe to provide to PyEO-FAS
    :group: pyeo-fas-recipe

With the classification is created, return to the PyEO-FAS recipe and select the classification recipe in the :guilabel:`SRC` tab.

.. thumbnail:: ../_images/cookbook/pyeo_fas/sources_datasets_cloud.png
    :title: The parameters within the Sources tab, with optical datasets and maximum cloud cover auto-populated from the classification recipe
    :group: pyeo-fas-recipe

2. Optical datasets
"""""""""""""""""""

Once the classification recipe is specified, the optical datasets should auto-select the same sources that were used to create the baseline. These same optical datasets will also be the basis for the monitoring time-series.

3. Maximum scene cloud cover
""""""""""""""""""""""""""""

Here the maximum cloud cover per image for the monitoring time-series can be specified, scenes that exceed this percentage will be removed from the time-series. This percentage is inherited from the parameter used to create the optical mosaic specified to the classification recipe, but can be amended. It is advised that this value is kept relatively high to permit more images for evaluation.

4. From/to classes
""""""""""""""""""

These are the classes to monitor changes between and the classes available to select are auto-populated from the classification recipe. Here the **FROM** class is set to :code:`Forest`, and the **TO** classes are set to :code:`Soil` and :code:`Disturbed Vegetation`, enabling deforestation monitoring.

.. thumbnail:: ../_images/cookbook/pyeo_fas/sources_fromto.png
    :title: The classes to monitor changes from and to, within the Sources tab.
    :group: pyeo-fas-recipe

Once these parameters are set, select :btn:`<fa-solid fa-chevron-right> Next` to continue to the next step.

Date ranges
^^^^^^^^^^^

This section concerns the time periods to observe changes. The **Baseline window** is inherited from the **classification** recipe and cannot be amended here. The date range of the **Monitoring window** to look for deforestation is specified here and auto-populates to immediately after the baseline window, for one year.

It is recommended to start this window immediately after the baseline to ensure continuity. The duration of the monitoring window is dependent on the user, and should:

-   Reflect a period where changes can persist long enough to pass the minimum change detections threshold specified later in the **change rules** window.
-   Be appropriate for the revisit time of the satellite imagery (e.g. Landsat 8 and 9: 8 days, Sentinel-2: 5 days) 

.. thumbnail:: ../_images/cookbook/pyeo_fas/dates.png
    :title: The baseline and monitoring date ranges, within the Date ranges tab.
    :group: pyeo-fas-recipe

Once the monitoring window is set, select :btn:`<fa-solid fa-check> Done`, and the change report will begin compiling.

.. tip::

    Whilst the change report will start to compute and can be investigated, it is advised to amend further parameters in the **pre-processing** and **detection rules** tabs before analysis.

Pre-processing
^^^^^^^^^^^^^^

Multiple pre-processing parameters can be set to improve the quality of the images included in the monitoring time-series, though three of the following options are automatically inherited from the optical mosaic supplied in the classification recipe.

**1. Correction**

-   :guilabel:`Surface reflectance`: Use scenes' atmospherically corrected surface reflectance.
-   :guilabel:`BRDF correction`: Correct for bidirectional reflectance distribution function (BRDF) effects, uses greater computation memory.

**2. Cloud masking**

-   :guilabel:`Moderate`: Rely only on image source QA bands for cloud masking.
-   :guilabel:`Aggressive`: Rely on image source QA bands and a cloud-scoring algorithm for cloud masking (this will probably "mask" some built-up areas and other bright features).

**3. Compositing method**

-   :guilabel:`Medoid`: Uses the pixel closest to the median value. As a real pixel from the stack, the final value embeds metadata (e.g. the date of observation).
-   :guilabel:`Median`: Uses the computed median value. If no pixel matches this value, the pixel will not embed any metadata. It tends to produce smoother mosaics.

.. thumbnail:: ../_images/cookbook/pyeo_fas/pre-process.png
    :title: The parameters for pre-processing the images of the monitoring time-series, inherited from the classification recipe.
    :group: pyeo-fas-recipe

**4. More**

One parameter may need adjusting if this was not set in the optical mosaic. Select :guilabel:`More` to access the advanced pre-processing options, and ensure :guilabel:`SEPAL cloud score` and :guilabel:`S2 Cloud Score+` are set to 20%. Per image, pixels with a cloud probability above this percentage will be masked out from the monitoring time-series. This is important to reduce the likelihood of cloudy or hazy pixels from influencing a misclassification and affecting the likelihood of a false change being reported.

.. thumbnail:: ../_images/cookbook/pyeo_fas/pre-process_more.png
    :title: The advanced parameters for pre-processing the images of the monitoring time-series.
    :group: pyeo-fas-recipe

Detection rules
^^^^^^^^^^^^^^^

.. note::

    Whilst this section is optional as these parameters are set by default, it is advised to customise these to suit the user's needs.

    -   Require index drop: :guilabel:`Yes`
    -   Index: :guilabel:`NDVI`
    -   Minimum drop: :guilabel:`0.2`
    -   Minimum consecutive changes: :guilabel:`2 images`

**Require index drop**

-   :guilabel:`Yes`: Require the index to drop by at least the chosen threshold (baseline index minus baseline monitoring) before an alert is confirmed.
-   :guilabel:`No`: Does not require an index decrease between the baseline and monitoring image, to be considered a change.

**Index**

The spectral index to monitor decreases of. Defaults to any available indices that range from 0 to 1 and is dependent on the available wavelength bands of the imagery source.

-   :guilabel:`NDVI`: Normalized Difference Vegetation Index
-   :guilabel:`NDMI`: Normalized Difference Moisture Index
-   :guilabel:`NBR`: Normalized Burn Ratio

**Minimum drop**

The minimum threshold for the index to decrease from the baseline image to the monitoring images, to be considered a change. Defaults to :guilabel:`0.2`.

**Minimum consecutive detections**

The minimum changes detected consecutively to be considered a change. Defaults to :guilabel:`2 images`.

.. thumbnail:: ../_images/cookbook/pyeo_fas/detection_rules.png
    :title: The detection rules to customise the change detection report
    :group: pyeo-fas-recipe

Analysis
--------

.. tip::

    In the upper-right corner, you can select :btn:`<fa-solid fa-cloud-arrow-down>` to download the change report to SEPAL as a GeoTIFF file or as an EE asset.

Below, is the visualisation screen users see once the change report has finished compiling. The map below is the default visualisation, the *Total Changes* layer of the change report. This layer represents the number of changes between the FROM and TO classes.

.. thumbnail:: ../_images/cookbook/pyeo_fas/analysis_default_view.png
    :title: The default analysis screen
    :group: pyeo-fas-recipe

To further understand the changes identified by PyEO-FAS, users can use additional layers of the change report and panels, like below. Here the map is split into four panes, which are:

- The baseline mosaic **(1)**
- The most recent month of the monitoring time-series (**2**)
- The total changes layer (**3**)
- The first change date decision layer (**4**).

The first change date decision layer shows the dates of all the changes that have passed the values specified by the :guilabel:`Minimum consecutive changes` and :guilabel:`Minimum drop` (if using) parameter(s). Enabling users to understand *when* a change was first detected.

.. thumbnail:: ../_images/cookbook/pyeo_fas/analysis_recommended_view.png
    :title: The analysis screen with the recommended map views
    :group: pyeo-fas-recipe

To achieve the four panel visualisation as above:

1. Select the :btn:`<fa-solid fa-layer-group>` layers-to-show icon in the top-right of the screen to open the **layers panel**.
2. To add the baseline mosaic, select :btn:`<fa-solid fa-plus> Add`, select either **Add a SEPAL recipe** or **Add an Earth Engine asset** (depending on if you exported the baseline mosaic as an asset), and specify the path to the mosaic. 
3. Drag and drop the baseline mosaic layer onto a position (centre, a side, or a corner) to choose where it appears; drag it between positions to rearrange it, or off the areas to remove it.

.. thumbnail:: ../_images/cookbook/pyeo_fas/analysis_adding_a_layer.png
    :title: The layers panel for adding additional layers of the change report and helpful imagery.
    :group: pyeo-fas-recipe

4. To add imagery of the end of the monitoring time-series, a mosaic must first be created. In another recipe window, select the **optical mosaic** recipe, specify a time-period of *2023-12-01* to *2023-12-31* and leave all remaining parameters as default. The mosaic can be exported as an asset for faster loading when navigating the map.
5. Drag the recent imagery mosaic onto the top-right of the map.
6. To add the first change date decision map, navigate to the **layers panel**, select **this recipe** and drag to the bottom-right of the map.
7. Select the :btn:`<fa-solid fa-bars>` of the bottom-right layer, change the **Bands** selector to :guilabel:`FCD decision map`.

Users are encouraged to explore the layers of the change report if they wish to, which are further explained in the Appendix. 

Export
------

To validate the class changes identified in the change report using the **PyEO-FAS Validation Module**, users need to export the change report as a :guilabel:`Google Earth Engine Asset` first.

.. important::

    You cannot export a recipe as an asset or a :code:`.tif` file without a small computation quota. If you are a new user, see :doc:`../setup/resource`.

Users can also export the change report to the :guilabel:`SEPAL workspace` in :code:`.tif` format, which can then be downloaded to the user's local drive. To learn more, go to `Exchange files with SEPAL <../setup/filezilla.html>`__.

Starting the download
^^^^^^^^^^^^^^^^^^^^^

Selecting the :icon:`fa-solid fa-cloud-arrow-down` tab will open the **Retrieve** pane where you can select the exportation parameters, namely the bands to retrieve, the scale and file type.

For more information, see the **Export** section of the :doc:`classification` tutorial.

.. thumbnail:: ../_images/cookbook/pyeo_fas/export.png
    :title: The retrieve pane of the PyEO-FAS recipe.
    :group: pyeo-fas-recipe

Operational Recommendations
---------------------------

The parameters of PyEO-FAS can be amended depending on the immediate goal: long or short-term monitoring. To quickly experiment with other parameters, users can duplicate this recipe by selecting the :btn:`<fa-solid fa-bars>` button in the top-right of the interface.

PyEO-FAS operates on the principle of assessing the consistency of land cover changes between the baseline and images within the monitoring time-series. For longer-term monitoring and to be more confident in detecting a change, users should increase the value of :guilabel:`Minimum consecutive changes`, meaning changes must persist for longer to be included in the first change date decision map. Additionally, changes with greater severity can be identified using a higher :guilabel:`Minimum drop` value. For short-term monitoring, such as over a month, a lower value for :guilabel:`Minimum consecutive changes` will report this change in the first change date decision map, but this has a greater likelihood of erroneous noise.

References
----------

Pacheco-Pascagaza, A. M., Gou, Y., Louis, V., Roberts, J. F., Rodríguez-Veiga, P., Bispo, P. da C., Espírito-Santo, F. D. B., Robb, C., Upton, C., Galindo, G., Cabrera, E., Cendales, I. P. P., Santiago, M. A. C., Negrete, O. C., Meneses, C., Iñiguez, M., & Balzter, H. (2022). Near Real-Time Change Detection System Using Sentinel-2 and Machine Learning: A Test for Mexican and Colombian Forests. *Remote Sensing*, 14(3), 1–21. https://doi.org/10.3390/rs14030707

Reading, I., Bika, K., Drakesmith, T., McNeill, C., Cheesbrough, S., Byrne, J., & Balzter, H. (2024). Due diligence for deforestation-free supply chains with Copernicus Sentinel-2 imagery and machine learning. *Forests*, 15(4), 617. https://doi.org/10.3390/f15040617

Roberts, J. F., Mwangi, R., Mukabi, F., Njui, J., Nzioka, K., Ndambiri, J. K., Bispo, P. C., Espirito-Santo, F. D. B., Gou, Y., Johnson, S. C. M., Louis, V., Pacheco-Pascagaza, A. M., Rodriguez-Veiga, P., Tansey, K., Upton, C., Robb, C., & Balzter, H. (2022). Pyeo: A Python package for near-real-time forest cover change detection from Earth observation using machine learning. *Computers & Geosciences*, 167, 105192. https://doi.org/https://doi.org/10.1016/j.cageo.2022.105192

Appendix
--------

.. note::

    This section is optional, containing additional material for users wishing to further understand the PyEO-FAS recipe.

Change Report Structure
^^^^^^^^^^^^^^^^^^^^^^^

================================== ===========
Change Report Layers               Description
================================== ===========
available_image_count              Number of images processed per pixel within the overall cloud percentage cover limit set by the user in the SEPAL Recipe GUI.
occluded_count                     Number of cloud occluded (or out-of-orbit) images unavailable for classification and analysis.
total_changes                      Number of classifier detected from/to changes.
first_change_date_above_threshold  Earliest classification change date where there is no missing data or cloud, which passed the delta index threshold.
post_fcd_change_count              Count if a change was detected after a first change has already been detected.
post_fcd_nochange_count            Count if a no change was detected after a first change has already been detected after passing an index threshold.
post_fcd_occluded_count            Count of cloud occluded (or out-of-orbit) pixels after a first change was detected.
post_fcd_valid_image_count         Count of valid (no cloud) images for this pixel since first change was detected.
post_fcd_change_repeatability_pct  Repeatability of change detection after first change is detected - as a percentage of available valid images.
binary_timeseries_decision         Boolean of changes where minimum consecutive changes threshold and a change consistency equal to or above 50% are fulfilled.
fcd_decision_map                   First change date masked by binary_timeseries_decision.
delta_index_change_count           Count if a change passed the index minimum drop threshold and was not cloud occluded (or out-of-orbit).
binary_delta_index_decision_map    Boolean based on whether the index transition between the baseline and monitoring images passed the index minimum drop threshold. Does not include whether the classifier identified this as a change.
binary_delta_class_decision_map    Boolean based on whether the classifier identified a change. Does not include whether the index transition identified a change.
binary_combined_delta_decision_map Boolean based on where binary_delta_index_decision_map and binary_delta_class_decision_map are True.
from_class_count                   Count of the FROM classifications
to_class_count                     Count of the TO classifications
binary_decision_from_to_map        Boolean based on where both from_class_count and to_class_count exceed 2.
================================== ===========