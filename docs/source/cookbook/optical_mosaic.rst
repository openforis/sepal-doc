Optical mosaics
===============
*Combine images to create single raster datasets with optical mosaics*

Overview
--------

A mosaic is a combination or fusion of two or more images. In SEPAL, you can create a single raster dataset from several raster datasets by mosaicing them together.
This can be achieved on both contiguous rasters (see first image below) and overlapping images (see second image below).

.. thumbnail:: ../_images/cookbook/optical_mosaic/mosaic_contiguous.gif
    :width: 49%
    :group: optical-mosaic-recipe
    :title: Contiguous rasters

.. thumbnail:: ../_images/cookbook/optical_mosaic/mosaic_overlay.png
    :width: 49%
    :group: optical-mosaic-recipe
    :title: Overlapping images

These overlay areas can be managed in various ways. For example, you can choose to:

-   keep only the raster data from the first or last dataset;
-   combine the values of the overlay cells using a weighting algorithm;
-   average the values of the overlay cells; or
-   take the maximum or minimum value.

In addition, certain corrections can be made to the image to account for clouds, snow and other factors; these operations are complex and repetitive.

SEPAL offers you an interactive and intuitive way to create mosaics in any area of interest (AOI).

.. Note::

    You won't be able to retrieve the images if your SEPAL and Google Earth Engine (GEE) accounts are not connected. For more information, go to :doc:`../setup/gee`.

Start
-----

Once the mosaic recipe is selected, SEPAL will display the recipe process in a new tab (see **1** in the image below) and the **AOI selection** window will appear in the lower right (**2**).

.. thumbnail:: ../_images/cookbook/optical_mosaic/landing.png
    :group: optical-mosaic-recipe
    :title: The landing page of the optical mosaic recipe

The first step is to change the name of the recipe. This name will be used to identify your files and recipes in SEPAL folders. Use the best-suited convention for your needs. Simply double-click the tab and write a new name. It defaults to :code:`Optical_mosaic_<start_date>_<end_date>_<band name>`.

.. thumbnail:: ../_images/cookbook/optical_mosaic/default_title.png
    :title: Optical mosaics default title
    :width: 49%

.. thumbnail:: ../_images/cookbook/optical_mosaic/modified_title.png
    :title: Optical mosaics modified title
    :width: 49%

.. note::

    The SEPAL team recommends using the following naming convention: :code:`<aoi name>_<dates>_<measure>`.

Parameters
----------

In the lower-right corner, five tabs are available, which allow you to customize the mosaic creation to your needs:

-   :guilabel:`AOI`: area of interest
-   :guilabel:`DAT`: target date of interest for the mosaic/composite
-   :guilabel:`SRC`: source datasets of the mosaic/composite
-   :guilabel:`SCN`: scene selection parameters
-   :guilabel:`CMP`: composition parameters

.. thumbnail:: ../_images/cookbook/optical_mosaic/no_parameters.png
    :title: The five tabs to set up SEPAL optical mosaic parameters
    :group: optical-mosaic-recipe

AOI selection
^^^^^^^^^^^^^

The data exported by the recipe will be generated from within the bounds of the AOI. There are multiple ways to select the AOI in SEPAL:

-   Administrative boundaries
-   EE Tables
-   Drawn polygons

They are extensively described in our documentation. For more information, read :doc:`../feature/aoi_selector`.

.. thumbnail:: ../_images/cookbook/optical_mosaic/aoi.png
    :title: Select AOI based on administrative layers
    :group: optical-mosaic-recipe

Date
^^^^

Yearly mosaic
"""""""""""""

In the :guilabel:`DAT` tab, select a year which pixels in the mosaic should come from. Then select the :icon:`fa-solid fa-check` :guilabel:`Apply` button.

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_year.png
    :title: The year selection panel
    :group: optical-mosaic-recipe

