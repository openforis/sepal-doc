Classification
==============

Build supervised classifications of mosaic images to create easy-to-use user interfaces with the Classification recipe
----------------------------------------------------------------------------------------------------------------------

Overview
--------

With this recipe, SEPAL will help users build a supervised classification of any mosaic image. It is built on top of the most advanced tools available on Google Earth Engine (GEE) (including the classifiers CART, RandomForest, NaiveBayes and SVM), allowing users to create an easy-to-use user interface to:

-   select the image to classify;
-   define the class table; and
-   add training data from external sources and on-the-fly selection.

In combination with the other tools of SEPAL, the classification recipe can help you provide accurate land-use maps, without writing a single line of code.

Start
-----

Once the classification recipe is selected, SEPAL will show the recipe process in a new tab (1) and the **Image selection** window will appear in the lower-right (2).

.. thumbnail:: ../_images/cookbook/classification/landing.png
    :group: classification-recipe
    :title: The landing page of the classification recipe.

The first step is to change the name of the recipe. This name will be used to identify your files and recipes in SEPAL folders. Use the best-suited convention for your needs. Simply double-click the tab and enter a new name. It will default to :code:`Classification_<timestamp>`.

.. thumbnail:: ../_images/cookbook/classification/default_title.png
    :title: Classification default title.
    :width: 49%

.. thumbnail:: ../_images/cookbook/classification/modified_title.png
    :title: Classification modified title.
    :width: 49%

.. note::

    The SEPAL team recommends using the following naming convention: :code:`<image_name>_<classification>_<measures>`.

Parameters
----------

In the lower-right corner, the following five tabs are available, allowing you to customize the time series to your needs:

-   :guilabel:`IMG`: The image to classify.
-   :guilabel:`LEG`: The legend of the classification system.
-   :guilabel:`TRN`: The training data of the model.
-   :guilabel:`AUX`: The auxiliary global dataset to use in the model.
-   :guilabel:`CLS`: The classifier configuration.

.. thumbnail:: ../_images/cookbook/classification/parameters.png
    :group: classification-recipe
    :title: The parameters of the classification recipe.

Image selection
^^^^^^^^^^^^^^^

The first step consists of selecting the image bands on which to apply the classifier. The number of selected bands (i.e. images) is not limited.

.. note::

    Keep in mind that increasing the number of bands to analyse will improve the model but slow down the rendering of the final image.

.. note::

    If multiple images are selected, each selected image should overlap each other. If masked pixels are found in one of the bands, the classifier will mask them.

Select :btn:`<fa-solid fa-plus> Add`. The following screen should be displayed:

.. thumbnail:: ../_images/cookbook/classification/image_source.png
    :group: classification-recipe
    :title: The two available image sources for classification.

