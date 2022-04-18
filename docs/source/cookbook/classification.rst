Classification
==============

Overview
--------

With this recipe, SEPAL will help the user build a supervised classification of any mosaic image. It is build on top of the most advanced tools available on Google Earth Engine (These classifiers include CART, RandomForest, NaiveBayes and SVM) and create a easy-to-use User interface to:

-   select the image to classiffy
-   define the class table
-   add training data from external sources and on-the-fly selection

In combination with the other tools of SEPAL the classifcation recipe can help you provide accurate land-use maps, without coding a single line of code.

Start
-----

Once the classification recipe is selected, SEPAL will show up the recipe process in a new tab (1) and the image selection window will open itself on the bottom right side (2). 

.. thumbnail:: ../_images/cookbook/classification/landing.png
    :group: classification-recipe
    :title: the landing page of the classification recipe

The first step is to change the name of the recipe. This name will be used to name your files and recipes in the SEPAL folders. Use the best-suited convention for your need. Simply double-click the tab and write a new name. It will default to :code:`Classification_<timestamp>`.

.. thumbnail:: ../_images/cookbook/classification/default_title.png
    :title: classification default title 
    :width: 49%

.. thumbnail:: ../_images/cookbook/classification/modified_title.png
    :title: classification modified title 
    :width: 49%
    
.. note::

    The SEPAL team recommends using the following naming convention: :code:`<image_name>_<classification>_<measures>`.

Parameters
----------

On the bottom right corner, 5 tabs are available. They will allow you to customize the time series to your needs.

-   :guilabel:`IMG`: the image to classify
-   :guilabel:`LEG`: the legend of the classification system
-   :guilabel:`TRN`: the training data of the model
-   :guilabel:`AUX`: the auxiliary global dataset to use in the model
-   :guilabel:`CLS`: the classifier configuration

.. thumbnail:: ../_images/cookbook/classification/parameters.png
    :group: classification-recipe
    :title: the parameters of the classification recipe

Image selection
^^^^^^^^^^^^^^^

The first step consist in selecting the image(s) bands on which to apply the classifier. The number of selected bands (i.e. images) is not limited. 

.. note:: 

    Keep in mind that increasing the number of bands to analyse will improve the model but slow down the rendering of the final image.

.. danger:: 

    If multiple images are selected, they should be overlapping the first one. if masked pixels are found in one of the bands, the classifier will mask them well.

click on :btn:`<fas fa-plus> Add`. The following screen should be displayed : 

.. thumbnail:: ../_images/cookbook/classification/image_source.png
    :group: classification-recipe
    :title: the 2 availabel images sources for classification

