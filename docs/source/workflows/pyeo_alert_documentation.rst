PyEO forest alerts
==================
*Generate and validate forest disturbance alerts from optical satellite imagery using PyEO on SEPAL.*

Background
----------

Near real-time forest disturbance monitoring aims to identify recent changes in forest cover so that analysts and forest managers can review potential loss events promptly. Sentinel-2 provides multispectral optical observations at up to 10 m spatial resolution, with a nominal five-day revisit from the two-satellite constellation. Actual usable observations depend on cloud cover, acquisition availability and image quality.

**PyEO** stands for *Python for Earth Observation*. The PyEO forest alerts workflow combines satellite imagery, machine-learning land-cover classification and time-series change detection. Its implementation on `SEPAL <https://sepal.io/>`_ provides an interface for preparing imagery, mapping land cover, detecting candidate disturbances and reviewing alerts. The PyEO software was developed with forest-monitoring users, including partners in Kenya, and has been used in forest monitoring projects preceding AIM4Forests. See the `PyEO project documentation <https://clcr.github.io/pyeo/>`_.

This page describes the **PyEO Forest Alerts on SEPAL** workflow, illustrated by the **Mato Grosso, Brazil** pilot presented for AIM4Forests. The workflow is intended for detection and review of candidate forest disturbance events. An alert is not, by itself, independently verified evidence of deforestation or a statistically representative estimate of deforested area.

Methodology
-----------

Complete the workflow in five stages:

1. **Preparation:** define the area of interest (AOI), land-cover classes, baseline and monitoring periods, and imagery sources.
2. **Mosaic:** assemble a cloud-screened optical baseline mosaic.
3. **Classification:** train a supervised classifier using labelled samples to produce a baseline land-cover map.
4. **PyEO Alerts:** examine subsequent observations for changes in spectral vegetation condition and land-cover class, applying recurrence and persistence conditions to flag candidate forest disturbances.
5. **Validation:** review alert polygons against before/after imagery, record verdicts and supporting information, and export reviewed results.

The baseline classification defines the land cover from which transitions are monitored. The monitoring stage then identifies candidate transitions from selected forest classes to selected non-forest classes. The PyEO recipe also provides rules based on vegetation-index decline and the consistency of detections over time. These rules help distinguish persistent disturbances from isolated anomalous observations, although cloud artefacts, seasonal vegetation changes and classification errors can still produce false alerts.

.. note::

   The numerical settings and interface labels below document the **Brazil demonstration**, not universally recommended defaults. Adapt the AOI, dates, classes and thresholds to the monitoring region and the current SEPAL implementation. Some interface controls may differ between the test and production instances.

Supported imagery and software
------------------------------

The demonstrated workflow uses **Sentinel-2 surface-reflectance imagery** for optical mosaics and time-series analysis. The SEPAL mosaic interface also offers Landsat imagery as an alternative source. The presentation demonstrates optical imagery; it does not establish an operational Sentinel-1/SAR processing pathway for this particular PyEO SEPAL recipe.

The workflow uses the SEPAL processing interface, Google Earth Engine (GEE) assets for storing spatial inputs and outputs, and the **Deforestation Alert Analysis** SEPAL application for reviewing candidate alerts. The demonstration uses a **Random Forest** classifier for baseline land-cover mapping.

How-to guide
------------

Requirements
""""""""""""

Before starting, prepare:

1. Access to the appropriate SEPAL instance and its processing recipes.
2. Access to Google Earth Engine assets and permission to read the AOI, training data and exported products.
3. An AOI geometry, supplied in the example as an Earth Engine table.
4. A baseline period and a monitoring period.
5. A land-cover legend and labelled training samples for classification.
6. Sufficient processing resources for image retrieval and, for validation, a running SEPAL compute instance.
7. Reference imagery or other evidence for evaluating alerts.

Brazil pilot configuration
""""""""""""""""""""""""""

