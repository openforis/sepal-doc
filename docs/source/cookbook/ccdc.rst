CCDC - Asset Creation
=====================

Background
----------

Powered by the API of `Google's Earth Engine <https://earthengine.google.com/>`_, SEPAL facilitates the workflow for applying the Continuous Change Detection and Classification (CCDC) approach as proposed by `Zhu & Woodcock 2014 <https://www.sciencedirect.com/science/article/pii/S0034425714000248>`_.

CCDC is a holistic methodological framework that encompasses various aspects of space-borne land mapping and monitoring using multi-temporal satellite imagery. The core of the method is a **temporal segmentation** algorithm applied at **pixel-level**. It is furthermore capable to utilize all available **bands** and derived *band ratios*.

CCDC is **data-agnostic**, meaning any type of multi-temporal satellite imagery can be ingested (e.g. optical, radar). SEPAL supports its usage with Landsat, Sentinel-1 & 2 as well as Planet basemaps and daily imagery. Note that for the latter, a Planet API key is necessary.

The temporal segmentation step starts by fitting a 3rd order harmonic model to each band of the initial part of the time-series. Thereafter, the observations are tested against the model for each band selected as a **breakpoint band**. In case of a significant repetitive deviation from the model, a break is flagged. Subsequently, a new segment is initialized for the upcoming observations until the next break is going to be detected.

A **CCDC asset** retains the information of change(s) happening for each pixel, including the date of the break as well as its magnitude. In addition, the model parameters are stored for the time-series segments in between those breaks. Therefore, another way of thinking about a **CCDC asset** is to consider it as a **condensed, synthetic time-series**. By only storing each segments model parameters, we drastically reduce the storage needs as opposed to store the full-time-series. At the same time, we retain the possibility to re-create the data at any given point in time by using the model's parameters.

.. warning::

    The creation of a CCDC asset is the mandatory first step for all types of subsequent workflows and analysis. This step is highly compute intense, which makes it difficult for on-the-fly-processing. An export as an Earth Engine asset is highly recommended. For this, your SEPAL account needs to be connected to your Google Earth Engine account. Follow `Connect SEPAL to GEE <../setup/gee.html>`__ to learn how to register for Google Earth Engine and connect it to your SEPAL account.


Getting Started
---------------

Create Recipe
^^^^^^^^^^^^^^

Once logged into SEPAL, open the recipe menu by clicking on the orange :btn:`<fa fa-globe>` button at the top left of the SEPAL start screen. Within the recipe menu (*see figure below*), select CCDC, which opens a new SEPAL recipe tab.

.. thumbnail:: ../_images/cookbook/ccdc_asset/recipe_selection.png
    :group: ccdc-recipe-selection
    :title: Selection menu for SEPAL recipes
    :width: 60%
    :align: center

Rename Recipe
^^^^^^^^^^^^^

The first step one should do is to change the name of the recipe by double-clicking on tab on the top of the map. This will have the effect that your recipe will be automatically saved and is visible in the list of created recipes. Furthermore, the given name will be used for exported files, both locally and on Earth Engine. We suggest to use the following convention: :code:`CCDC-asset_<aoi>_<sensor(s)>_<start_date>_<end_date>`.

.. thumbnail:: ../_images/cookbook/ccdc_asset/recipe_unnamed.png
    :title: CCDC asset default title
    :width: 40%

.. thumbnail:: ../_images/cookbook/ccdc_asset/recipe_renamed.png
    :title: CCDC assed modified title
    :width: 40%

Parameter selection
-------------------

The following steps describe the parameter selection that can be found on the lower right of the screen.

.. thumbnail:: ../_images/cookbook/ccdc_asset/ccdc_start_screen.png
    :title: CCDC assed parameters

.. line-break::

The buttons open the following dialogues:

-   :guilabel:`AOI` Area of interest (AOI)
-   :guilabel:`DAT` Time of Interest (TOI), i.e. the time-span for the underlying time-series
-   :guilabel:`SRC` Selection of sensor(s)
-   :guilabel:`PRC` Pre-processing parameters
-   :guilabel:`OPT` CCDC Parameters

Area of Interest
^^^^^^^^^^^^^^^^

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

