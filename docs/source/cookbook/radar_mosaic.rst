Radar mosaics
=============
*Generate analysis-ready data from the SAR mission with radar mosaics*

Overview
--------

The SEPAL recipe for radar mosaics allows users to generate analysis-ready data (ARD) from the Sentinel-1 C-Band synthetic aperture radar (SAR) mission, which can be used in subsequent analysis, such as land cover classification.

Unlike optical sensors, a SAR sensor emits its own microwave signal and records what is scattered back to it (the **backscatter**). It therefore acquires images day and night and through clouds, which makes it particularly valuable in persistently cloudy regions such as the tropics.

SEPAL builds the mosaic from the `Sentinel-1 GRD <https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD>`__ collection available in Google Earth Engine (GEE). Only scenes acquired in **Interferometric Wide swath** (IW) mode with both **VV** and **VH** polarizations are used:

-   **VV**: vertically transmitted, vertically received. Sensitive to surface scattering (e.g. bare soil, water, rough surfaces).
-   **VH**: vertically transmitted, horizontally received. Sensitive to volume scattering (e.g. vegetation canopies).

All backscatter values are expressed in decibels (dB). Sentinel-1 data are available from 2014 onward.

The recipe can produce two kinds of outputs:

-   **Time scan**: for every pixel, statistics (e.g. median, minimum, maximum, standard deviation) are computed from all the acquisitions within a period. Time scans capture both the typical backscatter and its variation over time, and are well suited to land cover mapping.
-   **Point-in-time mosaic**: every pixel comes from the acquisition closest to a target date, giving a snapshot of the surface around that date.

.. note::

    You won't be able to retrieve the images if your SEPAL and Google Earth Engine (GEE) accounts are not connected. For more information, go to :doc:`../setup/gee`.

Start
-----

To create a new radar mosaic, go to the :btn:`<fa-solid fa-globe>` **Process** section and select :btn:`<fa-solid fa-plus> Add recipe` (first image below). In the **Create recipe** list that opens, select **Radar mosaic** (second image).

.. thumbnail:: ../_images/cookbook/radar_mosaics/create_recipe.png
    :width: 49%
    :title: Select **Add recipe** in the **Process** section
    :group: radar-mosaic-recipe

.. thumbnail:: ../_images/cookbook/radar_mosaics/sepal_recipes.png
    :width: 49%
    :title: Select **Radar mosaic** in the **Create recipe** list
    :group: radar-mosaic-recipe

Once the **Radar mosaic** recipe is selected, SEPAL will display the recipe process in a new tab. The first step is to change the name of the recipe. This name will be used to identify your files and recipes in SEPAL folders. Use the best-suited convention for your needs. Simply double-click the tab (see **1** in the image below) and write a new name. It defaults to :code:`Radar_mosaic_<creation date>_<creation time>` (e.g. :code:`Radar_mosaic_2026-10-09_14-18-05`).

.. note::

    The SEPAL team recommends using the following naming convention: :code:`<aoi name>_<dates>_<measure>`.

.. thumbnail:: ../_images/cookbook/radar_mosaics/landing.png
    :title: The landing page of the radar mosaic recipe
    :group: radar-mosaic-recipe

Parameters
----------

When a new recipe opens, the **Area of interest** window is displayed in the lower-right corner (see **2** in the image above). To its right, three tabs are available, which allow you to customize the mosaic creation to your needs:

-   :guilabel:`AOI`: area of interest
-   :guilabel:`DAT`: dates of the mosaic (time scan or point in time)
-   :guilabel:`OPT`: processing options (orbits, corrections, filters)

Select a tab to open the corresponding panel. Each panel is described in the following sections.

AOI selection
^^^^^^^^^^^^^

The data exported by the recipe will be generated from within the bounds of the AOI. There are multiple ways to select the AOI in SEPAL:

-   Administrative boundaries
-   EE Tables
-   Drawn polygons
-   Assets or recipes

They are extensively described in our documentation. For more information, read :doc:`../feature/aoi_selector`.

Dates
^^^^^

In the :guilabel:`DAT` tab, you can define the dates or time frame of the mosaic. There are three ways of specifying the dates; select one of the following options under :guilabel:`Type`:

-   :guilabel:`Year`: builds a **time scan** from all acquisitions of a calendar year (1 January to 31 December). Select the **Year** in the picker. This is the default, and the recommended option for land cover mapping.
-   :guilabel:`Date range`: builds a **time scan** from all acquisitions between a **From date** and a **To date** of your choice (e.g. a single season, or several years).
-   :guilabel:`Date`: builds a **point-in-time mosaic**. Select a **Target date**; each pixel will come from the acquisition closest to that date (SEPAL searches up to about six months before and after it).

