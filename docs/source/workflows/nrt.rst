Near real time forest disturbance mapping (CCDC-based)
======================================================

Background
----------

Near real time forest disturbance mapping (NRT-FDM) can be useful for a variety of applications, especially policy enforcement. In this workflow description, we provide a step-by-step guide on how to set-up an NRT-FDM on SEPAL by using the advanced functionality of the CCDC algorithm.

Requirements
------------

1. Area of interest
2. Forest mask and/or training data for forest/non-forest
3. Data Science for Food and Agricultural Systems (DSFAS)

Main Steps
----------

1. Create CCDC asset for historical period (-3 + 1 year around forest mask year).
2. Create CCDC slice at coinciding forest mask date of the historical period.
3. Provide/generate training data for the end of the historical period for forest/non-forest.
4. Classify CCDC slice from Step 2.
5. Generate new CCDC asset utilizing the classification from Step 4.
6. Generate CCDC slice with latest valid date.
7. Classify new **[insert missing information here]**.
8. Create mosaic for latest period.
9. Compare index to probability change.

**[--> not issue at the end of time-series - not compare it to last image, but to last year?]**

.. attention::

    The documentation of this functionality is under construction. **Text in bold should be reviewed and updated, as needed.**

.. tip::

    For specific help, `open an issue in our repository <https://github.com/openforis/sepal-doc/issues/new?assignees=&labels=&template=documentation-needed.md>`__.
