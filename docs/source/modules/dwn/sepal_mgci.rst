SEPAL-MGCI :sub:`beta`
======================

A tool to support the computation of SDG Indicator 15.4.2 – Mountain Green Cover Index

General Information
-------------------

About SEPAL-MGCI :sub:`beta`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SEPAL-MGCI :sub:`beta` was developed by the Food and Agriculture Organization (FAO) of the United Nations to support member countries to compute and report against SDG Indicator 15.4.2 as well as a tool to track the progress of efforts to monitor the ecosystem restoration.

SEPAL-MGCI :sub:`beta` is built on SEPAL (System for Earth Observation Data Access, Processing, and Analysis for Land Monitoring), an open-source cloud-based platform which allow users to query and process satellite data quickly and efficiently, tailor products for local needs and produce sophisticated and relevant geospatial analyses quickly. 

SEPAL-MGCI is in a beta stage and therefore it is still under development. Please contact the SEPAL-MGCI :sub:`beta` team with any comments or suggestions. If you have specific bugs to report or improvements to the tool that you would like to suggest, please use the `GitHub’s issue tracker <https://github.com/dfguerrerom/sepal_mgci/issues>`__ of the SEPAL-MGCI :sub:`beta` module and do follow the `contribution guidelines <https://github.com/dfguerrerom/sepal_mgci/blob/master/CONTRIBUTE.md>`__.

Authors 
^^^^^^^

SEPAL-MGCI :sub:`beta` has been developed by the Food and Agriculture Organization (FAO) of the United Nations. 

Contributors to SEPAL-MGCI :sub:`beta` and its documentation include Daniel Guerrero, Pierrick Rambaud, Corinna Ravilious and Xavier de Lamo.

License
^^^^^^^
SEPAL-MGCI :sub:`beta` is free and open source. It is licensed under `MIT license <https://opensource.org/licenses/MIT>`__. The documentation is made available under the terms of the `Creative Commons Attribution 4.0 International License (CC BY 4.0) <https://creativecommons.org/licenses/by/4.0>`__. The boundaries, names and designations used do not imply official endorsement or acceptance by the United Nations.

Data sources
^^^^^^^^^^^^

SEPAL-MGCI draws on a number of global data sources to allow the computation of the SDG 15.4.2 indicator when national data is not available. The datasets described below have been made available by the following organizations under separate terms as indicated in their respective metadata.

- **Land cover**: European Space Agency (ESA) Climate Change Initiative (CCI) Land cover available at the `ESA-CCI viewer <http://maps.elie.ucl.ac.be/CCI/viewer/index.php>`__.

- **Digital Elevation Model**: The Shuttle Radar Topography Mission (SRTM), available at `Google Earth Engine <https://developers.google.com/earth-engine/datasets/catalog/CGIAR_SRTM90_V4>`__.

- **Administrative Boundaries**: FAO GAUL: Global Administrative Unit Layers 2015, available at `Google Earth Engine <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1>`__.

.. note:: The  Administrative Boundaries provided in SEPAL-MGCI are in the public domain. The designations employed and the presentation of material on this map do not imply the expression of any opinion whatsoever on the part of the Secretariat of the United Nations concerning the legal status of any country, territory, city or area or of its authorities, or concerning the delimitation of its frontiers or boundaries. If using SEPAL-MGCI for official purposes, it is recommended that users use an official boundary provided by the designated office of their country.

Background
^^^^^^^^^^

SDG Indicator 15.4.2 – Mountain Green Cover Index (MGCI) is one of the two indicators under SDG Target 15.4, which aims to:

    "*ensure the conservation of mountain ecosystems, including their biodiversity, to enhance their capacity to provide benefits which are essential for sustainable development*". 

The Food and Agriculture Organization (FAO) of the United Nations is the custodian agency of this indicator. The Mountain Green Cover Index (MGCI) is designed to measure the extent and the changes of green vegetation in mountain areas to monitor progress towards SDG Target 15.4.

The MGCI is defined as the ratio of the mountain green cover area to the total mountain area:

.. math::
    
    MGCI = (Mountain Green Cover Area)/(Total Mountain Area)

Where: 