.. thumbnail:: ../_images/cookbook/radar_mosaics/dates.png
    :title: The **Dates** panel with the :guilabel:`Year` type selected
    :group: radar-mosaic-recipe

.. tip::

    The type you choose determines which bands can be exported. Time scans provide statistical bands (e.g. :code:`VV_med`), while point-in-time mosaics provide the backscatter of a single acquisition (e.g. :code:`VV`).

Options
^^^^^^^

The :guilabel:`OPT` tab controls which acquisitions are used and how they are corrected and filtered. The panel opens in a **simple** view showing the most common options; select :guilabel:`More` to reveal the **advanced** options (and :guilabel:`Less` to hide them again).

.. note::

    This step is optional. By default, SEPAL applies:

    -   Orbits: **Ascending** and **Descending**
    -   Geometric correction: **Terrain**
    -   Spatial speckle filter: **Lee Sigma** (kernel size 9, sigma 0.9, strong scatterers retained)
    -   Multitemporal speckle filter: **None**
    -   Outlier removal: **Moderate**
    -   Orbit overlap: **All**
    -   Border noise correction: **Sides** and **First/Last** (set in the advanced view)
    -   Min observations: **1** (set in the advanced view)

.. thumbnail:: ../_images/cookbook/radar_mosaics/options.png
    :title: The **Options** panel (simple view)
    :group: radar-mosaic-recipe

.. dropdown:: Show the advanced view (opened with **More**)
    :icon: image
    :margin: 3 0 0 0

    .. thumbnail:: ../_images/cookbook/radar_mosaics/options_advanced.png
        :width: 30%
        :group: radar-mosaic-recipe
        :title: The **Options** panel (advanced view, opened with **More**)

Orbits
""""""

Sentinel-1 acquires images while travelling north (**Ascending**) and south (**Descending**). The two orbit directions look at the surface from opposite sides, so slopes facing the sensor in one direction face away from it in the other. Select one or both directions (at least one is required).

Combining both directions increases the number of observations and coverage, but differences in viewing geometry can create visible artefacts, especially in mountainous areas.

.. tip::

    Check the orbit coverage of your AOI before deciding which orbits to use:

    1.  Select only :guilabel:`Ascending` and let the mosaic render.
    2.  Deselect :guilabel:`Ascending`, select :guilabel:`Descending` and let the mosaic render.
    3.  If only one orbit direction covers the entire AOI, use that one. If both do, select both, let the mosaic render and check for artefacts caused by combining them.

Geometric correction
""""""""""""""""""""

The backscatter recorded by the sensor depends on the angle at which the signal hits the ground. Geometric correction reduces this effect, so that values become comparable across the image and between orbits:

-   :guilabel:`None`: No geometric correction is applied (the backscatter is used as **sigma0**).
-   :guilabel:`Ellipsoid`: Ellipsoid correction (**gamma0** correction) is applied, normalizing the backscatter by the incidence angle over a smooth Earth model. Topography is not taken into account.
-   :guilabel:`Terrain`: Terrain correction is applied. In addition to the incidence angle, SEPAL uses the `Copernicus GLO-30 <https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30>`__ digital elevation model to compensate for the effect of slopes facing towards or away from the sensor, and masks areas affected by **layover** and **shadow**. Recommended in any area with significant relief.

