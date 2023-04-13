Direct Drivers Assessment
=========================

.. note::

    This documentation have been produced in the framework of the CAFI project, thus the CAFI area is used as an example but this methodology is not limited to the central African region and any other area can be used instead.

Creating cloud-free mosaics
---------------------------

To accurately determine disturbances within forest ecosystems and distinguish from other dynamics occurring in non-forest areas, a baseline forest mask is required. This is achieved by classifying cloud-free image mosaics, which are created using the optical and radar mosaic recipes.

As you can see in this `online animation <https://drive.google.com/file/d/1H5Br82CoE1QJnri0cBl1Pf2tRJV3kW96/view>`__, clouds are persistent in the Congo Basin region. For this reason we will produce mosaics of optical cloud-free imagery, and radar (cloud independent) composites for the best observations of the study region.

Optical cloud-free composite
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multi-temporal image mosaics are compiled from data collected over several months or years. Cloud-free pixels from multiple images are integrated into an image with fewer clouds, haze and shadows using the pixel quality band provided with image metadata.

We evaluated the availability of Landsat 4,5,7 and 8 images for the creation of optical mosaics for the baseline year or 2015. As you can see from the figure below, only certain sensors are available for certain time periods – from 2003 onwards the Landsat 7 sensor experienced a malfunction which results in data gaps in strips. This sensor should be only included when necessary, i.e. when not enough imagery is available. Luckily in SEPAL the selection of sensors is automatic based on the selected date and only provides the available options.

.. thumbnail:: ../_images/workflows/drivers/sensor_coverage.png
    :title: sensor time coverage
    :align: center
    :group: workflows-drivers


The coverage of Landsat over time is shown below. The western part of the study region along the coast, results in cloudy or data gaps in Gabon, Equatorial Guinea and Cameroon.

.. thumbnail:: ../_images/workflows/drivers/cafi_coverage.png
    :title: global coverage over the CAFI area
    :align: center
    :group: workflows-drivers

To create our optical mosaic, we will use the SEPAL optical mosaic recipe. To know more about the different available parameters please read :doc:`../cookbook/optical_mosaic`.

Within the recipe, select an AOI. In this example we will use and custom asset from GEE: :code:`projects/cafi_fao_congo/aoi/cafi_countries_buffer_simple`. It includes an ISO column to select countries. See :doc:`../feature/aoi_selector` for more AOI selection methods.

In the :btn:`DAT` section you can select the dates of interest.

For later years (after 2018), the sensor coverage is good so you can safely select all images of a single year.

For earlier eras, e.g. 2015 use the advance option to add images from prior years on a targeted season (in this case the full year). This will help to fill the gaps in cloudy areas.

.. thumbnail:: ../_images/workflows/drivers/season_selection.png
    :title: Select images from 3 year prior on the targeted season (full year) to improve the quality of the mosaic.
    :align: center
    :group: workflows-drivers


For data sources, more is generally better. Select all Landsat options for a consistent mosaic. If you like, Sentinel-2 can be added for more data but as the tiling system of the 2 agencies are different you will be force to use all available images.

If you are only working with Landsat (or only with Sentinel), you can manually select scenes if you want to tailor your mosaic and you have a lot of time to devote. :btn:`USE ALL SCENES` is the quicker and simpler approach.

For the composite options we recommend :btn:`SR` and :btn:`BRDF`, you can exclude pixels with low NDVI (particularly if you have a long time period) and select the options as shown in the following figures.

.. thumbnail:: ../_images/workflows/drivers/aoi_selection.png
    :title: Select a custom AOI from a EE Table
    :group: workflows-drivers
    :width: 24%

.. thumbnail:: ../_images/workflows/drivers/source.png
    :title: Select the Landsat sources for a mosaic.
    :group: workflows-drivers
    :width: 24%

.. thumbnail:: ../_images/workflows/drivers/scenes.png
    :title: Use all the available images to build the mosaic.
    :group: workflows-drivers
    :width: 24%

.. thumbnail:: ../_images/workflows/drivers/composite.png
    :title: The suggested set of compositing options.
    :group: workflows-drivers
    :width: 24%

You can then retrieve the mosaic as a Google asset at 30m resolution. We select the original bands as all other indices can be recalculated later: :btn:`BLUE`, :btn:`GREEN`, :btn:`RED`, :btn:`NIR`, :btn:`SWIR1`, :btn:`SWIR2`, :btn:`THERMAL`

Once the exportation is finished, you can view the asset in Google Earth Engine. Here is an example using all of the above parameters:

.. thumbnail:: ../_images/workflows/drivers/final_mosaic.png
    :title: The produced mosaic on the CAFI region for the year 2015 (using images from 2012 onward).
    :align: center
    :group: workflows-drivers

ALOS Palsar mosaics
^^^^^^^^^^^^^^^^^^^

Radar imagery has the added benefit of being cloud-free by design as the active sensors is not influenced by the clouds.

Alos Palsar is a L-band radar that gives good results for monitoring forestry. Data is provided by the Kyoto & Carbon Initiative from the Japanese Space Agency (JAXA) for the year 2015 onward. SEPAL is providing an application to select and download them to your user space.

For more information about the parameters, Please see :doc:`../module/dwn/alos_mosaic`.


Sentinel-1 mosaics
^^^^^^^^^^^^^^^^^^

You can use the Sentinel-1 recipe to create a mosaic from ESA Copernicus radar data.

The aoi selection is the same as for the optical mosaic.
For the dates you can enter a year, a date range, or a single date. When you add a year or date range, SEPAL will provide a “time-scan” composite which includes bands which are statistical metrics of the range of data including phase and amplitude which assess the phenology and variations within the time period.

For the options the following are proposed:

-   Both ascending and descending will ensure complete coverage of the AOI
-   The terrain correction will mask any errors due to topography, or terrain “shadows”
-   We don’t need to apply a speckle filter
-   Moderate outlier removal will provide the most consistent results

Select which bands to export in the retrieve window




