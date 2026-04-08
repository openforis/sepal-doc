.. _mangrove-mapping:

Mangrove mapping with SEPAL
============================

This article describes a complete workflow for mapping mangroves using SEPAL — FAO's free, open-source, web-based cloud platform for satellite data analysis. The approach combines multi-sensor satellite data, global mangrove reference datasets, and machine learning classification to produce locally relevant mangrove maps and detect change over time. An optional extension covers above-ground biomass (AGB) mapping.

.. note::

   **Author:** Erik Lindquist, Forestry Officer, Food and Agriculture Organization of the United Nations (FAO)

Overview
--------

The workflow consists of the following stages:

1. :ref:`Registration and setup <mangrove-setup>`
2. :ref:`Request SEPAL resources <mangrove-resources>`
3. :ref:`Define the area of interest <mangrove-aoi>`
4. :ref:`Build an optical mosaic (optional) <mangrove-optical>`
5. :ref:`Build a radar mosaic (optional) <mangrove-radar>`
6. :ref:`Load global mangrove reference datasets <mangrove-global-datasets>`
7. :ref:`Create the high-confidence mangrove reference map <mangrove-remapping>`
8. :ref:`Generate training data <mangrove-training>`
9. :ref:`Incorporate Google Satellite Embeddings <mangrove-embeddings>`
10. :ref:`Classify mangroves <mangrove-classification>`
11. :ref:`Map above-ground biomass (optional) <mangrove-biomass>`
12. :ref:`Detect change using CCDC <mangrove-ccdc>`
13. :ref:`Download and export results <mangrove-export>`

Why use SEPAL for mangrove mapping?
-------------------------------------

SEPAL democratises access to satellite data and analysis tools, enabling autonomous land monitoring without the need for local compute infrastructure. For mangrove mapping specifically, SEPAL provides:

-  **Multi-sensor data access** – seamless integration of optical (Sentinel-2, Landsat, NICFI/Planet) and synthetic aperture radar (SAR) (Sentinel-1 C-band, ALOS L-band) imagery
-  **Multi-temporal analysis** – time-series processing and change detection using the Continuous Change Detection and Classification (CCDC) algorithm
-  **Cloud-based classification** – machine learning classification recipes powered by Google Earth Engine (GEE)
-  **Global reference data** – integration with existing global mangrove products to generate locally relevant training data automatically
-  **Team collaboration** – data saved as GEE assets can be shared across a team, allowing one person to build a composite that all team members can access and classify

.. _mangrove-setup:

1. Registration and setup
--------------------------

Before starting, create accounts on two platforms.

1.1 Google Earth Engine
~~~~~~~~~~~~~~~~~~~~~~~

SEPAL's processing recipes run on GEE. A free GEE account is required.

1. Go to `earthengine.google.com <https://earthengine.google.com>`__.
2. Sign up using a Gmail account.
3. Wait for approval (usually within a few hours to a few days).

1.2 SEPAL
~~~~~~~~~

1. Go to `sepal.io <https://sepal.io>`__ and register for a free account.
2. Connect the GEE account within SEPAL settings.

.. seealso::

   For a step-by-step walkthrough of SEPAL setup, see :doc:`../setup/register`.

.. _mangrove-resources:

2. Request SEPAL resources
---------------------------

SEPAL is always free to use; however, downloading data and running high-performance computing in the cloud requires resources to be allocated to an account. Resources are requested via the **User report** button (displayed as **$ 0/h**) in the lower-right corner of the **SEPAL interface**.

To request resources:

1. Select the **User report** button in the lower-right corner of the **SEPAL interface**.
2. Select **Request additional resources**.
3. Enter the requested amounts. For most mapping work, the following is a reasonable starting point:

   -  **Processing:** $10 USD/month of cloud compute time
   -  **Storage:** $10 USD/month
   -  **Workspace:** 10 gigabytes (GB) of personal SEPAL workspace storage

4. Enter a short message describing the work (e.g. "Mangrove mapping").
5. Select **Apply**. The SEPAL team will review and approve the request.