Seasonal mosaic
"""""""""""""""

Select :guilabel:`More` in the :guilabel:`DAT` panel to expand the date selection tool. Rather than selecting a year, you can select a season of interest.

Select the :icon:`fa-solid fa-calendar` (**1**) to open the **Date selection** pop-up window. The selected date will be the target of the mosaic (i.e. the date from which pixels in the mosaic should ideally come from).

Using the main slider (**2**), define a season around the target date by identifying a start date and end date. SEPAL will then retrieve the mosaic images between those dates.

The number of images in a single season of one year may not be enough to produce a correct mosaic. SEPAL provides two secondary sliders to increase the pool of images to create the mosaic. Both count the number of seasons SEPAL can retrieve in the past (:code:`Past season` - [**3**]) and in the future (:code:`Future season` - [**4**]).

When the selection is done, select the :icon:`fa-solid fa-check` :guilabel:`Apply` button.

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_season.png
    :title: The **Season selection** pane
    :group: optical-mosaic-recipe

Sources
^^^^^^^

As mentioned in the introduction, a mosaic combines raster datasets that can come from multiple satellite sources. In the :guilabel:`SRC` tab, select one or more **optical** data sources to build the mosaic from.

**Landsat** scenes are distributed in two quality tiers:

-   **Tier 1** holds the scenes with the highest data quality. They are processed to Level-1 Precision Terrain (L1TP), have well-characterized radiometry, are intercalibrated across the different Landsat sensors and are geo-registered within prescribed tolerances (12 m root mean square error [RMSE] or less). Tier 1 scenes are consistent across the full collection and suitable for time-series analysis.
-   **Tier 2** (marked :guilabel:`T2`) holds scenes that do not meet the Tier 1 criteria, for example because of significant cloud cover, insufficient ground control or systematic-only terrain correction (L1GT/L1GS). They can still be useful; analyze the RMSE and other properties to determine their suitability for your study.

The following optical sources are available (select a link to open the corresponding Google Earth Engine dataset):

-   :guilabel:`L9`: `Landsat 9 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2>`__ (Tier 1; from 2021).
-   :guilabel:`L8`: `Landsat 8 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2>`__ (Tier 1; from 2013).
-   :guilabel:`L7`: `Landsat 7 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_L2>`__ (Tier 1; from 1999).
-   :guilabel:`L4-5`: `Landsat 4 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT04_C02_T1_L2>`__ combined with `Landsat 5 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_L2>`__ (Tier 1; 1982–2012).
-   :guilabel:`L9 T2`, :guilabel:`L8 T2`, :guilabel:`L7 T2`, :guilabel:`L4-5 T2`: the **Tier 2** equivalents of the datasets listed above.
-   :guilabel:`S2`: `Sentinel-2 <https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED>`__ (Sentinel-2A and Sentinel-2B; from 2015). A wide-swath, high-resolution, multispectral imaging mission supporting Copernicus Land Monitoring studies, including the monitoring of vegetation, soil and water cover, as well as the observation of inland waterways and coastal areas.

.. note::

    SEPAL uses the Landsat **Collection 2** archive and the **harmonized** Sentinel-2 collection.

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_source.png
    :title: The **Source selection** pane
    :group: optical-mosaic-recipe

You can also restrict the imagery with the :code:`Max cloud cover %` slider: scenes whose cloud cover is higher than this threshold are excluded before the mosaic is built.

To validate your selection, select the :icon:`fa-solid fa-check` :guilabel:`Apply` button (labelled :guilabel:`Done` when you first create the recipe through the setup wizard).

Scenes
^^^^^^

.. note::

    If Sentinel and Landsat data have been selected, you will be forced to use all scenes. As the tiling system from Sentinel and Landsat data are different, it's impossible to select scenes using the tool presented in the following sections.

You can use multiple options to select the best scenes for your mosaic. The most simple is to use every image available based on the date parameters. Select :guilabel:`Use all scenes` and all images will be integrated into the mosaic.

Choose :guilabel:`Select scenes` and pick one of the three available :code:`Priority` options, based on the needs of your analysis (SEPAL sorts the images available for each tile):

-   :guilabel:`Cloud free`: Prioritizes imagery as cloud-free as possible, ignoring the date.
-   :guilabel:`Balanced`: Prioritizes imagery that is neither too cloudy nor too far from the target date.
-   :guilabel:`Target date`: Prioritizes imagery as close as possible to the target date.

To validate your selection, select the :icon:`fa-solid fa-check` :guilabel:`Apply` button.

.. thumbnail:: ../_images/cookbook/optical_mosaic/scene_method.png
    :title: The **Scenes** pane
    :group: optical-mosaic-recipe

Composite
^^^^^^^^^

The :guilabel:`CMP` tab controls how the selected scenes are corrected, how clouds and snow are masked, and how the final pixel values are computed. The panel opens in a **simple** view showing the most common options; select :guilabel:`More` to reveal the **advanced** options (and :guilabel:`Less` to hide them again).

.. note::

    This step is optional. By default, SEPAL applies:

    -   **Corrections**: :guilabel:`SR` and :guilabel:`BRDF`
    -   **Cloud masking**: :guilabel:`Moderate`
    -   **Composing method**: :guilabel:`Medoid`

    The advanced view additionally defaults to no pixel filters, no cloud buffering and snow/ice masking turned on.

.. thumbnail:: ../_images/cookbook/optical_mosaic/composite_options.png
    :group: optical-mosaic-recipe
    :title: The composite options pane (simple view)

.. dropdown:: Show the advanced view (opened with **More**)
    :icon: image
    :margin: 3 0 0 0

    .. thumbnail:: ../_images/cookbook/optical_mosaic/composite_options_advanced.png
        :width: 30%
        :group: optical-mosaic-recipe
        :title: The composite options pane (advanced view, opened with **More**)

Corrections
"""""""""""

