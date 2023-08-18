GuidosToolbox Workbench
=======================

This document provides usage instructions for the image analysis module **GWB** (`GuidosToolbox Workbench <https://forest.jrc.ec.europa.eu/en/activities/lpa/gwb/>`_), here implemented as a Jupyter dashboard on SEPAL. Citation reference: `GuidosToolbox Workbench: Spatial analysis of raster maps for ecological applications <https://doi.org/10.1111/ecog.05864>`_.

Introduction
------------

In 2008, the GuidosToolbox (`GTB <https://forest.jrc.ec.europa.eu/en/activities/lpa/gtb/>`_, `Vogt and Riitters 2017 <https://doi.org/10.1080/22797254.2017.1330650>`_) was developed as a graphical user interface (GUI) to Morphological Spatial Pattern Analysis (`MSPA <https://forest.jrc.ec.europa.eu/en/activities/lpa/mspa/>`_) of raster data (`Soille and Vogt 2009 <https://doi.org/10.1016/j.patrec.2008.10.015>`_). The GTB has since been enhanced with numerous modules for analysis of landscape objects, patterns, and networks, and specialized modules for assessing fragmentation and restoration. The GuidosToolbox Workbench (`GWB <https://forest.jrc.ec.europa.eu/en/activities/lpa/gwb/>`_) provides the most popular GTB modules as a set of command-line applications for 64bit Linux systems. In the following, we describe the implementation of GWB on the SEPAL platform as a Jupyter dashboard based on the `GWB CLI tool <https://docs.sepal.io/en/latest/cli/gwb.html>`_. 

Presentation
^^^^^^^^^^^^

To launch the app please follow the `SEPAL registration steps <https://docs.sepal.io/en/latest/setup/register.html>`_ and then move to the SEPAL Apps dashboard (purple wrench icon on the left side panel), search for and click on GWB ANALYSIS.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/dashboard.png
    :title: SEPAL dashboard 
    :group: gwb-module
    
The application should launch itself in the About section, allowing to select the tool you want to use. 

.. note::
    
    If this is the first time you use the app, you will actually see the following popup:
    
    .. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/licence.png
        :title: licence
        :group: gwb-module
        
    This licence needs to be accepted to use the **GWB** modules. It is also available in the section :code:`Licence` of the app. 
    If you don't want to accept this Licence, just close the app tab.

Usage
^^^^^

General structure
"""""""""""""""""

The application is strucured as followed: 

On the left side you will find a navigation drawer that you can open and close using :btn:`<fa-solid fa-ellipsis-vertical>` (topleft side of the window).

.. tip:: 

    On small devices such as tablet or phones, the navigation drawer will be hidden by default. Click on :btn:`<fa-solid fa-ellipsis-vertical>` (topleft side of the window) to show the full extent of the app. 
    
    .. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/small_device_without_menu.png
        :title: small screen without drawer
        :width: 49%
        :group: gwb-module
        
    .. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/small_device_with_menu.png
        :title: small screen with drawer
        :width: 49%
        :group: gwb-module
        
Each name in the list corresponds to one **GWB** module, presented individually in the next sections. By clicking on it you will display the panels relative to the function you want to use. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/landing.png
    :title: presentation of the structure
    :group: gwb-module

.. danger:: 

    All **GWB** modules require categorical raster input maps in data type unsigned byte (8bit), with discrete integer values within [0, 255] byte. Any other data format will raise an error.
    
Launch a module
"""""""""""""""

For all modules, the first step is sanitizing the image provided by the user and changing the band values according to the module requirements.
    
Then you can select the parameters associated to the selected module and run it by clicking on the final button. 
In the next section we'll describe every module and their specificities.

.. note::

    The :code:`module_results` folder is not dedicated to save your dada but only produce them. Once created, no binary image using the same name can be produced. If you're running the same analysis with different parameters you can safely reuse the same one, if not please delete/move the previous image before running. A warning message will be displayed in the application.

Modules
-------

Each module is presented individually. You can directly jump to the module of interest by clicking on the related link under the section Modules in the right panel of this page and this documentation will guide you through the respective processing steps.

ACC
^^^

This module will conduct the **Accounting** analysis. Accounting will label and calculate the area of all foreground objects. The result are spatially explicit maps and tabular summary statistics. Details on the methodology and input/output options can be found in the `Accounting <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Objects-Accounting.pdf>`_ product sheet.