Once resources are approved, the **Download** button (displayed as a cloud with an arrow icon) will become active in all recipes. Even $1 of resources is sufficient to activate downloading to GEE or Google Drive.

.. note::

   SEPAL supports requests for larger amounts of resources for intensive work, such as training machine learning models. Describe the use case in the request message if needed.

.. _mangrove-aoi:

3. Define the area of interest
--------------------------------

Use the same area of interest (AOI) for all downstream recipes to ensure composites, reference layers, and classification outputs are spatially aligned.

1. Open **Process** in the **SEPAL interface**.
2. Set the AOI using an administrative boundary, an uploaded geometry, or a drawn polygon.

.. _mangrove-optical:

4. Build an optical mosaic (optional)
--------------------------------------

.. note::

   This step is only required if Google Satellite Embeddings are **not** used as the classification input (see :ref:`Section 9 <mangrove-embeddings>`). If using embeddings, proceed directly to :ref:`Section 6 <mangrove-global-datasets>`.

A cloud-free optical mosaic provides the spectral bands used for classification. In SEPAL, all processing starts with a *recipe*. Open a new recipe from the recipe book by selecting the **+** button, then the green **Add recipe** button.

Recommended data sources
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Source
     - Spatial resolution
     - Temporal resolution
     - Bands
   * - Sentinel-2
     - 10 m
     - 5 days
     - 12
   * - Landsat (8/9)
     - 30 m
     - 16 days
     - 8
   * - NICFI/Planet
     - 4.5 m
     - Monthly
     - 4

Recommended bands and indices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Sentinel-2, include bands: **B2, B3, B4, B5, B6, B7, B8, B8A, B11, B12**.

Suggested derived indices:

-  normalized difference vegetation index (NDVI)
-  normalized difference moisture index (NDMI)
-  normalized difference water index (NDWI)
-  modified normalized difference water index (MNDWI)
-  red-edge NDVI variants
-  Tasseled Cap Brightness, Greenness and Wetness
-  short-wave infrared (SWIR) ratios (B11/B8, B12/B11)
-  enhanced vegetation index (EVI)

.. note::

   Avoid the **Aerosol** band for vegetation mapping — it captures atmospheric rather than surface conditions. The near-infrared (NIR) and SWIR bands are particularly important for mangroves: NIR is sensitive to chlorophyll and vegetation health; SWIR helps distinguish inundated vegetation from upland forest and open water.

Composite method
~~~~~~~~~~~~~~~~

Use the **Medoid** composite method, which selects actual observed pixel values rather than statistical summaries, preserving spectral integrity. Save the recipe with a meaningful name (e.g. ``Optical_Medoid_2023``) so it can be referenced in the classification recipe.

.. seealso::

   See :doc:`../cookbook/optical_mosaic` for full instructions on the SEPAL optical mosaic recipe.

.. _mangrove-radar:

5. Build a radar mosaic (optional)
------------------------------------

.. note::

   This step is only required if Google Satellite Embeddings are **not** used as the classification input.

SAR data penetrates cloud cover and is sensitive to canopy structure and soil moisture — making it a valuable complement to optical data in tropical coastal environments where persistent cloud cover limits optical data availability.

Recommended data source
~~~~~~~~~~~~~~~~~~~~~~~~

The primary radar source used in this workflow is **Sentinel-1 C-band SAR**:

-  spatial resolution: 10 m
-  temporal resolution: 12 days
-  bands: VV and VH polarisations

ALOS PALSAR L-band mosaics (25 m, yearly) can be added where available for additional structural information.

Recommended statistics to include
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Band
     - Description
   * - VV mean
     - Average VV backscatter across the year
   * - VH mean
     - Average VH backscatter across the year
   * - VV/VH ratio
     - Structural differentiation
   * - VH standard deviation
     - Seasonal variability; helps distinguish vegetation types

Save the recipe as ``Radar_Mosaic_YYYY``.

