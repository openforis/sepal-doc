Perform area estimation analysis with SEPAL-CEO
===============================================

.. note::

    All thanks goes to `SIG-GIS <https://sig-gis.com>`_ for this documentation material.

.. warning::

    To follow this tutorial, you need to:

    -   register to SEPAL
    -   register to GEE
    -   register to CEO

Introduction
------------

Welcome to area estimation with SEPAL and CEO!

In this manual, you will learn how to perform area estimation for land use/land cover and two date change detection classifications. We will use sample-based approaches to area estimation. This approach is preferred over pixel-counting methods because all maps have errors. For example, maps derived from land cover land use classifications may have errors due to pixel mixing, or noise in the input data. Using pixel-counting methods will produce biased estimates of area, and you cannot tell whether these are overestimates or underestimates. Sample based approaches create unbiased estimates of area and the error associated with your map.

The goal of this manual is to teach you how to perform these tasks such that you can conduct your own area estimation for land use/land cover or change detection classifications.

In this manual, you will find four modules covering methods, and one module covering the documentation needed for replicating these methods. The modules are as follows:

* In `module 1`_, you will learn how to generate mosaics based on satellite imagery in SEPAL. You will learn how to build these mosaics by selecting different data sources and images based on dates and cloud cover.
* In `module 2`_, you will learn how to perform a land use/land cover image classification using random forest methods. You will learn how to define your land uses and land covers, collect training data, and run your model.
* In `module 3`_, you will learn how to perform image change detection. Building on skills from `module 1`_ and `module 2`_, you will define what change looks like, collect training data, and run your model. You will also learn about different tools to perform time series analysis.
* In `module 4`_, you will learn how to calculate a sample-based estimate of area and error. You will learn how to use stratified random sampling and verification image analysis in order to calculate area and error estimates based on the classification you create in `module 2`_. You will also learn about some key documentation steps in preparation for `module 5`_.
* In `module 5`_, you will learn about documenting and archiving your area estimation project. The information in this step is required for your project to be replicated by yourself or your colleagues in the future, either for additional areas or points in time.

These exercises include step-by-step directions and are built to facilitate learning through reading and by doing. This manual will be accompanied by short videos, which will visually illustrate the steps described in the text.

.. graphviz::

    digraph process {
           mosaic [label="Mosaic Image creation", href="#mosaic-generation-landsat-sentinel-2", shape=box];
           classif [label="Image classification", href="#image-classification", shape=box];
           change [label="Two dates cange detection", href="#image-change-detection", shape=box];
           sample [label="Sample based area and error", href="#sample-based-estimation-of-area-and-accuracy", shape=box];
           doc [label="Documentation", href="#documentation-and-archiving", shape=box];
           mosaic -> classif;
           mosaic -> change;
           classif -> sample;
           change -> sample;
           sample -> doc;
        }

Our primary tool for this Manual is the System for Earth Observation Data Access, Processing, & Analysis for Land Monitoring (SEPAL). SEPAL is a web based cloud computing platform that enables users to create image composites, process images, download files, create stratified sampling designs, and more all from your browser. SEPAL is a system for earth observations, data access, processing & analysis for land monitoring, which is a cloud-based computing software designed by the United Nation's Food and Agricultural Organization (FAO) to aid in remote sensing applications in developing countries. SEPAL is part of the Open Foris suite of tools. Geoprocessing is possible via Jupyter, JavaScript, R, R Shiny apps, and Rstudio. SEPAL also integrates with Collect Earth Online (CEO) and the Google Earth Engine (GEE).

SEPAL provides a platform for users to access satellite imagery (Landsat and Sentinel-2) and perform change detection and land cover classifications using a set of easy-to-use tools. SEPAL was designed to be used in developing countries where internet access is limited and computers are often outdated and, thus, inefficient for processing satellite imagery. It achieves this by drawing on a cloud-based supercomputer, which enables users to process, store, and interpret large amounts of data. Many more advanced functions than what we will cover here are available in SEPAL for more advanced users.

We will also use two other tools that SEPAL integrates with: CEO and GEE. Collect Earth Online (CEO), is a free and open-source image viewing and interpretation tool, suitable for projects requiring information about land cover and/or land use. CEO enables simultaneous visual interpretations of satellite imagery, providing global coverage from MapBox and Bing Maps, a variety of satellite data sources from Google Earth Engine, and the ability to connect to your own Web Map Service (WMS) or Web Map Tile Service (WMTS). The full functionality is implemented online, no desktop installation is necessary. CEO allows institutions to create projects and leverage their teams to collect spatial data using remote sensing imagery. Use cases include historical and near-real-time interpretation of satellite imagery and data collection for land cover/land use model validation.

Google Earth Engine (GEE) combines a multi-petabyte catalog of satellite imagery and geospatial dataset with planetary-scale analysis capabilities and makes it available for scientists, researchers, and developers to detect changes, map trends, and quantify differences on the Earth's surface. The code portion of GEE (called Code Editor) is a web-based IDE for the Earth Engine JavaScript API. Code Editor features are designed to make developing complex geospatial workflows fast and easy. The Code Editor has the following elements: JavaScript code editor; a map display for visualizing geospatial dataset; an API reference documentation (Docs tab); Git-based Script Manager (Scripts tab); Console output (Console tab); Task Manager (Tasks tab) to handle long-running queries; Interactive map query (Inspector tab); search of the data archive or saved scripts; and geometry drawing tools.

.. seealso::

    You can find more information at these sites, among others:

    -   An older forest change detection manual for SEPAL: `Forest Cover Change Detection with SEPAL <https://drive.google.com/file/d/1kPE2wFNDqNpXycqTJfNUtZf9iWsQHcab/view?usp=sharing>`_
    -   Olofsson et al 2014: `FAO - SFM Tool Detail: Good practices for estimating area and assessing accuracy of land change <http://www.fao.org/sustainable-forest-management/toolbox/tools/tool-detail/en/c/411863/>`_
    -   CEO documentation: `https://collect.earth/support <https://collect.earth/support>`_
    -   GEE documentation: `Earth Engine Code Editor from Google Earth Engine <https://developers.google.com/earth-engine/guides/playground>`_
    -   REDD Compass: `Front Page - GFOI <https://reddcompass.org/frontpage>`_
    -   Reporting and Verification: `Reporting and Verification - GFOI <https://reddcompass.org/reporting-verification>`_

Project Planning Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Project planning and methods documentation play a key role in any remote sensing analysis project. While we use example projects in this Manual, in the future you may use these techniques for your own projects. We encourage you to think about the following items to ensure your resulting products will be relevant, and that your chosen methods are well documented and transparent.

-   Descriptions and Objectives of the Project (State issues and information needs). Are you trying to conform to an IPCC Tier?

-   Descriptions of the end user product (data, information, monitoring system or map that will be created by the project).  What type of information do you need? A map? An inventory? A change product? That is, do you need to know where different land cover types exist or do you just need an inventory of how much there is?

-   How will success be defined for this project? Do you require specific accuracy or a certain level of detail in the final map product?

-   Description of the project area / extent (national/subnational/specific forest/etc.)

-   Description of the features/classes to be modeled or mapped.

    -   Do you have a national definition of “forest”?
    -   Are you aware of the IPCC guidelines for the recommended land use classes and how they will relate to mapping land cover?
    -   Do you have key categories that will drive different analysis techniques?

-   Considerations for measuring, reporting, and verifying your data.

    -   Do you have a strategy; do you know what is required? Do you know where to get the required information? Looking ahead, are you on the right path (who are the decision makers that will inform these strategies?)
    -   What field data will be required for classification and accuracy assessment?
    -   Do you have an existing National Forest Monitoring System (NFMS) in place?

-   Will you supplement your remote sensing project with existing data (local data on forest type, management intent, records of natural disturbance…)?

-   Partnerships (vendors, agencies, bureaus, etc.)

.. _module 1:

Mosaic generation (Landsat & Sentinel 2)
----------------------------------------

SEPAL provides a robust interface for generating Landsat and Sentinel 2 mosaics. Mosaic creation is the first step for the image classification and two date change detection processes covered in `module 2`_ and `module 3`_ respectively. These mosaics can be downloaded locally or to your Google Drive.

In this tutorial, you will create a Landsat mosaic for the Mai Ndombe region of the Democratic Republic of the Congo, where REDD+ projects are currently underway.

.. note::

    **Objectives**

    -   Learn how to create an image mosaic
    -   Become familiar with a variety of options for selecting dates, sensors, mosaicking and download options.
    -   Create a cloud-free mosaic for 2016

.. warning::

    **Prerequisites**

    -   SEPAL account

Create a Landsat Mosaic
^^^^^^^^^^^^^^^^^^^^^^^

If SEPAL is not already open, click to open SEPAL in your browser: https://sepal.io/ and login.
Click on the :code:`Processing` tab.
Then, click on :code:`Optical Mosaic`.
When the Optical Mosaic tab opens, you will see an **Area of Interest** window in the lower right hand corner of your screen.

There are three ways to choose your area of interest. Bring up the menu by clicking the carrot to the right of the window label.

-   Select Country/Province (the default)
-   Select from EE table
-   Draw a polygon

.. figure:: ../_images/workflows/area_estimation/area_of_interest.png
   :alt: The Area of Interest menu
   :width: 350
   :align: center

We will use the :code:`Select a country/province` option.

In the list of countries that pops up, scroll down until you see the available options for **Congo, Dem Republic of**. Note there is also the Republic of Congo, which is not what we're looking for.

.. note::

    Under Province/Area, notice that there are many different options.

Select :code:`Mai-Ndombe`.

.. tip::
    **Optional**: You can add a **Buffer** to your mosaic. This will include an area around the province of the specified size in your mosaic.

Click :code:`Next`.

.. figure:: ../_images/workflows/area_estimation/country_province.png
   :alt: The Country or Province selection screen.
   :align: center

In the :code:`Date` menu you can select the :code:`Year` you are interested in or click on :code:`More`.

-   This interface allows you to refine the dates or seasons you are interested in.
-   You can select a :code:`target date` (The date in which pixels in the mosaic should ideally come from), as well as adjust the start and end date flags.
-   You can also include additional seasons from the past or the future by adjusting the :code:`Past Seasons` and :code:`Future Seasons` slider. This will include additional years' data of the same dates specified. For example, if you're interested in August 2015, including one future season will also include data from August 2016. This is useful if you're interested in a specific time of year but there is significant cloud cover.
-   For this exercise, let's create imagery for the dry season of 2019.

    -   Select July 1 of 2019 as your target date (**2019-07-01**), and move your date flags to **May 1-September 30**.
    -   Click :code:`Apply`.

.. figure:: ../_images/workflows/area_estimation/date_menu.png
   :alt: The date menu.
   :align: center

Now select the :code:`Data Sources (SRC)` you'd like. Here, select the **Landsat L8 & L8 T2** option. The color of the label turns brown once it has been selected.Then click :code:`Done`.

-   **L8** began operating in 2012 and is continuing to collect data
-   **L7** began operating in 2001, but has a scan-line error that can be problematic for dates between 2005-present
-   **L4-5 TM,** collected data from July 1982-May 2012
-   **Sentinel 2 A+B** began operating in June 2015

Now SEPAL will load a preview of your data. By default it will show you where RGB band data is available. You can click on the RGB image at the bottom to choose from other combinations of bands or metadata.

-   When it is done, examine the preview to see how much data is available. For this example, coverage is good. However, in the future when you are creating your own mosaic, if there is not enough coverage of your area of interest, you will need to adjust your parameters.
-   To do so, notice the five tabs in the lower right. You can adjust the initial search parameters using the first three of these tabs. For example, Click on :code:`Dat` to expand the date range if you would like.
-   The last two tabs are for :code:`scene selection` and :code:`composite`, which are more advanced filtering steps. We'll cover those now.

.. figure:: ../_images/workflows/area_estimation/mosaic_preview.png
   :alt: A preview of your mosaic.
   :align: center

We're now going to go through the **scene selection process**. This allows you to change which specific images to include in your mosaic.

-   You can change the scenes that are selected using the :code:`SCN` button on the lower right of the screen. You can use all scenes or select which are prioritized. You can revert any changes by clicking on :code:`Use All Scenes` and then :code:`Apply`.
-   Change the **Scenes** by selecting **Select Scenes** with Priority: **Target Date**

.. figure:: ../_images/workflows/area_estimation/scene_selection.png
   :alt: Selecting scenes for your mosaic.
   :align: center

Click :code:`Apply`. The result should look like the below image.

.. note::

    Notice the collection of circles over the **Mai Ndombe** study area and that they are all populated with a zero. These represent the locations of scenes in the study area and the numbers of images per scene that are selected. The number is currently 0 because we haven't selected the scenes yet.

.. figure:: ../_images/workflows/area_estimation/scene_selection_zeros.png
    :alt: Scene selection process showing zeros before selection.
    :align: center

Click the :code:`Auto-Select` button to auto-select some scenes.

.. figure:: ../_images/workflows/area_estimation/auto_select_scenes.png
    :alt: Arrow showing the button for auto selecting scenes.
    :width: 550
    :align: center

You may set a minimum and maximum number of images per scene area that will be selected. Increase the minimum to **2** and the maximum to **100**. Click :code:`Select Scenes`. If there is only one scene for an area, that will be the only one selected despite the minimum.

.. figure:: ../_images/workflows/area_estimation/auto_select_scenes_menu.png
    :alt: Menu for auto selecting scenes.
    :width: 350
    :align: center

You should now see imagery overlain with circles indicating how many scenes are selected.

.. figure:: ../_images/workflows/area_estimation/imagery_number_scenes.png
    :alt: Example of the imagery with the number of scenes selected
    :width: 450
    :align: center

You will notice that the circles that previously displayed a zero now display a variety of numbers. These numbers represent the number of Landsat images per scene that meet your specifications.

Hover your mouse over one of the circles to see the footprint (outline) of the Landsat scene that it represents. Click on that circle.

.. figure:: ../_images/workflows/area_estimation/select_scenes_interface.png
    :alt: The select scenes interface showing 0 available and 4 selected scenes
    :align: center

In the window that opens, you will see a list of selected scenes on the right side of the screen. These are the images that will be added to the mosaic. There are three pieces of information for each:

-   Satellite (e.g. L8, L7, L5 or L4)
-   Percent cloud cover
-   Number of days from the target date

To expand the Landsat image, hover over one of the images and click :code:`Preview`. Click on the image to close the zoomed in graphic and return to the list of scenes.
To remove a scene from the composite, click the :code:`Remove` button when you hover over the selected scene.

.. figure:: ../_images/workflows/area_estimation/remove_preview_scenes.png
    :alt: Removing or previewing selected scenes.
    :align: center

.. figure:: ../_images/workflows/area_estimation/scene_preview.png
    :alt: Scene preview screen.
    :align: center

On the left hand side, you will see **Available Scenes**, which are images that will not be included in the mosaic but can be added to it. If you have removed an image and would like to re-add it or if there are additional scenes you would like to add, hover over the image and click :code:`Add`.

-   Once you are satisfied with the selected imagery for a given area, click :code:`Close` in the bottom right corner.
-   You can then select different scenes (represented by the circles) and evaluate the imagery for each scene.

.. figure:: ../_images/workflows/area_estimation/select_scenes_1.png
    :alt: Select scenes screen showing one available scene and 3 selected scenes
    :width: 450
    :align: center

You can also change the composing method using the :code:`CMP` button on the lower right.

.. note::

    Notice that there are several additional options including shadow tolerance, haze tolerance, NDVI importance, cloud masking and cloud buffering.

For this exercise, we will leave these at their default settings. If you make changes, click :code:`Apply` after you're done.

.. figure:: ../_images/workflows/area_estimation/composite.png
    :alt: The composite menu.
    :width: 350px
    :align: center

Now we'll explore the :code:`Bands` dropdown. Click on the :code:`Red|Green|Blue` at the bottom of the page.

.. figure:: ../_images/workflows/area_estimation/arrow_bands.png
    :alt: Arrow pointing at the red, green, blue bands.
    :align: center

The below dropdown menu will appear.

-   Select the **NIR, RED, GREEN** band combination. This band combination displays vegetation as red, with darker reds indicating dense vegetation. Bare ground and urban areas appear grey or tan, while water appears black. NIR stands for near infrared.
-   Once selected, the preview will automatically show what the composite will look like.
-   Use the scroll wheel on your mouse to zoom in to the mosaic and then click and drag to pan around the image. This will help you assess the quality of the mosaic.

.. figure:: ../_images/workflows/area_estimation/bands_menu.png
    :alt: The band combinations menu.
    :width: 350px
    :align: center

The map now shows the complete mosaic that incorporates all of the user-defined settings. Here is an example, yours may look different depending on which scenes you chose.

.. figure:: ../_images/workflows/area_estimation/completed_mosaic.png
    :alt: The imagery preview with the completed mosaic shown.
    :width: 450
    :align: center

Using what you've learned, take some time to explore adjusting some of the input parameters and examine the influence on the output. Once you have a composite you are happy with, we will download the mosaic (instructions follow).

-   For example, if you have too many clouds in your mosaic, then you may want to adjust some of your settings or choose a different time of year when there is a lower likelihood of cloud cover.
-   The algorithm used to create this mosaic attempts to remove all cloud cover, but is not always successful in doing so. Portions of clouds often remain in the mosaic.

Name and Save your Recipe and Mosaic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, we will name the ‘recipe' for creating the mosaic and explore options for the recipe.

.. note::
    You will use this recipe when working with the classification or change detection tools, as well as when loading SEPAL mosaics into SEPAL's Collect Earth Online.

.. tip::

    You can make the recipe easier to find by naming it. Click on the tab in the upper right and type in a new name. For this example use *MiaNdombe_LS8_2019_Dry.*

Now let's explore options for the recipe. Click on the three lines in the upper right hand corner.

-   You can **Save the recipe** (SEPAL will do this automatically on retrieval) so that it is available later.
-   You can also **Duplicate the recipe**. This is useful for creating two years of data, as we will do in `module 3`_.
-   Finally you can **Export the recipe**. This downloads a zip file with a JSON of your mosaic specifications.

Click on :code:`Save recipe….` This will also let you rename the mosaic if you choose.

.. figure:: ../_images/workflows/area_estimation/save_duplicate_export_recipe.png
    :alt: Save, duplicate, export recipe menu.
    :align: center

Now if you click on the three lines icon, you should see an additional option: **Revert to old revision...**

.. figure:: ../_images/workflows/area_estimation/revert_to_old_revision.png
    :alt: After saving the menu adds a revert to old revision option.
    :align: center

Clicking on this option brings up a list of auto-saved versions from SEPAL. You can use this to revert changes if you make a mistake.


