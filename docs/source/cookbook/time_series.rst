Time series
===========

*Create and retrieve SITS to study patterns and key changes in landscape evolution over time*

Overview
--------

A Satellite Image Time Series (SITS) is a set of satellite images taken of the same scene at different times. A SITS makes use of different satellite sources to obtain a larger data series with a short time interval between two images. In this case, it is fundamental to observe the spatial resolution and registration constraints.

Satellite observations offer opportunities for understanding how the Earth is changing, determining the causes of these changes and predicting future changes. Remotely sensed data, combined with information from ecosystem models, offer an opportunity for predicting and understanding the behaviour of Earth's ecosystems. Sensors with high spatial and temporal resolutions make the observation of precise spatio-temporal structures in dynamic scenes more accessible. Temporal components integrated with spectral and spatial dimensions allow the identification of complex patterns concerning applications connected with environmental monitoring and analysis of land cover dynamics.

Change detection can only provide a "before and after" scenario; a time-series analysis provides an opportunity to study patterns and key changes in the landscape evolution over time.

This SEPAL recipe allows users to create and retrieve a SITS of one or more bands or indexes, built from **optical** (Landsat and Sentinel-2), **radar** (Sentinel-1) or **Planet** imagery available in Google Earth Engine (GEE). Every acquisition in the selected period becomes one band of the output, named after its acquisition date.

.. note::

    You won't be able to retrieve the images if your SEPAL and Google Earth Engine (GEE) accounts are not connected. For more information, go to :doc:`../setup/gee`.

Start
-----

To create a new time series, go to the :btn:`<fa-solid fa-globe>` **Process** section and select :btn:`<fa-solid fa-plus> Add recipe` (first image below). In the **Create recipe** list that opens, select **Time series** (second image).

.. thumbnail:: ../_images/cookbook/time_series/create_recipe.png
    :width: 49%
    :title: Select **Add recipe** in the **Process** section
    :group: time-series-recipe

.. thumbnail:: ../_images/cookbook/time_series/sepal_recipes.png
    :width: 49%
    :title: Select **Time series** in the **Create recipe** list
    :group: time-series-recipe

Once the **Time series** recipe is selected, SEPAL will display the recipe process in a new tab. The first step is to change the name of the recipe. This name will be used to identify your files and recipes in SEPAL folders. Use the best-suited convention for your needs. Simply double-click the tab (see **1** in the image below) and write a new name. It defaults to :code:`Time_series_<creation date>_<creation time>` (e.g. :code:`Time_series_2026-10-22_10-15-30`).

.. note::

    The SEPAL team recommends using the following naming convention: :code:`<aoi name>_<start>-<end>_<measure>_<sensors>` (e.g. :code:`sgp_2012-2018_ndfi_l78`).

.. thumbnail:: ../_images/cookbook/time_series/landing.png
    :title: The landing page of the time series recipe
    :group: time-series-recipe

Parameters
----------

When a new recipe opens, the **Area of interest** window is displayed in the lower-right corner (see **2** in the image above). To its right, four tabs are available, which allow you to customize the time series to your needs:

-   :guilabel:`AOI`: area of interest
-   :guilabel:`DAT`: start and end dates of the time series
-   :guilabel:`SRC`: source datasets of the time series
-   :guilabel:`PRC`: pre-processing parameters

Select a tab to open the corresponding panel. Each panel is described in the following sections.

AOI selection
^^^^^^^^^^^^^

The data exported by the recipe will be generated from within the bounds of the AOI. There are multiple ways to select the AOI in SEPAL:

-   Administrative boundaries
-   EE Tables
-   Assets or recipes
-   GeoID
-   Drawn polygons

For more information, read :doc:`../feature/aoi_selector`.

Dates
^^^^^

In the :guilabel:`DAT` tab, select the **Start date** and the **End date** of the time series. Select a date field to open the date picker, or type the date in the :code:`YYYY-MM-DD` format.

-   **Start date**: the first date of the time series (inclusive). It defaults to **2000-01-01**.
-   **End date**: the last date of the time series (exclusive). It defaults to the current date.