.. seealso::

   See :doc:`../cookbook/radar_mosaic` for full instructions on the SEPAL radar mosaic recipe.

.. _mangrove-global-datasets:

6. Load global mangrove reference datasets
-------------------------------------------

Load three global datasets as **EE Asset** recipes in SEPAL to build the high-confidence reference map in :ref:`Section 7 <mangrove-remapping>`. Each dataset is available in the GEE catalog or the Awesome GEE Community Catalog.

To add an **EE Asset** recipe:

1. Add a new recipe and select **EE Asset**.
2. Set the AOI.
3. Search for the asset by name or paste the asset path.
4. Select **Done**.
5. To visualise, open the **Menu** (☰) → select **+** → select the band → set min/max values → select **Apply**.
6. Save the recipe with the name indicated below.

6.1 Global Mangrove Watch (GMW) v3 — 2020 extent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 70

   * - **Asset path**
     - ``projects/sat-io/open-datasets/GMW/extent/GMW_V3``
   * - **Band**
     - ``b1`` (1 = mangrove, 0 = non-mangrove)
   * - **Date filter**
     - 2020-01-01 to 2020-12-31; select first image
   * - **Save as**
     - ``GMW_2020_EEAsset``

6.2 ESA WorldCover land cover — 2021
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 70

   * - **Asset path**
     - ``ESA/WorldCover/v200``
   * - **Band**
     - ``Map``
   * - **Mangrove class value**
     - 95
   * - **Save as**
     - ``WorldCover_2021_EEAsset``