Image type
""""""""""

The users can select image coming from an **existing recipe** (all computed band will be available or an exported **GEE asset**. Both should be :code:`ee.Image` (no :code:`Time series`, no :code:`ee.ImageCollection`).

-   **existing recipe**: 
    
    -   advantages:

        -   All the computed bands from SEPAL can be used
        -   Any modification to the existing recipe will be propagated to the final classification 

    -   Defaults:

        -   The initial recipe will be computed at each rendering step slowing down the classificaiton process
        -   Can break the on-the-fly rendering due to GEE timeout errors

-   **GEE asset**:  

    -   advantages:
        
        -   Can be shared with other users 
        -   The computation will be faster as the Image is already exported
    
    -   Defaults:

        -   Only the exported bands will be available
        -   The :code:`Image` need to be reexported to propagate changes

Both methods behave the same way in the interface.

Select bands 
""""""""""""

.. tip::

    For this example we will use a public asset created with the optical mosaic tool from SEPAL. It's a Sentinel 2 mosaic of the Eastern Province of Zambia in the dry season from 2012 to 2020. Multiple bands are available. 

    Use the following asset name if you want to reproduce our workflow: :code:`projects/sepal-cookbook/assets/classification/zmb-eastern_2012_2021`

Image bands
###########

Once a asset has been selected, SEPAL will loads its bands in the interface. You can use any band that is natively existing in the image as input for the classification process. simply click on the band name to select them. The selected bands are summurazied in the expansion panel title (1) and displayed in gold in the panel content (2).

In this example image we selected :code:`red`, :code:`nir`, :code:`swir`, and :code:`green`.

.. thumbnail:: ../_images/cookbook/classification/native_bands.png
    :group: classification-recipe
    :title: select :code:`red`, :code:`nir`, :code:`swir`, and :code:`green` from the source image

Derived bands
#############

The analysis is not limited to the natively available bands. SEPAl can also built extra derived bands on the fly. Click :btn:`<fas fa-plus> derived bands` at the bottom of the popup window and select and deriving method. A new panel is added to the expansion panel with the selected method name (1). the selected method will be applied on the selected bands.

.. note:: 

    If more than 2 bands are selected, the operation will be applied on the cartesian product of the bands. If I select bands :math:`A`, :math:`B` and :math:`C` and apply the :code:`difference` derived bands, I'll add 3 bands to my analysis: 

    -   :math:`A - B`
    -   :math:`A - C`
    -   :math:`B - C`


.. thumbnail:: ../_images/cookbook/classification/derived_bands.png
    :group: classification-recipe
    :title: select :code:`red` and :code:`nir` in normalized difference derived band adding one extra band to the analysis: the NDVI

.. note::

    You should have notify that in the figure, we compute the normalized difference between :code:`nir` and :code:`red` which is indeed the NDVI. It is also precomputed in the :code:`indexes` derived bands.

Once the image selection is done, you can click on :btn:`<fas fa-check> Apply` and the popup window will close itself. The images and bands will be displayed in the :guilabel:`IMG` panel on the bottom right corner of the screen. click on the :btn:`<fas fa-trash>` will remove the image and it's band from the analysis all together.

.. thumbnail:: ../_images/cookbook/classification/selected_bands.png
    :group: classification-recipe
    :title: all the selected bands from the selected images

From there, click on :btn:`<fas fa-chevron-right> Next` to jump to the next step.

Legend setup
^^^^^^^^^^^^

In this step the user will specify the legend that should be used in the output classified image. Any categorical classification associating integer value to a class name will work. SEPAL provides multiple ways to create and customize a legend.

.. thumbnail:: ../_images/cookbook/classification/landing_legend.png
    :group: classification-recipe
    :title: The landing menu of the legend parameter

.. important::

    Legends created here are fully compatible with other fonctionnalities of SEPAL including applications

Manual legend
"""""""""""""

The first and most natural way of building a legend is to do it from scratch. Click on :btn:`<fas fa-plus> Add` to add an new class to your legend.
A class is defined by 3 key elements: 

- a color (1): click on the little colored square to open the color picker and select any color. each color must be unique
- a value (2): select any integer value. This value must be unique
- a class (3): the class description. It cannot be empty.

Click again on :btn:`<fas fa-plus> Add` to add an extra class line. the :btn:`<fas fa-trash>` can be used to removed a specific line. 

.. tip::

    Click on :btn:`HEX` (4) to display the hexadecimal value of the used color. It can also be used to insert a known color palette using its values.

If multiple class are created and you are not sure what to use to color them you can select a preselected color-map (5). They are provided by the `gee community <https://github.com/gee-community/ee-palettes>`__ and will be applied on every existing class in your panel. 

.. thumbnail:: ../_images/cookbook/classification/create_legend.png
    :group: classification-recipe
    :title: Manual creation of a legend


Import legend
"""""""""""""

If you already have a file discribing your legend you can use it instead of declaring every legend item one by one. Your legend need to be saved in csv format and containing the following information: 

- the color: stored as hexadecimal value (e.g. "#FFFF00") or in 3 columns (red, bleu, green)
- the value: stored as integer
- the class: stored as string

.. note::

    The column names will help SEPAl to guess the informations but are not compulsory.

For example a csv containing the following information is fully qualified to be used in SEPAL: 

.. code-block::

    code,class,color
    10,Tree cover,#006400
    20,Shrubland,#ffbb22
    30,Grassland,#ffff4c
    40,Cropland,#f096ff
    50,Built-up,#fa0000
    60,Bare,#b4b4b4
    70,Snow,#f0f0f0
    80,Water,#0064c8
    90,Herbaceous wetland,#0096a0
    95,Mangroves,#00cf75
    100,Moss,#fae6a0

This one is the same using rgb defined colors: 

.. code-block::

    code,class,red,blue,green
    10,Tree cover,0,100,0
    20,Shrubland,255,187,34
    30,Grassland,255,255,76
    40,Cropland,240,150,255
    50,Built-up,250,0,0
    60,Bare,180,180,180
    70,Snow,240,240,240
    80,Water,0,100,200
    90,Herbaceous wetland,0,150,160
    95,Mangroves,0,207,117
    100,Moss,250,230,160

Once the fully qualified legend file is prepared on your computer, click on :btn:`<fas fa-chevron-up>` and then on :code:`Import from CSV`. It will open a popup window where you can drag'n'drop the file or select it manually from your computer files. As shown on the next image you can then select the columns that are defining your csv. Click on :btn:`single column` for heaxadecimal defined colors and :btn:`multiple columns` for RGB defined colors.

.. thumbnail:: ../_images/cookbook/classification/import_csv.png
    :group: classification-recipe
    :title: Import legend from csv

Click on :btn:`<fas fa-check> Apply` to validate your selection. The classes will be added to the legend panel and you'll be able to modify the legend using the parameters presented in the previous section.

.. thumbnail:: ../_images/cookbook/classification/imported_csv.png
    :group: classification-recipe
    :title: Imported legend from csv

Click on :btn:`<fas fa-check> Done` to validate this step. every panel should be closed and the colors of the megend are now displayed at the bottom of the map. No classification is performed as we didn't provided any training data. Nevertheless, this step is the last parameter mandatory step. Training data can be added using the on-the-fly training fonctionality. 

Export legend
"""""""""""""

Once your legend is validated, Click again on the :btn:`<fas fa-chevron-up>` and then on :code:`Export as CSV`. A file will be downloaded to you computer named: :code:`<recipe_name>_legend.csv` containing the legend information in the following format: 

.. code-block::

    color,value,label
    #006400,10,Tree cover
    ...


Select Training data
^^^^^^^^^^^^^^^^^^^^

.. warning:: 

    This step is not mandatory 

2 inputs are required to create the classification output: 

- pixel values (i.e bands) to classiy 
- training data to set up the classification model

This menu will help the user manage the used training data of the model. To open it simply click on :btn:`TRN` on the bottom right side of the window.

.. thumbnail:: ../_images/cookbook/classification/training_landing.png
    :group: classification-recipe
    :title: training menu opening window

Collected reference data
""""""""""""""""""""""""

The collected reference data are data selected on the fly by the user. The workflow will be explained further down this documentation. In this panel these data can be managed by the user.

The data is a pair associating coordinates to a class value, they will be used to create training data in the classification model. If you're satisfied with the current selection and you want to share these data with others, click on the :btn:`<fas fa-chevron-up>` and then on :code:`export reference data to csv`. A file will be created named: :code:`<recipe_name>_reference_data.csv` and send to your computer. It will embed all the gathered point data using the following convention:

.. code-block::

    XCoordinate,YCoordinate,class
    32.77189961605467,-11.616264558754402,80 
    ...

On the other hand if you are not satisfied with the selected data, click on :btn:`<fas fa-chevron-up>` and then on :code:`clear collected reference data` to remove every collected data from the analysis. 

.. tip:: 

    A confirmation popup should prevent you from accidentally delete everything.  

Existing training data
""""""""""""""""""""""