The start date must be before the end date. Dates can be selected from 1982-08-22 (the start of the Landsat 4 archive) onward.

.. thumbnail:: ../_images/cookbook/time_series/dates.png
    :title: The **Dates** panel
    :group: time-series-recipe

Sources
^^^^^^^

In the :guilabel:`SRC` tab, select the imagery the time series is built from. Three types of data are available: **Optical** (Landsat and Sentinel-2), **Radar** (Sentinel-1) and **Planet**. A time series uses a single type of data: first, select the **Type**, then the **Data set**.

-   :guilabel:`Optical`: select one or more of the optical datasets. By default, all Tier 1 Landsat datasets are selected (**L9**, **L8**, **L7** and **L4-5**).

    -   :guilabel:`L9`, :guilabel:`L8`, :guilabel:`L7`, :guilabel:`L4-5`: **Landsat 9**, **8**, **7** and **4-5** (Tier 1).
    -   :guilabel:`L8 T2`, :guilabel:`L9 T2`, :guilabel:`L7 T2`, :guilabel:`L4-5 T2`: the **Tier 2** equivalents of the datasets listed above.
    -   :guilabel:`S2`: **Sentinel-2** (Sentinel-2A and Sentinel-2B).

    For a description of each dataset and of the Landsat tiers, see the `Sources <optical_mosaic.html#sources>`__ section of the **Optical mosaic** recipe.

-   :guilabel:`Radar`: :guilabel:`S1`, the **Sentinel-1** C-band SAR collection (Sentinel-1A and Sentinel-1B).
-   :guilabel:`Planet`: select one of the Planet collections:

    -   :guilabel:`NICFI basemaps`: the **NICFI Planet basemaps** (level 1 composites) over the tropics.
    -   :guilabel:`Custom basemaps`: your own image collection of **Planet basemaps** (level 1 composites).
    -   :guilabel:`Daily imagery`: your own image collection of **daily Planet imagery** (level 2).

    For **Custom basemaps** and **Daily imagery**, enter the ID of the GEE image collection in the **Earth Engine asset ID** field.

Datasets with no imagery in the selected dates are grayed out (unless already selected).

In the advanced view (select :guilabel:`More`), you can also select one of your **Classification** recipes in the optional **Classification** field. Its classifier is then applied to every acquisition of the time series, and the class probabilities (and, for regression, the predicted value) become available as bands in the chart and in the retrieve panel.

.. thumbnail:: ../_images/cookbook/time_series/sources.png
    :title: The **Sources** panel (advanced view)
    :group: time-series-recipe

Pre-processing
^^^^^^^^^^^^^^

The :guilabel:`PRC` tab defines how the images are corrected and masked before they are added to the time series. Its content depends on the **Type** selected in the :guilabel:`SRC` tab.

.. note::

    This step is optional; default values are set for every type of data.

Optical
"""""""

For optical data, the panel is a simplified version of the `Composite <optical_mosaic.html#composite>`__ panel of the **Optical mosaic** recipe: as every acquisition is kept, there is no composing method, no pixel filters and no cloud buffering. The panel opens in a **simple** view; select :guilabel:`More` to reveal the **advanced** options (and :guilabel:`Less` to hide them again).

.. note::

    By default, SEPAL applies:

    -   Corrections: **None** (top-of-atmosphere reflectance is used)
    -   Cloud masking: **Moderate**
    -   Snow/ice masking: **On**

.. thumbnail:: ../_images/cookbook/time_series/preprocess_optical.png
    :title: The **Pre-process** panel for optical data (advanced view)
    :group: time-series-recipe

**Corrections**

-   :guilabel:`SR`: Uses the atmospherically corrected surface reflectance of the scenes instead of the top-of-atmosphere (TOA) reflectance.
-   :guilabel:`BRDF`: Corrects for bidirectional reflectance distribution function (BRDF) effects. In the advanced view, the **BRDF Multiplier** field controls how much correction is applied: the higher the value, the stronger the correction (default **4**).
-   :guilabel:`Calibrate`: Calibrates the bands to improve the consistency between sensors. In a time series, calibration is always applied when **SR** is not selected.

**Cloud masking**