.. tip::

    Now, when you open SEPAL and click the Search option, you will see a row with this name that contains the parameters you just set.

.. figure:: ../_images/workflows/area_estimation/revision_menu.png
    :alt: Revisions menu dropdown.
    :align: center

Finally, we will save the mosaic itself. This is called ‘retrieving' the mosaic. This step is necessary to perform analysis on the imagery.

To download this imagery mosaic to your SEPAL account, click the :code:`Retrieve` button.

.. figure:: ../_images/workflows/area_estimation/retrieve.png
    :alt: The retrieve button.
    :align: center

.. figure:: ../_images/workflows/area_estimation/retrieve_menu.png
    :alt: The retrieve menu
    :align: center

A window will appear with the following options:

-   **Bands to Retrieve:** select the desired bands you would like to include in the download.

    -   Select the **Blue, Green, Red, NIR, SWIR 1 and SWIR 2** bands. These are visible spectrum and infrared data collected by Landsat.
    -   Other bands that are available include Aerosol, Thermal, Brightness, Greenness, and Wetness. More information on these can be found at: https://landsat.gsfc.nasa.gov/landsat-data-continuity-mission/.
    -   Metadata on Date, Day of Year, and Days from Target can also be selected.

-   **Scale:** the resolution of the mosaic. Landsat data is collected at 30m resolution, so we will leave the slider there.
-   **Retrieve to:** Sepal Workspace is the default option. Other options may appear depending on your permissions.

When you have the desired bands selected, click :code:`Retrieve`.

You will notice the :code:`Tasks` icon is now spinning. If you click on it, you will see the data retrieval is in process. This step will take some time.

.. figure:: ../_images/workflows/area_estimation/retrieval_task.png
   :alt: Retrieval task being carried out
   :align: center

.. note::
   This will take around **25 minutes** to finish downloading, however, you can move on to the next exercise without waiting for the download to finish.

.. _module 2:

Image classification
--------------------

The main goal of this Module is to construct a single-date land cover map by classification of a Landsat composite generated from Landsat images. Image classification is frequently used to map land cover, describing what the landscape is composed of (grass, trees, water, impervious surface), and to map land use, describing the organization of human systems on the landscape (farms, cities, wilderness). Learning to do image classification well is extremely important and requires experience. So here is your chance to build some experience. You will first consider the types of land cover classes you would like to map and the amount of variability within each class.

There are both supervised (uses human guidance including training data) and unsupervised (no human guidance) classification methods. The random forest approach used here uses training data and is thus a supervised classification method.

There are a number of supervised classification algorithms that can be used to assign the pixels in the image to the various map classes. One way of performing a supervised classification is to utilize a Machine Learning algorithm. Machine Learning algorithms utilize training data combined with image values to learn how to classify pixels. Using manually collected training data, these algorithms can train a classifier, and then use the relationships identified in the training process to classify the rest of the pixels in the map. The selection of image values (e.g., NDVI, elevation, etc.) used to train any statistical model should be well thought out and informed by your knowledge of the phenomenon of interest to classify your data (e.g., into forest, water, other, and clouds).

In this module, we will create a land cover map using supervised classification in SEPAL. We will train a random forest machine learning algorithm to predict land cover with a user generated reference data set. This data set is collected either in the field or manually through examination of remotely sensed data sources such as aerial imagery. The resulting model is then applied across the landscape. You will complete an accuracy assessment of the map output in `module 4`_.

Before starting your classification, you will need to create a response design with details about each of the land covers / land uses that you want to classify (Exercise 2.1); create mosaics for your area of interest (in `section 2.2`_ we will use a region of Brazil); and collect training data for the model (Exercise 2.3). Then, in Exercise 2.4 we will run the classification and examine our results.

The workflow in this module has been adapted from exercises and material developed by Dr. Pontus Olofsson, Christopher E. Holden, and Eric L. Bullock at the Boston Education in Earth Observation Data Analysis in the Department of Earth & Environment, Boston University. To learn more about their materials and their work, visit their GitHub site at https://github.com/beeoda.

At the end of this module you will have a classified land use land cover map.

.. note::

    This section takes approximately 4 hours to complete.


.. _section 2.1:

Response design for classification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating consistent labeling protocols is necessary for creating accurate training data and later, accurate sample based estimates (see `module 4`_). They are especially important when more than one researcher is working on a project and for reproducible data collection. Response design helps a user assign a land cover / land use class to a spatial point. The response design is part of the metadata for the assessment and should contain the information necessary to reproduce the data collection. The response design lays out an objective procedure that interpreters can follow and that reduces interpreter bias.

In this exercise, you will build a decision tree for your classification along with much of the other documentation and decision points (for more on decision points, please see `section 5.1`_).

.. note::

    **objective**: Learn how to create a classification scheme for land cover land use classification mapping.


Specify the classification scheme
"""""""""""""""""""""""""""""""""

“Classification scheme” is the name used to describe the land cover and land use classes adopted. It should cover all of the possible classes that occur in the area of interest. Here, you will create a classification scheme with detailed definitions of the land cover and land use classes to share with interpreters.

Create a decision tree for your land cover or land use classes. There may be one already in use by your department. The tree should capture the most important classifications for your study. Here is an example:

-   This example includes a hierarchical component. For example, the green and red categories have multiple sub-categories, which might be multiple types of forest or crops or urban areas. You can also have classification schemes that are all one level with no hierarchical component.
-   For this Exercise, we'll use a simplified land cover and land use classification as in this graph:

.. graphviz::

    digraph process {
           lc [label="Land cover", shape=box];
           f [label="Forest", shape=box, style="filled" color="darkgreen"];
           nf [label="Non forest", shape=box, style="filled", color="grey"];
           lc -> f;
           lc -> nf;
        }

When creating your own decision tree, be sure to specify if your classification scheme was derived from a template, including the IPCC (Intergovernmental Panel on Climate Change) land-use categories, CLC (CORINE land cover), or LUCAS (land cover and land use, landscape).

-   If applicable, your classification scheme should be consistent with the national land cover and land use definitions.
-   In cases where the classification scheme definition is different from the national definition, you will need to provide a reason.

Create a detailed definition for each land cover and land use and change class included in the classification scheme. We recommend you include measurable thresholds.

Our classification will take place in Brazil, in an area of the Amazon rainforest undergoing deforestation.

-   We'll define Forest as an area with over 70% tree cover.
    ii. We'll define Non-forest as areas with less than 70% tree cover. This will capture urban areas, water, and agricultural fields.

-   For creating your own classifications, here's some things to keep in mind:

    -   It is important to have definitions for each of the classes. A lack of clear definitions of the land cover classes can make the quality of the resulting maps difficult to assess, and challenging for others to use. The definitions you come up with now will probably be working definitions that you find you need to modify as you move through the land cover classification process.

    .. note::

        As you become more familiar with the landscape, data limitations, and the ability of the land cover classification methods to discriminate some classes better than others, you will undoubtedly need to update your definitions.

    -   As you develop your definitions, you should be relating back to your applications. Make sure that your definitions meet your project objectives. For example, if you are creating a map to be used as part of your UNFCCC greenhouse gas reporting documents you will need to make sure that your definition of forest meets the needs of this application.

    .. note::

        The above land cover tree is an excerpt of text from the Methods and Guidance from the Global Forest Observations Initiative (GFOI) document that describes the Intergovernmental Panel on Climate Change (IPCC) 2003 Good Practice Guidance (GPG) forest definition and suggestions to consider when drafting your forest definition. When creating your own decision tree, be sure to specify if your definitions follow a specific standard, e.g., using ISO standard Land Cover Meta-Language (LCML, ISO 19144-2) or similar.

    -   During this online training course, you will be mapping land cover across the landscape using the Landsat composite, a moderate resolution data set. You may develop definitions based upon your knowledge from the field or from investigating high resolution imagery. However, when deriving your land cover class definitions, it's also important to be aware of how the definitions relate to the data used to model the land cover.

    .. note::

        You will continue to explore this relationship throughout the exercise. Will the spectral signatures between your land cover categories differ? If the spectral signatures are not substantially different between classes, is there additional data you can use to differentiate these categories? If not, you might consider modifying your definitions.

More resources are available online, for example at http://www.ipcc.ch/ipccreports/tar/wg2/index.php?idp=132.

.. _section 2.2:

Create a mosaic for classification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We first need an image to classify before running a classification. For best results, we will need to create an optical mosaic with good coverage of our study area. We will build on knowledge gained in `module 1`_ to create an optical mosaic in SEPAL and retrieve it to Google Earth Engine.

In SEPAL you can run a classification on either a mosaic recipe or on a GEE asset. It is best practice to run a classification using an asset rather than on-the-fly with a recipe. This will improve how quickly your classification will export and avoid computational limitations.

.. note::

    **objectives**:

    -   Build on knowledge gained in `module 1`_
    -   Create a mosaic to be the basis for your classification

.. warning::

    **Prerequisit**: `module 1`_

Creating and exporting a mosaic for a drawn AOI
"""""""""""""""""""""""""""""""""""""""""""""""

We will create a mosaic for an area in the Amazon basin. If any of the steps for creating a mosaic are unfamiliar, please revisit `module 1`_.

Navigate to the Process tab, then create a new optical mosaic by selecting Optical Mosaic on the Process menu.
Under :code:`Area of Interest`:

-   Select **Draw Polygon** from the dropdown list.

    .. figure:: ../_images/workflows/area_estimation/aoi_dropdown.png
        :alt: Area of interest dropdown menu.
        :width: 450px
        :align: center

-   Navigate using the map to the State of Rondonia (Brazil) and either draw a polygon around it or draw a polygon within the borders. A smaller polygon will export faster.

    .. figure:: ../_images/workflows/area_estimation/rondonia.png
        :alt: A polygon drawn around the State of Rondonia.
        :align: center

Now use what you have learned in `module 1`_ to create a mosaic with imagery from the year 2019 (whole year or part of year, your choice).

.. tip::

    Don't forget to consider which satellites you would like to include and which scenes you would like to include (all, some).

Your preview should include imagery data across your entire area of interest. This is important for your classification. Try also to get a cloud-free mosaic, as this makes your classification easier.

Name your mosaic for easy retrieval. Try **Module2_Amazon**.

When you're satisfied with your mosaic, **Retrieve** it to Google Earth Engine. Be sure to include the red, green, blue, nir, swir1, and swir2 layers. You may choose to add the greenness, etc. layers as well.

Finding your Earth Engine Asset
"""""""""""""""""""""""""""""""

For future exercises, you may need to know how to find your Earth Engine Asset.

1.  Navigate to https://code.earthengine.google.com/ and login.
2.  Navigate to your **Assets** tab in the left hand column.
3.  Under **Assets,** look for the name of the mosaic you just exported.
4.  Click on the mosaic name.
5.  You will see a window with information about your mosaic pop up.
6.  Click on the two overlapping box icon to copy your asset's location.

.. figure:: ../_images/workflows/area_estimation/mosaic_information.png
    :alt: Your mosaic's information pane.
    :align: center

.. _section 2.3:

Creating a classification & training data collection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this exercise, we will learn how to start a classification process and collect training data. These training data points will become the foundation of the classification in `section 2.4`_. High quality training data is necessary to get good land cover map results. In the most ideal situation, training data is collected in the field by visiting each of the land cover types to be mapped and collecting attributes. When field collection is not an option, the second best choice is to digitize training data from high resolution imagery, or at the very least for the imagery to be classified.

In general, there are multiple pathways for collecting training data. Using desktop GIS, including QGIS and ArcGIS, to create a layer of points is one common approach. Using GEE is another approach. You can also use CEO to create a project of random points to identify (see detailed directions in `section 4.1.2`_). All of these pathways will create .csv or an GEE table that you can import into SEPAL to use as your training data set.

However, SEPAL has a built-in reference data collection tool in the classifier. In this exercise, we will use this tool to collect training data. Even if you use a .csv or GEE table in the future, this is a helpful feature to collect additional training data points to help refine your model.

In this assignment, you will create training data points using high-resolution imagery, including Planet NICFI data. These will be used to train the classifier in a supervised classification using SEPAL's random forests algorithm. The goal of training the classifier is to provide examples of the variety of spectral signatures associated with each class in the map.

.. note::

    **objectives**: Create training data for your classes that can be used to train a machine learning algorithm.

.. warning::

    **Prerequisites**:

    -   SEPAL account
    -   Land cover categories defined in `section 2.1`_.
    -   Mosaic created in `section 2.2`_

Set up your classification
""""""""""""""""""""""""""

In the **Process** menu, click the green plus symbol and select **Classification.**

Add the Amazon optical mosaic for classification:

-   Click :code:`+ Add` and choose either **Saved Sepal Recipe** or **Earth Engine Asset** (recommended).

    -   If you choose **Saved Sepal Recipe**, simply select your `module 2`_ Amazon recipe.
    -   If you choose **Earth Engine Asset**, enter the Earth Engine Asset ID for the mosaic. The ID should look like “users/username/Module2_Amazon”.

    .. tip::

        Remember that you can find the link to your Earth Engine Asset ID via Google Earth Engine's Asset tab (`section 2.2`_).

-   Select bands: Blue, Green, Red, NIR, SWIR1, & SWIR2. You can add other bands as well if you included them in your mosaic.
-   You can also include **Derived bands** by clicking on the green button on the lower left.
-   Click :code:`Apply`, then click :code:`Next`.

.. warning::

    Selecting **Saved Sepal Recipe** may cause the following error at the final stage of your classification:

    .. code-block:: console

        Google Earth Engine error: Failed to create preview

    This occurs because GEE gets overloaded. If you encounter this error, please retrieve your classification as described in `section 2.2`_.

In the Legend menu, click :code:`+ Add` This will add a place for you to write your first class label.

-   You will need two legend entries.
-   The first should have the number 1 and a Class label of Forest.
-   The second should have the number 2 and a Class  label of Non-forest.
-   Choose colors for each class as you see fit.
-   Click :code:`Close`.

.. figure:: ../_images/workflows/area_estimation/classification_legend.png
    :alt: Classification legend.
    :align: center

Collect training data points
""""""""""""""""""""""""""""

Now that you have created your classification, you are ready to begin collecting data points for each land cover class.

In most cases, it is ideal to collect a large amount of training data points for each class that capture the variability within each class and cover the different areas of the study area. However, for this exercise, you will only collect a small number of points: around 25 per class. When collecting data points, make sure that your plot contains only the land cover class of interest (no plots with a mixture of your land cover categories).

.. tip::

    To help you understand why the random forest algorithm might get some categories you are trying to map confused with others, you will use spectral signatures charts in CEO-SEPAL to look at the NDVI signature of your different land cover classes. You should notice a few things when exploring the spectral signatures of your land cover classes. First, some classes are more spectrally distinct than others. For example, water is consistently dark in the NIR and MIR wavelengths, and much darker than the other classes. This means that it shouldn't be difficult to separate water from the other land cover classes with high accuracy.

Not all pixels in the same classes have the exact same values—there is some natural variability! Capturing this variation will strongly influence the results of your classification.

First, let's become familiar with the SEPAL Interface. In the upper right corner of the map is a stack of three rectangles. If you mouse over this icon, it says "Select layers to view."

.. note::

    Available base layers include SEPAL (Minimal dark Sepal default layer), Google Satellite, and Planet NICFI composites.

We will use the Planet NICFI composites for this example. The composites are available in either RGB or false color infrared (CIR). Composites are available monthly after September 2020 and for every 6 months prior back till 2015.

-   Select RGB, Jun 2019 (6 months).

.. tip::

    You can also select "Show labels" to enable labels that can help you orient yourself in the landscape.

.. figure:: ../_images/workflows/area_estimation/layer_view.png
   :alt: The layers available.
   :align: center

Now click on the point icon. When you mouse over this icon, it says "Enable reference data collection."

With reference data collection enabled, you can start adding points to your map.

Use the scroll wheel on your mouse to zoom in to the study area. You can click-hold and drag to pan around the map. Be careful though, as a single click will place a point on the map.

.. tip::

    If you accidentally add a point, you can delete it by clicking on the red **Remove** button.

Now we will start collecting forest training data:

-   Zoom into an area that is clearly forested. When you find an area that is completely forested, click it once.
-   You have just placed a training data point!
-   Click the **Forest** button in the training data interface to classify the point.

.. tip::

    If you haven't classified the point yet, then you can just click somewhere else on the map instead of deleting the record.

.. figure:: ../_images/workflows/area_estimation/collecting_forest_data.png
    :alt: Collecting forest data in the SEPAL interface.
    :align: center

.. note::

   Ideally you should switch back to the Landsat mosaic to make sure that this forested area is not covered with a cloud. If you mistakenly classify a cloudy pixel as Forest, then the results will be impacted negatively if your Landsat mosaic does have cloud-covered areas.

   However, this interface does not allow for switching between the Base Layer imagery and your exported mosaic. If you are using another training data collection method, keep this point in mind.

If you need to modify classification of any of your data points, you can click on the point to return to the classification (or delete) options.

Begin collecting the rest of the 25 **Forest** training data points throughout other parts of the study area.

-   The study area contains an abundance of forested land, so it should be pretty easy to identify places that can be confidently classified as forest. If you'd like, use the charts function to ensure that there is a relatively high NDVI value for the point.
-   Ensure you are placing data points within the extent of the mosaic (Rondonia).

Collect about 25 points for the **Forest** land cover class.

.. warning::

    When you are done, zoom out to the full extent of the area. Did you place data points somewhat equally across the full region? Are all points clustered in the same region? It's best to make sure you have data points covering the full spatial extent of the study region, add more points in areas that are sparsely represented if needed.

After you collect your training data for **Forest**, you may see the classification preview appear.

-   To disable the classification preview to continue to collect training data, return to the map layer selector.
-   Uncheck the "Classification" Overlay.

.. figure:: ../_images/workflows/area_estimation/classification_overlay.png
    :alt: Disabling the classification overlay.
    :width: 450
    :align: center

Once you are satisfied with your forested training data points, move on to the **Non-Forest** training points.

-   Since we are using a very basic set of land cover classes for this exercise, this should include agricultural areas, water, and buildings and roads. Therefore, it will be important that you focus on collecting a variety of points from different types of land cover throughout the study area.
-   **Water** is one of the easiest classes to identify and the easiest to model, due to the distinct spectral signature of water.

    -   Look for water bodies within Rondonia.
    -   Collect 10-15 data points for Water and be sure to spread them throughout Lake Mai Ndombe, the water sources feeding into it, and a couple of the water bodies/rivers to the eastern side of the mosaic. Be sure to put 2-3 points on rivers.
    -   Some wetland areas may have varying amounts of water throughout the year, so it is important to check both Planet NICFI maps for 2019. (Jun 2019 and Dec 2019).

.. figure:: ../_images/workflows/area_estimation/data_points_water.png
   :alt: Collecting data points in water.
   :align: center

Let's now collect some building and road non-forest Training Data.

-   There are not very many residential areas in the region. However, if you look you can find homes with dirt roads, and there are some airports as well.
-   Place a point or points within these areas and classify them as Non-forest. Do your best to avoid placing the points over areas of the town with lots of trees.
-   Find some roads, and place points and classify as Non-forest. These may look like areas of bare soil. Both bare soil and roads are classified as Non-forest, so place some points on both.

.. figure:: ../_images/workflows/area_estimation/data_points_residential.png
   :alt: Collecting residential and other human settlement area data points.
   :align: center

Next, place several points in grassland/pasture, shrub, and agricultural areas around the study area.

-   Shrubs or small, non-forest vegetation can sometimes be hard to identify, even with high-resolution imagery. Do your best to find vegetation that is clearly not forest.
-   The texture of the vegetation is one of the best ways to differentiate between trees and grasses/shrubs. Look at the below image and notice the clear contrast between the area where the points are placed and the other areas in the image that have rougher textures and that create shadows.

.. figure:: ../_images/workflows/area_estimation/data_points_low_vegetation.png
   :alt: Collecting low vegetation data
   :align: center

.. note::
   If you are using QGIS etc. to collect training data, you should also collect **cloud** training data in the **Non-forest** class, if your Landsat has any clouds. If there are some clouds that were not removed during the Landsat mosaic creation process you will need to create training data for the clouds that remain so that the classifier knows what those pixels represent. Sometimes clouds were detected during the mosaic process and were mostly removed. However, you can see some of the edges of those clouds remain.

   Note that you may not have any clouds in your Landsat imagery.

Continue collecting Non-forest points. Again, be sure to spread the points out across the study area.

Once again when you are done collecting data for these categories, zoom out to the full extent of the study region.

-   Did you place data points somewhat equally across the full region?
-   Are all points clustered in the same area?
-   It's best to make sure you have data points covering the full spatial extent of the study region, add more points in areas that are sparsely represented if needed.

.. _section 2.4:

Classification using machine learning algorithms (Random Forests)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../_images/workflows/area_estimation/random_forest_model_outcome.png
   :alt: The outcome of a random forest model.
   :align: center

As mentioned in the Module introduction, the classification algorithm you will be using today is called random forest.  The random forest algorithm creates numerous decision trees for each pixel. Each of these decision trees votes on what the pixel should be classified as. The land cover class that receives the most votes is then assigned as the map class for that pixel. Random forests are efficient on large data and accurate when compared to other classification algorithms.

To complete the classification of our mosaicked image you are going to use a random forests classifier contained within the easy-to-use Classification tool in SEPAL. The image values used to train the model include the Landsat mosaic values and some derivatives, if selected (such as NDVI). There are likely additional data sets that can be used to help differentiate land cover classes, such as elevation data.

After we create the map, you might find that there are some areas that are not classifying well. The classification process is iterative, and there are ways you can modify the process to get better results. One way is to collect more or better reference data to train the model. You can test different classification algorithms, or explore object based approaches opposed to pixel based approaches. The possibilities are many and should relate back to the nature of the classes you hope to map. Last but certainly not least is to improve the quality of your training data. Be sure to log all of these decision points in order to recreate your analysis in the future.

.. note::

    **objective**: Run SEPAL's classification tool.

.. warning::

    **prerequisites**:

    -   Land cover categories defined in `section 2.1`_
    -   Mosaic created in `section 2.2`_
    -   Training data created in `section 2.3`_

Add training data collected outside of sepal
""""""""""""""""""""""""""""""""""""""""""""

.. note::

    This section is fully optional

If you collected training data using QGIS, CEO, or another pathway, you will need to add the Training Data we collected in `section 2.3`_ in the :code:`TRN` tab.

Click on the green :code:`Add` button.

-   Import your training data
    -   Upload a CSV file.
    -   Select Earth Engine Table and enter the path to your Earth Engine asset in the EE Table ID field.

-   Click :code:`Next`.
-   For **Location Type**, select "X/Y" coordinate columns" or "GEOJSON Column" depending on your data source. GEE assets will need the GEOJSON column option.
-   Click :code:`Next`.
-   Leave the **Row filter expression** blank. For **Class format**, select "Single Column" or "Column per class" as your data dictates.
-   In the **Class Column** field select the column name that is associated with the class.
-   Click :code:`Next`.

Now you will be asked to confirm the link between the legend you input previously and your classification. You should see a screen as follows. If you need to change anything, click the green plus buttons. Otherwise, click :code:`Done`, then click :code:`Close`.

.. figure:: ../_images/workflows/area_estimation/link.png
   :alt: link between legend and classification
   :align: center

Review additional classification options
""""""""""""""""""""""""""""""""""""""""