Instead of collecting all the data by hand, SEPAL provides numerous way to include already existing training data into your analysis. This data can bu from multiple format and will be included in the model to improve the quality of the final map. 

.. danger::

    The imported files can use an extended version of the Legend provide in the previous step but To avoid unexpected behaviour, at least one of the class of your legend and the provided training data needs to match

.. danger:: 

    If the added training data are out of the image to classify they will have no impact on the final result with the exception of the "SEPAL recipe".

To add new data, click on :btn:`<fas fa-plus> Add` and choose the type of data to import: 

.. thumbnail:: ../_images/cookbook/classification/import-training-data.png
    :group: classification-recipe
    :title: the different types of training data available in SEPAL

CSV
###

By selecting :btn:`csv file`, SEPAL will request a file from your computer in :code:`.csv` format. The file needs to provide 2 information: geographic coordinates and class value. 

It can be done using coordinates in :code:`EPSG:4326` lattitude and logitude coordinates as well as a `GeoJSON <https://geojson.org>`__ compatible point object. The file can embed multiple other columns that will not be considered during the naalysis. 

The following table is compatible with SEPAL: 

.. code-block::

    XCoordinate,YCoordinate,class,class_name,editor_name
    32.77189961605467,-11.616264558754402,80,Srublands,Pierrick rambaud
    ...

