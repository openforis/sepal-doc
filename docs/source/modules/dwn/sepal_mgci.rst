SEPAL-SDG 15.4.2 :sub:`beta`
============================

*A tool to support the computation of SDG Indicator 15.4.2 Indicator 15.4.2: (a) Mountain Green Cover Index and (b) Proportion of degraded mountain land using SEPAL (System for Earth Observation Data Access, Processing, and Analysis for Land Monitoring). *

This guide will introduce you to SEPAL-SDG 15.4.2 :sub:`beta` and will provide you detailed instructions on how the set it up and carry out the computation of both sub-indicators in a step-by-step manner. Screenshots are included to make it easier for the user to know what each description refers to.


General Information
-------------------

About SEPAL-SDG 15.4.2 :sub:`beta`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SEPAL-SDG 15.4.2 :sub:`beta` has been developed by the Food and Agriculture Organization (FAO) of the United Nations to support  national authorities to compute and report against SDG Indicator 15.4.2. SEPAL-SDG 15.4.2 :sub:`beta` is built on SEPAL, an open-source cloud-based platform that allows users to query and process satellite data quickly and efficiently, tailor products for local needs, and produce sophisticated and relevant geospatial analyses quickly. To know more about SEPAL visit the `SEPAL website <https://docs.sepal.io/en/latest/>`_.

SEPAL-SDG 15.4.2 :sub:`beta` is in a beta stage and therefore it is still under development. If you have specific bugs to report or improvements to the tool that you would like to suggest, please use the `GitHub’s issue tracker <https://github.com/dfguerrerom/sepal_mgci/issues>`_ of SEPAL-SDG 15.4.2 :sub:`beta` and do follow the `contribution guidelines <https://github.com/dfguerrerom/sepal_mgci/blob/master/CONTRIBUTE.md>`_.

Authors
^^^^^^^

SEPAL-SDG 15.4.2 :sub:`beta` has been developed by the Food and Agriculture Organization (FAO) of the United Nations, and has been funded by Norway's International Climate and Forest Iniciative (NICFI).

SEPAL-SDG 15.4.2 :sub:`beta` has been developed by Daniel Guerrero. Ann Cheptoo Rotich developed the technical documentation. Xavier de Lamo led and supervised the development of both products.

License
^^^^^^^
SEPAL-SDG 15.4.2 :sub:`beta` is free and open source. It is licensed under `MIT license <https://opensource.org/licenses/MIT>`_. The documentation is made available under the terms of the `Creative Commons Attribution 4.0 International License (CC BY 4.0) <https://creativecommons.org/licenses/by/4.0/>`_. 

Data sources
^^^^^^^^^^^^

SEPAL-SDG 15.4.2 :sub:`beta` draws on a number of global data sources to allow the computation of the SDG 15.4.2 indicator when similar national data is not available. The datasets described below have been made available by the following organizations under separate terms as indicated in their respective metadata.

- **Land cover**: European Space Agency (ESA) Climate Change Initiative (CCI) Land cover, available at `ESA-CCI land cover website <https://maps.elie.ucl.ac.be/CCI/viewer/index.php>`_.
- **Digital Elevation Model**: The Shuttle Radar Topography Mission (SRTM), available at `Google Earth Engine Data SRTM <https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4>`_.
- **Administrative Boundaries**: FAO GAUL: Global Administrative Unit Layers 2015, available at `Google Earth Engine Data FAO GAUL <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1>`_.

**Note:** The  Administrative Boundaries provided in this tool are in the public domain. The designations employed and the presentation of material on this map do not imply the expression of any opinion whatsoever on the part of the Secretariat of the United Nations concerning the legal status of any country, territory, city or area or its authorities, or concerning the delimitation of its frontiers or boundaries. If using SEPAL-SDG 15.4.2 :sub:`beta` for official purposes, it is recommended that users use an official boundary provided by the designated office of their country.

Before using SEPAL-SDG 15.4.2 :sub:`beta`
-----------------------------------------

Initial setup
^^^^^^^^^^^^^
SEPAL is closely linked to Google Earth Engine (GEE), a Google-powered Earth-observation cloud-computing platform, as it builds in many of its functionalities. This means that to run SEPAL-SDG 15.4.2 :sub:`beta` you will need to have **connected SEPAL and GEE accounts**. 

