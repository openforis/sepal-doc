Near-Real-Time Forest Disturbance Mapping (CCDC based)
======================================================

Background
----------
Near-Real-Time Forest Disturbance Mapping (NRT-FDM) can be useful for a variety of applications, foremost policy enforcement. In this workflow description we provide a step-by-step guide on how to set-up a NRT-FDM on SEPAL by using advanced functionality of the CCDC algorithm.

Requirements
------------

1. Area of Interest
2. Forest Mask and/or Training data for Forest/Non-forest
3. dsfas

Main Steps
----------

1. Create CCDC Asset for historical period (-3 + 1 year around forest mask year)
2. Create CCDC Slice at coinciding forest mask date of the historical period
3. Provide/Generate Training Data for the end of the historical period for Forest/Non-Forest
4. Classify CCDC Slice from Step 2
5. Generate new CCDC Asset utilizing the classification from Step 4
6. Generate CCDC slice with latest valid date
7. Classify new

8. Create mosaic for latest period
9. Compare index to probability change

--> not issue at the end of time-series
- not compare it to last image, but to last year?

.. warning::

    The documentation of this functionality is under construction.

.. tip::

    For specific help, please open an issue on our repository by clicking
