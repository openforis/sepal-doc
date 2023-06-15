SEPAL Planet Active Fires Explorer
==================================

The SEPAL Planet Active Fires Explorer (SEPAFE) is a module developed on the SEPAL platform based on the `Fire Information for Resource Management System (FIRMS) <https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/about-firms>`_ using Planet Scope imagery from Planet Labs.

SEPAFE aims to provide users with a quick way to receive and validate fire alerts from the FIRMS programme by using daily Planet imagery.

.. image:: https://raw.githubusercontent.com/dfguerrerom/planet_active_fires_explorer/main/doc/img/sepal_active_fires_home.png


Settings panel
--------------

The **Settings** panel is composed of three tabs, including :code:`Planet imagery`, :code:`Area of interest` and :code:`Alerts` (each of them is necessary to receive fire alerts).

.. tip:: The **Settings** panel can be opened or closed by selecting the :btn:`<fa-solid fa-bars>` button.

Connect your Planet API key
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: This step is optional but highly recommended. Although you can go through the next tabs and receive fire alerts from the different satellite sources, to leverage the potential of the module, you will need a Planet API key with access to daily imagery. 

- Validate your Planet API key: provide a valid API key in the input box and click over the validation button, the module will check whether the key is valid or not, and the messages of its connection will be displayed directly in the **Alerts** widget. Once your validation is done, you can open the **Advanced settings** panel and modify its inputs. 

.. tip:: Use the **Planet status** bar located in the upper-left corner to receive useful messages related to Planet imagery, such as problems with the key or number of images loaded.

- Open the **Advanced settings** panel, which displays:

  - :code:`Max number of images`: The maximum number of Planet images to be simulatenously displayed in each alert.
  - :code:`Search up to 'x' days before`: The number of days before the fire alert date to search for the best image available.
  - :code:`Search up to 'x' days after`: The number of days after the fire alert date to search for the best image available.
  - :code:`Cloud cover threshold`: The maximum cloud cover threshold accepted in the images (based on Planet metadata).
    
.. image:: https://raw.githubusercontent.com/dfguerrerom/planet_active_fires_explorer/main/doc/gif/planet.gif
   :align: center

Select area of interest (AOI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The module has two options to select an AOI to filter alerts.

- Draw a shape: When this option is selected, three drawing tools will be displayed in the upper-left corner of the map (you can select `square`, `circle`, or `polygon`, and draw them on the map).
- Select a country: Enter the name of the country directly into the search box, or navigate through it by using the scroll bar to select the desired country. Once the country is selected, it will be displayed in the map view.
  
.. image:: https://raw.githubusercontent.com/dfguerrerom/planet_active_fires_explorer/main/doc/gif/aoi.gif
   
Receive fire alerts
^^^^^^^^^^^^^^^^^^^

- Recent: The products to be downloaded come from the Moderate Resolution Imaging Spectroradiometer (MODIS) and the Visible Infrared Imaging Radiometer Suite (VIIRS) within the last 24 hours, 28 hours, and 7 days.

- Historical: For historical products, you will be able to download alerts from 2000 until the most recent completed year from the MODIS satellite. Use the historical button to filter by date.

After selecting the **Get alerts** button, the module will start the download process and clip the alerts to the given AOI. The alerts will be displayed on the map according to a color map for alert confidence, ranging from green, orange, and red, for the confidence values high, nominal and low (for VIIRS) and >80, >70 < 80, <50 for MODIS.

.. attention:: Depending on the sensor source and whether your alert request is recent or historical, the download/clip process could take more time. This module is intended to receive quick validation of fire alerts. If you are requesting an area with more than 10000 fire alerts, you will be asked if you want to display all of the alerts on the map (which could highly affect the performance of the tool) or if you want to download them to your desktop or SEPAL environment.

Navigate through alerts
-----------------------

Once the alerts are being displayed on the map, you will be able to navigate through each of them by using the :code:`Navigation widget`. Use the :code:`Next` and :code:`Prev` buttons to navigate through the fire alerts; use the :code:`Confidence` dropdown menu to filter the alerts by confidence (for more information, see `What is the detection confidence? <https://earthdata.nasa.gov/faq/firms-faq>`_).

The confidence value was added to help users gauge the quality of individual fire pixels included in the Level 2 fire product. The confidence field should be used with caution; it will likely vary in meaning in different parts of the world. Nevertheless, some of our end users have found such a field to be useful in excluding false-positive occurrences of fire. They are different for MODIS and VIIRS.

.. image:: https://raw.githubusercontent.com/dfguerrerom/planet_active_fires_explorer/main/doc/gif/alerts_navigation.gif

.. tip:: You can activate or deactivate the **Fire navigation** widget by selecting the :btn:`<fa-solid fa-fire>` button.

.. tip:: Planet parameters can be changed at any time. To refresh the results from the current alert, select the :btn:`<fa-solid fa-rotate>` icon

Manually load planet imagery
----------------------------

Select any point on the map and use the refresh icon :btn:`<fa-solid fa-rotate>` to retrieve Planet imagery using the parameters set in Step 1. The module will use the current acquisition alert date to search images. This option is useful when you want to explore surrounding areas close to the alert point but without alerts to display.

.. attention:: To use this option, you will need a valid Planet Level 2 key. Otherwise, you will get an error message displayed in the status bar.

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/planet_active_fires_explorer/master/doc/en.rst