Use the following values to reproduce the supplied Brazil (Mato Grosso) demonstration. Adjust them for other study areas.

.. list-table:: Brazil demonstration inputs and settings
   :header-rows: 1
   :widths: 35 65

   * - Parameter
     - Demonstration value
   * - Region
     - Mato Grosso, Brazil
   * - AOI centre
     - 15.0204° S, 59.1616° W
   * - AOI bounding box
     - 59.1866°–59.1366° W; 15.0454°–14.9954° S (approximately 30 km²)
   * - Baseline period
     - 2019-01-01 to 2020-01-01
   * - Monitoring period
     - 2021-05-01 to 2021-08-31
   * - AOI asset
     - ``/aim4forests-499914/assets/Brazil_AOI`` (project-specific path)
   * - Training asset
     - ``/aim4forests-499914/assets/Brazil_trainingPoints`` (project-specific path)
   * - Land-cover classes
     - Forest, Soil, Grassland, Dry Forest
   * - Imagery
     - Sentinel-2 surface reflectance
   * - Maximum scene cloud cover
     - 25%
   * - Maximum per-pixel cloud probability
     - 45%
   * - Baseline classifier
     - Random Forest, 25 trees
   * - Alert retrieval scale
     - 10 m

.. important::

   The presentation contains two descriptions of the forest-to-non-forest transitions. Its preparation overview lists ``{Forest, Dry Forest} -> {Soil, Grassland}``, while the detailed PyEO Alerts recipe walkthrough explicitly selects ``{Forest} -> {Soil, Grassland}``. The instructions below follow the **detailed recipe configuration**. Confirm the intended source classes before running a new analysis.

1. Prepare the project
""""""""""""""""""""""

**Create and organise the project**

1. Sign in to SEPAL and open the **Process** screen.
2. Choose **Create recipe** to see the available processing tools.
3. Create or select a project to group the optical mosaic, classification and forest alerts recipes.
4. In the demonstration, the project is named ``Brazil_MatoGrosso``. Other project workspaces shown are ``Ghana_Ashanti`` and ``Kenya_TransNzoia``.
5. Use clear names identifying the region, year and recipe type; this makes it easier to select the correct baseline and alert outputs later.

**Define the monitoring objective**

Identify the AOI, the land-cover classes and the class transitions of interest. In the Brazil demonstration, the monitored changes are from **Forest** to **Soil** or **Grassland**. Select the baseline and monitoring dates before processing imagery. Ensure that the Earth Engine AOI and training assets are accessible from the account running the recipes.

**Result:** a defined AOI, monitoring objective, date ranges and organised project workspace.

2. Create an optical mosaic
"""""""""""""""""""""""""""

The optical mosaic provides the baseline representation of land cover before the monitored changes.

**Select the area of interest**

1. Create an **Optical mosaic** recipe.
2. In the **Area of interest** panel, select **EE table**.
3. Choose the Brazil AOI Earth Engine asset and verify that its footprint appears on the map.

**Set the baseline dates**

4. Select the demonstration baseline window, **1 January 2019 to 1 January 2020**. The target date shown in the walkthrough is **2 July 2019**.
5. Do not add additional past or future seasons for this example.

**Configure imagery and preprocessing**

6. Select **Sentinel-2** as the imagery source.
7. Set the maximum scene cloud cover to **25%**.
8. Use **surface reflectance** imagery. The demonstrated processing settings retain orbit overlap and quickly remove tile overlap.
9. Apply the cloud-screening options shown in the walkthrough, including **SEPAL cloud score** and **Sentinel-2 Cloud Score+**; the example specifies a maximum per-pixel cloud probability of **45%**.
10. Choose the **Medoid** compositing method to represent typical baseline conditions.
11. Generate the 2019 mosaic and export it as an **Earth Engine image asset** for classification.

**Result:** a cloud-screened 2019 baseline optical mosaic.

.. note::

   Cloud-screening controls may be expressed as scores or probabilities with different directions and scales. Verify the meaning of the threshold in the current recipe rather than treating every score as a cloud probability.

