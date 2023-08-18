Vector file manager
===================

This module have been designed on top of the interactive framework `sepal_ui <https://github.com/12rambau/sepal_ui>`_. it allows the upload files from its local computer and transform them into assets in Google Earth Engine. On top of any AOI the module can also be used to produce a grid coresponding to our best product (NICFI 2,5m resolution10x10km grid). 

.. note:: 

    both operations will end with a dialog window with the ID of your asset. Copy-paste it to use this asset in other SEPAL tools

Upload file in SEPAL and GEE 
----------------------------

Using the first avalaibale tile you can upload any file from your local computer to SEPAL. 

.. figure:: https://raw.githubusercontent.com/openforis/import_to_gee/master/doc/img/import.png

Once the file is available in your SEPAL folders use it in the AOI selector. This selector have been customized to only allow selection through: 

- :guilabel:`admin level 2`: select an administrative level 2
- :guilabel:`draw a shape`: manually draw a shape on the map 
- :guilabel:`Upload file`: Use a shapefile as an asset
- :guilabel:`Use point file`: Use a :code:`.csv` file as an aoi asset. Point file need to have at least 3 columns (id, lattitude and longitude) but you can use any custom names

By validating the selection a task will be launched on GEE to transform your table into a GEE asset. please go to your earthengine task list if you want to monitor the evolution of your upload.

.. figure:: https://raw.githubusercontent.com/openforis/import_to_gee/master/doc/img/results.png

Create Grid over AOI
--------------------

The second drawer will allow you to create a grid on top of any AOI. THe grid is corresponding to the Planet Lab Grid to fit the needs of our best product in term of resolution (2.5m). 

.. note:: 

    the planet grid is constructing a 2048x2048 grid of SQUARES. The latitude extends is bigger (20048966.10m VS 20026376.39) so to ensure the "squariness" Planet lab have based the numerotation and extends of it square grid on the longitude only. the extreme -90 and +90 bands are thus exlucded but there are no so relevant cells for forestry observation
    
An extra column is added to the grid called "batch" you can select the size of the batch by changing the width of the batch usin the initial grid cell as unit. E.g. by setting :guilabel:`grid size` to 10 you'll create grid batch of 10x10 cells. The naming will be set automatically according to your AOI name and the batch size. 

By validating, you will create a geojson file that will live in :code:`module_results/aoi/<asset_name>.geojson` and launch the creation of the same grid in your GEE assets.


.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/vector_manager/release/doc/en.rst
