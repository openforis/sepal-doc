SDG 15.3.1
==========

The amount of degraded land relative to the total amount of land is measured by SDG Indicator 15.3.1. Target 15.3 of SDG 15 promotes "Life on Land" and reads as follows: Combat desertification by 2030, restore degraded land and soil, including those damaged by droughts, floods, and desertification, and work towards a world free of land degradation. To help achieve Target 15.3 of the Sustainable Development Goals, governments, international organisations, and civil society must take action to combat desertification and restore degraded land. Sustainable land management can be a significant measure that has a positive impact on degraded land. By taking such actions, we can ensure the preservation of biodiversity, promote sustainable land use, and create a sustainable future for generations to come. These actions can help improve the health of the environment and boost agricultural production in these areas, which will in turn ensure food security, reduce poverty, and promote social welfare.

This module allows generating data for reporting on SDG indicator 15.3.1. The SEPAL SDG indicator module follows UNCCD `good practice guidance version 2 <https://www.unccd.int/sites/default/files/documents/2021-09/UNCCD_GPG_SDG-Indicator-15.3.1_version2_2021.pdf>`__. 

The methodology for SDG 15.3.1 module for GPG v1 (`good practice guidance from UNCCD on SDG 15.3.1 <https://prais.unccd.int/sites/default/files/helper_documents/4-GPG_15.3.1_EN.pdf>`__) was implemented in consultation with the `trends.earth <https://trends.earth/docs/en/index.html>`__ team and `Conservation International <https://www.conservation.org>`__.

Methodology
-----------

What is Land degradation?
^^^^^^^^^^^^^^^^^^^^^^^^^
The United Nations Convention to Combat Desertification (UNCCD) defines land degradation as "\ *the reduction or loss of the biological or economic productivity and complexity of rain-fed cropland, irrigated cropland, or range, pasture, forest, and woodlands resulting from a combination of pressures, including land use and management practises"* (`UNCCD 1994, Article
1 <https://www.unccd.int/sites/default/files/relevant-links/2017-01/UNCCD_Convention_ENG_0.pdf>`__).
This definition was adopted for the SDG 15.3.1

UNCCD Good Practice Guidelines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In 2017, the UNCCD released the first version of the  `good practice guidance (GPG) <https://prais.unccd.int/sites/default/files/helper_documents/4-GPG_15.3.1_EN.pdf>`__. In 2021, a revised version of the `GPG <https://www.unccd.int/sites/default/files/documents/2021-09/UNCCD_GPG_SDG-Indicator-15.3.1_version2_2021.pdf>`__ was published. The module is based on the most recent version of the GPG (version 2). The GPG outlines a comprehensive approach to land degradation and suggests methods for restoring degraded land by providing guidance for governments, businesses, local communities, and other stakeholders.


Approach
""""""""

The amount of land degradation for SDG Indicator 15.3.1 is measured using a combination of three sub-indicators. The results of the sub-indicators are put together using the one-out-all-out statistical principle to make a binary indicator that says the land in question is either "degraded" or "not degraded." 

- The transition of land cover over time provides important insights into how land characteristics have changed. 

- Trends in land productivity measure important changes in productivity over time, whether they are positive, negative, or stay the same. 

- Changes in above- and below-ground carbon stocks, which are currently shown by soil organic carbon (SOC) stocks.

Any significant decrease or negative change in one of the three sub-indicators is regarded as land degradation. 

Sub-indicators
##############

Productivity
++++++++++++

The land productivity sub-indicator measures the changes in land productivity. A continuous decrease in productivity for a long time indicates potential degradation in land productivity.
Three matrices are used to detect such changes in productivity:

**Productivity trend**
     

It measures the trajectory of changes in productivity over time.

The `Mann–Kendall <https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient>`__ trend test is used to describe the monotonic trend or
trajectory (increasing or decreasing) of the productivity for a given
time period.

To identify the scale and direction of the trend a five-level scale is
proposed:

-  Z score < -1.96 = Degrading, as indicated by a significant decreasing
   trend

-  Z score < -1.28 AND ≥ -1.96 = Potentially Degrading

-  Z score ≥ -1.28 AND ≤ 1.28 = No significant change

-  Z score > 1.28 AND ≤ 1.96 = Potentially Improving, or

-  Z score > 1.96 = Improving, as indicated by a significant increasing
   trend

The area of the lowest negative z-score level (< -1.96) is considered
degraded, the area between z-score -1.96 to 1.96 is considered stable and the 
area above 1.96 is considered improved for calculating the sub-indicator.

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/trend_z.svg
    :alt: trend z score

