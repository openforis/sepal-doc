Radar Mosaics
*************

The SEPAL recipe for radar mosaics allows to generate Analysis-Ready-Data (ARD) from
the Sentinel-1 C-Band SAR mission that can be used in subsequent analysis
such as land cover classification.

Quick guide Timescan
====================

The following steps reflect the default procedure for creating
a yearly Timescan that is for example useful for annual Land Cover Mapping.

1. Select the Radar Mosaic within the Sepal recipes
2. Select your AOI and the year
3. Check for orbit coverage

    3.1 De-select all processing parameters

    3.2 Select **Ascending Orbit** and let the mosaic render

    3.3 De-select **Ascending** and select **Descending Orbit** and let mosaic render

    3.4 See if both orbits cover the entire AOI. If yes, select both and let the mosaic render and check for artifacts that may originate from using both orbits. If not, select the orbit that covers the entire AOI

4. Select **TERRAIN** under geometric operations
5. Select **MODERATE** under outlier removal
6. Export Median, Min, Max, and STD layers for both polarization bands VV and VH

The following video tutorial depicts those steps in a reproducable way:

.. youtube:: lip8C4tq7ig
    :height: 315
    :width: 560

More detailed explanation on what a Timescan is, how it relates to the concept of Analysis-Ready-Data
and what influences do the processing parameters have will be added later.