In the simple view, choose a preset:

-   :guilabel:`Moderate`: Standard cloud masking.
-   :guilabel:`Aggressive`: Uses the same algorithms with stricter thresholds. It masks more clouds, but may also mask built-up areas and other bright features.
-   :guilabel:`Custom`: Automatically selected when you fine-tune the individual cloud-masking algorithms in the advanced view.

In the advanced view, you can add and configure the individual cloud-masking algorithms (**SEPAL Cloud Score**, **S2 Cloud Score+**, **S2 Cloud Probability**, **Landsat CFMask** and **Pino 26**). The available algorithms depend on the selected datasets: the S2 algorithms require Sentinel-2, **Landsat CFMask** requires Landsat, and **Pino 26** requires Sentinel-2 only, without **SR**. They are described in the `Cloud masking <optical_mosaic.html#cloud-masking>`__ section of the **Optical mosaic** recipe.

**Sentinel-2 overlap (advanced view)**

Shown only when Sentinel-2 is selected. Sentinel-2 acquisitions overlap both between orbits and between neighbouring tiles, which can result in duplicated observations.

-   **Orbit overlap**: :guilabel:`Keep` the overlap between Sentinel-2 orbits or :guilabel:`Remove` it. Defaults to **Keep**.
-   **Tile overlap**: :guilabel:`Keep` the overlap between Sentinel-2 tiles, :guilabel:`Quick remove` most of it, or :guilabel:`Remove` all of it. Defaults to **Quick remove**.

**Snow/ice masking (advanced view)**

-   :guilabel:`On`: Masks snow. This tends to leave some pixels with shadowy snow.
-   :guilabel:`Off`: Doesn't mask snow. Note that some clouds might get misclassified as snow; therefore, disabling snow masking might lead to cloud artifacts.

