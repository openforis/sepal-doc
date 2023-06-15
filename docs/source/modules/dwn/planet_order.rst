Planet order
============

This dasboard application, based on the `SEPAL-UI <https://sepal-ui.readthedocs.io/en/latest/>`_ framework, provides users with an interface to explore and download Planet Lab images.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/demo.png
    :group: planet-order

.. attention::

    To start this module, you need to (`sign up for NICFI <https://docs.sepal.io/en/latest/setup/nicfi.html#access-nicfi-through-gee>`_) and (`connect your GEE account to SEPAL <https://docs.sepal.io/en/latest/setup/gee.html#connection-between-gee-and-sepal>`_).

On the landing page of our module, on the lower left of the window, you will find three buttons:

-   :btn:`<fa-solid fa-file-code>`: Opens the GitHub repository that is used to create this module in a new tab (our code is open-source and distributed under the MIT license).
-   :btn:`<fa-solid fa-book-open>`: Leads to the wiki page.
-   :btn:`<fa-solid fa-bug>`: Opens the isse tracker of our GitHub repository in a new tab (you can write here if you experience bugs or if you have any feature requests; the SEPAL team will answer as quickly as possible).

Parameters
----------

In the lower-right corner, two tabs are available:

-   :btn:`<fa-solid fa-map-marker-alt>`: Planet Lab area of interest (AOI) selection 
-   :btn:`<fa-solid fa-globe>`: Planet Lab authentification

In the upper-left corner, three other tabs will allow you to interact with the data:

-   :btn:`<fa-solid fa-magnifying-glass>`: the Planet order manager
-   :btn:`<fa-solid fa-palette>`: color management
-   :btn:`<fa-solid fa-cloud-arrow-down>`: download panel

Select an AOI
-------------

The application uses the same AOI selector that you will find in many other SEPAL applications (see the `Module AOI section <https://docs.sepal.io/en/latest/feature/aoi_selector.html#module-aoi>`__ for more information).

Planet Lab authentication
-------------------------

To authenticate the user, complete the form in the second tab with either your credentials or a Planet API key, which you can find in the settings section in your Planet profile page. Once the values are set, select :btn:`Validate`. If your Planet credentials are valid, the :btn:`NICFI` button should turn green. You can now select a mosaic from the provided list.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/planet_auth.png
    :group: planet-order

.. note::

    If you're not yet registered to Planet, please follow `the documentation for signing up for Planet Lab data <https://docs.sepal.io/en/latest/setup/register.html#sign-up-for-planet-lab-data>`_.

Manage orders
-------------

In the upper-left section, the Planet order selector is now activated. You can select any mosaic in the mosaic dropdown list above the map. Using the :btn:`next` or :btn:`prev` button to go to the next or previous mosaic in the list (they are in chronological order).

Once a mosaic is selected, the module will display the basemaps on the map.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select.png
    :group: planet-order

Manage color combination
------------------------

Select :btn:`<fa-solid fa-palette>` on the upper-left side of the map, which will show the different color combinations available, including:

-   Red-green-blue (RGB)
-   Color-infrared (CIR)
-   Normalized difference vegetation index (NDVI)
-   Normalized difference water index (NDWI)
-   Visual atmosphere resistance index (VARI)
-   Modified soil-adjusted vegetation index (MSAVI2)
-   Modified triangular vegetation index (MTVI2)
-   Triangular greenness index (TGI)

Selecting one will update the displayed basemap.

.. note::

    More information about band combination can be found on `the Planet documentation page <https://developers.planet.com/docs/basemaps/tile-services/indices/>`__.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_rgb.png
    :group: planet-order
    :width: 32%

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_cir.png
    :group: planet-order
    :width: 32%

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_ndvi.png
    :group: planet-order
    :width: 32%

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_ndwi.png
    :group: planet-order
    :width: 32%

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_vari.png
    :group: planet-order
    :width: 32%

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_msavi2.png
    :group: planet-order
    :width: 32%

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_mtvi2.png
    :group: planet-order
    :width: 32%

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select_tgi.png
    :group: planet-order
    :width: 32%

Download data
-------------

Once you are satisfied with your mosaic selection, you can select the :btn:`<fa-solid fa-cloud-arrow-down>` button, which will launch the downloading process of your images from the Planet server to your folders.

The images will be stored in the following folder: :code:`~/module_results/planet-order/<aoi_name>/<mosaic_name>/`.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/download.png
    :group: planet-order

.. tip::

    In the parent folder (:code:`/home/<sepalID>/module_results/planet-order/<aoi_name>/`), you will find a .geojson file of the Planet grid, which can be useful for other tools.

.. note::

    If the requested image is not available (e.g. the grid points to water area, the image was too cloudy and filtered by Planet, you don't have the rights to download it, etc.) the image will fail.

    If the image already exists in your folder, it will be skipped. This behaviour allows you to restart a process if your SEPAL connection crashes without needing to restart all the downloads.

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/planet-order/release/doc/en.rst
