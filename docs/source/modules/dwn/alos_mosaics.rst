ALOS Kyoto & Carbon Mosaics by JAXA
===================================

This module was adapted to the SEPAL environment from `this script by Vollrath <https://code.earthengine.google.com/3784ea8db0b93bcaa41d1a3ada0c055e>`_.

Designed on top of the interactive framework `sepal_ui <https://github.com/12rambau/sepal_ui>`_, this module allows users to extract ALOS K&C mosaics.

Necessary inputs include:

-    an area of interest (AOI)
-    a year
-    select filters

The user will be able to display the mosaic in an interactive map and export it as a Google Earth Engine (GEE) asset and/or SEPAL .tif file.

The three-step process is described in the sections below, as well as presented in the following video tutorial. 

.. youtube:: Asc8Nz0B1DI

Select an AOI
-------------

Using the provided **AOI selector**, select an AOI of your choice between the different methods available in the tool. We provide three administrative descriptors (from level 0 to 2) and three custom shapes (drawn directly on the map, asset or shapefile).

.. figure:: https://raw.githubusercontent.com/lecrabe/alos_mosaics/main/doc/img/aoi_select.png
    
    AOI selector
    
.. note::

    If a custom AOI from a shape or drawing is selected, you will be able to use it directly. The upload to GEE will be launched in the background.

Process mosaic 
--------------

In the **Process** tile, set the different parameters of your mosaic: 

-   **Year**: the year of interest 
-   **Speckle filter**: the speckle filter to use during the process    
    -   no filter
    -   refined lee: speckle noise removal technique based on the Lee Filter (for more information, see `A.S. Yommy et al.<https://doi.org/10.1109/IHMSC.2015.236>`_
    -   Quegan filter: See `Quegan et al. <https://doi.org/10.1109/36.964973>`_
-   **Shadow masking**: activate or deactivate shadow masking
-   **Db**: whether or not to scale the output to Db

After setting your parameters, select the button. The dataset will be automatically sent to the **Vizualization** tile.

.. figure:: https://raw.githubusercontent.com/lecrabe/alos_mosaics/main/doc/img/parameters.png

    Dataset parameters 

Display dataset
---------------

The dataset is automatically displayed on the interactive map, allowing you to zoom in and out.

Choose from three diplay options:

-   Backscatter RGB (HH, HV, HH/HV power ratio)
-   Radar Forest Degradation Index (RFDI, Mitchard *et al.*, 2012)
-   Forest/Non-Forest

.. figure:: https://raw.githubusercontent.com/lecrabe/alos_mosaics/main/doc/img/display.png

    Display information

Export dataset
--------------

When you're satified with the information displayed, it can be exported for further use in GIS software or in a GEE process. The tool provides two main exportation options: as an asset (in GEE) or a .tif file (in SEPAL).

Both use the GEE export system and share the same set of parameters:

-   Export backscatter (HH, HV, HH/HV power ratio)
-   Export/add Radar Forest Degradation Index (RFDI, Mitchard *et al.*, 2012)
-   Export/add GLCM texture layers for HH and HV polarizations (Variance, Homogeneity, Dissimilarity)
-   Export/add auxiliary metadata layers (Acq. Date, LIA, QA layer)
-   Export K&C forest/non-forest map (separate file)
-   Set the resolution as an integer number

.. note:: 

    The default export parameters include: 25 metre resolution with backscatter and RFDI.
    
.. figure:: https://raw.githubusercontent.com/lecrabe/alos_mosaics/main/doc/img/export.png

    Export
    
.. attention::

    When exporting images to SEPAL, do not quit the application until the downloading process is complete.

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/alos_mosaics/release/doc/en.rst
