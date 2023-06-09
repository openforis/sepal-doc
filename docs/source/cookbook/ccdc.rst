CCDC - asset creation
=====================

Background
----------

Powered by the API of `Google's Earth Engine <https://earthengine.google.com/>`_, SEPAL facilitates the workflow for applying the Continuous Change Detection and Classification (CCDC) approach, as proposed by `Zhu & Woodcock 2014 <https://www.sciencedirect.com/science/article/pii/S0034425714000248>`_.

CCDC is a holistic methodological framework that encompasses various aspects of space-borne, multitemporal land mapping and monitoring using multitemporal satellite imagery. The core of the method is a **temporal segmentation** algorithm applied at **pixel-level**. It is furthermore capable of utilizing all available **bands** and derived **band ratios**.

CCDC is "data-agnostic", meaning any type of multitemporal satellite imagery can be ingested (e.g. optical, radar). SEPAL supports its usage with Landsat, Sentinel-1 and Sentinel-2, as well as Planet basemaps and daily imagery (note: for the latter, a Planet API key is necessary).

The temporal segmentation step starts by fitting a third-order harmonic model to each band of the initial part of the time-series. Then, the observations are tested against the model for each band selected as a **breakpoint band**. In case of a significant repetitive deviation from the model, a break is flagged. Subsequently, a new segment is initialized for the upcoming observations until the next break is detected.

A **CCDC asset** retains the information of change(s) occurring for each pixel, including the date of the break and its magnitude. In addition, the model parameters are stored for the time-series segments in between those breaks. Therefore, another way of thinking about a **CCDC asset** is to consider it as a **condensed, synthetic time-series**. By only storing each segment's model parameters, we drastically reduce the storage needs as opposed to storing the full-time-series. At the same time, we retain the possibility of recreating the data at any given point in time by using the model's parameters.

.. attention::

    The creation of a CCDC asset is the mandatory first step for all types of subsequent workflows and analysis. This step is highly intense computationally, which makes it difficult for on-the-fly processing. An export as a GEE asset is highly recommended. For this, your SEPAL account needs to be connected to your GEE account (see `Connect SEPAL to GEE <../setup/gee.html>`__).

Getting Started
---------------

Create Recipe
^^^^^^^^^^^^^

Once logged into SEPAL, open the recipe menu by selecting the orange :btn:`<fa-solid fa-globe>` button in the upper left of the SEPAL start screen. Within the **Recipe** menu (*see figure below*), select **CCDC**, which opens a new SEPAL recipe tab.

.. thumbnail:: ../_images/cookbook/ccdc_asset/recipe_selection.png
    :group: ccdc-recipe-selection
    :title: Selection menu for SEPAL recipes
    :width: 60%
    :align: center

Rename recipe
^^^^^^^^^^^^^

The first step is to change the name of the recipe by double-clicking on the tab on the top of the map. This will automatically save your recipe and make it visible in the list of created recipes. The given name will be used for exported files, both locally and on GEE. We suggest using the following convention: :code:`CCDC-asset_<aoi>_<sensor(s)>_<start_date>_<end_date>`.

.. thumbnail:: ../_images/cookbook/ccdc_asset/recipe_unnamed.png
    :title: CCDC asset default title
    :width: 40%

.. thumbnail:: ../_images/cookbook/ccdc_asset/recipe_renamed.png
    :title: CCDC asset modified title
    :width: 40%

Parameter selection
-------------------

The following steps describe the parameter selection that can be found in the lower right of the screen.

.. thumbnail:: ../_images/cookbook/ccdc_asset/ccdc_start_screen.png
    :title: CCDC asset parameters

.. line-break::

The buttons open the following dialogues:

-   :guilabel:`AOI` Area of interest (AOI)
-   :guilabel:`DAT` Time of Interest (TOI), i.e. the time-span for the underlying time-series
-   :guilabel:`SRC` Selection of sensor(s)
-   :guilabel:`PRC` Preprocessing parameters
-   :guilabel:`OPT` CCDC parameters

Area of interest
^^^^^^^^^^^^^^^^

The data exported by the recipe will be cut to the bounds of the AOI. There are multiple ways to select the AOI in SEPAL:

-   Administrative boundaries
-   EE tables
-   Drawn polygons

These are described in our documentation (see :doc:`../feature/aoi_selector`).

.. thumbnail:: ../_images/cookbook/ccdc_asset/aoi.png
    :title: Select AOI based on administrative layers
    :group: ccdc-asset-recipe

Date range
^^^^^^^^^^

