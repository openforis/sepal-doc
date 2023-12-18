BFAST Explorer
==============
*Analyse Landsat SR time-series pixel data*

.. note::

  This tutorial was created using **BFAST Explorer v0.0.1**. If you are using a newer version, some features might differ.

Description
-----------

**BFAST Explorer** is a `Shiny <https://shiny.rstudio.com/>`__ app, developed using R and Python, designed for the analysis of Landsat surface reflectance time series pixel data (BFAST refers to Breaks for Additive Seasonal and Trend).

Three change detection algorithms – **bfastmonitor**, **bfast01** and **bfast** – are used to investigate temporal changes in trend and seasonal components via breakpoint detection.

If you encounter any problems, please send a message to almeida.xan@gmail.com or `create an issue on GitHub <https://github.com/almeidaxan/bfast-explorer/>`__.

Tutorial
--------

Follow this short tutorial to learn how to properly use the tool.

Map tab 
*******

The **Map** tab is the starting tab that is initially displayed when running the tool. It is composed of an interactive map (rendered using the Google Maps engine) and a navigation toolbar. Explore the map by zooming in and panning around.

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-01.jpg
  :group: bfast-explorer

Users can also use the **Search** field located at the top of the toolbar to search for a location. The map automatically zooms in on the desired location, similar to Google Maps. 

In this example, we searched for :code:`unicamp campinas` (the University of Campinas).

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-02.jpg
  :group: bfast-explorer

Now, let's zoom out all the way and place a marker in the north of Brazil, as shown in the example. To place a marker, simply click on the map. Multiple markers can be placed, if desired.

To clear all placed markers, select the red |trash-icon| button on the left side of the toolbar.

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-03.jpg
  :group: bfast-explorer

Next, select one of the markers to download its Landsat pixel data by selecting an already placed marker (it will be highlighted; only one marker may be selected at a time).

By selecting a marker, you can now choose a combination of which satellites to download from using the dropdown menu, located on the bottom of the toolbar. In the example, we have choosen all of the available satellite products: Landsat 5, 7 and 8 SR.

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-04.jpg
  :group: bfast-explorer

Then, press the blue |download-icon| :guilabel:`Get data` button, located on the right side of the toolbar, which will initiate the download of all historical data available. The download progress is displayed in the lower-right corner; it should take less than ten seconds for the three selected products.

.. note::
    
    At the time of writing this article, all surface reflectance data were not available from GEE. Depending on where you place your markers, you may receive the following message: "No data available for the chosen satellite(s) and/or region...Please change your query and try again." Since the SEPAL platform relies on GEE to download data, the SEPAL team can not help with this issue. 

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-05.jpg
  :group: bfast-explorer

If the download is successful, you'll receive a message directing you to the |chart-icon| :guilabel:`Analysis` tab.

Analysis tab
************

In the **Analysis** tab, we can analyse the downloaded data and save the results locally as files.

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-06.jpg
  :group: bfast-explorer

First, choose which **Satellite time series date** to visualize. Even though data was downloaded from Landsat 5, 7 and 8 SR, they can't be analysed separately. However, let's proceed by choosing all of them.

The time series of the first spectral band (:code:`b1`) is plotted for all satellites. A legend distinguishes the different sources.

.. note::
    
    Use caution when comparing **Spectral bands** data from different satellites, as they may not correspond to the same wavelength range (for more information, see `this page <https://landsat.usgs.gov/what-are-band-designations-landsat-satellites>`__).

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-07.jpg
  :group: bfast-explorer

Apart from the spectral bands, there are also four spectral-bands-derived indexes available: **NDVI**, **NDMI**, **EVI** and **EVI2**. As an example, let's check the **NDVI time series**.

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-08.jpg
  :group: bfast-explorer

All time series data can be downloaded as a file by selecting the blue |download-icon| :guilabel:`Data` button. All data will be downloaded as a .csv file, ordered by the acquisiton date. An additional column is included in order to distinguish satellite sources.

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-09.jpg
  :group: bfast-explorer

The time series plot can be downloaded as an image by selecting the blue |download-icon| :guilabel:`Plot` button. A window will appear offering some raster (.jpeg, .png) and a vectorial (.svg) image output formats.

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-10.jpg
  :group: bfast-explorer

Next, select the **Change detection algorithm**. Three options are available: **bfastmonitor**, **bfast01** and **bfast** (for more information, see `this page <http://bfast.r-forge.r-project.org/>`__).

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-11.jpg
  :group: bfast-explorer

By selecting **bfastmonitor**, you can tweak four parameters in the left sidebar: :code:`formula`, :code:`history period type`, :code:`harmonic order`, and :code:`start of monitoring`. These parameters have different impacts on results, which can be verified on the right side plot. Here, we set the maximum value of the :code:`harmonic order` to **9** to avoid problems.

Similar to the time series, the results of the change detection algorithms as .rds data files can also be downloaded by selecting the blue |download-icon| :guilabel:`Results` button. To download the plot, select the blue |download-icon| :guilabel:`Plot` button.

For more information on how to load .rds files on R, see `this page <http://www.fromthebottomoftheheap.net/2012/04/01/saving-and-loading-r-objects/>`__.

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-12.jpg
  :group: bfast-explorer

By selecting **bfast01**, you can tweak two parameters: :code:`formula` and :code:`harmonic order`.

Here, the maximum value of the :code:`harmonic order` is set dynamically, depending on the time series data length and the choice of the :code:`formula` parameter.

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-13.jpg
  :group: bfast-explorer

Finally, by selecting **bfast**, you can tweak two parameters: :code:`h` (minimal segment size) and :code:`season type`. 

Since **bfast** can detect multiple breakpoints, it may take a couple of seconds to process in comparison to the previous two algorithms.

.. thumbnail:: https://raw.githubusercontent.com/almeidaxan/bfast-explorer/master/md/images/tutorial-14.jpg
  :group: bfast-explorer
  
.. |chart-icon| raw:: html

    <i class="fa fa-chart-bar"></i>

.. |trash-icon| raw:: html

    <i class="fa fa-trash"></i>
    
.. |download-icon| raw:: html 

    <i class="fa fa-download"></i>

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/bfast-explorer/master/md/tutorial.rst
