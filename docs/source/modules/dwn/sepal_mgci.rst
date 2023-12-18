SEPAL - MGCI :sub:`beta`
========================
*Compute and report against SDG Indicator 15.4.2, as well as track the progress of efforts to monitor ecosystem restoration*

General information
-------------------

About SEPAL–MGCI :sub:`beta`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SEPAL-MGCI :sub:`beta` was developed to help member countries compute and report against SDG Indicator 15.4.2, as well as track the progress of efforts to monitor ecosystem restoration (MGCI refers to Mountain Green Cover Index).

It is available on the SEPAL platform in a beta stage (i.e. still in development).

If you have questions or concerns, use the `SEPAL-MGCI GitHub issue tracker <https://github.com/dfguerrerom/sepal_mgci/issues>`__, follow our documentation's `Contribution guidelines <https://github.com/dfguerrerom/sepal_mgci/blob/master/CONTRIBUTE.md>`__.

Please contact the **SEPAL-MGCI :sub:`beta` team** with any comments or suggestions. 

Authors 
^^^^^^^

SEPAL-MGCI :sub:`beta` was developed by the Food and Agriculture Organization of the United Nations (FAO). 

Specific contributors to SEPAL-MGCI :sub:`beta` and its documentation include:

-    Daniel Guerrero
-    Pierrick Rambaud 
-    Corinna Ravilious 
-    Xavier de Lamo

License
^^^^^^^
SEPAL-MGCI :sub:`beta` is free and open-source. It is licensed under an `MIT license <https://opensource.org/licenses/MIT>`__. 

The documentation is made available under the terms of the `Creative Commons Attribution 4.0 International License (CC BY 4.0) <https://creativecommons.org/licenses/by/4.0>`__. The boundaries, names and designations used do not imply official endorsement or acceptance by the United Nations.

Data sources
^^^^^^^^^^^^

**SEPAL-MGCI** draws on a number of global data sources to allow the computation of SDG Indicator 15.4.2 when national data is not available. 

The datasets described below have been made available by the following organizations under separate terms, as indicated in their respective metadata:

- **Land cover**: European Space Agency (ESA) Climate Change Initiative (CCI) land cover available at the `ESA-CCI viewer <http://maps.elie.ucl.ac.be/CCI/viewer/index.php>`__.

- **Digital elevation model**: The Shuttle Radar Topography Mission (SRTM), available via `Google Earth Engine (GEE) <https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4>`__.

- **Administrative boundaries**: FAO Global Administrative Unit Layers (GAUL) 2015, available via `GEE <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1>`__.

.. note:: The **Administrative boundaries** provided in **SEPAL-MGCI** are in the public domain. Designations employed and presentation of material on this map do not imply the expression of any opinion whatsoever on the part of the Secretariat of the United Nations concerning the legal status of any country, territory, city, or area or of its authorities, or concerning the delimitation of its frontiers or boundaries. If using **SEPAL-MGCI** for official purposes, it is recommended that users use an official boundary provided by the designated office of their country.

Background
^^^^^^^^^^

SDG Indicator 15.4.2 – Mountain Green Cover Index (MGCI) is one of the two indicators under SDG Target 15.4, which aims to "ensure the conservation of mountain ecosystems, including their biodiversity, to enhance their capacity to provide benefits which are essential for sustainable development".

FAO is the custodian agency of this indicator. The MGCI is designed to measure the extent and changes of green vegetation in mountain areas to monitor progress towards SDG Target 15.4.

The MGCI is defined as the ratio of the mountain green cover area to the total mountain area:

.. math::
    
    MGCI = (Mountain Green Cover Area)/(Total Mountain Area)

Where: 

- **Mountain green cover area**: Sum of mountain area (km :sup:`2`) covered by cropland, grassland, forestland, shrubland and wetland, as defined based on the Intergovernmental Panel on Climate Change (IPCC) classification (Penman *et al.*, 2003). This component is calculated from the vegetation descriptor layer.
- **Total mountain area**: Total area (km :sup:`2`) of mountains. In both the numerator and denominator, mountain area is defined according to Kapos *et al.* (2000). This component is calculated from the mountain descriptior layer.
- **Vegetation descriptor layer**: The vegetation descriptor layer categorizes land cover into green and non-green areas. Green vegetation includes both natural vegetation and vegetation resulting from anthropic activity (e.g. crops, afforestation). Non-green areas include very sparsely vegetated areas, bare land, water, permanent ice/snow, and urban areas. The vegetation descriptor layer is derived from a land cover map, where land cover categories are classified into IPCC categories and then in green/non-green areas. 

  .. _ipcc_classes:
  
  .. csv-table:: IPCC classification
     :header: "Code", "Description"
     :widths: auto
     :align: center
  
     "1","Forest"
     "2","Grassland"
     "3","Cropland"
     "4","Wetland"
     "5","Settlement"
     "6","Other land"