- **Mountain Green Cover Area**: sum of mountain area (km :sup:`2`) covered by cropland, grassland, forestland, shrubland and wetland, as defined based on the IPCC classification (Penman et al. 2003). This component is calculated from the vegetation descriptor layer. 
- **Total Mountain Area**: total area (Km :sup:`2`) of mountains. In both the numerator and denominator, mountain area is defined according to Kapos et al. 2000. This component is calculated from the mountain description layer.
- **Vegetation descriptor layer**: The vegetation descriptor layer categorizes land cover into green and non-green areas. Green vegetation includes both natural vegetation and vegetation resulting from anthropic activity (e.g. crops, afforestation, etc.). Non-green areas include very sparsely vegetated areas, bare land, water, permanent ice/snow and urban areas. The vegetation description layer is derived from a land cover map, where land cover categories are classified into IPCC categories and then in green/non-green areas. 

  .. _ipcc_classes:
  
  .. csv-table:: IPCC Classification
     :header: "Code", "Description"
     :widths: auto
     :align: center
  
     "1","Forest"
     "2","Grassland"
     "3","Cropland"
     "4","Wetland"
     "5","Settlement"
     "6","Other land"


- **Mountain descriptor layer**:  The mountain descriptor layer consists in a map of mountain classes following the UNEP-WCMC classification (Kapos et al. 2000). The UNEP-WCMC classification classifies the world mountain areas according altitude, slope and elevation range into the following categories.

  
  .. csv-table:: Mountain classes
     :header: "UNEP-WCMC Mountain Class", "Description"
     :widths: auto
     :align: center
  
     "1","Elevation > 4.500 meters"
     "2","Elevation 3.500–4.500 meters"
     "3","Elevation 2.500–3.500 meters"
     "4","Elevation 1.500–2.500 meters and slope > 2"
     "5","Elevation 1.000–1.500 meters and slope > 5 or local elevation range (LER 7 kilometer radius) > 300 meters"
     "6","Elevation 300–1.000 meters and local elevation range (7 kilometer radius) > 300 meters"

SEPAL-MGCI :sub:`beta` allows the user to compute each of these description layers to then calculate MGCI values for any given area using both global and user-provided data. The results of this analysis can then be exported to a set of standardized reporting tables where MGCI values are disaggregated by mountain class and IPCC land category, as specified in the  `metadata of SDG Indicator 15.4.2 <https://unstats.un.org/sdgs/metadata/files/Metadata-15-04-02.pdf>`_.

References
^^^^^^^^^^

- Kapos, V., Rhind, J., Edwards, M., Prince, M., & Ravillous, C. (2000). Developing a map of the world’s mountain forests. In M. F. Price , & N. Butt (Eds.), Forests in Sustainable Mountain Development: A State-of-Knowledge Report for 2000 (pp. 4-9). Wallingford: CAB International.  
- Penman, J., Gytarsky, M., Hiraishi, T., Krug, T., Kruger, D., Pipatti, R., Buendia, L., Miwa, K., Ngara, T., Tanabe, K. (2003). Good Practice Guidance for Land Use, Land-use Change and Forestry. Good Practice Guidance for Land Use, Land-use Change and Forestry. 

Before using SEPAL-MGCI :sub:`beta`
-----------------------------------

To run the MGCI SEPAL module you will need a web browser, an Internet connection, and a SEPAL and Google Earth Engine (GEE) account:

- **SEPAL**: is the environment where the SEPAL-MGCI :sub:`beta` is deployed and therefore displayed. To create a SEPAL account, please follow the `registration steps <https://docs.sepal.io/en/latest/setup/register.html#sign-up-to-sepal>`__ and then familiarize yourself with the tool by exploring its interface.
- **Google Earth Engine (GEE)**: SEPAL-MGCI :sub:`beta` has been built under the GEE Python API, which means that all the computational steps are done through the GEE servers. To open a GEE account, please follow the `registration steps <https://docs.sepal.io/en/latest/setup/gee.html#create-a-gee-account>`__ and don't forget to `initialize the home folder <https://docs.sepal.io/en/latest/setup/gee.html#initialize-the-home-folder>`__.
- **Connect your SEPAL and GEE accounts**: the last step is to connect both accounts, you can achieve this by following the `step-by-step <https://docs.sepal.io/en/latest/setup/gee.html#connection-between-gee-and-sepal>`__.

SEPAL interface
---------------

If you are new to SEPAL, it is recommended to take a look over the interface and familiarize yourself with the main tools. A detailed description of the features can be consulted in the `interface documentation <https://docs.sepal.io/en/latest/setup/presentation.html#sepal-interface>`__. 

To open SEPAL-MGCI :sub:`beta` use the `apps tab <https://docs.sepal.io/en/latest/setup/presentation.html#apps-tab>`__ and navigate through the pages, or type into the search box "Mountain Green Cover Index", click over the app drawer and wait patiently until the SEPAL-MGCI :sub:`beta` module is displayed in your session (it may take a few minutes). The module should look like the following image:

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/0_app_overview.PNG
   :align: center
   :width: 600
   :alt: MGCI module


