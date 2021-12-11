CCDC - Asset Creation
*********************

Introduction
------------

Powered by the API of `Google's Earth Engine <https://earthengine.google.com/>`_, SEPAL facilitates the workflow for applying the Continuous Change Detection and Classification (CCDC) approach as proposed by `Zhu & Woodcock 2014 <https://www.sciencedirect.com/science/article/pii/S0034425714000248>`_.

CCDC is a holistic methodological framework that encompasses various aspects of land mapping and monitoring by using multi-temporal satellite data. The core of the method is a *temporal segmentation* at *pixel-level*. CCDC is data-agnostic, meaning any type of multi-temporal satellite imagery can be theoretically ingested. As opposed to other time-series methods, it is capable to utilize all available bands and derived band ratios.

The temporal segmentation step includes fitting a harmonic model to the observed time-series and detect breaks that indicate a change in land cover or land use. We call the information layers stored from this process a **CCDC asset**.

The layers of the **CCDC asset** contain information of change happening for each pixel, including the date of the break as well its magnitude. In addition, the model parameters are stored for the time-series segments in between those breaks. With the help of these parameters it is possible to extract synthetic images at any given point in time (i.e. *CCDC slices*) that can be used for any subsequent type of classification or regression task.

.. warning::

    The creation of a CCDC asset is the mandatory first step for all types of subsequent workflows and analysis. This step is highly compute intense, which makes it difficult for on-the-fly-processing. An export as an Earth Engine asset is highly recommended. For this, your SEPAL account needs to be connected to your Google Earth Engine account. Follow `Connect SEPAL to GEE <../setup/gee.html>`__ to learn how to register for Google Earth Engine and connect it to your SEPAL account.

Getting Started
---------------

Once logged into SEPAL, open the recipe menu (1) by clicking on the |recipes| button at the top left of the SEPAL start screen. Within the recipe menu (1), select CCDC, which opens a new SEPAL recipe tab (2).

.. |recipes| image:: ../_images/icons/recipes.png
    :width: 4%

The first step is to change the name for the recipe, so once it is closed, you can

On the lower right, you can select :icon:`fas fa-globe`
Once the time-series recipe is selected, SEPAL will show up the recipe process in a new tab(1), the base map will change to Google high-resolution imagery and the AOI selection window will open itself on the bottom right side (2).


Parameter selection
-------------------


Pixel analysis
-------------


Export
------

Quick Guide for Landsat-8 based Asset creation
==============================================

1. Create a CCDC recipe
2. Select your Area of Interest in the **AOI** tab
3. Select your time of interest in the  **DAT** tab, considering a initialization period (12 clear observations, 2-3 years for cloudy areas) before you expect some change.
4. Within the **SRC*** tab, select L8 under Optical datasets and use the color bands blue, green, red, nir, swir1 and swir2 for breakpoint detection.
5. Within the **PRC** tab select *Surface Reflectance* and *BRDF correction*. In addition set the default parameter for cloud masking to **AGGRESSIVE** and turn the cloud shadow mask on.
6. Within the **OPT** tab you can leave the default options.
7. Finally, you will export your assets using the *Download Button*


.. tip::
    The creation of a CCDC asset is computationally intense. Therefore, results shall be exported as an Earth Engine asset for the smooth operation of subsequent steps.


.. info::





.. warning::

    The documentation of this functionality is under construction.

.. tip::

    For specific help, please open an issue on our repository by clicking on this `link <https://github.com/openforis/sepal-doc/issues/new?assignees=&labels=&template=documentation-needed.md>`__.