Date Range
^^^^^^^^^^

In the :guilabel:`DAT` tab, you will be asked to select the starting date and the ending date of the time series. Click on the date tex field to open a date picker popup. Click on the :btn:`<fa fa-check> Select` button to validate a date. When both dates are selected click on :btn:`<fa fa-check> apply` button.

.. thumbnail:: ../_images/cookbook/ccdc_asset/dates.png
    :title: Select AOI based on EE table
    :width: 49%
    :group: time-series-recipe

.. thumbnail:: ../_images/cookbook/ccdc_asset/datepicker.png
    :title: Select AOI based on EE table
    :width: 49%
    :group: time-series-recipe

Sensor selection
^^^^^^^^^^^^^^^^

After clicking the :guilabel:`NEXT` button in the date selection, the sensor selection pop-up menu will automatically open (1). Here you need to specify the sensor(s) and the bands used for the breakpoint detection. You have the choice between 3 types, :guilabel:`OPTICAL` (including the Landsat and Sentinel-2 missions), :guilabel:`RADAR` (including the Sentinel-1 mission) and :guilabel:`PLANET`, where both daily imagery or monthly basemaps can be used as data input (given you have a valid Planet API key).

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_overview.png
    :title: Sensor Selection
    :width: 100%
    :group: ccdc-asset-recipe

Optical data
""""""""""""

CCDC is originally tested on optical *Landsat* satellites. In SEPAL you have the possibility to select and combine all past and present Landsat missions, including *Tier 1* and *Tier 2* collections, to run it on decadal-long time-series.

.. warning::

    The inclusion of *Tier 2* products as well as *Landsat 7* may introduce artifacts due to the reduced quality of the data. For recent short-term time-series it might be better to either select the Landsat-8 or Sentinel-2 mission, which deliver imagery from 2013 and 2015, respectively. This will however reduce the density of observations for the underlying time-series.

.. warning::

    For very cloud-prone regions, it is also possible to combine the *Landsat* data with the *Sentinel-2* data to densify the underlying time-series. Note that because of differences in the sensors (although band names are equal) and the overpass time, artifacts may be introduced that will affect the breakpoint detection.

The breakpoint detection is at the heart of CCDC. The respective selection of bands can considerably affect the outcome of the CCDC breakpoint detection. Unfortunately, there does not seem to be a *"one size fits all"* preset for all kinds of applications. Scientific evidence is suggesting to use all color bands but the blue `Zhu et al 2020 <https://www.sciencedirect.com/science/article/pii/S0034425719301002>`_. According to the study, the selection of additional ratio bands does not add any improvement. However, it should be noted that this assumption is based on the detection of all types of land cover changes and that the study uses a modified version of CCDC (named COLD), where the change in bands are weighted differently than in the original version used in SEPAL, respectively Google Earth Engine.

.. tip::

    The use of the color bands allows you to later select the :code:`Green` and the :code:`Swir1` band as TMASK bands for CCDC's internal, multi-temporal cloud removal. You find this in the :guilabel:`OPT` button pop-up menu under :guilabel:`MORE`.

If the creation of the CCDC asset is aimed at the detection of both, forest degradation and deforestation, the *Normalized Difference Fraction Index* :code:`NDFI` might be another suitable choice as applied by `Bullock et al 2020 <https://www.sciencedirect.com/science/article/pii/S0034425718305200>`_. Note that this article and the NDFI are specifically tested over tropical rainforest of the Brazilian Amazon. Changes in other forest types might be better captured by different ratios or the color bands. For instance one can consider the *Normalized Differenced Moisture Index* :code:`NDMI` when looking at Mangrove forests.

.. tip::
    In case of doubt, we suggest to go for the default option and use all of the color bands, except the blue one.

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_color_breakbands.png
    :title: Sensor Selection - Color breakpoint bands
    :width: 49%
    :group: ccdc-asset-recipe

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_ndfi_breakband.png
    :title: Sensor Selection - NDFI breakpoint band
    :width: 49%
    :group: ccdc-asset-recipe

