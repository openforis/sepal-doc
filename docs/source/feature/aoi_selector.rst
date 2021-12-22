Select AOI
==========

Area of Interest Selection
==========================

In the majority of SEPAL modules, the first mandatory input, is the area of interest (AOI), this input will be used as a boundary to cut the process and its outputs. Depending on if you are using the default `:btn:`<fas fa-globe>` process recipes` or the `:btn:`<fas-wrench>` custom modules` you will find different user interfaces.

Recipe AOI
^^^^^^^^^^

The recipe section is accessible through the orange :icon:`fas fa-globe` globe located at the left side of the SEPAL window. 

.. thumbnail:: ../_images/cookbook/optical_mosaic/no_parameters.png
    :title: The 5 tabs to set up SEPAL optical mosaic parameters
    :group: optical-mosaic-recipe

For many of the recipes, an area of interest has to be selected. Locate the AOI selection button at the bottom right corner. Click the :guilabel:`AOI` button to open the selection window.

There are multiple ways to select AOI's in the SEPAL process recipes:

-   Country/province (administrative boundaries).
-   EE Tables (Earth Engine).
-   Drawn polygons.

.. thumbnail:: ../_images/cookbook/optical_mosaic/aoi_landing.png
    :title: The 3 differents ways to select an AOI in SEPAL
    :group: optical-mosaic-recipe

.. tip:: 

    The selected method at this step is not definitive, you can change it at any stage by simply clicking the :icon:`fa fa-globe` :guilabel:`<selection method>` dropdown on the top of the AOI window and a list with the available methods will be displayed.

Administrative boundaries
"""""""""""""""""""""""""

You can select administrative layers as AOI. These geometries are extracted from the `FAO GAUL Level 0 <https://data.apps.fao.org/map/catalog/srv/eng/catalog.search?id=12691#/metadata/9c35ba10-5649-41c8-bdfc-eb78e9e65654>`__ dataset available on `GEE <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1>`__. To use them, select the :guilabel:`Select country/province` method in the dropdown list. 

.. note::

    As GEE does not support non-Latin characters, accents and special characters have been removed from country and province names.

In the first dropdown menu, you will be able to select a Country (administrative layer 0) from the country list.  
Optionally, you can select a province (administrative level 0) within the country selected. The dropdown list is updated on the fly with the 1st administrative level boundaries according to the country selection. If nothing is selected, the whole country will be considered. 

A buffer can be applied to the AOI boundaries, define its size using the provided slider (in km). It is by default set to 0, i.e. disabled. 

.. note:: 

    The area of interest and preview will take longer to show up when buffering is enabled.

Once all the parameters are selected, the AOI will be previewed in the small map at the bottom of the frame. To validate it click the :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom on the AOI and draw it in grey on the map.

.. thumbnail:: ../_images/cookbook/time_series/aoi_administrative.png
    :title: Select AOI based on administrative layers
    :group: optical-mosaic-recipe

EE table
""""""""

You can use custom AOI defined by shapes. These shapes need to be ingested in Earth Engine as a :code:`ee.FeatureCollection` (see `how to upload custom assets to GEE <../setup/gee.html#upload-files-to-gee>`__). To use this method, select :guilabel:`EE table` .

In the first dropdown, provide a completely qualified GEE asset name (e.g. :code:`projects/gtfp-fao/assets/aoi_ecowas`). 

.. warning::

    Make sure you have access to this asset. If that is not the case, ask the owner of the source to modify the sharing permission, otherwise, you won't be able to use the dataset.

-   Select :guilabel:`include all` and the whole geometries associated with the features will be used as an AOI. 
-   Select :guilabel:`filter` and you will be able to provide a column name and a value to filter the table. The Aoi will then be reduced to the filtered features in the input asset. 

A buffer can be applied on these boundaries, define its size using the provided slider (in km). It is by default set to 0, i.e. disabled. 

.. note:: 

    The area of interest and the preview will take longer to show up when buffering is enabled.

Once all the parameters are selected, the AOI will be previewed in the small map at the bottom of the frame. To validate it, click the :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom in on the AOI and draw it in grey on the map.

.. thumbnail:: ../_images/cookbook/time_series/aoi_table.png
    :title: Select AOI based on EE table
    :group: optical-mosaic-recipe

Draw polygon
""""""""""""

You can use a custom AOI defined by a drawn shape. This shape will be converted into a :code:`ee.FeatureCollection` on the fly. Select :guilabel:`draw a polygon` to use this method.

The pointer in the map will be converted into a :icon:`fa fa-plus`. Click successively on the map to draw a polygon.

Once the geometry is closed, the AOI will be previewed in the small map at the bottom of the frame. To validate it click the :icon:`fa fa-check` :guilabel:`Apply` button. Once validated, the map will zoom on the AOI and draw it in grey on the map.

.. thumbnail:: ../_images/cookbook/time_series/aoi_polygon.png
    :title: Select AOI based on drawn polygon
    :group: optical-mosaic-recipe


Module AOI
^^^^^^^^^^

The module AOI selector is available in some of the SEPAL-contrib modules. To access an app, click the purple wrench :icon:`fa fa-wrench` located on the left side of the SEPAL platform, use the app's dashboard to open a module.

An AOI selector module is composed of two main sections: the available methods (1) and the map (2). Although we will mention all the features and methods available, some of them might not be available in the context of the module you are working on.

.. thumbnail:: ../_images/feature/aoi_selector/module_aoi_overview.png
    :title: Module AOI selector

