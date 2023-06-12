Deforestation alert analysis
============================

.. warning::

    To use this module, you must at least register to the NICFI PlanetLab program and link your GEE account to it. More information can be found at :doc:`../../setup/nicfi`.


Set up
------

From the SEPAL app dashboard (purple :icon:`fa-solid fa-wrench` on the left side), search for and click on **deforestation alert analysis**.

.. note::

    The launching process can take several minutes

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/landing.png
    :title: the interface displayed to the end user
    :group: alert-module

The application should launch itself as a map displaying the world. At the bottom-left side you will find 3 special buttons to open useful links:

-   :btn:`<fa-solid fa-book-open>` the link to the documentation of the module
-   :btn:`<fa-solid fa-bug>` the link to open a new issue in the github repository
-   :btn:`<fa-solid fa-file-code>` the link to the source code of the application

Clicking on them will open the link in a new webpage.


In the bottom right corner of the map. 3 buttons will help the user navigate through the different widgets of the application:


-   :btn:`<fa-solid fa-location-dot>`: the widget to select the AOI (Area of interest)
-   :btn:`<fa-solid fa-triangle-exclamation>`: the widget to select the alerts and filter them
-   :btn:`<fa-solid fa-globe>`: the widget to select Planet parameters

In the top left corner there is :btn:`<fa-solid fa-info>` button to open the metatada interface. More information in the next sections of this document.

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/widgets.png
    :title: the different areas of interaction of the module
    :group: alert-module

Parameters
----------

The settings need to be fully validated to load the alerts on the map. It has 3 sections that need to be filled in order:

-   **AOI**
-   **Alert**
-   **Planet** (optional)

Area of interest
^^^^^^^^^^^^^^^^

The Area Of Interest (AOI) is set using the same  interface as in other applications. You can read :doc:`../../feature/aoi_selector` for more information.

In this step the user will be able to select any type of AOI method. When validated, the AOI will be displayed in gold on the map.

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/aoi.png
    :title: The selection of an AOI.
    :group: alert-module

Alert
^^^^^

The user then needs to select the alert system to use. Various drivers are available in the module and the documentation will reflects any changes or addition made by the SEPAL team.

Follow this process:

-   Select a driver in the dropdown list. The module will show in blue the area covered by the driver. If you don't see a background color change, your AOI is not covered
-   Then select a date range. It can be xx days in the past using the "recent" mode or any time in the past using the "historical" mode.
-   using the slider, you can filter the minimal size of the alerts from 0 to 100 ha. 0 corresponding to no filter at all.

.. note::

    Some Alert drivers are already filtered by dates, the date selector is thus not displayed


.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/glad_l_settings.png
    :width: 24%
    :title: when selecting the GLAD-L widget
    :group: alert-module

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/radd_settings.png
    :width: 24%
    :title: when selecting the RADD widget
    :group: alert-module

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/nrt_settings.png
    :width: 24%
    :title: when selecting the NRT widget
    :group: alert-module

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/glad_s_settings.png
    :width: 24%
    :title: when selecting the GLAD-S widget
    :group: alert-module

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/cusum_settings.png
    :width: 24%
    :title: when selecting the CUSUM widget
    :group: alert-module

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/jica_settings.png
    :width: 24%
    :title: when selecting the SINGLE-DATE widget
    :group: alert-module

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/recover_settings.png
    :width: 24%
    :title: when selecting The RECOVER widget
    :group: alert-module

GLAD-L
######

By selecting this alert system, you will use the GLAD alerts based on the Landsatsatellites.

    Since the opening of the Landsat archive in 2008, medium spatial resolution data have been available for use in alert-based applications.  Since 2013, two Landsat sensors, the Enhanced Thematic Mapper Plus (ETM+) onboard Landsat 7, and the Operational Land Imager (OLI) onboard Landsat 8, have been systematically acquiring global multi-spectral observations at a 30m spatial resolution.  The orbits of the two spacecraft are coordinated to enable potential 8-day repeat coverage globally.   Given this cadence, the use of Landsat as a near-real time source of land change information is possible. The data displayed and made available here quantify forest disturbance events for the tropics using ETM+ and OLI data as an input.  Daily updates are made for areas where quality land observations are acquired.  We define forest cover as 5m tall trees with a canopy closure exceeding 30%.  An alert is defined as any Landsat pixel that experiences a canopy loss in excess of 50% cover.