Corrections are applied to the stacked pixels to improve the quality of the mosaic.

-   :guilabel:`SR`: Surface reflectance improves comparison between multiple images over the same region by accounting for atmospheric effects such as aerosol scattering and thin clouds, which can help in the detection and characterization of Earth surface change. Top-of-atmosphere (TOA) images are used if not selected.
-   :guilabel:`BRDF`: Uses a bidirectional reflectance distribution function (BRDF) model to characterize surface reflectance anisotropy. For a given land area, the BRDF is established based on selected multi-angular observations of surface reflectance. When BRDF is enabled, the advanced view shows a :code:`BRDF Multiplier` field that controls how much correction is applied (values of 3–4 usually work well; lower it if the effect is overcompensated, raise it if it is not compensated enough).
-   :guilabel:`Calibrate`: Calibrates the bands to improve a cross-sensor mosaic.

    .. note::

        This option is only available if:

        -   Landsat and Sentinel-2 data are mixed; and
        -   surface reflectance (:guilabel:`SR`) correction is disabled.

Cloud masking
"""""""""""""

Controls how clouds are detected and masked. In the simple view, choose a preset:

-   :guilabel:`Moderate`: Relies only on the image source QA bands for cloud masking.
-   :guilabel:`Aggressive`: Relies on the image source QA bands together with a cloud-scoring algorithm. This will probably mask out some built-up areas and other bright features.
-   :guilabel:`Custom`: Automatically selected (and otherwise disabled) when you fine-tune the individual cloud-masking algorithms in the advanced view.

In the advanced view you can add and configure the individual cloud-masking algorithms with the :icon:`fa-solid fa-plus` button. The available algorithms depend on the sources you selected:

-   :guilabel:`SEPAL cloud score`: SEPAL's own cloud-scoring algorithm, with a configurable *maximum cloud probability*. Always available.
-   :guilabel:`S2 Cloud Score+`: Sentinel-2 Cloud Score+, with a *maximum cloud probability* and a choice of scoring band — :guilabel:`cs` (instantaneous clear-sky similarity) or :guilabel:`cs_cdf` (likelihood of being clear over time). Sentinel-2 sources only.
-   :guilabel:`S2 Cloud Probability`: the Sentinel-2 cloud-probability dataset, with a configurable *maximum cloud probability*. Sentinel-2 sources only.
-   :guilabel:`Landsat CFMask`: the Landsat CFMask QA bands. You can set :code:`Cloud Masking`, :code:`Cloud Shadow Masking` and :code:`Cirrus Masking` each to :guilabel:`Off`, :guilabel:`Moderate` or :guilabel:`Aggressive`, and choose whether to :guilabel:`Keep` or :guilabel:`Remove` dilated clouds. Landsat sources only.
-   :guilabel:`Pino 26`: the Pan-Tropical Sentinel-2 cloud-detection algorithm developed by Dario Simonetti (for more information, see `D. Simonetti [2021] <https://doi.org/10.1016/j.dib.2021.107488>`__). Only available for a Sentinel-2-exclusive source when :guilabel:`SR` correction is disabled.