- **Mountain descriptor layer**:  The mountain descriptor layer consists of a map of mountain classes following the UN Environment Programme World Conservation Monitoring Centre (UNEP-WCMC) classification (Kapos *et al.*, 2000), which classifies world mountain areas according to altitude, slope and elevation range into the following categories:
  
  .. csv-table:: Mountain classes
     :header: "UNEP-WCMC Mountain Class", "Description"
     :widths: auto
     :align: center
  
     "1","Elevation > 4.500 m"
     "2","Elevation 3.500–4.500 m"
     "3","Elevation 2.500–3.500 m"
     "4","Elevation 1.500–2.500 m and slope > 2"
     "5","Elevation 1.000–1.500 m and slope > 5 or local elevation range (LER 7 km radius) > 300 m"
     "6","Elevation 300–1.000 m and local elevation range (7 km radius) > 300 m"

SEPAL-MGCI :sub:`beta` allows the user to compute each of these descriptive layers to then calculate MGCI values for any given area using both global and user-provided data. The results of this analysis can then be exported to a set of standardized reporting tables where MGCI values are disaggregated by mountain class and IPCC land category, as specified in the `metadata of SDG Indicator 15.4.2 <https://unstats.un.org/sdgs/metadata/files/Metadata-15-04-02.pdf>`_.

References
^^^^^^^^^^

- Kapos, V., Rhind, J., Edwards, M., Prince, M. & Ravillous, C. 2000. Developing a map of the world’s mountain forests. In: *Forests in Sustainable Mountain Development: A State-of-Knowledge Report for 2000*. pp. 4–9. Wallingford, CAB International.
- Penman, J., Gytarsky, M., Hiraishi, T., Krug, T., Kruger, D., Pipatti, R., Buendia, L., Miwa, K., Ngara, T. & Tanabe, K. 2003. *Good Practice Guidance for Land Use, Land-use Change and Forestry*.

Before using SEPAL-MGCI :sub:`beta`
-----------------------------------

To run the **SEPAL-MGCI** module you will need: 

-    a web browser 
-    an internet connection
-    SEPAL and Google Earth Engine (GEE) accounts

    - **SEPAL**: The environment where the SEPAL-MGCI :sub:`beta` is deployed and therefore displayed. To create a SEPAL account, please follow the `registration steps <https://docs.sepal.io/en/latest/setup/register.html#sign-up-to-sepal>`__. Then, familiarize yourself with the tool by exploring its interface.
    - **Google Earth Engine (GEE)**: SEPAL-MGCI :sub:`beta` has been built under the GEE Python API, which means that all computational steps are done through GEE servers. To open a GEE account, follow the `registration steps <https://docs.sepal.io/en/latest/setup/gee.html#create-a-gee-account>`__, remembering to `initialize the home folder <https://docs.sepal.io/en/latest/setup/gee.html#initialize-the-home-folder>`__.
    - **Connect your SEPAL and GEE accounts**: The last step is to connect both accounts by following `these step-by-step instructions <https://docs.sepal.io/en/latest/setup/gee.html#connection-between-gee-and-sepal>`__.

SEPAL interface
---------------

If you are new to SEPAL, it is recommended to take a review the interface and familiarize yourself with the main tools. A detailed description of the features can be consulted in the `interface documentation <https://docs.sepal.io/en/latest/setup/presentation.html#sepal-interface>`__.

To open SEPAL-MGCI :sub:`beta`: 

-    use the `apps tab <https://docs.sepal.io/en/latest/setup/presentation.html#apps-tab>`__ and navigate through the pages, or 
-    enter "Mountain Green Cover Index" into the search box, select the app drawer, and wait until the SEPAL-MGCI :sub:`beta` module has been displayed in your session (it may take a few minutes). The module should look like the following image:

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/0_app_overview.PNG
   :align: center
   :width: 600
   :alt: MGCI module