Image type
""""""""""

Users can select images coming from an **Existing recipe** or an exported **GEE asset** (see advantages and disadvantages below). Both should be an :code:`ee.Image`, rather than a :code:`Time series` or :code:`ee.ImageCollection`.

-   **Existing recipe**:

    -   Advantages:

        -   All of the computed bands from SEPAL can be used.
        -   Any modification to the existing recipe will be propagated in the final classification.

    -   Disadvantages:

        -   The initial recipe will be computed at each rendering step, slowing down the classification process and potentially breaking on-the-fly rendering due to GEE timeout errors.

-   **GEE asset**:

    -   Advantages:

        -   Can be shared with other users.
        -   The computation will be faster, as the image has already been exported.

    -   Disadvantages:

        -   Only the exported bands will be available.
        -   The :code:`Image` needs to be re-exported to propagate changes.

Both methods behave the same way in the interface.

Select bands
""""""""""""

.. tip::

    For this example, we will use a public asset created with the optical mosaic tool from SEPAL. It's a Sentinel-2 mosaic of Eastern Province in Zambia during the dry season from 2012 to 2020. Multiple bands are available.

    Use the following asset name if you want to reproduce our workflow: :code:`projects/sepal-cookbook/assets/classification/zmb-eastern_2012_2021`

Image bands
###########

Once an asset has been selected, SEPAL will load its bands in the interface. You can use any band that is native to the image as input for the classification process. Simply click on the band name to select them. The selected bands are summarized in the expansion panel title (1) and displayed in gold in the panel content (2).

In this example, we selected the following:

-   :code:`red`
-   :code:`nir`
-   :code:`swir`
-   :code:`green`

.. thumbnail:: ../_images/cookbook/classification/native_bands.png
    :group: classification-recipe
    :title: Select :code:`red`, :code:`nir`, :code:`swir`, and :code:`green` from the source image.

Derived bands
#############

The analysis is not limited to natively available bands. SEPAL can also build additional derived bands on-the-fly.

Select :btn:`<fa-solid fa-plus> Derived bands` at the bottom of the pop-up window and select the deriving method to. This will add a a new panel to the expansion panel with the selected method name (1). The selected method will be applied to the selected bands.

.. note::

    If more than two bands are selected, the operation will be applied to the Cartesian product of the bands. If you select bands :math:`A`, :math:`B` and :math:`C`, and apply the :code:`Difference` derived bands, you'll add three bands to your analysis:

    -   :math:`A - B`
    -   :math:`A - C`
    -   :math:`B - C`

.. thumbnail:: ../_images/cookbook/classification/derived_bands.png
    :group: classification-recipe
    :title: Select :code:`red` and :code:`nir` in the normalized difference derived band, adding one extra band to the analysis: the NDVI.

.. note::

    You should notice that in the figure, we compute the normalized difference between :code:`nir` and :code:`red` (i.e. the NDVI). It is also precomputed in the :code:`Indexes` derived bands.

Once the image selection is done, select :btn:`<fa-solid fa-check> Apply` and the pop-up window will close. The images and bands will be displayed in the :guilabel:`IMG` panel on the lower-right corner of the screen. By selecting the :btn:`<fa-solid fa-trash>` button, you will remove the image and its band from the analysis altogether.

.. thumbnail:: ../_images/cookbook/classification/selected_bands.png
    :group: classification-recipe
    :title: All the selected bands from the selected images.

From there, select :btn:`<fa-solid fa-chevron-right> Next` to continue to the next step.

Legend setup
^^^^^^^^^^^^

In this step, the user will specify the legend that should be used in the output classified image. Any categorical classification that associates integer value to a class name will work. SEPAL provides multiple ways to create and customize a legend.

.. thumbnail:: ../_images/cookbook/classification/landing_legend.png
    :group: classification-recipe
    :title: The landing menu of the legend parameter.

.. important::

    Legends created here are fully compatible with other functionalities of SEPAL, including applications.

Manual legend
"""""""""""""

The first and most natural way of building a legend is to do it from scratch.

Select :btn:`<fa-solid fa-plus> Add` to add a new class to your legend.

A class is defined by three key elements:

- Color (1): Select the small color square to open the color selector and choose any color (color[s] must be unique).
- Value (2): Select any integer value (value must be unique).
- Class (3): Insert a class description (cannot be empty).

Select the :btn:`<fa-solid fa-plus> Add` button again to add an extra class line. The :btn:`<fa-solid fa-trash>` button can be used to remove a specific line.

.. tip::

    Select :btn:`HEX` (4) to display the hexadecimal value of the selected color. It can also be used to insert a known color palette by utilizing its values.

If multiple classes are created and you are not sure which one to use, you can apply colors to them by selecting a preselected color-map (5). They are provided by the `gee community <https://github.com/gee-community/ee-palettes>`__ and will be applied to every existing class in your panel.

.. thumbnail:: ../_images/cookbook/classification/create_legend.png
    :group: classification-recipe
    :title: Manual creation of a legend.

Import legend
"""""""""""""

If you already have a file describing your legend, you can use it, rather than identifying every legend item individually. Your legend needs to be saved in .csv format and contain the following information:

- color (stored as a hexadecimal value [e.g. "#FFFF00"] or in three columns [red, blue, green]);
- value (stored as an integer); and
- class (stored as a string).

.. note::

    The column names will help SEPAL predict information, but are not compulsory.

For example, a .csv file containing the following information is fully qualified to be used in SEPAL:

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

This one is the same using RGB-defined colors:

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

Once the fully qualified legend file has been prepared on your computer, select :btn:`<fa-solid fa-chevron-up>` and then :code:`Import from CSV`, which will open a pop-up window where you can drag and drop the file or select it manually from your computer files.

As shown on the next image, you can then select the columns that are defining your .csv file (select :btn:`Single column` for hexadecimal-defined colors and :btn:`multiple columns` for RGB-defined colors).

.. thumbnail:: ../_images/cookbook/classification/import_csv.png
    :group: classification-recipe
    :title: Import legend from csv.

Select :btn:`<fa-solid fa-check> Apply` to validate your selection. The classes will be added to the legend panel and you'll be able to modify the legend using the parameters presented in the previous section.

.. thumbnail:: ../_images/cookbook/classification/imported_csv.png
    :group: classification-recipe
    :title: Imported legend from a .csv file.

Select :btn:`<fa-solid fa-check> Done` to validate this step.

Every panel should be closed and the colors of the legend are now displayed at the bottom of the map. No classification is performed, as we didn't provide any training data. Nevertheless, this step is the last mandatory step for setting parameters. Training data can be added using the on-the-fly training functionality.

Export legend
"""""""""""""

Once your legend is validated, select the :btn:`<fa-solid fa-chevron-up>` and then :code:`Export as CSV`.

A file will be downloaded to you computer named :code:`<recipe_name>_legend.csv`, which will contain the legend information in the following format:

.. code-block::

    color,value,label
    #006400,10,Tree cover
    ...


Select training data
^^^^^^^^^^^^^^^^^^^^

.. note::

    This step is not mandatory.

Two inputs are required to create the classification output:

- pixel values (e.g. bands) to classify; and
- training data to set up the classification model.

This menu will help the user manage the training data of the model used. To open it, select :btn:`TRN` in the lower-right side of the window.

.. thumbnail:: ../_images/cookbook/classification/training_landing.png
    :group: classification-recipe
    :title: Training menu opening window.

Collected reference data
""""""""""""""""""""""""

Collected reference data are data selected on-the-fly by the user. The workflow will be explained later in the documentation. In this panel, this type of data can be managed by the user.

The data appear as a pair, associating coordinates to a class value, which will be used to create training data in the classification model.

If you're satisfied with the current selection and you want to share the data with others, select :btn:`<fa-solid fa-chevron-up>` and then :code:`Export reference data to csv`. A file will be created named: :code:`<recipe_name>_reference_data.csv` and sent to your computer. It will embed all of the gathered point data using the following convention:

.. code-block::

    XCoordinate,YCoordinate,class
    32.77189961605467,-11.616264558754402,80
    ...

If you are not satisfied with the selected data, select :btn:`<fa-solid fa-chevron-up>` and then :code:`Clear collected reference data` to remove all collected data from the analysis.

.. tip::

    A confirmation pop-up window should prevent you from accidentally deleting everything.

Existing training data
""""""""""""""""""""""

