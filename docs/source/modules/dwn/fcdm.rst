Forest Canopy Disturbance Monitoring (FCDM)
===========================================

.. note::

    Former Delta-rNBR, Version 2.4

FCDM Tool
---------

Overview 
^^^^^^^^

The FCDM tool supports the detection of forest canopy disturbance from remote sensing satellites, providing indications of forest degradation processes. Reporting on forest degradation is required by many tropical countries participating in the programme, Reducing Emissions from Deforestation and Forest Degradation and the role of conservation, sustainable management of forests and enhancement of forest carbon stocks in developing countries (REDD+). However, compared to deforestation, the mapping of forest degradation has proven to be technically much more challenging. In particular, signs of a forest canopy disturbance is less prominent, as it does not result in a change of land cover.

The FCDM tool has been developed at the Joint Research Centre (JRC) within the ReCaREDD Project. It uses a change detection approach based on the difference (delta) of the self-referenced "Normalized Burn Ratio" index (Delta-rNBR) (`Langner et al. [2018] <https://doi.org/10.3390/rs10040544>`__), in order to detect forest canopy change over defined periods at the pixel and sub-pixel level. The underlying Delta-rNBR index allows the detection of forest canopy disturbance within tropical (semi-)evergreen forest canopies ("forest remaining forest"), resulting from certain actions, such as tree removal, felling damages, logging trails, and leading.

.. thumbnail:: https://forobs.jrc.ec.europa.eu/iforce/images/fcdm_process.jpg
    :title: Processing steps of the FCDM tool
    :group: fcdm

General purpose
^^^^^^^^^^^^^^^

- detection of all kind of tree canopy disturbances (natural or human-induced) within evergreen and semi-evergreen forests
- manual screening of the data by an experienced human interpreter, in order to separate natural disturbances from human disturbances
- close to real-time monitoring of possible canopy cover changes

Citation
^^^^^^^^

Publications, models and data products that make use of this tool must include proper acknowledgement, including citing datasets and presenting the following reference for the source:

- Langner, A., Miettinen, J., Kukkonen, M., Vancutsem, C., Simonetti, D., Vieilledent, G., Verhegghen, A., Gallego, J. & Stibig, H-J. 2018. Towards Operational Monitoring of Forest Canopy Disturbance in Evergreen Rain Forests: A Test Case in Continental Southeast Asia. *Remote Sensing* (10, 4): 544. https://doi.org/10.3390/rs10040544

Contact
^^^^^^^

> **Original algorithm**  
> Author: Andreas Langner (SvBuF)  
> Email: andi.langner@gmail.com, andreas-johannes.langner@ec.europa.eu

> **SEPAL adaptation**  
> Author: Pierrick Rambaud (FAO)  
> Email: Pierrick.rambaud@fao.org

Usage
-----

Select AOI
^^^^^^^^^^

The *delta-rNBR* will be calculated based on user inputs. The first mandatory input is the area of interest (AOI). In this step you’ll have the possibility to choose from a predefined list of administrative layers or use your own datasets. The available options are:

**Pre-defined layers**

-   Country/province
-   Administrative level 1
-   Administrative level 2

**Custom layers**

-   Vector file
-   Drawn shapes on map
-   Google Earth Engine (GEE) asset

After choosing the desired area, select the :code:`Select these inputs` button; the map will show your selection.

.. note::

    You can only select one AOI. In some cases, depending on the input data, you could run out of resources in GEE.
    
.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/aoi_selector.png
    :title: AOI selection of the Sandan province in Cambodia
    :group: fcdm

Workflow parameters
^^^^^^^^^^^^^^^^^^^

Select :guilabel:`process` to display the process panel. In this section, we'll describe each parameter you can set in the app to customize your analysis.

Select time periods
*******************

Selected time periods are the periods that will be used as **reference** and **analysis** periods.

Use the :code:`datepicker` to select the start date and end date of these time periods.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/datepicker-demo.gif
    :title: demo of the datepicker usage
    :group: fcdm

.. note::

    As suggested in the article, FCDM analysis performs better with time periods smaller or equal to a year. Longer periods tend to accumulate noise. As an example, the following parameters are fitting: 
    -   reference period: :code:`2019-01-01 2019-12-31`
    -   analysis period: :code:`2020-01-01 2020-12-31`
    
.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/time_period.png 
    :title: Selection of two time periods covering the entire year of 2020 as analysis and 2019 as reference
    :group: fcdm    

Sensors parameters
******************

Sensors
#######

.. attention::

    The sensor list is updated with the available satellite dataset for the selected time periods. The user is thus forced to select the dates first.

The sensors can be selected in the dropdown menu. This list is only showing the satellite datasets that are available for the selected time period. The user needs to select at least one.

.. note::

    Data from Sentinel and Landsat programme cannot be mixed.
    
