Probability Map Subtraction (PROMS)
===================================

Overview
--------

This tutorial provides a step-by-step guide to estimate forest change areas between two dates using an improved area estimation technique. The method leverages a statistically optimized stratification of forest and forest change areas using continuous probability layers and sample allocation.


.. thumbnail:: ../_images/workflows/proms/workflow.png
    :title: Workflow
    :align: center


.. note::

    In lighter green optional data and steps.


Workflow Steps
--------------


- Input Data Collection for Time 1 and Time 2
- Training data on Stable Forest and Stable Non-Forest between Time 1 And Time 2
- Forest Probability Classification at Time 1 and Time 2
- Forest Change Probability Calculation
- Inclusive Forest Mask Application (Optional)
- Stratification
- Sample Allocation
- Sample Interpretation and analysis


Summary Approach
----------------

In this tutorial, we will demonstrate the methodology applied to the region of Alto Paraguay, aiming to estimate the forest change area between the years 2018 (Time 1) and 2020 (Time 2).

Step 1: Input Data
******************

The first step is to select the input imagery for classification. A minimum of one type of data source is required; however, for optimal classification results, a combination of sensors is recommended. The selection depends on data availability and quality for your study area. To capture changes occurring between Time 1 and Time 2, it is recommended to create annual composites for one year before and one year after each respective time point. This approach includes all possible changes that occurred during Time 1 and Time 2.

SEPAL Tools for Image Combination:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

SEPAL offers several tools to combine images from several sensors into single raster:

- **Optical Mosaics**: For creating optical mosaics, refer to the `Optical Mosaics tool <https://docs.sepal.io/en/latest/modules/Optical_mosaics.html>`__.
- **Radar Mosaics**: For creating radar mosaics, use the  `Radar Mosaics tool <https://docs.sepal.io/en/latest/modules/Radar_mosaics.html>`__.
- **Planet Mosaic**: For creating optical mosaics with high-resolution imagery, see the `Planet Mosaic tool <https://docs.sepal.io/en/latest/modules/Planet_mosaic.html>`__.

For areas with seasonal vegetation variations (e.g., dry forests), consider using Continuous Change Detection and Classification (CCDC). Refer to `CCDC Asset Creation <https://docs.sepal.io/en/latest/modules/CCDC_asset_creation.html>`__ for more information.

Case Study Data Preparation:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&

In our case study, we created:

- Planet Mosaics, Sentinel-1 Time Scans, Sentinel-2 Mosaics in SEPAL.
- ALOS-2 Time Scans in Google Earth Engine (`Link to Script <https://code.earthengine.google.com/168e52df4131e4ccff013f248cbc6cc6>`__)

These datasets were prepared for both years 2017 and 2021 (one year before and one year after Time 1 and Time 2, respectively).

.. thumbnail:: ../_images/workflows/proms/InputData.gif
    :title: Workflow
    :align: center


Step 2: Training Data
*********************

Create training data on the presence and absence of forest for your period of interest. Depending on availability, training data can be sourced from:

- **Existing Maps**: Extract samples from global or regional forest maps.
- **Field Data**: Use ground-truth data collected from field surveys.
- **Other Sources**: Extract samples from datasets like GEDI or GLANCE.

Step 3: Forest Probability Classification
*****************************************

Obtain forest probability maps for Time 1 and Time 2 through supervised classification of your input data, using training data on forest and non-forest classes. It is preferable to use stable samples from the period between Time 1 and Time 2.

Using SEPAL's Classification Tool:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

SEPAL offers a user-friendly `Classification tool <https://docs.sepal.io/en/latest/modules/Classification.html>`__ for building supervised classifications.

Case Study Implementation:
&&&&&&&&&&&&&&&&&&&&&&&&&&

Auxiliary Data: Added terrain data from the `MERIT Digital Elevation Model <http://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/>`__ to the mosaic stack for both years. Classifier: Used a Random Forest Classifier in probability output mode. Output: Generated forest probability maps for 2017 and 2021.

.. note::

    If the number of samples that changed class between Time 1 and Time 2 is small relative to the total number, it won’t significantly affect Random Forest results due to its multiple decision trees and bootstrapping method.

.. thumbnail:: ../_images/workflows/proms/Classification.gif
    :title: Workflow
    :align: center

Step 4: Forest Change Probability Calculation
*********************************************

Calculate the forest change probability map by finding the difference between the forest probability maps of Time 1 and Time 2.

Using SEPAL's Band Math Tool:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

The `Band Math tool <https://docs.sepal.io/en/latest/modules/Band_math.html>`__ allows for mathematical operations on images from SEPAL or Google Earth Engine.

Case Study Calculation:
&&&&&&&&&&&&&&&&&&&&&&&&

