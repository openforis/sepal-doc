CCDC Slice
==========

Background
------------

Powered by the API of Google's `Earth Engine <https://earthengine.google.com/>`_, SEPAL facilitates the workflow for applying the Continuous Change Detection and Classification (CCDC) approach as proposed by `Zhu & Woodcock 2014 <https://www.sciencedirect.com/science/article/pii/S0034425714000248>`_.

CCDC is a holistic methodological framework that encompasses various aspects of space-borne, multi-temporal land mapping and monitoring using multi-temporal satellite imagery. The core of the method is a **temporal segmentation** algorithm applied at **pixel-level**.

Before creating a CCDC slice, a CCDC asset needs to be created (as described in :doc:`ccdc`). The asset holds all parameters that are needed to re-produce the modelled time-series of the underlying data. As those parameters are stored at pixel-level we retain the possibility to extract each pixel's modelled reflectance at any given point in time, or for a time-span of the underlying time-series. This is what is meant by **slicing**.

In addition, we can access the parameters describing the model of the temporally intersecting segment. Those can be used in as input features for subsequent classification tasks and generally improve class separability.

Getting Started
---------------

Create Recipe
^^^^^^^^^^^^^^

Once logged into SEPAL, open the recipe menu by clicking on the orange :btn:`<fa fa-globe>` button at the top left of the SEPAL start screen. Within the recipe menu (*see figure below*), select CCDC slice, which opens a new SEPAL recipe tab.

.. thumbnail:: ../_images/cookbook/ccdc_slice/recipe_selection.png
    :group: recipe-ccdc-slice
    :title: Selection menu for SEPAL recipes
    :width: 60%
    :align: center

Rename Recipe
^^^^^^^^^^^^^

The first step one should do is to change the name of the recipe by double-clicking on tab on the top of the map. This will have the effect that your recipe will be automatically saved and is visible in the list of created recipes. Furthermore, the given name will be used for exported files, both locally and on Earth Engine. We suggest to use the following convention: :code:`CCDC-slice_<aoi>_<sensor(s)>_<date>`.

.. thumbnail:: ../_images/cookbook/ccdc_slice/recipe_unnamed.png
    :title: CCDC asset default title
    :width: 40%

.. thumbnail:: ../_images/cookbook/ccdc_slice/recipe_renamed.png
    :title: CCDC assed modified title
    :width: 40%

Parameter selection
-------------------

The following steps describe the parameter selection that can be found on the lower right of the screen.

.. thumbnail:: ../_images/cookbook/ccdc_slice/ccdc_slice_start_screen.png
    :group: recipe-ccdc-slice
    :title: CCDC slice parameters

.. line-break::

The buttons open the following dialogues:

-   :guilabel:`SRC` Selection of CCDC asset source
-   :guilabel:`DAT` Date or date range selection
-   :guilabel:`OPT` CCDC Slicing Parameters


Selection of CCDC asset source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CCDC slices are created out of CCDC assets. Here you have the choice to select the base asset that will be used to generate the slice.

Two options are provided, one is to directly point to an existing Sepal recipe. Note that in this case, the CCDC asset needs to be re-generated on the fly based on the parameter settings of the CCDC asset. In most cases this is very compute intense and may lead to time-out errors.

Therefore it is rather recommended to opt for option 2, where an existing CCDC asset is selected from Earth Engine. In this case, the CCDC asset needs to be exported first, so that we can then point to its asset location within Earth Engine directly. This usually allows for instant visualization as the slicing procedure does not require lots of computing power.


Date (Range) selection
^^^^^^^^^^^^^^^^^^^^^^

As described above, the slicing procedure cuts out the model parameters of a specific date in order to generate the expected reflectance at that given point in time. This can be either a concrete date :btn:`single date`, or a date range :btn:`date range`. For the latter, the median value of the selected time period over the modelled time-series is calculated.

In addition, it is possible to display the detected breaks for the intersecting temporal segments. Note that for date ranges, more than 1 break can fall within the specific time-period. This needs to be considered in the next parameter setting, the CCDC slicing parameters.

.. thumbnail:: ../_images/cookbook/ccdc_slice/date_selection.png
    :group: recipe-ccdc-slice
    :title: date selection parameter

CCDC Slicing Parameters
^^^^^^^^^^^^^^^^^^^^^^^

Specific Date
"""""""""""""

In case a single date has been selected, the slicing parameters will look as shown in the Figure below.