- To **Create a SEPAL account** please follow the `registration steps described here <https://docs.sepal.io/en/latest/setup/register.html#sign-up-to-sepal>`_ and then familiarize yourself with the tool by exploring its interface.
- To **Create a Google Earth Engine (GEE) account** please follow these `steps <https://docs.sepal.io/en/latest/setup/gee.html#create-a-gee-account>`_ and don't forget to `initialize the home folder <https://docs.sepal.io/en/latest/setup/gee.html#initialize-the-home-folder>`_.
- To **Connect your SEPAL and GEE accounts** follow the `instructions described here <https://docs.sepal.io/en/latest/setup/gee.html#connection-between-gee-and-sepal>`_.

Data Requirements
^^^^^^^^^^^^^^^^^
SDG Indicator 15.4.2 requires several spatial data inputs to be computed. These include:

- **A Mountain Area Map:** For the purposes of standardization and international comparability of indicators values, SDG Indicator 15.4.2 adheres to the UNEP-WCMC mountain definition (UNEP-WCMC, 2002). The UNEP-WCMC method defines total global mountain area as the sum of seven classes (commonly known as ‘Kapos mountain classes’), based on elevation, slope and local elevation ranges parameters. This mountain area is subdivided into bioclimatic belts (Nival, Alpine, Montane, and Remaining Mountain Area) based on average temperatures as defined by Körner et al. (2011). A global mountain area map based on these definitions and methodologies has been developed by FAO and is used by default by SEPAL-SDG 15.4.2 :sub:`beta` as part of the computations. 

- **A National Administrative Boundary for the country of interest:** SEPAL-SDG 15.4.2 :sub:`beta` has been conceived to facilitate the computation of of SDG Indicator 15.4.2 at country level. To facilitate access to this , SEPAL-SDG 15.4.2 :sub:`beta` uses as a default global data source for national boundaries: the FAO GAUL Global Administrative Unit Layers 2015 data set. However, the tool also allows national agencies to use their own national country boundary layer if available. 

- **A collection of Land Cover Maps for the country of interest:** Land cover maps represent spatial information on different types (classes) of physical coverage of the Earth's surface, e.g. forests, grasslands, croplands, lakes, wetlands. This data serves different functions for SDG Indicator 15.4.2: In Sub-Indicator 15.4.2a, land cover is used to categorize land into green and non-green cover areas. In Sub-Indicator 15.4.2b, land cover is used to identify areas where changes in the type of land cover may indicate a decline or loss of biodiversity, mountain ecosystem functions or services that are considered desirable in a local or national context. The collection of land cover maps to compute this indicator should be available from the year 2000. Simlarly, to the national administrative boundary dataset, SEPAL-SDG 15.4.2 :sub:`beta` provides access to the default land cover maps selected by FAO to compute the indicator (see Data Sources section). However, it also facilitates national authorities to use relevant national or regional land cover datasets. These datasets should also be available as GEE assets as an `image collection <https://developers.google.com/earth-engine/guides/ic_creating>`_ in order to allow SEPAL-SDG 15.4.2 :sub:`beta` to access it. The next section of the tutorial will explain you how to do this.  

Uploading files into Google Earth Engine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
GEE allows the uploading of different types of data formats: shapefiles, raster images, image collection and CSV tables. This section will show how to upload different data types into the platform.

1. Go to **Assets** in the top left panel in the **Earth Engine Code Editor** page. Clicking on it will open the **Asset Manager**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/setting_up/uploading_gee/new%20button.PNG
   :align: center
   :width: 900
   :alt: GEE_Interface

2. Select **New**. You will have several choices, including **Raster** (Geotiffs or TFRecords), **Vector* (Shapefiles) and **Data tables** (csv files), which will be described in the following subsections.

2.3.1 Uploading a vector file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. In SEPAL-SDG 15.4.2 :sub:`beta` custom country boundaries need to be uploaded in vector format. To do so, choose **Shapefiles**. A pop-up window will appear. Navigate to the location of your data.
2. In the pop-up window, select the file you want to upload from your computer. You can upload the vector data in a compressed mode as a :code:`.zip` file. If not, remember that the a :code:`.shp` file alone is not sufficient and must be accompanied with other files describing the vector data.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/setting_up/uploading_gee/all%20files%20listed.PNG
   :align: center
   :width: 300
   :alt: Vector_File