Click on :code:`AUX` to examine the auxiliary data sources available for the classification.

Auxiliary inputs are optional layers which can be added to help aid the classification. There are three additional sources available:
-   Latitude: Includes the latitude of each pixel
-   Terrain: Includes elevation of each pixel from SRTM data
-   Water: Includes information from the JRC Global Surface water Mapping layers

Click on :code:`Water` and :code:`Terrain` and then :code:`Apply`.

Click on **CLS** to examine the classifier being used.

-   The default is a random forest with 25 trees.
-   Other options include classification and regression trees (CART), Naive Bayes, support vector machine (SVM), minimum distance, and decision trees (requires a CSV).
-   Additional parameters for each of these can be specified by clicking on the **More** button in the lower left.
-   For this example, we will use the default random forest with 25 trees.

If you turned off your classification preview previously to collect training data, now is the time to turn it back on.

-   Click on the "Select layers to show" icon.
-   Select "Classification"
-   Make sure Classification now has a check mark next to it, indicating that the layer is now turned on.

.. figure:: ../_images/workflows/area_estimation/classification_preview.png
    :alt: A preview of a classification.
    :align: center

Now we'll save our classification output.

-   First, rename your classification by typing a new name in the tab.
-   Click :code:`Retrieve classification` in the upper right hand corner (cloud icon).
-   Choose **30 m** resolution.
-   Select the Class, Class probability, Forest % and Non-forest % bands.
-   Retrieve to your **SEPAL Workspace.**
    .. note::

        You can also choose **Google Earth Engine Asset** if you would like to be able to share your results or perform additional analysis in GEE. However with this option, you will need to download your map from GEE using the Export function.

-   Once the download begins, you will see the spinning wheel in the bottom left of the web-page in **Tasks.** Click the spinning wheel to observe the progress of your export.
-   When complete, if you chose SEPAL workspace, the file will be in your SEPAL downloads folder. (Browse > downloads > classification name folder). If you chose GEE Asset the file will be in your GEE Assets.

.. figure:: ../_images/workflows/area_estimation/retrieval_interface.png
    :alt: The retrieval interface.
    :width: 450
    :align: center

QA/QC considerations and methods
""""""""""""""""""""""""""""""""

Quality assurance and quality control, commonly referred to as QA/QC, is a critical part of any analysis. There are two approaches to QA/QC: formal and informal. Formal QA/QC, specifically sample-based estimates of error and area are described in `module 4`_. Informal QA/QC involves qualitative approaches to identifying problems with your analysis and classifications to iterate and create improved classifications. Here we'll discuss one approach to informal QA/QC.

Following analysis you should spend some time looking at your change detection in order to understand if the results make sense. We'll do this in the classification window. This allows us to visualize the data and collect additional training points if we find areas of poor classification. Other approaches not covered here include visualizing the data in Google Earth Engine or in another program, such as QGIS or ArcMAP.

With SEPAL you can examine your classification and collect additional training data to improve the classification.

.. figure:: ../_images/workflows/area_estimation/examine_classification_map.png
    :alt: Examining your change detection map
    :align: center

Turn on the imagery for your Classification and pan and zoom around the map. Compare your Classification map to the 2015 and 2020 imagery. Where do you see areas that are correct? Where do you see areas that are incorrect? If your results make sense, and you are happy with them, great! Go on to the formal QA/QC in `module 4`_.

.. warning::

    if you are not satisfied, collect additional points of training data where you see inaccuracies. Then re-export the classification following the steps in `section 2.3`_.

.. _module 3:

Image change detection
----------------------

Image change detection allows us to understand differences in the landscape--or more correctly, in the satellite images taken of the landscape--over time. There are many questions that change detection methods can help answer, including “When did deforestation take place?” and “How much forest area has been converted to agriculture in the past 5 years?”

Most methods for change detection use algorithms backed by statistical methods to extract and compare information in the satellite images. To conduct change detection then, we need multiple mosaics or images, each one representing a point in time. Here, we will describe how to detect change between two dates using a simple model, however this theory can be expanded to include more dates. In addition, we'll describe time series analysis, which generally looks at longer periods of time.

The objective of this module is to become associated with methods of detecting change for an area of interest using the SEPAL platform. This will build upon and incorporate what we have covered in the previous modules including: creating mosaics, creating training samples, and classifying imagery. This module is split into two exercises. The first addresses change detection using two dates, and the second more advanced methods using time series analysis with the BFAST algorithm and LandTrendr. At the end of this module you will know how to conduct a two-date change detection in SEPAL, have a basic understanding of the BFAST tool in SEPAL, and be familiar with TimeSync and LandTrendr.

This module should take you approximately 3 hours.

.. _section 3.1:

Two date change detection
^^^^^^^^^^^^^^^^^^^^^^^^^

In this Exercise, you will learn how to conduct a two-date change detection in SEPAL. This approach uses the same classification algorithm you used in `module 2`_. This approach can be used with more than two dates if you so choose in the future.

In this example, you will create optical mosaics and classify them, building on skills learned in Modules 1 and 2. Alternatively, you may also use two classifications from your own research area.

.. note::

    **objectives**:

    -   Learn how to conduct a two-date change detection
    -   Build on skills learned in `module 1`_ & `module 2`_

.. warning::

    **Prerequisites**:

    -   SEPAL account
    -   Complete `module 1`_ & `module 2`_ or be familiar with the skills covered

Create mosaics for change detection
"""""""""""""""""""""""""""""""""""

Before we can identify change, we first need to have images to compare. We will create two mosaics of Sri Lanka, generate some training data, and then classify the mosaics. This is discussed in detail in `module 1`_ & `module 2`_.

Open the :code:`Process` menu and click on :code:`Optical mosaic`. Alternatively click the **green plus symbol** to open the **Create Recipe** menu and then click on :code:`Optical Mosaic`.

use the following data:

-   Choose **Sri Lanka** for the Area of interest (AOI).
-   Select 2015 for the Date (DAT).
-   Select Landsat 8 (L8) as the source (SRC).
-   In the Composite (CMP) menu, ensure the surface reflectance **(SR) correction** is selected and median is the compositing method.

Click :code:`Retrieve Mosaic` and select **Blue, Green, Red, NIR, SWIR1, SWIR2**. Then select Google Earth Engine Asset, and lastly click :code:`retrieve`.

.. note::

   If you don't see the Google Earth Engine asset option, you'll need to connect your Google account to SEPAL by clicking on your user name in the lower right.

.. figure:: ../_images/workflows/area_estimation/retrieval_mosaic.png
   :alt: The retrieval screen for mosaics.
   :width: 450
   :align: center

Repeat previous steps but change the **Date** parameter to 2020.

.. note::

   It may take a significant amount of time before your mosaics finish exporting.

Start the classification
""""""""""""""""""""""""

Now we will begin the classification, as we did in `module 2`_. There are multiple pathways for collecting training data. Using desktop GIS, including QGIS and ArcGIS, to create a layer of points is one common approach. Using GEE is another approach. You can also use CEO to create a project of random points to identify (see detailed directions in `section 4.1.2`_). All of these pathways will create .csv or an GEE table that you can import into SEPAL to use as your training data set.

However, SEPAL has a built-in reference data collection tool in the classifier. This is the tool you used in `module 2`_, and we will again use this tool to collect training data. Even if you use a .csv or GEE table in the future, this is a helpful feature to collect additional training data points to help refine your model.

In the **Process** menu, click the green plus symbol and select :code:`Classification`.
Add the two Sri Lanka optical mosaics for classification by clicking **+ Add** and choose either **Saved Sepal Recipe** or **Earth Engine Asset** (recommended).

-   If you choose **Saved Sepal Recipe**, simply select your `module 2`_ Amazon recipe.
-   If you choose **Earth Engine Asset**, enter the Earth Engine Asset ID for the mosaic. The ID should look like “users/username/SriLanka2015”.

.. tip::

    Remember that you can find the link to your Earth Engine Asset ID via Google Earth Engine's Asset tab (see **Exercise 2.2 Part 2**).

Select bands: Blue, Green, Red, NIR, SWIR1, & SWIR2. You can add other bands as well if you included them in your mosaic. You can also include **Derived bands** by clicking on the green button on the lower left and then click :code:`Apply`.

Repeat the previous steps for your 2020 optical mosaic.

.. figure:: ../_images/workflows/area_estimation/two_assets.png
   :alt: Two assets ready for classification.
   :align: center

.. warning::

    Selecting **Saved Sepal Recipe** may cause the following error at the final stage of your classification:

    .. code-block:: console

        Google Earth Engine error: Failed to create preview

    This occurs because GEE gets overloaded. If you encounter this error, please retrieve your classification as described in `section 2.2`_.

.. _section 3.1.3:

Collect change classification training data
"""""""""""""""""""""""""""""""""""""""""""

Now that we have the mosaics created, we will collect change training data. While more complex systems can be used, we will consider two land cover classes that each pixel can be in 2015 or 2020: forest and non-forest. Thinking about change detection, we will use three options: stable forest, stable non-forest, and change. That is, between 2015 and 2020 there are four pathways: a pixel can be forest in 2015 and in 2020 (stable forest); a pixel can be non-forest in 2015 and in 2020 (stable non-forest); or it can change from forest to non-forest or from non-forest to forest. If you use this manual to guide your own change classification, remember to log your decisions including how you are thinking about change detection (what classes can change and how), and the imagery and other settings used for your classification.

.. graphviz::

    digraph G {
        rankdir=LR;
        subgraph cluster0 {
            node [style=filled, shape=box];
            a0 [label="Non-forest", color=lightgrey];
            a1 [label="Forest", color=darkgreen];
            label = "2015";
        }
        subgraph cluster1 {
            node [style=filled, shape=box];
            b0 [label="Non-forest", color=lightgrey];
            b1 [label="Forest", color=darkgreen];
            label = "2018";
        }
        a0 -> b0 [color=grey];
        a1 -> b1 [color=darkgreen];
        a1 -> b0 [color=orange];
        a0 -> b1 [color=orange];

    }


In the Legend menu, click :code:`+ Add`. This will add a place for you to write your first class label. You will need three legend entries:

-   The first should have the number 1 and a Class label of Forest.
-   The second should have the number 2 and a Class  label of Non-forest.
-   The third should have the number 3 and a Class label of Change.

Choose colors for each class as you see fit and click :code:`Close`.

.. figure:: ../_images/workflows/area_estimation/3_classes.png
    :alt: Classification legend.
    :align: center

Now, we'll create training data. First, let's pull up the correct imagery. Click on "Select layers to view". As a reminder, available base layers include:
-   SEPAL (Minimal dark Sepal default layer)
-   Google Satellite
-   Planet NICFI composites

We will use the Planet NICFI composites for this example. The composites are available in either RGB or false color infrared (CIR). Composites are available monthly after September 2020 and for every 6 months prior back till 2015. Select Dec 2015 (6 months). Both RGB and CIR will be useful, so choose whichever you prefer. You can also select "Show labels" to enable labels that can help you orient yourself in the landscape. You will need to switch between this **Dec 2015** data and the **Dec 2020** data to find stable areas and changed areas.

.. note::

   If you have collected data in QGIS, CEO, or another program, you can skip the following steps. Simply click on **TRN** in the lower right. Click **+ Add** then upload your data to SEPAL. Finally click on the **CLS** button in the bottom right and you can skip to `section 3.1.4`_


Now click on the point icon. When you mouse over this icon, it says "Enable reference data collection".

With reference data collection enabled, you can start adding points to your map.

Use the scroll wheel on your mouse to zoom in to the study area. You can click-hold and drag to pan around the map. Be careful though, as a single click will place a point on the map.

.. tip::

   If you accidentally add a point, you can delete it by clicking on the red :code:`Remove` button.

Collect training data for the "Stable Forest" class. Place points where there is forest in both 2015 and 2020 imagery.Then collect training data for the "Stable Non-forest" class. Place points where there is not forest in either 2015 or 2020. You should include water, built up areas, bare dirt, and agricultural areas in your points. Finally collect training data for the "Change" class.

.. tip::

    If you are having a hard time finding areas of change several tools can help you:

    -   you can use the Google satellite imagery to help. Areas of forest loss often appear as black or dark purple patches on the landscape. Be sure to always check the 2015 and 2020 Planet imagery to verify Change.
    - The CIR (false color infrared) imagery from Planet can also be helpful in identifying areas of change.
    - You can also use SEPAL's on-the-fly classification to help after collecting a few Change points.
        -   If the classification does not appear after collecting the Stable Forest and Stable Non-forest classes, click on the "Select layers to view" icon.
        -   Toggle the "Classification" option off, and then on again.
        -   You may need to click on "CLS" on the bottom right of the screen, then click "Close" to get the classification map to appear.
        -   With the Classification map created, you can find change pixels and confirm whether they are change or not by comparing 2015 and 2020 imagery.

One trick for determining change is to place a "Change" point in an area of suspected change. Then you can compare 2015 and 2020 imagery without losing the place you were looking at. If it is not Change, you can switch which classification you have identified the point as.

.. figure:: ../_images/workflows/area_estimation/finding_change.png
   :alt: Using Google imagery to examine areas for change.
   :align: center

Continue collecting points until you have approximately 25 points for Forest and Non-forest classes and about 5 points for the Change class. More is better. Try to have your points are spread out across Sri Lanka.

If you need to modify classification of any of your data points, you can click on the point to return to the classification options. You can also remove the point in this way.

When you are happy with your data points, click on the :code:`AUX` button in the bottom right. Select **Terrain** and **Water**. This will add auxiliary data to the classification.

Finally click on the :code:`CLS` button in the bottom right. You can change your classification type to see how the output changes.
8. If it has not already, SEPAL will now load a preview of your classification.

.. figure:: ../_images/workflows/area_estimation/change_detection_model_preview.png
    :alt: A preview of the change detection model output.
    :width: 450
    :align: center

.. note::

   If any of the previous sections is unclear, review `module 1`_ or `module 2`_ for more detailed explanations of how to process mosaics, and collect training data with CEO.

.. _section 3.1.4:

Two date classification retrieval
"""""""""""""""""""""""""""""""""