SEPAL-MGCI :sub:`beta` module
-----------------------------

SEPAL-MGCI :sub:`beta`, as any other SEPAL module, is divided into two main sections:

- **Process drawers**: where you can find the processing steps to accomplish the goal of the module. In SEPAL-MGCI :sub:`beta`, this is composed by 4 steps:

  - Area of interest selection
  - Mountain descriptor
  - Vegetation descriptor
  - MGCI results
  

- **Help drawers**: used to describe the tool, objectives and give a background about how it was developed. This is composed by:

  - Source code: the module was developed under a `MIT license <https://opensource.org/licenses/MIT>`__, which means that the development is freely accessible and the code is public. It will link you to the GitHub repository of the module.
  - Wiki: It will point to the latest documentation on SEPAL-MGCI :sub:`beta`. This is where you can start learning the workflow and features of the module.
  - Bug report: No tool is perfect and we are not exempt from bugs. Fortunately, our team is always aware and on constant alert to fix any problem. Use this section to report any unexpected result or behavior. To do so, please follow the `contribution guidelines <https://github.com/dfguerrerom/sepal_mgci/blob/master/CONTRIBUTE.md>`__.


Area of interest (AOI)
----------------------

The calculation of the MGCI will be restricted to a specific area of interest. In this step, you will have the option to choose between a predefined list of administrative layers or to use a custom dataset. The available options are described below:
 
- Predefined layers: 
   - Country/province
   - Administrative level 1
   - Administrative level 2
   
- Custom layers
   - Vector file: use this option to upload a custom vector file. Select the "Vector file" method in the dropdown list, a file manager will be displayed below and will allow you to search and select a vector file stored in your SEPAL environment (see `how to exchange files with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html#exchange-files-with-sepal>`__). The below dropdown called "Column" is useful to filter the features of the vector file, the default option is "Use all features", to filter the collection, select a column and a "Value" in the corresponding dropdown, then click over the :guilabel:`Select aoi` button. 
     
     .. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/1_vector_file.PNG
        :align: center
        :width: 600
        :alt: AOI selection
     
     .. note:: the AOI tool will read the following formats: [".shp", ".geojson", ".gpkg", ".kml"] and it will transform its original coordinates into EPSG:4326
     
   - GEE Asset name: see how to `upload an asset in GEE <https://docs.sepal.io/en/latest/setup/gee.html#upload-files-to-gee>`__
   

   
As all the processing is done in GEE, all custom layers have to be previously stored as an `earth engine asset <https://developers.google.com/earth-engine/guides/asset_manager>`__ in your GEE account (it could be private) or in a third-party account as a public asset (see `how to upload an asset in GEE <https://docs.sepal.io/en/latest/setup/gee.html#upload-files-to-gee>`__). The dropdown menu will query all the assets in your GEE folder that matches the Image type. You can select it from the dropdown or write/paste it directly.

.. warning:: The  Administrative Boundaries provided in SEPAL-MGCI are in the public domain. The designations employed and the presentation of material on this map do not imply the expression of any opinion whatsoever on the part of the Secretariat of the United Nations concerning the legal status of any country, territory, city or area or of its authorities, or concerning the delimitation of its frontiers or boundaries. If using SEPAL-MGCI for official purposes, it is recommended that users use an official boundary provided by the designated office of their country.

After selecting the desired area, click over the :guilabel:`Select AOI` button and the map will show up your selection.

.. note:: 

    You can only select one area of interest. In some cases, depending on the input data, the process could take longer (see :ref:`calculation <calculation>` section for more info).

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/1_aoi_selection.PNG
   :align: center
   :width: 600
   :alt: AOI selection


Mountain descriptor layer 
-------------------------

This section of SEPAL-MGCI :sub:`beta` produces a UNEP-WCMC mountain class map for the study area selected in the previous step using a Digital Elevation Model (DEM) as an input. You have the option to provide a custom DEM for your study area or use the Shuttle Radar Topography Mission (SRTM) DEM, at 90 meter resolution developed by NASA/CGIAR. 

Questionnaire
^^^^^^^^^^^^^

Here you have to indicate the DEM dataset you wish to use to develop the mountain class map. If you wish to use your own DEM dataset, select “Yes”. By clicking over the desired option, the module will hide or display a text box to insert or select an asset id.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/2_questionaire.PNG
   :align: center
   :width: 300
   :alt: DEM questionnaire