Setup the input image
"""""""""""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, the following two files will be added to your :code:`downloads` folder:
    
    -   :code:`example.tif`: 0 byte - Missing, 1 byte - Background, 2 byte - Foreground
    -   :code:`clc3class.tif`: 1 byte - Agriculture, 2 byte - Natural, 3 byte - Developed
    
    .. thumbnail::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :title: download sample dataset
        :group: gwb-module
        
    
    Once the files are downloaded, follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdown menus will list the discrete values of your raster input image. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground
-   special background 1 (optional)
-   special background 2 (optional)

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte).

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/4_classes.png
    :title: upload 4 classes
    :group: gwb-module

.. tip::

    For forest analysis, set forest as foreground and all the other classes as background. If you specify special background, it will be treated separately in the analysis (e.g. water, buildings).
    
Select the parameters
"""""""""""""""""""""
You will need to select parameters for your computation: 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/acc_params.png
    :title: acc params
    :group: gwb-module
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8
    -   spatial pixel resolution: 25
    -   area thresholds: 200 2000 20000 100000 200000
    -   option: default
    -   big3pink: True

Foreground connectivity
#######################

This sets the foreground connectivity of your analysis: 

-   8 neighbors (default) will use every pixel in the vicinity (including diagonals)
-   4 neighbors only use the vertical and horizontal ones

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :title: connectivity image
    :width: 50%
    :group: gwb-module
    
Spatial pixel resolution
########################

Set the spatial pixel resolution of your image in meters. It is only used for the summary.

Area thresholds
###############

Set up to 5 area thresholds (measured in pixels). 

Options
#######

Two computation options are available: 

-   stats + image of viewport (default)
-   stats + images of ID, area, viewport (detailed)

Big3pink
########

Two options are available: 

-   do not highlight the 3 largest objects (False)
-   show the 3 largest objects in pink color (True)


Run the analysis
""""""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display information about the computation. Upon completion, it will turn to green and display the computation log. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/acc_results.png
    :title: information logs
    :group: gwb-module

The resulting files are stored in the folder :code:`module_results/gwb/acc/`, for example:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_acc.tif`
-   :code:`<raster_name>_bin_map_acc.csv`
-   :code:`<raster_name>_bin_map_acc.txt`

.. danger::

    If the rectangle turns red, carefully read the information in the log. For example, your current instance may be too small to handle the file you want to analyse. In this case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`example.tif` file.

.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_acc.png
    :width: 50%
    :align: center
    :group: gwb-module


DIST
^^^^

This module will conduct the **Euclidean Distance** analysis. Each pixel will show the shortest distance to the foreground boundary. Pixels inside a foreground object have a positive distance value while background pixels have a negative distance value. The result are spatially explicit maps and tabular summary statistics.
Details on the methodology and input/output options can be found in the `Distance <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Distance-Euclidean.pdf>`_ product sheet.

Setup the input image
"""""""""""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, the following two files will be added to your :code:`downloads` folder:
        
    -   :code:`example.tif`: 0 byte - Missing, 1 byte - Background, 2 byte - Foreground
    -   :code:`clc3class.tif`: 1 byte - Agriculture, 2 byte - Natural, 3 byte - Developed
    
    .. thumbnail::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :title: download sample dataset
        :group: gwb-module
        
    
    Once the files are downloaded, follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdown menus will list the discrete values of your raster input image. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte).

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/2_classes.png
    :title: upload 2 classes
    :group: gwb-module

.. tip::

    For forest analysis, set forest as foreground and all the other classes as background.
    
Select the parameters
"""""""""""""""""""""
You will need to select parameters for your computation: 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/dist_params.png
    :title: dist params
    :group: gwb-module
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8
    -   Options: Euclidian Distance only

Foreground connectivity
#######################

This set the foreground connectivity of your analysis: 

-   8 neighbors (default) will use every pixel in the vicinity (including diagonals)
-   4 neighbors only use the vertical and horizontal one

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :title: connectivity image
    :width: 50%
    :group: gwb-module

Options
#######

Two computation options are available: 

-   compute the Euclidian Distance only
-   compute the Euclidian Distance and the Hysometric Curve


Run the analysis
""""""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display information about the computation. Upon completion, it will turn to green and display the computation log. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/dist_results.png
    :title: information logs
    :group: gwb-module

The resulting files are stored in the folder :code:`module_results/gwb/dist/`, for example:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_dist.tif`
-   :code:`<raster_name>_bin_map_dist.txt`
-   :code:`<raster_name>_bin_map_dist_hist.png`
-   :code:`<raster_name>_bin_map_dist_viewport.tif`