Now that the hard work of setting up the mosaics and creating and adding the training data is complete, all that is left to do is retrieve the classification.

To retrieve your classification, click the cloud icon in the upper right to open the **Retrieve** panel.

-   Select **Google Earth Engine Asset** if you would like to share your map or if you would like to use it for further analysis
-   Select **SEPAL Workspace** if you would like to use the map internally only.

Then use the following parameters:
- **resolution**: 30 m resolution
- **Selected bands**:  the Class, Class probability, Forest % and Non-forest % bands.


Finally click :code:`Retrieve`.

Quality assurance and quality control
"""""""""""""""""""""""""""""""""""""

Quality assurance and quality control, commonly referred to as QA/QC, is a critical part of any analysis. There are two approaches to QA/QC: formal and informal. Formal QA/QC, specifically sample-based estimates of error and area are described in `module 4`_. Informal QA/QC involves qualitative approaches to identifying problems with your analysis and classifications to iterate and create improved classifications. Here we'll discuss one approach to informal QA/QC.

Following analysis you should spend some time looking at your change detection in order to understand if the results make sense. This allows us to visualize the data and collect additional training points if we find areas of poor classification. Other approaches not covered here include visualizing the data in Google Earth Engine or in another program, such as QGIS or ArcMAP.

With SEPAL you can examine your classification and collect additional training data to improve the classification.

.. figure:: ../_images/workflows/area_estimation/examine_change_detection_map.png
   :alt: Examining your change detection map
   :align: center

Turn on the imagery for your Classification and pan and zoom around the map.
Compare your Classification map to the 2015 and 2020 imagery. Where do you see areas that are correct? Where do you see areas that are incorrect?
If your results make sense, and you are happy with them, great! Go on to the formal QA/QC in `module 4`_.

.. note::

    However, if you are not satisfied, collect additional points of training data where you see inaccuracies. Then re-export the classification following the steps in `section 3.1.3`_.

Deforest Tool
^^^^^^^^^^^^^

The DEnse FOREst Time Series (deforest) tool is a method for detecting changes in forest cover in a time series of Earth observation data. As input it takes a time series of forest probability measurements, producing a map of deforestation and an 'early warning' map of unconfirmed changes. The method is based on the 'Baysian time series' approach of `Reiche et al. (2018) <https://www.sciencedirect.com/science/article/abs/pii/S0034425717304959?via%3Dihub>`_.

The tool was designed as part of the Satellite Monitoring for Forest Management (SMFM) project. The SMFM project (2017 - 2020) aimed to address global challenges relating to the monitoring of tropical dry forest ecosystems, and was conducted in partnership with teams in Mozambique, Namibia and Zambia. For more informaton, see https://www.smfm-project.com/.

Full documentation is hosted at http://deforest.rtfd.io/.

This module should take you approximately 1-2 hours.


Data preparation
""""""""""""""""

For this exercise we will be using the sample data that is included with the tool. Additionally, instructions are given on how to create an time serries of forest probability using tools with the SEPAL platform.

.. csv-table::
    :header: "Objectives","Prerequisites"
    :widths: 20, 20

    "Learn how to use the SMFM Deforest tool", "SEPAL account"
    "","Completed SEPAL modules on mosaics, classification, & time series"

(Optional) Jupyter notebook basics
""""""""""""""""""""""""""""""""""

If you are unfamiliar with Jupyter notebooks this section is meant to get you aquatinted enough with the system to successfully run the SMFM Deforest tool. A notebook is significantly different than most SEPAL applications, but they are a powerful tool used in data science and other disciplines.

1. Cells

    Every notebook is broken into *cells*. Cells can come in a few formats, but typically they will be either **markdown** or **code**. Markdown cells are the descriptive text and images that accompany the coded to help a user understand the context and what the code is doing. Conversely, code cells run code or a system operation. There are many different languages which can be used in a Jupyter notebook. For this tool we will be using Python. 


.. figure:: ../_images/workflows/area_estimation/smfm_notebook_cell.png
    :alt: Example of a Jupyter Notebook cell.
    :width: 450
    :align: center



2. Running cells
    
    To run a cell, click on the cell then locate and click the *Run* button in the upper menu. You can run a cell more quickly using the keyboard shortcut **shift-enter**.


.. figure:: ../_images/workflows/area_estimation/smfm_notebook_run.png
    :alt: Example running a Jupyter Notebook cell.
    :width: 450
    :align: center


3. Kernel
    
    The kernel is the computation engine that executes the code in the jupyter notebook. In this case it is a python 3 kernel. For this tutorial you do not need to know much about this, but if you notebook freezes or you need to reset for any reason you can find kernel operations on the tool bar menu.

    Restarting the kernel:
        a. Navigate to the tool bar at the top of the notebook and select *Kernel*.
        b. From the dropdown menu, select *restart Kernel and Clear Outputs*

.. figure:: ../_images/workflows/area_estimation/smfm_notebook_kernel.png
    :alt: Example restarting Jupyter Notebook kernel.
    :width: 450
    :align: center


Preparing you data
""""""""""""""""""

For this exercise we will be using the sample data that is included with the tool. Additionally, instructions are given on how to create an time series of forest probability using tools with the SEPAL platform.

.. warning::
    SMFM Deforest is still in the process of being adapted for use on SEPAL. The forest probability time series will be derived from existing methods to produce a satellite time series implemented on SEPAL. 


This tutorial will use the demo data that is packaged with the SMFM Deforest tool, but steps are presented on how to use the current SEPAL implementation with the tool. Note though, that the data preparation steps in SEPAL can take many hours to complete. If you are unfamiliar with any of the preparations steps, please consult the relevant modules.

If you already have a time series of percent forest coverage feel free to use that.
    
A. Download demo data

   1. Navigate to your SEPAL **Terminal**.
   2. Start a new instance or  join your current instance.
   3. Clone the deforest Github repository to your SEPAL account using the following command.
   
   ``` git clone https://github.com/smfm-project/deforest ``` 
   
B. Use SEPAL workflow to generate time series of forest probability images

   1. Create an optical mosaic for your area of interest using the Process tab Optical Mosaic process. If this is unfamiliar to you, please see the tutorials here on OpenMRV under process "Mosaic generation with SEPAL".

   2. Save the mosaic as a recipe.

   3. Open a new classification and point to the optical mosaic recipe as the image to classify. Use the Process tab Classification process. If this is unfamiliar to you, please see the tutorials here on OpenMRV under process "Classification".   

      1. Select the bands you want to include in the classification.
      2. Add forest/non-forest training data.
 
         1. Sample points directly in SEPAL.
         2. Optionally, use Earth Engine asset. 
   
      3. Apply the classifier.
      4. Select the **%forest output**.
      5. Save the classification as a recipe.
   
   1. Open a new time-series

      1.  Select the same area of interest as your mosaic. 
      2.  Choose a date range for the time series.
      3.  In the 'SRC' box select satellites you used in the previous steps and the classification to apply.
      4.  Then you can download the time series to your SEPAL workspace.

.. note::
   It will take many hours to download the classified time series to your account depending upon how large your area of interest is.

Setup
"""""

Navigate to the **Apps** menu by clicking on the wrench icon and typing "SMFM" into the search field. Select "SMFM Deforest".

.. note::
   Sometimes the tool takes a few minutes to load. Wait until you see the tool's interface. In case the tool fails to load properly, please close the tab and repeat the above steps. If this does not work, reload SEPAL.

1. Click and run the first cell under the **Setup** header. This cell runs two commands, the first installs the deforest Python module and the second runs the **--help** switch to display some documentation on running the tool.
   
   1. If the help text is output beneath the cell, move onto the 3rd step. If there is an error, continue to step 2. The error message might say:
   
``` python3: can't open file '/home/username/deforest/sepal/change.py': [Errno 2] No such file or directory ```

.. figure:: ../_images/workflows/area_estimation/smfm_notebook_1_setup.png
    :alt: Successful setup.
    :width: 450
    :align: center

    Successful setup.

2. Install the package via the SEPAL Terminal
   
   1. Navigate to your SEPAL **Terminal**.
   2. Type *1* to access the terminal of session #1. You can think of a session as an instance of a virtual machine that is connected to your SEPAL account. 
   3. Clone the deforest github repository to your SEPAL account.
      
      .. code-block:: console
      
          git clone https://github.com/smfm-project/deforest
          
   4. Return to the SMFM notebook and repeat step 1.

.. figure:: ../_images/workflows/area_estimation/smfm_clone_deforest.png
    :alt: Cloning a repository via the SEPAL terminal.
    :width: 450
    :align: center

3. Once you have successfully set up the tool, take a moment to read through the help document of the deforest tool that is output below the Jupyter notebook cell you just ran. In the next part we will explain in more detail some of the parameters.

Process the time series
"""""""""""""""""""""""

Processing the time series imagery can be done with a single line of code using the Deforest change.py command line interface.

1. To use the demo imagery, you do not need to change any of the inputs. However, if you are using a custom time series you will need to make some modifications. To change the command to point to a custom time series of percent forest images you will need to update the path to your time series.
Original::

   !python3 ~/deforest/sepal/change.py ~/deforest/sepal/example_data/Time_series_2021-03-24_10-53-03/0/ -o ~/ -n sampleOutput -d 12-01 04-30 -t 0.999 -s 6000 -v

Example path to time series updated::

   !python3 ~/deforest/sepal/change.py  ~/downloads/PATH_TO_TIME_SERIES/0/ -o ~/ -n sampleOutputT -d 12-01 01-08 -t 0.999 -s 6000 -v


.. note::
   By default the time series should be downloaded to a **downloads** folder in your home directory and should have another folder in it named **0**.

1. Parameters

.. csv-table::
   :header: "Name","Switch","Description"
   :widths: 10, 10, 20

   "Output location","-o","output location where images will be saved on SEPAL account"
   "Output name","-n","Output file name prefix"
   "Date range","-d","A date range filter. Dates need to be formatted as '-d MM-DD MM-DD' "
   "Threshold","-t","Set a threshold probability to identify deforestation (between 0 and 1). High thresholds are more strict in the identification of deforestation. Defaults to 0.99."
   "Scale","-s","Scale inputs by a factor of 6000. In a full-scale run this should be set to 10000, here it's used to correct an inadequate classification."
   "Verbose","-v","Prints information to the console as the tool is run."

If you would like to use a time frame other than the example, update the **date range** switch. 


3. Run the **Process the time series** cell.

   1. By default the tool is set to use verbose (-v) output. With this option, as each image is processed a message will be printed to inform us of the progress.

   This cell runs two commands:
      a. The first line is running the SMFM Deforest change detection algorithm (change.py).
      b. After processing the images we print them out to ensure the program runs successfully.

   .. note::
      The exclamation mark (**!**) is used to run commands using the underlying operating system. When we run *!ls* in the notebook it is the same as running *ls* in the terminal.

   The output deforestation image will be saved to the home directory of SEPAL account(home/username) by default. If you want to save your images in a different location it can be changed by adding the new path after the **-o** switch.

   2. (Optional) Download outputs to local computer
   
      1. Navigate to the *Files* section of your SEPAL account.
      2. Locate the output image to download and click to select it. In this case the image is named *sampleOutput_confirmed*.
      3. Click the download icon.

Data visualization
""""""""""""""""""

Now that we have run the deforestation processing chain, we can visualize our output maps. The outputs of the SMFM tool are two images **confirmed** and **warning**. We will look at the confirmed image first.

1. Run the first **Data visualization** cell of the Jupyter notebook.

   a. If you changed the name of your output file be sure to update the path on line 8 for the variable *confirmed*.


    .. figure:: ../_images/workflows/area_estimation/smfm_confirmations.png
        :alt: Example of a Jupyter Notebook cell.
        :width: 450
        :align: center

    
   The confirmed image shows the years of change that have been detected in the time series. Stable forest is colored green, non forest is colored yellow, and the change years colored by a blue gradient. 

   It is recommended that the user discards the first 2-3 years of change, or uses a very high quality forest baseline map to mask out locations that weren't forest at the start of the time series. This is needed since our input imagery is a forest probability time series which initially considers the landscape as forest.

Next, we will check out the deforest warning output.

1. Run the second **Data visualization** cell
    
    .. figure:: ../_images/workflows/area_estimation/smfm_warnings.png
        :alt: Example of a Jupyter Notebook cell.
        :width: 450
        :align: center

    
   This image shows the combined probability of non-forest existing at the end of our time series in locations that have not yet been flagged as deforested. This can be used to provide information on locations that have not yet reached the threshold for confirmed changes, but are looking likely to be possible. 
   
   You can view a demonstration of the above steps on `YouTube <https://youtu.be/9BswdPlncfM>`_.

Additional Resources
""""""""""""""""""""

-   Source code: The source code of the Deforest tool and Jupyter notebook can be found in the `GitHub repository <https://github.com/smfm-project/deforest>`_.
-   Bug report: in case you notice a bug or have issues using the tool, you can report an issue using the `Issues section <https://github.com/smfm-project/deforest/issues>`_ of the Github repository. This will take you to an issue creation page on the GitHub repository of the tool.

Other approaches to time series analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this exercise, you will learn more about time series analysis. SEPAL has the BFAST option, described first. We also provide information on TimeSync and LandTrendr, products currently only available outside of SEPAL and CEO.

TimeSync integration is coming to CEO in 2021.

.. note::

    **objectives**:

    -   Learn the basics of BFAST explorer in SEPAL
    -   Learn about time series analysis options outside of SEPAL

.. warning::

    **Prerequisit**: SEPAL account

BFAST Explorer
""""""""""""""

Breaks For Additive Seasonal and Trend (BFAST) is a change detection algorithm for time series which detects and characterizes changes. BFAST integrates the decomposition of time series into trend, seasonal, and remainder components with methods for detecting change within time series. BFAST iteratively estimates the time and number of changes, and characterizes change by its magnitude and direction (Verbesselt et al. 2009).

BFAST Explorer is a Shiny app, developed using R and Python, designed for the analysis of Landsat Surface Reflectance time series pixel data. Three change detection algorithms - bfastmonitor, bfast01 and bfast - are used in order to investigate temporal changes in trend and seasonal components, via breakpoint detection. If you encounter any bugs, please send a message to almeida.xan@gmail.com, or create an issue on the GitHub page.

More information can be found online at http://bfast.r-forge.r-project.org/.

Navigate to the **Apps** menu by clicking on the wrench icon and then Type “BFAST” into the search field and select BFAST Explorer.

Find a location on the map that you would like to run BFAST on. Click a location to drop a marker, and then click the marker to select it. Select **Landsat 8 SR** from the select satellite products dropdown. Click :code:`Get Data`, It may take a moment to download all the data for the point.

.. figure:: ../_images/workflows/area_estimation/BFAST_explorer.png
    :alt: The BFAST Explorer interface.
    :align: center

Click the :code:`Analysis` button at the top next to the :code:`Map` button.

-   **Satellite product**: Add your satellite data by selecting them from the satellite products dropdown menu.
-   **Data**: The data to apply the BFAST algorithm to and plot. There are options for each band available as well as indices such as NDVI, EVI, and NDMI. Here select **ndvi.**
-   **Change detection algorithm**: Holds three options of BFAST to calculate for the data series.

    -   **Bfastmonitor**: Monitoring the first break at the end of the time series.
    -   **Bfast01**: Checking for one major break in the time series.
    -   **Bfast**: Time series decomposition and multiple breakpoint detection in tend and seasonal components.

Each BFSAT algorithm methodology has characteristics which affect when and why you may choose one over the other. For instance, if the goal of an analysis is to monitor when the last time change occurred in a forest then “Bfastmonitor” would be an appropriate choice. Bfast01 may be a good selection when trying to identify if a large disturbance event has occurred, and the full Bfast algorithm may be a good choice if there are multiple times in the time series when change has occurred.

Select **bfastmonitor** as the algorithm.

.. figure:: ../_images/workflows/area_estimation/BFAST_explorer_interface.png
   :alt: The BFAST Explorer interface.
   :align: center

You can explore different bands (including spectral bands e.g. b1) along with the different algorithms.

.. figure:: ../_images/workflows/area_estimation/BFAST_visualization.png
   :align: center

You can also download all the time series data by clicking the blue :code:`Data` button. All the data will be downloaded as a .CSV, ordered by the acquisition date.
You can also download the time series plot as an image, by pressing the blue :code:`Plot` button. A window will appear offering some raster (.JPEG, .PNG) and a vectorial (.SVG) image output formats.

.. note::

   The black and white flashing is normal.

