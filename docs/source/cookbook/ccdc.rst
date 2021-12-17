CCDC - Asset Creation
*********************

Background
------------

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

Once logged into SEPAL, open the recipe menu by clicking on the orange :icon:`fas fa-globe` button at the top left of the SEPAL start screen. Within the recipe menu (*see figure below*), select CCDC, which opens a new SEPAL recipe tab.

.. thumbnail:: ../_images/cookbook/ccdc_asset/recipe_selection.png
    :group: ccdc-recipe-selection
    :title: Selection menu for SEPAL recipes
    :width: 60%

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

|
The buttons open the following dialogues:

:guilabel:`AOI` Area of interest (AOI)

:guilabel:`DAT` Time of Interest (TOI), i.e. the time-span for the underlying time-series

:guilabel:`SRC` Selection of sensor(s)

:guilabel:`PRC` Pre-processing parameters

:guilabel:`OPT` CCDC Parameters

Area of Interest
^^^^^^^^^^^^^^^

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

In the :guilabel:`DAT` tab, you will be asked to select the starting date and the ending date of the time series. Click on the date tex field to open a date picker popup. Click on the :icon:`fa fa-check` :guilabel:`Select` button to validate a date. When both dates are selected click on :icon:`fa fa-check` :guilabel:`apply` button.

.. thumbnail:: ../_images/cookbook/time_series/dates.png
    :title: Select AOI based on EE table
    :width: 49%
    :group: time-series-recipe

.. thumbnail:: ../_images/cookbook/time_series/datepicker.png
    :title: Select AOI based on EE table
    :width: 49%
    :group: time-series-recipe

Sensor selection
^^^^^^^^^^^^^^^^

After clicking the :guilabel:`NEXT` button in the date selection, the sensor selection pop-up menu will automatically open (1). Here you need to specify the sensor(s) and the bands used for the breakpoint detection. You have the choice between 3 types, optical (including the Landsat and Sentinel-2 missions), radar (including the Sentinel-1 mission) and Planet data, where both daily imagery or monthly basemaps can be used as data input (given you have a valid Planet API key).

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_overview.png
    :title: Sensor Selection
    :width: 100%
    :group: ccdc-asset-recipe

Optical data
"""""""""""

CCDC is originally tested on optical Landsat satellites. In SEPAL you have the possibility to select adn combine all past and present Landsat missions, including Tier 1 and Tier 2 collections, to run it on decadal-long time-series.

.. warning::

    The inclusion of Tier 2 products as well as Landsat 7 may introduce artifacts due to the reduced quality of the data. For recent short-term time-series it might be better to either select the Landsat-8 or Sentinel-2 mission, which deliver imagery from 2013 and 2015, respectively. This will however reduce the density of observations for the underlying time-series.

.. warning::

    For very cloud-prone regions, it is also possible to combine the Landsat data with the Sentinel-2 data to densify the underlying time-series. Note that because of differences in the sensors (although band names are equal) and the overpass time, artifacts may be introduced tht will affect the breakpoint detection.

The breakpoint detection is at the heart of CCDC. The respective selection of bands can considerably affect the outcome of the CCDC breakpoint detection. Unfortunately, there does not seem to be a *"one size fits all"* preset for all kinds of applications. Scientific evidence is suggesting to use all color bands but the blue `Zhu et al 2020 <https://www.sciencedirect.com/science/article/pii/S0034425719301002>`_. According to the study, the selection of additional ratio bands does not add any improvement. However, this assumption is based on the detection of all kinds of land cover changes and uses a modified version of CCDC (COLD), where the change in bands are weighted differently than in the original version used in SEPAL, respectively Google Earth Engine.

.. tip::

    The use of the color bands allows you to later select the *Green* and the *Swir1* band as TMASK bands for CCDC's internal, multi-temporal cloud removal. You find this in the :guilabel:`OPT` button pop-up menu under :guilabel:`MORE`.

If the creation of the CCDC asset is aimed at the detection of both, forest degradation and deforestation, the *Normalized Degradation Forest Index* NDFI might be another suitable choice as applied by `Bullock et al 2020 <https://www.sciencedirect.com/science/article/pii/S0034425718305200>`_. Note that this article and the NDFI are specifically tested over tropical rainforest of the Brazilian Amazon. Changes in other forest types might be better captured by different ratios or the color bands. For instance one can consider the *Normalized Differenced Moisture Index* NDMI when looking at Mangrove forests.

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

In order to create a CCDC asset based on underlying radar time-series, you need to select the :guilabel:`RADAR` button. This will make use the Sentinel-1 C-Band SAR Image Collection in Google Earth Engine. To the best of our knowledge, no scientific studies have been done that investigate the ideal band selection for breakpoint detection. As a starting point we suggest to use the default option that includes the VV and the VH band.

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_radar.png
    :title: Sensor Selection - Radar
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

Planet data
"""""""""""