More information on these alerts can be found on the `GLAD forest alert page <https://glad.umd.edu/dataset/glad-forest-alerts>`__.

RADD
####

.. note::

    RADD alerts only cover the tropical part of the Americas and Africa. More information can be found in their documenation.

Selecting this alert system, you will use the RADD alerts:

    Sentinel-1’s cloud-penetrating radar provides gap-free observations for the tropics consistently every 6 to 12 days. In the densely cloud covered tropics, this represents a major advantage for the rapid detection of small-scale forest disturbances such as subsistence agriculture and selective logging. The RADD (RAdar for Detecting Deforestation) alerts contribute to the World Resources Institute’s Global Forest Watch initiative in providing timely and accurate information to support a wide range of stakeholders in sustainable forest management and law enforcement activities against illegal deforestation. The RADD alerts are implemented in Google Earth Engine. RADD alerts are available openly via Google Earth Engine, the Global Forest Watch platform, SEPAL.io and EarthMap.org.

More information on these alerts can be found on the `Wageningen university portal <https://www.wur.nl/en/Research-Results/Chair-groups/Environmental-Sciences/Laboratory-of-Geo-information-Science-and-Remote-Sensing/Research/Sensing-measuring/RADD-Forest-Disturbance-Alert.htm>`__.

NRT
###

.. danger::

    This functionality will remain experimental until the SEPAL team removes the "beta" status on the near real time alert creation recipe.

Selecting this alert system, the user will use the near real time alerts provided by the SEPAL recipe on a specific AOI and for specific dates.
You only needs to provide access to the alert asset.

.. note::

    The footprint of the alert is only displayed once the asset is selected.

GLAD-S
######

.. warning::

    When publishing this documentation (2022-04-26) only the north part of South America is covered by the alert system. Open the following `link <https://code.earthengine.google.com/3b5238d7558dbafec5072838f1bac1e9?hideCode=true>`__ to see the area in the GEE code editor.

By selecting this alert system, you will use the GLAD alerts based on the Sentinel 2 satellites.

    Loss of primary forest is mapped in near-real time at 10m resolution using Sentinel-2 multispectral data. Cloud, shadow, water are detected in each new Sentinel-2 image and a forest loss algorithm is applied to all remaining clear land observations. The algorithm relies on the spectral data in each new image in combination with spectral metrics from a baseline period of the previous two years. Confidence is built through repeated loss observations in the consequent images.

CUSUM
#####

.. note::

    this will be using the :code:`.tif` output of :doc:`cusum`.

Once you've run the CUSUM module, you'll obtain a 3 bands :code:`.tif` file. Ingest this file in Google Earth Engine using the `code editor interface <https://code.earthengine.google.com/>`__. Once the map is available in your assets you can use it in the module. If you don't find the asset in the list, click on the :icon:`fa-solid fa-arrows-rotate` icon to reload your asset list.

.. note::

    The footprint of the alert is only displayed once the asset is selected.

SINGLE-DATE
###########

For this alert driver, the AOI parameter is ignored and all the alerts available in the file be loaded.

Any alert system including a vector file of geometries and metadata. If included the label will be infered from the ``id`` and the date of the alert need to be set by the user. By default every alert will be using this one so Planet data will not point straight to the correct images.

The source needs to be a geojson file using the following format:

.. code-block:: json

    {
	    "type": "FeatureCollection",
	    "features": [{
		    "geometry": {
			    "coordinates": ["<feature_coordinates>"],
			    "geodesic": false,
			    "type": "Polygon"
		    },
		    "id": "+605258+71623",
		    "properties": {
                "prop1": 0.0,
                "prop2": 0.0
		    },
		    "type": "Feature"
	    },
        {"<other_feature_complete_description>"}
	    ]
    }

.. note::

    Vietnamese forest department is using a specific alert system that works well. It generates a geojson file every 10 days. This system have been developped in partnership with JICA and you can check the GEE application `here (vietnamese) <http://canhbaomatrung.kiemlam.org.vn>`__.


RECOVER
#######

For this alert driver, the AOI parameter is ignored and all the alerts available in the file be loaded.

The user can save it's work by exporting the already interpreted alerts in :code:`.gpkg` forma`. By selecting this format, you will be able to recover your previous analysis and continue the interpretation process.

JJ-FAST
#######

