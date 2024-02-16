eSBAE - ensemble Sample Based Area Estimation
================================
*accurate forest change estimates and uncertainty using multi-source remote sensing, change detection algorithms over a dense sampling grid*

The ensemble Sample Based Area Estimation workflow aims to produce
reliable estimates of forest change, including uncertainty using dense
sampling and a multi-algorithmic approach.

This workflow is provided as a set of notebooks allowing users to follow
an optimized workflow for creating Sample Based Area Estimates resulting
from an ensemble classification of various time-series and remote
sensing products over a very dense set of points. This is further
enhanced through an optimized stratification strategy based on the
Kozak-Neyman stratification.

The eSBAE notebook repository contains standard scripts for conducting
the workflow using generic global data, without a priori training data.

These scripts can be cloned from
https://github.com/sepal-contrib/eSBAE_notebooks

Most of the data and functionality is coming from Google Earth Engine,
for which you will need a valid account. It is possible to freely sign
up here: https://code.earthengine.google.com/register

The eSBAE notebooks are a series of Jupyter notebooks intended to
streamline the process of creating activity data for measurement,
reporting, and verification of REDD+ and other carbon standards.

eSBAE is mainly based on the sampling-handler python library that
provides all the necessary underlying functionality. While the notebooks
take away the heavy burden of coding each single element, you will only
need to declare some basic input variables that define your custom
needs. This means you do not need to be an experienced python
programmer, but basic understanding does help.

You will notice that the structure of each notebook is fairly similar,
with only the parameter settings adapting for the current step. You can
also use individual parts for specific purposes, but going through each
of the notebooks consecutively ensures the best way for a smooth
execution of the entire process.

There are two elements that tie the outputs of each notebook together -
the *Project Name* and an underlying configuration file. This not only
eases the interaction but also ensures transparency, reproducibility,
and interaction between different steps/notebooks.

Description of scripts in the eSBAE_notebooks repository:

*00-Introduction-to-Jupyter and Python.ipynb* is an introductory script
that explains the basic usage of Python and the different kinds of
datatypes.

*01_pre-analysis* provides code and functions for the extraction of some
basic information on forest statistics for a given area of interest as
well as sample size and error calculations.

*02_sample_design.ipynb* creates the grid of points based on squares or
hexagons for your area of interest, using the spacing estimated in the
previous script.

*03_time_series_extract* is the process for extracting satellite time
series for the sampling design you produced in script 02.

*04_dataset_augmentation.ipynb* executes various change detection
algorithms (BFAST, CUSUM, CCDC among others) based on the previously
extracted time series.

*05_unsupervised_subsampling.ipynb* runs a KMeans unsupervised
clustering algorithm to extract “statistically balanced” training data
in order to sample all classes of change and no change, while over
proportionally capturing rare classes. This script is recommended when
you do not have an prior training data

For the CAFI drivers project, we developed customized scripts for all
steps after step 4 dataset augmentation, as we have visually interpreted
data available to use as training to estimate probabilities of change
and subsequently stratify the entire grid of points to select samples
for further visual interpretation.

The CAFI DDD eSBAE scripts can be cloned from this repository:
https://github.com/aurelgrooves/CAFI_DDD

These scripts perform the following tasks:

*esbae_05a_merge_esbae_ceo_str_random.ipynb*: This workflow combines the
validated stratified random data from phase I of the project with the
eSBAE variables from the dataset augmentation step.

*esbae_05b_supervised_w_CAFI_data.ipynb*: performs a supervised
classification of change types (deforestation, degradation, stable and
non-forest) on the systematic eSBAE variables using the stratified
random data from phase I as training. This outputs a probability of
forest change for all points and 3 strata: high probability of no
change, medium probability of change and high probability of change.

*esbae_05c_CAFI_sampling_for_CEO.ipynb*: uses the supervised model and
strata created in the previous step to extract the desired number
proportional samples for validation with CEO.