Spatial speckle filter
""""""""""""""""""""""

All SAR images contain **speckle**: a grainy, "salt-and-pepper" noise caused by the interference of the signals scattered back within each pixel. Spatial speckle filters reduce it by taking neighbouring pixels into account, at the cost of some spatial detail:

-   :guilabel:`None`: Doesn't apply any speckle filter.
-   :guilabel:`Gamma Map`: A statistical (Bayesian) filter that assumes the backscatter of the surface follows a gamma distribution, and estimates the most likely value of each pixel from its neighbours. It smooths homogeneous areas well while preserving edges and texture.
-   :guilabel:`Lee`: An adaptive filter based on the mean and variance of the pixels within the kernel. It smooths strongly in homogeneous areas (e.g. water, fields) and less around edges and bright features, where the local variance is high.
-   :guilabel:`Refined Lee`: An improved version of the Lee filter that detects edges and filters along them, using differently oriented windows instead of a square one. It preserves edges and linear features (e.g. roads, field boundaries) better, but can be very slow. It uses a fixed window, so it has no **Kernel size** setting.
-   :guilabel:`Lee Sigma`: An improved version of the Lee filter that only averages the neighbouring pixels whose values are close to the expected value of the centre pixel (within a range set by **Sigma**). This avoids blurring edges and bright point targets, and gives a good balance between speckle reduction and detail. It is the default.
-   :guilabel:`SNIC`: Simple Non-Iterative Clustering is used to group pixels into small, homogeneous clusters (superpixels), which filters out speckle.

.. note::

    Time scans combine many acquisitions, which already averages out much of the speckle. Speckle filtering has a stronger effect on point-in-time mosaics, which rely on a single acquisition per pixel.

Spatial speckle filter options (advanced view)
##############################################

When a filter other than :guilabel:`None` is selected, a summary of its settings appears below the filter buttons. Select it to open the **Spatial speckle filter options** window. The settings available depend on the filter:

.. thumbnail:: ../_images/cookbook/radar_mosaics/speckle_options.png
    :width: 80%
    :align: center
    :group: radar-mosaic-recipe
    :title: The **Spatial speckle filter options** window for the :guilabel:`Lee Sigma` filter, opened by selecting the settings summary

-   **Kernel size**: the size, in pixels, of the moving window used by the filter (from 3 to 25; default **9**). Larger windows remove more speckle but blur more detail. Applies to :guilabel:`Gamma Map`, :guilabel:`Lee` and :guilabel:`Lee Sigma`.
-   **Sigma**: the range of values considered similar to the centre pixel (from 0.5 to 0.95; default **0.9**). Larger values include more neighbouring pixels in the average, giving stronger smoothing. Applies to :guilabel:`Lee Sigma`.
-   **Seed spacing**: the spacing, in pixels, of the cluster seeds (from 3 to 15; default **5**). Larger values create larger clusters. Applies to :guilabel:`SNIC`.
-   **Compactness**: how compact (square) the clusters are (from 0 to 2; default **0.15**). Larger values create more regular clusters; 0 disables spatial distance weighting. Applies to :guilabel:`SNIC`.
-   **Strong scatterers**: bright, strong scatterers such as buildings don't tend to include much speckle, and some filters tend to blur them. Choose :code:`Retain` (default) to keep their original values, or :code:`Filter` to apply the filter to them as well. Applies to all filters.
-   **VV threshold** and **VH threshold**: the backscatter values (in dB; defaults **0** and **-5**) above which a pixel is considered a strong scatterer. Shown only when :code:`Retain` is selected.

Multitemporal speckle filter
""""""""""""""""""""""""""""

(Shown only when a spatial speckle filter is selected.) Multitemporal filters reduce speckle further by using a series of acquisitions of the same track, preserving more spatial detail than a spatial filter alone:

-   :guilabel:`None`: Doesn't apply any multitemporal speckle filter.
-   :guilabel:`Quegan`: First applies the selected spatial filter to each acquisition, then restores the detail lost by that filter using the other acquisitions of the same track. Detail that is consistent over time (e.g. edges, small features) is kept, while random speckle is averaged out. For more information, see `S. Quegan et al. [2000] <https://ieeexplore.ieee.org/document/842003>`__.
-   :guilabel:`RABASAR`: (Ratio-based multitemporal SAR despeckling.) Averages the acquisitions of the same track into a nearly speckle-free reference image, then applies the selected spatial filter only to the ratio between each acquisition and that reference. This keeps the spatial detail of the reference while preserving the changes specific to each acquisition.

In the advanced view, select the settings summary below the filter buttons to open the **Multitemporal speckle filter options** window, where you can set the **Number of images** (from 2 to 100; default **10**): how many acquisitions of the same track, taken around the middle of the selected period, are used by the filter. More images reduce speckle further but increase processing time.

.. note::

    Multitemporal filtering is computationally intensive and significantly increases the processing time of the mosaic.

Outlier removal
"""""""""""""""

Individual acquisitions can contain unusually high or low values (e.g. caused by heavy rain, flooding or processing artefacts). Outlier removal compares, for each pixel, every acquisition with the median of all acquisitions, and removes those that deviate too much:

-   :guilabel:`None`: Doesn't remove outliers.
-   :guilabel:`Moderate`: Removes outliers (values more than **3** standard deviations from the median).
-   :guilabel:`Aggressive`: Removes more outliers (values more than **2.6** standard deviations from the median).

.. tip::

    Outlier removal relies on the temporal statistics of each pixel, so it is most effective with time scans built from many acquisitions.

Orbit overlap
"""""""""""""

Neighbouring Sentinel-1 tracks (identified by their **relative orbit number**) overlap, so some pixels are observed from several tracks with slightly different viewing angles. This option defines which tracks contribute to each pixel:

-   :guilabel:`All`: Includes values from all orbit numbers for a pixel.
-   :guilabel:`Dominant`: Only includes values from the dominant orbit number (the one with the most acquisitions) for a pixel. This produces a more consistent viewing geometry, at the cost of fewer observations.
-   :guilabel:`Adjacent`: Includes values from the dominant orbit of both the ascending and the descending orbits. When only one orbit direction is selected, this behaves like :guilabel:`Dominant`.

Border noise correction (advanced view)
"""""""""""""""""""""""""""""""""""""""

