CCDC-based Near-Real-Time Forest Disturbance Alerts
===================================================

Background
----------
Near-Real-Time Forest Disturbance Monitoring (NRT-FDM) entails remote sensing techniques that are based on dense time-series and target the generation of recent disturbance events in forested areas. The main objective is to detect those changes as early as possible. This priotization usually comes at the cost of accuracy, as the methods are optimized for speed and timeliness. They are therefore not suited for area estimations (such as for MRV) where accuracy is the main objective.

NRT-FDM is a rapidly evolving field of research and many different approaches have been proposed. The most common ones are based on the detection of abrupt changes in the time-series, which are then classified as disturbance events.

This page provides background information and and a detailed **HOW-TO** for a customised implementation of the CCDC algorithm on the SEPAL platform that is optimized for the generation of near-real-time alerts. It supports various sensor types and satellites, such as medium to very high resolution optical and radar data from Landsat, Sentinel 1 and 2 as well as Planet Labs daily data.

Methodology
-----------
Originally, the CCDC algorithm is a well-established pixel-based method for the detection of changes in dense time-series and is usually applied for mapping changes of land use and land cover over longer periods of time. The algorithm is based on the assumption that the time-series can be modelled by a harmonic function. The harmonic function is fitted to the time-series and the modelled values are compared to the observations. If the difference between the modelled and the observed values exceeds a certain threshold, a break is added, and a new segment is created based on the subsequent observations, fitting a new harmonic model. The threshold for a break is defined as a multiple of the Root-Mean-Square-Error (RMSE) of the harmonic model. You can find more details in the `original article <https://www.sciencedirect.com/science/article/abs/pii/S0034425714000248>`_.

The method implemented in SEPAL is a customised version of that technique, which is optimized for near-real-time alert generation. It consists of 2 elements:
1. A historic reference in the form of a CCDC asset, containing past segments
2. A pixel-wise change detection applied to current imagery and the modelled value of the CCDC asset from 1 year before.

The harmonic model of the historic CCDC asset allows to intersect the observations and retrieve a modelled reflectance at any given point in time, a process also called slicing. This information is used for comparison to newly incoming imagery. The observed value from a newly incoming image is compared to the modelled value from exactly 1 year before. This shall ensure that the comparison is always based on the same phenological stage. If the observed value deviates to a certain degree from the historic value, the pixel is flagged as disturbance.

.. figure:: ../_images/workflows/nrt/method.png
   :alt: A plotted time-series (white) and CCDC model (yellow), with highlughted calibration and monitoring period.
   :width: 800
   :align: center

The degree of deviation is defined as a multiple of the RMSE originating from the harmonic model fitting the observations from a year earlier. Going above that threshhold means a change is initially detected. This value defines the sensitivity of the detection and is expressed as confidence.

A disturbance event counts as confirmed a number of subsequent observations adhere to the same criteria. This is to avoid false positives. The number of observations in a row is defined by the user. The default is 3.

The logic of using a comparison to the modelled value from 1 year before has some important implications. A typical user of a NRT-FDM is usually interested in a monitoring period the spans last days to weeks, but not in the entire year (the default value of the monitoring period is 2 months). Changes that happen within the year, but before the monitoring period, would be included. The method therefore introduces a calibration period that directly precedes the monitoring period. Confirmed changes that already happened before or during the calibration period are not included in the final output by default. This is to ensure that the user only receives alerts for changes that happened during the monitoring period. The length of the calibration period is defined by the user. The default is 3 months. The advanced options allow to turn this behaviour off.

Another advanced option regards the handling of regrowth. Small disturbances from selective logging in tropical forests usually result in a quick canopy closure. By default the algorithms removes those changes as they could originate as well from image artifacts such as re-occuring haze.

..
   Supported Sensors
   -----------------

   Optical Sensors
   """""""""""""""
   - Landsat/Sentinel-2: Users can select both sensors. However, it is recommended to use the combination of both sensors only in the change recipe (see how-to). For processing and storage efficiency, the historic reference can be based on a single sensor only. Even though Landsat has a lower resolution, it still provides a robust historical reference for the higher resolution Sentinel-2 data, while storage is reduced by a factor of 9.

   - Planet: It is possible to use daily Planet imagery to generate alerts at very high spatial and temporal resolution. Apart from some special arrangments, Planet daily imagery is not free. In any way it must be first accessed through the Planet API and ingested into Google Earth Engine as an Image Collection for both, historical reference as well as monitoring. In an operational scenario, this Image Collection is subseuqently populated over time with new, incoming images for the selected area.

   Radar Sensors
   """""""""""""
   - Sentinel-1: The Sentinel-1 sensor is supported. In first test cases it showed reasonable results, but we encourage to test against the dedicated BAYTS recipe whose results are usually more robust. In addition, it is highly recommended to check the current `observation plan <https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1/observation-scenario>`_, as due to the failure of Sentinel-1B, some regions are not covered.

How-to
------

Requirements
""""""""""""
1. Area of Interest (EE table, Country/Regional boundaries, self-drawn polygon)
2. Forest Mask (optional, but recommended)
3. Planet API key (optional, only for Planet daily imagery)

From this `link <https://docs.google.com/presentation/d/1gVb8Ewevp_fQNChSQT-wGRdSIM79x0II/edit?usp=sharing&ouid=107111160061452891127&rtpof=true&sd=true>`_ you can download a PowerPoint Presentation that provides a step-by-step guide for the use of a combination of Landsat and Sentinel-2 imagery over an area in Bolivia. Once you are more familiar, it will help to read further to understand the underlying logic of the workflow.