*esbae_05d_merge_sbae_ceo_systematic.ipynb*: the data validated in CEO
are merged with the eSBAE points for country of interest

*esbae_05e_supervised_CAFI_all_points.ipynb*: performs a supervised
classification of change types on all points using the validated data.
The years of change are applied using CUSUM dates.

*esbae_06_calculate_areas.ipynb*: calculate areas and margin of error
for deforestation and degradation annually or for all years as well as
stable, non-forested areas.

Installing eSBAE_notebooks and CAFI_DDD in your SEPAL workspace.

1. Activate an m2 instance in the SEPAL terminal

..

.. thumbnail:: ../_images/workflows/esbae/instances.png
    :title: activating an instance
    :align: center
    :group: workflows-eSBAE

2. Once the instance is started type the following command:

+-----------------------------------------------------------------------+
| Git clone https://github.com/sepal-contrib/eSBAE_notebooks            |
+=======================================================================+
+-----------------------------------------------------------------------+

You will see a new folder created in your SEPAL workspace

.. thumbnail:: ../_images/workflows/esbae/notebook_folder.png
    :title: notebooks installed in your SEPAL workspace
    :align: center
    :group: workflows-eSBAE

Now you are ready to start the analysis.

Click on the Apps menu in SEPAL and double click to open Jupyter Lab:

.. thumbnail:: ../_images/workflows/esbae/jupyter.png
    :title: open Juypter Lab
    :align: center
    :group: workflows-eSBAE

You can then navigate to the eSBAE_notebooks directly and open the
scripts

.. thumbnail:: ../_images/workflows/esbae/jupyter_open.png
    :title: opening Jupyter Lab
    :align: center
    :group: workflows-eSBAE

**Script 0 - Introduction to Jupyter Notebooks and Python**

This script takes you through the basic interface and datatypes of
python. To execute a cell and continue to the next one, hit Shift +
Enter on your keyboard.

.. thumbnail:: ../_images/workflows/esbae/keyboard.png
    :title: execute a cell using shift + enter
    :align: center
    :group: workflows-eSBAE

A cell that has not been executed is indicated by [ ]. When it is
running you will see [ \* ] and when it has executed you will see a
number in the brackets in the order of execution. For example [ 5 ]
means this cell was executed 5th in the series.

To de-active a line enter # at the beginning of the line. This will
effectively tell SEPAL to skip whatever follows.

Use this notebook to practice executing cells and change some of the
contents to understand what the script does.

*Important:* for each script, always execute all the cells in order, do
not skip any, particularly the first cell which imports libraries and
installs needed tools and functions.

**Script I - Pre-analysis**

Forest and Deforestation statistics, sample size and error calculation & simulation
===================================================================================

This notebook provides code and functions for the extraction of some
basic information on forest statistics for a give area of interest as
well as sample size and error calculations. It is structured in the
following parts:

1. Forest area and deforestation statistics according to Global Forest
   Change product (`Hansen et al
   2013 <https://10.0.4.102/science.1244693>`__)

2. Theoretical sample size and error calculation according to Cochran
   for capturing deforestation events

3. Simulation of sampling error based on Global Forest Change product

**1 - Basic Parameter Settings**
================================

Here you will define some of the key parameters to create the subsequent
forest statistics.

1. Project Name: This will not only give your work a name, but it also
   defines the output folder within the module_results/esbae (if you are
   on SEPAL), as well as a directory within your Earth Engine assets.
   **NOTE** that it shall not contain any space.

2. Area of Interest (AOI): Your AOI defines the spatial extent for which
   the data will be generated and analyzed. It can come in different
   formats, such as a (filtered) Earth Engine feature collection, an OGR
   compatible geospatial data format (e.g. Shapefile, Geopackage, KML,
   GeoJSON), or a geopandas GeoDataFrame object. You can enter a country
   name to use the boundaries from FAO GAUL, you can find the country
   names here:
   https://data.apps.fao.org/catalog/dataset/gaul-code-list-global-admin-1

