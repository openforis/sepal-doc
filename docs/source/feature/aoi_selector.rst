AOI selection
=============

In most SEPAL recipes, the first mandatory input is the area of interest (AOI), which is used as a boundary to clip the processing and its outputs.

This page describes how to select the AOI in :btn:`<fa-solid fa-globe>` **Process** recipes. :btn:`<fa-solid fa-wrench>` **Applications** each have their own way of loading an AOI; see the documentation of each application.

Open or create a recipe from the orange :btn:`<fa-solid fa-globe>` globe icon on the left side of the SEPAL interface, then select the :guilabel:`AOI` button in the lower-right corner to open the AOI panel.

There are multiple methods for selecting AOIs in SEPAL process recipes:

-   :guilabel:`Select country/province` (administrative boundaries)
-   :guilabel:`Select from EE Table` (GEE tables)
-   :guilabel:`From asset or recipe` (the area covered by a GEE image asset or another SEPAL recipe)
-   :guilabel:`From GeoID` (a location registered with the Open Foris GeoID service)
-   :guilabel:`Draw a polygon` (drawn polygons)

.. thumbnail:: ../_images/feature/aoi_selector/aoi_landing.png
    :title: The AOI button and the different ways to select an AOI in SEPAL
    :group: feature_aoi
    :align: center
    :width: 700

.. note::

    In the **EE Asset** recipe, an additional method is available: :guilabel:`EE asset bounds`, which uses the bounds of the selected GEE asset as the AOI.

For every method, the AOI is previewed in the small map at the bottom of the panel. To validate it, select the :btn:`<fa-solid fa-chevron-right> Next` button. Once validated, the map will zoom in on the AOI and draw it in grey on the map.

.. tip::

    The selected method is not definitive. You can change it at any stage by selecting the title of the AOI panel (marked with :icon:`fa-solid fa-chevron-down`). A list with the available methods will be displayed.

Country/province
""""""""""""""""

You can select administrative boundaries as AOIs.

These geometries are extracted from the FAO GAUL dataset (levels 0 and 1), available on GEE (`level 0 <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level0>`__ and `level 1 <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1>`__). For more information, see the `FAO GAUL metadata <https://data.apps.fao.org/map/catalog/srv/eng/catalog.search?id=12691#/metadata/9c35ba10-5649-41c8-bdfc-eb78e9e65654>`__.

To use them, select the :guilabel:`Select country/province` method.

.. note::

    Country and province names are written without accents or special characters.

In the **Country** dropdown list, select a country. Optionally, select a province in the **Province/area** dropdown list. This list is updated on the fly based on the selected country. If no province is selected, the whole country will be considered.

A buffer can be applied to the boundaries by defining its size (km) using the **Buffer** slider (from 0 to 100 km). By default, it is set to :code:`0` and is therefore disabled.

.. note::

    The AOI and the preview will take longer to display when buffering is enabled.

Once all parameters are selected, the AOI will be previewed in the small map at the bottom of the panel. To validate it, select the :btn:`<fa-solid fa-chevron-right> Next` button.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_administrative.png
    :title: Select AOI based on administrative boundaries
    :group: feature_aoi
    :align: center
    :width: 700

EE table
""""""""

You can use the features of a GEE table (:code:`ee.FeatureCollection`) as an AOI.

The table needs to be ingested in GEE (see `How to upload custom assets to GEE <../setup/gee.html#upload-files-to-gee>`__).

To use this method, select :guilabel:`Select from EE Table`.

In the **EE Table** field, provide a completely qualified GEE asset name (e.g. :code:`projects/gtfp-fao/assets/aoi_ecowas`).

.. attention::

    Make sure you have access to this asset. If you do not have access, ask the owner of the source to modify sharing permissions; otherwise, you won't be able to use the dataset.

In **Rows**:

-   Select :guilabel:`Include all` and all geometries associated with the features will be used as an AOI.
-   Select :guilabel:`Filter` and you will be able to select a **Column** and a **Value** to filter the table; the AOI will then be reduced to the filtered features in the input asset.

A buffer can be applied to the boundaries by defining its size (km) using the **Buffer** slider (from 0 to 100 km). By default, it is set to :code:`0` and is therefore disabled.

.. note::

    The AOI and the preview will take longer to display when buffering is enabled.

Once all parameters are selected, the AOI will be previewed in the small map at the bottom of the panel. To validate it, select the :btn:`<fa-solid fa-chevron-right> Next` button.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_table.png
    :title: Select AOI based on EE table
    :group: feature_aoi
    :align: center
    :width: 700

Asset or recipe
"""""""""""""""