The columns used to define the X (longitude) and Y (lattitude) coordiantes are manually set up in the popup window. Click on :btn:`<fas fa-chevron-left> Next` once every column is filled.

.. thumbnail:: ../_images/cookbook/classification/import-training-csv-coords.png
    :group: classification-recipe
    :title: import a csv file in SEPAL as training data

.. tip::

    If your file contains a GeoJSON columns instead of coordinates, click on :btn:`geojson column` to switch the interface to 1 column selection.


Now that you set up the coordinates of your points SEPAL will request the columns specifying the class value (not the name) In a second frame. Only the single column is supported so far. So select the column from your file that embed the class values. 

.. tip::

    Using the :code:`row filter expression` text field, one can filter out some lines of the table. Refer to the `features <#>`__ section to know more.

.. thumbnail:: ../_images/cookbook/classification/import-training-csv-class.png
    :group: classification-recipe
    :title: import a csv file in SEPAL as training data

Click on :btn:`<fas fa-chevron-left> next` to add the data to model. SEPAL will provide a summary of the classes in the legend of the classification and the number of trainng poin added by your file.

the :btn:`<fas fa-check> Done` button will finish the uploading procedure.

.. thumbnail:: ../_images/cookbook/classification/import-training-csv-summary.png
    :group: classification-recipe
    :title: import a csv file in SEPAL as training data

GEE table 
#########

By selecting :btn:`Earth Engine Table`, SEPAL will request a file from your computer in :code:`.csv` format. The file needs to provide 2 information: geographic coordinates and class value.

Every steps are the same as the csv table, the only difference should be the geometry column as GEE asset usually embed by default a :code:`.goejson` column. If this column exist it will be autodetected by SEPAL.

For the other steps, please reproduce what was presented in the CSV section.

.. thumbnail:: ../_images/cookbook/classification/import-training-gee-coords.png
    :group: classification-recipe
    :title: import an GEE table in SEPAL as training data

.. note::

    To build the documentation example, you can use this public asset: :code:`projects/sepal-cookbook/assets/classification/zmb_eastern_esa_2012_2021_reference_data`.


Sample classification
#####################

Instead of providing points dataset, SEPAL can also extract reference data from an already existing classification. It's a good way to improve an already exisiting classification system using an image with better resolution. 

To sample data, SEPAL will in each class randomly select a number of points and extract the class value using the provided resolution.

start by selecting btn:`sample classification`. In the opened popup window, where all the parameter can be set.