..

   If you want to select a province, enter a province name in the
   country line and change the aoi line to the following:

+-----------------------------------------------------------------------+
| :mark:`aoi = gaul.filter(ee.Filter.eq("ADM1_NAME", country)).union()` |
+=======================================================================+
+-----------------------------------------------------------------------+

Otherwise you can use an existing GEE asset for example, the buffered
simplified boundary of Cameroun from the CAFI database:

+-----------------------------------------------------------------------+
| :mark:`aoi=ee.FeatureCollection('projects/cafi_fa                     |
| o_congo/aoi/cafi_countries_buffer_simple').filter(ee.Filter.eq('ISO', |
| 'CMR'));`                                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

3. Start and end year will define the temporal extent, for which
   deforestation areas are extracted from the GFC product. This area
   will ultimately be used to determine the sampling size based on
   Cochran's equation.

..

   For the CAFI project we will extract all data from 2010 to the
   present:

+-----------------------------------------------------------------------+
| :mark:`# envisaged FREL/change assessment period (years are           |
| inclusive)                                                            |
| start_year = 2010 # YYYY format                                       |
| end_year = 2024 # YYYY format`                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

..

   4. Tree cover and mmu determine by which threshholds the GFC product
   will be filtered in order to consider a (set of) pixels as forest.
   Values are set in percentage and hectare.

   You can set the parameters according to the forest definitions for
   the CAFI countries described
   `here <https://lookerstudio.google.com/u/0/reporting/c19ee6c9-04ff-4522-9f38-fe15bc04e9d3>`__

:mark:`# forest definition
tree_cover = 10 # in percentage
mmu = 0.5 # in hectare`

The final component of this script will evaluate the optimal grid
spacing and sample size for your area of interest to reach an expected
margin of error.

.. thumbnail:: ../_images/workflows/esbae/grid_spacing.png
    :title: estimating the optimal grid size
    :align: center
    :group: workflows-eSBAE

**II - Sample Design**

This script creates the point samples for time series extraction and
analysis.

This script requires an m2 instance, but for larger areas such as DRC, a
c8 instance is needed..

**Introduction**
----------------

The base for the eSBAE approach is a dense grid that captures change at
a sufficient level of confidence. A systematic sampling design shall be
be employed. This notebook provides the functionality to create such a
grid over the given AOI (defined in Notebook 1).

Two grid shapes are available, i.e. squared or hexagonal grid. In
addition, it is necessary to determine the size of each grid cell as
well as the projection.

**Squared grid**
----------------

Squared grids are a simple way of creating a grid. They are in use for
various geospatial applications. The grid size of the squared grid is
selected in metres, defining the single border length of each grid cell.

**Hexagonal grid**
------------------

Lately, hexagonal grids are adapted in National Forest Monitoring Sytems
as they possess some particular characteristics. Foremost, they reduce
the error on area, but they also do assure that each point within the
grid cell is mre or less at the same distance to the centre. Indeed, the
ideal shape under that criteria would be a circle. It is however not
possible to create a consistent grid of circles. The hexagon is the
shape of polygon that comes closest to this criteria, while being able
to provide a consistent grid.

The notebook provides a simplified interface to the dggrid software
library from `Southern Oregon
University <https://www.discreteglobalgrids.org/software/>`__. DGGRID
holds code to generetate standardized hexagonal grids based on a
*Discrete Global Grid System (DGGS)* with a set of predefined
resolutions for specific projections optimized for equal area.

It is important to understand that DGGRID has a **fixed set of
resolutions** that should be selected from column *res* in the below
table (You need to check the manual for other resolutions if you select
a different projection than the ISEA3H)

For advanced usage it is recommended to consult the
`manual <https://webpages.sou.edu/~sahrk/docs/dggridManualV70.pdf>`__.

