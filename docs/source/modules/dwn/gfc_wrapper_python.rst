Forest change mask
==================

Base Forest mask and Fragmentation tool 

This application allows the user to:
-   define an area of interest
-   retrieve tree cover change data from the `Hansen et al, (2013) <https://science.sciencemag.org/content/342/6160/850>`_ dataset
-   combine the layers to produce a forest change map, for a given canopy cover threshold

Background info on Global Forest Change (GFC)
---------------------------------------------

GFC provides global layers of information on tree cover and tree cover change since 2000, at 30m spatial resolution and consists of:

-   Tree canopy cover for the year 2000 (treecover2000)
-   Global forest cover gain 2000–2012 (gain)
-   Year of gross forest cover loss event (lossyear)

For more information please refer to:

-   `Hansen, M. C. et Al. 2013. “High-Resolution Global Maps of 21st-Century Forest Cover Change.” Science 342 (15 November): 850–53. <https://science.sciencemag.org/content/342/6160/850>`_
-   University of Maryland, GFC `dataset <http://earthenginepartners.appspot.com/science-2013-global-forest>`_

.. thumbnail:: https://earthengine.google.com/static/images/hansen.jpg
    :group: gfc_wrapper

Usage
-----

.. thumbnail:: https://raw.githubusercontent.com/openforis/gfc_wrapper_python/master/doc/img/gfc_app.gif 
    :group: gfc_wrapper

Select an AOI
^^^^^^^^^^^^^

Using the provided AOI selector, select an AOI of your choice between the different methods available in the tool. We provide 3 administration descriptions (from level 0 to 2) and 3 custom shapes (drawn directly on the map, asset or shapefile). 

.. thumbnail:: https://raw.githubusercontent.com/openforis/gfc_wrapper_python/master/doc/img/select_aoi.png 
    :group: gfc_wrapper
    :title: aoi selector 
    
.. note::

    If a custom aoi from shape or drawing is selected, you will be able to use it directly and the upload to GEE will be launched in the background. Check your `GEE code editor <https://code.earthengine.google.com>`_ to use it elsewhere.
    
GFC visualization
^^^^^^^^^^^^^^^^^
Two parameters are available to select the data: 

-   Use the slider to change the threshold to consider between forest and non-forest areas. Once you've selected a value, click on :code:`update map` to update the interactive map layers. 
-   Use the Range slider to move the dates to consider in the analysis.

The new layer is a combination of the GFC layers to produce a forest change map, for a given canopy cover threshold. Only pixels that have a treecover above the threshold will be considered as forest. Every treecovered pixel prior to the start date will be considered as "non forest" and every changed that occurs after the end date will be considered as "stable forest". The legend is displayed in the map. You're allowed to zoom in-out, the data will be dynamically recomputed in GEE. 

When changing the value of the threshold or the dates, a new layer will be added to the map so you can compare and select the more appropriate value of parameters for your analysis. 

.. warning:: 

    The parameters that will be used for the next step is the last asked value of threshold. If you want to come back to a previous value, move the slider back and click on :code:`update map` again.  
  

.. thumbnail:: https://raw.githubusercontent.com/openforis/gfc_wrapper_python/master/doc/img/viz.png
    :group: gfc_wrapper

Export selected data 
^^^^^^^^^^^^^^^^^^^^

Considering the Aoi selected in **step 1** and the parameters selected in **step 2**, the module will generate a combination of the GFC layers to produce a forest change map, for a given canopy cover threshold and between specific dates. It will live in a :code:`~/gfc_wrapper_results/<aoi_name>` folder of your sepal environment.

3 results will be produced:

-   The map of the forest change mask using the color tab presented in the interactive maps (:code:`..._gfc_map.tif``)
-   The distribution of each defined zone (:code:`..._gfc_stat.csv`)
-   The legend of the raster (:code:`..._gfc_legend.pd```

You can download these 3 files directly from the interface using the green buttons. These files are name after your parameters following this convention: :code:`<threshold>_<start_date>_<end_date>_<file>.<suffix>`

.. warning:: 

    The statistic computations are run in the `World Mollweide (ESRI:54009) <https://epsg.io/54009>`_ projection. The results may differs if you want to get them in a local projection.

.. thumbnail:: https://raw.githubusercontent.com/openforis/gfc_wrapper_python/master/doc/img/export.png
    :group: gfc_wrapper

.. thumbnail:: https://raw.githubusercontent.com/openforis/gfc_wrapper_python/master/doc/img/results.png
    :group: gfc_wrapper

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/gfc_wrapper_python/release/doc/en.rst
