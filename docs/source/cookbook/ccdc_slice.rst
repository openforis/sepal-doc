CCDC Slice
==========

Background
------------

Powered by the API of `Google's Earth Engine <https://earthengine.google.com/>`_, SEPAL facilitates the workflow for applying the Continuous Change Detection and Classification (CCDC) approach as proposed by `Zhu & Woodcock 2014 <https://www.sciencedirect.com/science/article/pii/S0034425714000248>`_.

.. warning::
    Creating a CCDC necessitates an already existing CCDC asset, either as a *Saved Sepal Recipe* or, preferibly, as a *Google Earth Engine Asset*. You find the How-To `here ../ccdc.html`_

As those parameters are stored at pixel-level we retain the possibility to extract each pixel's modelled reflectance at any given point in time for the time-span of the underlying time-series. In addition, we can access the parameters describing the model of the temporally intersecting segment. Those can be used in the feature space of subsequent classification and generally improve class separability. This step is called slicing and is further described in the `**CCDC slice recipe** <../cookbook/ccdc_slice.html>`__).

.. warning::

    The documentation of this functionality is under construction.

.. tip::

    For specific help, please open an issue on our repository by clicking on this `link <https://github.com/openforis/sepal-doc/issues/new?assignees=&labels=&template=documentation-needed.md>`__.
