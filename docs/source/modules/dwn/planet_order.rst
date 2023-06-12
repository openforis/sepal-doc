Planet order
============

This dasboard application based on the `sepal-ui <https://sepal-ui.readthedocs.io/en/latest/>`_ framework, provide the user with a friendly interface to explore and download Planet Labs images.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/demo.png
    :group: planet-order

.. warning::

    in order to start this module, you need to have register on the planet NICFI contract (`Register NICFI PlanetLab <https://docs.sepal.io/en/latest/setup/register.html#sign-up-for-planet-lab-data>`_) and connect your GEE account to SEPAL (`connect GEE to SEPAL <https://docs.sepal.io/en/latest/setup/gee.html#connection-between-gee-and-sepal>`_).


In the landing page of our module at the bottom left of the window, you'll find 3 buttons:

-   The :btn:`<fa-solid fa-file-code>` will open in a new tab the GitHub repository that is used to create this module. our code is open-source and distributed under the MIT License.
-   The :btn:`<fa-solid fa-book-open>` button will lead you to the wiki page
-   The :btn:`<fa-solid fa-bug>` will open in a new tab the isse tracker of our GitHub repository. You can write here if you experience bugs or if you have any feature request. Our maintainer will answer as fast as possible.

Parameters
----------

In the lower right corner, 2 tabs are available:

-   :btn:`<fa-solid fa-map-marker-alt>` the Area of interest selection PlanetLab
-   :btn:`<fa-solid fa-globe>` The planet authentification PlanetLab

In the top left corner, 3 other tbas will allow you ton interact with the data:

-   :btn:`<fa-solid fa-magnifying-glass>` the Planet order manager
-   :btn:`<fa-solid fa-palette>` The color management
-   :btn:`<fa-solid fa-cloud-arrow-down>` the Download panel

Select an AOI
-------------

The application use the same AOI selector that you will find in lots of other application in SEPAL. Go to the `Module AOI section <https://docs.sepal.io/en/latest/feature/aoi_selector.html#module-aoi>`__ for more information.

Planet Lab authentication
-------------------------

To authenticate the user, feel the form in the second tab with either your credentials or a planet API key. you can find it in your Planet profile page in the settings section. Once the values are set click on :btn:`validate`. If your Planet credentials are valid, the :btn:`NICFI` button should turn green. You can now select a mosaic in the provided list.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/planet_auth.png
    :group: planet-order

.. note::

    If you're not yet register to Planet please follow our `documentation <https://docs.sepal.io/en/latest/setup/register.html#sign-up-for-planet-lab-data>`_

Manage orders
-------------

In the top-left section, the planet order selector is now activated. You can select any mosaic in the mosaic dropdown on top of the map. using the :btn:`next` or :btn:`prev` button will jump to the next/prev mosaic in the list (they are in chronological order).

Once a mosaic is selected the module will display the basemaps on the map.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/mosaic_select.png
    :group: planet-order

Manage color combination
------------------------

Click on :btn:`<fa-solid fa-palette>` on the top-left side of the map. This button will expand and show the different color combo available:

-   Red-Green-Blue (RGB)
-   Color-infrared (CIR)
-   Normalized Difference Vegetation Index (NDVI)
-   Normalized Difference Water Index (NDWI)
-   Visual Atmosphere Resistance Index (VARI)
-   Modified Soil-adjusted Vegetation Index (MSAVI2)
-   Modified Triangular Vegetation Index (MTVI2)
-   Triangular Greenness Index (TGI)

Selecting one will update the displayed basemap.

.. note::

    More information about the band combination can be found on `Planet documentation page <https://developers.planet.com/docs/basemaps/tile-services/indices/>`__.

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

Download Data
-------------

Once you are satisfied with your mosaic selection, you can click on the :btn:`<fa-solid fa-cloud-arrow-down>` button. This will launch the downloading process of your images from Planet server to your folders.

The images will be stored in the following folder : :code:`~/module_results/planet-order/<aoi_name>/<mosaic_name>/`.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/planet-order/master/doc/img/download.png
    :group: planet-order

.. tip::

    In the parent folder (:code:`/home/<sepalID>/module_results/planet-order/<aoi_name>/`) you will find a .geojson file of the planet grid. This can be useful for other tools.

.. note::

    If the requested image is not available (the grid point to water area, the image was to cloudy so filtered by Planet, you don't have the rights to download it.. etc) the image will fail.
    If the image already exist in your folder it will be skipped. This behaviour allow you to restart a process if your SEPAL conection crashed without restarting all the downloads.



.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/planet-order/release/doc/en.rst