In the :guilabel:`DAT` tab, you will be asked to select the start date and the end date of the time series. Select the date text field to open the date selection pop-up menu. Select the :btn:`<fa-solid fa-check> Select` button to choose a date. When both dates have been chosen, select the :btn:`<fa-solid fa-check> Apply` button.

.. thumbnail:: ../_images/cookbook/ccdc_asset/dates.png
    :title: Select AOI based on EE table
    :width: 49%
    :group: ccdc-asset-recipe

.. thumbnail:: ../_images/cookbook/ccdc_asset/datepicker.png
    :title: Select AOI based on EE table
    :width: 49%
    :group: ccdc-asset-recipe

Sensor selection
^^^^^^^^^^^^^^^^

After selecting the :guilabel:`Next` button in the date selection pop-up menu, the sensor selection pop-up menu will automatically open (1), where you need to specify the sensor(s) and the bands used for breakpoint detection: 

-   :guilabel:`OPTICAL` (including the Landsat and Sentinel-2 missions);
-   :guilabel:`RADAR` (including the Sentinel-1 mission); and 
-   :guilabel:`PLANET`, where both daily imagery or monthly basemaps can be used as data input (given you have a valid Planet API key).

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_overview.png
    :title: Sensor selection
    :width: 100%
    :group: ccdc-asset-recipe

Optical data
""""""""""""

CCDC is originally tested on optical **Landsat** satellites. In SEPAL, you have the possibility of selecting and combining all past and present Landsat missions, including **Tier 1** and **Tier 2** collections, to run them on decadal-long time-series.

.. attention::

    The inclusion of **Tier 2** products and **Landsat 7** may introduce artifacts, due to the reduced quality of data. For recent, short-term time-series, it might be better to either select the Landsat-8 or Sentinel-2 mission, which deliver imagery from 2013 and 2015, respectively; however, this will reduce the density of observations for the underlying time-series.

.. attention::

    For cloud-prone regions, it is also possible to combine **Landsat** data with **Sentinel-2** data to densify the underlying time-series (note: due to differences in the sensors [although band names are equal] and overpass time, artifacts may be introduced that will affect breakpoint detection).

Breakpoint detection is at the heart of CCDC. The respective selection of bands can considerably affect the outcome of CCDC breakpoint detection. Unfortunately, there does not seem to be a "one-size-fits-all" preset for all kinds of applications. Scientific evidence suggests using all color bands but blue (`Zhu *et al.*, 2020 <https://www.sciencedirect.com/science/article/pii/S0034425719301002>`_). According to the study, the selection of additional ratio bands does not add any improvement. However, it should be noted that this assumption is based on the detection of all types of land-cover changes and that the study uses a modified version of CCDC (named COLD), where the change in bands are weighted differently than in the original version used in SEPAL (respectively Google Earth Engine).

.. tip::

    The use of the color bands allows you to later select the :code:`Green` and the :code:`Swir1` band as TMASK bands for CCDC's internal, multitemporal cloud removal (you can find this in the :guilabel:`OPT` button pop-up menu under :guilabel:`MORE`.

If the creation of the CCDC asset is aimed at the detection of both forest degradation and deforestation, the **Normalized difference fraction index** (:code:`NDFI`) might be another suitable choice as applied by `Bullock *et al.* (2020) <https://www.sciencedirect.com/science/article/pii/S0034425718305200>`_. (Note: This article and the NDFI are specifically tested over tropical rainforest of the Brazilian Amazon. Changes in other forest types might be better captured by different ratios or color bands. For instance, one can consider the **Normalized difference moisture index** [:code:`NDMI`] when looking at mangrove forests.)

.. tip::
    In case of doubt, we suggest to go for the default option and use all of the color bands, except blue.

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_color_breakbands.png
    :title: Sensor selection – color breakpoint bands
    :width: 49%
    :group: ccdc-asset-recipe

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_ndfi_breakband.png
    :title: Sensor selection – NDFI breakpoint band
    :width: 49%
    :group: ccdc-asset-recipe

Radar data
""""""""""

In order to create a CCDC asset based on underlying radar time-series, you need to select the :guilabel:`RADAR` button. This will utilize **Sentinel-1** C-Band SAR Image Collection in GEE. (To the best of our knowledge, no scientific studies have been done that investigate the ideal band selection for breakpoint detection. As a starting point, we suggest using the default option, which includes the :code:`VV` band and the :code:`VH` band.)

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_radar.png
    :title: Sensor selection – Radar
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

Planet data
"""""""""""

For the creation of a CCDC asset based on **Planet** data, you have the choice of either selecting **Planet custom basemaps** (including NICFI Level 1 data), or **Planet daily imagery** itself.

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_planet.png
    :title: Sensor selection – Planet
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