For the creation of a CCDC asset based on Planet data, you have the choice of either selecting the Planet custom basemaps (including the NICFI Level 1 data), or daily imagery itself.

.. thumbnail:: ../_images/cookbook/ccdc_asset/sensor_selection_planet.png
    :title: Sensor Selection - Planet
    :width: 49%
    :align: center
    :group: ccdc-asset-recipe

|
In both cases, the data already needs to reside within Earth Engine as an *ImageCollection asset*, whose ID needs to be filled in the respective field.

In case you want to use the NICFI Level-1 basemaps, you can use the already existing assets within Earth Engine, given that you enabled the access feature as explained `here <https://developers.planet.com/docs/integrations/gee/nicfi/>`_. The NICFI Level-1 assets are splitted by continent and have the following Asset IDs:

    - projects/planet-nicfi/assets/basemaps/africa
    - projects/planet-nicfi/assets/basemaps/asia
    - projects/planet-nicfi/assets/basemaps/americas


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


.. thumbnail:: ../_images/cookbook/time_series/pre_processing.png
    :title: The pre-processing panel to select the extra filtering processes that will improve the quality of the provided images.
    :group: time-series-recipe


Radar data
""""""""""

The default parameters (below figure on the left) are rather optimized for performance and coverage than for the quality. It is therefore recommended to modify them accordingly (below figure on the right).

.. thumbnail:: ../_images/cookbook/ccdc_asset/prc_radar_default.png
    :title: Prc Selection - Radar default
    :width: 49%
    :group: ccdc-asset-recipe

.. thumbnail:: ../_images/cookbook/ccdc_asset/prc_radar_recommended.png
    :title: Prc Selection - Radar recommended
    :width: 49%
    :group: ccdc-asset-recipe

|
The orbit selection for radar satellites refers to the flight direction of the satellite that is different from sun-adverted and the sun-facing side of the planet. One distinguishes ascending (from south pole towards north pole) and descending (from north to south pole) direction. Being independent from the sunlight, radar satellites can acquire at both, day and nighttime. However, they do not acquire constantly.

In case of the Sentinel-1 mission, areas outside of Europe are usually only covered by either one or the other. With the help of the below figure you should be able to see by which orbit direction your Area of Interest is covered.

.. image:: https://sentinels.copernicus.eu/documents/247904/3944045/Sentinel-1-Revisit-Coverage-Frequency-Geometry-2019.jpeg
    :alt: Sentinel-1 observation scenario
|
.. warning::
    While you can select both orbits to be on the safe side, marginal areas that are covered by both orbits might result in different models than for areas only covered by on eor the other, due to the differences in observation geometry. It is therefore recommended to properly select your orbit direction. Instead, if it happens that your full AOI is covered by both orbits, do also select both.

Setting the *Geometric Correction* to :guilabel:`TERRAIN` will correct for distortions of the radar backscatter signal along slopes. This is crucial for all types of land cover or biogeophysical parameter retrieval and is therefore **highly recommended**.

Speckle Filtering is a common step in radar remote sensing and reduces the random noise within radar imagery. While CCDC has already a very effective filtering effect on the backscatter through the time-series modelling, selecting the multi-temporal :guilabel:`QUEGAN` shall improve the detection of breaks and is therefore recommended. However, as it is very compute intense, processing and export


CCDC parameters
^^^^^^^^^^^^^^^


Pixel analysis
-------------



Export
------

Quick Guide for Landsat-8 based Asset creation
==============================================

1. Create a CCDC recipe
2. Select your Area of Interest in the **AOI** tab
3. Select your time of interest in the  **DAT** tab, considering a initialization period (12 clear observations, 2-3 years for cloudy areas) before you expect some change.
4. Within the **SRC*** tab, select L8 under Optical datasets and use the color bands blue, green, red, nir, swir1 and swir2 for breakpoint detection.
5. Within the **PRC** tab select *Surface Reflectance* and *BRDF correction*. In addition set the default parameter for cloud masking to **AGGRESSIVE** and turn the cloud shadow mask on.
6. Within the **OPT** tab you can leave the default options.
7. Finally, you will export your assets using the *Download Button*


.. tip::
    The creation of a CCDC asset is computationally intense. Therefore, results shall be exported as an Earth Engine asset for the smooth operation of subsequent steps.


.. info::





.. warning::

    The documentation of this functionality is under construction.

.. tip::

    For specific help, please open an issue on our repository by clicking on this `link <https://github.com/openforis/sepal-doc/issues/new?assignees=&labels=&template=documentation-needed.md>`__.