You can use the area covered by an existing image as an AOI.

To use this method, select :guilabel:`From asset or recipe`, then choose the type of source:

-   :guilabel:`Asset`: provide a GEE image or image collection asset in the **Asset or recipe** field.
-   :guilabel:`Recipe`: select one of your SEPAL recipes that produces an image in the **Asset or recipe** field. By default, only the recipes of the current project are listed; select :guilabel:`ALL` to list the recipes of all your projects.

The AOI will be the area covered by the selected asset or recipe.

.. attention::

    Make sure you have access to the asset. If you do not have access, ask the owner of the source to modify sharing permissions; otherwise, you won't be able to use the dataset.

Once all parameters are selected, the AOI will be previewed in the small map at the bottom of the panel. To validate it, select the :btn:`<fa-solid fa-chevron-right> Next` button.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_source.png
    :title: Select AOI based on an asset or recipe
    :group: feature_aoi
    :align: center
    :width: 700

GeoID
"""""

You can use a location registered with the Open Foris GeoID service as an AOI.

A GeoID is a permanent identifier for a location – a point or a boundary – registered with the `Open Foris GeoID <https://www.openforis.org/geoid/>`__ service. To find the GeoID of a location, use the `GeoID service <https://geoid.openforis.org/>`__.

To use this method, select :guilabel:`From GeoID`.

In the **GeoID** field, paste a GeoID or a link containing one. SEPAL extracts the GeoID from the text and checks it with the GeoID service.

.. note::

    -   An AOI uses a single GeoID. If the text contains more than one GeoID, an error message will be displayed.
    -   If the GeoID is not registered with the GeoID service, an error message will be displayed and the AOI cannot be validated.
    -   If the GeoID service cannot be reached or is limiting requests, a **Not checked** warning will be displayed; you can still validate the AOI or try again later.

In the **Buffer (m)** field, you can define the buffer in whole metres. Its effect depends on the type of location:

-   **Point**: the AOI is the square reaching the buffer distance from the point in each direction. By default, the buffer is :code:`250` m, which creates a 500 m × 500 m square. The minimum buffer is :code:`10` m.
-   **Boundary**: the AOI extends the buffer distance beyond the boundary. By default, the buffer is :code:`0`, which keeps the boundary as it is.

Leave the field empty to use the default buffer.

Once the GeoID is checked, the AOI will be previewed in the small map at the bottom of the panel. To validate it, select the :btn:`<fa-solid fa-chevron-right> Next` button.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_geoid.png
    :title: Select AOI based on a GeoID (a boundary with a 0 m buffer)
    :group: feature_aoi
    :align: center
    :width: 700

Polygon
"""""""

You can use a custom AOI defined by a drawn shape, which will be converted into a :code:`ee.FeatureCollection` on the fly.

To use this method, select :guilabel:`Draw a polygon`.

The pointer on the map will be converted into a :icon:`fa-solid fa-plus`, and a **Drawing mode: polygon** label will be displayed in the upper-left corner of the map.

Click successively on the map to draw a polygon.

Once the shape is closed, the AOI will be previewed in the small map at the bottom of the panel. To validate it, select the :btn:`<fa-solid fa-chevron-right> Next` button.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_polygon.png
    :title: Select AOI based on drawn polygon
    :group: feature_aoi
    :align: center
    :width: 700