TimeSync and LandTrendr
"""""""""""""""""""""""

Here we will briefly review TimeSync and LandTrendr, two options available outside of SEPAL that may be useful to you in the future. It is outside of the scope of this manual to cover them in detail but if you're interested in learning more we've provided links to additional resources.

TimeSync
++++++++

TimeSync was created by Oregon State University, Pacific Northwest Research Station, the Forest Service Department of Agriculture, and the USFS Remote Sensing Applications Center.

From the TimeSync User manual version 3:

    "TimeSync is an application that allows researchers and managers to characterize and quantify disturbance and landscape change by facilitating plot-level interpretation of Landsat time series stacks of imagery (a plot is commonly one Landsat pixel). TimeSync was created in response to research and management needs for time series visualization tools, fueled by rapid global change affecting ecosystems, major advances in remote sensing technologies and theory, and increased availability and use of remotely sensed imagery and data products..."

TimeSync is a Landsat time series visualization tool (both as a web application and for desktops) that can be used to:

-   Characterize the quality of land cover map products derived from Landsat time series.
-   Derive independent plot-based estimates of change, including viewing change over time and estimating rates of change.
-   Validate change maps.
-   Explore the value of Landsat time series for understanding and visualizing change on the earth's surface.

TimeSync is a tool that researchers and managers can use to validate remotely sensed change data products and generate independent estimates of change and disturbance rates from remotely sensed imagery. TimeSync requires basic visual interpretation skills, such as aerial photo interpretation and Landsat satellite image interpretation.”

From TimeSync's Introduction materials, here is an example output:

.. figure:: ../_images/workflows/area_estimation/TimeSync_example.png
   :alt: An example from TimeSync.
   :align: center

For more information on TimeSync, including an online tutorial (for version 2 of TimeSync), go to: https://www.timesync.forestry.oregonstate.edu/tutorial.html. There you can register for an account and work through an online tutorial with examples and watch a recorded TimeSync training session. You can also find the manual for version 3 of TimeSync here: http://timesync.forestry.oregonstate.edu/training/TimeSync_V3_UserManual_doc.pdf, and an introductory presentation here: https://timesync.forestry.oregonstate.edu/training/TimeSync_V3_UserManual_presentation.pdf.


LandTrendr
++++++++++

LandTrendr has much the same functionality as TimeSync, but runs in Google Earth Engine. It was created by `Dr. Robert Kennedy <https://ceoas.oregonstate.edu/people/robert-kennedy>`_'s lab with funding from the US Forest Service Landscape Change Monitoring System, the NASA Carbon Monitoring System, a Google Foundation Grant, and U.S. National Park Service Cooperative Agreement. Recent contributors include David Miller, Jamie Perkins, Tara Larrue, Sam Pecoraro, and Bahareh Sanaie (Department of Earth and Environment, Boston University). Foundational contributors include Zhiqiang Yang and Justin Braaten in the Laboratory for Applications of Remote Sensing in Ecology located at Oregon State University and the USDA Forest Service's Pacific Northwest Research Station.

From Kennedy, R.E., Yang, Z., Gorelick, N., Braaten, J., Cavalcante, L., Cohen, W.B., Healey, S. (2018). Implementation of the LandTrendr Algorithm on Google Earth Engine. Remote Sensing. 10, 691.:

    "LandTrendr (LT) is a set of spectral-temporal segmentation algorithms that are useful for change detection in a time series of moderate resolution satellite imagery (primarily Landsat) and for generating trajectory-based spectral time series data largely absent of inter-annual signal noise. LT was originally implemented in IDL (Interactive Data Language), but with the help of engineers at Google, it has been ported to the GEE platform. The GEE framework nearly eliminates the onerous data management and image-pre-processing aspects of the IDL implementation. It is also light-years faster than the IDL implementation, where computing time is measured in minutes instead of days."

From LandTrendr's documentation, here's an example output in the GUI. However, LandTrendr has significant non-GUI data analysis capabilities. For a comprehensive guide to running LT in GEE visit: https://emapr.GitHub.io/LT-GEE/landtrendr.html.

.. figure:: ../_images/workflows/area_estimation/LandTrendr.png
   :alt: The LandTrendr interface
   :align: center

.. _module 4:

Sample-based estimation of area and accuracy
--------------------------------------------

Once you have either a land use/land cover (LULC) map (`module 2`_) or a change detection map (`module 3`_), the next step is to estimate the area within each LULC type or change type and the error associated with your map (this Module). All maps have errors, for example model output errors from pixel mixing or input data noise. Our objective is to create unbiased estimates of the area for each mapped category.

To do this, we will use sample-based estimations of area and error instead of ‘pixel counting' approaches. Pixel counting approaches simply sum the area belonging to each different class. However, this doesn't account for classification errors--for example, the probability that a pixel classified as wetland should be open water. Therefore, the pixel counting approach provides no quantification of sampling errors and no assurance that estimates are unbiased or that uncertainties are reduced (Stehman, 2005; GFOI, 2016).

Sample-based estimations of area and error create estimations of errors in pixel classification and use this to inform estimations of area. Therefore, sample-based estimations are in keeping with the IPCC General Guidelines (2006) that estimates should not be over- or under- estimates, and that uncertainty should be reduced as much as practically possible. For more information on the theory behind choosing sample-based estimations of area and error over pixel counting approaches, see:

* GFOI. 2016. Integration of remote-sensing and ground-based observations for estimation of emissions and removals of greenhouse gases in forests: Methods and Guidance from the Global Forest Observations Initiative, Edition 2.0, Food and Agriculture Organization, Rome
* GOFC-GOLD. 2016. A sourcebook of methods and procedures for monitoring and reporting anthropogenic greenhouse gas emissions and removals associated with deforestation, gains and losses of carbon stocks in forests remaining forests, and forestation. GOFC-GOLD Report version COP22-1, (GOFC-GOLD Land Cover Project Office, Wageningen University, The Netherlands)
* Gallego, FJ. 2004. Remote sensing and land cover area estimation. International Journal of Remote Sensing, 25(15): 3019-3047, DOI: 10.1080/01431160310001619607
* IPCC. 2006. Guidelines for national Greenhouse Gas Inventories. Volume 4: Agriculture, Forestry and Other Land Use. http://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html
* REDD Compass: https://www.reddcompass.org/

There are four steps to sample-based estimation of area and accuracy. First, you will use the different classes in your LULC or change detection map to create a stratified sampling design in SEPAL using the Stratified Area Estimator (SAE) - Design tool (Exercise 4.1). Then you will revisit your response design and labeling protocols to use with data collection in CEO (Exercise 4.2). Finally, you will use data generated in CEO (Exercise 4.3) to calculate the sample-based estimates in SEPAL, using the Stratified Area Estimator- Analysis tool (Exercise 4.4). This tool quantifies the agreement between the validation reference points and the map product, providing information on how well the class locations were predicted by the Random forest classifier.

This process will provide two important outputs. First, you will have estimates of the area for each LULC or change type. Second, you will have a table that describes the accuracy for each LUC or change type. This is often called a confusion matrix. These may be final products for your projects. However, if you decide that your map is not accurate enough, this information can be fed back into the classification or change detection algorithms to improve your model.

This Module takes approximately 3 hours to complete.

.. _section 4.1:

Sample design and stratification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stratified random sampling is an easy to use, easy to understand, and well supported sampling design (for more information, see Olofsson et al. 2014. Good practices for assessing accuracy and estimating area of land change, Remote Sensing of Environment 148, 42-57). With stratified random sampling, each class (e.g. land use, land cover, change type) is treated as a strata. Then, a sample is randomly taken from each sample, either in proportion to area, in proportion to expected variance, or in equal numbers across strata.

We will use the SEPAL SAE-Design tool. You will upload your classified map and set some basic parameters, then the SAE-Design tool will generate a set of stratified random points that are placed in each of the different land cover classes represented in your map. The number of points in each class will be scaled to the area each class covers in the map. The total sample size, the number of points used to validate the map will depend on your expected overall accuracy. Be sure to log these choices as part of your documentation (`module 5`_).

.. note::

    **objectives**:

    -   Generate a stratified random sample based on your image classification
    -   Upload your stratification to SEPAL

.. warning::

    **Prerequisites**:

    -   Classification from `module 2`_
    -   advanced users can use the classification from `module 3`_

.. _section 4.1.1:

Uploading files to SEPAL
""""""""""""""""""""""""
If your classification is not stored in SEPAL (for example, a classification in GEE or a classification created through CODED), you will need to upload it to SEPAL in order to use SEPAL's stratified random sample tool. Several option are described in this `page <../setup/FileZilla.html>`_ of the documentation.

.. _section 4.1.2:

Creating a stratified random sample
"""""""""""""""""""""""""""""""""""

We will use SEPAL to create a stratified random sample. To begin, you can use the test dataset available in SEPAL or you can use a raster of your classification loaded into SEPAL.

If you have a large area you are stratifying, please first increase the size of your instance (see `Introduction to SEPAL <../setup/presentation.html#terminal-tab>`_).

A well-prepared sample can provide a robust estimate of the parameters of interest for the population (percent forest cover, for example). The goal of a sample is to provide an unbiased estimate of some population measure (e.g. proportion of area), with the smallest variance possible, given constraints including resource availability. Two things to think about for sample design are: do you have a probability based sample design? That is, does every sample location have some probability of being sampled? And second, is it geographically balanced? That is, are all regions in the study area represented. These factors are required for the standard operating procedures when reporting for REDD+.

These directions will provide a stratified random sample of the proper sampling size.

First, navigate to https://sepal.io/ and sign in. Select the :code:`Apps` button (purple wrench). Type ‘stratified' into the search bar or scroll through the different process apps to find “Stratified Area Estimator - Design”. Select **Stratified Area Estimator - Design.** Note that loading the tool takes a few minutes.

.. figure:: ../_images/workflows/area_estimation/stratified_area_estimator_design.png
    :alt: Stratified Area Estimator-Design tool.
    :align: center

.. note::

    Sometimes the tool fails to load properly (none of the text loads) as seen below. In this case, please close the tab and repeat the above steps.

    .. figure:: ../_images/workflows/area_estimation/fail_stratified_estimator_tool.png
        :alt: Failure of the stratified area estimator tool.
        :align: center

When the tool loads properly, it will look like the image below. Read some of the information on the **Introduction** page to acquaint yourself with the tool.

On the **Introduction** page, you can change the language from English to French or Spanish.
The Description, Background, and "How to use the tool" panels provide more information about the tool.
The Reference and Documents panel provides links to other information about stratified sampling, such as REDD Compass.

.. figure:: ../_images/workflows/area_estimation/stratified_estimator_interface.png
   :alt: The stratified estimator interface.
   :align: center

The steps necessary to design the stratified area estimator are located on the left side of the screen and they need to be completed sequentially from top to bottom.
Select :code:`Map input` on the left side of the screen.

For this exercise, we'll use the classification from `module 2`_.

.. note::

    However, you can substitute another classification, such as the change detection classification created in `module 3`_ if you would like.

In the **Data type** section, click :code:`Input`.
In the **Browse** window that opens, navigate to the `module 2`_ dataset and select it. Then click  on :code:`Select`.

.. tip::

    Note that the **Output folder** section shows you where in your SEPAL workspace all the files generated from this Exercise will be saved.

.. seealso::

    Optionally, you can use a csv with your raster areas instead. We won't discuss that here.

Next, click :code:`Strata areas` on the left side of the screen. In the **Area calculation** section, select :code:`OFT`. **OFT** stands for the Open Foris Geospatial Toolkit. R is slower but avoids some errors that arise with OFT.

.. warning::

    If you choose to use OFT, it will return values for the map that are incorrect if your map stored using certain formats (e.g. signed 8 bit). If this is the case, then please use the R option and it will work correctly. If using OFT, always compare the **Display map** with the **Legend labeling** values returned to make sure they match.

.. figure:: ../_images/workflows/area_estimation/stratified_estimator_map_legend.png
   :alt: Stratified estimator tool showing the display map and legend and areas filled out.
   :align: center

The **“Do you want to display the map”** checkbox allows you to display your geotiff under “Display map”.

.. tip::

    The colors displayed in the SAE-Design tool in this section may be different than what you see elsewhere. Additionally, if your ‘no data' class is 0, the tool will color this as well.

Click the **Area calculation and legend generation** button. This will take a few minutes to run. After it completes, notice that it has updated the **Legend labeling** section of the page.

Next, you will need to adjust the class names in the **Legend labeling** section. Type in the following class names in place of the numeric codes for your Amazon:
-   0 = No Data
-   1 = Forest
-   2 = Non-Forest

Now click :code:`Submit Legend`. The **Legend and Areas** section will now be populated with the map code, map area, and edited class name.
You can now **Rename** and **Download** the area file if you would like. However it will save automatically to your Sepal workspace.
When you're done, click on **Strata selection** on the left panel.

Now you need to specify the expected accuracies. You will do this for each class. Get more information by clicking the **plus** button to the right of the box that says **What are the expected accuracies?**.

-   Specify the expected user accuracy helps the program determine which classes might need more points relative to their area.
-   Some classes are easier to identify--including common classes and classes with clear identifiers like buildings.
-   Classes that are hard to identify include rare classes and classes that look very similar to one another. Having more classes with low confidence will increase the sample size.
    -   Select the value for classes with high expected user accuracy with **the first slider**. This is set to 0.9 by default, and we'll leave it there.
    -   Then, select the value for classes with low expected user accuracy with **the second slider**. This is set to 0.7 by default, and we'll leave it there as well.

Now we need to assign each class to the high or the low expected user accuracy group. Think about your forest and non-forest classes. Which do you think should be high confidence? Which should be low confidence? Why?
Click on the box under **“high confidence”** and assign your high confidence class(es). Then, click on the box under **“low confidence”** that appears and assign the corresponding class(es). If you make a mistake, there's no way to remove the classes. However, just change one of the sliders slightly, move it back, and the class assignments will have been reset.

.. danger::

    For this exercise, please assign both Forest & Non-forest to the high confidence class. If you assign either to the low confidence class, you will not be able to use the CEO-SEPAL bridge in `section 4.2`_.

     DO NOT assign your No Data class to either high or low confidence.

.. figure:: ../_images/workflows/area_estimation/high_low_expected_user_accuracy.png
   :alt: High and low expected user accuracy.
   :align: center

When you're satisfied, click on **Sampling Size** on the left panel.

Now we will calculate the required sample size for each strata. You can click on the “+” button to get more information.

-   First we need to set the **standard error of the expected overall accuracy.** It is 0.01 by default, however for this exercise we will set it to 0.05.

    .. seealso::

        This value affects the number of samples placed in each map class. The lower the value, the more points there are in the sample design. Test this by changing the error from 0.05 to 0.01, and then change it back to point 0.05. Alternatively, you can click the up/down button to the right of the number.

    .. note::

        Note that you can adjust this incrementally with the up/down arrows on the right side of the parameter.

-   Then determine the **minimum sample size per strata.** By default it is 100. For the purposes of this test we will set it to 20, **but in practice this should be higher.**

    .. note::

        You can also check the “Do you want to modify the sampling size” box.

-   If you would like, you can edit the name of the file & download a csv with the sample design. The file contains the table shown above with some additional calculations. However, SEPAL will automatically save this file.

.. figure:: ../_images/workflows/area_estimation/stratified_estimator_sampling.png
    :alt: The stratified estimator sampling size and distribution of samples screen.
    :align: center

When you're ready, click on **Sample allocation** to the left. The final step will select the random points to sample.
Select **Generate sampling points** and wait until the progress bar in the bottom right finishes. Depending on your map, this may take multiple minutes. A map will pop up showing the sample points. You can pan around or zoom in/out within the sample points map. he resulting **distribution of samples** should look similar to the below image.

.. note::

    These values will vary depending on your map and the standard error of expected overall accuracy you set.

.. warning::

    Sometimes this step fails, no download button will appear, and you will need to refresh the page and restart the process.

.. figure:: ../_images/workflows/area_estimation/stratified_estimator_map.png
   :alt: The stratified estimator tool's sample allocation screen.
   :align: center

Now fill out the four fields to the right. You can add additional data by specifying which country the map is in. Here, Leave the **Choose your country name…** section blank. Specify the **number of operators,** or people who will be doing the classification. Here, leave it set to 1. For CEO, this might be the number of users you think your project will have. The **size of the interpretation box** depends on your data and corresponds to CEO's sample plot. This value should be set to the spatial resolution of the imagery you classified (Landsat= 30 meters). Here, leave it at 30 m.

.. note::

    When should you use CEO, and when should you use the CEO-SEPAL bridge? In general, **the CEO-SEPAL bridge should only be used for fairly simple use cases.** More specifically, CEO-SEPAL is a great option when you have only high-confidence categories, have a relatively small number of points, when you will collect the data yourself, and when the built in questions about your data points suffice. For other situations, you will want to create a CEO project. Creating a CEO project through the collect.earth website is a better option when you have low-confidence categories, a larger number of points in your sample, when you want to use specific validation imagery, when multiple people will collect data and you need to track who is collecting data, and when you need more complex or custom questions about your data points.

If you would like to create a project via CEO, click on **Download .csv** and follow the steps in `section 4.1.3`_ below. After following the directions in this, you will proceed to `section 4.2`_.

.. warning::

    We highly recommend using this approach, and we will demonstrate it in this manual.

To create a project via the CEO-SEPAL bridge, click on **Create CEO project**. This will create a CEO project via the CEO-SEPAL bridge. This process will take a few minutes and you should see text and completion bars in the lower right as calculations happen. Copy-paste the link into your browser window when it appears.

.. tip::

    Be sure to save this link somewhere so you can reference it later.

.. danger::
   You MUST be logged out of CEO for this pathway to work.

.. figure:: ../_images/workflows/area_estimation/ceo_project_sepal.png
   :alt: Creating a CEO project through SEPAL.
   :align: center

When the project has been created, you can skip down to `section 4.2`_.
You can download a .shp file to examine your points in QGIS, ArcGIS, or another GIS program. You can also create a CEO project using a .shp file, however that is outside of the scope of this manual. Directions can be found in the Institutional manual found here: https://collect.earth/support.

.. _section 4.1.3:

Creating a CEO project via CSV
""""""""""""""""""""""""""""""

For projects with large sample sizes, where you want to have multiple people collecting validation data, or where you want to use specific validation imagery, you will want to create a project through CEO rather than through the CEO-SEPAL bridge. Note that the TOTAL number of plots you want to sample using a .csv must be 50,000 or less. If you have more plots, break it into multiple projects.

Make sure you have downloaded the .csv of your stratified random sample plots (`section 4.1.2`_). Open your downloaded .csv file in Excel or the spreadsheet program of your choice. First, make sure that your data doesn't contain a strata of ‘no data'. This can occur if your classification isn't a perfect rectangle, as seen in this example of Nepal (the red circles are samples that the tool created in the ‘no data' area).

.. tip::

    If you have ‘no data' rows, return to the SEPAL stratified estimator, and be sure to not include your no data class in the strata selection step.

.. figure:: ../_images/workflows/area_estimation/example_data_sepal_classification.png
   :alt: Example data from the SEPAL classification.
   :align: center

Right now, your stratification is grouped by land cover type (**map_class** column). To reduce the human tendency to use the order of the plots to help identify them (i.e. knowing the first 100 plots were classified forest, so being more likely to verify them as forest instead of determining if that is correct) we suggest first randomizing the order of the rows. To do this, click the :code:`Sort & Filter` button in Excel.

.. figure:: ../_images/workflows/area_estimation/sort_filter_excel.png
   :alt: Using the Sort and Filter features in Excel.
   :align: center

Next, Sort on the ‘id' field by value, either smallest to largest or largest to smallest.

.. figure:: ../_images/workflows/area_estimation/custom_filter_excel.png
   :alt: A custom sort in Excel.
   :width: 450
   :align: center

Now we need to add the correct columns for CEO. Remember that Latitude is the Y axis and longitude is the X axis. For CEO, the first three columns must be in the following order: longitude, latitude, plotid. The spelling and order matter. If they are wrong CEO will not work correctly.

-   Rename ‘id' to PLOTID. You can also add a new PLOTID field by creating a new column labeled PLOTID, and fill it with values 1-(number of rows).
-   Rename the ‘XCoordinate' column to ‘LONG' or ‘LONGITUDE'.
-   Rename the ‘YCoordinate' column to ‘LAT' or ‘LATITUDE'.
-   Reorder the columns in Excel so that LAT, LONG, PLOTID are the first three columns, in that order.

Save your updated .csv, making sure you save it as a .csv and not as an .xlsx file.

Navigate to collect.earth. Login to your CEO account. If you're already the administrator of an institution, navigate to your institution's landing page by typing in the institution's name and then clicking on the Visit button.

.. tip::

    Creating a project in CEO requires you to be the administrator of an institution. If you're not an admin, go ahead and create a new institution. Click on create new institution from the homepage, then fill out the form & click create institution.

