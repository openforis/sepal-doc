Damage Proxy Maps
=================

**Damage Proxy Maps based on Coherence Change Detection**

This module provides a fully-automated workflow for the creation of Damage Proxy Maps based on the method of Coherent Change Detection (CCD) with Sentinel-1 SLC data as described by `Tay et al. 2020 <https://www.nature.com/articles/s41597-020-0443-5>`_. 

The output data files consist of the Damage Proxy Map as GeoTiff (*dmp_...tif*) and KMZ (*dmp_...kmz*) file, as well as the raw CCD values in GeoTiff (*CCD_...tif*) and GeoJSON (*CCD_...geojson*) format. 

The files are found within a **newly created folder**. The folder name is based on the name of your AOI and the event date. 

.. warning:: 

    Minimum requirements:

    -   **m16 instance** (16 CPU and 64 GB RAM)
    -   **50 GB of free disk space** 
    
The two steps of the process are explained in the following section:
    
Select an AOI
-------------

Using the provided AOI selector, select an AOI of your choice between the different methods available in the tool. We provide 3 administration descriptions (from level 0 to 2) and 3 custom shapes (drawn directly on the map or ogr compatible files). 

.. figure:: https://raw.githubusercontent.com/sepal-contrib/damage_proxy_maps/main/doc/img/aoi_select.png 
    
    aoi selector
    
Pameters
--------

-   Disaster event date: Pick the date where the disaster event happened.
-   copernicus credentials: Provide your scihub credentials for search and download of the relevant Sentinel-1 scenes. If you do not have an account, go to `Copernicus Scihub <https://scihub.copernicus.eu/>`_ and register.  

Clicking this button will trigger the full workflow. Some of the steps may take a while (e.g. download, processing), so be patient. If you suffer from an instable internet connection, make sure to set the minimum runtime of your instance to 2 hours. Otherwise make sure to keep the connection to the SEPAL website (i.e. do not close browser or browser tab).

.. note::

    If the processing did not finish, you can re-run the module with the same parameters, and the processing will continue from where it stopped.
    
Once the computation is finished the result files will be stored in the :code:`module_results/Damage_proxy_map/<aoi name>_<event date>/` folder. 

.. figure:: https://raw.githubusercontent.com/sepal-contrib/damage_proxy_maps/main/doc/img/complete.png 

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/damage_proxy_maps/release/doc/en.rst