**Productivity state**
     

The state represents the current level of productivity in a land unit compared to
the historical observations of productivity for that land unit over
time. It is measured as follows:

.. math::

   \mu = \frac{\sum_{n-15}^{n-3}x_n}{13} \\

   \sigma = \sqrt{\frac{\sum_{n-15}^{n-3}(x_n-\mu)^2}{13}}

Where, :math:`x` is the productivity and n is the year of analysis.

The mean productivity of the current period is given as:

.. math:: \bar{x} = \frac{\sum_{n-2}^nx_n}{3}

and the :math:`z` score is given as

.. math:: z =\frac{\bar{x}-\mu}{\frac{\sigma}{\sqrt{3}}}

The five-level stats are as follows:

-  Z score < -1.96 = Degraded, showing a significantly

   lower mean in the recent years compared to the longer term

-  Z score < -1.28 AND ≥ -1.96 = At risk of degrading

-  Z score ≥ -1.28 AND ≤ 1.28 = No significant change

-  Z score > 1.28 AND ≤ 1.96 = Potentially Improving

-  Z score > 1.96 = Improving, as indicated by a significantly higher
   mean in recent years compared to the longer term.
   


The area of the lowest negative z-score level (< -1.96) is considered degraded, 
the area between z-score -1.96 to 1.96 is considered stable and the area above 
1.96 is considered improved for calculating the sub-indicator.

Productivity performance
           

Productivity performance indicates the level of local land productivity
relative to other regions with similar productivity potential.

The maximum productivity index, :math:`NPP_{max}` value (90 :sup:`th` percentile)
observed within the simillar ecoregion is campared the observed
productivty value (observed NPP). It is given as:

.. math:: \text{performance} = \frac{NPP_{observed}}{NPP_{max}}

The pixels with an NPP (vegetation index) less than 0.5 of the :math:`NPP_{max}`
is considered as degraded.

Either of the following look-up tables can be used to calculate the sub-indicator:

Look-up table to combine productivity metrics

+------------+------------+----------------+---------------+---------------+
|  Trend     | State      | Performance    | Productivity sub-indicator    |
|            |            |                | GPG v1        | GPG v 2       |
+============+============+================+===============+===============+
| Degrdaded  |  Degrdaded |  Degrdaded     | Degrdaded     |  Degrdaded    |
+------------+------------+----------------+---------------+---------------+
| Degrdaded  |  Degrdaded |  Not degrdaded | Degrdaded     |  Degrdaded    |
+------------+------------+----------------+---------------+---------------+
| Degrdaded  |  Stable    |  Degrdaded     | Degrdaded     |  Degrdaded    |
+------------+------------+----------------+---------------+---------------+
| Degrdaded  |  Stable    |  Not degrdaded | Degrdaded     |  Stable       |
+------------+------------+----------------+---------------+---------------+
| Degrdaded  |  Improved  |  Degrdaded     | Degrdaded     |  Degrdaded    |
+------------+------------+----------------+---------------+---------------+
| Degrdaded  |  Improved  |  Not degrdaded | Degrdaded     |  Degrdaded    |
+------------+------------+----------------+---------------+---------------+
| Stable     |  Degrdaded |  Degrdaded     | Degrdaded     |  Degrdaded    |
+------------+------------+----------------+---------------+---------------+
| Stable     |  Degrdaded |  Not degrdaded | Stable        |  Stable       |
+------------+------------+----------------+---------------+---------------+
| Stable     |  Stable    |  Degrdaded     | Stable        |  Degrdaded    |
+------------+------------+----------------+---------------+---------------+
| Stable     |  Stable    |  Not degraded  | Stable        |  Stable       |
+------------+------------+----------------+---------------+---------------+
| Stable     |  Improved  |  Degraded      | Stable        |  Stable       |
+------------+------------+----------------+---------------+---------------+
| Stable     |  Improved  |  Not degraded  | Stable        |  Stable       |
+------------+------------+----------------+---------------+---------------+
| Improved   |  Degraded  |  Degraded      | Degraded      |  Degraded     |
+------------+------------+----------------+---------------+---------------+
| Improved   |  Degrdaded |  Not degrdaded | Improved      |  Improved     |
+------------+------------+----------------+---------------+---------------+
| Improved   |  Stable    |  Degraded      | Improved      |  Improved     |
+------------+------------+----------------+---------------+---------------+
| Improved   |  Stable    |  Not degraded  | Improved      |  Improved     |
+------------+------------+----------------+---------------+---------------+
| Improved   |  Improved  |  Degraded      | Improved      |  Improved     |
+------------+------------+----------------+---------------+---------------+
| Improved   |  Improved  |  Not degraded  | Improved      |  Improved     |
+------------+------------+----------------+---------------+---------------+