Radar Data
""""""""""

In order to create a CCDC asset based on underlying radar time-series, you need to select the :guilabel:`RADAR` button. This will make use the *Sentinel-1* C-Band SAR Image Collection in Google Earth Engine. To the best of our knowledge, no scientific studies have been done that investigate the ideal band selection for breakpoint detection. As a starting point we suggest to use the default option that includes the :code:`VV` and the :code:`VH` band.

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_radar.png
    :title: Sensor Selection - Radar
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

Planet data
"""""""""""

For the creation of a CCDC asset based on *Planet* data, you have the choice of either selecting the *Planet custom basemaps* (including the NICFI Level 1 data), or *Planet daily imagery* itself.

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_planet.png
    :title: Sensor Selection - Planet
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

.. line-break::

In both cases, the data already needs to reside within Earth Engine as an *ImageCollection asset*, whose ID needs to be filled in the respective field.

In case you want to use the *NICFI Level-1 basemaps*, you can use the already existing assets within Earth Engine, given that you enabled the access feature as explained `here <https://docs.sepal.io/en/latest/setup/nicfi.html>`_. The NICFI Level-1 assets are split by continent and have the following Asset IDs:

-   projects/planet-nicfi/assets/basemaps/africa
-   projects/planet-nicfi/assets/basemaps/asia
-   projects/planet-nicfi/assets/basemaps/americas

.. tip::

    For data ordered through the Planet API (i.e. daily imagery or custom basemaps other than NICFI Level 1 data), you can specify Earth Engine as the download location.

Using CCDC with Planet has not been explored widely, so that again the optimal selection of the breakpoint bands depends on testing it out by yourself. However, in accordance with Landsat based analysis we suggest to use the Green , Red and NIR bands to get started.


Pre-processing options
^^^^^^^^^^^^^^^^^^^^^^


Optical data
"""""""""""""

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
-   :guilabel:`Aggressive`: rely on image source QA bands and a cloud scoring algorithm for cloud masking. This will probably mask out some built-up areas and other bright features.

**Snow masking**

-   :guilabel:`On`: mask snow. This tends to leave some pixels with shadowy snow
-   :guilabel:`Off`: don't mask snow. Note that some clouds might get misclassified as snow, and because of this, disabling snow masking might lead to cloud artifacts.


.. thumbnail:: ../_images/cookbook/ccdc_asset/pre_processing.png
    :title: The pre-processing panel to select the extra filtering processes that will improve the quality of the provided images.
    :group: time-series-recipe


Radar data
""""""""""

The default parameters (below figure on the left) are rather optimized for performance and coverage than for the highest quality of the data. It is therefore recommended to modify them accordingly (below figure on the right).

.. thumbnail:: ../_images/cookbook/ccdc_asset/prc_radar_default.png
    :title: Prc Selection - Radar default
    :width: 49%
    :group: ccdc-asset-recipe

.. thumbnail:: ../_images/cookbook/ccdc_asset/prc_radar_recommended.png
    :title: Prc Selection - Radar recommended
    :width: 49%
    :group: ccdc-asset-recipe

.. line-break::

**Orbit Selection**
The orbit selection for radar satellites refers to the flight direction of the satellite that is different from sun-adverted and the sun-facing side of the planet. One distinguishes ascending (from south pole towards north pole) and descending (from north to south pole) direction. Being independent from the sunlight, radar satellites can acquire at both, day and nighttime. However, they do not acquire constantly.

In case of the Sentinel-1 mission, areas outside of Europe are usually only covered by either one or the other. With the help of the below figure you should be able to see by which orbit direction your Area of Interest is covered.

.. image:: https://sentinels.copernicus.eu/documents/247904/3944045/Sentinel-1-Revisit-Coverage-Frequency-Geometry-2019.jpeg
    :alt: Sentinel-1 observation scenario

.. line-break::

.. warning::

    While you can select both orbits to be on the safe side, marginal areas that are covered by both orbits might result in different models than for areas only covered by on eor the other, due to the differences in observation geometry. It is therefore recommended to properly select your orbit direction. Instead, if it happens that your full AOI is covered by both orbits, do also select both.

**Geometric Correction**

Setting the *Geometric Correction* to :guilabel:`TERRAIN` will correct for distortions of the radar backscatter signal along slopes. This is crucial for all types of land cover or biogeophysical parameter retrieval and is therefore **highly recommended**.

**Speckle-Filtering**

Speckle Filtering is a common step in radar remote sensing and reduces the random noise within radar imagery. While CCDC has already a very effective filtering effect on the backscatter through the time-series modelling, selecting the multi-temporal :guilabel:`QUEGAN` shall improve the detection of breaks and is therefore recommended. However, as it is very compute intense, processing and export might take a considerable amount of time, and in some cases might even fail.

**Outlier Removal**

Sentinel-1 data is prone to some rare artifacts, such as interferences from other radio wave sources or heavy rainfall events. SEPAL offers the option to exclude them by a multi-temporal outlier detection. By default, a :guilabel:`MODERATE` reduction is appropriate to remove such artifacts. More aggressive filtering might include actual change events and is therefore not recommended.

Planet data
"""""""""""

