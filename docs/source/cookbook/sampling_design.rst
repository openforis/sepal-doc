Sampling design
===============
*Plan and export random or systematic sample locations, with optional stratification*

Overview
--------

The **Sampling design** recipe creates point locations for collecting reference observations. Use it to:

-   define the area where samples may be placed;
-   divide the area into strata, when needed;
-   plan how many samples to collect;
-   distribute the samples among the strata;
-   choose random or systematic sample placement; and
-   export the sample locations to a Google Earth Engine (GEE) table asset or the SEPAL workspace.

The recipe creates the sampling design only. It does not label the sample locations, assess map accuracy or calculate final area estimates.

Sampling Design does not show an interactive preview because generating and validating the sample locations can exceed interactive-map limits. The locations are created through an export. A completed GEE table asset can later be added to the map from the **Layers** panel.

.. important::

    A sampling design can be valid but still be a poor fit for the study. Consider what must be estimated, how much uncertainty is acceptable, how many locations can be assessed reliably with the available time and resources, and how the results will be calculated. Consult a sampling specialist when the results will support official statistics or other high-impact decisions.

Terms used in this recipe
^^^^^^^^^^^^^^^^^^^^^^^^^

-   **Area of interest (AOI)**: the outer geographic boundary within which samples may be selected.
-   **Stratum**: a non-overlapping part of the eligible sampling area, commonly defined by a map class.
-   **Target reporting category**: the category the design is mainly intended to estimate, such as forest or forest loss. It can differ from the strata.
-   **Reference observation**: information recorded for a sample, such as whether forest or forest loss is present. It may come from visual interpretation of high-resolution satellite imagery, a field inventory or another suitable source.
-   **Anticipated proportion**: a planning estimate of how common the target reporting category is across the AOI and, when stratified, within each stratum. It is prior information, not a result measured from the sample.
-   **Sample allocation**: the number of samples assigned to each stratum.
-   **Sample arrangement**: the method used to place the samples within each stratum.

Sampling theory in brief
^^^^^^^^^^^^^^^^^^^^^^^^

Sampling means observing selected locations to learn about a larger area or population without visiting every place. How those locations are chosen affects what conclusions the sample can support.

This recipe covers one part of a study: it decides how many locations to select and where to place them. Exporting the points does not finish the study. Reference observations must still be collected or interpreted at those locations and analysed in a way that accounts for how the locations were selected and allocated.

Anticipated proportions, calculated sample sizes and displayed uncertainty estimates are planning values, not results measured from the collected observations.

Workflow
--------

Create a sampling design in the following order:

1.  Select the AOI.
2.  Choose an unstratified or stratified design.
3.  Anticipate the target proportion, when useful prior information is available.
4.  Plan the sample count and its allocation.
5.  Choose random or systematic sample placement.
6.  Export the sample locations and review the result.

Changing an earlier step may invalidate a later step. An orange error indicator means that the affected panel must be reviewed again before continuing.

Start
-----

Go to the **Process** tab and select :btn:`<fa-solid fa-circle-plus> Add recipe` > **Sampling design**.

The setup wizard opens the **Area of interest** and **Stratification** panels. Complete both panels to initialize the recipe. The following parameter buttons then become available in the lower-right corner:

-   :guilabel:`STR`: Stratification
-   :guilabel:`PRO`: Anticipate proportion
-   :guilabel:`ALO`: Sample Allocation
-   :guilabel:`ARR`: Sample Arrangement

Select the :btn:`<fa-solid fa-cloud-arrow-down>` button in the upper-right corner to export a complete design.

.. thumbnail:: ../_images/cookbook/sampling_design/overview.png
    :group: sampling-design-recipe
    :title: Sampling Design workspace with linked map areas, the parameter toolbar and exported sample points

Area of interest
----------------

Use the **Area of interest** panel to define the outer boundary within which sample locations may be selected. The AOI may come from a country or administrative boundary, a drawn geometry, a GEE table, or another source supported by the standard SEPAL AOI selector.

Choose an AOI that covers the area from which sample locations should be selected.

Check the AOI before continuing:

-   Include every location that belongs to the population of interest.
-   Avoid unnecessary geometric detail. Very complex boundaries can increase processing time.

Stratification
--------------

Use the **Stratification** panel to choose whether the sample is divided among map classes.