.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/look-up-table.svg
    :alt: Look up table


Available Dataset: 
                  

Sensors : MODIS, Landsat 4, 5, 7 and 8, Sentinel 2

NPP metric: NDVI, EVI and MSVI, Terra NPP

Land cover
++++++++++

The land cover sub-indicator is based on transitions of land cover from the initial year to the final year. A transition matrix is used to mark the transitions as degraded, stable or improved. A default matrix with predefined transition statuses is given based on UNCCD land cover categories. The transitions can be altered in the matrix considering  local context and  settings.

Default land cover dataset: ESA CCI land cover (1992 - 2020)


**Transition matrix for custom land cover legends**

A custom transition matrix can be used in combination with the custom land cover legend. The matrix needs to be a comma-separated value(.csv) file in the following form:

The first two columns, excluding the first two cells (:math:`a_{31}...a_{n1} \text{and } a_{32}...a_{n2}` ), must contain class labels  and pixel values for the initial land cover respectively.
The first two rows, excluding the first two cells, (:math:`a_{13}...a_{1n} \text{and } a_{23}...a_{2n}` ) must contain class labels and pixel values for the final land cover respectively. The rest of the higher indexed cells :math:`\left(\left[\begin{matrix}a_{33}&\cdots&a_{3n}\\\vdots&\ddots&\vdots\\2_{n3}&\cdots&3_{nn}\end{matrix} \right]\right)` must contain the transition matrix. Cells :math:`a_{11},a_{12},a_{21}, \text{and } a_{22}` can be used to store some metadata. Use 1 to denote improved transitions, 0 for stable and -1 for degraded transitions.

.. math::
    \mathbf{A} = \left[ \begin{matrix}%
    a_{11}&a_{12}&a_{13}&\cdots&a_{1n}\\
    a_{21}&a_{22}&a_{23}&\cdots&a_{2n}\\
    a_{31}&a_{32}&a_{33}&\cdots&a_{3n}\\
    \vdots&\vdots&\vdots&\ddots&\vdots\\
    a_{n1}&a_{n2}&a_{n3}&\cdots&a_{nn}\end{matrix}\right]


An example of a custom transition matrix:

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/ipccsx_matrix_explained.svg
    :alt: custom transition matrix

Soil Organic Carbon
+++++++++++++++++++

Based on the IPCC methodology (Chapter 6).


Final indicator
+++++++++++++++

The final indicator is calculated based on the one out all out the principle.

Users Guide
-----------

Select AOI
^^^^^^^^^^

SDG indicator 15.3.1 will be calculated based on the user inputs. The first mandatory input is the Area Of Interest (AOI). In this step you’ll have the possibility to choose from a predefined list of administrative layers or use your own datasets, the available options are:

**Predefined layers**

-   Country/province
-   Administrative level 1
-   Administrative level 2

**Custom layers**

-   Vector file
-   Drawn shapes on the map
-   Google Earth Engine Asset

After selecting the desired area, click over :guilabel:`Select these inputs` and the map shows up your selection.

.. note::

    You can only select one area of interest. In some cases, depending on the input data you could run out of resources in GEE.
    
.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/aoi_selection.png
    :alt: AOI selection
    