.. danger::

    If the rectangle turns red, carefully read the information in the log. For example, your current instance may be too small to handle the file you want to analyse. In this case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`example.tif` file.
    
.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_dist_hmc.png
    :width: 49%
    :group: gwb-module

.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_dist.png
    :width: 49%
    :group: gwb-module

FAD
^^^

This module will conduct the **fragmentation** analysis at **five fixed observation scales**. Because forest fragmentation is scale-dependent, fragmentation is reported at five observation scales, which allows different observers to make their own choice about scales and threshold of concern. The change of fragmentation across different observation scales provides additional interesting information. Fragmentation is measured by determining the Forest Area Density (**FAD**) within a shifting, local neighborhood. It can be measured at pixel or patch level. The result are spatially explicit maps and tabular summary statistics. Details on the methodology and input/output options can be found in the `Fragmentation <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Fragmentation-FADFOS.pdf>`_ product sheet.

Setup the input image
"""""""""""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, the following two files will be added to your :code:`downloads` folder:
        
    -   :code:`example.tif`: 0 byte - Missing, 1 byte - Background, 2 byte - Foreground
    -   :code:`clc3class.tif`: 1 byte - Agriculture, 2 byte - Natural, 3 byte - Developed
    
    .. thumbnail::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :title: download sample dataset
        :group: gwb-module
        
    
    Once the files are downloaded, follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdown menus will list the discrete values of your raster input image. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground
-   special background 1 (optional)
-   special background 2 (optional)

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte).

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/4_classes.png
    :title: upload 4 classes
    :group: gwb-module

.. tip::

    For forest analysis, set forest as foreground and all the other classes as background. If you specify special background, it will be treated separately in the analysis (e.g. water, buildings).

.. warning::

    The special background 2 is the non-fragmenting background (optional), see the `Fragmentation <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Fragmentation-FADFOS.pdf>`_ product sheet for details.

    
Select the parameters
"""""""""""""""""""""
You will need to select parameters for your computation: 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/fad_params.png
    :title: acc params
    :group: gwb-module
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8
    -   Computation precision: float-precision
    -   Options: per-pixel density, color-coded into 6 fragmentation classes (FAD)

Foreground connectivity
#######################

This sets the foreground connectivity of your analysis: 

-   8 neighbors (default) will use every pixel in the vicinity (including diagonals)
-   4 neighbors only use the vertical and horizontal one

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :title: connectivity image
    :width: 50%
    :group: gwb-module
    
Computation precision
######################

Set the precision used to compute your image. Float precision (default) will give more accurate results compared to rounded byte but will also take more computing resources and disk space.

Options
#######

Three computation options are available: 

-   FAD: per-pixel density, color-coded into 6 fragmentation classes
-   FAD-APP2: average per-patch density, color-coded into 2 classes
-   FAD-APP5: average per-patch density, color-coded into 5 classes

Run the analysis
""""""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display information about the computation. Upon completion, it will turn to green and display the computation log. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/fad_results.png
    :title: information logs
    :group: gwb-module