Any file errors will be highlighted by the uploader, as in the example below:

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/setting_up/uploading_gee/error%20message.PNG
   :align: center
   :width: 500
   :alt: Vector_Error

3. Once all files are loaded correctly, they are displayed in the task manager. Typically this process takes a couple of minutes depending on the size of the dataset. The progress of the upload is displayed in the task manager as shown below:

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/setting_up/uploading_gee/task%20manager.PNG
   :align: center
   :width: 300
   :alt: vector_uploading_process

4. The uploaded assets will be listed in the Assets List under the Assets tab. If not displayed, click on the Refresh button.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/setting_up/uploading_gee/upload_success.PNG
   :align: center
   :width: 700
   :alt: Assets_listed

5. Clicking on the asset will open a pop-window. The asset is ready for use. You can now visualize, share or delete it accordingly it entirely:

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/setting_up/uploading_gee/asset%20details.PNG
   :align: center
   :width: 800
   :alt: asset_popupwindow

Uploading a raster file
^^^^^^^^^^^^^^^^^^^^^^^

1. In SEPAL-SDG 15.4.2 :sub:`beta`, land cover maps need to be uploaded as raster files and made available as an `image collection <https://developers.google.com/earth-engine/guides/ic_creating>`_. To do so, select **Image**.

2. In the pop-up window, select the file you want to upload from your computer (compatible formats include :code:`.tiff`, :code:`.tif`, :code:`.json`, :code:`.tfrecord` or :code:`.tfrecord.gz`; the name of your asset can be changed in the next text field). By default, the asset will be named after the basename. Please ensure that the name includes the reference year of the land cover map.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/setting_up/uploading_gee/geotiff_upload.PNG
   :align: center
   :width: 300
   :alt: Geotiff_upload

3. Repeat step 2 for each of the land cover maps.

4. Once all the land cover maps have been uploaded, you can create an image collection following `Google Earth Engine good practice guidelines on the topic <https://developers.google.com/earth-engine/guides/ic_creating>`_.

Uploading a table file
^^^^^^^^^^^^^^^^^^^^^^
Google Earth Engine allows the upload of tabular data in CSV format. To upload a table file do the following:

1. Select New > **csv file upload**. 
2. In the pop-up window that appears, select the file you want to upload from your computer (note: compatible formats include :code:`.csv`, :code:`.json`).

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/setting_up/uploading_gee/uploading_csv.PNG
   :align: center
   :width: 300
   :alt: Geotiff_upload

.. tip::

   Now you can access and use your assets in SEPAL. As you have already established a connection between your GEE and SEPAL accounts, all your assets are synced and available for you in SEPAL. You will be able to select them from the dropdown or copy/paste them directly from GEE when prompted in SEPAL-SDG 15.4.2 :sub:`beta`

The SEPAL interface and the SEPAL-SDG 15.4.2 :sub:`beta` module
---------------------------------------------------------------

If you are new to SEPAL, it is recommended to take a look over the interface and familiarize yourself with the main tools. A detailed description of the features can be consulted in the `interface documentation <https://docs.sepal.io/en/latest/setup/presentation.html#sepal-interface>`_.


Setting up a SEPAL instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Applications such as the SEPAL-SDG 15.4.2 :sub:`beta` make use of SEPAL instances; running them will use your SEPAL computing resources. Selecting an app automatically initiates the process and starts the smallest instance to run the SEPAL sandbox. However, in some cases, especially where more powerful processing is required, you might need larger instances. For this reason, in some cases you may need manually set up a larger SEPAL instance before running SEPAL-SDG 15.4.2 :sub:`beta`. To do that do the following:

1. Go to the `SEPAL terminal <https://docs.sepal.io/en/latest/setup/presentation.html#terminal>`_ (blue icon in the left panel in the image below) and wait for the instance selector to start.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/defining_e/sepal_terminal.PNG
   :align: center
   :width: 300
   :alt: Geotiff_upload

2. Type the instance name. In our case m2 or m4 should suffice, then press ENTER.
3. Wait for the instance to finish loading.
4. Once completed, go back to the dashboard of the application to launch your app. It will automatically use the instance you have set.