Pre-processing parameters of Planet data are similar ot the Landsat/Sentinel-2 options. The default parameters are reflecting a quite aggressive way of cloud removal (see figure below).

.. thumbnail:: ../_images/cookbook/ccdc_asset/prc_planet_default.png
    :title: Prc Selection - Planet default
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

.. line-break::

**Histogram Matching**

Histogram Matching is by default disabled. This is ok when dealing with already pre-processed monthly basemaps. However, if the collection is composed of daily imagery, it is highy recommended to :guilabel:`ENABLE` this option as it will harmonize the radiometry between each single image.

CCDC parameters
^^^^^^^^^^^^^^^

Presets
"""""""
Behind the :guilabel:`OPT` you can find 3 basic presets of CCDC parameters.
The selection of the presets can be interpreted at selecting the balance between commission and omission error for the breakpoint detection.

.. thumbnail:: ../_images/cookbook/ccdc_asset/opt_ccdc_simple.png
    :title: Opt Selection - Simple
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

.. line-break::

- The parameters of the :guilabel:`CONSERVATIVE` are favoring commission over omission error rate in the breakpoint detection (i.e. aiming at high User Accuracy, low False Positives). In other words, CCDC is going to detect less breaks, but they are more likely to be correct. This comes at the cost of missing some actual changes, therefore having an increased omission error.

- The parameters of the :guilabel:`MODERATE` are trying to balance commission and omission errors in the breakpoint detection. In other words, CCDC is going to both, omit and commit some of the actual changes, keeping both level of error rates similar with a balanced False Positive and False Negative detection rate.

- The parameters of the :guilabel:`AGGRESSIVE` are favoring omission over commission error rate in the breakpoint detection (i.e. aiming at high Producer Accuracy, low False Negatives). In other words, CCDC is going to detect more breaks than with the other settings, reducing the likelihood of missing change. This comes at the cost of also detecting a lot of falsely detected change though.

.. tip::

    If you have chosen the color bands for breakpoint detection within the sensor menu, it is worthwile to go into the advanced options using the :guilabel:`MORE` button and select the :guilabel:`GREEN` and :guilabel:`SWIR1` band as :guilabel:`TMASK BANDS`.

