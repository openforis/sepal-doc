SEPAL recipes
=============

Overview 
--------

Harness high performance cloud-based computing and modern geospatial data infrastructures via SEPAL recipes. They are the main feature of the platform and offer users the ability to query and process satellite data quickly and efficiently, tailor their products for local needs, and produce sophisticated and relevant geospatial analyses quickly and easily.  

A SEPAL recipe is a record of the steps and parameters used to make a dataset (e.g. optical mosaic, radar mosaic, classifiction, etc.). The recipe can be saved and the same data re-created 'on-the-fly' whenever needed or used in further analyses. A recipe is not, in itself, data. Using SEPAL recipes enables documentation of the parameters and steps used to create mosaics / composites, classifications, time-series and other datasets or information products. SEPAL recipes, once saved, are available from the SEPAL interface after you login to the platform. Recipes can be copied (for example to change only the sensor used, leaving all other parameters the same), deleted, and run.

With recipes, users can get access Google Earth Engine's multi-petabyte catalog of satellite imagery and use their planetary-scale analysis capabilities without writing a single line of code. Just connect your Google account to SEPAL.

Gallery
-------

.. thumbnail:: https://user-images.githubusercontent.com/149204/132474880-12333a36-dee0-4bdc-a0b4-0e9aab24b601.png
    :width: 30%
    :title: recipe list displayed in the web interface
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132481048-6149f776-a7ed-47cb-8f75-3519aa1b8f1e.png
    :width: 30%
    :title: create a recipe from available workflows
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132482428-16ef1555-26bc-441a-8717-d65db3b62ef4.png
    :width: 30%
    :title: optical mosaic of the Rome city in CIV colors
    :group: cookbook-index

.. thumbnail:: https://user-images.githubusercontent.com/149204/132474895-da433549-5d52-48cf-93ae-23c0ee9d47c0.png
    :width: 30%
    :title: nicfi planet composite NDVI false colors
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

    It is recommended to connect your SEPAL account to your Google Earth Engine account in order to read/write from GEE assets. If your accounts are not linked, you will only be able to download data to your SEPAL workspace.

To start a recipe, first go to the Process tab :icon:`fa fa-globe`. There you'll see the list of all the saved recipes in your SEPAL account.

.. thumbnail:: https://user-images.githubusercontent.com/149204/132474880-12333a36-dee0-4bdc-a0b4-0e9aab24b601.png
    :title: recipe list displayed in the web interface
 
Then click on the green :icon:`fa fa-plus-circle` button in the bottom right corner. It will open the recipe type selector popup. Select any of the available recipe type and follow our tutorials to know more about its usage. 

.. thumbnail:: https://user-images.githubusercontent.com/149204/132481048-6149f776-a7ed-47cb-8f75-3519aa1b8f1e.png
    :title: create a recipe from available workflows

recipes
-------

.. toctree::
    :maxdepth: 1
    :glob:

    *