Custom dataset
::::::::::::::

As all the processing is done in GEE, all the inputs have to be uploaded as an `earth engine asset <https://developers.google.com/earth-engine/guides/asset_manager>`__. When you are using a custom dataset, it has to be stored in your GEE account (it could be private) or in a third-party account as a public asset. The dropdown menu will query all the assets in your GEE folder that matches the Image type. You can select it from the dropdown or write/paste it directly.

After clicking the :guilabel:`Create UNEP-WCMC Mountain Class Map` button, the module will create the mountain descriptor layer, and it will be automatically displayed on the map.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/2_mountain_descriptor.PNG
   :align: center
   :width: 600
   :alt: Mountain layer example


Vegetation descriptor layer
---------------------------

This section of SEPAL-MGCI :sub:`beta` produces the vegetation descriptor layer needed to compute the MGCI for the selected study area. It does so by reclassifying a land cover map into the six :ref:`IPCC land cover classes <ipcc_classes>`  (Forest, Cropland, Grassland, Wetland, Settlements and Other Land) and then into green and non-green cover following the reclassification rules specified in the indicator’s metadata. 

Questionnaire
^^^^^^^^^^^^^

Here you have to indicate the land cover map that you wish to use to compute the vegetation descriptor layer. If you wish to use your own land cover map, select :guilabel:`yes`. If you select :guilabel:`no`, SEPAL-MGCI :sub:`beta` will use the CCI Land Cover datasets developed by the European Space Agency for the years 1992-2018 at 300 meters resolution to produce the vegetation descriptor layer for the selected area of interest.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_questionnaire.PNG
   :align: center
   :width: 600
   :alt: Vegetation descriptor questionnaire


If you have selected 'No'
:::::::::::::::::::::::::

SEPAL-MGCI :sub:`beta` will use the ESA-CCI Land Cover dataset and you just have to select in the dropdown menu the year for which you want to compute the analysis (“select band/property”). Once you have selected the year, click on :guilabel:`display on map` to create an IPCC land cover class.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_default.PNG
   :align: center
   :width: 600
   :alt: Default classification


If you have selected 'Yes'
::::::::::::::::::::::::::

Similarly to the mountain description layer, to be able to use your own land cover map you would need upload it first in your GEE account or in a third-party account as a public asset (see `how to upload files to gee <https://docs.sepal.io/en/latest/setup/gee.html#upload-files-to-gee>`__). The dropdown menu will query all the assets in your GEE folder that matches the Image type. You can select it from the dropdown or directly copy and paste the link to the dataset.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_custom.PNG
   :align: center
   :width: 600
   :alt: Custom classification


To allow SEPAL-MGCI :sub:`beta` to create an IPCC land cover class map using the land cover map you have provided, you will need to specify how the land cover classes of your map have to be reclassified into the :ref:`six IPCC classes <ipcc_classes>`.  You can do this in two different ways:

- Upload a table in a csv format (reclassification matrix) showing how the IPCC land cover equivalent of the classes of your land cover map. See its structure in the :ref:`reclassification matrix <reclass_table>` section below. To provide the information in this way, click on :guilabel:`yes` below the question 'Do you have a reclassification matrix table in a csv format'?.

  After having the table in the SEPAL enviroment, click over the :guilabel:`Filename`, navigate trhough the folders, select your table and click over the :guilabel:`load` button.
  


  .. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_search_table_and_load.PNG
     :align: center
     :width: 600
     :alt: Search and load table



  .. _reclass_table:
  
  .. tip:: What is a reclassification matrix table?:
      A reclassification matrix is a comma-separated values (CSV) file used to reclassify pixel values from one dataset into another. The CSV file only has to contain two values per line, the first one refers to the `from` value, while the second is the `target` value, just as it is described in the following table:
    
      .. csv-table:: Reclassification table example
         :header: "Origin class", "Target class"
         :widths: auto
         :align: center
   
         "311", "1"
         "111", "5"
         "...","..."
         "511", "4"
   
     To upload a classification table, please see the `how to exchange files in SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html#exchange-files-with-sepal>`__.
     
     **Note**: The target values must match with the :ref:`IPCC classification table <ipcc_classes>` 


- Directly specify the reclassification rules by clicking on :guilabel:`get table` and manually indicate the IPCC land cover equivalent (in the destination class column) of each of the land cover classes of your custom dataset (in the original class column) in the interactive table.  To provide the reclassification matrix using this method click on “No” below the question “Do you have a reclassification matrix table in a csv format’’?

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_1_reclassify_table.PNG
   :align: center
   :width: 600
   :alt: Reclassify table