Opening SEPAL-SDG 15.4.2 :sub:`beta`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To open the the SEPAL-SDG 15.4.2 :sub:`beta` module use the `apps tab <https://docs.sepal.io/en/latest/setup/presentation.html#apps-tab>`_ and navigate through the list of apps until you find the module (alternatively, you can type in the search box "SDG 15.4.2"). Once you have find it, click over the app drawer and wait patiently until SEPAL-SDG 15.4.2 :sub:`beta` module is displayed (it may take a few minutes). 

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/defining_e/sepal_app.PNG
   :align: center
   :width: 700
   :alt: MGCI module

The module should look like the image below. As any other SEPAL module, SEPAL-SDG 15.4.2 :sub:`beta` is divided into two main sections:

- **Process drawers**: Located on the top left of the interface. This is where you can find the processing steps to accomplish the goal of the module. In SEPAL-SDG 15.4.2 beta, this is composed by 4 processing steps: Area of interest; Land cover settings; Indicator settings and Results.

- **Help drawers**: Located just below the process drawers. This is used to describe the tool, the objectives and give a background about how it was developed. This is composed by the source code (the module was developed under a MIT license, which means that the development is freely accessible, and the code is public in GitHub); the Wiki (the latest documentation on tool) and the Bug report (use this section to report any unexpected result or behavior. To do so, please follow the `contribution guidelines <https://github.com/dfguerrerom/sepal_mgci/blob/master/CONTRIBUTE.md>`_.)

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/App_landing.PNG
   :align: center
   :width: 700
   :alt: MGCI module

Personalising SEPAL-SDG 15.4.2 :sub:`beta`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SEPAL includes functionalities to personalize the appearance of SEPAL-SDG 15.4.2 :sub:`beta`

**Theme customization:**
You can choose between a dark or light theme. To change the theme, click the light mode icon (highlighted) at the top ribbon of the interface. The application will need to be restarted to apply the changes.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/Theme_light.PNG
   :align: center
   :width: 700
   :alt: MGCI module

**Language selection:**
SEPAL-SDG 15.4.2 :sub:`beta` is currently only available in English. New language versions will be made available soon. 

Calculating SDG Indicator 15.4.2
--------------------------------

Conceptual framework
^^^^^^^^^^^^^^^^^^^^
This section will guide you through the sequence of processing steps to calculate SDG indicator 15.4.2. The main goal is to assess the changes in land cover in mountain areas by bioclimatic belts. The algorithm works using land cover data, a digital elevation model, a mountain area map and a national administrative boundary layer.

Overview of Sub-Indicator 15.4.2a (Mountain Green Cover Index)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Sub-indicator 15.4.2a**, Mountain Green Cover Index (MGCI), is designed to measure the extent and changes of green cover - i.e. forest, shrubs, trees, pasture land, cropland, etc. – in mountain areas. MGCI is defined as the percentage of green cover over the total surface of the mountain area of a given country and for given reporting year. The aim of the index is to monitor the evolution of the green cover and thus assess the status of conservation of mountain ecosystems. 

.. math::
    
    MGCI = (Mountain Green Cover Area n)/(Total Mountain Area)

Where: 

- **Mountain Green Cover Area n** = Sum of areas (in km2) covered by (1) tree-covered areas, (2) croplands,(3) grasslands, (4) shrub-covered areas and (5) shrubs and/or herbaceous vegetation, aquatic or regularly flooded classes in the reporting period n 
- **Total mountain area** = Total area of mountains (in km2). In both the numerator and denominator, mountain area is defined according to UNEP-WCMC (2002).

Overview of Sub-Indicator 15.4.2b (Proportion of degraded mountain land)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Sub-indicator 15.4.2b**, Proportion of degraded mountain land, is designed to monitor the extent of degraded mountain land as a result of land cover change of a given country and for given reporting year. Similarly to sub-indicator ‘’trends in land cover” under SDG Indicator 15.3.1 (Sims et al. 2021), mountain ecosystem degradation and recovery is assessed based on the definition of land cover type transitions that constitute degradation, as either improving, stable or degraded. The definition of degradation adopted for the computation of this indicator is the one established Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services (IPBES).

.. math::

	Proportion Of Degraded Mountain Land = (Degraded Mountain Area n) / (Total Mountain Area) * 100

Where:

- **Degraded mountain area n** = Total degraded mountain area (in km2) in the reporting period n. This is, the sum of the areas where land cover change is considered to constitute degradation from the baseline period. Degraded mountain land will be assessed based on the land cover transition matrix in Annex 1.
- **Total mountain area** = Total area of mountains (in km2). In both the numerator and denominator, mountain area is defined according to UNEP-WCMC (2002).

