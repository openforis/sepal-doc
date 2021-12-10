CCDC - Asset Creation
*********************

Overview
--------

Powered by the API of `Google's Earth Engine <https://earthengine.google.com/>`_, SEPAL facilitates the workflow for applying the Continuous Change Detection and Classification (CCDC) approach as proposed by `Zhu & Woodcock 2014 <https://www.sciencedirect.com/science/article/pii/S0034425714000248>`_.

CCDC is a holistic methodological framework that encompasses various aspects of land mapping and monitoring by using multi-temporal satellite data. The core of the method is the *temporal segmentation* at *pixel-level*. CCDC is data-agnostic, meaning any type of multi-temporal satellite imagery can be theoretically ingested. As opposed to other time-series methods, it is capable to utilize all available bands and derived band ratios.

The temporal segmentation step includes fitting a harmonic model to the observed time-series and detect breaks that indicate a change in land cover or land use. We call the information layers stored from this process a **CCDC asset**.

The layers of the **CCDC asset** contain information of change happening for each pixel. In addition, the model parameters are stored for the time-series in between those breaks.


The creation of a CCDC asset is the mandatory first step for all types of subsequent workflows and analysis.


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