.. line-break::

In both cases, the data already needs to reside within GEE as an **ImageCollection asset** (whose ID needs to be filled in the respective field, as well).

In case you want to use **NICFI Level-1 basemaps**, you can use the already existing assets within GEE, given that you enabled the access feature (see `this article <https://docs.sepal.io/en/latest/setup/nicfi.html>`_). The NICFI Level-1 assets are split by continent and have the following asset IDs:

-   projects/planet-nicfi/assets/basemaps/africa
-   projects/planet-nicfi/assets/basemaps/asia
-   projects/planet-nicfi/assets/basemaps/americas

.. tip::

    For data ordered through the Planet API (i.e. daily imagery or custom basemaps other than NICFI Level 1 data), you can specify GEE as the download location.

Using CCDC with Planet has not been explored widely, so the optimal selection of the breakpoint bands depends on testing it out by yourself. However, in accordance with Landsat-based analysis, we suggest using the green, red and NIR bands to get started.

Preprocessing options
^^^^^^^^^^^^^^^^^^^^^


Optical data
""""""""""""

.. attention::

    This section is optional as these parameters are set by default.

    -   Correction: :code:`None`
    -   Cloud detection: :guilabel:`QA bands`, :guilabel:`Cloud score`
    -   Cloud masking: :guilabel:`Moderate`
    -   Snow masking: :guilabel:`On`

Multiple preprocessing parameters can be set to improve the quality of the provided images. SEPAL has gathered four of them in the form of these interactive buttons. If you think others should be added, tell us in our `issue tracker <https://github.com/openforis/sepal/issues/new/choose>`__.

**Correction**

-   :guilabel:`Surface reflectance`: Use scenes' atmospherically corrected surface reflectance.
-   :guilabel:`BRDF correction`: Correct for bidirectional reflectance distribution function (BRDF) effects.

**Cloud detection**

-   :guilabel:`QA bands`: Use pre-created QA bands from datasets.
-   :guilabel:`Cloud score`: Use cloud scoring algorithm.

**Cloud masking**

-   :guilabel:`Moderate`: Rely only on image source QA bands for cloud masking.
-   :guilabel:`Aggressive`: Rely on image source QA bands and a cloud scoring algorithm for cloud masking. This will probably mask out some built-up areas and other bright features.

**Snow masking**

-   :guilabel:`On`: Mask snow (this tends to leave some pixels with shadowy snow).
-   :guilabel:`Off`: Don't mask snow (note: some clouds might get misclassified as snow, and because of this, disabling snow masking might lead to cloud artifacts).

.. thumbnail:: ../_images/cookbook/ccdc_asset/pre_processing.png
    :title: The preprocessing panel to select extra filtering processes that will improve the quality of provided images.
    :group: time-series-recipe


Radar data
""""""""""

The default parameters (see figure below, on the left) are optimized for performance and coverage, rather than for the highest quality of data. It is therefore recommended to modify them accordingly (see figure below, on the right).

.. thumbnail:: ../_images/cookbook/ccdc_asset/prc_radar_default.png
    :title: PRC selection – Radar default
    :width: 49%
    :group: ccdc-asset-recipe

.. thumbnail:: ../_images/cookbook/ccdc_asset/prc_radar_recommended.png
    :title: PRC selection – Radar recommended
    :width: 49%
    :group: ccdc-asset-recipe

.. line-break::

**Orbit selection**

The orbit selection for radar satellites refers to the flight direction of the satellite (different for the sun-adverted and sun-facing sides of the planet). One distinguishes the ascending direction (from south pole towards north pole) and one distinguishes the descending direction (from north to south pole). Being independent from sunlight, radar satellites can acquire during both day and night; however, they do not acquire constantly.

In the case of the Sentinel-1 mission, areas outside of Europe are usually only covered by either one or the other (see figure below to determine which orbit direction your AOI is covered by).

.. image:: https://sentinels.copernicus.eu/documents/247904/3944045/Sentinel-1-Revisit-Coverage-Frequency-Geometry-2019.jpeg
    :alt: Sentinel-1 observation scenario

.. line-break::

.. attention::

    While you can select both orbits to err on the side of caution, marginal areas that are covered by both orbits might result in different models than for areas only covered by one or the other, due to differences in observation geometry. It is therefore recommended to properly select your orbit direction. In the event that your full AOI is covered by both orbits, select both.

**Geometric correction**

Setting the **Geometric Correction** to :guilabel:`TERRAIN` will correct for distortions of the radar backscatter signal along slopes. This is crucial for all types of land cover or biogeophysical parameter retrieval, and is therefore **highly recommended**.

**Speckle-filtering**

Speckle filtering is a common step in radar remote sensing and reduces the random noise within radar imagery. While CCDC already has a very effective filtering effect on the backscatter through the time-series modelling, selecting the multitemporal :guilabel:`QUEGAN` should improve the detection of breaks, and is therefore recommended. However, as it is very intense computationally, processing and export might take a considerable amount of time, and may even fail in some cases.

**Outlier removal**

Sentinel-1 data is prone to some rare artifacts, such as interferences from other radio wave sources or heavy rainfall events. SEPAL offers the option to exclude them with multitemporal outlier detection. By default, a :guilabel:`MODERATE` reduction is appropriate to remove such artifacts. More aggressive filtering might include actual change events, and is therefore not recommended.

Planet data
"""""""""""