.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/sensor.png 
    :title: Select the Landsat family (L7 and L8) without thresholding L7 data
    :group: fcdm

Threshold for Landsat 7
#######################

Value of the threshold applied on Landsat 7 data. This is a correction parameter to remove some of the effects of SLC issues (by default, set to :code:`0.08`).

Cloud buffer
############

Value of the cloud buffering used in the cloud masking operation of the FCDM process (in meters; by default, set to :code:`500`).

Basemap
*******

The FCDM process needs to create a forest/non-forest mask to produce results, which is derived from data provided by the user. 

Three default datasets can be selected: 

-   Global forest cover: This mask will be based on the `global forest cover <https://earthenginepartners.appspot.com/science-2013-global-forest>`__ product from University of Maryland. The user will also need to provide the year to use and the tree cover level to differentiate forest from the rest.

    .. tip::

        The year is automatically set to the start year of the **reference** period.
    
-   TMF: This mask will be based on the `Tropical Moist Forest <https://forobs.jrc.ec.europa.eu/TMF/gee_tutorial/>`__ product from the JRC. The user will also need to provide the year of analysis.

    .. tip::

        The year is automatically set to the start year of the **reference** period.
    
-   No forest map: There will be no forest masking.

The user can also use any GEE asset by setting it's value in the :code:`textfield` or selecting an image in the raster list. The image needs to be a mask with values of the first band set to: 

-   0 for non-forest
-   1 for forest

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/basemap.png 
    :title: Use the built-in GFC dataset to build a forest mask with 70% tree cover, based on the 2019 version.
    :group: fcdm

Advanced parameters
*******************

These are the advanced parameters of the FCDM process. Please read this section carefully understand their objectives.

Self referencing
################

For the self-referencing kernel, set one parameter, **Radius of circular kernel**, which will define the buffer used for the self-referencing operation (in meters; by default, set to: code:`150`).

DDR
###

.. note::

    Disturbance-Density-Realted (DDR) filtering

Three parameters need to be set:

-   **Threshold for filtering**: The threshold of change magnitude that will be considered as intermediate disturbance results (by default, :code:`0.035`).
-   **Radius of circular kernel for filtering**: The radius of the buffer (in meters; by default, to: code:`80`).
-   **Min number of intermediate disturbance events per cleaning kernel**: the threshold number of intermediate disturbance events within a kernel to consider the kernel center pixel to be kept or discarded (irrespective of pixel value; by default, set to :code:`3`).

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/advanced_params.png 
    :title: The default set of advanced parameters
    :group: fcdm
    
Compute
*******

Select :guilabel:`Run FCDM Computation` to launch the process in GEE. The layers will automatically be displayed on the visualization map.

.. attention::

    This operation takes very little time since the actual computation is done when the map refreshes itself.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/run_fcdm.png 
    :title: The run panel
    :group: fcdm

Map
^^^

In this map, different layers of the computation will be displayed:

-   the forest mask (in green)
-   the delta-rNBR (in red, where there are disturbances)
-   the AOI (in light blue)

.. note::

    When the map is fully zoomed out, the disturbances are not visible because of the GEE pyramiding policy. Zoom in two to three times to see the disturbances.

.. attention::

    Every time the user zooms in, GEE will recompute all the values on the fly. This opreation is time consuming, so be patient. The forest mask is a simple image; when the delta-rNBR finishes refreshing, it will be perfectly aligned with the image. If it's blurry, GEE is still computing.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/result_map.png 
    :title: Vizualization of the Sandan province with all default parameters with the reference period of 2019 and 2020 analysis
    :group: fcdm

Download images
^^^^^^^^^^^^^^^

Select the cloud in the upper-left corner of the map to open the following pop-up window, where you will be able to customize exportation parameters.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/export_panel.png 
    :title: The downloading pop-up window
    :width: 50%
    :align: center
    :group: fcdm
    
-   **filename prefix**: The prefix used to describe the file (in SEPAL) or the asset (in GEE) (by default, :code:`<aoi_anme>_<referenced perdiod year>_<analysis_period_year`); it can be customized to anything, but every non-UTF8 character will automatically be changed in "_".
-   **select dataset**: The user can export any of the following datasets: :code:`Delta-rNBR`, :code:`Delta-rNBR wihthout DDR`, :code:`anaysis rNBR`, :code:`reference rNBR`, and :code:`forest mask` (by default, :code:`Delta-rNBR`).
-   **scale**: The user can select any exportation scale (from 10 m to 300 m).
-   **select export method**: as a SEPAL file or GEE asset

    .. attention::
    
        If you select :code:`as a SEPAL file`, the application cannot be closed before the end of the exportation. 
        If you choose to export to GEE, the process can be monitored from the GEE task manager.

Select :guilabel:`Apply` to start the exportation process.

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/fcdm/release/doc/en.rst