-   **sample per class**: that's the number of sample per class of the provided image. The more sample you request, the more accurate the model will be. If too many sample are selected though, the on-the-fly visualization will never render. default to: :code:`1000`.
-   **scale to sample in**: the scale use to create the sample in the provided image. It should match the image to classify resolution. default to: :code:`30m`.
-   **EE asset ID**: The id af the classification to sample. It should be an :code:`ee.Image` accecible to the user. 
-   **class band**: The class to use for classification value. The dropdown will be filled with the found bands in the provided asset.

.. note::

    To reproduce this example, use the following asset as image to sample: :code:`projects/sepal-cookbook/assets/classification/zmb_copernicus_landcover`.

.. thumbnail:: ../_images/cookbook/classification/import-training-sample.png
    :group: classification-recipe
    :title: parameters to sample training data from an existing classification

.. warning::

    When all the parameters are selected SEPAL build the sampling values on the fly, it can take time. They will only be displayed once the sampling is validated.

Click on :btn:`<fas fa-chevron-right> Next` to display the sampling summary. In this panel, SEPAL displays each class of the legend (the one defined in the previous section) and the number of samples created for it. Click on the :btn:`<fas fa-plus>` (1) buttons to change the number of samples in a specific class. SEPAL ignore by default the samples with :code:`null` value. One can select :btn:`default` (2) for any of the class so that these point end up in this default class instead of being ignored.

.. thumbnail:: ../_images/cookbook/classification/import-training-sample-summary.png
    :group: classification-recipe
    :title: parameters to sample training data from an existing classification

SEPAL recipe
############

SEPAL is also able to dirrectly apply a model build in another recipe as training data. In this case we are not importing the points but all the model from the external recipe. It will not add points to the map. It's useful when the same classification need to be applied on multiple years on the same area. The classification work can be carried on only on the first year and then applied recursively on all the others.

Click on :btn:`saved SEPAL recipe` to open the popup window. In the dropdown select one of the recipe saved on your SEPAL account. 

.. note::
    
    The imported recipe needs to be a classification recipe, if none are found, the dropdown will be empty.
    This recipe cannot come from another SEPAL account.

.. thumbnail:: ../_images/cookbook/classification/import-training-recipe.png
    :group: classification-recipe
    :title: Select an already existing SEPAL classification recipe to use its training data for your own classification

Use auxiliaries datasets
^^^^^^^^^^^^^^^^^^^^^^^^

some information that could be useful to the classification model are not always included in your Image bands. A comon exaple is Elevation. In order to improve the quality of the classification, SEPAL can provide some extra-dataset to add auxiliaries bands to the classification model. 

click on :btn:`AUX` to open the Auxiliaries tab. 3 sources are currently implemented in the platform. Any number of them can be selected. 

-   **Latitude**: On-the-fly latitude dataset build from the coordinates of each pixels center
-   **Terrain**: From the `NASA SRTM Digital Elevation 30m <https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003>`__ dataset, SEPAL wil use the :code:`elevation`, :code:`slope` and :code:`aspect` bands. It will also add an :code:`eastness` and :code:`northness` band derived from the :code:`aspect` one.
-   **Water**: from the `JRC Global Surface Water Mapping Layers, v1.3 <https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_3_GlobalSurfaceWater>`__ dataset, SEPAL will add the following bands:  :code:`occurrence`, :code:`change_abs`, :code:`change_norm`, :code:`seasonality`, :code:`max_extent`, :code:`water_occurrence`, :code:`water_change_abs`, :code:`water_change_norm`, :code:`water_seasonality` and :code:`water_max_extent`

.. thumbnail:: ../_images/cookbook/classification/auxiliary_tab.png
    :group: classification-recipe
    :title: Select preset auxiliary datasource to improve the quality of the classification

Classifier configuration
^^^^^^^^^^^^^^^^^^^^^^^^

.. warning:: 

    Customizing the classifier is a section dedicated to very advance user. make sure that you well understand how the classifier you're using works before changing it' parameters.

.. note::

    The default value is a Random Forest classifier using 25 trees.