**Sampling strategies**
-----------------------

The notebook allows to select from 2 sampling strategies within each
grid cell, *centroid* and *random*. The centroid will take the centre
point according to the projection selected, while the random option

**Projections**
---------------

When creating samples, an important consideration is the projection
used. Projections always exhibit distortions with regard to the actual
sphere-like shape of the Earth. As our aim is to give each sample the
same weight in terms of area representativeness, we shall select a
projection that is optimised for **equal area**.

**Squared grid projections**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the table below you can find some examples of global equal area
projections to select from. The information is taken from an article
from Yildrim & Kaya 2008 and can be found
`here <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3790990/#:~:text=The%20level%20of%20distortion%20can,compared%20to%20equal%2Darea%20maps>`__.
**Note** that the commonly used Lat/Lon projection (EPSG:4326) **does**
contain distortions that shall be avoided.

.. thumbnail:: ../_images/workflows/esbae/projections.png
    :title: projection codes
    :align: center
    :group: workflows-eSBAE

**Hexagonal grid projections and grid size**

By default, the ISEA3H projection is used. Consult the `dggrid
manual <https://webpages.sou.edu/~sahrk/docs/dggridManualV70.pdf>`__ for
further projections options.

.. thumbnail:: ../_images/workflows/esbae/dggs.png
    :title: hexagonal grid projections and size
    :align: center
    :group: workflows-eSBAE

**2 - Initialize SampleDesign Class**
-------------------------------------

In the below cell we initialize the SampleDesign Class

1. Grid shape: This defines which shape the underlying systematic grid
   shall have. Choices are squared or hexagonal.

2. Sampling strategy: Here it is set if the samplng point is set in the
   centre or at a random point within each grid cell.

3. Grid projection (as epsg/esri code): As described above, projection
   is an important part when creating the grid. However, equal area
   projections are not the most commonly used projections. The routine
   is able to use a different grid system internally for creating the
   grid and/or placing the centroid. Note that when having selected a
   hexagonal grid, this projection is only being used for the placement
   of the centroid.

4. Output projection: this will define the projection of the final
   output file, independent of the projection the grid was defined. For
   this, it can also be a projection that is not ideal for the creation
   of sampling grids such as Lat/Long.

**1.2 - Create grid cells and sample points for a squared grid**
----------------------------------------------------------------

In this example we create a hexagonal grid for Cameroun

+-----------------------------------------------------------------------+
| :mark:`esbae = SampleDesign(                                          |
| # set your project's name (NEEDS to be the same as in notebook 1 and  |
| 2)                                                                    |
| # no space allowed, use \_ instead                                    |
| project_name='CMR',                                                   |
| # defines the underlying grid,                                        |
| # choices: 'squared', 'hexagonal'                                     |
| shape='hexagonal',                                                    |
| # defines where the sample is placed within the grid,                 |
| # choices: 'random', 'centroid'                                       |
| strategy='centroid',                                                  |
| # defines the projection in which the grid is generated,              |
| # for hexagonal it applies to the centroid calculation only, as       |
| dggrid uses its own projection                                        |
| grid_crs="ESRI:54008",                                                |
| # defines the projection in which the grid is saved                   |
| out_crs='EPSG:4326',                                                  |
| # This is in case you haven't run notebook 1 and want to directly     |
| start from here                                                       |
| # aoi = ee.FeatureCollection('my_ee_feature_collection')              |
| )                                                                     |
| `                                                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

**2 - Create Grid**
===================

Another important aspect is the grid size. **NOTE** that the grid size
is selected differently for squared and hexagonal grids. A squared grid
is simply defined by the distance between each point (which is the same
as a single border length of the underlying grid).

The hexagonal grid, instead, relies on a hierarchical system and has
fixed resolutions (see Internode spacing in the above table). In
addition, it uses a very specific projection optimized for equal area
projections using hexagons.

For CAFI DDD we use a resolution of 1000m or resolution 16 hexagons