**Disaggregation:**

Both of these sub-indicators are disaggregated by mountain bioclimatic belts as defined by Körner et al. (2011). In addition, sub-indicator 15.4.2a is
disaggregated by the 10 SEEA classes based on UN Statistical Division (2014).  Those values are reported both as proportions (percent) and area (in square kilometres)

More detailed information on the overall conceptual framework of the indicator is available in the `indicator's metadata <https://unstats.un.org/sdgs/metadata/files/Metadata-15-04-02.pdf>`_.

Let’s us now compute SDG 15.4.2 step-by step using the example of Nepal.


Defining the area of interest (AoI)
-----------------------------------

The calculation of the SDG 15.4.2 will be restricted to a specific area of interest defined by the user. In this first step, you will have the option to choose between a predefined list of administrative layers or to use a custom dataset. 

**1.	Click on the Area of Interest Drawer to define your AoI.** 

A pop-up will display the available options to set your AoI: 

- Administrative definitions
- Custom layers

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/Area_of_Interest.PNG
   :align: center
   :width: 800
   :alt: MGCI module

**2. The Administrative definitions option uses the predifined administrative boundary layers available by default in the module. To define the Area of Interest using this option, do the following:**

- Select **Country** under Administrative definitions. 
- In the dropdown list that will appear, select the country or territory in which you want to calculate SDG Indicator 15.4.2. In this example, we will select Nepal, as shown below.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/Selecting_Nepal.PNG
   :align: center
   :width: 800
   :alt: selecting_nepal

- Click on **Select Area of Interest (AOI)** and the map will display your selection. A corresponding legend is also displayed. The algorithm automatically generates a legend based on the mountain bioclimatic belt classes and the area for each of them as defined in the global mountain map developed by FAO to compute this indicator. 

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/defining_aoi_customlayers.PNG
   :align: center
   :width: 700
   :alt: displaying_nepal

.. warning:: The  administrative boundaries available SEPAL-SDG 15.4.2 :sub:`beta` are extracted from FAO GAUL (Global Administrative Unit Layers) 2015 data set. The designations employed and the presentation of material on this map do not imply the expression of any opinion whatsoever on the part of the Secretariat of the United Nations concerning the legal status of any country, territory, city or area or of its authorities, or concerning the delimitation of its frontiers or boundaries. 

**3. The Custom layers option allow users to use their own national administrative boundary layers. To define the Area of Interest using your own custom administrative boundary layer you have two options: use a vector file that you have previously uploaded in GEE as an asset (GEE asset name option), or use a vector file that you have previously uploaded in your SEPAL environment (Vector file option). To use a GEE asset, do the following:**

- Choose **GEE Asset Name** as your AOI selection method.
- Copy the **Asset ID** in GEE and paste under "Select an asset"
- Specify the column or leave the "Use all features" option to leave the default settings.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/gee_asset_vector_selection.PNG
   :align: center
   :width: 600
   :alt: displaying_nepal

Land cover dataset 
------------------

In this section of the module, you have to indicate which land cover data you want to used in the analysis. If using land cover maps different from the default ones, you will also be requested to set up the land cover legend reclassification rules for Sub-indicator A and B, as well as the land cover transition matrix for computing Sub-Indicator B.

Defining your land cover dataset to be used in the analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**1.	Click on the Land cover dataset in the left panel menu.** A pop-up will ask you to indicate the land cover map you wish to use. 

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/Land_cover_dataset_landing.PNG
   :align: center
   :width: 900
   :alt: land cover module

**2. In the first question of the questionnaire, you have to indicate the land cover maps that you wish to use to compute the indicator. If you want to use your own custom land cover datasets and select :guilabel:`yes` to this question, a new button (Open Parameters Settings) will appear. If you select :guilabel:`no`, the module will automatically use the default global land cover datasets for calculating this indicator (see section Data Sources above). Let's assume that you whish to your own land cover maps**.

- Select :guilabel:`yes` to the first question. Then click on :guilabel:`Open Parameters Settings`

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/custom_dataset_subA.PNG
   :align: center
   :width: 800
   :alt: land cover module