Why stratify
^^^^^^^^^^^^

Stratification divides the eligible sampling area into non-overlapping strata before samples are selected. Its main statistical purpose is to improve sampling efficiency. A useful stratification may:

-   reduce the expected uncertainty for the same total number of samples; or
-   require fewer samples to reach the same target uncertainty.

These gains are not guaranteed. They are most likely when the strata separate areas with meaningfully different occurrences of the target reporting category and the samples are allocated appropriately. A poor stratification or allocation may provide no gain and can make the result less precise.

The stratification map does not need to show the target reporting category itself. For example, ecological zones can define strata in a design intended to estimate forest area.

Choose the design type
^^^^^^^^^^^^^^^^^^^^^^

Use one of the following designs:

-   **Unstratified**: sample the eligible area inside the AOI without dividing it into strata. Use this option when no useful stratification is available or separate allocation among map classes is unnecessary.
-   **Stratified**: use a categorical image to divide the AOI into strata and allocate samples separately to each.

Create an unstratified design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Turn on **Unstratified** to select sample locations across the eligible area inside the AOI without a stratification image or band.

Create a stratified design
^^^^^^^^^^^^^^^^^^^^^^^^^^

A categorical image assigns each pixel to a discrete class, such as a land-cover type or ecological zone. An image can contain one or more bands; select the band containing the class values to use as strata.

For a stratified design:

1.  Select **Asset** to use a GEE image asset, or **Recipe** to use the image output of another SEPAL recipe.
2.  Select a categorical image.
3.  Select the band containing the stratum values.
4.  Leave **Scale** blank to let SEPAL choose a suitable value. Enter a value in metres only when the design needs a different resolution.

.. note::

    When **Recipe** is selected, SEPAL evaluates that recipe as part of the stratification calculations and sample export. A processing-intensive recipe can make these operations slow or cause an Earth Engine timeout or memory error. If this happens repeatedly, export the recipe output as a GEE image asset and select it with **Asset**.

Once the required inputs are available, SEPAL automatically starts calculating the area and weight of each stratum within the AOI. Wait for the calculation to finish before continuing. The table displays:

-   **Value**: the numeric pixel value identifying the stratum;
-   **Area (ha)**: the mapped stratum area in hectares;
-   **Weight**: the stratum area divided by the total mapped area; and
-   **Total**: the total mapped area and a weight of 100 percent.

.. thumbnail:: ../_images/cookbook/sampling_design/stratification.png
    :group: sampling-design-recipe
    :title: Stratification from a categorical GEE image, calculated at a scale of 10 m
    :width: 60%

Review the calculated strata. Edit a label or colour when the image does not provide suitable class metadata. The labels and colours are included with the exported design.

.. important::

    A masked pixel has no usable value in the selected band and is not part of any stratum. Review the calculated total area and class list before allocating samples.

Sampling frame
^^^^^^^^^^^^^^

The sampling frame is the geographic area eligible for sample selection. For an unstratified design, it is the eligible area inside the AOI. For a stratified design, it is the eligible, unmasked pixels belonging to included strata inside the AOI. Locations outside the sampling frame cannot be selected.

Scale
^^^^^

Scale sets the resolution at which the stratification is read, and with it how much processing the calculations require. For a GEE image asset it starts from the image's own pixel size; see `Grids and projections`_. The approximate number of pixels processed depends on the AOI area divided by the square of the scale. For the same AOI, halving the scale processes approximately four times as many pixels; doubling it processes approximately one quarter as many.

A smaller scale can preserve more spatial detail when the source image supports that resolution, but it increases processing time and memory use. Choosing a scale finer than the source's useful resolution mostly resamples the same information and adds work. A larger scale is faster, but it can remove small or narrow strata, shift class boundaries and change the calculated area and weight of each stratum.

The class recorded for each sample is the one found at the sample location at the resolution in use.

Direct and Queued calculations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Choose how SEPAL calculates stratum areas. Workload depends on the number of pixels and the computation required for each pixel. AOI area and Scale determine the pixel count; a stored asset adds little processing, while a source **Recipe** may add little or a lot.

Select one of the following options:

-   **Direct**: start the calculation immediately in GEE's interactive environment.
-   **Queued**: place the calculation in GEE's batch queue. Batch tasks can run longer and may have more memory than Direct calculations, making them better suited to demanding work. GEE usually runs only a few batch tasks at once, so the calculation may wait for capacity.

