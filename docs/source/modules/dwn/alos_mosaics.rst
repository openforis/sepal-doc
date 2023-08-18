ALOS Kyoto & Carbon Mosaics by JAXA
===================================

This module have been designed on top of the interactive framework `sepal_ui <https://github.com/12rambau/sepal_ui>`_. it allows the user to extract ALOS K&C mosaics. 
The input are as simple as: an AOI, a year, and some filters. The user will be able to display the mosaic in an interactive map and export it as a GEE asset and/or a sepal Tif file.

This module is a sepalization of the follwing `script <https://code.earthengine.google.com/3784ea8db0b93bcaa41d1a3ada0c055e>`_ by A. Vollrath.

The process is done in 3 steps described in the bellow sections and presented in the bellow video tutorial: 

.. youtube:: Asc8Nz0B1DI

Select an AOI
-------------

Using the provided AOI selector, select an AOI of your choice between the different methods available in the tool. We provide 3 administration descriptions (from level 0 to 2) and 3 custom shapes (drawn directly on the map, asset or shapefile). 

.. figure:: https://raw.githubusercontent.com/lecrabe/alos_mosaics/main/doc/img/aoi_select.png 
    
    aoi selector 
    
.. note::

    If a custom aoi from shape or drawing is selected, you will be able to use it directly and the upload to GEE will be launched in the background
    

Process mosaic 
--------------

Then in the process tile, you need to set the different parameters of your mosaic: 

-   **year**: The year of interest 
-   **speckle filter**: the speckle filter to use during the process
    
    -   no filter
    -   refined lee: speckle noise removal technique based on the Lee Filter (for more information, see `A.S. Yommy et al. <https://doi.org/10.1109/IHMSC.2015.236>`_).
    -   Quegan filter: See `Quegan et al. <https://doi.org/10.1109/36.964973>`_
-   **Shadow masking**: activate or deactivate shadow masking
-   **Db**: whether or not to scale the output to Db

Once you are happy with your parameters, you can click on the button. The dataset will be automatically send to the vizualization tile.

.. figure:: https://raw.githubusercontent.com/lecrabe/alos_mosaics/main/doc/img/parameters.png

    dataset parameters 

Display dataset
---------------

As mentioned in the above section, the dataset is automatically displayed on the map. THis map is interactive allowing you to zoom in and out. 
Note that you can select betwee 3 diplay options: 

-   Backscatter RGB (HH, HV, HH/HV power ratio)
-   Radar Forest Degradation Index (RFDI, Mitchard et al. 2012)
-   Forest/Non-Forest

.. figure:: https://raw.githubusercontent.com/lecrabe/alos_mosaics/main/doc/img/display.png

    display informations

Export dataset 
--------------

Once you're happy with the information displayed then can be exported to be further used in a GIS software or in a GEE process. The tool provide 2 main exportation options, as an asset(in GEE) or as a Tif file in SEPAL. 

Both use the GEE export system and share the same set of parameter: 

-   Export Backscatter (HH, HV, HH/HV power ratio)
-   Export/Add Radar Forest Degradation Index (RFDI, Mitchard et al. 2012)
-   Export/Add GLCM texture layers for HH and HV polarizations (Variance,  Homogeneity, Dissimilarity)
-   Export/Add auxiliary metadata layers (Acq. Date, LIA, QA layer)
-   Export K&C Forest/Non-Forest map (separate file)
-   set the resolution as an integer number

.. note:: 

    The default export parameter are 25 meters resolution with backscatter and RFDI
    
.. figure:: https://raw.githubusercontent.com/lecrabe/alos_mosaics/main/doc/img/export.png

    export
    
.. danger::

    When the image is exported to SEPAL, you cannot quit the application until the downloading is finished.






.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/alos_mosaics/release/doc/en.rst
