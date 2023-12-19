TMF
===
*Wrapper for Tropical Moist Forests*


This module provides an interface to clip and download the TMF product (Source: EC JRC) inside SEPAL

About TMF
---------

The European Commission’s Joint Research Centre developed this new dataset on forest cover change in tropical moist forests (TMF) using 38 years of Landsat time series.  
The wall-to-wall maps at 0.09 ha resolution (30m) depict the TMF extent and the related disturbances (deforestation and degradation), and post-deforestation recovery (or forest regrowth) through two complementary thematic layers: a transition map and an annual change collection over the period 1990-2019.  
Each disturbance (deforestation or degradation) is characterized by its timing and intensity.
Deforestation refers to a change in land cover (from forest to non-forested land) when degradation refers to a temporary disturbance in a forest remaining forested such as selective logging, fires and unusual weather events (hurricanes, droughts, blowdown).  

License
^^^^^^^

All data here are produced under studies funded by the Directorate-General for Climate Action of the European Commission through the Roadless-For pilot project and the Lot 2 (Tropical moist Forest Monitoring) of the ForMonPol project (Forest Monitoring for Policies). All data are provided free of charge, without restriction of use. For the full license information see the Copernicus Regulation of the European Commission.

Citation
^^^^^^^^

Publications, models and data products that make use of these datasets must include proper acknowledgement, including citing datasets and the journal article as in the following citation.

For any use, please cite the source dataset:  

C. Vancutsem, F. Achard, J.-F. Pekel, G. Vieilledent, S. Carboni, D. Simonetti, J. Gallego, L.E.O.C. Aragão, R. Nasi. `Long-term (1990-2019) monitoring of forest cover changes in the humid tropics <https://doi.org/10.1126/sciadv.abe160>`_. Science Advances


TMF Explorer
^^^^^^^^^^^^

The `Tropical Moist Forest Explorer <https://forobs.jrc.ec.europa.eu/TMF/>`_ is a web-mapping tool that shows the dataset and allows users to navigate the tropics visualizing the main layers of the Tropical Moist Forest dataset without installing any software.  
We recommend its use to explore the TMF product


Data Users Guide
^^^^^^^^^^^^^^^^

For a description of the TMF datasets and details on how to use the data, you can download the `Data USers Guide <https://forobs.jrc.ec.europa.eu/TMF/download/TMF_DataUsersGuide_vf.pdf>`_.

Usage
-----

Select an AOI
^^^^^^^^^^^^^

Using the provided AOI selector, select an AOI of your choice between the different methods available in the tool. We provide 3 administration descriptions (from level 0 to 2) and 3 custom shapes (drawn directly on the map, asset or shapefile). 

.. figure:: https://raw.githubusercontent.com/lecrabe/tmf_sepal/main/doc/img/aoi_select.png 
    
    aoi selector
    
.. note::

    If a custom aoi from shape or drawing is selected, you will be able to use it directly and the upload to GEE will be launched in the background
    
Select parameters 
^^^^^^^^^^^^^^^^^

You need to select the start and final year of your analysis. TMF let you choose from 2014 to 2019. 
Then you need to select what is the output you want to display on the map:

-   Deforestation
-   Degradation
-   Annual change

Click on the validation button and your data will be automatically displayed on the map. If you want to change one of them you'll need to click on the button again. 

.. figure:: https://raw.githubusercontent.com/lecrabe/tmf_sepal/main/doc/img/parameters.png 

    Parameters
    
.. figure:: https://raw.githubusercontent.com/lecrabe/tmf_sepal/main/doc/img/display.png 
    
    display
    
Export 
^^^^^^

Once you're happy with the information displayed then can be exported to be further used in a GIS software or in a GEE process. The tool provide 2 main exportation options, as an asset(in GEE) or as a Tif file in SEPAL.  

.. figure:: https://raw.githubusercontent.com/lecrabe/tmf_sepal/main/doc/img/export.png 
    
    export
    
.. danger::

    When the image is exported to SEPAL, you cannot quit the application until the downloading is finished.




.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/tmf_sepal/release/doc/en.rst