The resulting files are stored in the folder :code:`module_results/gwb/fad/`, for example:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_fad_<class_number>.tif`
-   :code:`<raster_name>_bin_map_fad_barplot.png`
-   :code:`<raster_name>_bin_map_fad_mscale.csv` 
-   :code:`<raster_name>_bin_map_fad_mscale.tif`
-   :code:`<raster_name>_bin_map_fad_mscale.txt`
-   :code:`<raster_name>_bin_map_fad_mscale.sav`

.. danger::

    If the rectangle turns red, carefully read the information in the log. For example, your current instance may be too small to handle the file you want to analyse. In this case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`example.tif` file.
    
.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_fad_barplot.png
    :width: 49%
    :group: gwb-module

.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_fad_mscale.png
    :width: 49%
    :group: gwb-module

FRAG
^^^^

This module will conduct the **fragmentation** analysis at a **user-selected observation scale**. This module and its option are similar to :code:`fad` but allow the user to specify a single (or multiple) specific observation scale. The result are spatially explicit maps and tabular summary statistics. Details on the methodology and input/output options can be found in the `Fragmentation <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Fragmentation-FADFOS.pdf>`_ product sheet.

Setup the input image
"""""""""""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, the following two files will be added to your :code:`downloads` folder:
        
    -   :code:`example.tif`: 0 byte - Missing, 1 byte - Background, 2 byte - Foreground
    -   :code:`clc3class.tif`: 1 byte - Agriculture, 2 byte - Natural, 3 byte - Developed
    
    .. thumbnail::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :title: download sample dataset
        :group: gwb-module
        
    
    Once the files are downloaded, follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdown menus will list the discrete values of your raster input image. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground
-   special background 1 (optional)
-   special background 2 (optional)

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte).

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/4_classes.png
    :title: upload 4 classes
    :group: gwb-module

.. tip::

    For forest analysis, set forest as foreground and all the other classes as background. If you specify special background, it will be treated separately in the analysis (e.g. water, buildings).
    
.. warning::

    The special background 2 is the non-fragmenting background (optional), see the `Fragmentation <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Fragmentation-FADFOS.pdf>`_ product sheet for details.
    
Select the parameters
"""""""""""""""""""""

You will need to select parameters for your computation: 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/frag_params.png
    :title: acc params
    :group: gwb-module
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8
    -   Spatial pixel resolution: 25
    -   Computation precision: float-precision
    -   Windows size: 23
    -   Options: fragmentation at pixel or at patch level with various number of color-coded classes

Foreground connectivity
#######################

This sets the foreground connectivity of your analysis: 

-   8 neighbors (default) will use every pixel in the vicinity (including diagonals)
-   4 neighbors only use the vertical and horizontal one

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :title: connectivity image
    :width: 50%
    :group: gwb-module
    
Spatial pixel resolution
########################

Set the spatial pixel resolution of your image in meters. Only use for the summary.

Window size
###########

Set up to 10 observation windows sizes (in pixels).

Options
#######

Four computation options are available: 

-   FOS5: per-pixel density, color-coded into 5 fragmentation classes
-   FOS6: per-pixel density, color-coded into 6 fragmentation classes
-   FOS-APP2: average per-patch density, color-coded into 2 classes
-   FOS-APP5: average per-patch density, color-coded into 5 classes

Run the analysis
""""""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display information about the computation. Upon completion, it will turn to green and display the computation log. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/frag_results.png
    :title: information logs
    :group: gwb-module

The resulting files are stored in the folder :code:`module_results/gwb/frag/`, for example:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_frag_fad-<option>_<class>.tif`
-   :code:`<raster_name>_bin_map_frag.csv`
-   :code:`<raster_name>_bin_map_frag.txt`
-   :code:`<raster_name>_bin_map_frag.tif`

.. danger::

    If the rectangle turns red, carefully read the information in the log. For example, your current instance may be too small to handle the file you want to analyse. In this case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the FAD-APP2 option on the :code:`example.tif` file.
    
.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_fad-app2_23.png
    :width: 50%
    :group: gwb-module

LM
^^

This module will conduct the **Landscape Mosaic** analysis at a **user-selected observation scale**. The Landscape Mosaic measures land cover heterogeneity, or human influence, in a tri-polar classification of a location accounting for the relative contributions of the three land cover types **Agriculture**, **Natural**, **Developed** in the area surrounding that location. The result are spatially explicit maps and tabular summary statistics. Details on the methodology and input/output options can be found in the `Landscape Mosaic <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Pattern-LM.pdf>`_ product sheet.

Setup the input image
"""""""""""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, the following two files will be added to your :code:`downloads` folder:
        
    -   :code:`example.tif`: 0 byte - Missing, 1 byte - Background, 2 byte - Foreground
    -   :code:`clc3class.tif`: 1 byte - Agriculture, 2 byte - Natural, 3 byte - Developed
    
    .. thumbnail::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :title: download sample dataset
        :group: gwb-module
        
    
    Once the files are downloaded, follow the normal process using the :code:`downloads/clc3class.tif` file (3 classes).
    
The first step requires to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdown menus will list the discrete values of your raster input image. Select each class in your image and place them in one of the following categories: 

-   dominant land cover 1 (Agriculture)
-   dominant land cover 2 (Natural)
-   dominant land cover 3 (Developed)

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte).

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/3_classes.png
    :title: upload 3 classes
    :group: gwb-module
    
Select the parameters
"""""""""""""""""""""