SEPAL-MGCI :sub:`beta` module
-----------------------------

SEPAL-MGCI :sub:`beta`, as any other SEPAL module, is divided into two main sections:

- **Process drawers**: Find processing steps to accomplish the goal of the module, which consists of four steps:

  - Area of interest (AOI) selection
  - Mountain descriptor
  - Vegetation descriptor
  - MGCI results

- **Help drawers**: Learn more about the tool, objectives, and background on the module's development. This consists of:

  - Source code: The module was developed under an `MIT license <https://opensource.org/licenses/MIT>`__, meaning the development is freely accessible and the code is public (it will link you to the GitHub repository of the module).
  - Wiki: The latest documentation on SEPAL-MGCI :sub:`beta`, where you can start learning the workflow and module features.
  - Bug report: Use this section to report any unexpected results or behaviours by following the `contribution guidelines <https://github.com/dfguerrerom/sepal_mgci/blob/master/CONTRIBUTE.md>`__.

Area of interest (AOI)
----------------------

The calculation of the MGCI will be restricted to a specific AOI. In this step, you will have the option to choose between a predefined list of administrative layers or use a custom dataset. The available options include:
 
- Predefined layers: 
   - Country/province
   - Administrative level 1
   - Administrative level 2
   
- Custom layers
   - Vector file: Use this option to upload a custom vector file. Select the **Vector file** method in the dropdown list; a **File manager** will be displayed, allowing you to search and select a vector file stored in your **SEPAL environment** (see `How to exchange files with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html#exchange-files-with-sepal>`__). The dropdown menu **Column** is useful to filter the features of the vector file. The default option is **Use all features**. To filter the collection, select a **Column** and a **Value** in the corresponding dropdown list, then select the :guilabel:`Select aoi` button.
     
     .. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/1_vector_file.PNG
        :align: center
        :width: 600
        :alt: AOI selection
     
     .. note:: The AOI tool will read the following formats: [".shp", ".geojson", ".gpkg", ".kml"]; it will transform its original coordinates into EPSG:4326.
     
   - GEE asset name: See how to `upload an asset in GEE <https://docs.sepal.io/en/latest/setup/gee.html#upload-files-to-gee>`__.

Since all processing is done in GEE, custom layers have to be previously stored as an `Earth Engine asset <https://developers.google.com/earth-engine/guides/asset_manager>`__ in your GEE account (either private or in a third-party account as a public asset; see `How to upload an asset to GEE <https://docs.sepal.io/en/latest/setup/gee.html#upload-files-to-gee>`__). The dropdown menu will query all assets in your GEE folder that matches the image type. Select it from the dropdown menu or enter it directly.

.. attention:: 

    The administrative boundaries provided in SEPAL-MGCI are in the public domain. The designations employed and the presentation of material on this map do not imply the expression of any opinion whatsoever on the part of the Secretariat of the United Nations concerning the legal status of any country, territory, city, or area or of its authorities, or concerning the delimitation of its frontiers or boundaries. If using SEPAL-MGCI for official purposes, it is recommended that users use an official boundary provided by the designated office of their country.

After selecting the desired area, select the :guilabel:`Select AOI` button; the map will display your selection.

.. note::

    You can only select one AOI. In some cases, depending on the input data, the process could take longer (see the :ref:`calculation <calculation>` section for more info).

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/1_aoi_selection.PNG
   :align: center
   :width: 600
   :alt: AOI selection

Mountain descriptor layer 
-------------------------

This section of SEPAL-MGCI :sub:`beta` produces a UNEP-WCMC mountain class map for the study area selected in the previous step using a **Digital elevation model (DEM)** as an input. You have the option to provide a custom DEM for your study area or use the Shuttle Radar Topography Mission (SRTM) DEM (90 m resolution) developed by NASA/CGIAR.

Questionnaire
^^^^^^^^^^^^^

Here you have to indicate the DEM dataset you wish to use to develop the mountain class map. If you wish to use your own DEM dataset, select **Yes**. By selecting the desired option, the module will hide or display a text box to insert or select an asset ID.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/2_questionaire.PNG
   :align: center
   :width: 300
   :alt: DEM questionnaire

Custom dataset
::::::::::::::

