
Sentinel-1 Radar Bands
======================

When exporting a radar mosaic from the SEPAL platform, the following radar bands are available for analysis:

.. thumbnail:: ../_images/feature/bands/radar_export.png
    :title: SEPAL Optical Bands to export
    :align: center
    :width: 50%



Basic Radar Metrics (VV and VH Polarizations)
---------------------------------------------

- **Metrics Included**:
    - *VV_min, VV_max, VV_mean, VV_std, VV_med*: Statistics of the VV polarization signal, covering minimum, maximum, mean, standard deviation, and median.
    - *VH_min, VH_max, VH_mean, VH_std, VH_med*: Similar statistics for the VH polarization.
    - *ratio_VV_med_VH_med*: The ratio of the median values of VV to VH polarizations, indicating surface roughness and moisture.
    - *VV_cv, VH_cv*: Coefficient of variation for VV and VH, showing the variability relative to the mean.
    - *NDCV (Normalized Difference Coefficient of Variation)*: A normalized measure that highlights differences in texture or moisture content between VV and VH returns.
    - *orbit*: The orbit direction (ascending or descending), which can affect the radar's observation angle and thus the backscatter properties.

- **Description**: These metrics are essential for analyzing surface features, moisture content, vegetation, and other land cover characteristics using radar backscatter properties.
- **Usage**: Widely used in agricultural monitoring, flood mapping, forest monitoring, and urban expansion studies.

Harmonic Analysis Metrics (Conditional on Data Availability)
------------------------------------------------------------

- **Metrics Included** (Only if harmonic dependents are available):
    - *VV_phase, VV_amp, VV_res*: Phase, amplitude, and residuals of the VV signal following harmonic analysis.
    - *VH_phase, VH_amp, VH_res*: Similar metrics for the VH signal.
- **Description**: Harmonic analysis metrics help in understanding seasonal variations and temporal patterns in the radar signal, useful for long-term monitoring.
- **Usage**: Ideal for studying seasonal changes in vegetation, detecting changes in water bodies over time, and monitoring environmental changes.