You will need to select parameters for your computation: 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/lm_params.png
    :title: lm params
    :group: gwb-module
    
.. note::

    This parameter can be used to perform the default computation:
    
    -   window size: 23

Window size
###########

Set the square window size (in pixels). It should be an odd number in [3, 5, ...501].
with :math:`kdim` being the window size, which is related to the observation scale by the following formula: 

.. math::

    obs_scale = (pixres * kdim)^2 / 10000
    
with

-   :math:`obs_scale` in hectare
-   :math:`pixres` in meters
-   :math:`kdim` in pixels

Run the analysis
""""""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display information about the computation. Upon completion, it will turn to green and display the computation log. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/lm_results.png
    :title: information logs
    :group: gwb-module

The resulting files are stored in the folder :code:`module_results/gwb/lm/`, for example:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_lm_23.tif`
-   :code:`<raster_name>_bin_map_lm_23_103class.tif`
-   :code:`<raster_name>_bin_map_heatmap.csv`
-   :code:`<raster_name>_bin_map_heatmap.png`
-   :code:`<raster_name>_bin_map_heatmap.sav`
-   :code:`heatmap_legend.png`
-   :code:`lm103class_legend.png`

.. danger::

    If the rectangle turns red, carefully read the information in the log. For example, your current instance may be too small to handle the file you want to analyse. In this case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`clc3classes.tif` file.
    
.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/lm103class_legend.png
    :width: 49%
    :group: gwb-module

.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/clc3class_lm_23.png
    :width: 49%
    :group: gwb-module

MSPA
^^^^

.. warning:: 

    If you are considering using the MSPA module, keep in mind that the result provides a lot of information (up to 25 classes). The alternative module :code:`GWB_SPA` provides a similar but simplified assessment with up to 6 classes only. Both modules describe morphological features of foreground objects. While MSPA may address certain features of fragmentation, a more comprehensive assessment of fragmentation is obtained with the dedicated fragmentation modules :code:`GWB_FRAG` or :code:`GWB_FAD`.

This module will conduct the **Morphological Spatial Pattern Analysis**. `MSPA <https://forest.jrc.ec.europa.eu/en/activities/lpa/mspa/>`_ analyses shape and connectivity and conducts a segmentation of foreground patches in up to 25 feature classes. The result are spatially explicit maps and tabular summary statistics. Details on the methodology and input/output options can be found in the `Morphology <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Pattern-Morphology.pdf>`_ product sheet.

Setup the input image
"""""""""""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, the following two files will be added to your :code:`downloads` folder:
        
    -   :code:`example.tif`: 0 byte - Missing, 1 byte - Background, 2 byte - Foreground
    -   :code:`clc3class.tif`: 1 byte - Agriculture, 2 byte - Natural, 3 byte - Developed
    
    .. thumbnail::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :title: download sample dataset
        :group: gwb-module
        
    
    Once the files are downloaded, follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdown menus will list the discrete values of your raster input image. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte).

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/2_classes.png
    :title: upload 2 classes
    :group: gwb-module

.. tip::

    For forest analysis, set forest as foreground and all the other classes as background.
    
Select the parameters
"""""""""""""""""""""
You will need to select parameters for your computation: 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/mspa_params.png
    :title: mspa params
    :group: gwb-module
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8 (default)
    -   Edge width: 1
    -   Transition: True
    -   Intext: True
    -   Disk: False
    -   Statistics: False

Foreground connectivity
#######################

This sets the foreground connectivity of your analysis: 

-   8 neighbors (default) will use every pixel in the vicinity (including diagonals)
-   4 neighbors only use the vertical and horizontal one

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :title: connectivity image
    :width: 50%
    :group: gwb-module
    
Edge width
##########

Define the width (measured in pixels) of the Core-boundaries (Edges and Perforations).

Transition
###########

Select if you want to show transition pixels, where connecting pathways go through edges/perforations (transition=1 (true), default) or not (transition=0).