Instead of collecting all of the data by hand, SEPAL provides numerous ways to include already existing training data into your analysis. The data can be from multiple formats and will be included in the model to improve the quality of the final map.

.. note::

    The imported files can use an extended version of the legend provided in the previous step, but to avoid unexpected behaviour, at least one of the classes of your legend and the provided training data need to match.

.. note::

    If the added training data are outside of the image to classify, they will have no impact on the final result (with the exception of the SEPAL recipe).

To add new data, select :btn:`<fa-solid fa-plus> Add` and choose the type of data to import:

.. thumbnail:: ../_images/cookbook/classification/import-training-data.png
    :group: classification-recipe
    :title: The different types of training data available in SEPAL.

CSV
###

By selecting :btn:`csv file`, SEPAL will request a file from your computer in :code:`.csv` format. The file needs to include two pieces of information: geographic coordinates and class value.

This can be done using coordinates in :code:`EPSG:4326` latitude and longitude, as well as a `GeoJSON <https://geojson.org>`__ compatible point object. The file can embed other multiple columns that will not be considered during the analysis.

The following table is compatible with SEPAL:

.. code-block::

    XCoordinate,YCoordinate,class,class_name,editor_name
    32.77189961605467,-11.616264558754402,80,Shrublands,Pierrick rambaud
    ...

The columns used to define the X (longitude) and Y (latitude) coordinates are manually set up in the pop-up window. Select :btn:`<fa-solid fa-chevron-left> Next` once every column is filled.

.. thumbnail:: ../_images/cookbook/classification/import-training-csv-coords.png
    :group: classification-recipe
    :title: Import a .csv file in SEPAL as training data.

.. tip::

    If your file contains a GeoJSON column instead of coordinates, select :btn:`geojson column` to switch the interface to one column selection.

Now that you have set up the coordinates of your points, SEPAL will request the columns specifying the class value (not the name) in a second frame. Only the single column is supported so far. Select the column from your file that embeds the class values.

.. tip::

    Using the :code:`row filter expression` text field, one can filter out some lines of the table. Refer to the `features <#>`__ section to learn more.

.. thumbnail:: ../_images/cookbook/classification/import-training-csv-class.png
    :group: classification-recipe
    :title: Import a .csv file in SEPAL as training data.

