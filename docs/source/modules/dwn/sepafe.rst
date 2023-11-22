SEPAFE
======
*Receive and validate fire alerts from the FIRMS programme by using daily Planet imagery with SEPAFE*

The **SEPAL Planet Active Fires Explorer (SEPAFE)** is a module developed on the SEPAL platform based on the `Fire Information for Resource Management System (FIRMS) <https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/about-firms>`_ and using Planet Scope imagery from Planet Labs.

**SEPAFE** aims to provide users with a quick way to receive and validate fire alerts from the FIRMS programme by using daily Planet imagery.

.. image:: https://raw.githubusercontent.com/dfguerrerom/planet_active_fires_explorer/main/doc/img/sepal_active_fires_home.png

Settings pane
-------------

The **Settings** pane is composed of three tabs: :code:`Planet Imagery`, :code:`Area of Interest` and :code:`Alerts` (all necessary to receive fire alerts).

.. tip:: The **Settings** pane can be open and closed by selecting the **Settings** button (:btn:`<fa-solid fa-bars>`).

Connect your Planet API key
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: This step is optional but highly recommended. While you can receive fire alerts from different satellite sources by simply going through the next tabs, a Planet API key with access to daily imagery will allow you to fully leverage the module. 

- Validate your Planet API key: Provide a valid API key in the input box and select the **Validation** button. The module will check whether the key is valid and messages related to its connection will be displayed within the **Alerts** widget. Once your validation is done, you can open the **Advanced settings** expansion panel and modify its inputs.

.. tip:: Use the **Planet state** bar located in the upper-left corner to receive informative messages about Planet imagery (e.g. problems with the key, number of images loaded).

- Open the **Advanced settings** pane:

  - :code:`Max number of images`: Maximum number of planet images to be displayed at once in each alert.
  - :code:`Search up to 'x' days before`: Number of days before the fire alert date to search for the best image available.
  - :code:`Search up to 'x' days after`: Number of days after the fire alert date to search for the best image available.
  - :code:`Cloud cover threshold`: Maximum cloud cover threshold accepted in the images (based on Planet metadata).

.. image:: https://raw.githubusercontent.com/dfguerrerom/planet_active_fires_explorer/main/doc/gif/planet.gif
   :align: center

Select area of interest (AOI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The module has two options for selecting an AOI to filter alerts.

- **Draw a shape**: When selected, three drawing tools will be displayed in the upper-left corner of the map; you can select a `square`, `circle`, or a `polygon`, and draw them on the map.
- **Select a country**: Enter the name of the country into the search box (or navigate through it by using the scroll bar) and select the desired country. Once the country is selected, it will be displayed in the map view.
  
.. image:: https://raw.githubusercontent.com/dfguerrerom/planet_active_fires_explorer/main/doc/gif/aoi.gif
   
Receive fire alerts
^^^^^^^^^^^^^^^^^^^

- **Recent**: Products to be downloaded are coming from the Moderate Resolution Imaging Spectroradiometer (MODIS) and the Visible Infrared Imaging Radiometer Suite (VIIRS) for the last 24 hours, 28 hours, and the last 7 days.

- **Historical**: For historical products, you will be able to download alerts from 2000 until the last finished year from the MODIS satellite. Select the **Historical** button and filter by the dates.

After selecting the **Get alerts** button, the module will start the download process and clip the alerts to the given AOI. The alerts will be displayed on the map according to a color map for alert confidence – ranging from green to orange to red for the following confidence values:

-    **high, nominal, and low** (for VIIRS) 
-    **>80, >70 < 80, <50** (for MODIS)

.. attention:: Depending on the sensor source and whether your alert request is recent or historical, the download/clip process could take more time. This module is intended to get a quick validation of fire alerts. If you are requesting an area with more than 10000 fire alerts, you will be asked if you want to display all the alerts on the map — which could significantly affect the performance of the tool — or if you want to download them to your desktop/SEPAL environment.

Navigate through alerts
-----------------------

Once the alerts are displayed on the map, you will be able to navigate through each of them by using the :code:`navigation widget`. Use the :code:`next` and :code:`prev` buttons to navigate through the fire alerts; use the :code:`confidence` dropdown list to filter the alerts by confidence (see `What is the detection confidence? <https://earthdata.nasa.gov/faq/firms-faq>`_).

The confidence value was added to help users gauge the quality of individual fire pixels included in the Level 2 fire product. The confidence field should be used with caution; in different parts of the world, it will likely vary in meaning. Nevertheless, some of our end users have found such a field to be useful in excluding false-positive occurrences of fire. They are different for MODIS and VIIRS.

.. image:: https://raw.githubusercontent.com/dfguerrerom/planet_active_fires_explorer/main/doc/gif/alerts_navigation.gif

.. tip:: You can activate and deactivate the fire navigation widget by selecting the **Fires** button (:btn:`<fa-solid fa-fire>`).

.. tip:: Planet parameters can be changed at any time. To refresh results from the current alert, select the **Refresh** button (:btn:`<fa-solid fa-rotate>`).

Manually load planet imagery
----------------------------

Select any point on the map and use the **Refresh** icon (:btn:`<fa-solid fa-rotate>`) to retrieve Planet imagery using the parameters set in **Step 1**; the module will use the current acquisition alert date to search the images. This option is useful when you want to explore surrounding areas close to the alert point, but without alerts to display.

.. attention:: This option requires a valid Planet Level 2 key; otherwise, you will receive an error message in the **Status** bar.
