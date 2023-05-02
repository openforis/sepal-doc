FCDM
====

.. note::

    former Delta-rNBR, Version 2.4
    
FCDM Tool
---------

Overview 
^^^^^^^^

The FCDM tool supports the detection of forest canopy disturbance from satellite remote sensing and can provide indication on forest degradation processes. Reporting on forest degradation is required by many tropical countries participating in the REDD+ (Reducing Emissions from Deforestation and Degradation) program. 
However, compared to deforestation, the mapping of "forest degradation" has proven to be technically much more challenging and the signal of a forest canopy 
disturbance is less prominent, as it does not result in a change of land cover.

The FCDM tool has been developed at the Joint Research Centre (JRC) within the ReCaREDD Project and uses a change detection approach based on the difference (delta) of the self-referenced "Normalized Burn Ratio" index (Delta-rNBR; `Langner et al. 2018 <https://doi.org/10.3390/rs10040544>`__) to detect forest canopy change over defined periods at pixel and sub-pixel level. 
The underlying Delta-rNBR index allows the detection of forest canopy disturbance within tropical (semi-)evergreen forest canopies ("forest remaining forest"), 
resulting for instance from tree removal, felling damages or from logging trails and leading.

.. thumbnail:: https://forobs.jrc.ec.europa.eu/iforce/images/fcdm_process.jpg
    :title: Processing steps of the FCDM tool
    :group: fcdm

General Purpose 
^^^^^^^^^^^^^^^

- Detection of all kind of tree canopy disturbances (natural or human induced) within evergreen and semi-evergreen forests
- In order to separate natural from human disturbances we recommend manual screening of the data by an experienced human interpreter
- Close to real time monitoring of canopy cover changes possible

Citation
^^^^^^^^

Publications, models and data products that make use of this tool must include proper acknowledgement, including citing datasets and the journal article as in the 
following citation:

- `Langner A, Miettinen J, Kukkonen M, Vancutsem C, Simonetti D, Vieilledent G, Verhegghen A, Gallego J, Stibig H-J (2018). Towards Operational Monitoring of Forest Canopy Disturbance in Evergreen Rain Forests: A Test Case in Continental Southeast Asia. Remote Sensing. 10, 4, 544, `doi:10.3390/rs10040544 <https://doi.org/10.3390/rs10040544>`__

Contact 
^^^^^^^

> **Original algorithm**  
> Author:  Andreas Langner (SvBuF)  
> Email:  andi.langner@gmail.com, andreas-johannes.langner@ec.europa.eu  
  
> **sepal adaptation**  
> Author: Pierrick Rambaud (FAO)  
> Email: Pierrick.rambaud@fao.org


Usage
-----

Select AOI
^^^^^^^^^^

The *delta-rNBR* will be calculated based on the user inputs. The first mandatory input is the Area Of Interest (AOI). In this step you’ll have the possibility to choose from a predefined list of administrative layers or use your own datasets, the available options are:

**Predefined layers**

-   Country/province
-   Administrative level 1
-   Administrative level 2

**Custom layers**

-   Vector file
-   Drawn shapes on map
-   Google Earth Engine Asset

After selecting the desired area, click over the :code:`Select these inputs` button and the map shows up your selection.

.. note::

    You can only select one area of interest. In some cases, depending on the input data you could run out of resources in GEE.
    
.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/aoi_selector.png
    :title: AOI selection of the Sandan province in Cambodia
    :group: fcdm

Workflow parameters
^^^^^^^^^^^^^^^^^^^

Click on :guilabel:`process` to display the process panel. In this section we'll describe each parameter you can set in the app to customize your analysis.

Select Time periods
*******************

The selected time periods are the periods that will be used as **reference** and **analysis** period.
Simply click on the different :code:`datepicker` to select the start date end end date of this time periods. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/datepicker-demo.gif
    :title: demo of the datepicker usage
    :group: fcdm

.. note:: 

    As suggested in the article, the FCDM analysis performs better with time periods smaller or equal to a year. Longer periods tend to accumulate noise. As an example the following parameters are fitting: 
    -   reference period: :code:`2019-01-01 2019-12-31`
    -   analysis period: :code:`2020-01-01 2020-12-31`
    
.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/time_period.png 
    :title: Selection of 2 time periods covering the whole years of 2020 as analysis and 2019 as reference
    :group: fcdm
    

Sensors parameters
******************

Sensors
#######

.. warning::

    The sensor list is updated with the available satellites dataset for the selected time periods. User is thus forced to select the dates first. 
    
The sensors can be selected in the dropdown menu. This list is only showing the satellites datasets that are available for the selected time period. The user needs to select at least 1. 

.. note:: 

    Data from Sentinel and Landsat program cannot be mixed.
    
.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/sensor.png 
    :title: select the landsat famiy (L7 and L8) without thresholding L7 data
    :group: fcdm
    

