Vector file manager
===================

This module has been designed on top of the interactive framework, `sepal_ui <https://github.com/12rambau/sepal_ui>`_, allowing users to upload files from their local computers and transform them into assets in Google Earth Engine (GEE). The module can also be used to produce a grid on top of any area of interest (AOI), coresponding to our best product (NICFI 2.5 metre resolution 10 kilometre x 10 kilometre grid).

.. note::

    Both operations will end with a dialog window containing the ID of your asset, which can be used in other SEPAL tools by copying and pasting it.

Upload file in SEPAL and GEE
----------------------------

Using the first avalailable tile, upload any file from your local computer to SEPAL.

.. figure:: https://raw.githubusercontent.com/openforis/import_to_gee/master/doc/img/import.png

Once the file is available in your **SEPAL folders**, use it in the **AOI selector**. This selector has been customized to only allow selection through:

- :guilabel:`admin level 2`: Select Administrative Level 2
- :guilabel:`draw a shape`: Manually draw a shape on the map 
- :guilabel:`Upload file`: Use a shapefile as an asset
- :guilabel:`Use point file`: Use a :code:`.csv` file as an AOI asset; while the point file needs to have at least three columns (ID, latitude, longitude), any custom name can be used.

By validating the selection, a task will be launched in GEE to transform your table into a GEE asset. Go to your **earthengine** task list to monitor the upload process.

.. figure:: https://raw.githubusercontent.com/openforis/import_to_gee/master/doc/img/results.png

Create grid over AOI
--------------------

The second drawer will allow you to create a grid on top of any AOI. The grid corresponds to the PlanetLab grid, in order to fit the needs of our best product, in terms of resolution (2.5 metres).

.. note::

    PlanetLab constructs a 2048 x 2048 grid of squares. Since the latitude is larger (20048966.10 m vs 20026376.39 m), PlanetLab extends the longitude to maintain a square shape. The extreme -90 and +90 bands are thus excluded but there are no relevant cells for forestry observation.
    
An extra column is added to the grid: **Batch**. You can select the size of the batch by changing the width of the batch using the initial grid cell as a unit (e.g. by setting :guilabel:`grid size` to 10 you'll create a grid batch of 10 x 10 cells). The naming will be automatically set according to your AOI name and batch size.

By validating, you will create a GeoJSON file that will be stored in :code:`module_results/aoi/<asset_name>.geojson`, launching the creation of the same grid in your GEE assets.

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/vector_manager/release/doc/en.rst