By selecting this alert system, you will use the JJ-FAST alerts based on ALOS PALSAR data.

    The JICA-JAXA Forest Early Warning System in the Tropics (JJ-FAST) can detect deforestation sites with size larger than 2 hectares (Ver. 3.0, as of June 2020). Employing the microwave remote sensing technology, detections can be made even under the thick cloud cover which is characteristic for tropical regions especially during the rainy seasons. The system detects deforestation by means of L-band (1.25 MHz) Synthetic Aperture Radar (SAR) data acquired by the PALSAR-2 sensor aboard JAXA’s Advanced Land Observing Satellite 2 (ALOS-2) and provides the positioning information of detected sites to users free of charge via its web service.

    With frequent updates for the entire tropical forest belt, approximately every 1.5 months, JJ-FAST aims to function as an effective deterrent against illegal deforestation activities when it is utilized for forest monitoring in the target countries.

    Government forest authorities of tropical countries with large forest inventories are expected to be the main users of JJ-FAST. Since the polygons of detected deforestations cannot only be conveniently viewed online, but also downloaded for further GIS analysis, local authorities are able to effectively identify illegal activities by comparing JJ-FAST detections with available national land use maps and/or concession maps.


Validation
##########

Once everything is set, the user can click on :btn:`select alerts` and the module will start downloading the information from google earth engine. the module will tile the AOI in smaller chunks to avoid GEE limitation, if you use a big area downloading can take up to 15 min. The alerts are displayed as shapes in red on the map and the settings panel will close automatically. If alerts are found in your AOI.

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/alerts.png
    :title: The selected alerts displayed on the map.
    :group: alert-module

Metadata
--------

Click on :btn:`<fa-solid fa-info>` to show the metadata panel. This panel will allow you to validate the alerts identified by the driver using Planet VHR (Very High Resolution) imagery. All information about the current alert will be displayed in this table:

-   alert ID: the Id of the alert
-   geometry edition: a button to trigger geometry edition for one single alert
-   date: the identified date of the deforestation event
-   surface: the deforested surface in hectares
-   coordinates: the coordinates of the center of the alert
-   review: the visual evaluation performed by the user
-   comments: some extra comments on the alert

The next sections will cover the editable fields of this table.

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/metadata.png
    :title: the metadata of the alerts
    :group: alert-module

alert ID
^^^^^^^^

on the top you will find the list of alerts ordered by size. To acess them the user can either click on the blue arrows or click on the carret to select one in the dropdown menu. Once an alert is selected (represented now in orange on the map), the Planet panel will open itself on the top right corner of the map and the information of the alert will be displayed.

.. tip::

    To jump from one alert to another, the user can also directly click on the map, the information will be loaded automatically.

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/select_alert.png
    :title: select an alert in the list to hydrate the alert table
    :group: alert-module

Geometry edition
^^^^^^^^^^^^^^^^

Some drivers perform automatic analysis and sometimes the geometry of the alerts poorly represent what you see on the VHR imagery. Using this module you can redifine the geometry before exporting your results to perfectly fit the deforested area.

-   Click on :btn:`edit geometry`. It will release the edition interface (1).
-   Click on :btn:`<fa-solid fa-pen-to-square>` to start edition and move the white square to add or remove vertices.
-   Once done click on :btn:`save` to exit the edition mode

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/edit.png
    :title: the edition interface
    :group: alert-module

alternatively:

-   Click on :btn:`<fa-solid fa-trash>` to start the deletion interface
-   Click on :btn:`clear all` to remove the edited geometry. The geometry will be returned to it's original state before any edition was done.

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/clear.png
    :title: the reset process to cancel any edition
    :group: alert-module

Once the edition is completed click again on the button in the metada panel to stop edition: :btn:`finish edition`.

Date
^^^^

If the selected driver embeds the dates of the alerts, this field will be prefield with a meaningful date of deforestation event, if not we take the date found in the file title.

Once the deforestation event is identified you might want to update the date value to reflect what you see on the VHR imagery. Click in the field to use the datepicker.

Review
^^^^^^

By default all alerts are set to :code:`unset`. After interpreting the Planet imagery, change the value of the radio "review" from:

- :code:`yes`: the alert is valid as well as the date
- :code:`no`: the alert is not valid (no deforestation event)
- :code:`unset`: no review has been performed

Comments
^^^^^^^^

You can fill this comment section with any aditional information you might want. There is no size limits.