Select :btn:`<fa-solid fa-chevron-left> next` to add the data to the model. SEPAL will provide a summary of the classes in the legend of the classification and the number of training points added by your file.

Selecting the :btn:`<fa-solid fa-check> Done` button will complete the uploading procedure.

.. thumbnail:: ../_images/cookbook/classification/import-training-csv-summary.png
    :group: classification-recipe
    :title: Import a .csv file in SEPAL as training data.

GEE table
#########

By selecting :btn:`Earth Engine Table`, SEPAL will request a file from your computer in :code:`.csv` format. The file needs to provide two pieces of information: geographic coordinates and class value.

The process is nearly the same as found in the documentation above discussing .csv tables. The only difference should be the geometry column, as GEE assets usually embed a :code:`.goejson` column by default. If this column exists, it will be autodetected by SEPAL.

For the other steps, please reproduce what was presented in the .csv section above.

.. thumbnail:: ../_images/cookbook/classification/import-training-gee-coords.png
    :group: classification-recipe
    :title: Import a GEE table in SEPAL as training data.

.. note::

    To build the documentation example, you can use this public asset: :code:`projects/sepal-cookbook/assets/classification/zmb_eastern_esa_2012_2021_reference_data`.

Sample classification
#####################

Instead of providing dataset points, SEPAL can also extract reference data from an already existing classification. It's a good way to improve an already existing classification system using an image with a better resolution.

To sample data, SEPAL will randomly select a number of points in each class and extract the class value using the provided resolution.

Start by selecting btn:`Sample classification` in the opened pop-up window, where all of the the parameters can be set:

-   **Sample per class**: The number of samples per class of the provided image. The more samples you request, the more accurate the model will be (if too many samples are selected though, on-the-fly visualization will never render; default to: :code:`1000`).
-   **Scale to sample in**: The scale used to create the sample in the provided image (it should match the image to classify resolution; default to: :code:`30 m`).
-   **EE asset ID**: The ID of the classification to sample (it should be an :code:`ee.Image` accessible to the user).
-   **Class band**: The class to use for classification value (the dropdown menu will be filled with the bands found in the provided asset).

.. note::

    To reproduce this example, use the following asset as an image to sample: :code:`projects/sepal-cookbook/assets/classification/zmb_copernicus_landcover`.

.. thumbnail:: ../_images/cookbook/classification/import-training-sample.png
    :group: classification-recipe
    :title: Parameters to sample training data from an existing classification.

.. note::

    When all of the parameters are selected, it can take time, as SEPAL builds the sampling values on-the-fly. They will only be displayed once the sampling is validated.

Select :btn:`<fa-solid fa-chevron-right> Next` to display the sampling summary. In this panel, SEPAL displays each class of the legend (as defined in the previous section) and the number of samples created for it.

Select the :btn:`<fa-solid fa-plus>` (1) buttons to change the number of samples in a specific class. By default, SEPAL ignores the samples with a :code:`Null` value. One can select :btn:`Default` (2) for any of the classes, so that these points end up in this default class instead of being ignored.

.. thumbnail:: ../_images/cookbook/classification/import-training-sample-summary.png
    :group: classification-recipe
    :title: Parameters to sample training data from an existing classification.

SEPAL recipe
############

SEPAL is also able to dirrectly apply a model built in another recipe as training data. In this case, we are not importing the points, but all of the model from the external recipe. It will not add points to the map. It's useful when the same classification needs to be applied on the same area for multiple years. The classification work can be carried out only in the first year and then applied recursively on all the others.

Select :btn:`Saved SEPAL recipe` to open the pop-up window. In the dropdown menu, select one of the recipes saved in your SEPAL account.

.. note::

    The imported recipe needs to be a classification recipe. If none are found, the dropdown menu will be empty.

    This recipe cannot come from another SEPAL account.

.. thumbnail:: ../_images/cookbook/classification/import-training-recipe.png
    :group: classification-recipe
    :title: Select an already existing SEPAL classification recipe to use its training data for your own classification.

Use auxiliary datasets
^^^^^^^^^^^^^^^^^^^^^^

Some information that could be useful to the classification model is not always included in your image bands. A common example is **Elevation**. In order to improve the quality of the classification, SEPAL can provide some extra datasets to add auxiliary bands to the classification model.

Select :btn:`AUX` to open the **Auxiliaries** tab. Three sources are currently implemented in the platform (any number of them can be selected):

