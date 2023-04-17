Direct Drivers Assessment
=========================

.. note::

    This documentation has been produced in the framework of the Global CAFI Deforestation and Degradation Drivers project, which is a global methodology developed and piloted in the Central African region. The Congo Basin  area is used as an example but this methodology can be applied to any other geographic area.

Background
----------

Deforestation and forest degradation (DD) are complex processes that have many underlying causes. A comprehensive understanding of forest conversion to other land uses is instrumental for the development of policies and actions aiming to reduce the loss of forests and its associated carbon emission. It is important to understand recurring patterns and correlations that can help countries tailor their efforts towards reducing forest loss. The causes of deforestation and forest degradation vary both regionally and temporally (Curtis et al., 2018).  Different studies refer to agricultural expansion (cropland and pasture) as the largest direct cause of global deforestation (FAO, 2022; Gibbs et al., 2010; Hosonuma et al., 2012; Kissinger et al., 2012; Sandker et al., 2017). Commercial agriculture is estimated to be responsible for around 70-90% of the worldwide deforestation, while in Africa, both commercial and subsistence agriculture may account for similar importance in terms of forest loss, while fuel wood collection, charcoal production, and, to a lesser extent, livestock grazing in forests are the most important drivers of degradation.

However, these studies (as well as existing national studies on the drivers of deforestation and forest degradation in the Central African region) are generally based on data acquired up to 2014 and do not consider the recent trends in observed tree cover loss. They also do not take into account the importance of the spatial fragmentation of forests and the role played by degradation induced by forest exploitation (Molinario et al., 2015). Furthermore, they simplify causes of deforestation into a single driver, which does not adequately reflect the complex local context and interacting causes, decisions that lead to anthropogenic forest disturbance at local scales (Ferrer Velasco et al., 2020).

These recent trends and the lack of updated studies result in little consensus on the main drivers and agents of forest change at regional scales. There is a pressing need to systematically quantify the direct causes of deforestation and degradation via a systematic and comprehensive approach. An updated assessment should provide validated evidence on the role and weight of different drivers of forest loss and support decision making to address related challenges. A spatially explicit approach should also facilitate the assessment of the efficiency of policies and actions in different contexts. Improved spatial data on deforestation and forest degradation, and an improved understanding of the drivers will support land use planning approaches in two pilot areas where the regional analysis indicated clear opportunity for supporting land use decision making and planning.

In this context, FAO has developed a robust methodology to assess the recent trends and drivers of deforestation and forest degradation via collaborative approaches in which national experts, research institutes and civil society work together and join resources and data to reach a common view on the current and future causes and drivers of anthropogenic forest disturbances. These tools generate improved information for decision making and land use planning in the relevant management context.

The FAO, in partnership with the Central African Forest Initiative (CAFI), and a coalition of donor and partner countries have developed a global, standard, large-scale methodology to assess forest dynamics using cloud-computing solutions and open-source tools. The approach maps disturbances (both deforestation and degradation) and quantifies the contribution of multiple associated direct drivers. The methodology is used to assess deforestation and forest degradation trends and their associated current and historical direct drivers in six Central Africa countries as part of an international effort to mitigate climate change, support sustainable development goals, and protect biodiversity. The project builds on a collaborative approach, in which national experts, global research institutes and civil society work together, join resources and data to provide technical evidence and reach a common view on the current and historical trends, and direct drivers of forest disturbances.

Methodology
-----------

The major components of this this methodology include the generation of wall-to-wall geospatial data on forest cover types, changes, and discerning areas of deforestation from degradation for the entire Central African region. Next, these products are validated via visual interpretation and the presence of various direct drivers are identified to evaluate the direct causes of disturbance, and interpreted in the context of strategic investments for climate change mitigation and support for national efforts for emissions reduction.

The methodology uses FAO’s OpenForis suite of tools including the SEPAL platform for satellite data analysis, Collect Earth Online and Google Earth Engine. The approach analyses dense satellite time-series to generate geospatial data on forest changes which are then validated and interpreted for direct drivers in 5 major steps:

#. :ref:`workflows:drivers:mosaic`: processing of optical (Landsat 4/5/7/8) and radar (Sentinel 1/ALOS PALSAR) satellite images to create mosaics for the classification of wall-to-wall maps of vegetation types, recoded to a binary forest mask (following national forest definitions), and forest fragmentation assessment for the baseline year 2015

#. :ref:`workflows:drivers:series`: processing of optical satellite (Landsat 4/5/7/8) time series data covering 2012-2020 (2012-2015 is the historical time period, monitoring is from 2016-2020), using seasonal models and break detection algorithms to produce a forest change map for 2015-2020 at regional scale identifying areas of both deforestation and degradation.