.. tip:: After manually reclassifying your dataset, you can use the :guilabel:`save` button to store the table as a CSV file and you can use it later instead of manually filling up the table.
 
Display results
^^^^^^^^^^^^^^^

Once you have reclassified the new values or used the default land cover dataset, you can display the reclassified map by clicking over the :guilabel:`display map` button. Depending on your area of interest, the map should look like this:

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/3_3_vegetation_descriptor_2.PNG
   :align: center
   :width: 600
   :alt: Vegetation layer example map


.. tip:: Remember that the MGCI is only calculated over the mountain classes, so the vegetation layer will mask out the areas where there is no presence of a mountain class.

MGCI calculation
----------------

Once you have set the inputs in the previous steps, click on “Calculate MGCI” to calculate both the area of each IPCC land cover class and MGCI values for the whole mountain area and for each mountain class. The module has the option to do the calculation using the planimetric area or the `real surface area <https://www.fs.fed.us/rm/pubs_other/rmrs_2004_jenness_j001.pdf>`__. 
Each section will provide an overall MGCI displayed in a circle along with the summary of the area in each of the IPCC classes, as is shown in the below image.

.. _calculation:

Calculation
^^^^^^^^^^^

Depending on the size of your area of interest and whether you are using the real surface area or not, the process could take longer. As we explained in the previous sections, the calculation of the land cover/use area per mountain class, as well as the MGCI, is done in GEE, which means that the computation is restricted by the GEE available resources, one of these limitations is the time to get the results on the fly (see `computation time out <https://developers.google.com/earth-engine/guides/debugging#timed-out>`__), so any computation that takes more than five minutes will throw an exception.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/4_dashboard_1_calculation.PNG
   :align: center
   :width: 600
   :alt: Dashboard calculation


To overcome this limitation, the process will be executed as a task —which are operations that are capable of running much longer than the standard timeout (see `gee tasks <https://developers.google.com/earth-engine/guides/playground#tasks-tab>`__)—. If the computation is created as a task, you will see a similar message as the shown in the below image, and to get the results, please see the :ref:`calculation from task <calculation_from_task>` section, otherwise, the result will be displayed on the dashboard (see :ref:`dashboard <display>`).

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/4_computation_timeout.PNG
   :align: center
   :width: 600
   :alt: Computation timed out


.. _calculation_from_task:

Calculation from task
^^^^^^^^^^^^^^^^^^^^^

If the computation can't be done on the fly, a new file containing the id of the task is created and stored in the `../module_results/sdg_indicators/mgci/tasks` folder. This file will help you to track the status of the task at any moment. To do so, you only have to search this file in your SEPAL environment using the navigator by clicking on the :guilabel:`search file` button, and then clicking over the :guilabel:`Calculate MGCI` button and the result will be displayed if the process status is completed.

.. tip:: an alternative way to track the progress of the task is by using the `GEE task tracker <https://code.earthengine.google.com/tasks>`_, there you can find the tasks that are running on the server.

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/4_dashboard_tasks.PNG
   :align: center
   :width: 600
   :alt: Download from task
   
|

.. _display:

Display dashboard
^^^^^^^^^^^^^^^^^

No matter if you the computation is done on the fly or if you have used the task, the dashboard will be rendered in the same way, and this is divided into two sections:

- Overall MGCI: it indicates the overall index for the whole mountain area.
- Mountain class MGCI: it indicates the index for that specific mountain class.

.. note:: The module will only work with the 6 IPCC classes. If you have provided different values to the classes, the module will classify them as "other lands" class (IPCC 6). 


Export results
^^^^^^^^^^^^^^

After the calculation is done, the export button will become available. To generate the report, you have to enter the name of the institution you belong to and click on :guilabel:`export reporting tables` for the year of the land use/cover map. The report will consists in the following three files:

- ER_MTN_GRNCOV: Mountain green cover area (skqm).
- ER_MTN_GRNCVI: Mountain Green Cover Index.
- ER_MTN_TOTL: Total mountain area (sqkm)

.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/4_dashboard_export.PNG
   :align: center
   :width: 600
   :alt: Export report

Once the process is done, the alert message will show you where the report files are stored, to download them, you can use any of the options available at `exchange files in SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html#exchange-files-with-sepal>`__.

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/sepal_mgci/release/doc/en.rst