-   **Latitude**: On-the-fly latitude dataset built from the coordinates of each pixel's center.
-   **Terrain**: From the `NASA SRTM Digital Elevation 30 m <https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003>`__ dataset, SEPAL will use the :code:`Elevation`, :code:`Slope` and :code:`Aspect` bands. It will also add an :code:`Eastness` and :code:`Northness` band derived from :code:`Aspect`.
-   **Water**: From the `JRC Global Surface Water Mapping Layers, v1.3 <https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_3_GlobalSurfaceWater>`__ dataset, SEPAL will add the following bands: :code:`occurrence`, :code:`change_abs`, :code:`change_norm`, :code:`seasonality`, :code:`max_extent`, :code:`water_occurrence`, :code:`water_change_abs`, :code:`water_change_norm`, :code:`water_seasonality` and :code:`water_max_extent`.

.. thumbnail:: ../_images/cookbook/classification/auxiliary_tab.png
    :group: classification-recipe
    :title: Select preset auxiliary datasource to improve the quality of the classification.

Classifier configuration
^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    Customizing the classifier is a section designed for advanced users. Make sure that you thoroughly understand how the classifier you're using works before changing its parameters.

.. note::

    The default value is a **Random Forest** classifier using 25 trees.

The classification tool used in SEPAL is based on the `Smile - Statistical Machine Intelligence and Learning Engine Javascript <https://haifengl.github.io/classification.html>`__ library. Please refer to their documentation for specific descriptions of each model.

Select :btn:`CLS` to open the classification parameter menu. SEPAL supports 7 classifiers:

-   Random Forest
-   Gradient tree boost
-   cart
-   Naive Bayes
-   SVM
-   Min distance
-   Decision Tree

For each of them, the workflow is the same:

1.  Select the classifier by clicking on the corresponding name. SEPAL will display some of the parameters available.
2.  Select :btn:`More` on the lower left side of the panel to fully customize your classifier. The classification results will be updated on-the-fly.

.. thumbnail:: ../_images/cookbook/classification/cls_less.png
    :width: 49%
    :group: classification-recipe
    :title: The only simple parameter of a random forest classifier (number of trees).

.. thumbnail:: ../_images/cookbook/classification/cls_more.png
    :width: 49%
    :group: classification-recipe
    :title: All of the customization parameters of a random forest classifier.

On the fly training
-------------------

.. note::

    This process requires a good understanding of the visualization feature of SEPAL. Please refer to the `feature <#>`__ section for more information.

Once all of the parameters are set, the user is free to add extra training data in the web interface and the new points will be added to the final model, improving the quality of the classification.

Set up the view
^^^^^^^^^^^^^^^

In order to improve the classification, one must set up the view to display all of the information. While these guidelines could be modified and extended, they are still useful as an introductory resource.

In the following image, we displayed:

-   The current recipe (1) using the class colors in categorical mode.
-   The current image (what you are classifying) (2) using the NIR,RED,SWIR band combination.
-   The extra visual dataset NICFI PlaneLab data (3) from 2021.

The number (4) indicates a cluster of existing training points. Zoom-in and they will be displayed as markers using the color of the class they mark (5).

.. important::

    This initial classification has been set using sampled data. Since they are sampled from a larger image, some are out of the image. They will have no impact on the classification as they are applied to masked pixels (6).

.. thumbnail:: ../_images/cookbook/classification/classification_view.png
    :group: classification-recipe
    :title: A classification set-up ready to add new training data.


Select points
^^^^^^^^^^^^^

To start adding points, open the training interface by selecting :btn:`<fa-solid fa-map-marker>` in the upper-right of the screen (1). Once selected, the background color becomes darker and the pointer of the mouse becomes a :icon:`fa-solid fa-plus`.

The process to add new training data is as follows:

1.   **Click on the map to select a point**: You can click in any of the panels (this is not restricted to the recipe panel), but to be useful, the point needs to be within the border of the AOI. If it's not already the case, the class selection panel will appear in the upper-right of the window (2).
2.   **Select the class value**: The previous class value is preselected, but you can change it to any other class value from the defined legend. The legend is displayed as :code:`<legend_classname> (<legend_value>)`.

You can now click elsewhere on the map to add another point. If you are satisfied with the classification, select :btn:`<fa-solid fa-times> Close` (3) and select :btn:`<fa-solid fa-map-marker>` again to stop editing the points. Every time a new point is added, the classification map is recomputed and rendered in the left window.

.. thumbnail:: ../_images/cookbook/classification/add_point.png
    :group: classification-recipe
    :title: Manually adding new training data in the model.