+-----------------------------------------------------------------------+
| :mark:`# Those parameters apply to squared grid only (otherwise       |
| ignored)                                                              |
| esbae.squared_grid_size = 1000                                        |
| # Those parameters apply to hexagonal grid only                       |
| esbae.dggrid_resolution = 16 # this relates to the res column from    |
| the table above                                                       |
| esbae.dggrid_projection = 'ISEA3H'                                    |
| # generation of grid                                                  |
| c, p = esbae.generate_samples(upload_to_ee=True, save_as_ceo=True)`   |
+=======================================================================+
+-----------------------------------------------------------------------+

This script will produce an ee asset feature collection of your gridded
points.

The CAFI DDD point assets of 1km hexagonal grids produced for each
country are as follows:

users/faocongo/sbae/sbae_hex16_car

users/faocongo/sbae/sbae_hex16_cmr

users/faocongo/sbae/sbae_hex16_cog

users/faocongo/sbae/sbae_hex16_drc

users/faocongo/sbae/sbae_hex16_eqg

users/faocongo/sbae/sbae_hex16_gab

**III - eSBAE Time-Series Extraction**
======================================

**Extract various time-series data for large sets of points from Google Earth Engine**
--------------------------------------------------------------------------------------

This notebook takes you through the process of extracting time-series
for a set of points using `Google's Earth
Engine <https://earthengine.google.com/>`__. The script is optimized to
deal with thousands of points and will use parallelization to
efficiently extract the information from the platform.

**You will need**:

-  an uploaded table of points (Feature Collection from previous script)

-  the table needs a unique point identifier (‘point_id’)

**You should be aware, that:**

-  As a SEPAL user: this notebook does **not need huge resources**, as
   processing is done on the platform. A **m2 instance** is best suited.

-  The extraction can take up to days (>100000 points). If you are on
   SEPAL, make use of the **"keep instance running"** option within the
   user report dashboard. However, **do not forget** to shut down your
   machine once processing finished.

-  A logfile is created within your tmp-folder. Interruption of
   connectivity to the SEPAL server may lead to block the output of the
   Jupyter notebook. **This does not mean the processing stopped.** You
   can see in esbae_log\_(time) if the processing is still on going.

-  You can restart the kernel and execute all cells, and extraction will
   **start where it stopped**. This is also valid, if your instance has
   been shut down before processing was completely finished.

Here are the parameters for executing the time series extraction for
Cameroun:

+-----------------------------------------------------------------------+
| :mark:`esbae = TimeSeriesExtraction(                                  |
| # your project name that you use fo all of the notebooks              |
| project_name = 'CMR',                                                 |
| # your start and end date.                                            |
| # NOTE that this should go further back to the past than the          |
| # envisaged monitoing period for calibration purposes                 |
| ts_start = '2010-01-01', # YYYY-MM-DD format                          |
| ts_end = '2024-01-01', # YYYY-MM-DD format                            |
| # satellite platform (for now only Landsat is supported)              |
| satellite = 'Landsat',                                                |
| # at what resolution in metres you want to extract (shall conform     |
| with forest definition MMU)                                           |
| scale = 70, # pixel size in metres                                    |
| # wether the TS will be extracted on a bounding box with diameter     |
| scale with original scale (e.g 30m for Landsat) of the underlying     |
| data (True),                                                          |
| # or if the underlying data is rescaled to the scale (False)          |
| # setting it to True might be more accurate, but tends to be slower   |
| bounds_reduce = False,                                                |
| # bands                                                               |
| bands = [                                                             |
| 'green', 'red', 'nir', 'swir1', 'swir2', # reflectance bands          |
| 'ndfi', #'ndmi', 'ndvi', # indices                                    |
| 'brightness', 'greenness', 'wetness' # Tasseled Cap                   |
| ],                                                                    |
| # This is in case you haven't run notebook 1 and 2, and want to       |
| directly start from here                                              |
| #aoi =                                                                |
| ee.FeatureCollection(ee.FeatureCollection('projects/cafi_fao_con      |
| go/modeling/all_ceo_validation_TMF_2023').geometry().convexHull(100)) |
| aoi =                                                                 |
| ee.FeatureCollection(ee.FeatureCollect                                |
| ion('users/faocongo/sbae/sbae_hex16_cmr').geometry().convexHull(100)) |
| )`                                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