Demanding calculations can still be slow or fail with either option.

Anticipate proportion
---------------------

Use the **Anticipate proportion** panel to choose the one target reporting category that the design should plan for and describe how common it is expected to be within each stratum.

The target reporting category is the category whose area or proportion the design is mainly intended to estimate. It does not have to be one of the strata or originate from the stratification map. For example, ecological zones can be the strata while forest is the target reporting category.

Why anticipate a proportion
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Anticipated proportions help SEPAL plan where samples are expected to reduce uncertainty most. With an appropriate allocation strategy and credible anticipated proportions, the design may achieve similar expected precision with fewer observations, or better expected precision with the same number of observations.

SEPAL also uses anticipated proportions to estimate how precise the result may be. For a stratified design, you can set a precision target and let SEPAL calculate the total sample size, or set the number of samples you can assess and see the expected precision. For an unstratified design, you enter the number of samples directly and SEPAL can estimate the expected precision. This helps balance the desired precision against the available assessment capacity.

These calculations focus on one target reporting category. Choose the category that matches the main objective. Other categories can still be recorded. Inaccurate anticipated proportions can make the design less efficient, but they do not invalidate the observations collected later. The final precision is calculated from those observations and may differ from the planning result.

How stratification and proportions interact
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Unstratified** and **No proportions** control different parts of the design:

-   **Unstratified** means that the AOI is sampled as one stratum instead of being divided by a categorical image.
-   **No proportions** means that no prior estimate is supplied for a target reporting category. It does not mean that the proportion is zero or change which locations are eligible.

An unstratified or stratified design can therefore be used with or without anticipated proportions.

Choose how to anticipate proportions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Select **No proportions** when reliable prior information is unavailable. Otherwise, select one of the following methods:

Probability image
"""""""""""""""""

Choose **Probability image** when you have an estimated probability of the target reporting category at each location. SEPAL averages these probabilities within each stratum to approximate the expected proportion.

For example, suppose **Tree** is the target reporting category and a SEPAL classification provides a **Class** band and a **Tree %** probability band. The **Class** band can define land-cover strata, while **Tree %** anticipates the proportion of Tree within each stratum. Alternatively, ecological zones could define the strata while the same **Tree %** band anticipates Tree within each zone.

Select the probability band for the target category — **Tree %** in this example — not **Class probability**, which describes the confidence of whichever class was assigned at each location.

Categorical image
""""""""""""""""""

Choose **Categorical image** when a categorical map provides useful prior information about the target reporting category within each stratum. SEPAL calculates the fraction mapped as the selected target class and uses that fraction as the anticipated proportion.

For example, suppose **Tree** is the target reporting category. Ecological zones can define the strata, while the **Class** band of a land-cover map supplies the anticipated proportions by selecting **Tree** as the target class.

Do not reuse the categorical band that defines the strata. It would return 100 percent for the selected stratum and 0 percent for the others. A separate classification containing the same classes can be used when it is a credible source of prior information, but its results describe agreement between the two maps and should not be treated as evidence that either map is correct.

Manual
""""""

Select **Manual** to enter the anticipated percentage separately for each stratum. Base the values on prior studies, pilot observations or documented expert judgement.

Configure the panel
"""""""""""""""""""

For **Probability image** or **Categorical image**:

1.  Select an **Asset** or **Recipe**, then select the source image and band.
2.  For a probability image, indicate whether values range from 0 to 100 instead of 0 to 1. For a categorical image, select the target **Class**. When class metadata is unavailable, load the distinct values or enter the numeric class value.
3.  Enter the processing **Scale** and select **Direct** or **Queued**.

The **Direct** and **Queued** options behave as described under `Direct and Queued calculations`_. The Scale in this panel controls the anticipated-proportion calculation's pixel workload independently of the stratification Scale.

Once the required inputs are available, SEPAL automatically calculates the anticipated proportion for each stratum. Wait for the calculation to finish and review the values before continuing.

For an image-based method, SEPAL combines the calculated stratum proportions using their area weights. If reliable prior information is available for the AOI as a whole, enter **Anticipated overall proportion** to apply that value. SEPAL adjusts the stratum values to match it while keeping every stratum between 0 and 100 percent.

For example, suppose **Tree** is the target reporting category and the probability image produces an anticipated overall proportion of 5 percent. A previous assessment for the same area suggests that the proportion is closer to 10 percent. Enter **10** as the **Anticipated overall proportion**.

SEPAL doubles every calculated stratum proportion. A stratum calculated at 10 percent becomes 20 percent, while one calculated at 2 percent becomes 4 percent. The relative differences among strata are preserved, but their area-weighted overall proportion becomes 10 percent.

Review the calculated or manually entered proportions and any overall adjustment before continuing.

.. thumbnail:: ../_images/cookbook/sampling_design/proportions.png
    :group: sampling-design-recipe
    :title: Tree proportions anticipated from a probability image and adjusted to an overall proportion of 10 percent
    :width: 60%

Sample allocation
-----------------

Use the **Sample Allocation** panel to plan how many samples the design should contain and, for a stratified design, how they are distributed among the strata.

Anticipated proportions allow SEPAL to estimate precision for an entered sample size. For a stratified design, they also allow SEPAL to calculate the sample size needed for a precision target and use **Optimal** or **Power** allocation. Without anticipated proportions, enter the sample size directly; SEPAL cannot estimate precision for the target reporting category. **Proportional**, **Equal** and **Balanced** allocation remain available for a stratified design.

Why allocation matters
^^^^^^^^^^^^^^^^^^^^^^

The total sample size controls the overall assessment effort. When the total is fixed, assigning more samples to one stratum leaves fewer for the others. Two designs with the same total sample size can therefore have different expected precision.

Set the target
^^^^^^^^^^^^^^

With anticipated proportions, a stratified design can use one of two targets:

-   **Samples**: enter the total number of samples you can assess or have otherwise decided to collect. SEPAL estimates the expected precision for that sample size.
-   **Error**: enter a target relative margin of error. SEPAL calculates the total sample size expected to meet that target.

For an unstratified design, enter the sample count directly in the allocation table. When an anticipated proportion is available, SEPAL displays the expected margin of error for that count.

The **Error** target is a relative margin of error: it expresses the planned uncertainty as a percentage of the anticipated overall proportion, not as percentage points. It is a planning result and depends on the anticipated proportions being reasonable.

The **Confidence level** describes how often the calculated margin-of-error range would be expected to contain the true proportion if the sampling process were repeated many times. **95 percent** is the standard choice. Use **90 percent** when somewhat less confidence is acceptable in return for a smaller required sample, or **99 percent** when stronger confidence justifies a larger required sample.

.. important::

    SEPAL uses the total sample size, whether entered directly or calculated from an **Error** target, to allocate samples among strata. The margin of error, whether entered as the target or estimated from the sample size, is only a planning estimate. How closely it matches the final uncertainty depends largely on how closely the proportions found in the reference observations match the anticipated proportions. Calculate the final uncertainty from the collected observations using a method appropriate for the sampling design.

Choose an allocation strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The allocation strategy controls how the total sample size is divided among strata.

When comparing strategies, watch the value that SEPAL recalculates. With **Error** selected, a lower sample size indicates greater planned efficiency for the same uncertainty target. With **Samples** selected, a lower margin of error indicates greater planned efficiency for the same sample size. These comparisons depend on the anticipated proportions being credible.

.. list-table:: Allocation strategies
    :header-rows: 1
    :widths: 18 42 40

    * - Strategy
      - How it allocates samples
      - When it may be useful
    * - **Proportional**
      - Assigns samples in proportion to mapped stratum area.
      - When similar sampling effort per unit area is appropriate.
    * - **Equal**
      - Assigns sample counts as evenly as possible among strata. Counts can differ by one when the total does not divide evenly.
      - When small strata need strong representation. It can assign many samples to very small strata.
    * - **Balanced**
      - Uses the midpoint between equal and proportional allocation.
      - When a compromise between area and representation is needed.
    * - **Optimal**
      - Uses anticipated proportions to place more samples in strata expected to contribute more uncertainty.
      - When the anticipated proportions are credible and the main goal is efficient estimation of the target reporting category.
    * - **Power**
      - Modifies Optimal by reducing the influence of each stratum's expected target amount. A value of 1 matches Optimal; lower values shift relatively more samples toward smaller non-zero expected amounts.
      - When you want to give more representation than Optimal to strata expected to contain smaller amounts of the target reporting category.

Automatic allocations are rounded to whole samples and then adjusted to preserve the requested total and the minimum per stratum. The resulting allocated per-stratum counts can therefore differ slightly from the ideal mathematical proportions.

.. thumbnail:: ../_images/cookbook/sampling_design/allocation.png
    :group: sampling-design-recipe
    :title: Balanced allocation of 5000 samples among nine strata
    :width: 60%

Set the minimum per stratum
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use **Min samples/stratum** to require automatic allocation to assign at least this many samples to each stratum. The recipe requires at least two samples in every stratum.

This setting applies to Proportional, Balanced, Optimal and Power allocation. Equal and Manual use the hard minimum of two directly.

.. important::

    SEPAL requires at least two samples per stratum, but this is usually too few to describe a stratum reliably. If results will be reported by stratum, choose a higher minimum based on the required precision and the number of locations that can be assessed.

The total sample size must be large enough to satisfy the minimum for every stratum. Rare strata may not contain enough usable locations to meet the allocated count, even when the arithmetic allocation is valid.

Allocate manually
^^^^^^^^^^^^^^^^^

Select **Manual** to enter the sample size for every stratum. Each value must be an integer of at least two.

Review the allocation
^^^^^^^^^^^^^^^^^^^^^

Review the allocation table. Confirm that:

-   the total sample size can be assessed reliably within the available time and resources;
-   important and rare strata receive enough samples; and
-   any displayed margin of error is acceptable as a planning estimate.

The allocation sets the requested counts. Whether the export can place them is checked later; see `When too few sample locations are found`_.

Sample arrangement
------------------

Use the **Sample Arrangement** panel to place the allocated samples within the AOI or within each stratum.

Why arrangement matters
^^^^^^^^^^^^^^^^^^^^^^^

Arrangement controls spatial coverage and the randomization used to select locations. It does not change the allocation among strata. Choose it based on the intended analysis, spatial pattern of the population, operational constraints and need for reproducibility.

Random and systematic arrangements make different trade-offs:

-   Randomly placed locations can cluster or leave spatial gaps. No minimum separation is enforced.
-   Systematic placement spreads locations regularly across space. Reusing the same grid provides stable sample locations for estimates over time and may allow previously collected observations to be retained when the stratification is corrected.

Random arrangement
^^^^^^^^^^^^^^^^^^

Select **Random** to place locations randomly.

Systematic arrangement
^^^^^^^^^^^^^^^^^^^^^^

Select **Systematic** to place samples on a regularly spaced grid.

SEPAL places locations in a hexagonally spaced pattern and organizes them into a fixed set of nested **grid levels**. Each level represents an available sampling density. Moving one level coarser removes alternating locations in a fixed pattern, leaving roughly half within each stratum. Moving to a denser level adds those locations back while retaining the locations from coarser levels.

When the same grid is reused, this allows sampling intensity to be increased or reduced without replacing all existing locations.

Because sample counts change in steps between grid levels, a level will not usually match the requested count exactly. Within a stratified design, SEPAL selects a level separately for each stratum to approach its allocated count. The result combines stratification with systematic placement; it is not the same as applying one uniform grid across the AOI.

Choose a **Sample size strategy**:

.. list-table:: Systematic sample size strategies
    :header-rows: 1
    :widths: 18 42 40

    * - Strategy
      - Result
      - Statistical consideration
    * - **Oversample**
      - Selects a grid level intended to produce at least the requested count.
      - A successful export can exceed the requested count. If the densest permitted grid still cannot reach the request, the export stops with an error rather than returning fewer samples.
    * - **Closest**
      - Selects the available grid level closest to the requested count.
      - The final count may be above or below the request, but it must meet the minimum requirement per stratum.
    * - **Exact**
      - For each stratum, selects the least dense grid level that meets or exceeds the allocated count, then randomly removes excess locations in that stratum.
      - The result is not a purely systematic sample. If enough systematic locations cannot be found, the export stops with an error rather than returning fewer samples.

Choose a **Grid start**:

-   **Random**: derive the global grid start from the seed. Use this when the systematic design requires a randomized start.
-   **Fixed**: use the same fixed global start. This is useful for operational consistency, but it does not randomize the grid start.

Nearby locations are often more alike than locations farther apart. This is called spatial autocorrelation. Samples placed too close together may repeat much of the same information and improve precision less than samples spread farther apart. Use **Min distance** to keep systematic samples at least the chosen distance apart:

-   For a stratified design, leave the field empty to use twice the stratification pixel size. An entered value must be at least this large.
-   For an unstratified design, leave the field empty to apply no additional minimum-distance constraint.

.. thumbnail:: ../_images/cookbook/sampling_design/arrangement.png
    :group: sampling-design-recipe
    :title: Systematic arrangement using the closest sample count and a randomized grid start
    :width: 50%

A larger minimum distance can reduce the number of locations available in small or fragmented strata.

Export
------

.. important::

    Some sampling designs use temporary Earth Engine table assets before producing the final output. When temporary assets are required, the design needs a linked Earth Engine account with an asset root and sufficient asset quota, even when the final result is exported to the SEPAL workspace. Without a linked account, SEPAL can use its service account only for designs that do not require temporary assets, and the result can be exported only to the SEPAL workspace. See :doc:`../setup/gee` for information about linking an Earth Engine account and configuring an asset root.

The retrieve button remains disabled until the design is ready to export, including any linked-account and asset-root requirements. Hover over it to view the first unresolved problem.

Select :btn:`<fa-solid fa-cloud-arrow-down>` to open the **Retrieve** panel.

Choose a destination
^^^^^^^^^^^^^^^^^^^^

-   **GEE asset**: available when an Earth Engine account is linked. Export an Earth Engine table asset and enter the asset ID and sharing or overwrite settings.
-   **SEPAL workspace**: available with a linked account or, for designs that do not require temporary assets, with the SEPAL service account. Export a file in CSV, GeoJSON, KML, KMZ or Shapefile format.

Select **Retrieve** to start the export task.

When too few sample locations are found
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An allocation can pass the panel checks but still request more eligible locations than a stratum can supply. A stratum may be very small, fragmented or mostly masked, or systematic spacing may leave too few grid locations.

During export, SEPAL checks whether it can produce the count allocated to each stratum. If it cannot, the task stops and no output is published. **Closest** is the exception: it may accept the nearest available count above or below the allocation when the minimum requirement is met.

To inspect a sampling shortage:

1.  Open **Tasks** in the lower-left corner.
2.  Select the failed task to open **Task Details**.
3.  Read the **Progress** section.
4.  Review the affected strata, the number of locations found, the missed requirement and the suggestions for the current configuration.

Use the configuration-aware suggestions in **Progress** to revise the sample allocation, arrangement, stratification or AOI. Every stratum must still receive at least two locations, or the higher minimum set with **Min samples/stratum**.

If Earth Engine times out or runs out of memory, the failure is not a sampling shortage. To reduce the workload, use a stored GEE image asset instead of processing a source **Recipe**. If a stratification or anticipated-proportion calculation failed, use a coarser (larger) **Scale** in that panel. If the sample export failed, reducing the allocated sample counts may help. After any change, confirm that the sampling design still supports the study objective.

Output
------

Every output feature is a point with a sample identifier and stratum value.

GEE table asset
^^^^^^^^^^^^^^^

Each sample point in a GEE table asset includes these core properties:

-   :code:`id`: sample identifier;
-   :code:`stratum`: numeric stratum value.

The table asset stores the allocation, final counts, labels and colours as collection-level metadata. When you add an exported Sampling Design GEE table asset to a recipe map, SEPAL reads the :code:`stratum_class_values`, :code:`stratum_class_palette` and :code:`stratum_class_names` properties and uses them to style the points by stratum.

View the exported points
""""""""""""""""""""""""

After the GEE table export is complete:

1.  Open the :btn:`<fa-solid fa-layer-group>` **Layers** panel from the map toolbar.
2.  Select **Add** > **Add an Earth Engine asset**.
3.  Select the exported table asset.
4.  Add the asset and enable its feature layer for the required map area.

Open **Layer options** to adjust the styling or filter the displayed features.

A sample near a class boundary can appear to sit in the neighbouring class. Maps are drawn in the Web Mercator projection, which is rarely the projection a stratification is stored in, so the classes are redrawn onto the map's own grid before they are displayed. Near a boundary the class drawn under a point can differ from the one recorded for it. The sample location itself is exact, and the stratum recorded for it is the class found at that location when the design was created.

Zooming in reduces the effect but does not remove it. If samples appear clearly misplaced rather than marginally, the Scale may be coarser than the detail in the source image. See `Grids and projections`_.

SEPAL workspace file
^^^^^^^^^^^^^^^^^^^^

Workspace exports repeat design information on each row. Important fields include:

.. list-table:: Workspace output fields
    :header-rows: 1
    :widths: 28 72

    * - Field
      - Description
    * - :code:`id`
      - Sample identifier.
    * - :code:`stratum`, :code:`label`, :code:`color`
      - Stratum value and display information.
    * - :code:`stratumArea`, :code:`totalArea`
      - Mapped areas in square metres.
    * - :code:`stratumWeight`
      - Stratum area divided by total mapped area.
    * - :code:`requestedSampleSize`, :code:`actualSampleSize`
      - Planned and exported counts for the stratum.
    * - :code:`sampleExpansionArea`
      - Stratum area divided by the actual number of exported samples.
    * - :code:`sampleWeight`
      - Stratum weight divided by the actual number of exported samples.
    * - :code:`.geo`
      - Point geometry in formats that support this Earth Engine export field.

The :code:`sampleExpansionArea` and :code:`sampleWeight` fields are convenience values derived from the mapped stratum area or weight and the actual exported count: :code:`sampleExpansionArea` is :code:`stratumArea` divided by :code:`actualSampleSize`, and :code:`sampleWeight` is :code:`stratumWeight` divided by :code:`actualSampleSize`. These fields do not prescribe how final results should be calculated.

Retain :code:`actualSampleSize` as the final exported count when it differs from the requested count.

Grids and projections
---------------------

These settings are advanced. The defaults suit most designs, and a sampling design can be completed without changing them.

SEPAL performs its calculations on a grid of pixels. A grid is defined by a projection, which describes how the curved Earth is represented on a flat map, and a pixel size in metres.

Sampling Design uses two grids for different purposes:

-   The **stratification grid** determines how the stratification is read. It decides which stratum each location belongs to, the area and weight of each stratum, and the anticipated proportions. Set it with the **CRS** and **Scale** fields in the **Stratification** panel.
-   The **sample placement grid** determines where samples can be placed. Set its **CRS** in the **Sample Arrangement** panel.

The stratification grid
^^^^^^^^^^^^^^^^^^^^^^^

When the stratification is a single GEE image asset, SEPAL reads the image on its own grid. **CRS** shows the image's projection, and **Scale** is left empty with the image's pixel size shown in its place. Nothing is redrawn, so each sample records the class that the source image holds at that location.

Enter a **Scale** to read the stratification at a different resolution. A coarser value processes fewer pixels and calculates faster, but the strata are redrawn onto a grid at that resolution: boundaries between strata can shift slightly, and a location near a boundary may be assigned to a neighbouring stratum. Clear the field to return to the image's own grid.

Changing **CRS** also redraws the strata, because the image's own grid applies only in its own projection. Leave **Scale** blank to keep the detected pixel size, or enter a value to change the resolution too.

SEPAL also tries to detect a grid for image collections and **Recipe** sources. When a grid can be detected, blank fields use it. When it cannot, blank fields use the defaults shown in the form. Enter a **CRS** or **Scale** only when the design needs a different grid.

Stratum areas are measured in true square metres whichever grid is used, so areas and weights remain correct.

The sample placement grid
^^^^^^^^^^^^^^^^^^^^^^^^^

The available projections are equal-area, where every pixel covers the same amount of ground. This prevents some parts of the area of interest from containing more possible sample locations per square kilometre than others. The chosen arrangement and grid start still determine how locations are selected.

-   **EPSG:6933 — EASE-Grid 2.0 Global**: the default, suitable for most areas.
-   **EPSG:6931 — EASE-Grid 2.0 North**: for areas above roughly 60° north.
-   **EPSG:6932 — EASE-Grid 2.0 South**: for areas below roughly 60° south.

The global grid gives every pixel the same area at any latitude, but shapes and spacing become increasingly distorted towards the poles. The polar grids reduce this distortion and provide more even spacing there. What matters is how far north or south the area lies, not how large it is.

Changing this projection moves the sample locations. It does not change the calculated stratum areas or weights.

An unstratified random design places samples directly within the area of interest and does not use this grid.