When you're on the institution's page, click on the “Create New Project” button. This will go to the Create Project interface. We'll now talk about what each of the sections on this page does. For more information, please see the Institutional Manual available on the collect.earth Support page https://collect.earth/support.

-   **TEMPLATE**: This section is used to copy all the information—including project info, area, and sampling design—from an existing published project to a new project.

    -   This is useful if you have an existing project you want to duplicate for another year or location, or if you're iterating through project design. You can use a published or closed project from your institution or another institutions' public project.
    -   The project id is found in the URL when you're on the data collection page for the project.

-   **PROJECT INFO**: Under Project Info, enter the project's **Name** and **Description.**

    -   The **Name** should be short and will be displayed on the Home page as well as the project's Data Collection page.
    -   You should keep the **Description** short but informative.
    -   The **Privacy Level** radio button changes who can view your project, contribute to data collection, and whether admins from your institution or others creating new projects can use your project as a template.

-   **AOI**: The project area of interest (AOI) determines where sample plots will be drawn from for your project. This is the first step in specifying a sampling design for your project. There are two main approaches for specifying an AOI and sampling design.

    -   First, using CEO's built in system.
    -   Second, creating a sample in another program and importing it into CEO. **This is what we have done.** You will specify the AOI in the Sample Design step instead.
    -   You should choose your Basemap source, which will be the default imagery that the user sees.
    -   (Optional) Check the box for any additional imagery you would like to add.

-   **Sample Plot Design**: Here, click the radio button next to .csv.

    -   Click on **Upload,** and upload the .csv of your stratified random sample. Note that the number of plots you want to sample must be 5000 or less.
    -   Select if you would like round or square plots, and specify the size. For example, you might specify square plots of 30m width in order to match Landsat grid size.

-   **Sample Point Design**: Under the Sample Design header is really determining the sample point design within each sample plot.

    -   You can choose Random or Gridded, and how many samples per plot or the sample resolution respectively. You can also choose to have one central point.
    -   Using CEO's built in system, the maximum number of sample points per plot is 200. The maximum total number of sample points for the project across all plots is 50000.

-   **Survey Design:** This is where you design the questions that your data collectors/photo interpreters will answer for each of your survey plots. Each question creates a column of data. This raw data facilitates calculating key metrics and indicators and contributes to fulfilling your project goals.

    -   **Survey Cards** are the basic unit of organization. Each survey card creates a page of questions on the Data Collection interface.
    -   The basic workflow is: Create new top-level question (new survey card) THEN populate answers THEN create any child questions & answers THEN move to next top-level question (new survey card) & repeat until all questions have been asked.
    -   You can ask multiple types of questions (including the button—text questions from the Simple interface). You can also add survey rules in the Survey Rules Design panel.
    -   Broadly, there are four question types and three data types. They are combined into 10 different component types.
    -   The four question types are:

        -   Button: This creates clickable buttons, allowing users to select one out of many answers for each sample point.
        -   Input: Allows users to enter answers in the box provided. The answer text provided by the project creator becomes the default answer.
        -   Radio button: This creates radio buttons, allowing users to select one out of many answers for each sample point.
        -   Dropdown: Allows users to select from a list of answers.

    -   The three data types allowed are:

        -   Boolean: Use this when you have two options for a question (yes/no).
        -   Text: Use this when you have multiple options which are text strings. They may include letters, numbers, or symbols.
        -   Number: Use this when you have multiple options that are numbers, which do not contain letters or symbols.

    -   First, type in your question in the New question box, such as “Is this forest or non-forest?"
    -   Then click add survey question.
    -   A new survey card (Survey Card Number 1) will pop up with your question in it.
    -   You can now add answers.
    -   Create one answer for each of your land use types. Here we will use 1 and 2 to match our “Forest” and “Non-forest” in our classification. Be sure to include all your land use types.
    -   Note that the Stratified Area Estimator--Analysis only accepts numeric values for the land use types. If you would like to use human-readable text values (e.g. Forest instead of 1)

        .. danger::

            You MUST follow the directions in `section 4.3.2`_.

    -   You can add additional survey questions if you'd like to experiment. An example of two survey cards is shown below.

.. figure:: ../_images/workflows/area_estimation/example_survey_card.png
   :alt: An example survey card setup
   :width: 450
   :align: center

When you're done, click Create Project. If you're successful, you'll see the review project pane. The Project AOI will now show the location of a subset of your plots (a maximum number can be displayed).

Not shown are the Plot Review and Sample Design, which show a summary of the choices you made or the .csv and .shp files you uploaded. Survey Review shows all the Survey Cards you created, along with the corresponding Component Type, Rules, and Answers. At this point, your project has been created, but it has not been published so that other users can see it.

.. seealso::

    There is also review project functionality. As an administrator, you review your unpublished project and make suggestions to the questions etc. before it is published for data collection.

You can either click [Publish Project] or [Configure Geo-Dash]. The option to Configure Geo-Dash will be available after you publish your project, as well. For now, let's click on Configure Geo-Dash. A new window or tab will open and you'll now see the blank Geo-Dash configuration page.

Geo-Dash is a dashboard that opens in a second window when users begin to analyze sample plots. Geo-Dash provides users with additional information to help them interpret the imagery and better classify sample points and plots. The Geo-Dash tab can be customized to show information such as NDVI time series, forest degradation tools, additional imagery, and digital elevation data. If you click on Geo-Dash Help, You'll access information about all of the Geo-Dash widgets. This information is also in the CEO user manual. Add any widgets that you would like for your project. For example, add a NDVI widget following these steps:

-   Click on Add Widget, then select the Image Collection type.
-   Select your basemap imagery.
-   Now you'll see the data dropdown menu. Select NDVI in this menu.
-   Now you'll see the Title
-   give your widget a title that describes the data.
-   Select the date range using the calendar widgets or by typing it in.
-   When you're done, click Create.

You can now move the widget by clicking and dragging from the center and resize it by clicking and dragging the lower right-hand corner. When you're done adding widgets, close the Geo-Dash window.

On the project review page, click publish project. Collect earth will ask you to confirm, click OK. You can now visit your project from your institution's page and start collecting data!

More detailed instructions, including descriptions of many useful options, can be found in the manuals for CEO: https://collect.earth/support.

.. _section 4.2:

Data collection with data quality management approaches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have created a stratified random sample, you will use CEO (or optionally the CEO-SEPAL tool) to visually interpret the land cover at the sample locations using a suitable source of reference data, often remote sensing data. These visual interpretations will then inform the area and error estimation (`section 4.3`_). However, to ensure accurate human interpretation of land cover, you will need to adopt data quality management approaches. Thus in this exercise, you will check your classification design (`section 4.2.1`_), plan your data collection (`section 4.2.2`_), collect your data (`section 4.2.3`_) and set up quality management (`section 4.2.4`_ & `section 4.2.5`_).

The reason for this focus on data quality is simple: area and error estimates are based on the human interpreter's labeling of the sample; therefore, it is important that the labels are correct. Some recommend that three interpreters examine each unit independently, while other projects just have a sub-sample of the data points cross checked by another interpreter. In `section 4.2.4`_ & `section 4.2.5`_, you will consider this and design a quality assurance plan that meets the needs and budgets of your specific mapping projects and management needs.

Much of this information is based on Standard Operating Procedures developed by Till Neeff at FAO for global application. Working these exercises will help you abide by these guidelines and meet these standards of quality for the data collected.

.. note::

    **objectives**:

    -   Understand how to set up a successful verification project.
    -   Collect land cover verification data about each of your sample points
    -   Create quality management protocols for your verification project

.. warning::

    **Prerequisites**:

    -   Stratified random sample based on your image classification from `section 4.1`_
    -   CEO-SEPAL project initiated in `Section 4.1`_


.. _section 4.2.1:

Specify a classification scheme
"""""""""""""""""""""""""""""""

“Classification scheme” is the name used to describe the land cover / land use classes adopted. It should cover all the possible classes that occur in interest. Just as when you are creating training data for your classification, you will need to have a response design with consistent labeling protocols when collecting data for your area and error estimates.

If you have already created a response design in `module 2`_, you should use that.

If you have not created a response design for the classification you are now evaluating, please refer to Exercise 2.1 to create a classification scheme. Note that if your classification was trained using training points that differ substantially from your classification scheme, you may need to collect new training data and re-run your classification.

As a reminder, our classification used to classify our Forest/Non-forest land cover map was as follows:

.. graphviz::

    digraph process {
           lc [label="Land cover", shape=box];
           f [label="Forest", shape=box, style="filled" color="darkgreen"];
           nf [label="Non forest", shape=box, style="filled", color="grey"];
           lc -> f;
           lc -> nf;
        }

We defined Forest as an area with over 70% tree cover. We defined Non-forest as areas with less than 70% tree cover. This captured land covers including urban areas, water, and agricultural fields.

.. _section 4.2.2:

Planning data collection
""""""""""""""""""""""""

Now that we have the framework for the procedure for data collection with quality in mind we can work through what it would be like setting up the process for a team. Data collection efforts require planning, particularly for large efforts with many interpreters involved. We will discuss these planning aspects here.

In this part, you will assume the role of a **coordinator** and an **interpreter** for a small team working to validate the land cover classification from `module 2`_. A **coordinator** is responsible for organizing the team and tracking compliance information. An **interpreter** is responsible for collecting data.

Identify the reference data sources.

Ideally, you would have plots revisited in the field. However, this is rarely attainable given limited resources. An alternative is to collect reference observations through careful examination of the sample units using high resolution satellite data, or moderate resolution if high resolution is not available. The more data you have at your disposal the better.

If you have no additional data, you can use remote sensing data, such as Landsat data, for collecting reference observations, as long as the process to collect the reference data is more accurate than the process used to create the map being evaluated. Careful manual examination can be regarded as being a more accurate process than automated classification.

Consider what additional data you might be able to include in your verification. Do you have access to satellite data at a finer resolution than Landsat? Could you incorporate additional dataset such as stump data or on the ground verifications? You might try searching databases, such as https://developers.google.com/earth-engine/dataset/.

In CEO, these are the additional data sources that you have added to your CEO project. The CEO-SEPAL bridge uses only the default imagery, which is currently Mapbox Satellite.

Compile a list of your data sources and review it with your interpreters. Recording this information is important for documentation (see `module 5`_).

.. figure:: ../_images/workflows/area_estimation/data_source_recording.png
   :alt: A data source recording document.
   :align: center

Determine level of effort
+++++++++++++++++++++++++

Estimate the necessary level of effort for the data collection using the following formula:

    Minutes to interpret 1 sample unit * number of sample units = required level of effort for data collection

If information is available from previous inventories, use that experience to set the value on the time required for assessing sample units from previous experience using the same response design. Otherwise, carry out a test.

For this exercise, consider how long it took you to create your training data in `module 2`_ and use the formula above to estimate how long it will take to classify all your samples.

Identify data collection participants
+++++++++++++++++++++++++++++++++++++

As coordinator, you will identify the persons who may be involved in the data collection. You should set up minimum qualifications for participating in the data collection, such as familiarity with the landscape, previous experience, etc.

-   What qualifications do you think are important?
-   What qualifications are essential, and which would be nice to have?
-   How can you build capacity within your organization for data collection?

As coordinator, you will record names and contact information of all the participants in the data collection and training.

Here's a template:

.. csv-table::
    :header: Name, Contact, Institution, Role for data collection

    Name, Email address and/or phone number, Institution name, Coordinator
    Name, Email address and/or phone number, Institution name, Trainer
    Name, Email address and/or phone number, Institution name, Sample interpretation
    Name, Email address and/or phone number, Institution name, Sample interpretation
    Name, Email address and/or phone number, Institution name, etc.

And a worked example:

.. csv-table::
    :header: Name, Contact, Institution, Role for data collection

    Phạm Tuân, example@example.org, Institute for Collecting Data, Coordinator
    Sally Ride, example@example.org, Training Specialists Institution, Trainer
    Rodolfo Vela, example@example.org, Institute for Collecting Data, Sample interpretation
    Yuri Gagarin, example@example.org, Institute for Collecting Data, Sample interpretation

Based on this information, you will decide on the format and modality for the data collection and on a timeline. For example, the format of the data collection can be a mapathon set-up where a large group collects the data over a short amount of time or a smaller team that collects the data over long periods. The modality for the data collection concerns where the team collects the data, either in the same location or disparate locations e.g. in a mapathon, the interpreters could be in the same room interpreting the data. If the data collection is set up in disparate locations, modes of communication should be specified to help improve the consistency in the data interpretation. Multiple re-measurements for all samples is another option.

The logistics manager (if different from the coordinator) will arrange logistics, including space for data collection, sufficient time for data collection, and salary arrangements.

With your fictional team (above) and your timeline laid out in the scenario, decide on the format and modality for the data collection and on a timeline.

-   What other modalities of data collection can you think of?
-   What are the pros and cons of these modalities?

Organize training and calibration sessions
++++++++++++++++++++++++++++++++++++++++++

As a first step in the data collection, the coordinator and the trainer organize and prepare a training event for the interpreters who have confirmed their participation. The training should cover the following topics as a minimum:

-   the response design and the interpretation key (detailing location specific examples from all the classes in the classification system with visualization from multiple data sources available),
-   The software used for the data collection and how to ensure the data management and storage,
-   The data sources available, and
-   Quality management practices.

Knowing what you do now, consider list items above and briefly fill in details for each topic in another document. Write this as if you were planning a training event before collecting verification data for your forest/non-forest classification. What other topics do you think should be in the training?

The trainer should then implement the training event following these basic principles:

-   Create an environment for active participation, where participants can share questions and opinions
-   encourage communication between the interpreters
-   record attendance of the interpreters, and
-   assess the capacity of the interpreters at the end of the training and record the results.
-   Thinking about the basic principles for a training (a-d above) briefly write out how you might achieve these goals.

Following the training, the coordinator and the trainer should prepare a report summarizing:

-   The training actions taken,
-   The attendance (example below), and
-   The results of the assessment of capacity.

This information should be documented as part of the decision making process for the verification (see `module 5`_).


.. csv-table::
    :header: Name, Day 1, Day N

    Interpreter 1, present, present
    Interpreter x, present, present

Distribute and assign sample units to interpreters
++++++++++++++++++++++++++++++++++++++++++++++++++

As coordinator, you will decide on a fraction of sample units to be assessed multiple times by all interpreters for cross-checking. Using approximately 2.5% of plots for cross checks is a good starting point. The samples that are duplicated should have a unique identification, and/or be recorded in some way.

.. note::

    Note that we'll discuss this aspect of quality management in Part 4, so don't worry about that at this time.

The coordinator should then allocate sample units to interpreters based on some system. Allocation modalities are the modalities by which sample units are allocated to each interpreter e.g. randomly, following experience in a specific area.

.. tip::

    answer the following questions : What method might you prefer be used to allocate samples? Why?

The coordinator should use a standardized naming structure to distribute the samples to the interpreters. The coordinator should record the number of sample units, the interpreter assigned to assess those samples and the file location in a table like the one below. The naming structure can include metadata such as the date the samples are distributed, the name of the interpreter and the purpose of the data collection. Try preparing a document to distribute the sample units among interpreters like the table below:

.. csv-table::
    :header: Number of sample units, Interpreter name, File name, File archive location

    X sample units, Interpreter 1, e.g. collection_data_date \n[year/month/day] \n_version_number.csv, Link to cloud storage or folder path to repository

In CEO, multiple interpreters can work on the same project at the same time. This makes it very easy to collect data collaboratively. When you later download the data, each interpreter's email address will be attached to the point they collected. If you use CEO-SEPAL, you cannot collect this information at the time of writing.

.. _section 4.2.3:

Collecting data
"""""""""""""""

After training and sample allocation, it is time to collect data. This can occur in the CEO-SEPAL interface (for smaller projects) or via CEO for larger or multi-user projects. Here, we will demonstrate collecting data in CEO to ensure compliance with SOP and oversight requiring interpreter names be collected for the points they collect, however the directions are largely the same for the CEO-SEPAL bridge.  How to set up a CEO project is discussed in Exercise 4.1 Part 2. How to set up a CEO-SEPAL project is discussed at the end of `section 4.1.1`_.

Data collection by interpreters
+++++++++++++++++++++++++++++++

In general, data collection should include the following steps:

1.  When interpreting the samples, use an interpretation key as a guide for assessing different land use classes and transitions. When possible, consult other interpreters and the coordinator if there are any doubts about the image interpretation.
2.  The coordinator collects the data from all interpreters at defined intervals (intervals can be defined by number of samples or by time intervals) to perform quality assurance procedures, including auxiliary data checks, cold checks and hot checks, as defined in the quality assurance section.
3.  During the data collection, the coordinator organizes regular discussions and group assessment of samples with all the interpreters to ensure a mutual understanding of the interpretation techniques.
4.  Take notes of challenges and limitations during the data collection as well as potential sources of bias during the data collection. If working as part of a team of collectors pass this information along to the coordinator.

Data collection in CEO
++++++++++++++++++++++

To collect data in CEO, navigate to the project you created in `section 4.1.2`_. Your screen should look like this:

.. figure:: ../_images/workflows/area_estimation/data_collection_CEO.png
    :alt: The data collection interface in CEO
    :align: center

Click **Go to first plot.** This will take you to your first plot. Answer all of the questions for your first plot by clicking on the appropriate answers. If you created multiple questions, you can navigate between questions using the numbers above your question text. Click on :code:`Save` to save your answers and move on to the next plot.

.. figure:: ../_images/workflows/area_estimation/data_collection_process.png
   :alt: The data collection process in CEO
   :align: center

Continue answering questions until you reach the last plot. When you have finished answering all of the questions, navigate to your Institution's page.

.. note::

    Your project name should now be green, indicating that all plots have been completed. If it is yellow, click on the project name and answer the remaining questions.

.. figure:: ../_images/workflows/area_estimation/ceo_sepal_manual.png
   :alt: A partly completed project.
   :align: center

Click on the :code:`S` next to the project. This will download your project's sample data. Save it to your hard drive.

Data collection in CEO-SEPAL bridge
+++++++++++++++++++++++++++++++++++

For this example, navigate to the web address associated with your CEO-SEPAL bridge project. It should look something like this: https://collect.earth/collection?projectId=18301&tokenKey=b1216bbb-9395-41f8-bc02-f898c98465bf. You must be logged out of CEO for this link to work.

Click :code:`Go to first plot`. This will take you to your first plot. With the CEO-SEPAL bridge, there is only one question. It is “CLASS”, where you must assign the appropriate value to your point. The CEO-SEPAL bridge uses the names you typed in during the legend labeling stage of the Sample Design.

Click on :code:`Save` to save your answers and move on to the next plot.

Continue answering questions until you reach the last plot.

Data assembly
+++++++++++++

Data assembly is required ONLY when you have multiple data interpreters, each working on their own project. If you have used the CEO pathway above with multiple interpreters contributing to the same project, this step is not needed.

If you have multiple interpreters, after the data collection is completed the coordinator should create a consolidated database with all the collected sample data.

-   The coordinator should check that all necessary metadata and sample information is archived and included in the final database.
-   A description of the column names from the database should be archived with the database.
-   A standardized naming structure is used for the compiled database and includes metadata in the folder and file name.

Each sample in the consolidated database notes the round of data collection. The database can be amended to include additional rounds of data collection. Multiple versions are recorded and explanations between versions are included in the documentation template.

.. tip::

    In CEO, this is handled through the Institution's Project interface.

.. _section 4.2.4:

Quality management and archiving - Quality Assurance
""""""""""""""""""""""""""""""""""""""""""""""""""""