Since all processing is done in GEE, all inputs must be uploaded as an `Earth Engine asset <https://developers.google.com/earth-engine/guides/asset_manager>`__. When using a custom dataset, it must be stored in your GEE account (private or in a third-party account as a public asset). The dropdown menu will query all assets in your GEE folder that match the image type. You can select it from the dropdown menu or enter it directly.

After selecting the :guilabel:`Create UNEP-WCMC Mountain Class Map` button, the module will create the mountain descriptor layer; it will be automatically displayed on the map.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/2_mountain_descriptor.PNG
   :align: center
   :width: 600
   :alt: Mountain layer example

Vegetation descriptor layer
---------------------------

This section of SEPAL-MGCI :sub:`beta` produces the vegetation descriptor layer needed to compute the MGCI for the selected study area. It does so by reclassifying a land cover map into the six :ref:`IPCC land cover classes <ipcc_classes>` (Forest, Cropland, Grassland, Wetland, Settlements and Other Land), and then into green and non-green cover following the reclassification rules specified in the indicator’s metadata.

Questionnaire
^^^^^^^^^^^^^

Here you have to indicate the land cover map that you wish to use to compute the vegetation descriptor layer. If you wish to use your own land cover map, select :guilabel:`yes`. If you select :guilabel:`no`, SEPAL-MGCI :sub:`beta` will use the CCI land cover datasets developed by the European Space Agency (ESA) for the years 1992–2018 (at 300 m resolution) to produce the vegetation descriptor layer for the selected AOI.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_questionnaire.PNG
   :align: center
   :width: 600
   :alt: Vegetation descriptor questionnaire


If you have selected **No**
:::::::::::::::::::::::::::

SEPAL-MGCI :sub:`beta` will use the ESA-CCI land cover dataset. You just have to select the year for which you want to compute the analysis (**select band/property** in the dropdown menu). Once you have selected the year, select :guilabel:`display on map` to create an IPCC land cover class.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_default.PNG
   :align: center
   :width: 600
   :alt: Default classification

If you have selected **Yes**
::::::::::::::::::::::::::::

Similarly to the mountain descriptor layer, to be able to use your own land cover map you would need upload it first to your GEE account or in a third-party account as a public asset (see `How to upload files to GEE <https://docs.sepal.io/en/latest/setup/gee.html#upload-files-to-gee>`__). The dropdown menu will query all assets in your GEE folder that match the image type. You can select it from the dropdown list or directly copy and paste the link to the dataset.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_custom.PNG
   :align: center
   :width: 600
   :alt: Custom classification

To allow SEPAL-MGCI :sub:`beta` to create an IPCC land cover class map using the land cover map you have provided, specify how the land cover classes of your map have to be reclassified into the :ref:`six IPCC classes <ipcc_classes>` in one of two ways:

- Upload a table in .csv format (reclassification matrix), showing the IPCC land cover equivalent of the classes of your land cover map. See its structure in the :ref:`reclassification matrix <reclass_table>` section below. To provide information in this way, select :guilabel:`yes` below the question **Do you have a reclassification matrix table in .csv format?**

  Once the table is in the **SEPAL enviroment**, select :guilabel:`Filename`, navigate through the folders, choose your table, and select the :guilabel:`load` button.
  
  .. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_search_table_and_load.PNG
     :align: center
     :width: 600
     :alt: Search and load table

  .. _reclass_table:
  
  .. tip:: What is a reclassification matrix table?:
      A reclassification matrix is a comma-separated values (.csv) file used to reclassify pixel values from one dataset into another. The .csv file only has to contain two values per line: the first one refers to the **from** value, while the second is the **target** value (see following table).
    
      .. csv-table:: Reclassification table example
         :header: "Origin class", "Target class"
         :widths: auto
         :align: center
   
         "311", "1"
         "111", "5"
         "...","..."
         "511", "4"
   
     To upload a classification table, see `How to exchange files in SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html#exchange-files-with-sepal>`__.
     
     **Note**: The target values must match with the :ref:`IPCC classification table <ipcc_classes>`.

- Directly specify the reclassification rules by selecting :guilabel:`get table`; then, manually indicate the IPCC land cover equivalent (in the destination class column) of each of the land cover classes of your custom dataset (in the original class column) in the interactive table. To provide the reclassification matrix using this method, select **No** below the question, **Do you have a reclassification matrix table in .csv format?**

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_1_reclassify_table.PNG
   :align: center
   :width: 600
   :alt: Reclassification table