**5 - Set a custom grid**
-------------------------

This step is only necessary if you skipped notebook 2. You then need to
define an Earth Engine feature collection as well as the unique point
identifier. Uncomment the lines by removing the #

Here is the code for extracting time series on the CAFI DDD grid for
Cameroun:

+-----------------------------------------------------------------------+
| :mark:`esbae.sample_asset = 'users/faocongo/sbae/sbae_hex16_cmr'      |
| esbae.pid = 'point_id'`                                               |
+=======================================================================+
+-----------------------------------------------------------------------+

This process can take a long time and might need to be restarted several
times.

**4 - Check for already processed data (optional)**
---------------------------------------------------

This is useful for large points sizes and when the connection to Sepal
gets interrupted. Usually processing will continue, but it is not
straightforward to track progress. You can instead restart the kernel,
execute all cells and see if processing has been finished with the
following line of code.

This line will tell you when to proceed to the next notebook:

+-----------------------------------------------------------------------+
| :mark:`esbae.check_if_completed()`                                    |
|                                                                       |
| :mark:`INFO: Verifying the number of points for which the time-series |
| have already been extracted...`                                       |
|                                                                       |
| :mark:`INFO: Time-series data has been extracted completely. Time to  |
| move on with the dataset augmentation notebook.`                      |
+=======================================================================+
+-----------------------------------------------------------------------+

**IV - eSBAE Dataset Augmentation**
===================================

**Run various change detection algorithms on previously extracted time-series data**
------------------------------------------------------------------------------------

This notebook takes you through the process of running various change
detection algorithms for the time series extracted from your set of
points using `Google's Earth Engine <https://earthengine.google.com/>`__
as well as python routines. The script is optimized to deal with
thousands of points and will use parallelization to efficiently extract
the information from the platform.

**You will need**:

-  having successfully executed Notebook 3 of the eSBAE notebook series

**This notebook runs best on a r16 instance**

You must enter the following parameters:

The project name, same as in previous scripts

The start of the calibration period (specifically for BFAST)

And the time you want to analyze. This time period should be encompassed
in the time series you extracted in the previous step - otherwise the
data augmentation will not work.

The band which must be included in your band list and identified in
script 3.

Here the example for CAFI processing for Cameroun

+-----------------------------------------------------------------------+
| :mark:`esbae = DatasetAugmentation(                                   |
| # your project name, as set in previous notebooks                     |
| project_name = CMR,                                                   |
| # start of calibration period (mainly for bfast)                      |
| calibration_start = '2010-01-01', # YYYY-MM-DD format                 |
| # Actual period of interest, i.e. monitoring period                   |
| monitor_start = '2016-01-01', # YYYY-MM-DD format                     |
| monitor_end = '2023-12-31', # YYYY-MM-DD format                       |
| # select the band for univariate ts-analysis (has to be inside bands  |
| list)                                                                 |
| ts_band = 'ndfi'                                                      |
| )`                                                                    |
|                                                                       |
| You may have many different files to process, you will need to keep   |
| your instance alive to continue processing. If the instance has       |
| stopped or you have been disconnected, you may simply restart the     |
| script again. The script will indicate when processing has completed, |
| for example for Cameroun:                                             |
+=======================================================================+
+-----------------------------------------------------------------------+

.. thumbnail:: ../_images/workflows/esbae/data_augmentation_finished.png
    :title: data augmentation is complete
    :align: center
    :group: workflows-eSBAE