Modify existing points
^^^^^^^^^^^^^^^^^^^^^^

To modify existing points, select the :btn:`<fa-solid fa-map-marker>` to open the point editing interface and follow the following steps:

1.   **Select a point**: To select a point, click on an existing marker. It will appear bolder than the others. If it's not already the case, the class selection panel will appear in the upper-right of the window.
2.   **Change the class value**: The point class will be selected in the editing menu with a :icon:`fa-solid fa-check`. Select any other class value to change it.

Check the validity
^^^^^^^^^^^^^^^^^^

SEPAL embeds information to help the user understand if the amount of training data is sufficient to produce an accurate classification model. In the recipe window, change the band combination to :code:`Class probability`. The user now sees the probability of the model (i.e. the confidence level of the level with output class for each pixel). If the value is high (>80%), then the pixel can be considered valid; if the value is low (<80%), the model needs more training data or extra bands to improve the analysis.

In the example image, the lake is classified as a "permanent water body" with a confidence of 65%, which is higher than the rest of the vegetation around it.

.. thumbnail:: ../_images/cookbook/classification/classification_confidence.png
    :group: classification-recipe
    :title: The classification confidence around a lake in eastern Zambia.

This analysis can also be conducted class by class using the built-in :code:`<class_name> %` bands. Select the one corresponding to the class you want to assess (as you can see in the following image) and you'll get the % of confidence for each pixel to be in the sub-mentioned class.

.. thumbnail:: ../_images/cookbook/classification/water_confidence.png
    :group: classification-recipe
    :title: The classification confidence of "permanent water body" around a lake in eastern Zambia.

Export
------

Start download
^^^^^^^^^^^^^^

Selecting the :icon:`fa-solid fa-cloud-download-alt` tab will open the **Retrieve** panel where you can select the exportation parameters (1).

You need to select the band to export (2). There is no maximum number of bands; however, exporting useless bands will only increase the size and time of the output.

You can set a custom scale for exportation (3) by changing the value of the slider in meters (m). (Note: Requesting a smaller resolution than images' native resolution will not improve the quality of the output – just its size; keep in mind that the native resolution of Sentinel data is 10 m, while Landsat is 30 m.)

You can export the image to the :btn:`SEPAL workspace` or to the :btn:`Google Earth Engine Asset` list. The same image will be exported, but in the first case you will find it in :code:`.tif` format in the :code:`Downloads` folder; in the second case, the image will be exported to your GEE account asset list.

.. note::

    If :btn:`Google Earth Engine Asset` is not displayed, it means that your GEE account is not connected to SEPAL. Please refer to `Connect SEPAL to GEE <../setup/gee.html>`__.

Select :btn:`<fa-solid fa-check> Apply` to start the download process.

.. thumbnail:: ../_images/cookbook/classification/export.png
    :group: classification-recipe
    :title: The classification confidence of "permanent water body" around a lake in eastern Zambia.

Exportation status
^^^^^^^^^^^^^^^^^^

By going to the **Task** tab (in the lower-left corner using the :btn:`<fa-solid fa-tasks>` or :btn:`<fa-solid fa-spinner>` buttons, depending on the loading status), you will see the list of different loading tasks.

The interface will provide you with information about the task progress and it will display an error if the exportation has failed. If you are unsatisfied with the way we present information, the task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    This operation is running between GEE and SEPAL servers in the background. You can close the SEPAL page without ending the process.

When the task is finished, the frame will be displayed in green, as shown in the second image.

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

Once the download process is done, you can access the data in your SEPAL folders. The data will be stored in the :code:`Downloads` folder using the following format:

.. code-block::

    .
    └── downloads/
        └── <CLASSIF name>/
            ├── <CLASSIF name>_<gee tile id>.tif
            ├── <CLASSIF name>_<gee tile id>.tif
            ├── ...
            ├── <CLASSIF name>_<gee tile id>.tif
            └── <CLASSIF name>_<gee tile id>.vrt

.. note::

    Understanding how images are stored in an optical mosaic is only required if you want to manually use them. The SEPAL applications are bound to this tiling system and can digest this information for you.

The data are stored in a folder using the name of the optical mosaic as it was created in the first section of this article. As the number of data is spatially too big to be exported at once, the data are divided into smaller pieces and brought back together in a :code:`<MO name>_<gee tile id>.vrt` file.

.. tip::

    The full folder with a consistent tree folder is required to read the `.vrt`.


For support, `ask the community <https://groups.google.com/g/sepal-users>`__.