Available methods
"""""""""""
There are two types of processes that require different AOI inputs and it will depend on the way the module is created and where are the core processes done: directly in a ` SEPAL instance <../../modules/index.html#start-instance-manually>__` or in GEE. Although both interfaces look exactly the same, the inner used data sources will be different for the administrative definitions, see the administrative 



Administrative definitions
"""""""""""""""""""""""""""""""
Similar to the previously mentioned recipe AOI selector, the module AOI uses the `FAO GAUL GEE <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level0>`__ boundaries, but in this case, it allows you to recurse at a maximum second administrative level. The data sources are stored in GEE and can be consulted at:

- Country/province (level 0): countries or provinces at level 0, available at `FAO GAUL GEE level 0 <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level0>`__
- Admin level 1: first administrative level, `FAO GAUL GEE level 1 <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1>`__.
- Admin level 2: second administrative level, `FAO GAUL GEE level 2 <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level2>`__.

Use the :guilabel:`AOI selection method` dropdown list and select the target administrative level, a new dropdown will load up with all the corresponding boundaries to next administrative level that is linked with the base level: i.e. Select `Admin level 2` as method, chose `Colombia` as country, select the `Amazonas` department as the next level, and finally select `Leticia` municipality.


Custom geometries
"""""""""""""""""""""""

When you are looking for a more specific area of interest, the modules have at your disposal the following options:

- Vector file
- Drawn shape
- Point file
- GEE asset


Vector file
~~~~~~~~~~~

Use this option to upload a custom vector file. Select the `Vector file` method in the dropdown list, a file manager widget will be displayed below and will be able to search and select a vector file stored in your SEPAL environment (see `how to exchange files with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html#exchange-files-with-sepal>`_). The below dropdown called `Column` is useful to filter the features of the vector file, the default option is :guilable:`Use all features`, to filter the collection, select a column and a :guilabel:`Value` in the corresponding dropdown, then click the :guilabel:`Select aoi` button. 
     
.. image:: https://raw.githubusercontent.com/dfguerrerom/sepal_mgci/master/doc/img/1_vector_file.PNG
:align: center
:width: 600
:alt: AOI selection
     
.. note:: the available vector formats are: [".shp", ".geojson", ".gpkg", ".kml"]. Once selected, the module will transform its original coordinate system into EPSG:4326.


Drawn shape
~~~~~~~~~~~

Use this option to manually draw geometries in the map. Zoom in at your area of intereset by using the mouse wheel or the :btn:`<fas fa-plus>` and :btn:`<fas fa-minus>` buttons located at the top right corner. Three drawing geometries will be shown up at the top left corner of the map: a :icon:`<fas fa-polygon>` polygon, a :icon:`<fas fa-square>`square and a :icon:`<fas fa-circle>` cricle.

- Polygon: Draw your custom polygon by clicking the vertices of the geometry in the map. To close and finish your geometry, click the first vertex or use the :guilabel:`finish` button. Note that once you select the polygon geometry, three new buttons will be available at the top of the map: :guilabel:`Finish`, :guilabel:`Delete last point` and :guilabel:`Cancel`.

- Rectange: Click the top left corner of the rectangle in the map, that will be the first vertex of the geometry, now, —without clicking—, move the mouse to the opposite corner (bottom left) and click the map, it will close the geometry and the rectangle will be coloured in teal color.

- Circle: Click the center of the circle and then —without stopping clicking— draw the distance (radius), then drop the click, a new blue marker will appear in the map, showing the center of the circle. The geometry won't be drawn in the map until you select the geometry, so do not worry if you can't see the circle at this time, the module will save the geometry in the background.


Point file
~~~~~~~~~~

Use this method to load a single or multiple point dataset. Select :guilabel:`Point file` in the dropdown method list. Four new widgets will appear: a File selector (1) and three dropdown lists: ID (2), Longitude (2) and Latitude (3).

Use the file selector widget to navigate through the SEPAL enviroment and search a :code:`.csv` file containing the coordinates of your points. Make sure the file follows the structure of the following table:

.. csv-table::

   Id, x, y
   1, -74.0, 4.0
   2, -75.0, 5.0

Once the table is loaded, the system will try to automatically identify the :guilabel:`Id`, :guilabel:`Longitude` and :guilabel:`Latitude` columns. When this is not possible, the fields will remain empty and you will have to manually select the columns.

.. note:: note that the columns doesn't have to be named in any specific structure, the only requirement is that your dataset has to be composed of an Id, Longitude and Latitude columns.


GEE asset
~~~~~~~~~

Use this method to load a custom feature collection available as an asset in GEE. Select :guilabel:`GEE asset name` in the dropdown method list. Two widgets will appear by default: an Asset selector (1) and a dropdown list containing the columns of the selected asset (2).

The File selector widget will search for all the :code:`Table` assets (i.e. Feature Collection) stored into your GEE account. You can also copy and paste in the text field a custom third party asset, however, be sure that you have the access permission, otherwise the module won't be able to use that source and an error will be displayed.

Once you have selected a valid asset, the module will query all the available columns in your provided asset and will display them in the column dropdown widget. By default, all the features in the dataset will be selected :code:`Use all features`, however, if you are interested in using an specific geometry, select a column to filter your dataset and a new dropdown will load all the unique values for that specific column, select one.


.. note:: note that this method will only be available when you are using a module that requires a connection to your GEE account. You can check this by navigating through the apps dashboard and noticing the :icon:`fa fa-google` icon at the right side of the drawer.


.. note:: Not all the modules have all the mentioned methods, their availability will depend on the module context, i.e. some apps would require polygons while others points.

Finally, click the :guilabel:`Select AOI` button, if all the inputs are correct you will see a success message, otherwise an indicative error message will be displayed.