- Operation: Subtracted the forest probability band (probability_1) of the 2021 image from the 2017 image as an absolute value.
- Result: High values indicate a high probability of forest change, both possible ‘forest losses’ and ‘forest gains’; low values indicate stability.

.. thumbnail:: ../_images/workflows/proms/FProbDiff.gif
    :title: Workflow
    :align: center


For Multiple Monitoring Dates:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

When intermediate dates are available, calculate the maximum forest change probability:

.. raw:: html

    <style>
        .small-font-math {
            font-size: 12px;
        }
    </style>

.. raw:: html

    <div class="small-font-math">

.. math:: \text{Max Change Probability} = \max(\text{probabilities over all dates}) - \min(\text{probabilities over all dates})

.. raw:: html

    </div>


With only two dates:

.. math:: \text{Change Probability} = |\text{Probability at Time 1} - \text{Probability at Time 2}|

.. thumbnail:: ../_images/workflows/proms/FProbDiff2.gif
    :title: Workflow
    :align: center


Step 5: Inclusive Forest Mask Application (optional)
****************************************************

Apply a ‘forest mask’ to exclude areas with very low forest probability, focusing the stratification on relevant areas.

.. note::

    This mask should not be regarded as a commonly used forest mask but rather as a highly conservative one, designed to include all areas where forest could potentially exist at both Time 1 and Time 2, while excluding areas where forest is definitively absent, such as deserts, croplands, or built-up areas, especially when these categories constitute a significant portion of the total area).

Using SEPAL’s Band Math Tool:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Calculate Maximum Forest Probability: Use the Band Math tool to find the maximum probability across all dates (Time 1 and Time 2 in the case study).


Using SEPAL’s Remapping Tool:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Remap Values: With the Remapping tool, classify areas as 'forest' where the maximum forest probability exceeds a specified threshold, and mask out areas that fall below this threshold.

.. thumbnail:: ../_images/workflows/proms/ForestMaskCreation.gif
    :title: Workflow
    :align: center


Case study implementation:
&&&&&&&&&&&&&&&&&&&&&&&&&&

In our case study we used a 10% maximum forest probability threshold that masked out cropland areas.


Using SEPAL’s Masking Tool:
&&&&&&&&&&&&&&&&&&&&&&&&&&&

Apply Mask: Use the Masking tool to apply the ‘forest mask’ to the forest change probability layer.

.. thumbnail:: ../_images/workflows/proms/ForestMaskApplication.gif
    :title: Workflow
    :align: center




Step 6: Stratification
**********************


Convert the continuous forest change probability map into a categorical map using the SEPAL's `Unsupervised Classification tool <https://docs.sepal.io/en/latest/modules/Unsupervised_classification.html>`__ tool to create a stratification layer.


Using SEPAL’s Unsupervised Classification tool
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


- **Sampling**: Number of Samples: Use a high number (e.g., 100,000) for better representation, especially when areas with high forest change probability are small. Sampling Scale: Consider the forest definition (e.g., 70 meters aligning with a 0.5-hectare MMU).
- **Clusterer**: Algorithm: Use the k-means algorithm. Number of Clusters: Five classes are recommended (Kozak, 2011).


Case Study Implementation:
&&&&&&&&&&&&&&&&&&&&&&&&&&

Samples: 100,000 samples to train the clusterer. Sampling Scale: 70 meters.

.. thumbnail:: ../_images/workflows/proms/UnsupervisedClassification.gif
    :title: Workflow
    :align: center


Apply to Forest Areas Only:
&&&&&&&&&&&&&&&&&&&&&&&&&&&

The stratification could be applied exclusively to areas where forest could potentially exist during the period of interest (both stable and changing) using the masked forest change probability map as input image.

.. thumbnail:: ../_images/workflows/proms/UnsupervisedClassificationForestMask.gif
    :title: Workflow
    :align: center


Step 7: Sample allocation
*************************

Select the sample points for interpretation on the stratification layer using Neyman's method. The samples are optimally distributed according to the variability and area of each stratum:

:math:`n_h = \left( \frac{\text{sd} \cdot \text{área del estrato}}{\sum (\text{sd} \cdot \text{área})} \right) \cdot \text{targetSampleSize}`

Using Google Earth Engine
&&&&&&&&&&&&&&&&&&&&&&&&&

The sample allocation can be applied either to the unmasked stratification layer (as shown in the image above) or to the masked stratification layer (as depicted in the image below).

.. thumbnail:: ../_images/workflows/proms/SampleaAllocationForestMask.gif
    :title: Workflow
    :align: center


.. thumbnail:: ../_images/workflows/proms/SampleaAllocationNoForestMask.gif
    :title: Workflow
    :align: center

Case Study Implementation:
&&&&&&&&&&&&&&&&&&&&&&&&&&

Total number of samples to select: 3000.  Spatial resolution: 70m.

Step 8: Sample interpretation and analysis
******************************************

Estimate the forest change area.
