SEPAL recipes
=============

Overview 
--------

Harness high performance cloud-based computing and modern geospatial data infrastructures via SEPAL recipes. They are the main feature of the platform and offer users the ability to quickly and efficiently query and process satellite data, tailor their products for local needs, and produce sophisticated and relevant geospatial analyses.  

A SEPAL recipe is a record of the steps and parameters used to make a dataset (e.g. optical mosaic, radar mosaic, classification, etc.). The recipe can be saved, with the same data re-created, "on-the-fly" whenever needed or used in further analyses. A recipe is not, in itself, data. Using SEPAL recipes enables documentation of the parameters and steps used to create mosaics, composites, classifications, time-series and other datasets or information products. SEPAL recipes, once saved, are available in the SEPAL interface after you log in to the platform. Recipes can be run, deleted, or copied (e.g. to change the sensor used, while leaving all other parameters the same).

With recipes, you can access Google Earth Engine's (GEE) multi-petabyte catalog of satellite imagery and utilize their planetary-scale analysis capabilities without writing a single line of code, simply by linking your Google and SEPAL accounts.

Gallery
-------

.. thumbnail:: https://user-images.githubusercontent.com/149204/132474880-12333a36-dee0-4bdc-a0b4-0e9aab24b601.png
    :width: 30%
    :title: Recipe list displayed in the web interface.
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132481048-6149f776-a7ed-47cb-8f75-3519aa1b8f1e.png
    :width: 30%
    :title: Create a recipe from available workflows.
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132482428-16ef1555-26bc-441a-8717-d65db3b62ef4.png
    :width: 30%
    :title: Optical mosaic of the city of Rome in CIV colors.
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132474895-da433549-5d52-48cf-93ae-23c0ee9d47c0.png
    :width: 30%
    :title: Norway’s International Climate & Forests Initiative (NICFI) planet composite NDVI false colors
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132483174-154e792e-b6ce-4b22-ad08-1b8e4fdda829.png
    :width: 30%
    :title: sentinel1 time scan
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132474903-0d1db533-7427-49f6-9981-07aa5a0f6b71.png
    :width: 30%
    :title: sentinel1 harmonics
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132474907-d4a018a1-282f-4dbd-b870-90bae470d1a0.png
    :width: 30%
    :title: classification
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132474909-3a3c9f9d-4fb9-42b8-be01-2b354c7283a3.png
    :width: 30%
    :title: ccdc chart
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132474911-13fdd36a-e4fd-4ad2-93e2-e0a53510b1dc.png
    :width: 30%
    :title: visparams
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132478296-627a62cd-9d7b-40cf-a1aa-034c50664cf6.png
    :width: 30%
    :title: layers layout
    :group: cookbook-index

Start a recipe
--------------

.. tip::

    It is recommended to connect your SEPAL account to your GEE account, so that you can read and write GEE assets. If your accounts are not linked, you will only be able to download data to your SEPAL workspace.

To start a recipe, go to the Process tab :icon:`fa fa-globe`. There you'll see the list of all the saved recipes in your SEPAL account.

.. thumbnail:: https://user-images.githubusercontent.com/149204/132474880-12333a36-dee0-4bdc-a0b4-0e9aab24b601.png
    :title: Recipe list displayed in the web interface.
 
Click on the green :icon:`fa fa-plus-circle` button in the lower-right corner. It will open the recipe type selector pop-up. Select any of the available recipe types and follow our tutorials to learn more about each type's usage. 

.. thumbnail:: https://user-images.githubusercontent.com/149204/132481048-6149f776-a7ed-47cb-8f75-3519aa1b8f1e.png
    :title: Create a recipe from available workflows.

Save a recipe
-------------

.. note::

    Using saved recipes is the recommended method for sharing parameters to developers when debugging.

Select a recipe in the main menu to display it in a tab. Then click on :btn:`<fas fa-bars>` in the upper-right corner and select :btn:`Export recipe`. The file will be downloaded to your computer using the following name: :code:`<name_of_the_recipe>.json.zip`.

.. thumbnail:: ../_images/cookbook/index/export_recipe.png
    :title: Export the recipe to your local computer.


Recipes
-------

.. toctree::
    :maxdepth: 1
    
    optical_mosaic
    radar_mosaic
    planet_mosaic
    classification
    time_series
    ccdc
    ccdc_slice