Cloud buffering
"""""""""""""""

(Advanced view.) When pixels are identified as clouds, SEPAL can also mask a small buffer around them to prevent hazy pixels at the borders of clouds from being included in the mosaic.

.. note::

    Buffering is done at the pixel level, so using this option significantly increases the creation time of the mosaic.

-   :guilabel:`None`: Doesn't use cloud buffering.
-   :guilabel:`Moderate`: Masks an additional **120 m** around each larger cloud.
-   :guilabel:`Aggressive`: Masks an additional **600 m** around each larger cloud.

Snow/ice masking
""""""""""""""""

(Advanced view.) Defines how snowy or icy pixels are masked.

-   :guilabel:`On`: Masks snow. This tends to leave some pixels with shadowy snow.
-   :guilabel:`Off`: Doesn't mask snow. Note that some clouds might get misclassified as snow; therefore, disabling snow masking might lead to cloud artifacts.

Masked out pixels
"""""""""""""""""

(Advanced view.) Controls whether a pixel can end up completely masked when every available acquisition is cloudy and/or snowy.

-   :guilabel:`Prevent`: Prevents pixels from being completely masked out, keeping the best available (possibly cloudy/snowy) value.
-   :guilabel:`Allow`: Allows pixels to be completely masked out, leaving holes in the mosaic where no clear observation exists.

Pixel filters
"""""""""""""

(Advanced view.) Add filters with the :icon:`fa-solid fa-plus` button to remove pixels from the stack before compositing. Each filter excludes a percentage of the stack (set with a slider, defaulting to 50%); removing low-quality pixels improves the quality of the mosaic.

.. note::

    Each filter is applied iteratively (e.g. if the normalized difference vegetation index [NDVI] is already filtering all pixels but one, there will be nothing left in the stack to be filtered by date).

    Note as well that adding filters significantly increases the creation time of the mosaic.

-   **Shadow**: Excludes the selected percentage of pixels with the most shadow.
-   **Haze**: Excludes the selected percentage of pixels with the most haze. Only available when :guilabel:`SR` correction is disabled.
-   **NDVI**: Excludes the selected percentage of pixels with the lowest NDVI.
-   **Date**: Excludes the selected percentage of pixels farthest from the target date.

Sentinel-2 overlap
""""""""""""""""""

(Advanced view; shown only when Sentinel-2 is selected.) Sentinel-2 acquisitions overlap both between orbits and between neighbouring tiles, which can result in duplicated observations.

-   **Orbit Overlap**: :guilabel:`Keep` the overlap between Sentinel-2 orbits (more data, better models) or :guilabel:`Remove` it.
-   **Tile Overlap**: :guilabel:`Keep` the overlap between Sentinel-2 tiles, :guilabel:`Quick remove` most of it, or :guilabel:`Remove` all of it. Removing overlap adds an extra preprocessing step.

Composing method
""""""""""""""""

After filtering the stack of pixels, the composing method defines how the final pixel value is extracted.

-   :guilabel:`Medoid`: Uses the pixel closest to the median value. As a real pixel from the stack, the final value embeds metadata (e.g. the date of observation).
-   :guilabel:`Median`: Uses the computed median value. If no pixel matches this value, the pixel will not embed any metadata. It tends to produce smoother mosaics.

Analysis
--------

After selecting the parameters, you can start interacting with the scenes and begin the analysis.

In the upper-right corner, three tabs are available, which allow you to customize the mosaic scene selection and export the final result:

-   :btn:`<fa-solid fa-wand-sparkles>`: auto-select scenes
-   :btn:`<fa-solid fa-trash>`: clear selected scenes
-   :btn:`<fa-solid fa-cloud-arrow-down>`: retrieve mosaic

.. thumbnail:: ../_images/cookbook/optical_mosaic/analysis.png
    :title: The three tabs to select the scenes and export mosaic
    :group: optical-mosaic-recipe

.. note::

    If you have not selected the option :guilabel:`Select scenes` in the :guilabel:`SCN` tab, the :icon:`fa-solid fa-wand-sparkles` button will be disabled and the scene areas will be hidden as no scene selection needs to be performed (see those with a number in a circle on the previous screenshot).

    If you can't see the image scene area, you probably have selected a small AOI. Zoom out on the map and you will see the number of available images in the circles.