Intext
######

Select if you want to distinguish MSPA classes and Holes laying within Core objects (intext=1 (true), default) or not (intext=0).

Disk
####

Select if you want to process with minimum RAM usage (disk=0 (false), default) or not (disk=1 (true) requires 20% less RAM but +40% processing time).

Statistics
##########

Select if you want to calculate summary statistics (statistics=0 (false), default) or (statistics=1 (true) +10% processing time)

Run the analysis
""""""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display information about the computation. Upon completion, it will turn to green and display the computation log. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/mspa_results.png
    :title: information logs
    :group: gwb-module

The resulting files are stored in the folder :code:`module_results/gwb/mspa/`, for example:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_<4 params>.tif`
-   :code:`<raster_name>_bin_map_<4 params>.txt`

.. danger::

    If the rectangle turns red, carefully read the information in the log. For example, your current instance may be too small to handle the file you want to analyse. In this case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`example.tif` file.
    
.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/mspalegend.gif
    :width: 49%
    :group: gwb-module

.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_8_1_1_1.png
    :width: 49%
    :group: gwb-module

P223
^^^^

This module will conduct the **Density** (P2), **Contagion** (P22) or **Adjacency** (P23) analysis of foreground (**FG**) objects at a user-selected observation scale (`Riitters et al. (2000) <https://www.srs.fs.usda.gov/pubs/ja/ja_riitters006.pdf>`_). The result are spatially explicit maps and tabular summary statistics. The classification is determined by measurements of forest amount (P2) and connectivity (P22) within the neighborhood that is centered on a subject forest pixel. P2 is the probability that a pixel in the neighborhood is forest, and P22 is the probability that a pixel next to a forest pixel is also forest.

Setup the input image
"""""""""""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, the following two files will be added to your :code:`downloads` folder:
        
    -   :code:`example.tif`: 0 byte - Missing, 1 byte - Background, 2 byte - Foreground
    -   :code:`clc3class.tif`: 1 byte - Agriculture, 2 byte - Natural, 3 byte - Developed
    
    .. thumbnail::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :title: download sample dataset
        :group: gwb-module
        
    
    Once the files are downloaded, follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdown menus will list the discrete values of your raster input image. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground
-   special background (for P23 only)

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte).

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/p223_classes.png
    :title: upload 3 classes
    :group: gwb-module

.. tip::

    For forest analysis, set forest as foreground and all the other classes as background. If you specify special background, it will be treated separately in the analysis (e.g. water, buildings)
    
Select the parameters
"""""""""""""""""""""

You will need to select parameters for your computation: 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/p223_params.png
    :title: p223 params
    :group: gwb-module
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Window size: 27
    -   Computation precision: Float (default)
    -   Algorithm: FG-Density
    
Window size
###########

Set the square window size (in pixels) It should be an odd number in [3, 5, ...501] with :math:`kdim` being related to the observation scale by the following formula: 

.. math::

    obs_scale = (pixres * kdim)^2 / 10000
    
with 

- :math:`obs_scale` in hectare
- :math:`pixres` in meters
- :math:`kdim` in pixels

Computation precision
######################

Set the precision used to compute your image. Float precision (default) will give more accurate results compared to rounded byte but will also take more computing resources and disk space.

Algorithm
#########

The P223 module can run: **FG-Density** (P2), **FG-Contagion** (P22), or **FG-Adjacency** (P23)

P223 will provide a color-coded image showing [0,100]% for either **FG-Density**, **FG-Contagion**, or **FG-Adjacency** masked for the Foreground cover. Use the alternative options to obtain the original spatcon output without normalisation, masking, or color-coding.

.. tip::

    For original spatcon output **ONLY**:
    Missing values are coded as 0 (rounded byte), or -0.01 (float precision). For all output types, missing indicates the input window contained only missing pixels.

.. tip::

    For FG-Contagion and FG-Adjacency output **ONLY**, missing also indicates the input window contained no foreground pixels (there was no information about foreground edge).

For all output types, :math:`rounded byte = (float precision * 254) + 1`
    
You'll find the options displayed with the following names in the dropdown menu:

-   FG-Density   (FG-masked and normalised)
-   FG-Contagion (FG-masked and normalised)
-   FG-Adjacency (FG-masked and normalised)
-   FG-Density   (original spatcon output)
-   FG-Contagion (original spatcon output)
-   FG-Adjacency (original spatcon output)
-   FG-Shannon   (original spatcon output)
-   FG-SumD      (original spatcon output)

Run the analysis
""""""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display information about the computation. Upon completion, it will turn to green and display the computation log. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/p223_results.png
    :title: information logs
    :group: gwb-module

The resulting files are stored in the folder :code:`module_results/gwb/p223/`, for example:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_p<option>_<window>.tif`
-   :code:`<raster_name>_bin_map_p<option>_<window>.txt`

.. danger::

    If the rectangle turns red, carefully read the information in the log. For example, your current instance may be too small to handle the file you want to analyse. In this case, close the app, open a bigger instance and run your analysis again.

Here is the result of the computation using the P2 (Foreground-Density) option on the :code:`example.tif` file.

.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_p2_27.png
    :width: 50%
    :group: gwb-module

PARC
^^^^

This module will conduct the **parcellation** analysis. This module provides a statistical summary file (txt/csv- format) with details for each unique class found in the image as well as the full image content: class value, total number of objects, total area, degree of parcellation.
Details on the methodology and input/output options can be found in the `Parcellation <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Objects-Parcellation.pdf>`_ product sheet.

Setup the input image
"""""""""""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, the following two files will be added to your :code:`downloads` folder:
        
    -   :code:`example.tif`: 0 byte - Missing, 1 byte - Background, 2 byte - Foreground
    -   :code:`clc3class.tif`: 1 byte - Agriculture, 2 byte - Natural, 3 byte - Developed
    
    .. thumbnail::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :title: download sample dataset
        :group: gwb-module
        
    
    Once the files are downloaded, follow the normal process using the :code:`downloads/clc3classes.tif` file (3 classes).
    
The first step requires to select your image in your SEPAL folder. The image must be a categorical tif raster.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/0_classes.png
    :title: upload 0 classes
    :group: gwb-module
    
Select the parameters
"""""""""""""""""""""
You will need to select parameters for your computation: 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/parc_params.png
    :title: parc params
    :group: gwb-module
    
.. note::

    This parameter can be used to perform the default computation:
    
    -   Foreground connectivity: 8

Foreground connectivity
#######################

This set the foreground connectivity of your analysis:

-   8 neighbors (default) will use every pixel in the vicinity (including diagonals)
-   4 neighbors only use the vertical and horizontal one

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :title: connectivity image
    :width: 50%
    :group: gwb-module

Run the analysis
""""""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display information about the computation. Upon completion, it will turn to green and display the computation log. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/parc_results.png
    :title: information logs
    :group: gwb-module

The resulting files are stored in the folder :code:`module_results/gwb/parc/`, for example:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_parc.csv`
-   :code:`<raster_name>_bin_map_parc.txt`


.. danger::

    If the rectangle turns red, carefully read the information in the log. For example, your current instance may be too small to handle the file you want to analyse. In this case, close the app, open a bigger instance and run your analysis again.

Here is the result of the computation using the default parameters on the :code:`clc3classes.tif` file.

.. csv-table::
    :header: Class, Value, Count, Area[pixels], APS, AWAPS, AWAPS/data, DIVISION, PARC[%]

    1,1,45,2.44893e+06,54420.7,2.07660e+06,1.27136e+06,0.152039,1.19374
    2,2,164,957879.,5840.73,82557.6,19770.0,0.913812,17.7426
    3,3,212,593190.,2798.07,128177.,19008.4,0.783919,11.0897
    8-connected Parcels:, ,421, 4000000,9501.19, ,1310139.4,0.672465,8.07904

RSS
^^^

This module will conduct the **Restoration Status Summary analysis**. It will calculate key attributes of the current network status, composed of foreground (forest) patches and it provides the normalized degree of network coherence. The result are tabular summary statistics. Details on the methodology and input/output options can be found in the `Restoration Planner <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-RestorationPlanner.pdf>`_ product sheet.