The classification tools used in SEPAL is based on the `Smile - Statistical Machine Intelligence and Learning Engine Javascript <https://haifengl.github.io/classification.html>`__ librairy. Please refer to their documentation for specific description of each model. 

Click on :btn:`CLS` to open the classification parameter menu. SEPAL provide supports 7 classifiers: 

-   Random Forest
-   Gradient tree boost
-   cart
-   Naive Bayes
-   SVM
-   Min distance
-   Descision Tree

For each of them the workflow is the same. First select the classifier by clicking on the corresponding name then SEPAL will display some of the parameters available. Click on :btn:`more` at the bottom left side of the panel to fully customize your classifier. The classification results will be updated on-the-fly.

.. thumbnail:: ../_images/cookbook/classification/cls_less.png
    :width: 49%
    :group: classification-recipe
    :title: The only simple parameter of a random forest classifier (number of trees)

.. thumbnail:: ../_images/cookbook/classification/cls_more.png
    :width: 49%
    :group: classification-recipe
    :title: All the customization parameters of a random forest classifier

On-the-fly training
-------------------

.. warning::

    This process requires good understanding of the visualization feature of SEPAL so please refer to the `feature <#>`__ section for more.

Once all the parameter are set, the user is free to add extra training data in the web interface, the new points will be added to the final model and improve the quality of the classification. 

set up the view
^^^^^^^^^^^^^^^

In order to improve the classification One must set-up the view to display multiple information. This guideline can be extende and modified but it's a good starting point.

On the following image we displayed: 

-   the current recipe (1) using the class colors in categorical mode.
-   the current Image (what you are classifying) (2) using the NIR,RED,SWIR band combination
-   extra visual dataset NICFI PlaneLab data (3) from 2021.

On the view, the numbers (4) indicates cluster of existing training points. Zoom-in and they will be displayed as marker using the color of the class they mark (5).

.. important:: 

    This initial classification has been set using sampled data. As there are sampled from a bigger image, some are out of the image Area of interest, they will have no impact on the classification as they are applied on masked pixels (6). 

.. thumbnail:: ../_images/cookbook/classification/classification_view.png
    :group: classification-recipe
    :title: A classification set up ready to add new training data


Select points 
^^^^^^^^^^^^^

To start adding points, start the training interface by clicking on :btn:`<fas fa-map-marker>` on the top right side of the screen (1). Once clicked, the button turn into a darker background and the pointer of the mouse become a :icon:`fas fa-plus`.

The process to add new training data is the following: 

#.   **click on the map to select a point**: You can click in any of the panel (no restricted to the recipe one) but to be useful the point need to be within the border of the AOI. If it's not already the case the class selection panel will open itself on the top right side of the window (2). 
#.   **select the class value**: The previous class value is preselected but you can change it to any other class value from the defined legend. The legend is displayed as :code:`<legend_classname> (<legend_value>)`.

You can now click elswhere on the map to add another point. If you are satisfied with the classification, click on :btn:`<fas fa-times> close` (3) and click again on :btn:`<fas fa-map-marker>` to stop editiing the points. Every time a new point is added, the classification map is recomputed and rendered in the left window.

.. thumbnail:: ../_images/cookbook/classification/add_point.png
    :group: classification-recipe
    :title: Manually adding new training data in the model

Modify existing points
^^^^^^^^^^^^^^^^^^^^^^

To modify existing points, click the :btn:`<fas fa-map-marker>` to open the point editing interface and follow the following steps: 

#.   **select a point**: To select a point click on an existing marker. It will appear bolder than the others. If it's not already the case the class selection panel will open itself on the top right side of the window.
#.   **change the class value**: The point class will be selected in the editing menu with a :icon:`fas fa-check`. click on any other class value to chage it.

Check the validity
^^^^^^^^^^^^^^^^^^

SEPAL embeds information to help the user understand if the number of training data is sufficient to produce an accurate classification model. In the recipe window, change the band combination to :code:`class probality`. The user display now the probability of the model i.e. what is the confidency level of the level with output class for each pixel. if the value is high (>80%) then the pixel can be considered valid. If the value is less, the model need more training data or extra bands to improve the analysis. 