Select scenes
^^^^^^^^^^^^^

To create a mosaic, select the scenes that will be used to compute each pixel value of the mosaic. SEPAL provides a user-friendly interface that will guide you through the selection process. You don't have to select the stack for every pixel; instead, SEPAL will clip the AOI in smaller pieces called **Tiles**. These tiles correspond to the native tiling system of your dataset and are displayed on the map with circled numbers in their centroid. Each number corresponds to the number of scenes available to build the mosaic tile. Hover over these circles to see the tile boundaries appear.

.. note::

    Landsat and Sentinel datasets have a different grid system, which is why the selection process cannot be used if you have selected both of these datasets. If you have an idea related to the user interface (UI) that could make them work together, let us know in our `issue tracker <https://github.com/openforis/sepal>`__.

Auto-select scene
"""""""""""""""""

Selecting the :icon:`fa-solid fa-wand-sparkles` tab will open the **Auto-selection** pane.

Move the sliders to set the :code:`Minimum number of scenes` and the :code:`Maximum number of scenes` SEPAL should select in a tile. Then, select the :guilabel:`Select scenes` button to apply the auto-select method.

SEPAL will use the priority defined in the :guilabel:`SCN` tab to order the scene and collect the optimal number for your request.

.. note::

    The result is never perfect but can be used as a starting point for the manual selection of scenes.

.. thumbnail:: ../_images/cookbook/optical_mosaic/auto-select.png
    :title: Pane to select the minimum and maximum number of scenes to auto-select in each tile.
    :group: optical-mosaic-recipe

Clear all scenes
""""""""""""""""

If at least one scene is selected, the :icon:`fa-solid fa-trash` tab will be available. Select it to open the **Clear** pane.

Select :guilabel:`Clear scenes` to remove all manually and automatically selected scenes.

.. thumbnail:: ../_images/cookbook/optical_mosaic/remove_all.png
    :title: The pane to unselect all scenes from the mosaic.
    :group: optical-mosaic-recipe

Manual selection
""""""""""""""""

To open the **Scene selection** menu, hover over a tile circled-number and select it (**1**). The window will be divided into two sections:

-   **Available scene** (**2**): All the available scenes according to the parameters you selected. These scenes are ordered using the :code:`priority` parameter you set in the :guilabel:`SCN` tab.
-   **Selected scenes** (**3**): The scenes that are currently selected.

.. thumbnail:: ../_images/cookbook/optical_mosaic/select_scenes.png
    :title: The pop-up window used to select individual scenes for one single tile
    :group: optical-mosaic-recipe

Each thumbnail represents a scene of the tile stack. You have the option to include them in the mosaic. The scenes located on the left side are the **Available scenes**; the **Selected scenes** are on the right side. In both cases, the following information can be found on the thumbnail:

-   A small preview of the scene in the *red, green, blue* (true-colour) band combination.
-   The exact date in YYYY-MM-DD of the scene.
-   The satellite name :icon:`fa-solid fa-satellite-dish`.
-   The cloud coverage of the scene in percent and its position in the stack values :icon:`fa-solid fa-cloud`.
-   The distance from target day in days within the season and its position in the stack values :icon:`fa-solid fa-calendar-check`.

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_available.png
    :width: 24%
    :title: The thumbnail of a scene when it's in the available scene area
    :group: optical-mosaic-recipe

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_selected.png
    :width: 74%
    :title: The thumbnail of a scene when it's in the selected scene area
    :group: optical-mosaic-recipe

You can decide to move the scene to the **Selected scene** area by selecting :icon:`fa-solid fa-plus` :guilabel:`Add` or moving it back to the **Available scene** pane by selecting :icon:`fa-solid fa-minus` :guilabel:`Remove`.

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_available_hover.png
    :width: 24%
    :title: The thumbnail of a scene when it's in the **Available scene** area while hovering over it
    :group: optical-mosaic-recipe

.. thumbnail:: ../_images/cookbook/optical_mosaic/thumbnail_selected_hover.png
    :width: 74%
    :title: The thumbnail of a scene when it's in the **Selected scene** area while hovering over it
    :group: optical-mosaic-recipe

.. tip::

    Scenes are moved from one side to the other so they are not duplicated and cannot be selected twice. Be careful if your connection is slow; wait for the thumbnail to move before clicking again (if you click too fast, you could select two different images instead of one).

Once you are happy with your selection, select the :guilabel:`Apply` button to close the window and use the selected scenes to compute the mosaic on this tile. When the window is closed, SEPAL resets the rendering of all tiles.

Retrieve
^^^^^^^^

.. important::

    You cannot export a recipe as an asset or a :code:`.tif` file without a small computation quota. If you are a new user, see :doc:`../setup/resource`.

Selecting the :icon:`fa-solid fa-cloud-arrow-down` tab will open the **Retrieve** pane where you can select the exportation parameters.

.. thumbnail:: ../_images/cookbook/optical_mosaic/retrieve.png
    :title: The last pane of the optical mosaic: exportation
    :group: optical-mosaic-recipe

Bands
"""""