Advanced Options
""""""""""""""""
More advanced users have the possibility to manually set all of the actual CCDC parameters by clicking on the :guilabel:`MORE` button.

.. thumbnail:: ../_images/cookbook/ccdc_asset/opt_ccdc_advanced.png
    :title: Opt Selection - Advanced
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

.. line-break::

**Date Format**

This option allows to safe the dates in various formats. Note that SEPAL deals by default with :guilabel:`FRACTIONAL YEARS` in all of the CCDC related recipes.

**TMASK BANDS**

The bands selected here are used for additional multi-temporal filtering of cloud affected pixels that have not been identified as such throughout the pre-processing of the single images. For optical data from Landsat and Sentinel-2, the :guilabel:`GREEN` and :guilabel:`SWIR1` bands are recommended.

**Min Observations**

This is the number of observations needed before a break is actually confirmed based on its temporal behaviour. A low number will lead to more changes and reduce the gaps between two temporal segments. Higher numbers will lead to more confidence in the observed change, but in cloud-prone regions might lead to long gaps between two temporal segments. Usually, a number between 4 to 8 is recommended.

**Chi Square Probability**

The Chi-Square test will test if an observation is part of the general statistical distribution of the time-series. A low value of Chi-Square probability will favor the rejection of the null-hypothesis (i.e. being part of the statistical distribution), therefore flagging it as possible change. Ultimately, a lower value leads to more breaks detected, which favors omission over commission error.
A high value allows for more noise in the time-series, and less changes will be detected, therefore lowering the commission error rate.

**Min Number of Years Scaler**

This parameter determines the minimum length of any inner temporal segment.

**LAMBDA**

The lambda parameter is part of the LASSO regression used for the modelling of the time-series. It is used to generalize the model and thereby improving its predictive power. More specifically, it is controlling the weight of each of the parameters, and might result even in the annulation of some of the parameters. In practical terms, an initially 3rd order harmonic model, might shrink to a 1st order harmonic, if this provides the best generalized fit. Setting lambda to 0 will lead to a regular Ordinary-Least-Square regression, not providing any generalization. Instead, a higher value will provide a more generalised model. If lambda is set too high, the model will underfit, which also not wanted. Since a value of 20 has been found to provide a generally good performance, the sweet spot of neither over nor underfitting will be around this number.

**Max iterations**

Those are the iterations for the maximum number of runs for LASSO regression convergence. If set to 0, regular OLS is used instead of LASSO.

On-the-fly Pixel analysis
-------------------------

Click on the :btn:`<fa fa-chart-area>` button to start the plotting tool (1). Move the pointer to the main map, the pointer will be transformed into a :icon:`fa fa-plus` (2). Click anywhere in the AOI to plot data for this specific location in the following popup window.

The plotting area (3) is dynamic and can be customized by the user.

You can select the observation feature by selecting one of the available measures in the dropdown selector in the top left corner (4). The available bands are the same as the described previously.

Using the slider (5), the temporal width displayed can be changed. It cannot exceed the start and/or end date of the time series.

On the main graph, the orange lines shows the CCDC modelled time-series. Each of the blue points represents an actual observation. You can both hover over the point or the line to let the tooltip describe the value and date of the observation, as well as the model values and the temporal extent of the specific segment.

.. thumbnail:: ../_images/cookbook/ccdc_asset/ccdc_pixel_analysis.png
    :title: Pixel Analysis
    :width: 100%
    :group: ccdc-asset-recipe

.. warning::

    The plot feature is retrieving information from GEE on the fly and serving it in an interactive window. This operation can take time depending on the number of available observations and the complexity of the selected pre-processing parameters. If the popup window displays a spinning wheel, wait up to 2 min to see the data displayed.


Export
------

Trigger the export task
^^^^^^^^^^^^^^^^^^^^^^^

Click on the :btn:`<fas fa-cloud-download-alt>` button to open the export dialogue. Here you can select the bands to retrieve and the scale at which you would like to save the asset. CCDC Assets are only compatible with Google Earth Engine, for which a new asset will be created in your personal Earth Engine repository.

If the area covered is relatively small and you have enough storage quota left, you can generously select most of the bands relevant for land applications as shown in the below figure on the left. If you are more constrained by storage you will need ot decide on a subset of bands, for which the below figure on the right is a suggested starting point.

The scale parameter depends on the data selected and the level of detail you will need for your further analysis. Landsat based assets are usually created at 30 meters. Sentinel-1 and 2 can be at 10 meter, but will need 9 times more space as compared to 30 meter resolution.

.. thumbnail:: ../_images/cookbook/ccdc_asset/ccdc_export_full.png
    :title: Export CCDC Asset - full band selection
    :width: 49%
    :group: ccdc-asset-recipe

.. thumbnail:: ../_images/cookbook/ccdc_asset/ccdc_export_reduced.png
    :title: Export CCDC Asset - reduced band selection
    :width: 49%
    :group: ccdc-asset-recipe


Exportation status
^^^^^^^^^^^^^^^^^^

Going to the task tab (bottom left corner using the :btn:`<fa fa-tasks>` or :btn:`<fa fa-spinner>` buttons —depending on the loading status—), you will see the list of the different loading tasks. The interface will provide you with information about the task progress and it will display an error if the exportation has failed. If you are unsatisfied with the way we present information, the task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

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