6.3 Digital elevation model (MERIT DEM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 70

   * - **Asset path**
     - ``MERIT/DEM/v1_0_3``
   * - **Band**
     - ``dem``
   * - **Save as**
     - ``MERIT_DEM_EEAsset``

The digital elevation model (DEM) provides an elevation constraint — mangroves occupy low-lying intertidal zones, so pixels above 40 m elevation are excluded from the high-confidence product in :ref:`Section 7 <mangrove-remapping>`.

.. _mangrove-remapping:

7. Create the high-confidence mangrove reference map
------------------------------------------------------

This step converts the three global datasets into a single high-confidence binary map of mangrove and non-mangrove, which is then used to automatically generate training data for the local classification.

If multiple independent global datasets agree that a pixel is mangrove (or non-mangrove), confidence in that label is much higher than if only one dataset indicates this. The elevation constraint further removes unlikely mangrove locations.

Remapping rules
~~~~~~~~~~~~~~~

In SEPAL, use the **Remapping** recipe with the following logic:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Output class
     - Condition
   * - **Class 1 – Mangrove**
     - GMW ``b1`` = 1 **AND** WorldCover ``Map`` = 95 **AND** DEM ``dem`` < 40 m
   * - **Class 2 – Non-mangrove**
     - GMW ``b1`` = 0 **AND** WorldCover ``Map`` ≠ 95 **AND** DEM ``dem`` < 40 m
   * - *(No data)*
     - Pixels that do not meet either condition are excluded

**Output band:** ``class`` (1 = mangrove, 2 = non-mangrove)

**Save as:** ``Mangrove_HighConfidence_Remapping``

.. note::

   The DEM < 40 m filter restricts both mangrove and non-mangrove samples to the intertidal zone, improving the relevance of the non-mangrove class and avoiding confusion with upland forest.

.. tip::

   Use the divided interface (multi-view panel) to inspect the high-confidence product against the optical and radar mosaics before proceeding. Confirm that the mangrove extent looks reasonable for the area.

.. _mangrove-training:

8. Generate training data
--------------------------

With the high-confidence reference map produced, generate training data automatically by stratified sampling — more efficiently and at greater scale than manual digitising.

In SEPAL, training data is generated within the **Classification** recipe using the **Sample classification** option:

1. Open a new **Classification** recipe.
2. In the training data tab, select **Add** > **Sample classification**.
3. Set the sampling source to ``Mangrove_HighConfidence_Remapping`` (recipe reference) or an exported GEE asset of the same (band: ``class``).
4. Use balanced (stratified) sampling — equal numbers of samples per class.
5. Set a random seed for reproducibility.

Recommended sample sizes
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Area of interest
     - Samples per class
   * - Small AOI
     - 300–800
   * - Subnational/national AOI
     - 1000–2000
   * - Very large or heterogeneous AOI
     - 5000–10000

After sampling, inspect the training points visually against the imagery in the multi-view panel. If contaminated points are observed (e.g. mangrove samples landing on water), resample or remove them before running the classification.

.. _mangrove-embeddings:

9. Incorporate Google Satellite Embeddings (AlphaEarth Foundations)
--------------------------------------------------------------------

.. note::

   These are referred to as "Alpha Earth Embeddings" in some training materials. They are now publicly available as the **Google Satellite Embedding dataset**, powered by `AlphaEarth Foundations <https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/>`__ — a geospatial artificial intelligence (AI) model developed by Google and Google DeepMind.

What are satellite embeddings?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Satellite embeddings are pre-computed, AI-generated feature vectors that summarise multi-sensor, multi-temporal Earth observation data into a compact representation. Each 10 m pixel is described by a 64-dimensional embedding vector encoding a full year of observations from:

-  Sentinel-2
-  Landsat
-  Sentinel-1 SAR
-  Copernicus DEM (elevation)
-  ERA5 (climate)
-  GEDI LiDAR (vegetation structure)

Key advantages for mangrove mapping:

-  **Fewer training samples needed** – embeddings encode rich spatial and temporal context, reducing the labelled points required for accurate classification;
-  **Cloud-robust** – embeddings summarise an entire year of acquisitions, making them more robust to cloud contamination than single-date composites;
-  **No deep learning infrastructure required** – pre-computed and analysis-ready; compatible with SEPAL's built-in classifiers;
-  **Faster classification** – typically faster than classifying equivalent optical and radar inputs separately; and
-  **Temporal coverage** – annual embeddings available from 2017 onwards.

Loading embeddings as an EE Asset recipe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 70

   * - **Asset path**
     - ``GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL``
   * - **Asset type**
     - ImageCollection — mosaic or select target year
   * - **Bands**
     - All 64 embedding bands
   * - **Save as**
     - ``AlphaEarth_Embeddings_EEAsset``

1. Add a new recipe and select **EE Asset**.
2. Set the AOI.
3. Search for ``embeddings`` and select **Satellite Embeddings V1**, or paste the asset path above.
4. Select **Done**.
5. To confirm data is loading: open the **Menu** (☰) → select **+** → select any band (e.g. ``Z00``) → select **Apply**.
6. Save the recipe as ``AlphaEarth_Embeddings_EEAsset``.

When to use embeddings vs. optical/radar mosaics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Use **embeddings** when an annual classification is needed and good results are required with limited training data or compute time. When embeddings are used, optical and radar mosaics are **not** needed as classifier inputs.
-  Use **optical and radar mosaics** when classification at a specific sub-annual time point is needed, or when within-year temporal detail is important.
-  Both approaches can be combined if desired.

.. seealso::

   -  `GEE Data Catalog: Satellite Embedding V1 <https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL>`__
   -  `GEE tutorial series: Introduction to Satellite Embeddings <https://developers.google.com/earth-engine/tutorials/community/satellite-embedding-01-introduction>`__
   -  Brown et al. (2025)

.. _mangrove-classification:

10. Classify mangroves
-----------------------

With training data and image inputs prepared, run the SEPAL **Classification** recipe to produce a mangrove/non-mangrove map.

10.1 Set up the classification recipe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Add a new recipe and select **Classification**.
2. When asked which image to classify, choose one of the following:

   -  **Embeddings approach:** ``AlphaEarth_Embeddings_EEAsset`` only (do **not** add optical or radar mosaics)
   -  **Optical/radar approach:** the optical mosaic recipe plus the radar mosaic recipe
   -  **Combined approach:** embeddings plus optical and/or radar mosaics

10.2 Select input bands
~~~~~~~~~~~~~~~~~~~~~~~~

For the **embeddings approach**, add all 64 embedding bands.

For the **optical/radar approach**, recommended bands are:

-  Sentinel-2: B2, B3, B4, B5, B6, B7, B8, B8A, B11, B12, plus derived indices (NDVI, NDMI, NDWI, Tasseled Cap)
-  Sentinel-1: VV mean, VH mean, VH standard deviation

10.3 Define classification classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For mangrove mapping, a three-class legend is recommended:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Class
     - Description
   * - Mangrove
     - Mangrove forest
   * - Non-mangrove
     - All other land cover
   * - Water
     - Open water

Keep classes distinct — overlapping or ambiguous classes reduce classification accuracy. Assign recognisable colours (e.g. green for mangrove, blue for water).

10.4 Add training data
~~~~~~~~~~~~~~~~~~~~~~~

Reference the ``Mangrove_HighConfidence_Remapping`` recipe (or exported asset) generated in :ref:`Section 7 <mangrove-remapping>` and sampled in :ref:`Section 8 <mangrove-training>`. In the training data tab, select **Add** > **Sample classification**.

Add manual training points using the **Marker** icon if local knowledge suggests corrections are needed.

.. tip::

   The classification updates in real time as training points are added or modified, allowing the impact of each change to be seen immediately.

10.5 Configure the classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEPAL uses **Random Forest** by default. Recommended settings:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Parameter
     - Recommended value
   * - Number of trees
     - ~300 (use 25 for exploration; increase for production)
   * - Variables per split (mTry)
     - Default/auto
   * - Probability outputs
     - Enable if available

10.6 Interpret and refine results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the **Menu** (☰) to switch between display bands:

-  **Class** – the final classified map (one class per pixel)
-  **Mangrove percent** – the probability that each pixel belongs to the mangrove class; more informative than the binary class map for understanding model uncertainty

To improve results, iterate by:

-  tightening the high-confidence mask criteria in the **Remapping** recipe (:ref:`Section 7 <mangrove-remapping>`) and resampling (:ref:`Section 8 <mangrove-training>`);
-  adding more training samples;
-  increasing the number of Random Forest trees; or
-  adjusting the input data stack.

.. seealso::

   See :doc:`../cookbook/classification` for full instructions on the SEPAL classification recipe.

.. _mangrove-biomass:

11. Map above-ground biomass (optional)
----------------------------------------

In addition to mangrove extent, SEPAL can produce wall-to-wall maps of above-ground biomass (AGB) by combining point-based biomass measurements with satellite embeddings using a **Regression** recipe.

11.1 Approach
~~~~~~~~~~~~~~

Where biomass measurements are available (from field plots or GEDI LiDAR), and where the 64 embedding bands are available, the known biomass values can be statistically related to the embedding values and applied to every pixel across the AOI — producing a continuous biomass estimate map.

11.2 Option A – Using GEDI LiDAR data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Global Ecosystem Dynamics Investigation (GEDI) is a full-waveform LiDAR instrument on the International Space Station, capturing vegetation height, canopy structure, and above-ground biomass density. GEDI data are point samples rather than wall-to-wall, but can be used as training data to produce a continuous biomass map.

To load GEDI L4A as an EE Asset recipe:

.. list-table::
   :widths: 30 70

   * - **Asset**
     - GEDI L4A Above Ground Biomass Density v2.1
   * - **Band**
     - ``AGBD`` (above-ground biomass density, Mg/ha)
   * - **Visualisation**
     - Thermal colour palette, min = 0, max = ~194
   * - **Save as**
     - ``GEDI_L4A_EEAsset``

To run the biomass regression:

1. Add a new recipe and select **Regression**.
2. Select ``AlphaEarth_Embeddings_EEAsset`` as the image (all 64 bands).
3. In the training data tab, select **Add** > **Sample image**.
4. Select ``GEDI_L4A_EEAsset`` as the source, with ``AGBD`` as the target band.
5. Set the number of samples (increase for production results).
6. Select **Apply** and run.

.. note::

   If the study area is changing rapidly, match the GEDI acquisition year to the target image year. For more stable mangrove areas, using all available GEDI data is acceptable.

11.3 Option B – Using field-collected AGB data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Field-collected plot data with geographic coordinates can be uploaded to GEE as an asset table and used as training data in the **Regression** recipe.

To upload field data to GEE:

1. In the GEE Code Editor, go to the **Assets** tab.
2. Select **New** > **CSV file**.
3. Upload the data file — GEE handles reprojection automatically.
4. Note the asset ID from the asset details panel.

To run the regression using field data:

1. Add a new recipe and select **Regression**.
2. Select ``AlphaEarth_Embeddings_EEAsset`` as the image (all 64 bands).
3. In the training data tab, select **Add** > **Earth Engine table**.
4. Paste the field data table asset ID.
5. Select the AGB column as the target value band.
6. Select **Apply** and run.

11.4 Interpreting biomass results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The regression produces a continuous map of estimated above-ground biomass (Mg/ha). Results improve significantly with more training samples and more trees in the Random Forest model. Consider reserving 20–30% of samples for independent validation.

.. _mangrove-ccdc:

12. Detect change using CCDC
-----------------------------

To map mangrove loss or gain over time, this workflow uses the Continuous Change Detection and Classification (CCDC) algorithm (Zhu and Woodcock, 2014). CCDC fits a time-series model to each pixel using all available satellite observations and detects structural breaks — making it well suited to detecting mangrove conversion events.

12.1 Create a CCDC asset
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Add a new recipe and select **CCDC Asset**.
2. Define the AOI and date range.
3. Select input imagery (Sentinel-2 and/or Landsat recommended).
4. Run the recipe and save the result as a GEE asset.

.. tip::

   Pre-built CCDC assets for specific study areas may be shared by the SEPAL team or colleagues as GEE asset links, avoiding the need to run this computationally intensive step independently.

.. seealso::

   See :doc:`../cookbook/ccdc_slice` for full instructions on creating a CCDC asset.

12.2 Extract CCDC slices
~~~~~~~~~~~~~~~~~~~~~~~~~

A *CCDC slice* is a snapshot of the fitted time-series model at a specific date — providing harmonised, cloud-free spectral values consistent across dates. CCDC slices can be used:

-  as additional input bands in the **Classification** recipe (:ref:`Section 10 <mangrove-classification>`) for improved accuracy using spatio-temporal descriptors; or
-  from two different dates to detect change between them.

.. seealso::

   See :doc:`../cookbook/ccdc_slice` for full instructions on using CCDC slices.

12.3 Run change detection
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Option A – Index Change recipe (two-date comparison):**

1. Add a new recipe and select **Index Change**.
2. Load CCDC slices from two target dates (e.g. 2015 and 2023).
3. Run the recipe to produce a map of positive and negative spectral change.
4. Interpret positive and negative values as mangrove gain or loss.

**Option B – Near-real-time alert recipe:**

SEPAL includes an alert recipe based on CCDC that compares the time-series model to very recent observations (last few days to weeks), enabling near-real-time detection of mangrove disturbance events for operational monitoring.

.. _mangrove-export:

13. Download and export results
--------------------------------

13.1 Export destinations
~~~~~~~~~~~~~~~~~~~~~~~~~

Select the **Download** button (cloud with arrow icon) in any recipe to open the export dialog. Choose:

-  **Bands to export** – e.g. ``class`` for a classified map, or ``mangrove_percent`` for a probability map;
-  **Scale** – spatial resolution in metres (e.g. 10 m for Sentinel-2 or embeddings-based results); and
-  **Destination:**

   -  **Google Earth Engine asset** – exports to the GEE asset folder; recommended for further analysis or sharing;
   -  **Google Drive** – exports to Google Drive for local download; or
   -  **SEPAL workspace** – exports to the SEPAL workspace; use if running further analysis inside SEPAL.

13.2 Monitor export tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~

After selecting **Retrieve**, a spinning icon appears on the purple task button. A green check mark indicates completion. Monitor tasks in the GEE Code Editor under the **Tasks** tab.

13.3 Upload data to GEE
~~~~~~~~~~~~~~~~~~~~~~~~

To use local raster or vector data in SEPAL (e.g. field plots, administrative boundaries, existing maps):

1. In the GEE Code Editor, go to the **Assets** tab and select **New**.
2. Select the file type:

   -  **GeoTIFF** for raster data;
   -  **Shapefile** – upload ``.shp``, ``.shx``, ``.dbf``, and ``.prj`` files together; or
   -  **CSV** for tabular data with geographic coordinates.

3. GEE handles reprojection automatically.
4. Copy the asset ID and use it in any SEPAL **EE Asset** recipe or training data input.

Summary: recommended input data stack
---------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Layer
     - Asset/source
     - Purpose
   * - Optical mosaic (Medoid)
     - Sentinel-2 (B2–B12 + indices)
     - Spectral features (if not using embeddings)
   * - Radar mosaic
     - Sentinel-1 (VV mean, VH mean, VH STD)
     - Structural features (if not using embeddings)
   * - Google Satellite Embeddings
     - ``GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL``
     - AI-derived multi-sensor features (64 bands)
   * - Global Mangrove Watch v3
     - ``projects/sat-io/open-datasets/GMW/extent/GMW_V3``
     - Reference mangrove mask
   * - ESA WorldCover v2
     - ``ESA/WorldCover/v200``
     - Reference land cover (mangrove class = 95)
   * - MERIT DEM
     - ``MERIT/DEM/v1_0_3``
     - Elevation constraint (< 40 m)
   * - High-confidence reference map
     - Remapping recipe output
     - Training data source
   * - GEDI L4A
     - GEE catalog
     - Biomass regression training (optional)
   * - Field AGB plots
     - User-uploaded GEE table
     - Biomass regression training (optional)
   * - CCDC asset
     - SEPAL CCDC Asset recipe
     - Change detection

Additional resources
---------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Resource
     - Link
   * - SEPAL platform
     - `sepal.io <https://sepal.io>`__
   * - SEPAL documentation
     - `docs.sepal.io <https://docs.sepal.io>`__
   * - SEPAL certified online course
     - `FAO SEPAL course <https://www.fao.org/in-action/sepal/resources/certified-course/en>`__
   * - FAO SEPAL brochure
     - `fao.org/in-action/sepal <https://www.fao.org/in-action/sepal/en>`__
   * - Global Mangrove Watch v3.0
     - `JAXA GMW <https://www.eorc.jaxa.jp/ALOS/en/dataset/gmw/area/gmw_map_e.htm>`__
   * - ESA WorldCover
     - `ESA WorldCover <https://esa-worldcover.org>`__
   * - GEDI L4A AGB dataset
     - `GEDI L4A on GEE <https://developers.google.com/earth-engine/datasets/catalog/LARSE_GEDI_GEDI04_A_002>`__
   * - GEE Satellite Embeddings catalog
     - `GEE Data Catalog <https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL>`__
   * - AlphaEarth Foundations
     - `Google DeepMind blog <https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/>`__
   * - Contact
     - sepal@fao.org

References
-----------

Brown, C.F., Kazmierski, M.R., Pasquarella, V.J., et al. 2025. AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data. *arXiv preprint* arXiv:2507.22291.

Simard, M., Fatoyinbo, L., Smetanka, C., Rivera-Monroy, V.H., Castañeda-Moya, E., Thomas, N. and Van der Stocken, T. 2019. Mangrove canopy height globally related to precipitation, temperature and cyclone frequency. *Nature Geoscience*, 12: 40–45.

Zhu, Z. and Woodcock, C.E. 2014. Continuous change detection and classification of land cover using all available Landsat data. *Remote Sensing of Environment*, 144: 152–171.