Preprocessing parameters of Planet data are similar to the Landsat/Sentinel-2 options. The default parameters are reflecting a quite aggressive approach to cloud removal (see figure below).

.. thumbnail:: ../_images/cookbook/ccdc_asset/prc_planet_default.png
    :title: PRC selection – Planet default
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

.. line-break::

**Histogram matching**

Histogram matching is disabled by default. This is ok when dealing with already preprocessed monthly basemaps. However, if the collection is composed of daily imagery, it is highy recommended to :guilabel:`ENABLE` this option, as it will harmonize the radiometry between each single image.

CCDC parameters
^^^^^^^^^^^^^^^

Presets
"""""""
Behind :guilabel:`OPT`, you can find 3 basic presets of CCDC parameters. The selection of the presets can be interpreted at selecting the balance between commission and omission error for the breakpoint detection.

.. thumbnail:: ../_images/cookbook/ccdc_asset/opt_ccdc_simple.png
    :title: OPT selection – simple
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

.. line-break::

- The parameters of :guilabel:`CONSERVATIVE` are favoring commission over omission error rate in the breakpoint detection (i.e. aiming at high user accuracy and low false positives). In other words, CCDC is going to detect less breaks, but they are more likely to be correct. This comes at the cost of missing some actual changes, therefore having an increased omission error.

- The parameters of :guilabel:`MODERATE` are trying to balance commission and omission errors in the breakpoint detection. In other words, CCDC is going to both omit and commit some of the actual changes, keeping both level of error rates similar with a balanced false positive and false negative detection rate.

- The parameters of :guilabel:`AGGRESSIVE` are favoring omission over commission error rate in the breakpoint detection (i.e. aiming at high producer accuracy, low false negatives). In other words, CCDC is going to detect more breaks than with the other settings, reducing the likelihood of missing change; however, this comes at the cost of also detecting a lot of falsely detected change.

.. tip::

    If you have chosen the color bands for breakpoint detection within the sensor menu, it is worthwhile to go into the advanced options using the :guilabel:`MORE` button and select the :guilabel:`GREEN` and :guilabel:`SWIR1` band as :guilabel:`TMASK BANDS`.