Sentinel-1 scenes can contain low-quality, noisy pixels along their borders. Select one or both corrections:

-   :guilabel:`Sides`: Masks the sides of slices, by removing pixels whose incidence angle falls outside a given range. When selected, a settings summary appears; select it to open the **Border noise correction options** window and set the **Min angle** and **Max angle** in degrees (defaults: **30.88** and **45.35**).
-   :guilabel:`First/Last`: Masks the beginning of the first slice and the end of the last slice of an acquisition.

Min observations (advanced view)
""""""""""""""""""""""""""""""""

Use the **Min observations** slider (from 1 to 50) to mask pixels that have fewer valid acquisitions than the selected value. Statistics computed from only a few observations are less reliable, so increasing this value removes them from the mosaic (leaving gaps where data are scarce).

To validate your selection, select the :btn:`<fa-solid fa-check> Apply` button.

Retrieve
--------

.. important::

    You cannot export a recipe as an asset or a :code:`.tif` file without a small computation quota. If you are a new user, see :doc:`../setup/resource`.

In the upper-right corner, select the :btn:`<fa-solid fa-cloud-arrow-down>` button to open the **Retrieve** panel, where you can select the exportation parameters.

.. thumbnail:: ../_images/cookbook/radar_mosaics/retrieve.png
    :title: The **Retrieve** panel with the recommended time-scan bands selected
    :group: radar-mosaic-recipe

Bands to retrieve
^^^^^^^^^^^^^^^^^

Select the band(s) to export with the mosaic in **Bands to retrieve**. There is no maximum number of bands, but exporting useless bands will only increase the size and time of the output. The available bands depend on the **Type** selected in the :guilabel:`DAT` tab: a **time scan** or a **point-in-time** mosaic.