Radar
"""""

For radar data, the panel contains the same options as the `Options <radar_mosaic.html#options>`__ panel of the **Radar mosaic** recipe (orbits, geometric correction, speckle filters, outlier removal, orbit overlap, border noise correction and minimum observations). Refer to that article for a description of each option.

.. note::

    The defaults differ from the radar mosaic recipe, to keep each acquisition close to the original data:

    -   Orbits: **Ascending** and **Descending**
    -   Geometric correction: **Ellipsoid**
    -   Spatial speckle filter: **None**
    -   Multitemporal speckle filter: **None**
    -   Outlier removal: **None**

Planet
""""""

For Planet data, the panel contains the following options:

-   **Cloud masking**: Planet composites already remove clouds. Use this slider to remove additional clouds: the higher the value, the more pixels are masked as clouds. At **0%**, no additional clouds are removed. Defaults to **85%**.
-   **Cloud buffering**: :guilabel:`None`, :guilabel:`Moderate` (an additional **120 m** around each larger cloud) or :guilabel:`Aggressive` (an additional **600 m**). Defaults to **None**.
-   **Histogram matching** (only shown for **Daily imagery**): :guilabel:`Enabled` normalizes the images using histogram matching. This slows down processing significantly and can cause some details to be lost, but can significantly improve the overall consistency and noise level. Defaults to **Disabled**.

Analysis
--------

Once all the parameters are set, you can plot the time series of a pixel using the :btn:`<fa-solid fa-chart-area>` button in the upper-right corner of the map.

.. tip::

    The button is only enabled when the parameters are complete. If it is disabled, check your parameters, as some might be missing.

Plot
^^^^

Select :btn:`<fa-solid fa-chart-area>` to start the plotting tool. Move the pointer to the main map; the pointer will be transformed into a :icon:`fa-solid fa-plus`. Click anywhere in the AOI to plot the observations of this specific location in a pop-up window.

-   The coordinates of the selected point are displayed in the header of the window. Select :btn:`<fa-solid fa-copy>` next to them to copy them to the clipboard.
-   Select the band or index to display in the dropdown list in the upper-left corner. The available bands are the same as in the **Retrieve** panel (see `Bands to retrieve`_).
-   On the chart, each dot represents one valid observation (i.e. one that was not masked by the pre-processing). Hover over a dot to display its **Date** and **Observation** value. Values are scaled: optical values by 10,000 (e.g. an NDVI of 0.6 is displayed as 6000), radar **VV** and **VH** by 100, and **ratio_VV_VH** by 1,000.
-   Drag the handles of the range selector below the chart to zoom in on a period.
-   Select :btn:`<fa-solid fa-download> Export CSV` in the lower-left corner to download the observations of the selected band as a :code:`.csv` file, named :code:`<recipe name>_<band>_<latitude>_<longitude>.csv`. The file covers the whole period, even if you zoomed in on the chart, and contains the values as displayed on the chart.

Select :guilabel:`Close` (or press :kbd:`Esc`) to close the window.

.. thumbnail:: ../_images/cookbook/time_series/plot.png
    :title: The chart of the NDVI observations of a pixel
    :group: time-series-recipe

.. attention::

    The plot retrieves the information from GEE on the fly. Depending on the number of observations and the selected pre-processing parameters, this can take some time; a spinner is displayed while the data are loading. If the pixel has no valid observation, the message **Pixel has no observations** is displayed.

Retrieve
--------

.. important::

    You cannot retrieve a time series to your SEPAL workspace without a small computation quota. If you are a new user, see :doc:`../setup/resource`.

In the upper-right corner, select the :btn:`<fa-solid fa-cloud-arrow-down>` button to open the **Retrieve** panel, where you can select the exportation parameters. A time series is always retrieved to your **SEPAL workspace**.

.. thumbnail:: ../_images/cookbook/time_series/retrieve.png
    :title: The **Retrieve** panel
    :group: time-series-recipe

Bands to retrieve
^^^^^^^^^^^^^^^^^

Select one or more bands or indexes to export in **Bands to retrieve**. Each band is exported to its own folder (see `Access`_). The available bands depend on the **Type** selected in the :guilabel:`SRC` tab:

-   **Optical**: the spectral bands of the selected datasets (e.g. **blue**, **green**, **red**, **nir**, **swir1**, **swir2**) and the spectral indexes computed from them (e.g. **ndvi**, **ndmi**, **ndfi**). For the full list, see :doc:`../feature/optical_bands`.
-   **Radar**: **VV**, **VH**, **ratio_VV_VH** and **orbit**. For more information, see :doc:`../feature/radar_bands`.
-   **Planet**: **blue**, **green**, **red** and **nir**, and the indexes **ndvi**, **ndwi**, **evi**, **evi2** and **savi**.

If a **Classification** recipe is selected in the :guilabel:`SRC` tab, the class probability bands (or the regression band) are also available.

.. note::

    There is no fixed rule to the band selection. Each index is more adapted to a set of analyses in a defined biome. The knowledge of the study area, the evolution expected and the careful selection of an adapted measure will improve the quality of downstream analysis.

Scale
^^^^^

You can set a custom scale for exportation by selecting a value in metres (m). The default is **30 m**. Note that requesting a smaller resolution than the native resolution of the data (e.g. 30 m for Landsat, 10 m for Sentinel-2 and Sentinel-1) will not improve the quality of the output, just its size.

Additional outputs
^^^^^^^^^^^^^^^^^^

Select :guilabel:`SITS files` to also create, for every acquisition date, a :code:`.vrt` file that can be read as a data cube by the `sits R package <https://e-sensing.github.io/sitsbook/>`__. This option is off by default.

Destination
^^^^^^^^^^^

-   **Workspace path**: the destination folder in your SEPAL workspace. By default, :code:`downloads/<recipe name>`, or :code:`downloads/<project name>/<recipe name>` if the recipe belongs to a project.
-   **Filename prefix**: added to the name of every exported file. By default, the recipe name.

Select :guilabel:`More` to show additional export settings:

-   **Tile size**: the AOI is split into tiles of this size, in degrees (default **2**). Each tile is exported in its own folder.
-   **Shard size**: the size, in pixels, of the pieces GEE breaks the image into for processing (default **256**).
-   **File dimensions multiple**: the maximum size of each exported file, as a multiple of the shard size (default **2**, i.e. files of up to 512 x 512 pixels).
-   **CRS** and **CRS transform**: the coordinate reference system and, optionally, the affine transform of the exported images.

The default values are suitable in most cases; reduce the tile or shard size if the export runs out of memory.

Select :guilabel:`Retrieve` to start the export process.

Exportation status
^^^^^^^^^^^^^^^^^^

Follow the export in the **Tasks** tab (lower-left corner). For more information, see :doc:`../feature/tasks`.

The progress of a time series is reported tile by tile (e.g. :code:`Exported 40% of tile 1 out of 3.`), followed by :code:`Assembling tile 1 out of 3...` when the files of a tile are being stacked.

Access
^^^^^^

Once the export is complete, you can access the data in your SEPAL folders. By default, the data are stored in the :code:`downloads` folder using the following format:

.. code-block::

    .
    └── downloads/
        └── <recipe name>/
            ├── <band>/
            │   ├── <tile number>/
            │   │   ├── chunk-<start date>_<end date>/
            │   │   │   ├── <prefix>_<tile number>_<start date>_<end date>-<gee tile id>.tif
            │   │   │   ├── ...
            │   │   │   └── <prefix>_<tile number>_<start date>_<end date>-<gee tile id>.tif
            │   │   ├── ...
            │   │   ├── chunk-<start date>_<end date>/
            │   │   ├── tile-<gee tile id>/
            │   │   │   └── stack.vrt
            │   │   ├── ...
            │   │   ├── tile-<gee tile id>/
            │   │   ├── dates.csv
            │   │   └── stack.vrt
            │   ├── ...
            │   └── <tile number>/
            ├── ...
            ├── <band>/
            └── sits/
                ├── <tile number>/
                │   ├── SEPAL_<gee tile id>_<BAND>_<date>.vrt
                │   ├── ...
                │   └── SEPAL_<gee tile id>_<BAND>_<date>.vrt
                ├── ...
                └── <tile number>/

.. note::

    Understanding how images are stored in a time series is only required if you want to manually use them. The SEPAL applications are bound to this tiling system and can digest the information for you.

The data are stored in a folder named after the recipe, with one sub-folder per retrieved band (e.g. :code:`ndvi`). As GEE cannot export an image collection, and as the data are usually too big to be exported at once, SEPAL divides them into smaller pieces and reassembles them in :code:`stack.vrt` files:

-   **Tiles**: the AOI is divided into tiles of the selected **Tile size** (2 degrees by default). Each tile is stored in a folder named with its number, starting at :code:`0`.
-   **Chunks**: in each tile, the time period is divided into chunks of 3 months, stored in :code:`chunk-<start date>_<end date>` folders. Periods without any imagery are skipped. Each chunk contains one or more :code:`.tif` files, as GEE splits large images into pieces identified by a GEE tile ID (e.g. :code:`0000000000-0000000000`). Each file has one band per acquisition date, named with the date (:code:`YYYY-MM-DD`); acquisitions from the same day are merged using their median.
-   **Stacks**: in each tile, one :code:`tile-<gee tile id>/stack.vrt` file gathers the files of all chunks for one GEE tile, covering the full time period. The main :code:`stack.vrt` file of the tile then combines all of them.
-   **Dates**: the :code:`dates.csv` file lists all the observation dates of the tile in chronological order, matching the bands of :code:`stack.vrt`.
-   **SITS files** (only if selected in `Additional outputs`_): the :code:`sits` folder contains, for each tile, one :code:`.vrt` file per GEE tile, band and acquisition date. The band name is written in upper case, with hyphens instead of underscores (e.g. :code:`NDVI`, :code:`RATIO-VV-VH`). The files of all bands are stored in the same folder, so they can be loaded as one multi-band cube.

.. note::

    The dates contained in :code:`dates.csv` can differ from one tile to another, due to data availability and pre-processing filters.

.. tip::

    The full folder, with all its files, is required to read the :code:`.vrt` files.

.. important::

    Now that you have exported the time series to your SEPAL workspace, it can be downloaded to your computer using `file exchange options <../setup/filezilla.html>`__ or used in one of our `Time-series analysis modules <../modules/time-series.html>`__.
