AOI selection
=============

In most SEPAL recipes, the first mandatory input is the area of interest (AOI), which is used as a boundary to clip the processing and its outputs. This page describes how to select it.

Create a recipe from the orange :btn:`<fa-solid fa-globe>` globe icon on the left side of the SEPAL interface. The AOI panel opens automatically.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_landing.png
    :title: The AOI button and the different ways to select an AOI in SEPAL
    :group: feature_aoi
    :align: center
    :width: 700

The AOI panel, in the lower-right corner of the map, lists the available methods for selecting an AOI:

-   :guilabel:`Select country/province` (administrative boundaries)
-   :guilabel:`Select from EE Table` (GEE tables)
-   :guilabel:`From asset or recipe` (the area covered by a GEE image asset or another SEPAL recipe)
-   :guilabel:`From GeoID` (a location registered with the Open Foris GeoID service)
-   :guilabel:`Draw a polygon` (drawn polygons)

Once you select :btn:`<fa-solid fa-chevron-right> Next`, the map zooms in on the AOI and draws it in grey.

.. tip::

    The selected method is not definitive. You can change it at any stage by selecting the :guilabel:`AOI` button in the lower-right corner, then the title of the AOI panel (marked with :icon:`fa-solid fa-chevron-down`). A list with the available methods will be displayed.

Country/province
""""""""""""""""

You can use a country or a province as an AOI.

These boundaries come from the FAO Global Administrative Unit Layers (GAUL), levels 0 (countries) and 1 (provinces), available on GEE (`level 0 <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level0>`__ and `level 1 <https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1>`__).

.. note::

    -   SEPAL uses its own copy of the GAUL boundaries, in which some country boundaries have been modified. They may therefore differ from the original GAUL dataset.
    -   Country and province names are written without accents or special characters.

To use this method, select :guilabel:`Select country/province`.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_administrative.png
    :title: Select AOI based on administrative boundaries
    :group: feature_aoi
    :align: center
    :width: 700

In the **Country** dropdown list, select a country. Optionally, select a province in the **Province/area** dropdown list. This list is updated on the fly based on the selected country. If no province is selected, the whole country will be considered.

A buffer can be applied to the boundaries by defining its size (km) using the **Buffer** slider (from 0 to 100 km). By default, it is set to :code:`0` and is therefore disabled.

.. note::

    The AOI and the preview will take longer to display when buffering is enabled.

The selected country or province is displayed in the preview map at the bottom of the panel. Select :btn:`<fa-solid fa-chevron-right> Next` to validate it.

EE table
""""""""

You can use the features of a table uploaded to GEE (:code:`ee.FeatureCollection`) as an AOI (see `How to upload custom assets to GEE <../setup/gee.html#upload-files-to-gee>`__).

To use this method, select :guilabel:`Select from EE Table`.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_table.png
    :title: Select AOI based on EE table
    :group: feature_aoi
    :align: center
    :width: 700

In the **EE Table** field, provide a completely qualified GEE asset name (e.g. :code:`projects/gtfp-fao/assets/aoi_ecowas`).

.. attention::

    Make sure you have access to the table you provide. If you do not have access, ask the owner of the table to modify sharing permissions; otherwise, you won't be able to use the dataset.

In **Rows**:

-   Select :guilabel:`Include all` and all geometries associated with the features will be used as an AOI.
-   Select :guilabel:`Filter` and you will be able to select a **Column** and a **Value** to filter the table; the AOI will then be reduced to the filtered features in the table.

A buffer can be applied with the **Buffer** slider, as for the `Country/province`_ method.

When you filter the table, the selected features are displayed in the preview map at the bottom of the panel. Select :btn:`<fa-solid fa-chevron-right> Next` to validate the AOI.

.. note::

    With :guilabel:`Include all`, no preview is displayed. You can still select :btn:`<fa-solid fa-chevron-right> Next` to validate the AOI.

Asset or recipe
"""""""""""""""

You can use the area covered by an existing image as an AOI.

To use this method, select :guilabel:`From asset or recipe`.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_source.png
    :title: Select AOI based on an asset or recipe
    :group: feature_aoi
    :align: center
    :width: 700

Then choose the type of source:

-   :guilabel:`Asset`: provide a GEE image or image collection asset.
-   :guilabel:`Recipe`: select one of your SEPAL recipes that produces an image. By default, only the recipes of the current project are listed; select :guilabel:`ALL` to list the recipes of all your projects.

.. attention::

    Make sure you have access to the asset you provide. If you do not have access, ask the owner of the asset to modify sharing permissions; otherwise, you won't be able to use the dataset.

The area covered by the selected asset or recipe is displayed in the preview map at the bottom of the panel. Select :btn:`<fa-solid fa-chevron-right> Next` to validate it as the AOI.

GeoID
"""""

You can use a GeoID as an AOI.

A GeoID is a permanent identifier for a location – a point or a boundary – registered with the `Open Foris GeoID <https://www.openforis.org/geoid/>`__ service. To find the GeoID of a location, use the `GeoID service <https://geoid.openforis.org/>`__.

To use this method, select :guilabel:`From GeoID`.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_geoid.png
    :title: Select AOI based on a GeoID (a boundary with a 0 m buffer)
    :group: feature_aoi
    :align: center
    :width: 700

In the **GeoID** field, paste a GeoID or a link containing one. SEPAL extracts the GeoID from the text and checks it with the GeoID service.

.. note::

    -   An AOI uses a single GeoID. If the text contains more than one GeoID, an error message will be displayed.
    -   If the GeoID is not registered with the GeoID service, an error message will be displayed and the AOI cannot be validated.
    -   If the GeoID service cannot be reached or is limiting requests, a **Not checked** warning will be displayed; you can still validate the AOI or try again later.

In the **Buffer (m)** field, you can define the buffer in whole metres. Its effect depends on the type of location:

-   **Point**: the AOI is the square reaching the buffer distance from the point in each direction. By default, the buffer is :code:`250` m, which creates a 500 m × 500 m square. The minimum buffer is :code:`10` m.
-   **Boundary**: the AOI extends the buffer distance beyond the boundary. By default, the buffer is :code:`0`, which keeps the boundary as it is.

Leave the field empty to use the default buffer.

When the GeoID service confirms the GeoID, its area is displayed in the preview map at the bottom of the panel. Select :btn:`<fa-solid fa-chevron-right> Next` to validate it.

Polygon
"""""""

You can draw a polygon on the map and use it as an AOI.

To use this method, select :guilabel:`Draw a polygon`.

.. thumbnail:: ../_images/feature/aoi_selector/aoi_polygon.png
    :title: Select AOI based on drawn polygon
    :group: feature_aoi
    :align: center
    :width: 700

The pointer on the map will be converted into a :icon:`fa-solid fa-plus`, and a **Drawing mode: polygon** label will be displayed in the upper-left corner of the map.

Click successively on the map to draw a polygon. To close the polygon, click its first point. Press :kbd:`Esc` to cancel.

When you close the polygon, it is displayed in the preview map at the bottom of the panel. Select :btn:`<fa-solid fa-chevron-right> Next` to validate it.

EE asset bounds
"""""""""""""""

In the **EE Asset** recipe, an additional method is available: :guilabel:`EE asset bounds`, which uses the bounds of the selected GEE asset as the AOI.