#. :ref:`workflows:drivers:stratification`: Stratified random sampling is conducted on the change map from step 2. Systematic validation for all points identified as change, plus a sample of stable points is conducted in Collect Earth Online, evaluating land cover types, changes and dates of change and the identification of the presence of direct drivers.

#. :ref:`workflows:drivers:quantification`: The quantification of direct drivers by forest types, fragmentation class

.. _workflows:drivers:mosaic:

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

To create our optical mosaic, we will use the SEPAL optical mosaic recipe. To learn more about the different available parameters and how to use the recipe, please see :doc:`../cookbook/optical_mosaic`.

In this example we will use a  custom asset from GEE for the :btn:`AOI` parameter: :code:`projects/cafi_fao_congo/aoi/cafi_countries_buffer_simple`. It includes an ISO column to select Congo Basin countries according to their three digit code. See :doc:`../feature/aoi_selector` for more AOI selection methods.

In the :btn:`DAT` section you can select the dates of interest.

For later years (after 2018), the sensor coverage is good so you can safely select all images of a single year.

For earlier eras, e.g. 2015 use the advanced option to add images from prior years from a targeted season (in this case the full year). This will help to fill the gaps in cloudy areas.

.. thumbnail:: ../_images/workflows/drivers/season_selection.png
    :title: For the 2015, we will need to select images from 3 year prior on the targeted season (full year) to improve the quality of the mosaic and produce a nearly cloud-free result.
    :align: center
    :group: workflows-drivers


For data sources, more is generally better. Select all Landsat options for a consistent mosaic. If you like, Sentinel-2 can be added for more data, but as the tiling system of the 2 sensors are different you will be forced to use all available images - the option to select images will not be available.

If you are only working with Landsat (or only with Sentinel), you can manually select scenes if you want to tailor your mosaic and you have a lot of time to devote to your mosaic. :btn:`USE ALL SCENES` is the quicker and simpler approach and recommended for large areas.

For the composite options we recommend :btn:`SR` and :btn:`BRDF`, you can exclude pixels with low NDVI (particularly if you have a long time period) and select the following options:

    :group: workflows-drivers
    :width: 24%


You can then retrieve the mosaic as a Google asset at 30m resolution. We select the original bands as all other indices can be recalculated later: :btn:`BLUE`, :btn:`GREEN`, :btn:`RED`, :btn:`NIR`, :btn:`SWIR1`, :btn:`SWIR2`, :btn:`THERMAL`

Once the export is finished, you can view the asset in Google Earth Engine or SEPAL. Here is the 2015 mosaic of the Congo Basin using the above parameters:

.. thumbnail:: ../_images/workflows/drivers/final_mosaic.png
    :title: The produced mosaic on the CAFI region for the year 2015 (using images from 2012 onward).
    :align: center
    :group: workflows-drivers

ALOS Palsar mosaics
^^^^^^^^^^^^^^^^^^^

Radar imagery has the added benefit of being cloud-free by design as active sensors are not influenced by clouds.

Alos Palsar is a L-band radar that gives good results for monitoring forest ecosystems. Data is provided by the Kyoto & Carbon Initiative from the Japanese Space Agency (JAXA) for the year 2015 onward. SEPAL provides an application to select, process and download them to your user space pr Google Earth Engine Account.

For more information about the parameters, Please see :doc:`../modules/dwn/alos_mosaics`.


Sentinel-1 mosaics
^^^^^^^^^^^^^^^^^^

You can use the Sentinel-1 recipe to create a mosaic from ESA Copernicus radar data.

The aoi selection is the same as for the optical mosaic.
For the dates you can enter a year, a date range, or a single date. When you add a year or date range, SEPAL will provide a “time-scan” composite which includes bands which are statistical metrics of the range of data including phase and amplitude which assess the phenology and variations within the time period.

For the best results in the Congo Basin the following parameters are proposed:

-   Both :btn:`ascending` and :btn:`descending` orbits will ensure complete coverage of the AOI
-   The :btn:`terrain` correction will mask any errors due to topography, or terrain “shadows”
-   We don’t need to apply a speckle filter
-   :btn:`moderate` outlier removal will provide the most consistent results

Select which bands to export in the retrieve window, you may select all of them depending on the space available in your GEE repository or SEPAL workspace.
Resolution can also be selected accordingly - you can choose :btn:`30` to be at the same scale as the optical mosaic, which will be classified in the next step.

.. _workflows:drivers:series:

Time-series analysis
--------------------

.. warning::

    This part of the documentation is still under construction.

.. _workflows:drivers:stratification:

Sample Stratification
---------------------

.. warning::

    This part of the documentation is still under construction.

.. _workflows:drivers:quantification:

Quantify Direct Drivers
-----------------------

.. warning::

    This part of the documentation is still under construction.