.. tip:: After manually reclassifying your dataset, use the :guilabel:`save` button to store the table as a .csv file so that it can be used again later.
 
Display results
^^^^^^^^^^^^^^^

Once you have reclassified the new values or used the default land cover dataset, display the reclassified map by selecting the :guilabel:`display map` button. Depending on your AOI, the map should look like this:

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_3_vegetation_descriptor_2.PNG
   :align: center
   :width: 600
   :alt: Vegetation layer example map

.. tip:: 

    Remember that the MGCI is only calculated over mountain classes, so the vegetation layer will mask out the areas where there is no presence of a mountain class.

MGCI calculation
----------------

Once you have set the inputs in the previous steps, select **Calculate MGCI** to calculate both the area of each IPCC land cover class and MGCI values for the whole mountain area and for each mountain class. The module has the option of executing the calculation using the planimetric area or the `real surface area <https://www.fs.fed.us/rm/pubs_other/rmrs_2004_jenness_j001.pdf>`__. Each section will provide an overall MGCI displayed in a circle, along with the summary of the area in each of the IPCC classes, as shown in the below image.

.. _calculation:

Calculation
^^^^^^^^^^^

Depending on the size of your AOI and whether you are using the real surface area or not, the process could take longer. As explained in the previous sections, the calculation of the land cover/use area per mountain class, as well as the MGCI, is done in GEE, meaning that the computation is restricted by the available GEE resources; one of these limitations is the time to get the results on the fly (see `Computation time out <https://developers.google.com/earth-engine/guides/debugging#timed-out>`__).

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/4_dashboard_1_calculation.PNG
   :align: center
   :width: 600
   :alt: Dashboard calculation

To overcome this limitation, the process will be executed as a task, which is an operation that is capable of running much longer than the standard timeout (see `GEE tasks <https://developers.google.com/earth-engine/guides/playground#tasks-tab>`__). If the computation is created as a task, you will see a similar message as shown in the following image. To receive the results, see the :ref:`calculation from task <calculation_from_task>` section; otherwise, the result will be displayed on the dashboard (see :ref:`dashboard <display>`).

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/4_computation_timeout.PNG
   :align: center
   :width: 600
   :alt: Computation timed out

.. _calculation_from_task:

Calculation from task
^^^^^^^^^^^^^^^^^^^^^

If the computation can't be done on the fly, a new file containing the ID of the task is created and stored in the `../module_results/sdg_indicators/mgci/tasks` folder, which will help you track the status of the task. To do so, search for this file in your SEPAL environment using the **Navigator** by selecting the :guilabel:`search file` button; then, select the :guilabel:`Calculate MGCI` button. The result will be displayed if the process status is complete.

.. tip:: 

    An alternative way to track the progress of the task is by using the `GEE task tracker <https://code.earthengine.google.com/tasks>`_, where you can find tasks running on the server.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/4_dashboard_tasks.PNG
   :align: center
   :width: 600
   :alt: Download from task
   
|

.. _display:

Display dashboard
^^^^^^^^^^^^^^^^^

Whether the computation is done on the fly or you have used the task, the dashboard will be rendered in the same way (i.e. divided into two sections):

- Overall MGCI: Indicates the overall index for the whole mountain area.
- Mountain class MGCI: Indicates the index for that specific mountain class.

.. note:: The module will only work with the six IPCC classes. If you have provided different values to the classes, the module will classify them as the **Other lands** class (IPCC 6).

Export results
^^^^^^^^^^^^^^

After the calculation is done, the **Export** button will become available. To generate the report, enter your institution's name and select :guilabel:`export reporting tables` for the year of the land use/cover map. The report will consist of the following three files:

- ER_MTN_GRNCOV: Mountain green cover area (skqm).
- ER_MTN_GRNCVI: Mountain Green Cover Index.
- ER_MTN_TOTL: Total mountain area (sqkm)

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/4_dashboard_export.PNG
   :align: center
   :width: 600
   :alt: Export report

Once the process is done, the alert message will display the storage location of the report files, which can be downloaded by using any of the options presented in `Exchange files in SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html#exchange-files-with-sepal>`__.

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/sepal_mgci/release/doc/en.rst