Parameters
""""""""""

To run the computation of SDG 15.3.1, several parameters need to be set. Please read the `Good practice guidelines <https://www.unccd.int/sites/default/files/documents/2021-09/UNCCD_GPG_SDG-Indicator-15.3.1_version2_2021.pdf>`__ to better understand the parameters required to calculate SDG 15.3.1 indicator and it's sub-indicators.

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/parameters.png
    :alt: parameters

Mandatory parameters
####################

-   **Assessment period**: are set in years and must be in the correct order. The **Starting year** that you select will update the list of available sensors. You won't be able to choose sensors that were not launched by the **Ending year**

.. note::
        In a strictly technical sense, the productivity state metric assessment period should be longer than four years (historical plus the last three years). However, the assessment time frame for each of the sub-indicators and metrics is customizable in the :ref:`sdg-advanced-parameters` section.

-   **Sensors**: After selecting the dates, all the available sensors within the timeframe will be available. You can deselect or re-select any sensor you want. The default value is set to all the Landsat satellites available within the selected timeframe.

.. note::
   
        Some of the sensors are incompatible with each other. Thus selecting Landsat, MODIS or Sentinel dataset in the **sensors** dropdown will deselect the others.
        
-   **Vegetation index**: The vegetation index will be used to compute the trend trajectory, default to *NDVI*.

-   **trajectory**: There are 3 options available to calculate the productivity trend that describes the trajectory of change, default to *productivity (VI) trend*.

-   **land ecosystem functional unit**: default to *Global Agro-Environmental Stratification (GAES)*, other available options are:

    - `Global Agro Ecological Zones (GAEZ), historical AEZ with 53 classes <https://gaez.fao.org/>`__ 
    - `World Ecosystem <https://doi.org/10.1016/j.gecco.2019.e00860>`__
    - `Global Homogeneous Response Units <https://doi.pangaea.de/10.1594/PANGAEA.775369>`__
    - Calculate based on the land cover (`ESA CCI <https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-land-cover?tab=overview>`__) and soil texture (`ISRIC <https://www.isric.org/explore/soilgrids>`__)

-   **climate regime**: default to *Per pixel based on global climate data* but you can also use a fixed value everywhere using a predefined climate regime in the dropdown menu or select a custom value on the slider


.. _sdg-advanced-parameters:

Advanced parameters
###################

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/advanced_parameters.png
    :alt: advanced parameters

Productivity parameters
+++++++++++++++++++++++++++++++

Assessment periods for all the metrics can be specified individually. Keep them blank to use the Start and End dates for the respective metric. 

.. note::
    
     If the Starting  and Ending years you've chosen for your assessment period aren't at least four years apart, then you'll also need to choose an assessment period for the productivity state that's longer than that. The module will disregard the value of a particular metric if you only specify the start or end year.

The default productivity look-up table is set to GPG version 2. You could also select GPG version 1. Please refer to the approach section for the tables.  Please read section 4.2.5 of the `GPG version 2 <https://www.unccd.int/sites/default/files/documents/2021-09/UNCCD_GPG_SDG-Indicator-15.3.1_version2_2021.pdf>`__ to know more about the look-up table.

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/prod_params.png
    :alt: productivity parameters


Land cover parameters:
++++++++++++++++++++++++++++++

**Water body data**

The default water body data is set to JRC water body seasonality data with a seasonality of 8 months. An :code:`ee.Image` can be used for the water body data with a pixel value greater than equal to 1. Waterbody can be extracted from the land cover data by specifying the corresponding pixel value. Set the slider at 70 to use the waterbody extent from ESA CCI land cover data in case of default land cover and land cover data using UNCDD land cover categories (default matrix).


.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/water_body.png
    :alt: water body


The default land cover is set to the ESA CCI land cover data. The tool will use the CCI land cover system of the **start date** and the **end date**. These land cover images will be reclassified into the UNCCD land cover categories and used to compute the land cover sub-indicator. However, You can specify your own data for the start and the end land cover data. Provide the :code:`ee.Image` asset name and the band that need to be used and the default dataset will be replaced in the computation with the specified land cover data. 

.. note::

     If you would like to use the default land cover transition matrix, the custom dataset needs to be classified in the UNCCD land cover categories. Please refer to :ref:`sdg-reclassify` to know how to reclassify the local dataset into different classification systems.
    
To compute the land cover sub-indicator with the UNCCD land cover categories, the user can modify the default transition matrix. Based on the user's local knowledge of the conditions in the study area and the land degradation process occurring there, use the table below to identify which transitions correspond to degradation (D), improvement (I), or no change in terms of land condition (S).

The rows stand for the initial classes and the columns for the final classes.

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/default_matrix.png
    :alt: water body


    
**Custom land cover transition matrix**

If you would like to use a custom land cover transition matrix, select the :guilabel:`Yes` radio button and select the CSV file. Use `this matrix <https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/utils/ipccsx_matrix.csv>`__ as a template to prepare a matrix for your land cover map.

.. tip::

    The module varifies the land cover pixel values with the values mentioned in the transition matrix. If there is/are missing class/es in your land cover data, switch of :guilabel:`Verify land cover pixel` to bypasss the exact matching of pixel values.

SOC parameters:
+++++++++++++++++++++++
    
Launch the computation
######################

Once all the parameters are set you can run the analysis by clicking on :guilabel:`Load the indicators`.
It takes time to calculate all the sub-indicator. Look at the Alert at the bottom of the panel that displays the current state of analysis.

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/validate_data.png
    :alt: validate data


Results
"""""""

The results are displayed to the end user in the next panel. On the left, the user will find the transition and the distribution charts on the right, an interactive map where every indicator and sub-indicators are displayed.

Click on the :guilabel:`donwload` button to export all the layers, charts and tables to your SEPAL folder. 

The results are gathered in the :code:`module_results/sdg_indicators/` folder. In this folder a folder is set for each AOI (e.g. :code:`SGP/` for Singapore) and within this folder results are grouped by run computation. the title of the folder reflect the parameters following this symbology: :code:`<start_year>_<end_year>_<satellites>_<vegetation index>_<lc units>_<custom LC>_<climate>`.

.. note:: 

    As an example for computation used in this documentation, the results were saved in : :code:`module_results/sdg_indicator/SGP/2015_2019_modis_ndvi_calculate_default_cr0/`

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/results.png
    :alt: validate data
    
.. note:: 

    The results are interactive, don't hesitate to interact with both the charts and the map layers using the widgets.
    
    .. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/results_interaction.gif
        :alt: result interaction
        
Transition graph 
^^^^^^^^^^^^^^^^

This chart is the `Sankey diagram <https://en.wikipedia.org/wiki/Sankey_diagram>`__ of the land cover transition between baseline and target year. The colour is corresponding to the initial class.

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/transition_graph.png
    :alt: transition graph
    :width: 40%
    :align: center

Distribution graph 
^^^^^^^^^^^^^^^^^^

This chart displays the distribution of the SDG 15.3.1 indicator by land cover classes.

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/distribution_graph.png
    :alt: distribution chart
    :width: 40%
    :align: center

Interactive map
^^^^^^^^^^^^^^^

Following layers are available on the interactive map:

-   Final indicator SDG 15.3.1
-   land cover sub-indicator
-   Productivity sub-indicator
-   Land cover sub-indicator
-   SOC sub-indicator
-   Land cover maps, and
-   AOI


.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/lc_map.png
    :alt: lc_map
    :width: 80%
    :align: center


.. _sdg-reclassify:

Reclassify
""""""""""