- A new pop-up window will open to allow you to select your the collection of land cover maps as a GEE asset (remember that they must be stored as a `GEE image collection <https://developers.google.com/earth-engine/guides/ic_creating>`_ to be able to be imported. Use the bottom arrow to choose your asset or copy/paste it directly from GEE. Then click on :guilabel:`Get classes`

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/importgeeimagecollection.PNG
   :align: center
   :width: 900
   :alt: land cover module

Reclassify the legend of your land cover map to compute sub-Indicator A
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Once you have specified your custom land cover maps, you will be required to reclassify the legend of your land cover maps into the 10 landcover classes as defined by the UN-SEEA land cover classification, which is the default land cover legend for this sub-indicator.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/reclass_sub_A.PNG
   :align: center
   :width: 900
   :alt: reclass subA

You can do this in two different ways:

- Upload a reclassification matrix table in a csv format, indicating the SEEA land cover equivalent of the classes of your land cover map. To provide the information in this way, click on the arrow icon in the top right corner of the pop-up window. The table must already be uploaded in your SEPAL environment. To learn how to do that, please see the `how to exchange files in SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html#exchange-files-with-sepal>`_. Note that the target values must match with the UN-SEAA classes codes for sub-indicator A (click on the info button at the top of the table for information on how the SEEA classes are codified into numbers).

.. _reclass_table:
  .. tip:: What is a reclassification matrix table?:

     A reclassification matrix is a comma-separated values (CSV) file used to reclassify old pixel values into new ones. The CSV file only has to contain two values per line, the first one refers to the `from` value, while the second is the `target` value, just as it is described in the following table: 

      .. csv-table:: Reclassification table example
         :header: "Origin class", "Target class"
         :widths: auto
         :align: center

         "311", "1"
         "111", "5"
         "...","..."
         "511", "4"

- Directly specify the reclassification rules by manually indicating the SEEA land cover equivalent (in the destination class column) of each of the land cover classes of your land cover map (in the original class column). After manually reclassifying your legend, you can use the save button at the top of the table to store the table as a CSV file, and use it in a future calculation instead of manually filling up the table.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/Reclassify_landcover.PNG
   :align: center
   :width: 800
   :alt: Reclassify table

In our example, we will reclassify Nepal’s national land cover class using the following guide:

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/reclassification_guide_subA.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

- Once you have reclassified all the land classes for Sub-Indicator A, click on "Reclassify Land Cover for Sub-Indicator B"

Reclassify the legend of your land cover map to compute Sub-Indicator B
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This step allows you to reclassify the legend of your land cover map for computing Sub-Indicator B. 

In contrast to Sub-Indicator A, the land cover legend used for the calculation of Sub-Indicator B does not necessarily have to be the 10 UN-SEEA classes mentioned earlier. In this sub-indicator, the UN-SEEA legend can be adapted to the national context to ensure that it adequately captures the key degradation and improvement transitions identified in the prior step. For instance, a given country may decide to differentiate "natural forests" from "tree plantations" in sub-indicator B. 

For this reason, this step allows users to apply a new reclassification, or alternatively, used the same reclassification rules as in Sub-Indicator A. In the latter case. In any of both cases, users will need to upload the land cover reclassification rules in a csv file, following the same method as in the prior step.

Upload a transition matrix for computing Sub-Indicator B
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This step should only be completed if you have prodivded different land cover reclassification rules for Sub-Indicator B in the prior step. In such a case, in this step you will need to upload a land cover transition matrix, defining which land cover transitions are considered to be “degradation” and “improvement”, consistent to the legend you have provided in the prior step. This will allow SEPAL-SDG 15.4.2 :sub:`beta` to compute this sub-indicator in the next processing steps. 

Here again the transition matrix should have been previously uploaded in your SEPAL environment as a csv file, containing the following columns: from_code, to_code, impact_code, columns names have to be exactly the same.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/4_transition_matrix.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

Changing the default land cover transition matrix for computing Sub-Indicator B using the default global land cover data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SEPAL-SDG 15.4.2 :sub:`beta` allows the user to modify the default land cover transition matrix without needing to provide a custom land cover map. This allow national authorities to adapt the transition matrix to to the local context and in this way better capture the main land degradation processes occurring in the country without needing to provide alternative land cover data.

This can be done selecting :guilabel:`Yes` in the second question of the land cover dataset questionnaire, and then clicking on "Open Parameter Settings".

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/Yes_to_second_question.PNG
   :align: center
   :width: 800
   :alt: Reclassify table

This will open a pop-up window including the default land cover transitions matrix, showing positive land cover transitions in green, negative in red, and stable/neutral transitions in blue. The matrix can be directly modified by clicking on each cell and changing the sign of the transition.


.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/Modify_default_transitions.PNG
   :align: center
   :width: 900
   :alt: Reclassify table

Once finished, just click outside the window and move to the next processing step: Indicators Settings.

.. note::

   Adapting the default land cover transition matrix using the default global land cover data should be carefully considered. Decisions about which land cover transitions are linked to a degradation or an improvement process in the context of sub-indicator B should be made taking into account the expected change in biodiversity and the mountain ecosystem functions or services that are considered desirable in a local or national context. For these reasons, FAO recommends to consider as degradation all land cover transitions that involve changes from natural land cover types (such as forests, shrublands, grasslands, wetlands) to anthropogenic land cover types (artificial surfaces, cropland, pastures, plantation forests, etc.) as a general rule, given that land use change is known to be the primary driver of biodiversity loss (IPBES, 2019).

Indicators settings
-------------------

Now that we have defined our area of interest and the land cover data to be used in the analysis, together with the land cover legend reclassification rules and associated transitions matrix, click on the **Indicator Settings drawer** to start setting the parameters that the tool will need in the computation of the sub-indicators.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/Indicator_settings.PNG
   :align: center
   :width: 900
   :alt: Reclassify table

From here on, let’s tackle the sub-indicators individually.

Defining parameters for Sub-indicator A: Mountain Green Cover Index
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**1. Click on the add layer icon (highlighted below) to define the years for which the indicator will be calculated**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/sub_indicatorA.PNG
   :align: center
   :width: 600
   :alt: Reclassify table

**2. In the pop-up window that will appear you need to link each of the land maps (either the default ones or the custom ones that you may have uploaded in the prior steps) to the corresponding reference year of each map. You can report one or multiple years. To increase the number of years to be reported, just click on the + sign to define additional years that you need to report.** 

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/sub_a_reporting_years.PNG
   :align: center
   :width: 500
   :alt: Reclassify table

.. note::

   Remember that reporting years for Sub-indicator A are 2000, 2005, 2010, 2015 and subsequently every 3 years (2018, 2021, 2024,...). If you are using custom national land cover maps that are not annually updated and does not exactely match reporting years (for example, you may have a land cover map for 2004 instead of 2005), the tool will automatically interpolates values for the reporting years based on the years for which land cover data is available. 

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/defining_multiple_years.PNG
   :align: center
   :width: 400
   :alt: Reclassify table

**3.	When finished, press OK. The list of reporting years will now be listed at the bottom of the Sub-Indicator A box.**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/defining_multiple_results.PNG
   :align: center
   :width: 500
   :alt: Reclassify table

Defining parameters for Sub-Indicator B: Proportion of Degraded Mountain Land.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In contrast to Sub-Indicator A, in Sub-Indicator B the extent of degraded mountain land is calculated first in the baseline period 2000 - 2015. This baseline sets the benchmark ​from which the extent of land degradation is measured and monitored​ every 3 years after 2015. Put simply, new land cover degradation in the reporting periods (2018, 2021, 2024, ...) is added to the baseline to estimate the current extent of land cover degradation.  This is why in this instance the tool automatically uses the 2000-2015 as baseline.

**1. Define your landcover maps for the baseline years (2000 and 2015) by linking each of the land maps to the corresponding reference year of each map. If you are using custom national land cover maps that does not exactely match reporting years of the baseline, select the map whose reference year is closest to the reporting year (For example, you could select a land cover map for 1998 for the reporting year 2000).**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/sub_B_baseline.PNG
   :align: center
   :width: 500
   :alt: Reclassify table

**2. Then define the land cover maps for each of the reporting years and click OK**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/subB_reporting_years.PNG
   :align: center
   :width: 500
   :alt: Reclassify table

Calculation of SDG Indicator 15.4.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Once you have set the parameters of each sub-indicator, the tool is now ready to run as shows below:

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/calculate_mgci.PNG
   :align: center
   :width: 600
   :alt: Reclassify table

**1. Click on the "Calculate MGCI" to initiate the computation.**

**2. Once is completed, you should see something like the image below:**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/MGCI_done..PNG
   :align: center
   :width: 600
   :alt: Reclassify table

.. tip::

   SEPAL-SDG 15.4.2 :sub:`beta` calculates the indicator values assuming a planimetric area methods by default. To calculate indicator values using a real surface area method (a method that takes into account the third dimension of mountain surfaces through the use of digital elevation models and is known to derive closer estimates of the real surface area of mountain regions), click on "Use Real Surface Area"

3. The entire process is done "on the fly” and thus you need to export your reporting tables to visualize and use them when required. To do that, click on  the "Export Reporting Tables". When completed, a message will appear indicating where the tables have been exported. 

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/Export_Tables.PNG
   :align: center
   :width: 600
   :alt: Reclassify table

Calculation from Task
^^^^^^^^^^^^^^^^^^^^^
As explained in the previous sections, SEPAL runs on GEE. This means that the computation is restricted by the GEE available resources. One of these limitations is the time to get the results on the fly (see `computation time out <https://developers.google.com/earth-engine/guides/debugging#timed-out>`_). So any computation that takes more than five minutes will throw an exception. To overcome this limitation, the process will be executed as a task —which are operations that are capable of running much longer than the standard timeout. If the computation is created as a task, you will see a similar message as the shown in the below image.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/tasks_notice.png
   :align: center
   :width: 600
   :alt: Reclassify table

When computation can’t be done on the fly, a new file containing the id of the task is created and stored in the ../module_results/sdg_indicators/mgci/tasks folder. This file will help you to track the status of the task at any moment. An alternative way to track the progress of the task is by using the GEE task tracker, there you can find the tasks that are running on the server.

**1. To enable a computation from task; first we need to locate the tasks file within SEPAL.**

To do so, you only have to search this file in your SEPAL environment using the navigator by clicking on the search file button, and then clicking over the Calculate MGCI button and the result will be displayed if the process status is completed. To locate the tasks manually, alternatively to locate the tasks navigate to the File Layer > Downloads > Module results>Tasks on SEPAL as shown below.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/locating_tasks.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

**2. Once that’s done in GEE, you will need to bring it back to SEPAL for the tool to finish computation. Click on the "Calculation from Task" tab to initiate this process.**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/calculation_from_task.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

**3. Load your task to finish computation.**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/task_file_choice.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

Visualizing the results
-----------------------

We can visualize the results in the following two ways: 

• The exported tables: These provide the full results of the computation in a tabular format.

• Using the MGCI results drawer provides a simplified and visual representation of the results.

Let’s look at these individually.

Exporting tables
^^^^^^^^^^^^^^^^

As explained earlier, once computation is completed, users can export the reporting tables to their SEPAL environment

**1. To locate the tables, navigate to the Files Tab > Under the Downloads, you should see your table under MGCI reports as shown below:**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/downloading_report.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

**2. To download the report from SEPAL, click on the report and this activates the download icon in the top right side of the screen.**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/export_mgci.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

**3. Once the report is downloaded, you can visualize the results of the computation as seen below for all the reporting years defined earlier on.**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/results_excel_subA.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

The tables follow the standard format for SDG reporting and therefore can be used to report SDG Indicator 15.4.2 values to FAO

Visualizing the results through the MGCI Results Drawer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SEPAL-SDG 15.4.2 :sub:`beta` also allows to explore the results of the computation visually. The module generates dashboards that show the changes that have occurred in the area of interest. To generate these dashboards do the following;

**1.	Click on the **MGCI results drawer** in the left panel. To see the results from the computation for Sub-Indicator A, choose which year you want to visualize and click on the Calculate button. 

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/MGCI_Results_SUbA.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

This generates dashboards to visualize the results of the computation. As seen below, the tool will generate an Overall MGCI for your study area. Additionally, a dashboard will be generated for each of the bioclimatic classes.

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/Visualizing%20SUbA.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

**2. To see the results for Sub-Indicator B, choose a target year (baseline or one of the reporting years) using the drop-down arrow and a bioclimatic belt. Then click on Calculate:**

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/results_sub_indicator_b.PNG
   :align: center
   :width: 700
   :alt: Reclassify table

The results, shown as transitions in land cover types for a given belt will be displayed using a Sankey Plot, as shown below:

.. image:: https://raw.githubusercontent.com/xavidelamo/sepal_images/main/computation/nival_results.PNG
   :align: center
   :width: 700
   :alt: Reclassify table
.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/sepal_mgci/release/doc/en.rst