Export
^^^^^^

At the very bottom of the metadata panel 3 exportation button can be found. Each one will export the alerts and their reviews in a specific format.

to kml
######

Export the alerts as a :code:`.kml` file readable with Google Earth. Each alert will use its ID as label. You can export them at the beginning of the review if you want to use Google Earth in the review process.

to gpkg
#######

Export the alerts as a :code:`.gpkg` file readable by any GIS software. It will embed the geometry and all the properties associated with each feature/alert (including the original geometry). This file can be used to save progresses and reused as an input of the process.

to csv
######

Export the alerts as a :code:`.csv` file. Each alert properties are kept and the file represents each feature using the coordinates (lattitude/longitude) of the center of each alert.

Planet imagery
--------------

To interprete the validity of the alert, this module is based on the Planet NICFI imagery.

Parameters
^^^^^^^^^^

.. note::

    this panel is fully optional. If nothing is set, the module will use Planet NICFI level 1 data (monthly mosaics). If you have a NICFI level 2 access, providing your API key will grant you access to daily imagery.

click on :btn:`<fa-solid fa-globe>` to access the`planet API interface. In this panel you can connect to your Planet Profile using either your credentials or your password.

-   Select the credential mode between "credentials" and "API key"
-   Set and validate your credentials

If the icon is green then you are connected.

Click on :btn:`NICFI` to see the details of the substrictions available with your profile. If the level 2 data are accecible you will be granted access to daily imagery for reviewing steps.

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/level0.png
    :width: 32%
    :title: the level 0 subsciption to Planet imagery
    :group: alert-module

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/level1.png
    :width: 32%
    :title: the level 1 subsciption to Planet imagery
    :group: alert-module

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/level2.png
    :width: 32%
    :title: the level 2 subsciption to Planet imagery
    :group: alert-module

Advance parameters
^^^^^^^^^^^^^^^^^^

Once validated you'll be able to modify the Planet advance parameters. These parameters are used to request images to Planet, some default parameters have been set but changes may improve the readability of the image.

-   **number of images**: the max number of images to display on the map, default to 6
-   **day before**: number of previous day the interface can search for images. useful when lot of cloud coverage, default to 1
-   **day after**: number of previous day the interface can search for images. useful when lot of cloud coverage, default to 1
-   **cloud coverage**: the requested maximal cloud coverage of the images, default to 20%

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/planet_settings.png
    :title: The planet settings
    :group: alert-module

Level 1 (monthly)
^^^^^^^^^^^^^^^^^

Level 1 data are monthly mosaics. When a alert is clicked, the module will load the closest month from the observation date. the user can then use the Planet navigator to change the displayed image.
Click on the :btn:`<fa-solid fa-palette>` to change the color of the images from CIR to RGB. The user can select the monthly mosaic directly from the dropdown menu or use the navigation buttons. :btn:`<fa-solid fa-chevron-left>` (res. :btn:`<fa-solid fa-chevron-right>`) will move from one mont in the past (res. in the future). The :btn:`<fa-solid fa-circle>` will set back on the closest date from the observation date.

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/planet_monthly_rgb.png
    :width: 49%
    :title: the planet monthly mosaic displayed in rgb
    :group: alert-module

Level 2 (daily)
^^^^^^^^^^^^^^^

.. warning::

    This option is only available for users that have a NICFI level 2 access.

Level 2 data are daily imagery. When an alert is clicked, the module will load the closest day from the observation date and display images using the advanced parameters provided by the user.

.. tip::

    Multiple images are displayed at once so don't hesitate to play with the layer control to hide and show different scenes.

Thus user can navigate through the images using the buttons in the Planet navigator. Click on :btn:`<fa-solid fa-chevron-left>` (res. :btn:`<fa-solid fa-chevron-right>`) to move one day in the past (res. one day in the future). Click on :btn:`<fa-solid fa-chevron-left>` :btn:`<fa-solid fa-chevron-left>` (res. :btn:`fa-solid fa-chevron-right` :btn:`<fa-solid fa-chevron-right>`) to move one month in the past (res. one month in the future). The :btn:`<fa-solid fa-circle>` will set back on the closest date from the observation date.

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/alert_module/master/doc/img/planet_daily.png
    :title: the planet daily mosaic displayed in cir
    :group: alert-module

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/alert_module/release/doc/en.rst
