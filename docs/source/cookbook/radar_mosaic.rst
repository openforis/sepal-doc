Radar mosaics
=============

Generate analysis-ready data (ARD) from the SAR mission with Radar mosaics
--------------------------------------------------------------------------

The SEPAL recipe for radar mosaics allows users to generate analysis-ready data (ARD) from the Sentinel-1 C-Band synthetic aperture radar (SAR) mission, which can be used in subsequent analysis, such as land cover classification.

Quick guide: timescans
----------------------

The following steps demonstrate the default procedure for creating a yearly timescan, which is useful for tasks such as land cover mapping.

1. Select the **Radar mosaic** within SEPAL recipes.
2. Select your area of interest (AOI) and the year.
3. Check for orbit coverage.

    3.1 De-select all processing parameters.

    3.2 Select **Ascending orbit** and let the mosaic render.

    3.3 De-select **Ascending orbit** and select **Descending orbit**. Let the mosaic render.

    3.4 See if both orbits cover the entire AOI. If they do not, select the orbit that covers the entire AOI. If they do, select both and let the mosaic render; then, check for artifacts that may originate from using both orbits. 

4. Select **Terrain** under Geometric operations.
5. Select **Moderate** under Outlier removal.
6. Export Median, Min, Max, and STD layers for both polarization bands VV and VH.

The following video tutorial demonstrates these steps in a reproducible way:

.. youtube:: lip8C4tq7ig
    :height: 315
    :width: 560

More detailed explanations of what a timescan is, how it relates to the concept of ARD, and what influences the processing parameters have will be added to this documentation at a later date.

For support, :doc:`ask the community <https://groups.google.com/g/sepal-users>`.