In the example image, the lake is classified as "permanent water body" with a confidence of 65% wich is better than the rest of the vegetation around it. 

.. thumbnail:: ../_images/cookbook/classification/classification_confidence.png
    :group: classification-recipe
    :title: The classification confidence around a lake in eastern Zambia

This analysis can also be conducted class by class using the built-in :code:`<class_name> %` bands. Select the one corresponding to the class you want to assess as on the following image and you'll get the % of confidence for each pixel to be in the sub-mentioned class.

.. thumbnail:: ../_images/cookbook/classification/water_confidence.png
    :group: classification-recipe
    :title: The classification confidence of "permanent water body" around a lake in eastern Zambia

Export
------

start download
^^^^^^^^^^^^^^

Clicking on the :icon:`fas fa-cloud-download-alt` tab will open the retrieve panel where the you can select the exportation parameters (1).

You need to select the band to export (2). There is no max number of bands, however, exporting useless bands will only increase the size and the time of the output. 

You can set a custom scale for exportation (3) by changing the value of the slider (m). Requesting a smaller resolution than images native resolution will not improve the quality of the output, just its size so keep in mind that Sentinel data native resolution is 10 m and Landsat is 30 m.

You can export the image to :btn:`sepal workspace` or to :btn:`google earth engine asset`. The same image will be exported but in the first case you will find it in :code:`.tif` format in the :code:`downloads` folder, in the second one the image will be exported to your GEE account asset list. 

.. warning::

    If :btn:`google earth engine asset` is not displayed, it means that your GEE account is not connected to SEPAL, please refer to `Connect SEPAL to GEE <../setup/gee.html>`__.

Click on :btn:`<fas fa-check> apply` to start the download process. 


.. thumbnail:: ../_images/cookbook/classification/export.png
    :group: classification-recipe
    :title: The classification confidence of "permanent water body" around a lake in eastern Zambia

Exportation status
^^^^^^^^^^^^^^^^^^

Going to the task tab (bottom left corner using the :btn:`<fa fa-tasks>` or :btn:`<fa fa-spinner>` buttons —depending on the loading status—), you will see the list of the different loading tasks. The interface will provide you with information about the task progress and it will display an error if the exportation has failed. If you are unsatisfied with the way we present information, the task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    This operation is running between GEE and SEPAL servers in the background, you can thus close the SEPAL page without killing the process.

When the task is finished the frame will be displayed in green as shown on the second image.

.. thumbnail:: ../_images/cookbook/time_series/download.png
    :width: 49%
    :title: Evolution of the downloading process of the recipe displayed in the task manager of SEPAL.
    :group: classification-recipe

.. thumbnail:: ../_images/cookbook/time_series/download_complete.png
    :width: 49%
    :title: Completed downloading process of the recipe displayed in the task manager of SEPAL.
    :group: classification-recipe

Access
^^^^^^

Once the download process is done, you can access the data in your SEPAL folders. The data will be stored in the :code:`downloads` folder using the following format:

.. code-block::

    .
    └── downloads/
        └── <CLASSIF name>/
            ├── <CLASSIF name>_<gee tile id>.tif
            ├── <CLASSIF name>_<gee tile id>.tif
            ├── ...
            ├── <CLASSIF name>_<gee tile id>.tif
            └── <CLASSIF name>_<gee tile id>.vrt

.. danger::

    Understanding how images are stored in an Classification output is only required if you want to manually use them. The SEPAL applications are bound to this tiling system and can digest this information for you.

The data are stored in a folder using the name of the Classification as it was set in the first section of this document. As the number of data is spatially too big to be exported at once, the data are cut into small pieces and brought back together in a :code:`<CLASSIF name>_<gee tile id>.vrt` file. 

.. tip:: 

    The full folder with a consistent tree folder is required to read the `.vrt`