Quality assurance and control are fundamental in ensuring that your validation and resulting area estimates are as accurate as can be and are unbiased. This part will cover the steps of how to perform quality assurance.

For change detection maps, you will want to check for and exclude impossible transitions through logical checks. Make sure that the changes make sense. E.x. having a transition from Water <= 20% to Aquaculture may make sense, but a transition from Water <= 20% to Developed High Intensity would not.

Also be sure to document all impossible transitions. These should be included in your response design tree as well.

Conduct ongoing hot, cold and auxiliary data checks during data collection and conduct regular review meetings among all interpreters. We'll go through each of these now.

-   **Auxiliary data checks**: use an external data source, such as externally created maps, to compare to the sample unit classification. Discrepancies between the two dataset can be flagged for rechecking. Confirmed differences between the two dataset can be documented to showcase why sample-based area estimation may give different results than other data sources.

    For example, the Copernicus Global Land Cover Layers: CGLS-LC100 collection 2, available via GEE, can be used as a comparison layer https://developers.google.com/earth-engine/dataset/catalog/COPERNICUS_Landcover_100m_Proba-V_Global.

    .. tip::

        Ask questions when comparing your map and auxiliary maps:

        -   Where do you notice agreement between the two maps?
        -   Where do you notice disagreement between the two maps?
        -   What are some reasons you could attribute to the discrepancies between them?

-   **Cold checks**: sample units that are randomly selected from the data produced by interpreters. The decisions made by the interpreters are reviewed by the coordinator or group of interpreters meeting together. If the error by the interpreter reflects a systematic error in their interpretation, it is discussed directly with the interpreter and the affected sample units are corrected.

    Review the table below that was a result of a cold check you conducted on the plots analyzed by the interpreters.

    .. note::

        Based on some of these answers:

        -   what can you conclude about the data?
        -   What plots should likely be reviewed?
        -   What other information could you gain from examining how the interpreters are performing?

    **Cold checks** can be created in CEO by creating multiple projects with the same sample plots. Multiple interpreters can each complete one of these projects, allowing for comparison.

    .. csv-table::
        :header: Interpreter, Plot 1 (Forest), Plot 2 (Forest), Plot 3 (Water)

        Sally Ride, Non Forest Vegetation, Non Forest Vegetation, Water
        Rodolfo Vela, Forest, Forest, Build up
        Yuri Gagarin, Forest, Forest, Water

-   **Hot checks**: sample units that are flagged as low confidence. These marked sample units should be further reviewed by the coordinator or group of interpreters meeting together. Once reviewed, labels that are deemed to be incorrect on these sample units should be adjusted by the interpreter.

    .. tip::

        -   If you're conducting this training with others, ask your colleagues about sample units that you're unsure about.
        -   Have your colleagues show you sample units that they are unsure about.
        -   Discuss these sample units and make changes to the labels based on your discussion.

You must create a project using CEO to add additional questions about confidence level. If you create a project via the ceo-sepal interface, you will have only one question about land use/cover class.

.. _section 4.2.5:

Quality management and archiving - Quality Control
""""""""""""""""""""""""""""""""""""""""""""""""""

Quality control refers to the quality of interpretation through cross-validation based on a set of samples that were assessed by two or more interpreters. See also the cold data check mentioned above. These checks can be conducted in CEO by creating multiple projects with the same sample plots. Multiple interpreters can each complete one of these projects, allowing for comparison.

Establish a reference interpretation for each of the cross-validation sample units.

Choose a reference interpretation--this should be one of the interpreter's class assignments. This reference interpretation will be the basis for establishing the performance of individual interpreters.

Calculate agreement for each interpreter based on the reference interpretation. For each pair of interpreters, create a confusion matrix and include it in your project documentation.

.. csv-table::
    :header: , class 1 (ref), class 2 (ref), class k (ref)

    Class 1 (interpreter), Counts of sample points, Counts of sample points, Counts of sample points
    Class 2 (interpreter), Counts of sample points, Counts of sample points, Counts of sample points
    Class k (interpreter), Counts of sample points, Counts of sample points, Counts of sample points

To work an example, pretend that you and another interpreter have both collected data on a set of sample units on this Amazon land cover classification. Here are the results:

.. csv-table::
    :header: Point number, Interpreter 1, Reference

    1, Forest, Forest
    2, Forest, Forest
    3, Forest, Non-forest
    4, Non-forest, Non-forest
    5, Non-forest, Forest
    6, Forest, Forest
    7, Non-forest, Non-forest
    8, Non-forest, Non-forest
    9, Non-forest, Forest
    10, Forest, Forest

Calculate the confusion matrix below:

.. csv-table::
    :header: , Forest (ref), Non-forest (ref)

    Forest (Interpreter),,
    Non-Forest (Interpreter),,

Based on the confusion matrices, for each interpreter, overall agreement with the reference is to be calculated as follows:

    Agreement between interpreter and the majority = Sum of counts in all the diagonal cells / Sum of all counts

The overall agreement per interpreter can be reported as below:

.. csv-table::
    :header: Interpreter, Overall agreement

    Interpreter 1, Sum of counts in all of the diagonal cells/ Sum of all counts
    Interpreter 2, Sum of counts in all of the diagonal cells/ Sum of all counts
    Interpreter N, Sum of counts in all of the diagonal cells/ Sum of all counts


Using the table below, calculate the agreement between interpreters:

.. csv-table::
    :header: , Class 1 (majority), Class 2 (majority), Class 3 (majority)

    Class 1 (Sally Ride), 90, 8, 2
    Class 2 (Sally Ride), 6, 84, 10
    Class 3 (Sally Ride), 2, 6, 92
    Class 1 (Rodolfo Vela), 89, 9, 2
    Class 2 (Rodolfo Vela), 12, 88, 0
    Class 3 (Rodolfo Vela), 3, 0, 97
    Class 1 (Yuri Gagarin), 94, 6, 0
    Class 2 (Yuri Gagarin), 7, 86, 7
    Class 3 (Yuri Gagarin), 1, 4, 95

.. csv-table::
    :header: Interpreter, Overall agreement

    Sally Ride, Sum of counts in all of the diagonal cells/ Sum of all counts
    Rodolfo Vela, Sum of counts in all of the diagonal cells/ Sum of all counts
    Yuri Gagarin, Sum of counts in all of the diagonal cells/ Sum of all counts

Per-class agreement among interpreters should be analyzed and reported as follows:

..csv-table
    :header: , All interpreters agreeing, One interpreter disagreeing, Two interpreters disagreeing, etc.

    Class 1 (reference), Percent, Percent, Percent, Percent
    Class 2 (reference), Percent, Percent, Percent, Percent
    Class 3 (reference), Percent, Percent, Percent, Percent
    Total, Percent, Percent, Percent, Percent

For this example, consider the following case:

.. csv-table::
    :header: Point number, Interpreter 1, Interpreter 2, Interpreter 3, Reference

    1 , Forest    , Forest    , Forest    , Forest
    2 , Forest    , Forest    , Non-forest, Forest
    3 , Forest    , Non-forest, Non-forest, Non-forest
    4 , Non-forest, Non-forest, Non-forest, Non-forest
    5 , Non-forest, Forest    , Forest    , Forest
    6 , Forest    , Forest    , Non-forest, Forest
    7 , Non-forest, Non-forest, Non-forest, Non-forest
    8 , Non-forest, Non-forest, Non-forest, Non-forest
    9 , Non-forest, Forest    , Non-forest, Forest
    10, Forest    , Forest    , Forest    , Forest


Now calculate the per-class agreement. Note that percent should be calculated by #/10 points for this example.

.. csv-table::
    :header: , All interpreters agreeing, One interpreter disagreeing, Two interpreters disagreeing

    Forest (reference)    , Percent, Percent, Percent, Percent
    Non-forest (reference), Percent, Percent, Percent, Percent
    Total                 , Percent, Percent, Percent, Percent

.. _section 4.3:

Area and uncertainty estimation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The final step of calculating the sample-based estimates of error and area is taking the map areas (generated in `section 4.1`_), and your verification data points from our data collection (`section 4.2`_), conducted according to the response design rules (`section 4.1`_) and using statistics to output the final estimates of area and uncertainty.

In `section 4.3.1`_, we provide an optional description of error matrices, also called confusion matrices. This provides the underlying theory for using the SEPAL “Stratified estimator--Analysis” tool to conduct the area and uncertainty estimation. This tool quantifies the agreement between the validation reference points and the map product, providing information on how well the class locations were predicted.
Please note that you will need to upload your collected data from CEO to Sepal using the directions found in `section 4.1.1`_. If you used the CEO-SEPAL bridge, you must log out of CEO for the “Import CEO Project” link to work.

.. note::

    **objectives**:

    -   create area estimate for your classification
    -   create uncertainty/error estimate for your classification

.. warning::

    **Prerequisites**:

    -   Completed verification data, or reference data (`section 4.2`_)
    -   Map areas generated by your sampling design (`section 4.1`_)

.. _section 4.3.1:

Understanding the error matrix
""""""""""""""""""""""""""""""

.. note::

    This step is fully optional

A common tool to quantify agreement is the error matrix (sometimes called a confusion matrix). The error matrix organizes the acquired sample data in a way that summarizes key results and aids the quantification of accuracy and area. This is a simple cross-tabulation that compares the (algorithm assigned) map category labels to the (human assigned) reference category labels (your validation classification). The count for each pairwise combination are included in the blue and yellow cells in the following example.

.. figure:: ../_images/workflows/area_estimation/confusion_matrix_example.png
   :alt: A confusion matrix example.
   :align: center

-   The main diagonal of the error matrix (blue cells) includes the count of the number of correct classifications.
-   The off-diagonal elements (yellow cells) show map classification errors.
-   The user's accuracy can be quantified by dividing the number of correctly classified plots by the sum of the plots classified as the mapped class. For the forest class in the example above, this is 17 correctly identified points divided by 19 total forest plots. User's accuracies for each class are shown in the orange cells. User's accuracy is the complement of errors of commission (sites that are classified as forest in the map, but are not actually forest).
-   The producer's accuracy can be quantified by dividing the number of correctly classified plots by the sum of the plots classified as the mapped class in the validation reference sample. For the forest class in the example above, this is 17 correctly identified points divided by 20 samples that were classified as forest from the reference data. Producer's accuracies for each class are shown in the pink cells. Producer's accuracy is the complement of errors of omission (sites that are not classified as forest in the map that are actually forest).


For your own data, calculate an error matrix following the above guidelines:

.. figure:: ../_images/workflows/area_estimation/example_error_matrix.png
   :alt: An example error matrix.
   :align: center

Here's a completed example for a project using 4 classes:

.. figure:: ../_images/workflows/area_estimation/example_error_matrix_4class.png
   :alt: Example error matrix for a 4 class project.
   :align: center

In this example, the user's accuracy for Forest is 94.7%; so the error of commission is 5.3%. The user's accuracy for water is 90%, which means the error of commission is 10%. What this means is that according to the reference data, the map creator mapped 5.3% of Forest land cover in the wrong class and 10% of water in the wrong class. The producer's accuracy for Forest is 75%, meaning the error of omission is 25%. The producer's accuracy for water is 90%, so the error of omission is 10%. This means that 25% of the forest reference samples were mapped in the wrong land cover class, while only 10% of water was mapped in the wrong class. Calculate the errors of omission and commission for Other and Cloud land cover classes.

Once the error matrix is created, the area estimation becomes straightforward. Essentially, we use the frequency of these errors of omission and commission for each map class to calculate updated map areas based on our knowledge of how likely each class is to be classified as something else. We can also calculate the uncertainties for the total area of each class.

At the heart of the analysis is the implementation of an unbiased area estimator. Different estimators can be implemented to assess accuracy. In the next part, you will use a stratified estimation since you have a sample stratified by the discrete map classes.

.. _section 4.3.2:

Preparing your CEO collected data for analysis in SEPAL
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. note::

    This step is fully optional

Open the .csv file you downloaded from Collect Earth Online in `section 4.2.3`_. It will probably have a name like “ceo-project-name-sample-data-yyyy-mm-dd.csv”. Inspect the column data.

You should have:

-   A column named “PL_MAP_CLASS” that consists of numeric values. These are the classes assigned by the classification.
-   A column with your question about the correct map class as the column header. In this example, it is “IS THIS FOREST OR NON-FOREST”.

These are the classes you assigned manually in CEO based on map imagery. This will either be numeric (1 or 2) or text (Forest and Non-forest) depending on how you set up your Collect Earth Online project.

.. note::

    If your column for the correct map class is numeric, you can directly save your .csv file and upload it to SEPAL.

If your column for the correct map class is text, you will need to either:

-   Check that your text column matches exactly the Legend Labels you added during sample design (Exercise 4.1).
-   Check that capitalization is the same, e.g. Non-forest and Non-forest not Non-forest and non-forest.
-   OR Create another column with the associated numeric value. In this very case:

    -   First, create a new column and name it COLLECTED_CLASS.
    -   In the formula cell, type: =IF([text column letter]2="Forest",1,2). For this example, the text column letter is U.

        .. note::

            This will use an if statement to assign the number 1 to sample plots you assigned the value “Forest” to, and the number 2 to other plots (here, plots labeled Non-forest). If you have more than two classes, you will need to use nested IF statements.

    -   Press enter. You should now see either a 1 or a 2 populate the column. Double check that it is the correct value.
    -   Fill the entire column.

.. figure:: ../_images/workflows/area_estimation/example_dataset.png
   :alt: An example dataset
   :width: 400
   :align: center

Finally Save your .csv file and upload it to SEPAL.

.. _section 4.3.3:

Using the stratified estimator in SEPAL
"""""""""""""""""""""""""""""""""""""""

The aim of this stratified sampling design tool is to analyze results from a stratified sampling design that can be used for area estimates. The idea is to combine a map (used as a stratification of the landscape of interest) with a visual map interpretation of samples to produce an area estimation.

The concept is derived from map accuracy assessment principles: characterized frequency of errors (omission and commission) for each map class may be used to compute area estimates and also to estimate the uncertainties (confidence intervals) for the areas for each class.

First, open the Stratified Area Estimator-Analysis Tool. In the Apps SEPAL window select Stratified Area Estimator - Analysis. This tool is very similar to the Design tool that you used to create your stratified sample.

You will land on the **Introduction** page which allows you to choose your language and provides background information on the tool. Note that Reference and Documents are in the same place as the Design tool. The pages that contain the necessary steps for the workflow are on the left side of the screen and need to be completed sequentially.

.. figure:: ../_images/workflows/area_estimation/stratified_estimator_analysis_tool.png
   :alt: The stratified estimator analysis tool.
   :align: center

Select the **Inputs** page on the left side of the screen. You will see two data requirements under the **Select input files** section.

-   **Reference Data**:  this refers to the table that you classified and exported in the previous section. It will contain a column that identifies the map output class for each point as well as a column for the value from the image interpreter (validation classification).

    -   For projects completed in CEO: Select the **Reference data** button and navigate to the .csv file you downloaded from CEO and then uploaded to SEPAL in `section 4.3.2`_.
    -   For projects completed in CEO-SEPAL bridge:
        -   Check that you are logged out of the Collect Earth Online website.
        -   Paste the URL from your CEO-SEPAL bridge project into the field marked **CEO url**. You can also click the **Paste CEO url from clipboard** button.
        -   Click :code:`Import CEO project`. This will populate the input file for the Reference data as well as the column names.

-   **Area data**:  this is a CSV that was automatically created during the Stratified Area Estimator--Design workflow. It contains area values for each mapped land cover class.

    -   Click the **Area data** button.
    -   Open the **sae_design_AmazonClassification** folder, or the folder labeled :code:`sae_design_your-name-here` if you did not call your classification **AmazonClassification**. As a reminder, if you exported your classification to the SEPAL workspace, the file will be in your SEPAL downloads folder. (downloads > classification folder > sae_design_AmazonClassification). Within this folder, select **area_rast.csv** (see image below).

.. figure:: ../_images/workflows/area_estimation/add_classification.png
   :alt: Adding the classification
   :width: 450
   :align: center

Next, you will need to adjust some parameters so that the tool recognizes the column names for your reference data and area data that contain the necessary information for your accuracy assessment. You should now see a populated **Required input** panel on the right side of the screen.

Choose the column with the reference data information.

.. note::

    -   For projects completed in CEO: This will either be your question name or the new column name you created in Part 2 above. Here it is COLLECTED_CLASS following the directions in `section 4.3.2`_.
    -   For projects completed in CEO-SEPAL: ref_code

Choose the column with the map data information

.. note::

    -   For projects completed in CEO: PL_MAP_CLASS
    -   For projects completed in CEO-SEPAL: map_code

Choose the map area column from the area file—map_area
Choose the class column from the area file—map_code or map_edited_class. The map_edited_class has the names you entered manually during the design phase, while the map_code has the numeric class codes.

.. note::

    -   For projects completed in CEO: Use map_code if you have a column in your reference data. If you use map_edited_class you must make sure that capitalization.
    -   For projects completed in CEO-SEPAL, use map_code.

You can add a **Display data** column to enable validation on the fly. You can choose any column from your CEO or CEO-SEPAL project. We recommend either your map class (e.g. PL_MAP_CLASS) or your reference data class (e.g. question name column). This example uses a CEO project.

.. figure:: ../_images/workflows/area_estimation/required_input_fields.png
   :alt: The required input fields.
   :width: 450
   :align: center

Once you have set these input parameters, select :code:`Check` on the left side of the window. This page will simply plot your samples on a world map. Fix the locations of your plots by specifying the correct columns to use as the X and Y coordinates in the map. Click the drop down menus and select the appropriate coordinate columns for X and Y coordinates. X coordinate should be LON; Y coordinate should be LAT.

Next, click the :code:`Results` page on the left side of the screen.

The **Results** page will display a few different accuracy statistics, including a **Confusion Matrix, Area Estimates,** and a **Graph** of area estimates with confidence intervals. The Confusion Matrix enables you to assess the agreement of the map and validation data sets.

The rows represent your assignments while the columns represent the map classifier's. The diagonal represents the number of samples that are in agreement, while the off diagonal cells represent points that were not mapped correctly (or potentially not interpreted correctly).

.. figure:: ../_images/workflows/area_estimation/confusion_matrix_output_sepal.png
   :alt: The confusion matrix output by SEPAL.
   :width: 450
   :align: center

Typically you would have to create the confusion table yourself and calculate the accuracies, however, the SAE-Analysis tool does this for you.

.. seealso::

    -   If you completed section `section 4.3.1`_, how does the SAE-Analysis tool's calculations compare with your own?
    -   You can download confusion matrix as tabular data (.csv) using the button.

Under **Area estimates**, the table shows you the area estimates, and producer's and user's accuracies, all of which were calculated from the error matrix and the class areas (sample weights) from the map product you are assessing.

Estimations are broken up into simple and stratified estimates, each of which has its own confidence interval. In this exercise we collected validation data using a stratified sample, so the values we need to use are the stratified random values. Note that all area estimates are in map units. You can change your desired **confidence interval** using the slider at the top of the panel. You can Download area estimates as tabular data (.csv) using the button.

.. figure:: ../_images/workflows/area_estimation/area_estimate.png
   :alt: The area estimates screen in SEPAL.
   :align: center

The **Graph** plots area estimates based on: map pixel count, stratified random sample, simple random sample, unbiased stratified random and direct estimate stratified random.

In this exercise we collected validation data using a stratified sample, so the values we need to use are the stratified random values. Need to define unbiased stratified random and direct estimate stratified random.

.. note::

    Note that the Map pixel count value differs from these stratified random sample estimates. This shows how using a map pixel count is a poor estimation of actual area.

.. figure:: ../_images/workflows/area_estimation/area_estimate_graph.png
   :alt: A graph of the area estimates based on different sample design.
   :width: 450
   :align: center

.. _module 5:

Documentation and archiving
---------------------------

Documentation of your area estimate and archiving this information for future reference are critical in order to replicate your estimation process. Examples where you would want to repeat your analysis include different areas (states, provinces, ecological regions) or time periods (months, years).

We have built in documentation steps into other Modules of this Manual, however here we bring this information together. We discuss key documentation steps, including logging decision points (`section 5.1`_), Reporting (`section 5.2`_), Commenting in code (`section 5.3`_), and Version control (`section 5.4`_), as well as archiving steps (`section 5.5`_).

This module should take approximately 1 hour to read. The time taken to complete this module for your specific situation will vary depending on the size and scope of your project.

.. _section 5.1:

Logging decision points
^^^^^^^^^^^^^^^^^^^^^^^

Logging decision points is a critical part of documenting your area estimation process and being able to recreate your estimation process.

A decision point is anywhere where you make a decision about your project that can change the outcome. For example, “We decided that pixels with over 75% tree cover should be classified as Forest cover” is a decision point.

In the previous Modules, we have suggested that you document these types of decision points as you go along. This includes:

* `module 2`_:

  * Logging your land use decision tree (`section 2.1`_).
  * Logging your land use classification definitions (`section 2.1`_).
  * Settings used for classification, along with any refinements (`section 2.4`_).

* `module 3`_:

  * Logging two date change detection decisions, including what classes can change and imagery and processes used in the classification (`section 3.1`_)

* `module 4`_:

  * Stratification choices (`section 4.1`_).
  * Data collection procedures (`section 4.2`_).

You may also choose to follow your organization's Standard Operating Procedures. For example: https://drive.google.com/file/d/1u4sXx6Y8qPKvbIYJFide5EI6L_ygpS5p/view?usp=sharing.

.. _section 5.2:

Reporting
^^^^^^^^^

Writing a report summarizing your findings is a critical part of your area estimation. If you are conducting an area estimation for internal use, this report will provide you with a blueprint for future estimations. If you are conducting an area estimation for another organization, this report will convey your results and the quality of your analysis.

Here we provide a rough outline of what you should include in your reporting.

In your report, you should include:

-   An introduction, describing why the project was completed and any goals of the project.
-   Your project's methods, that is how your project was completed. it should include:

    -   All tools used in your analysis.
    -   All decision points (`section 5.1`_)
    -   Any other information needed to recreate your project.

-   Your project results:

    -   Your area estimation (`section 4.3`_).
    -   The error associated with your classification (`section 4.3`_).
    -   A comparison of any self checks (one interpreter) and cross checks (between interpreters) with the main sets of plots.

-   Any actions or next steps arising from your analysis.

Writing your report will take time and attention. Documenting your steps along the way, as discussed in Modules 1-4 and Exercise 5.1 will help you write your report more efficiently.

.. danger::

    **Always follow your organization's reporting guidelines**. For example, if your estimation is developed to support a National Forest Monitoring System, you will need to comply with UN reporting standards.

As another example, FAO's Standard Operating Procedure requires reports include at least the following information about the data collection process:

-   A brief narrative on the modalities for data collection
-   The interpreters, their contact information, institutions and roles
-   Overview of sample unit allocation to interpreters and any subsequent revisions made to the allocation
-   A summary of the training conducted that details the topics covered
-   A list of attendees for the training and their attendance record
-   Challenges and limitations during the data collection
-   Potential sources of bias during the data collection
-   Impossible transitions excluded from data collection
-   The results of the assessment of interpretation quality
-   External appraisal of interpretation quality contact information and narrative report from the appraiser

.. _section 5.3:

Commenting in Scripts
^^^^^^^^^^^^^^^^^^^^^

While none of the steps involved in this manual require writing code, more complex classification projects may use programming environments such as Google Earth Engine. This Exercise discusses best practices for commenting your code if you use tools such as Google Earth Engine.

Leaving comments in your code can be a helpful way to describe information of what a particular function does, leave warnings or considerations to other programmers (including your future self!), provide key information on licensing, or save information on what you still want to complete while coding. In this section we will briefly demonstrate both good and bad commenting techniques.

When commenting your code you should take into account your target audience. Is your code going to be used for a workshop? Will it be read by other scientists or programmers? Or will you lose access to it after submitting it to a publication or project partner? Answering these questions will help you determine what approach to take when commenting your code.

Many of these tips are derived from the suggestions laid out in Robert C. Martins' book *Clean Code*, which would be a good reference if you would like to learn more about coding cleanly and commenting:

-   **Keep comments short**. Keeping your comments short is helpful to both the writer of the comment and the reader. Having multiple long comments in your code can lead to readers skipping over them and thus making them inefficient. Long comments can start to clutter your code.

- It is best to use comments **sparingly** and when possible **rename variables** or use functions to reflect what you would like to have commented. Comments can quickly become outdated and are less of a priority to update. Comments are a representation of what your code does, but can sometimes be misleading.

-   Using comments to add some informative content or explain the intent behind your code, but **don't be redundant**. Informative comments are little snippets of information that aid in reading through your code. A comment explaining your intent can be useful where the processing you have done is slightly complicated to read through.

-   **Don't leave in commented out code**. Leaving in commented out code quickly becomes confusing. Is the commented out code something new that is to be implemented? Is it something that was broken and the other code fixed? Should it be uncommented to provide a different result? It is best to use a form of version control so you can safely delete these lines and go back to them if you need to later.

-   Try to **not be redundant** with comments. Comments that simply reiterate what the code is doing often are not helpful and will add to clutter. Use comments to clarify what the code is doing. This is nice for when you are using code in a workshop, or perhaps in a final version which is released with a publication that will not be changed later.

-   Do be careful as just like with other comments, errors in them are just as bad as in your code!

Here are three examples of comment types:

Comments that clarify:

.. code-block:: javascript

    ////////////////////////////////////////////////////////
    // User defined variables                            ///
    ////////////////////////////////////////////////////////

    // Main variables for defining region of interest,
    // start and end period, and sensors to include

    // Available sensors are : Landsat, Sentinel2, Sentinel1,
    var sensor = 'Landsat';

Comments that are informative:

.. code-block:: javascript

    // returns most recent image with time series of images as property
    Return ee.Image(latestImagery)

Comments that describe intent:

.. code-block:: javascript

    // This is the best way I found to add images to the target image as a property
    var processMetaData = imageCollection.map(function f (img){
        var imageDate = img.get('system:time_start')
        var previousImages = otherImageCollection.filterDate(imageDate.advance(-1,'month') , imageDate).filterBounds(img.geometry().bounds())
        return img.set('images', previousImages.toList())
    });

And here is an example where comments (A) can be replaced by variables (B).

.. code-block:: javascript

    /////////////////////////////////////////
    //      example A: using comments      //
    /////////////////////////////////////////

    // Did the user pass in a year range that is within the valid range for
    // the selected satellite?

    if(dateInputBox.getValue().includes(sensorDateRangeDict[sensorInputBox.getValue()]){
        // run analysis for date range
        var results = myAnalysis(dateInputBox.getValue(),sensorInputBox.getValue())
    }

.. code-block:: javascript

    ///////////////////////////////////////////////
    //      example B: using variable names      //
    ///////////////////////////////////////////////

    var selectedDateRange = dateInputBox.getValue()
    var selectedSensor = sensorInputBox.getValue()
    var selectedSensorDateRange = sensorDateRangeDict[selectedSensor]

    if( selectedDateRange.includes(selectedSensorDateRange)) {
        var results = myAnalysis(selectedDateRange, selectedSensor)
    }

In this example above you can see that you write roughly the same number of lines of code with and without comments. However, by adding descriptive variable names, the code itself becomes simpler to understand.

Finally, note that reading the actual code will always be truer than reading the comments. In the first example it poses the question: “Did the user pass in a year range that is within the valid range for the selected satellite?“ But what if you choose to include aerial imagery or UAV data sources at some point? Chances are you won't feel compelled to go back and update your comment.

.. _section 5.4:

Transparent coding: GitHub and saving GEE scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to commenting your code so that future users can understand what is being done, saving your code is another important part of project documentation. As in `section 5.3`_, this exercise is only relevant if you have implemented code in your area estimation, such as through Python or Google Earth Engine.

In this exercise we will touch upon how to be transparent with your code and save your code. Any time you are writing a script or some code, it is probably a good idea to have a version control system in place so you can track your changes, and have a backup in case a mistake happens to your code. We discuss this in two contexts: Git for local code, and Google Earth Engine's approach to version control.

Version Control and Git
"""""""""""""""""""""""

Version control is “a system that records changes to a file or set of files over time so that you can recall specific versions later” (Git 2020; Online at: https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control). Version control can be applied to many different file types, but is most commonly used with text based code, such as Python and R scripts.

.. note::

    The following explanation is adapted from the Software Carpentry Git lesson.

We'll start by exploring how version control can be used to keep track of what one person did and when.

We've all been in this situation before: it seems ridiculous to have multiple nearly-identical versions of the same document. Some word processors let us deal with this a little better, such as Microsoft Word's Track Changes, Google Docs' version history, or LibreOffice's Recording and Displaying Changes.

Version control systems start with a base version of the document and then record changes you make each step of the way. You can think of it as a recording of your progress: you can rewind to start at the base document and play back each change you made, eventually arriving at your more recent version.

.. figure:: ../_images/workflows/area_estimation/version_control_system.png
   :alt: Figure showing how version control systems work

Once you think of changes as separate from the document itself, you can then think about “playing back” different sets of changes on the base document, ultimately resulting in different versions of that document. For example, two users can make independent sets of changes on the same document.

.. figure:: ../_images/workflows/area_estimation/version_control_multiple_contributors.png
   :alt: Version control with multiple contributors

A version control system is a tool that keeps track of these changes for us, effectively creating different versions of our files. It allows us to decide which changes will be made to the next version (each record of these changes is called a `commit <http://swcarpentry.GitHub.io/git-novice/reference.html#commit>`_, and keeps useful metadata about them. The complete history of commits for a particular project and their metadata make up a `repository <http://swcarpentry.GitHub.io/git-novice/reference.html#repository>`_. Repositories can be kept in sync across different computers, facilitating collaboration among different people.”

Of version control systems, Git (and implementation GitHub that includes a GUI Desktop version) is perhaps the most widely used. Here we provide a very basic overview of Git and links to additional resources.

Git is a popular free and open source software for a distributed version control system and is the basis of GitHub. With a GitHub account, you can create repositories to hold your code and track the changes you make to it as you develop it. GitHub stores all your code, which means that even if something happens to your computer, your code will be saved.

This is also a great way to share or collaborate on code. You can easily send a link to your repository to whomever you want, and you could have other scientists working on one portion of the code on their home computer while you do as well.

.. seealso::

    If you would like to learn more about git or version control, you can work through the Software Carpentry workshop at your own pace here: http://swcarpentry.GitHub.io/git-novice/.

You can work through how to set up a git repository system for yourself or your organization (unpaid but must run locally or on your own servers).

.. note::

    -   Information on Git can be found here: https://git-scm.com/.
    -   Information on GitHub, including how to sign up, can be found here: https://github.com/ (GitHub has free and paid service tiers).

.. tip::

    With https://zenodo.org/ and GitHub together, you can create DOI numbers for versions of your code for publication.

Google Earth Engine version control
"""""""""""""""""""""""""""""""""""

Google Earth Engine has implemented version control and version history for all scripts and repositories written on the platform. To access the version control, click the history icon next to a script in order to compare or revert it to an older version.

.. figure:: ../_images/workflows/area_estimation/gee_scripts.png
   :alt: The GEE scripts tab.
   :width: 450
   :align: center

Detailed information can be found under “Development Environments: Earth Engine Code Editor” here: https://developers.google.com/earth-engine/guides/playground

.. figure:: ../_images/workflows/area_estimation/earth_engine_code_editor.png
   :alt: Earth engine code editor
   :align: center

.. _section 5.5:

Data archiving and creating metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Finally, we will discuss the information needed for proper data archiving, which overlaps significantly with creating metadata for your area estimation. Metadata is a set of data that provides information about other data, such as your classification and area estimation data.

Data archiving
""""""""""""""

For data archiving, the following information needs to be compiled:

-   A database of the sample data collected by the interpreters including:

    -   The geographical coordinates in define coordinate or projection system.
    -   The unique identification code for each sample unit.
    -   The interpretation of all sample units including the previous interpretation(s) of the sample unit in the case this was revised or corrected.

-   The interpretation of sample units conducted by the coordinator.
-   Metadata regarding the interpreter that collected the sample data, when the data was collected, which data sources were used.

Think about the work you did in completing Modules 1-4. What other data do you think should be archived? What would be helpful to your colleagues or yourself in the future looking to replicate your work?

You should store the data collection report, your data tables, any metadata, etc. in a standard format. When naming files you should follow a naming convention such as Data collection_data_date[year/month/day]_version number (FAO SOP). When writing your documentation report, you should include links to your data storage locations.

Creating metadata
"""""""""""""""""

This worksheet is designed to assist you in becoming more efficient and informed about documenting and archiving information relating to the planning, preparation, and management of remote sensing dataset and analysis, such as analyses conducted for forest inventory monitoring (e.g. REDD+ activities).

Documentation and archiving remote sensing analysis methods ensures there is transparency and makes it easier to replicate or improve methods as programs increase in complexity and robustness. For more information on the good practice recommendations for documentation, archiving and reporting please refer to the 2006 IPCC Guidelines Vol. 1 Chp. 6 Section 11.

Below we have provided you with headings and some questions for each step in the metadata creation process, that is, where you should provide information about your workflow in order to ensure transparency about your data and processing steps and comply with best practices. The information you provide below should be sufficient and clear enough so that someone else can understand how the analysis was conducted and would be able to replicate it.

When completing this exercise, think about the work you have completed in the 4 first modules. When you conduct your own classification and area estimation processes in the future, take the time to customize and add additional sections to this document. This exercise is designed to get you started in this practice and moving down the right path.

.. csv-table::
    :header: Preparing and Downloading Cloud-free Composite Using Google Earth,
    :widths: 50, 50

    Data used                         ,
    Time frame for composite          ,
    Software used                     ,
    Pre-processing methods             ,
    Methods for cloud removal         ,
    Assess RS results                 ,
    Assumptions (Note: Need to archive outputs before proceeding with analysis),

.. line-break::

.. csv-table::
    :header: "Creating Band Ratios, Indices and Image \Transformation for use in Classification and Change Detection Analysis",
    :widths: 50, 50

    Software used,
    Description of indices,
    Assess RS results,
    Assumptions (Note: Need to archive outputs before proceeding with analysis),

.. line-break::

.. csv-table::
    :header: Image Classification Scheme,
    :widths: 50, 50

    "Document Clear definitions for classes or categories (i.e., land use categories defined by the IPCC as: Forest Land, Cropland, Grassland, Wetlands, Settlements, and Other Land)",
    "Have you identified any categories as \“Key Categories\”? How is the analysis different?  Please refer to Volume 1, Chapter 4 of the 2006 IPCC Guidelines on what defines a \“Key Category\”.",
    Assess RS results,
    Assumptions (Note: Need to archive outputs before proceeding with analysis),

.. line-break::

.. csv-table::
    :header: Collect Reference Data,
    :widths: 50, 50

    What type of reference data are you using?,
    What is your sampling scheme and what is the logic for its design?,
    Assess RS results,
    Assumptions (Note: Need to archive outputs before proceeding with analysis),

.. line-break::

.. csv-table::
    :header: Perform Land Cover Classification or Land Cover Change Analysis,
    :widths: 50, 50

    Software,
    Analysis technique,
    Assess RS results,
    Assumptions (Note: Need to archive outputs before proceeding with analysis),

.. line-break::

.. csv-table::
    :header: Perform Accuracy Assessment,
    :widths: 50, 50

    Sampling approach,
    Analysis technique,
    Assess results,
    Assumptions (Note: Need to archive outputs before proceeding with analysis)

.. line-break::

conclusion
----------

.. important::

    **Congratulations! You have completed the SEPAL-CEO Area Estimation cookbook!**

Now you know:

-   How to perform an accuracy assessment and generate area estimates in SEPAL
-   How to conduct a two-date change detection classification in SEPAL
-   How to create a stratified random sampling design for your map and a project (CEO or CEO-SEPAL) to collect reference data
-   How to create a Landsat mosaic using the many customizable parameters in SEPAL
-   How to collect training data in SEPAL's classification interface
-   How to produce map classifications in SEPAL
-   How to assess important quality assurance metrics for your project
-   How to log key decision points for your project!
-   How to comment code
-   How to use version control options for your project!
-   How to report your area estimation project

.. spelling::

    AmazonClassification
    sae
    ceo
    mapathon
    sourcebook
    plotid
    SriLanka