.. thumbnail:: ../_images/cookbook/ccdc_slice/ccdc_slice_date_parameters.png
    :group: recipe-ccdc-slice
    :title: Selection menu for CCDC slice parameters
    :align: center

The first parameter is the number of **harmonics** used to extract the modelled reflectance at the given point in time. 3 harmonic terms are set by default. lowering this number will result in a smoothed time-series that does not depict intra-annual periodicity. Setting this value to 1 will only capture the inter-annual periodicity, i.e. annual seasonality, while a value of 0 results in the mean value over the segments time period.

The **Gap Strategy** relates to the presence of gaps between 2 temporal segments, i.e. the presence of a break. After a detected break, CCDC re-initializes a new model (i.e. new segment) only after a couple of observations. In between, no model is available from which to extract the data. In order to avoid masked pixels the user has the possibility to:

-   :btn:`Interpolate` - use a temporally weighted mean between the previous and the subsequent model for the given data
-   :btn:`Extrapolate` - use the extrapolated value of the closest, previous, or next model for the given date
-   :btn:`Mask` - mask the value as no data

In case of extrapolation the additional option **Segment to Extrapolate** allows to choose either the model parameters from the previous, next or closest segment with respect to the selected data. Furthermore, the **Max Days to Extrapolate** setting allows to limit the number of days until this procedure is considered valid. If the difference between the selected date and the segment's valid time period is greater than this threshold value, the pixel will be automatically masked.

Date Range
""""""""""

In case a date range has been selected, the slicing parameters will look as shown in the Figure below.

.. thumbnail:: ../_images/cookbook/ccdc_slice/ccdc_slice_date_range_parameters.png
    :group: recipe-ccdc-slice
    :title: Selection menu for CCDC slice parameters - date range
    :align: center

The first parameter is the number of **harmonics** used to extract the modelled reflectance at the given point in time. 3 harmonic terms are set by default. lowering this number will result in a smoothed time-series that does not depict intra-annual periodicity. Setting this value to 1 will only capture the inter-annual periodicity, i.e. annual seasonality, while a value of 0 results in the mean value over the segments time period.

Then you need to select the **Break analysis band**. As the slice is including a range of observation, the model can include multiple segments and thus multiple breaks. this parameter will select the band used by SEPAL to select the break that will be kept in the slice output.

Breaks identified by the CCDC asset at the end of the time period are usually errors. if your slicing is ending at the same date as your CCDC asset, you should consider masking the end break. 

SEPAL offers 4 ways of selecting the remaining break:

- :guilabel:`first`: the first break within the slice date range
- :guilabel:`last`: the last break within the slice date range
- :guilabel:`magnitude`: the break with the highest magnitude of change 
- :guilabel:`confidence`: the break with the highest confidence value (see :doc:`ccdc` for mor information about confidence computation)

By selecting a specific breack direction, the break sekection will only take into acount the break with a :guilabel:`decrease` or :guilabel:`increase` magnitude. By default we consider :guilabel:`any` break direction.

By moving the slider, you will ignore the break with a low confidence from the anlysis. You can exclude break up to 50%. If no break respects the requested confidence, the highest available will be selected.

Visualization
-------------

Click on the :btn:`<fa fa-chart-area>` button to start the plotting tool (1). Move the pointer to the main map, the pointer will be transformed into a :icon:`fa fa-plus`. Click anywhere in the AOI to plot data for this specific location in the following popup window.

The plotting area (3) is the same as the one presented in the CCDC recipe with small adjustment to the slicing operation. Refer to :ref:`ccdc_pixel_analys` for a complete description.

The plotting area cover all the CCDC asset range, in red (4) the user will see the slice. It will be a sector of the plot if date range is selected and a red line if single date is selected.

.. thumbnail:: ../_images/cookbook/ccdc_slice/pixel_analysis.png
    :title: Pixel Analysis of a date range slice of a CCDC asset
    :group: recipe-ccdc-slice

.. warning::

    The plot feature is retrieving information from GEE on the fly and serving it in an interactive window. This operation can take time depending on the number of available observations and the complexity of the selected pre-processing parameters. If the popup window displays a spinning wheel, wait up to 2 min to see the data displayed.

Export
------

Trigger the export task
^^^^^^^^^^^^^^^^^^^^^^

Click on the :btn:`<fas fa-cloud-download-alt>` button to open the export dialogue. Here you can select the bands to retrieve and the scale at which you would like to save the slice. CCDC slices can be both exported to Google Earth Engine as well as your SEPAL workspace.

Bands
Band type

Segment bands


Exportation status
^^^^^^^^^^^^^^^^^^