Advanced Options
""""""""""""""""
More advanced users have the possibility of manually setting all of the actual CCDC parameters by selecting the :guilabel:`MORE` button.

.. thumbnail:: ../_images/cookbook/ccdc_asset/opt_ccdc_advanced.png
    :title: OPT selection – Advanced
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

.. line-break::

**Date format**

This option allows saving the dates in various formats. (Note: by default, SEPAL deals with :guilabel:`FRACTIONAL YEARS` in all CCDC-related recipes.)

**TMASK BANDS**

The bands selected here are used for additional multitemporal filtering of cloud-affected pixels that have not been identified as such throughout the preprocessing of single images. For optical data from Landsat and Sentinel-2, the :guilabel:`GREEN` and :guilabel:`SWIR1` bands are recommended.

**Min observations**

This is the number of observations needed before a break is actually confirmed based on its temporal behaviour. A low number will lead to more changes and reduce the gaps between two temporal segments. Higher numbers will lead to more confidence in the observed change; however in cloud-prone regions, higher numbers might lead to long gaps between two temporal segments. Usually, a number between 4 and 8 is recommended.

**Chi-Square probability**

The Chi-Square test will test if an observation is part of the general statistical distribution of the time-series. A low value of Chi-Square probability will favor the rejection of the null-hypothesis (i.e. being part of the statistical distribution), therefore flagging it as possible change. Ultimately, a lower value leads to more breaks detected, which favors omission over commission error. A high value allows for more noise in the time-series, and less changes will be detected, therefore lowering the commission error rate.

**Min number of years scaler**

This parameter determines the minimum length of any inner-temporal segment.

**LAMBDA**

The LAMBDA parameter is part of the LASSO regression used for the modelling of the time-series. It is used to generalize the model, thereby improving its predictive power. More specifically, it is controlling the weight of each of the parameters, and might result even in the annulation of some of the parameters. In practical terms, an initial third-order harmonic model might shrink to a first-order harmonic, if this provides the best generalized fit. Setting LAMBDA to 0 will lead to a regular Ordinary-Least-Square regression, not providing any generalization. Instead, a higher value will provide a more generalized model. If LAMBDA is set too high, the model will underfit, which is also not wanted. Since a value of 20 has been found to provide a generally good performance, the sweet spot of neither overfitting nor underfitting will be around this number.

**Max iterations**

Those are the iterations for the maximum number of runs for LASSO regression convergence. If set to 0, regular OLS is used instead of LASSO.

.. ccdc_pixel_analys

On-the-fly pixel analysis
-------------------------

Select the :btn:`<fa-solid fa-chart-area>` button to start the plotting tool (1). Move the pointer to the main map; the pointer will be transformed into a :icon:`fa-solid fa-plus` (2). Click anywhere in the AOI to plot data for this specific location in the following pop-up window.

The plotting area (3) is dynamic and can be customized by the user.

You can select the observation feature by selecting one of the available measures in the dropdown selector in the upper-left corner (4). The available bands are the same as those previously described.

Using the slider (5), the temporal width displayed can be changed. It cannot exceed the start and/or end date of the time series.

On the main graph, the orange lines show the CCDC-modelled time-series. Each of the blue points represents an actual observation. You can both hover over the point or the line to let the tooltip describe the value and date of the observation, as well as the model values and the temporal extent of the specific segment.

.. thumbnail:: ../_images/cookbook/ccdc_asset/ccdc_pixel_analysis.png
    :title: Pixel analysis
    :width: 100%
    :group: ccdc-asset-recipe

.. attention::

    The plot feature is retrieving information from GEE on-the-fly and serving it in an interactive window. This operation can take time depending on the number of available observations and the complexity of the selected preprocessing parameters. If the pop-up window displays a spinning wheel, wait up to two min to see the data displayed.

Export
------

.. important::

    You cannot export a recipe as an asset or a :code:`.tiff` file without a small computation quota (if you are a new user, see :doc:`../setup/resource`).

Trigger the export task
^^^^^^^^^^^^^^^^^^^^^^^

Select the :btn:`<fa-solid fa-cloud-arrow-down>` button to open the export dialogue. Here you can select the bands to retrieve and the scale at which you would like to save the asset. CCDC assets are only compatible with GEE (a new asset will be created in your personal GEE repository).

If the area covered is relatively small and you have enough storage quota left, you can generously select most of the bands relevant for land applications (see figure below, on the left). If you are more constrained by storage, you will need to decide on a subset of bands (see figure below, on the right, for a suggested starting point).

The scale parameter depends on the data selected and the level of detail you will need for further analysis. Landsat-based assets are usually created at 30 m. Sentinel-1 and 2 can be at 10 m, but will need nine times more space as compared to 30 m resolution.

.. thumbnail:: ../_images/cookbook/ccdc_asset/ccdc_export_full.png
    :title: Export CCDC asset – full band selection
    :width: 49%
    :group: ccdc-asset-recipe

.. thumbnail:: ../_images/cookbook/ccdc_asset/ccdc_export_reduced.png
    :title: Export CCDC asset – reduced band selection
    :width: 49%
    :group: ccdc-asset-recipe


Exportation status
^^^^^^^^^^^^^^^^^^

Going to the task tab (lower-left corner using :btn:`<fa-solid fa-list-check>` or :btn:`<fa-solid fa-spinner>` buttons, depending on the loading status), you will see the list of different loading tasks. The interface will provide you with information about the task progress; it will display an error if the exportation has failed. If you are unsatisfied with the way we present information, the task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    This operation is running between GEE and SEPAL servers in the background; you can thus close the SEPAL page without killing the process.

When the task is finished, the frame will be displayed in green (see second image below).

.. thumbnail:: ../_images/cookbook/ccdc_asset/download.png
    :width: 49%
    :title: Evolution of the downloading process of the recipe displayed in the task manager of SEPAL.
    :group: ccdc-asset-recipe

.. thumbnail:: ../_images/cookbook/ccdc_asset/download_complete.png
    :width: 49%
    :title: Completed downloading process of the recipe displayed in the task manager of SEPAL.
    :group: ccdc-asset-recipe