You need to select the band(s) to export with the mosaic. There is no maximum number of bands, but exporting useless bands will only increase the size and time of the output. To discover the full list of available bands with SEPAL, see :doc:`../feature/optical_bands`.

.. tip::

    There is no fixed rule to the band selection. Each index is more adapted to a set of analyses in a defined biome. The knowledge of the study area, the evolution expected and the careful selection of an adapted band combination will improve the quality of downstream analysis.

Dates
#####

-   :guilabel:`dayOfYear`: the Julian calendar date (day of the year)
-   :guilabel:`daysFromTarget`: the distance to the target date within the season in days

.. note::

    These metadata bands are only available when the :guilabel:`Medoid` composing method is used (the :guilabel:`Median` method produces artificial pixels that carry no metadata).

Scale
"""""

You can set a custom scale for exportation by selecting a value in metres (m) (note that requesting a smaller resolution than the images' native resolution will not improve the quality of the output – just its size – keep in mind that the native resolution of Sentinel data is 10 m, while Landsat is 30 m).

Destination
"""""""""""

Choose a single destination for the export:

-   :guilabel:`SEPAL workspace`: the image is written to your SEPAL files in :code:`.tif` format (by default in the :code:`Downloads` folder).
-   :guilabel:`Google Earth Engine asset`: the image is exported to your GEE account as an asset. You can export it either as a single :guilabel:`Image` or as an :guilabel:`Image collection` (tiled, which is better suited to large exports), and set its sharing to :guilabel:`Private` or :guilabel:`Public`.
-   :guilabel:`Google Drive`: the image is exported to the Google Drive of the connected Google account.

.. Note::

    The :guilabel:`Google Earth Engine asset` and :guilabel:`Google Drive` destinations are only displayed when a Google account is connected to SEPAL. If they are missing, please refer to `Connect SEPAL to GEE <../setup/gee.html>`__.

Select :guilabel:`Retrieve` to start the export process.

Exportation status
""""""""""""""""""

In the **Tasks** tab (lower-left corner using the :icon:`fa-solid fa-list-check` or :icon:`fa-solid fa-spinner` buttons, depending on the loading status), you will see the list of the different loading tasks. The interface will provide you with information about task progress and display an error if the exportation has failed.

If you are unsatisfied with the way we present information, the task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    This operation is running between GEE and SEPAL servers in the background. You can close the SEPAL page without stopping the process.

When the task is finished, the frame will be displayed in green, as shown on the second image below.

.. thumbnail:: ../_images/cookbook/time_series/download.png
    :width: 49%
    :title: Evolution of the download process of the recipe displayed in SEPAL's **Task manager**
    :group: time-series-recipe

.. thumbnail:: ../_images/cookbook/time_series/download_complete.png
    :width: 49%
    :title: Completed download process of the recipe displayed in SEPAL's **Task manager**
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

    Understanding how images are stored in an optical mosaic is only required if you want to manually use them. The SEPAL applications are bound to this tiling system and can digest the information for you.

The data are stored in a folder using the name of the optical mosaic as it was created in the first section of this article. As the number of data is spatially too big to be exported at once, the data are divided into smaller pieces and brought back together in a :code:`<MO name>_<gee tile id>.vrt` file.

.. tip::

    The full folder with a consistent tree folder is required to read the `.vrt`

.. important::

    Now that you have exported the optical mosaic to your SEPAL workspace, it can be downloaded to your computer using `file exchange options <../setup/filezilla.html>`__ or used in other SEPAL workflows.