Time scan
"""""""""

Available when the type is :guilabel:`Year` or :guilabel:`Date range`. The statistics are computed per pixel from all the acquisitions that remain after filtering:

-   :guilabel:`VV_min`, :guilabel:`VH_min`: minimum backscatter.
-   :guilabel:`VV_mean`, :guilabel:`VH_mean`: mean backscatter.
-   :guilabel:`VV_med`, :guilabel:`VH_med`: median backscatter. Less sensitive to extreme values than the mean.
-   :guilabel:`VV_max`, :guilabel:`VH_max`: maximum backscatter.
-   :guilabel:`VV_std`, :guilabel:`VH_std`: standard deviation of the backscatter, a measure of how much the surface changes over time.
-   :guilabel:`VV_cv`, :guilabel:`VH_cv`: coefficient of variation of the backscatter (in dB).
-   :guilabel:`orbit`: the most frequent relative orbit number of the pixel.

SEPAL can also fit a harmonic model (a linear trend plus a yearly cycle) to the acquisitions of each pixel. The following bands describe that model:

-   :guilabel:`VV_t`, :guilabel:`VH_t`: the slope of the linear trend over time.
-   :guilabel:`VV_phase`, :guilabel:`VH_phase`: the phase of the yearly cycle, i.e. the time of year when the backscatter peaks.
-   :guilabel:`VV_amp`, :guilabel:`VH_amp`: the amplitude of the yearly cycle, i.e. the strength of the seasonal variation.
-   :guilabel:`VV_res`, :guilabel:`VH_res`: the residuals of the fit, i.e. how well the model describes the data.

.. note::

    The harmonic model is only computed when at least one of its bands is selected, and it increases the processing time. It requires enough acquisitions spread over the period to give meaningful results; it is best suited to periods of a year or more.

Point in time
"""""""""""""

Available when the type is :guilabel:`Date`:

-   :guilabel:`VV`, :guilabel:`VH`: the backscatter of the selected acquisition.
-   :guilabel:`ratio_VV_VH`: the difference :code:`VV - VH` in dB (equivalent to the VV/VH ratio in linear units).
-   :guilabel:`dayOfYear`: the day of the year of the selected acquisition.
-   :guilabel:`daysFromTarget`: the number of days between the selected acquisition and the target date.
-   :guilabel:`orbit`: the relative orbit number of the selected acquisition.

.. tip::

    For land cover mapping, the median, minimum, maximum and standard deviation bands of both polarizations (:code:`VV_med`, :code:`VV_min`, :code:`VV_max`, :code:`VV_std` and their :code:`VH_` equivalents) of a yearly time scan are a good starting point. They can be combined with optical bands in the :doc:`classification` recipe.

Scale
^^^^^

You can set a custom scale for exportation by selecting a value in metres (m). The default is **20 m**. Note that requesting a smaller resolution than the native resolution of the data (10 m pixel spacing for Sentinel-1 GRD) will not improve the quality of the output, just its size.

Destination
^^^^^^^^^^^

Choose a single destination for the export:

-   :guilabel:`Google Earth Engine asset`: the image is exported to your GEE account as an asset. You can export it either as a single **Image** or as an **Image collection** (tiled, which is better suited to large exports), and set its sharing to **Private** or **Public**. The **Asset ID** field defines where the asset is saved in your GEE account.
-   :guilabel:`Google Drive`: the image is exported to the Google Drive of the connected Google account.
-   :guilabel:`SEPAL workspace`: the image is written to your SEPAL files in :code:`.tif` format. The **Workspace path** defines the destination folder (by default :code:`downloads/<recipe name>`, or :code:`downloads/<project name>/<recipe name>` if the recipe belongs to a project), and the **Filename prefix** is added to the name of every exported file (by default, the recipe name).

.. note::

    The **Google Earth Engine asset** and **Google Drive** destinations are only displayed when a Google account is connected to SEPAL. If they are missing, please refer to `Connect SEPAL to GEE <../setup/gee.html>`__.

Select :guilabel:`More` to show additional export settings (e.g. **Shard size**, **Tile size**, **CRS** and **CRS transform**). The default values are suitable in most cases; reduce the shard or tile size if the export runs out of memory.

Select :guilabel:`Retrieve` to start the export process.

Exportation status
^^^^^^^^^^^^^^^^^^

Open the **Tasks** tab (lower-left corner, using the :icon:`fa-solid fa-list-check` or :icon:`fa-solid fa-spinner` button, depending on the loading status) to follow the export. Each task shows the recipe type, the destination and the name of the recipe (e.g. a **Radar mosaic** exported to the **SEPAL workspace**), together with its current status (e.g. :code:`Google Earth Engine is exporting`). A running task displays a spinner, and a green check mark appears once it has completed.

You can filter the list with :guilabel:`All`, :guilabel:`Active`, :guilabel:`Completed` and :guilabel:`Failed / Canceled`, or find a task by name with the **Search tasks** field. Select :btn:`<fa-solid fa-xmark>` to stop a running task and :btn:`<fa-solid fa-trash>` to remove a task from the list.

.. thumbnail:: ../_images/cookbook/radar_mosaics/download.png
    :width: 49%
    :title: Radar mosaic exports in SEPAL's **Tasks** tab: one completed, one in progress
    :group: radar-mosaic-recipe

.. thumbnail:: ../_images/cookbook/radar_mosaics/download_complete.png
    :width: 49%
    :title: The details of a completed export
    :group: radar-mosaic-recipe

Select a task to open its details: the duration and submission time (**Status**), the recipe type and origin (**Recipe configuration**), the destination, output path and access (**Location**), and the export progress or error message (**Progress**).

The task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    This operation is running between GEE and SEPAL servers in the background. You can close the SEPAL page without stopping the process.

Access
^^^^^^

Once the export to the SEPAL workspace is complete, you can access the data in your SEPAL folders. By default, the data are stored in the :code:`downloads` folder using the following format:

.. code-block::

    .
    └── downloads/
        └── <recipe name>/
            ├── <recipe name>_<gee tile id>.tif
            ├── <recipe name>_<gee tile id>.tif
            ├── ...
            ├── <recipe name>_<gee tile id>.tif
            └── <recipe name>.vrt

.. note::

    Understanding how images are stored in a radar mosaic is only required if you want to manually use them. The SEPAL applications are bound to this tiling system and can digest the information for you.

The data are stored in a folder named after the recipe (see `Start`_). Large images are too big to be exported as a single file, so they are divided into smaller tiles (:code:`.tif` files), which are brought back together by a :code:`<recipe name>.vrt` file.

.. tip::

    The full folder, with all its files, is required to read the :code:`.vrt` file.

.. important::

    Now that you have exported the radar mosaic to your SEPAL workspace, it can be downloaded to your computer using `file exchange options <../setup/filezilla.html>`__ or used in other SEPAL workflows.

Video tutorial
--------------

The following video tutorial demonstrates how to create a yearly time scan for land cover mapping in a reproducible way:

.. youtube:: lip8C4tq7ig
    :height: 315
    :width: 560