Setup the input image
"""""""""""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, the following two files will be added to your :code:`downloads` folder:
        
    -   :code:`example.tif`: 0 byte - Missing, 1 byte - Background, 2 byte - Foreground
    -   :code:`clc3class.tif`: 1 byte - Agriculture, 2 byte - Natural, 3 byte - Developed
    
    .. thumbnail::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :title: download sample dataset
        :group: gwb-module
        
    
    Once the files are downloaded, follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdown menus will list the discrete values of your raster input image. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte).

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/2_classes.png
    :title: upload 2 classes
    :group: gwb-module

.. tip::

    For forest analysis, set forest as foreground and all the other classes as background.
    
Select the parameters
"""""""""""""""""""""
You will need to select parameters for your computation: 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/rss_params.png
    :title: rss params
    :group: gwb-module
    
.. note::

    This parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8

Foreground connectivity
#######################

This set the foreground connectivity of your analysis: 

-   8 neighbors (default) will use every pixel in the vicinity (including diagonals)
-   4 neighbors only use the vertical and horizontal one

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :title: connectivity image
    :width: 50%
    :group: gwb-module

Run the analysis
""""""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display information about the computation. Upon completion, it will turn to green and display the computation log. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/rss_results.png
    :title: information logs
    :group: gwb-module

The resulting files are stored in the folder :code:`module_results/gwb/rss/`, for example:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`rss<connectivity>.txt`
-   :code:`rss<connectivity>.csv`

.. danger::

    If the rectangle turns red, carefully read the information in the log. For example, your current instance may be too small to handle the file you want to analyse. In this case, close the app, open a bigger instance and run your analysis again.

Here is the result of the computation using the default parameters on the :code:`example.tif` file.

.. csv-table::
    :header: FNAME, AREA, RAC[%], NR_OBJ, LARG_OBJ, APS, CNOA, ECA, COH[%], REST_POT[%]
    
    example_bin_map.tif,428490.00,42.860572,2850,214811,150.34737,311712,221292.76,51.644789,48.355211

SPA
^^^

This module will conduct the **Simplified Pattern Analysis**. SPA analyses shape and conducts a segmentation of foreground patches into 2, 3, 5, or 6 feature classes. The result are spatially explicit maps and tabular summary statistics. :code:`GWB_SPA` is a simpler version of :code:`GWB_MSPA`. Details on the methodology and input/output options can be found in the `Morphology <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Pattern-Morphology.pdf>`_ product sheet.

Setup the input image
"""""""""""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, the following two files will be added to your :code:`downloads` folder:
        
    -   :code:`example.tif`: 0 byte - Missing, 1 byte - Background, 2 byte - Foreground
    -   :code:`clc3class.tif`: 1 byte - Agriculture, 2 byte - Natural, 3 byte - Developed
    
    .. thumbnail::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :title: download sample dataset
        :group: gwb-module
        
    
    Once the files are downloaded, follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdown menus will list the discrete values of your raster input image. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte).

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/2_classes.png
    :title: upload 2 classes
    :group: gwb-module

.. tip::

    For forest analysis, set forest as foreground and all the other classes as background.
    
Select the parameters
"""""""""""""""""""""

You will need to select parameters for your computation: 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/spa_params.png
    :title: spa params
    :group: gwb-module
    
.. note::

    This parameter can be used to perform the default computation:
    
    -   number of pattern classes: 2: Small & linear features (SLF), Coherent

Number of pattern classes
#########################

Set the number of pattern classes you want to compute:

-   2: Contiguous, Small & linear features (SLF)
-   3: Core, Core-Openings, Margin
-   5: Core, Core-Openings, Edge, Perforation, Margin
-   6: Core, Core-Openings, Edge, Perforation, Islet, Margin

Run the analysis
""""""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display information about the computation. Upon completion, it will turn to green and display the computation log. 

.. thumbnail:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/spa_results.png
    :title: information logs
    :group: gwb-module

The resulting files are stored in the folder :code:`module_results/gwb/spa/`, for example:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_spa<number of classes>.tif`
-   :code:`<raster_name>_bin_map_spa<number of classes>.txt`

.. danger::

    If the rectangle turns red, carefully read the information in the log. For example, your current instance may be too small to handle the file you want to analyse. In this case, close the app, open a bigger instance and run your analysis again.

Here is the result of the computation using SPA2 (2 classes) on the :code:`example.tif` file.

.. thumbnail:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_spa2.png
    :width: 50%
    :group: gwb-module

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/gwb/release/doc/en.rst