3. Classify land cover
""""""""""""""""""""""

The classification recipe produces a land-cover map that defines the baseline forest and non-forest classes.

**Choose imagery and the legend**

1. Create a **Classification** recipe and select the 2019 optical mosaic as the input image.
2. Open the legend builder and define the classes **Forest**, **Soil**, **Grassland** and **Dry Forest**.
3. Assign each class a unique numeric identifier and display colour. Ensure that the identifiers match those used by the training data.

**Add training samples**

4. Add training points using the SEPAL interface or import an existing CSV, such as the example ``BrazilTrainingPoints.csv``.
5. Check that the points overlay the expected land-cover features and that their labels match the legend.
6. Inspect individual training points and reassign or remove incorrectly labelled samples where necessary.

**Train and inspect the classifier**

7. Select **Random Forest**, using **25 trees** in the demonstration. Other parameters, including variables per split and bag fraction, may be tuned.
8. Run the classification and compare the mosaic, classified image and class-confidence layers in the linked map views.
9. Use the map cursor to inspect pixel classes and confidence. The presentation illustrates a **Forest (1)** pixel with **87%** confidence; this is an example pixel, not an overall accuracy score.
10. Review training samples and classifier parameters if the spatial pattern is implausible. Save or export the baseline classification for use in the alert recipe.

**Result:** a classified 2019 land-cover map and associated classification confidence information.

.. important::

   A class-confidence value is not a substitute for independent classification accuracy assessment. Avoid treating training-data fit or an example pixel confidence as an overall accuracy estimate.

4. Generate PyEO forest alerts
""""""""""""""""""""""""""""""

The **PyEO Forest Alerts** recipe uses the baseline classification and the monitoring image time series to identify candidate forest disturbance events.

**Load the baseline and monitoring dates**

1. Create a **PyEO Forest Alerts** recipe.
2. Add the baseline classification from an existing SEPAL recipe or Earth Engine asset.
3. Arrange layers in the multi-pane viewer if useful: baseline mosaic, classification, total detected changes and first change date.
4. Confirm that the baseline dates have been inherited from the selected classification.
5. Set the monitoring period to **1 May 2021 through 31 August 2021** using the date picker.

**Configure image processing and detection**

6. Review the monitoring-image preprocessing settings, including surface reflectance, orbit and tile overlap, and cloud masking with the available SEPAL and Sentinel-2 Cloud Score+ options.
7. In the PyEO options, configure a **minimum NDVI drop** to identify loss of greenness.
8. Set the **minimum number of cumulative detections** and **detection consistency** (a percentage from 0 to 100) to control recurrence and persistence.
9. Select the class transitions of interest. The detailed example uses **FROM: Forest** and **TO: Soil, Grassland**.
10. Run the recipe and inspect the resulting change layers.

.. note::

   The presentation identifies the NDVI-drop, cumulative-detection and consistency controls, but **does not specify their numerical values**. Enter values appropriate to your experiment and record them alongside the exported results. Do not infer default values from this example.

**Interpret the change products**

The multi-pane interface can show the total number of detected changes and the first change date at the selected pixel. Two illustrative map inspections in the presentation show **14 changes / 13 June 2021** and **9 changes / 23 July 2021** at different locations. These are example pixel readings, not region-wide totals. The first-change-date map can help visualise the spatial progression of disturbance through the monitoring period.

**Retrieve and export**

11. Select **Retrieve** and choose the bands needed for subsequent analysis and validation. The demonstrated outputs include total changes, first change date and the first-change-date decision map.
12. Set the export spatial scale to **10 m** for the example.
13. Export the result to **Google Earth Engine** as an **Image** asset. The walkthrough uses **Private** sharing.
14. Wait for the export to finish, then verify the resulting asset and its band names before opening the validation application.

**Result:** an Earth Engine image asset containing forest disturbance alert and change-date layers.

5. Validate forest disturbance alerts
"""""""""""""""""""""""""""""""""""""

The **Deforestation Alert Analysis** application supports project-based review of the exported PyEO alert map. The demonstrated application presents an **eight-step setup and evaluation process**.

**Launch and create a validation project**

1. Start a SEPAL compute instance if required (the walkthrough suggests a ``c4`` instance) and open **Deforestation Alert Analysis** from the applications/tools menu.
2. Create a new project or reopen an existing project. The example project is ``Brazil_MatoGrosso_4mnths``.

**Step 1 – Area of interest**

3. Choose the saved Earth Engine AOI table and select **All features** for the AOI column/selection option shown in the example.
4. Select the AOI and check that the map zooms to the expected region.

**Step 2 – Alerts**

5. Add a custom alert source from **Earth Engine**, selecting the exported PyEO image asset (example name: ``Forest_alerts_Brazil_4m``).
6. Select the **SEPAL PyEO alerts** format and map the required bands:

   * **Alert band:** ``binary_timeseries_decision``
   * **Date band:** ``fcd_decision_map``

7. Preview the alerts. In the demonstration, **orange** indicates confirmed/high-confidence alerts and **purple** indicates probable/lower-confidence alerts.

**Step 3 – Optional layers**

8. Add supporting imagery or reference layers from Earth Engine if they help interpret detected changes. This step is optional.

**Step 4 – Period**

9. Set the review period to **2021-05-01 through 2021-08-31** and the look-back to **0 days**, as demonstrated.

**Step 5 – Download and harmonize**

10. Download the alert source and align it to the project grid. The Brazil example uses **EPSG:32721**, **10 m** resolution and a grid of **544 × 559 pixels**.
11. Apply optional inclusion or exclusion masks if needed. Inspect the harmonisation report before continuing.

The demonstration reports **10,426 alert pixels** with dates from **8 June to 7 August 2021**. These numbers describe the specific example output, not a general result or an independently verified area estimate.

**Step 6 – Integrate and vectorize**

12. Group neighbouring alert pixels into reviewable polygons.
13. Set the demonstrated minimum cluster size to **0.5 ha**. The walkthrough also shows an option to retain small clusters if they touch earlier confirmed loss areas and to review larger clusters first.
14. Generate the alert polygons and inspect their spatial extent.

**Step 7 – Questionnaire**

15. Optionally configure questions to record information for each reviewed alert. The demonstration uses **Loss Driver** and **Response Urgency**.
16. Example loss-driver responses include agricultural expansion, livestock grazing, logging, urban expansion, shifting cultivation and mining. Multiple selections can be permitted.
17. Example urgency choices are **Month**, **Week** and **Today**. The presentation also shows selection of a default Word report template.

**Step 8 – Evaluation**

18. Choose **solo** or **multiple evaluators** review mode and start the analysis.
19. Examine the before-and-after optical imagery and the alert polygon. The demonstrated verdicts are **True Alert**, **False Positive** and **Needs Review**.
20. Answer the questionnaire where applicable and select **Save** to record each review.
21. Move to the next alert and repeat until the required review set is complete.
22. Use the summary and export tools to retrieve reviewed alert information.

**Result:** reviewed alert polygons, analyst verdicts, optional questionnaire responses and exportable supporting evidence.

Validation exports and interpretation
"""""""""""""""""""""""""""""""""""""

The presentation shows the following export options for individual alerts:

* **Alert data:** GeoPackage together with before/after GeoTIFF images.
* **Alert report:** a Word document generated from the selected project template.
* **Timelapse:** an animated GIF based on available satellite observations.

The example includes a Sentinel-2 timelapse for one alert and a Landsat timelapse for another. Results can be inspected in GIS software such as QGIS or incorporated into reporting workflows.

In the demonstrated validation overview, **two of two alerts were reviewed**, with **95.4 ha detected** and **94.3 ha recorded as confirmed loss**; the largest alert covers **94.3 ha**. These are **example review outputs**, not a statistically validated accuracy assessment or transferable performance benchmark. A formal accuracy assessment requires an appropriate reference sample and assessment design.

Workflow outputs
----------------

.. list-table:: Outputs by stage
   :header-rows: 1
   :widths: 25 45 30

   * - Stage
     - Main output
     - Next use
   * - Preparation
     - AOI, periods, class legend and project organisation
     - Mosaic and classification setup
   * - Optical mosaic
     - Baseline optical image / Earth Engine asset
     - Supervised classification
   * - Classification
     - Baseline land-cover map and confidence layers
     - Forest/non-forest transition selection
   * - PyEO Alerts
     - Change counts, first-change-date and decision bands
     - Alert review and validation
   * - Validation
     - Reviewed polygons, verdicts, supporting images and reports
     - Follow-up, reporting and parameter refinement

Troubleshooting and quality checks
----------------------------------

**Area of interest or training assets are not visible**
   Confirm that the selected Earth Engine account has access to the relevant assets and that the correct project and asset paths have been used.

**Training points do not match the legend**
   Check class identifiers, class names, geometry and training-data attributes. Each numeric class value must correspond to the intended legend category.

**The classified image appears implausible**
   Inspect the training points and mosaic quality, adjust training data or classifier settings, and evaluate against independent reference information where available.

**Few or no alerts appear**
   Check the monitoring dates, usable image availability, cloud masking, selected class transitions and NDVI/recurrence/consistency thresholds. Do not lower thresholds without considering false positives.

**Validation cannot read the alert asset**
   Confirm the Earth Engine image export completed and that the selected format is **SEPAL PyEO alerts** with ``binary_timeseries_decision`` and ``fcd_decision_map`` mapped to the correct fields.

**The validation application does not start**
   Check that the required SEPAL compute instance is running and that your account has sufficient resources.

**Alert areas or dates look incorrect**
   Verify the AOI, CRS, output scale, date-band interpretation and harmonisation grid. Review sample locations against before/after imagery.

Screenshots and illustrations
-----------------------------

The supplied project presentation includes step-by-step SEPAL screenshots. To publish them in Sphinx, first export the selected images to the documentation repository (for example, under ``docs/source/_images/workflows/pyeo/``) and then add ``.. figure::`` directives with valid relative paths, alt text and captions. **No image paths are included here because the screenshots have not yet been installed in the repository.**

Recommended figures include the five-stage workflow overview; the Brazil AOI and project selection; optical mosaic AOI, dates and cloud settings; classification legend, training points and confidence panes; PyEO detection options and change maps; Earth Engine retrieval bands; validation band mapping, harmonisation, vectorisation, review and exports.

References and further reading
------------------------------

* `SEPAL documentation <https://docs.sepal.io/en/latest/>`_ — general SEPAL recipes and application guidance.
* `SEPALSTYLE guide <https://docs.sepal.io/en/latest/team/style_guide.html>`_ — writing and interface terminology conventions.
* `CCDC NRT-FDM workflow <https://docs.sepal.io/en/latest/workflows/nrt.html>`_ — related SEPAL near real-time disturbance workflow and documentation style reference; **not** the PyEO detection algorithm.
* `PyEO software documentation <https://clcr.github.io/pyeo/>`_ — background on Python for Earth Observation.
* `AIM4Forests programme <https://www.fao.org/in-action/aim4forests/en>`_ — programme context.

.. note::

   **Documentation source:** *PyEO Forest Alerts on SEPAL — UI workflow walkthrough* (Ivan Reading, Mateus de Souza Macul and Heiko Balzter), supplied project presentation. The demonstration-specific values, screenshots and review outcomes on this page are drawn from that presentation. The article follows the structure of the supplied ``nrt.rst`` reference and the `SEPALSTYLE guide <https://docs.sepal.io/en/latest/team/style_guide.html>`_. Verify settings against the currently deployed SEPAL recipes before operational use.