.. warning:: 

    To reclassify a land cover data, it needs to be available to the user as a :code:`ee.Image` in GEE.

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/reclassification.png
    :alt: reclassification


In order to use a custom land cover map, the user needs to first reclassify to a classification system. 

First, select the asset in the combobox. It will be part of the dropdown value if the asset is part of the user's asset list. If that's not the case simply set the name of the asset in the TextField.


Then select the band that will be reclassified.

For the default UNCCD land cover categories,  values between 10 to 70 are used to describe the following land cover classes:

#. Tree-covered areas (10)
#. Grassland (20)
#. Cropland (30)
#. Wetland (40)
#. Artificial surface (50)
#. Other lands (60)
#. Water bodies (70)

These categories are specified in the default UNCCD classification system. For a custom legend/classification system, upload a matrix with first clomun as pixel values, second column as class label and third as colour code HEX format. An example is given below:

+--+-----------------+-------+
|21|Rural settlement |#005CE6|
+--+-----------------+-------+
|22|Mixed plantation |#FFFFBE|
+--+-----------------+-------+
|23|Urban settlement |#FFAA00|
+--+-----------------+-------+
|24|Mines            |#F2D9BF|
+--+-----------------+-------+
|25|Bare soil        |#E6E600|
+--+-----------------+-------+
|26|Rivers           |#2699CC|
+--+-----------------+-------+
|27|Lake             |#40B3FF|
+--+-----------------+-------+
|28|Mangrove         |#5C8944|
+--+-----------------+-------+
|29|Forest           |#B3FF80|
+--+-----------------+-------+
|30|Cropland         |#704489|
+--+-----------------+-------+
|31|Grassland        |#99FF00|
+--+-----------------+-------+
|32|Orchard          |#1DBD9C|
+--+-----------------+-------+


.. note::

    This band need to be a categorical band, the reclassification sytem won't work with continuous values.
    
Click on :guilabel:`get table`. This will generate a table with all the categorical values of the asset. In the second column the user can set the destination value. 

.. tip::

    - If the destination class is not set, the class will be interpreded as no_ata i.e. 0;
    - click on :guilabel:`save` to save the reclassification matrix. It's useful when the baseline and target map are in the same classification system;
    - click on :guilabel:`import` to import a previously saved reclassification matrix.
    
    
Click on :guilabel:`reclassify` to export the map in GEE using the IPCC classification system. The export can be monitored in GEE. 

The following GIF will show you the full reclassification process with an simple example.

.. image:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/master/doc/img/reclassify_demo.gif
    :alt: reclassification demo


.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/sdg_15.3.1/release/doc/en.rst