Threshold for landsat 7
#######################

Value of the threshold applied on Landsat 7 data. This is a correction parameter to remove some of the effects of SLC issue. Default set to :code:`0.08`.

Cloud buffer
############

Value of the cloud buffering used in the cloud masking operation of the FCDM process in meters. Default set to :code:`500`. 

Basemap
*******

The FCDM process need to create a forest non-forest mask to produce the results. This mask is derivated from data provided by the user.
Three default datasets can be selected: 

-   Global forest cover: This mask will be based on the `global forest cover <https://earthenginepartners.appspot.com/science-2013-global-forest>`__ product from University of Maryland. The user will also need to provide the year to use and the treecover level to diferenciate forest from the rest.
    
    .. tip::

        The year is automatically set to the start year of the **reference** period.
    
-   TMF: This mask will be based on the `Tropical Moist Forest <https://forobs.jrc.ec.europa.eu/TMF/gee_tutorial/>`__ product from JRC. The user will also need to provide the year of analysis.
    
    .. tip::

        The year is automatically set to the start year of the **reference** period.
    
-   No forest map: there will be no forest masking

The user can also use any GEE asset by setting it's value in the :code:`textfield` or selecting an image in the raster list. The image needs to be a mask with values of the first band set to: 
-   0 for non-forest 
-   1 for forest



.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/basemap.png 
    :title: use the built-in GFC dataset to build a forest mask with a 70% of treecover and based on the 2019 version. 
    :group: fcdm

Advanced parameters
*******************

These parameters are advanced parameters of the FCDM process please read the article carefully to get a good understanding of their objectives. 

Self-referencing
################

For the self referencing kernel you simply need to set 1 single parameter: **Radius of circular kernel** that will define in meter the buffer used for the self-referencing operation. default set to: code:`150`.

DDR
###

.. note::

    Disturbance-Density-Realted (DDR) filtering

Here, 3 parameters need to be set: 

-   **Threshold for filtering**: The threshold of change magnitude that will be considered as intermediate disturbance result. Default to :code:`0.035`.
-   **Radius of circular kernel for filtering**: in meter, the radius of the buffer. Default to: code:`80`.
-   **Min number of intermediate disturbance events per cleaning kernel**: the threshold number of intermediate disturbance events within a kernel to consider the kernel center pixel to be kept or discarded (irrespective of pixel value). Default set to :code:`3`.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/advanced_params.png 
    :title: the default set of advanced parameters
    :group: fcdm
    
Compute
*******

Click on :guilabel:`Run FCDM Computation` to launch the process in GEE. The layers will automatically be displayed on the visualisation map.

.. warning::
    
    This operation takes no time as the actual computation is done when the map refreshes itself.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/run_fcdm.png 
    :title: the run panel
    :group: fcdm

Map
^^^

In this map, the different layers of the computation will be displayed:

-   the forest mask (in green) 
-   the delta-rNBR (red where there are disturbances)
-   the AOI (in light blue)

.. note::

    When the map is fully zoomed out, the disturbances are not visible because of GEE pyramiding policy. Zoom in 2 to 3 times to see the disturbances.

.. warning:: 

    Every time the user zoom in, GEE will recompute all the values on the fly. This opreation is time consuming so be patient. The forest mask is a simple image, when the delta-rNBR finishes its refresh, it's perfectly aligned with it. As long as it's blurry, it means that GEE is still computing.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/result_map.png 
    :title: vizualization of the SANDAN province with all the default parameters with reference period of 2019 and analysis 2020
    :group: fcdm
    
    
Download images
^^^^^^^^^^^^^^^

Click on the cloud in the top left corner of the map, it will open the following popup where the user will be able to customize exportation parameters.  

.. thumbnail:: https://raw.githubusercontent.com/12rambau/fcdm/master/doc/img/export_panel.png 
    :title: the downloading popup
    :width: 50%
    :align: center
    :group: fcdm
    
-   **filename prefix**: the prefix that will be used to described the file in SEPAL or the asset in GEE. Default to :code:`<aoi_anme>_<referenced perdiod year>_<analysis_period_year``. It can be customize in anything but every non UTF8 character will automatically be changed in "_".
-   **select dataset**: the user can export any of the following datasets: :code:`Delta-rNBR`, :code:`Delta-rNBR wihthout DDR`, :code:`anaysis rNBR`, :code:`reference rNBR` and :code:`forest mask`. default to only :code:`Delta-rNBR`.
-   **scale**: The user can select any exportation scale from 10m to 300m.
-   **select export method**: as a SEPAL file or as a GEE asset
    
    .. warning::
    
        if you select :code:`as a SEPAL file`, then the application cannot be closed before the end of the exportation. 
        On the other hand GEE export can be monitored from the GEE task manager.
        
Click :guilabel:`Apply` to start the exportation process. 
    

    



.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/fcdm/release/doc/en.rst
