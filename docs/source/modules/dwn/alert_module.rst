Alert analysis module
=====================
*Monitor forest cover loss alerts in an area of interest, period after period*

.. labels-ok: Apps; Map; Alert analysis module

**Alert analysis module** is a SEPAL app for monitoring forest cover loss in an area of interest (AOI). The app:

-   downloads the Global Land Analysis and Discovery (GLAD) alerts GLAD-L and GLAD-S2 and the Radar for Detecting Deforestation (RADD) alerts from Google Earth Engine (GEE), and your own alert sources if you have them;
-   aligns them on one grid;
-   groups touching alert pixels into alerts, each listing every source that flagged it; and
-   lets you review the alerts one by one on *before* and *after* satellite images.

For each alert, confirm or reject it, answer your own questions about it, and redraw its polygon by hand or with two neural-network models. The review can be split among several evaluators. The results come out as GeoPackage files, comma-separated values (CSV) tables, Word reports and animated GIF images.

This article is for forest-monitoring analysts who use SEPAL. It describes each step of the app, in the order of use, and ends with a worked example.

.. _defo-workflow:

Workflow at a glance
--------------------

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/anim/workflow.gif
    :alt: The two workflow levels: the Prepare alerts steps, from the area of interest to the alert set, then the Set up review steps, locked until that set exists

The **Workflow** panel holds the steps in two levels: **Prepare alerts** builds an alert set, and **Set up review** prepares its review. The other tools open from the left rail (see `The app window <defo-window_>`_).

.. list-table::
    :header-rows: 1
    :widths: 20 30 50

    *   -   Level
        -   Subsection
        -   Purpose
    *   -   –
        -   `Project <defo-project_>`_
        -   Create, open, import or delete a project, the folder that holds all your work.
    *   -   **Prepare alerts**
        -   `Area of interest <defo-aoi_>`_
        -   Choose the area to monitor.
    *   -
        -   `Monitoring period <defo-period_>`_
        -   Set the dates of a monitoring round.
    *   -
        -   `Alert sources <defo-alerts_>`_
        -   Choose the alert datasets of the period and download them.
    *   -
        -   `Harmonize <defo-harmonize_>`_
        -   Align the downloads on one grid and apply the masks.
    *   -
        -   `Integrate & vectorize <defo-integrate_>`_
        -   Combine the sources into an alert set, one polygon per alert.
    *   -   **Set up review**
        -   `Additional layers <defo-layers_>`_ (optional)
        -   Add reference layers to judge the alerts by.
    *   -
        -   `Questionnaire <defo-questionnaire_>`_ (optional)
        -   Write the questions asked for every alert, and choose the report template.
    *   -
        -   `Evaluation <defo-evaluation_>`_
        -   Review alone, or split the alerts among evaluators.
    *   -   –
        -   `Analysis <defo-analysis_>`_
        -   Review each alert on before and after images.
    *   -   –
        -   `Overview <defo-overview_>`_
        -   View the figures of an alert set.
    *   -   –
        -   `Export <defo-export_>`_
        -   Export the files of one alert, or the alerts of a whole set.

**Set up review** stays locked until the project has an alert set: build one in **Prepare alerts** first.

For a worked example from start to finish, see `Use case: alert review in Madre de Dios, Peru <defo-use-case_>`_.

.. _defo-setup:

Set up
------

Requirements:

-   a SEPAL account;
-   a GEE account connected to SEPAL; and
-   for the *Planet* images of the Analysis timeline, access to the Planet NICFI (Norway's International Climate and Forest Initiative) tropical mosaics in GEE.

To start the app, go to the SEPAL **Apps** dashboard and select **Alert analysis module**.

The app runs in your SEPAL session and keeps your projects in your SEPAL home, under ``module_results/deforestation_alerts/``.

.. note::

    The launching process can take several minutes.

.. _defo-window:

The app window
^^^^^^^^^^^^^^

The map fills the window. The **Workflow** panel on the right side holds the steps. A narrow rail of icons runs down the left side.

The header of the **Workflow** panel stays in view while the step under it scrolls:

-   One title row shows the step's position among all the steps (e.g. "3 / 8"), its name and what it holds ("3 sources"). An optional step that is still empty shows no count. The arrows on each side go to the step before or after.
-   Select the name to open the list of steps, grouped under the two levels, **Prepare alerts** and **Set up review**. Each step has a numbered dot: filled when the step has outputs (an AOI, periods, sources…), a grey ring when it is still empty. The two optional steps, **Additional layers** and **Questionnaire**, have a dashed dot. A locked step is greyed out and says why (e.g. "Build an alert set first."). A level's name gets a check mark once its last required step has outputs. Select a step to open it.
-   Under the name, one line says what to do in the step (e.g. "Set the monitoring period."). The information button at the right side of that line opens the step's help.

At the bottom of the panel, **Back** and **Next** go to the step before or after, skipping locked steps. Hover over one to see the name of the step it opens.

To use the left rail:

-   Hover over an icon to view its name.
-   Select the arrow on the edge of the rail to expand it and show the names. Select its pin to keep it expanded. An expanded rail that is not pinned folds back when you click on the map, on the main screen as on the Analysis maps.

.. note::

    While a dialog is open, the rail does not respond. Close the dialog with its cross first.

From top to bottom, the rail holds:

-   **Map**: shows the map with no dialog over it;
-   **About**: a short description of the app (the sources it downloads, how the alerts are reviewed and exported, and where your projects are saved);
-   **Project**: opens the `Project <defo-project_>`_ dialog;
-   **Analysis**: opens the `Analysis <defo-analysis_>`_ screen; and
-   **Overview**: opens the `Overview <defo-overview_>`_ dialog.

At the bottom of the rail are three links to the app's GitHub repository (its source code, its documentation and a form to report a bug), then two buttons:

-   The theme button switches, at each click, between the dark theme (moon icon), the light theme (sun icon) and an automatic theme that follows your system's setting.
-   The language selector shows the code of the current language. Select it to choose English, Spanish, French or Portuguese. The app's labels change at once. At first, the app follows the browser's language when it is one of these four, and English otherwise.

The browser remembers the theme and the language for the next session.

.. _defo-project:

Project
-------

All work happens inside a *project*: one AOI, its alert sources, its monitoring periods and every alert set built from them. A project is a folder in your SEPAL home. The app saves it automatically after every change: there is no **Save** button.

Use the **Project** dialog to create, open, import, copy and delete projects. It opens by itself when the app starts. Afterwards, select **Project** in the left rail.

When no project is open
^^^^^^^^^^^^^^^^^^^^^^^

.. shot: project-empty | The Project dialog right after the app starts, with no project open: the "Continue where you left off" card for the demo project (name, count chips, AOI, "modified … ago", Continue button), then the three buttons New project / Manage projects (n) / Import. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/project-empty.png
    :alt: The Project dialog with no project open

With saved projects, the dialog offers the one changed last under **Continue where you left off**, with its counts, its AOI and when it was changed: select **Continue** to open it. With no saved project, it reads **No project open**. Below are three buttons:

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Button
        -   Description
    *   -   **New project**
        -   Asks for a name and creates an empty project.
    *   -   **Manage projects**
        -   Lists the projects saved in your SEPAL folder, to open or delete one. The button shows how many there are and is disabled while there are none.
    *   -   **Import**
        -   Imports a review package made by a colleague (see `Import a review package <defo-project-import_>`_).

.. tip::

    Creating a project first is not required. Go straight to the `AOI <defo-aoi_>`_ step and select an area: the app creates a project named after the area and today's date (e.g. ``PER_Madre_De_Dios_20261019``).

When a project is open
^^^^^^^^^^^^^^^^^^^^^^

.. shot: project-open | The Project dialog with the demo project open: a tinted card with the project name in bold, the green "saved" chip and the pencil and copy icons, the count chips, the AOI "PER_Madre_De_Dios" and "Saved … ago"; then the buttons New project / Manage projects (n) / Import. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/project-open.png
    :alt: The Project dialog with a project open

The dialog shows:

-   the project's name with a chip: **saved** once the project is on disk, or **save failed** in red when the last automatic save did not work (a line below gives the reason; the changes are still in the app, so fix the cause, usually a full disk, before closing the browser tab);
-   a summary: the AOI (or "no AOI yet") and the number of sources, periods and alert sets; and
-   when the project was last saved (e.g. "Saved 3 minutes ago").

The pencil icon next to the name renames the project and the copy icon duplicates it. The buttons below are the same as when no project is open: **New project**, **Manage projects** and **Import**.

.. _defo-project-create:

Create a project
^^^^^^^^^^^^^^^^

.. shot: project-new | The "New project" name form open over the Project dialog, with "Madre de Dios 2026" typed in the Project name field and the Create button enabled. Crop to the form.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/project-new.png
    :alt: The New project form

To create a project:

1.  Select **New project**.
2.  Enter a name in the **Project name** field.
3.  Select **Create** (or press **Enter**).

The **Project name** accepts letters, digits, spaces, hyphens (``-``) and underscores (``_``) only. It must not be empty and must differ from every project folder already in your SEPAL folder (ignoring upper and lower case).

The name is checked while you type. If it matches a saved project, the form offers a link such as **Open Madre de Dios 2026 instead**.

The new project opens on the `AOI <defo-aoi_>`_ step, always the first step of the workflow.

Open, search and delete projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. shot: project-manage | The "Manage projects" dialog with three saved projects and a version 1 recipe (recipe_2026-08-12-101500, its outlined "version 1" chip first, its pencil greyed) listed, the demo project selected and marked with the outlined "open" chip, each row showing its count chips (sources, periods, alert sets), its AOI and "modified … ago", and on the right its size, a pencil and a red bin, the Search projects field empty, the Open button enabled. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/project-manage.png
    :alt: The Manage projects dialog

**Manage projects** lists every saved project with:

-   small chips for its number of sources, periods and alert sets (the alert-set chip is coloured when the project has results to review);
-   its AOI (or "no AOI yet") and when it was last changed (e.g. "modified 2 days ago");
-   its size on disk, measured when the dialog opens; and
-   an **open** chip on the project that is open now.

A recipe saved with the previous version of the app is listed too, with a **version 1** chip (see `Open a version 1 recipe <defo-project-v1_>`_).

To open a project:

1.  Enter text in the **Search projects** field to keep only the projects whose name contains it.
2.  Select a project.
3.  Select **Open**.

To rename a project:

1.  Select the pencil icon on its row (or next to the name of the open project).
2.  Enter the new name. It follows the same rules as a new project's name.
3.  Select **Rename**.

A project cannot be renamed while a task is still writing into it.

To delete a project:

1.  Select the red bin icon on its row. The confirmation dialog shows the size of the project folder.
2.  Enter the project's name exactly in the confirmation field.
3.  Select **Delete**.

.. attention::

    Deleting removes the whole project folder: downloads, alert sets, reviews and reports. It cannot be undone.

    -   Deleting the open project closes it first.
    -   A project cannot be deleted while a task (a download, an **Integrate & vectorize** run or a review save) is still writing into it. Wait for the task to end.

.. _defo-project-duplicate:

Duplicate a project
^^^^^^^^^^^^^^^^^^^

**Duplicate** copies the open project under a new name. The copy keeps the AOI, sources, masks, layers and grid, the look-back and the report template, without periods or alert sets. The copy opens on its AOI step.

Use it to:

-   start a new monitoring round from the same setup; or
-   monitor another area once the AOI of a project is locked (see `Area of interest <defo-aoi_>`_).

**Duplicate** is not offered for a review copy.

.. _defo-project-import:

Import a review package
^^^^^^^^^^^^^^^^^^^^^^^

When a project's creator splits the alerts among several evaluators (see `Evaluation <defo-evaluation_>`_), each evaluator receives a *review package*: one .zip file.

To work on a review package:

1.  Copy the .zip file into your SEPAL folder.
2.  In the **Project** dialog, select **Import**.
3.  In the **Import a review package** dialog, select the file in **Review package (.zip)**. The import starts as soon as the file is selected.

The package becomes a new project, a *review copy*, named after the original project and the evaluator (e.g. ``madre-de-dios__e01-ana``). It opens directly on the `Analysis <defo-analysis_>`_ screen, filtered to the alerts assigned to that evaluator. In a review copy the setup steps are locked, and a banner reads: "Review copy for (evaluator), from (project). Setup is locked."

If the same package was already imported, the **Already imported** dialog offers two options:

-   **Open existing copy**: opens the existing copy, with its reviews; or
-   **Import as new copy**: imports the package again as a separate project. The existing copy is never overwritten.

.. important::

    A *reviewed copy* (the file an evaluator sends back) cannot be imported here. The project's creator merges it in the `Evaluation <defo-evaluation_>`_ step of the original project.

.. _defo-project-v1:

Open a version 1 recipe
^^^^^^^^^^^^^^^^^^^^^^^

Recipes saved with the previous version of the app (version 1) stay in their folders under ``module_results/deforestation_alerts/``. **Manage projects** lists them among the projects, marked with a **version 1** chip. Hover over the chip to read: "Saved with the previous version. It is converted the first time you open it; the old files are kept."

To open a recipe, select it, then select **Open**, as for a project (or **Continue**, when the dialog offers it). The first time, the app converts it into a project in the same folder: the row reads "Converting (name)…" while the app gets the recipe's AOI (from GEE for an administrative area or an asset) and reads its alerts. The project then opens on the `Analysis <defo-analysis_>`_ screen, and the app confirms, e.g. "recipe_2026-08-12-101500 was converted from version 1. 5 of 40 alerts reviewed." Later opens skip the conversion.

The converted project keeps:

-   the recipe's period, sources and alerts;
-   every review: the status, the description, the drawn polygon, the area, the administrative names, the before and after images, and the alert the review stopped at; and
-   the recipe's mask and extra layer, as the additional layers ``v1 mask`` and ``v1 layer``, and its report template when the file is still there.

The alerts are drawn as rectangles (the boxes version 1 drew around them), with the polygon drawn in a review on top. They keep their version 1 numbers, which start at 0. An alert without a drawn polygon gets an area estimated from its number of alert pixels. When part of the recipe cannot be converted, a warning lists it once, after the conversion (e.g. "source CCDC: not imported as a source, kept in the alert set only").

A converted project is locked, and a banner reads: "This project comes from a version 1 recipe. Only additional layers can be changed; review, save and export work as usual." Its AOI, period, sources, Harmonize, Integrate & vectorize, questionnaire and report template cannot change, and it cannot be duplicated. The `Evaluation <defo-evaluation_>`_ step is not available: one person reviews the project. The `Additional layers <defo-layers_>`_ can be added, edited and deleted.

The recipe's own files (``recipe_parameters.json``, ``alert_db.csv`` and the files made for each alert) are never changed. A recipe cannot be renamed before it is converted: its pencil icon reads "Open it once to convert it first."

If the conversion fails, nothing is written, and the message gives the cause, e.g. "Could not get the area of interest: (error). The recipe was not changed."

Where the files are
^^^^^^^^^^^^^^^^^^^

Each project is a folder named after the project, under ``module_results/deforestation_alerts/`` in your SEPAL home:

.. list-table::
    :header-rows: 1
    :widths: 30 70

    *   -   Inside the project folder
        -   Content
    *   -   ``project.json``
        -   The project's settings and history. The app writes it on every save.
    *   -   ``aoi.geojson``
        -   The AOI, when it is a drawn shape or a vector file. An administrative area or a GEE asset is read from GEE instead.
    *   -   ``masks/``
        -   The masks of `Harmonize <defo-harmonize_>`_, aligned on the project's grid.
    *   -   ``imagery/``
        -   The index of satellite scenes used on the Analysis screen.
    *   -   ``periods/<start>_<end>/``
        -   One folder per monitoring period: ``raw/`` downloads, ``harmonized/`` rasters, and ``sets/`` with one folder per alert set.

.. note::

    Leave these files alone while the app is running. Use the app's `export <defo-export_>`_ tools to take results out.

.. _defo-aoi:

Area of interest
----------------

.. labels-ok: AOI selection method; Country/Province; Admin level 1; Admin level 2; Vector file; Drawn shapes; GEE Asset name; Select AOI; Select an AOI name; Select an asset; column; value; Use all features; Table file; id; latitude; longitude; Column; Value

The AOI is the area the project monitors:

-   every alert download is cut to it;
-   the coverage of each alert source is measured over it; and
-   the project's grid is built around it.

Open the **AOI** step, the first step of the **Workflow** panel. The step is always available, even with no project open.

.. shot: aoi-admin | The AOI step in the Workflow panel with AOI selection method = Admin level 1, Country/Province = Peru, Admin level 1 = "Madre De Dios" (as the list spells it), after Select AOI was pressed: the Madre de Dios outline is drawn on the main map, zoomed to it. Crop to the panel plus the map.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/aoi-admin.png
    :alt: Selecting Madre de Dios as an administrative area

Select the area
^^^^^^^^^^^^^^^

To select the AOI:

1.  Choose a method in the **AOI selection method** dropdown menu.
2.  Fill out its fields.
3.  Select **Select AOI**.

The area is drawn on the map and saved with the project at once.

.. shot: aoi-methods | The AOI step with the AOI selection method dropdown open, showing the two groups (Administrative definitions, Custom geometries) and the methods down to Drawn shapes (the list scrolls for the rest). Crop to the panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/aoi-methods.png
    :alt: The AOI selection methods

.. list-table::
    :header-rows: 1
    :widths: 20 40 40

    *   -   Method
        -   Input
        -   Notes
    *   -   **Country/Province**
        -   A country.
        -   Administrative boundaries come from the Food and Agriculture Organization of the United Nations (FAO) Global Administrative Unit Layers (GAUL) dataset.
    *   -   **Admin level 1**
        -   A country, then a first-level unit (a region, state or department).
        -   Each list fills in once the level above is chosen.
    *   -   **Admin level 2**
        -   A country, a first-level unit, then a second-level unit (a province or district).
        -
    *   -   **Vector file**
        -   A .shp, .geojson, .gpkg or .kml file in your SEPAL folder.
        -   Keep every feature, or choose a **column** and a **value** to keep only the matching features.
    *   -   **Drawn shapes**
        -   Shapes drawn on the map with the drawing tools that appear, and an optional name in **Select an AOI name**.
        -   All the drawn shapes together form the AOI. Without a name, it is called ``drawn_`` plus the date and time.
    *   -   **GEE Asset name**
        -   A GEE table (feature collection) or image you can read, chosen in **Select an asset** or pasted as its full ID.
        -   For a table, keep only the features whose **Column** has a given **Value**.

When the selection is done, the app confirms: "AOI saved: (name)". The **Workflow** panel shows the AOI's name in the header, and the `Period <defo-period_>`_ step unlocks.

.. tip::

    A national AOI works, but everything after it (downloads, the grid, vectorization) grows with the area. Start with a province or a district while learning the app.

What happens when an area is selected
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an area is selected:

-   If no project is open, a project is created and named after the AOI and today's date (e.g. ``PER_Madre_De_Dios_20261019``). An administrative area is named after the country's ISO code and the unit's name.
-   The coverage of every alert source over the new area is checked once and saved in the project. The `Alerts <defo-alerts_>`_ step shows it.
-   If the project already had a different AOI, every download, harmonized raster and mask made for the old area is deleted, because they were cut to it. The project's grid is reset, so that it is built again around the new area.

When the AOI is locked
^^^^^^^^^^^^^^^^^^^^^^

Once the project has an alert set, its AOI cannot change: a new area would invalidate every download and every alert footprint. The step then shows "This project already has alert sets, so its AOI is locked. Duplicate the project (Project dialog) to monitor another area." and the selector is disabled.

To monitor another area with the same sources, masks, layers and grid, select **Duplicate** in the `Project <defo-project-duplicate_>`_ dialog, then select the new area in the copy.

In a review copy (see `Import a review package <defo-project-import_>`_), the step shows only the AOI's name: the area is the one chosen by the project's creator.

.. important::

    The AOI cannot change while a task is writing into the project (a download or an **Integrate & vectorize** run). The app displays: "A job is writing into this project; change the AOI once it has finished." Wait for the task to end, then select the area again.

.. _defo-period:

Monitoring period
-----------------

A *period* is one monitoring round, usually a month. For each period, the app downloads the period's alert sources over its dates plus a *look-back* before them, and builds that period's alert sets. A project usually holds a series of consecutive periods.

Both dates of a period are included: a period from 1 to 31 January keeps the alerts dated on the 1st and on the 31st. The same holds for its search window.

Open the **Period** step of the **Workflow** panel. It unlocks once the project has an `AOI <defo-aoi_>`_.

.. shot: period-list | The Period step of the demo project with its one period listed: "start → end" in the Period column, the Sets count, the Status column, the period's radio selected (active), and the notes under it ("Search window: … → …", "No earlier set: every alert in the search window is kept", and "Its dates are fixed: it has alert sets." if it has a set). Crop to the Workflow panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/period-list.png
    :alt: The Period step with one period

.. _defo-period-tracking:

Loss that spans several periods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each period is processed on its own, but forest loss does not keep to the period's dates. Some loss could be missed between two periods:

-   a clearing that starts too small to be an alert;
-   alerts that the providers publish late, after their period was processed; or
-   a clearing that keeps growing at the edge of an alert reported in an earlier period.

The app tracks this loss from one period to the next, and never reports the same loss twice:

.. list-table::
    :header-rows: 1
    :widths: 35 65

    *   -   Case
        -   What the app does
    *   -   Loss already reported by an earlier period
        -   Its pixels (the *footprint* of the earlier alert set) are removed from the new period's run, so it is not reported again.
    *   -   A cluster too small to be an alert, or an alert published late
        -   The `look-back <defo-period-lookback_>`_ searches back into the earlier period: the pixels set aside come back and can join new pixels to form an alert.
    *   -   A clearing that grows next to a reviewed alert
        -   The new alert is `linked to the earlier alert <defo-period-growth_>`_ as a *growth alert*, and kept even when it is under the minimum size.

.. _defo-period-lookback:

The search window and the look-back
"""""""""""""""""""""""""""""""""""

A clearing often starts small and grows over the following weeks. In the period where it starts, its cluster of alert pixels is still smaller than the **Minimum cluster size** of `Integrate & vectorize <defo-integrate_>`_, so it does not become an alert: its pixels are set aside as *not analysable*.

The look-back keeps these pixels in play:

-   Each period searches a wider *search window*: its own dates plus the look-back days before its start.
-   The pixels set aside by the earlier period come back into the run and join the new pixels that touch them.
-   If the cluster they form together reaches the minimum size, it becomes an alert. Its first detection date is the date of its earliest pixel, in the earlier period.

To avoid reporting the same loss twice, every pixel already reported by an alert set of an *earlier* period is removed before the new period's alerts are built: only what was set aside comes back. The look-back also catches alerts that the providers published late, after the earlier period was processed.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/anim/lookback.gif
    :alt: The look-back: a cluster too small in one period joins the next period's pixels and becomes an alert, and a reported alert is never reported again

.. note::

    The first period has no earlier set to compare with, so every alert in its search window is kept. Its row reads **No earlier set: every alert in the search window is kept**. With a look-back, that includes alerts dated before the period's start.

    A new project's first period starts with no look-back, so it searches only its own dates unless a look-back is set. A project made with **Duplicate** keeps the look-back of the project it was copied from.

.. _defo-period-growth:

Growth next to earlier alerts
"""""""""""""""""""""""""""""

The pixels of a reported alert are part of the footprint, so the look-back does not bring them back. But a clearing often keeps growing at the edge of an alert reported in an earlier period. The new pixels then form a cluster of their own, often smaller than the **Minimum cluster size**, which would be set aside like any small cluster.

When the earlier alert was saved as **True alert** or **Needs revision**, `Integrate & vectorize <defo-integrate-growth_>`_ keeps this growth in view:

-   A new alert that touches the earlier alert, or lies within one pixel of the grid from it, is a *growth alert*, linked to it.
-   A cluster under the minimum size is kept when it touches the earlier alert: it is a growth alert *under the minimum area* (unless **Keep smaller clusters that touch earlier confirmed loss** is cleared). A small cluster that touches nothing is set aside, and the look-back can still bring it back in the next period.
-   The run looks for earlier alerts in every earlier period, whatever the look-back.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/anim/growth.gif
    :alt: Growth: a confirmed alert grows at its edge in the next period, and the small new cluster is kept and linked to it, while a small cluster that touches nothing is set aside

The alerts linked to each other, across all periods, make the *history* of a clearing. Analysis shows it on each alert (see `Earlier alerts <defo-analysis-earlier_>`_), and the `Overview <defo-overview-growth_>`_ sums it up.

.. tip::

    Only the reviews saved when `Integrate & vectorize <defo-integrate_>`_ starts count. Review the alerts of a period before you run the next one, so that their growth is linked. An alert reviewed later can still be linked by hand in `Earlier alerts <defo-analysis-earlier_>`_.

The period list
^^^^^^^^^^^^^^^

Each row of **Periods** shows:

.. list-table::
    :header-rows: 1
    :widths: 20 80

    *   -   Column
        -   Description
    *   -   **Period**
        -   The period's dates ("start → end"), with notes under them: its search window and any warnings.
    *   -   **Sets**
        -   The number of alert sets built for this period.
    *   -   **Status** column
        -   **out of date** when a source download or an alert set no longer matches the current settings (run it again in `Alerts <defo-alerts_>`_, `Harmonize <defo-harmonize_>`_ or `Integrate & vectorize <defo-integrate_>`_); **missing** when an alert set's files are gone; a dash when everything is current.

The icons on the right side of each row:

-   the radio button makes the period *active*: `Alerts <defo-alerts_>`_, `Harmonize <defo-harmonize_>`_ and `Integrate & vectorize <defo-integrate_>`_ work on the active period;
-   the pencil icon changes its dates or look-back; and
-   the bin icon deletes the period.

.. _defo-period-add:

Add a period
^^^^^^^^^^^^

.. shot: period-new | The "New period" dialog pre-filled for a second period: Start = the day after the demo period's end, End = today, Look-back (days) = 90 (the last value used, the demo period's) with its hint, the "Search window: … → …" preview line and the masks note, Add period enabled. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/period-new.png
    :alt: The New period dialog

Select **New period**. The dialog is pre-filled so that the new period continues the series.

.. list-table::
    :header-rows: 1
    :widths: 20 35 45

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **Start**
        -   The first day of the period.
        -   The day after the latest period ends. For the first period, the first day of the current month.
    *   -   **End**
        -   The last day of the period.
        -   Today. Must be after **Start**. Two periods cannot have the same dates.
    *   -   **Look-back (days)**
        -   The number of days before **Start** that are also searched.
        -   0 (no look-back) for a new project's first period (a duplicated project keeps the look-back of its source), then the last value used. A whole number from 0 to 3650.

Under the fields, the dialog previews the search window ("Search window: start → end"). Select **Add period**: the period is created and becomes the active period.

A new period starts with the mask choices of the latest period. Change them in `Harmonize <defo-harmonize_>`_. Its alert sources are the ones marked **Add to new periods** in `Alerts <defo-alerts-new-periods_>`_; add or remove sources there.

.. tip::

    For the set-aside clusters to come back, the look-back must reach into the previous period. With a look-back of 0, the search window starts on the period's own first day and nothing set aside earlier is reconsidered.

    A cluster that stays too small stays in play in later periods for as long as their look-back reaches back to its pixels. A longer look-back gives a slowly growing clearing more time to reach the minimum size, but makes every download bigger (see `What earlier periods already reported <defo-integrate-earlier_>`_).

Change a period
^^^^^^^^^^^^^^^

For a period without alert sets, the pencil icon opens a dialog to change its dates. New dates give the period a new identity: its downloads and harmonized files are deleted, because they were made for the old window.

A period with alert sets has fixed dates (its note reads **Its dates are fixed: it has alert sets.**). The pencil icon then opens a dialog where only the look-back can change. The period's downloads then show as out of date.

Delete a period
^^^^^^^^^^^^^^^

Select the bin icon. The confirmation dialog lists what is deleted: the period's downloads and harmonized files, and its alert sets with their reviewed alerts.

.. important::

    A period with alert sets can be deleted only when it is the latest period. An earlier period's sets are the footprint the later sets were built from, so delete the later periods first. Periods cannot change or be deleted while a task is writing into the project.

.. _defo-alerts:

Alert sources
-------------

An *alert source* is a dataset of forest-loss alerts. Each alert pixel is *confirmed* (high confidence) or *probable* (low confidence) and carries the day it was first detected.

The **Alerts** step lists the sources of the active `period <defo-period_>`_, shows how much of the AOI and of the period each one covers, and downloads them. Each period has its own sources: a source added here is added to the active period only.

Open the **Alerts** step of the **Workflow** panel. It unlocks once the project has a `period <defo-period_>`_. It works on the active period: to work on another period, make it active in the `Period <defo-period_>`_ step first. The box at the top of the step names the period and its search window, e.g. "Period 2026-09-01 → 2026-09-30 · search window from 2026-06-03 (90 days of look-back)".

.. shot: alerts-list | The Alerts step of the demo project: the period box ("Period 2026-09-01 → 2026-09-30 · search window from 2026-06-03 (90 days of look-back)"), Add source, and the Sources table with GLAD-L, RADD and GLAD-S2, each with its "downloaded … · … MB" line, its green "AOI 100 %" and "✓ data to …" chips, the green "Downloaded" status and the map / Details / Download again / Remove from this period icons; the RADD info note. Crop to the Workflow panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/alerts-list.png
    :alt: The Alerts step with three downloaded sources

The source list
^^^^^^^^^^^^^^^

Each row of **Sources** shows:

.. list-table::
    :header-rows: 1
    :widths: 20 80

    *   -   Part of the row
        -   Description
    *   -   **Source**
        -   The source's name, then a line with what the row holds ("downloaded 2026-10-20 · 4.7 MB") or why it needs a download (e.g. "the search window changed (…): download again"), and two chips:

            -   **AOI**: the share of the AOI inside the source's footprint, e.g. "AOI 100 %". A source that covers only part of the AOI gets no alerts over the rest of it.
            -   The dates: "✓ data to 2026-10-30" (green) when the source has data up to the end of the search window, "data to … only" (orange) when its data stop inside the window, or "✗ data ends …" (red) when it has none in the window.

            A points or polygons source has one chip instead, "clipped to the AOI": its coverage is not checked.
    *   -   **Status**
        -   The row's state, or a button to download it (see `Download the sources <defo-alerts-download_>`_).
    *   -   Map icon
        -   Shows the source on the map: the alerts of the active period's search window. A GeoTIFF source is shown only once it is harmonized. A points or polygons source shows its features as read from the file, once its row is read (see `Points or polygons file <defo-alerts-vector_>`_).
    *   -   Information icon
        -   Opens the source's **Details** (see `The Details dialog <defo-harmonize-details_>`_), with the **Add to new periods** checkbox and, for a custom source, the **Edit** button.
    *   -   **Download again**
        -   Downloads the source again (see below).
    *   -   **Remove from this period**
        -   Removes the source from the active period (see `Remove a source from a period <defo-alerts-remove_>`_).

The coverage is checked once, when the AOI is chosen, and saved in the project. If the check failed (e.g. GEE was not reachable), a **Check again** button appears under the list.

Add a source
^^^^^^^^^^^^

Select **Add source** to open the **Add an alert source** dialog, then choose the **Source type**:

-   **Predefined or project source**: one of the catalogue sources, or a source of the project that is not in this period (e.g. one used in an earlier period); or
-   **Custom (0 of 6)**: your own GEE image, image collection or GeoTIFF, or a file of dated points or polygons. The count shows how many of the period's six custom slots are in use.

A period holds at most three predefined and six custom sources. The project keeps every source it has used, with no limit.

.. _defo-alerts-new-periods:

Under the source, the **Add to new periods** checkbox (selected by default) decides whether the periods created later start with this source. It never changes the existing periods. To change it later, open the source's **Details** with its information icon.

Predefined sources
""""""""""""""""""

.. shot: alerts-add-predefined | The "Add an alert source" dialog with Source type = Predefined or project source and the Alert source list open, showing each source followed by its coverage (e.g. "GLAD-S2 (Sentinel-2, 10 m) — covers the AOI"), and the Add to new periods checkbox. Use a project with one period where only GLAD-L is added, so RADD and GLAD-S2 are still offered. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/alerts-add-predefined.png
    :alt: Adding a predefined source

Choose a source in the **Alert source** dropdown menu, then select **Add source**. The list holds the predefined sources and the project's own sources that are not in this period yet. Each entry shows its coverage of the AOI. A source that does not cover the AOI at all is listed as disabled, with the reason.

.. list-table::
    :header-rows: 1
    :widths: 25 30 45

    *   -   Source
        -   Sensor and pixel size
        -   Coverage
    *   -   **GLAD-L (Landsat, 30 m)**
        -   Landsat, about 30 m.
        -   The land of its four regional tiles (Asia, Africa, Central and South America), between about 35°S and 35°N.
    *   -   **RADD (Sentinel-1, 10 m)**
        -   Sentinel-1 radar, 10 m. Sees through clouds.
        -   The humid tropics of Africa, Southeast Asia, and Central and South America. It detects only in primary humid tropical forest; elsewhere in its area, it reports no alerts.
    *   -   **GLAD-S2 (Sentinel-2, 10 m)**
        -   Sentinel-2, 10 m.
        -   90°W–30°W, 20°S–20°N.

When every source is in the period, the dialog reads: "Every source is already in this period."

Custom sources
""""""""""""""

.. shot: alerts-add-custom | The "Add an alert source" dialog with Source type = Custom (0 of 6), the Name suggested from the asset, Source = Earth Engine, a RADD image asset picked; under it, once the bands are read, Alert format = "RADD (suggested)" with its help line, Alert band and Date band filled in, the Date band's hint naming the suggested band. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/alerts-add-custom.png
    :alt: Adding a custom source from an Earth Engine asset

A custom source reads your own alert raster through one of four format presets. The form reads from top to bottom: the name, where the raster comes from, the raster itself, then its bands. The bands are read as soon as the raster is chosen ("Reading the bands…"), and the fields that depend on them appear only once they are read.

.. list-table::
    :header-rows: 1
    :widths: 20 40 40

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **Name**
        -   The source's name in lists, legends and file names.
        -   Suggested from the asset or file name. At most 24 characters, at least one letter or digit, unique in the project. GLAD-L, RADD and GLAD-S2 are reserved.
    *   -   **Source**
        -   Where the raster is read from: **Earth Engine** (an asset) or **GeoTIFF / VRT** (a file in your SEPAL folder: a GeoTIFF, or a VRT, a GDAL virtual raster read like the GeoTIFFs it points to). The third choice, **Points or polygons file (CSV, GPKG, SHP)**, is not a raster (see `Points or polygons file <defo-alerts-vector_>`_).
        -   **Earth Engine**.
    *   -   Asset or **GeoTIFF / VRT**
        -   The GEE image or image collection, or the .tif file.
        -   An image collection is used whole, the newest image on top. For a collection of weekly snapshots (like RADD's own), give the latest image's ID instead. The GeoTIFF needs a coordinate reference system.
    *   -   **Alert format**
        -   How the bands are read (see below). Shown when the raster has two bands or more. A raster with one band has no format to choose: the form reads "One band (…): read as the alert date." and the source is read as **Date only**.
        -   Suggested from the band names when the app recognizes them, and marked "(suggested)".
    *   -   **Alert band**
        -   The band holding the alert class.
        -   Only for **RADD**, **SEPAL CCDC alerts** and **SEPAL PyEO alerts**. Starts on the band the format expects; when the raster has no such band, the hint reads "Pick the band that holds the alert level."
    *   -   **Date band**
        -   The band holding the detection date.
        -   Always required. Starts on the band the format expects, and its hint names it (e.g. "3 bands. Date looks like the alert date."), or asks you to pick it.
    *   -   **Date encoding**
        -   How the date is written: **yymm (year and month; the alert is dated on the 1st)**, **yyddd (year and day of year)**, **yyyyddd (year and day of year)** or **decimal year**.
        -   Only for **Date only**. Suggested from the date band's values (see below).

For a **Date only** source, the app reads the lowest and highest values of the date band over the AOI ("Reading the date values…") and suggests the encoding they fit, for example "Values from 24001 to 24366: they read as yyddd." Check the suggestion: the app reads only the two ends of the range. When the values do not look like dates ("… don't look like dates. Check the Date band."), or when no pixel over the AOI has a date ("No dated pixel over the AOI: pick the encoding."), choose the encoding yourself.

The four formats:

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Alert format
        -   How a pixel becomes an alert
    *   -   **RADD**
        -   Alert band: 2 is probable, 3 is confirmed. Date band in ``yyddd``.
    *   -   **SEPAL CCDC alerts**
        -   Continuous Change Detection and Classification (CCDC) outputs. ``detection_count``: one or two detections are probable, three or more are confirmed. ``first_detection_date`` in fractional years.
    *   -   **SEPAL PyEO alerts**
        -   Outputs of the Python for Earth Observation (PyEO) change detection, read like CCDC. ``total_changes``: one or two changes are probable, three or more are confirmed. ``first_change_date_above_threshold`` in fractional years.
    *   -   **Date only**
        -   One date band in the chosen encoding. Every dated pixel is a confirmed alert.

When **Add source** is selected, the app checks the raster: the bands exist and are numeric, the dates can be read and the source covers the AOI. A problem is shown in red inside the dialog, which stays open for corrections. While the check runs, the button reads **Cancel** and stops it.

.. _defo-alerts-vector:

Points or polygons file
"""""""""""""""""""""""

.. shot: alerts-add-vector | The "Add an alert source" dialog with Source type = Custom (0 of 6), Source = Points or polygons file (CSV, GPKG, SHP), the capture's points CSV (_fixtures/field_alerts.csv) picked in Vector file, Name suggested from it; under it Longitude column = lon, Latitude column = lat, Date column = date, Dates are written = Day first (dd/mm/yyyy), Square side (m) = 30 with its hint, and the summary line "Dates read as day/month/year · 12 points, 0 polygons · … → … · 0 skipped". Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/alerts-add-vector.png
    :alt: Adding a custom source from a file of points

A custom source can also be a file of dated points or polygons, such as alerts reported from the field or by another system. Choose **Points or polygons file (CSV, GPKG, SHP)** in **Source**, then pick the file in **Vector file**: a .csv table, a GeoPackage (.gpkg) or a Shapefile (.shp, with its .shx and .dbf files next to it). The file is read at once ("Reading the file…"), and the fields that depend on it appear:

.. list-table::
    :header-rows: 1
    :widths: 20 40 40

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **Layer**
        -   The GeoPackage layer to read.
        -   Only for a GeoPackage with several layers. Starts on the first one.
    *   -   **Longitude column** and **Latitude column**
        -   The columns holding the coordinates of each point, in degrees (WGS84).
        -   Only for a CSV. Suggested from the column names (e.g. ``lon``, ``latitude``).
    *   -   **Date column**
        -   The column holding the date of each alert.
        -   Suggested from the column names (e.g. ``date``, ``fecha``).
    *   -   **Dates are written**
        -   **Day first (dd/mm/yyyy)** or **Month first (mm/dd/yyyy)**.
        -   Only when the dates read either way (e.g. 03/04/2026).
    *   -   **Square side (m)**
        -   Each point becomes a square of this side, centred on the point.
        -   Only when the file has points. 30 m by default.

A line under the fields sums up what is read, for example "Dates read as day/month/year · 12 points, 0 polygons · 2026-06-12 → 2026-09-11 · 0 skipped". Rows without a point or polygon, or without a date, are skipped.

How the file is read:

-   A CSV's columns can be separated by commas, semicolons or tabs. With semicolons, decimal commas are read too.
-   A GeoPackage or a Shapefile needs a coordinate system, which can be any one.
-   A date can be a date field, year-month-day (``2026-09-14``), ``yyyymmdd`` (``20260914``) or day and month in either order (``14/09/2026``).
-   Every point or polygon is a confirmed alert. A polygon keeps its shape; a polygon or a square smaller than a pixel still gives one pixel.
-   Where features overlap, the earliest date is kept.

The source needs no GEE: its coverage is not checked, and only the features inside the AOI become alert pixels. Its row in `Alerts <defo-alerts-download_>`_ reads the features of the period's search window (**Read file**); its map icon then shows them as read, points as dots and polygons as outlines. `Harmonize <defo-harmonize_>`_ turns them into alert pixels on the project grid, and its map icon shows that raster, to compare with the features.

**Read file** reads the file again when it was edited after the source was added. If the edit no longer fits the source (for example, a chosen column is gone, or the dates now read in the other day/month order), the row shows "The alert file changed since it was added. Edit the source to check it again."

Edit a custom source
""""""""""""""""""""

Open the source's **Details** with its information icon, then select **Edit** to reopen the form, titled with the source's name. The name is fixed; the raster, format and bands can change. The form keeps the saved format and bands until another raster is chosen.

Once an alert set uses the source, it can no longer be edited: remove it and add a new one.

.. _defo-alerts-download:

Download the sources
^^^^^^^^^^^^^^^^^^^^

Each source is downloaded over the period's search window, in its own projection and cut to the AOI. A GeoTIFF source is not downloaded: it is read from its file. What this guide says of a GeoTIFF source holds for a points or polygons source too; the line under its name reads "Points/polygons file". Downloading does not harmonize the source: that is the next step, `Harmonize <defo-harmonize_>`_, which runs only when you start it there.

The **Status** column reads:

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Status
        -   Meaning
    *   -   "Downloaded"
        -   Downloaded for the current search window. The line under the name gives the download date and the size on disk.
    *   -   **Download**
        -   The source is not downloaded for this period's search window yet, or its download is out of date. Select the button to download it.
    *   -   **Read file**
        -   The same for a GeoTIFF source, which is read from its file.
    *   -   **Retry**
        -   The last download failed. Its error is shown in red under the row.
    *   -   "Downloading 42%", "Reading", "Queued"
        -   The row is running, or waits for its turn ("waiting for the row above").
    *   -   "not covered", "no data"
        -   The source cannot run for this period: it does not cover the AOI, or it has no data for the search window (its dates chip is red).
    *   -   "File missing"
        -   The file of a GeoTIFF source is gone (see `Common messages <defo-harmonize-messages_>`_).

A blue button runs a row for the first time; an orange one redoes a file that is out of date. The line under the name then says why: for example "the search window changed (…): download again" or "the AOI changed: download again". In an evaluator's `review copy <defo-evaluation-return_>`_, nothing runs: the column reads "To download" instead of a button.

.. note::

    A downloaded row has no button: a source already downloaded for the period's search window is not downloaded again by itself. To fetch the latest alerts of a catalogue that keeps adding alerts to past dates, use **Download again**. The app asks first, with the window and the date of the file it replaces. It is not offered for a GeoTIFF source ("Nothing to download again: read from a file").

Each row is downloaded with its own button. Select the buttons of several rows to download them all: each starts its own job, and they queue, one row at a time. Rows that read "not covered" or "no data" have no button; a row that fails shows its error in red under it. The running row shows its own progress bar; a started row cannot be stopped.

The download also shows as a task notification titled **Download**, with the source it is on and its percentage.

.. _defo-alerts-remove:

Remove a source from a period
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Select the bin icon (**Remove from this period**), then confirm. The source's downloaded and harmonized files of this period are deleted. Alert sets of this period that already used it keep their alerts and show as out of date.

The source stays in the project: other periods keep it, and it can be added back with **Add source**. A source is never deleted from the whole project.

Common messages
^^^^^^^^^^^^^^^

"This source does not cover the AOI."
    The raster's footprint misses the area: check the asset or the AOI.

"A mapped band is missing." or "A mapped band is not numeric."
    Choose other bands or another format.

"This CCDC asset stores its dates as Julian days or Unix time …"
    Only CCDC outputs dated in fractional years are supported.

"This period already has 6 custom sources."
    Remove a custom source from the period before adding another one.

"This file cannot be read as CSV, GeoPackage or Shapefile."
    The file is not a .csv, .gpkg or .shp file, or it could not be read as one.

"The Shapefile is missing its .shx or .dbf file."
    Put the .shx and .dbf files with the same name as the .shp in its folder.

"The date column cannot be read: mixed day/month orders or no valid date."
    Some dates are written day first and others month first, or no value reads as a date. Choose another **Date column**, or write the dates in one format.

"No dated point or polygon in this file."
    No row has both a point or polygon and a date. Line features and rows without coordinates are skipped.

"A job is writing into this project; …"
    Sources cannot change during a download or an **Integrate & vectorize** run. Wait for it to end.

.. _defo-harmonize:

Harmonize
---------

This step puts every input of the active `period <defo-period_>`_ on one common grid. Each source downloaded in `Alerts <defo-alerts-download_>`_ is *harmonized*: aligned onto the project grid and cut by the period's masks. Nothing whose inputs are unchanged runs twice.

Open the **Harmonize** step of the **Workflow** panel. It unlocks once at least one source of the active period is downloaded (or is a GeoTIFF source). It works on the active period: to harmonize another period, make it active in the `Period <defo-period_>`_ step first.

From top to bottom, the step has three parts: the **Project grid**, the **Masks** and the **Sources for this period**.

.. shot: prepare-step | The Harmonize step of the demo project after a full run: the Project grid card (EPSG of the UTM zone, Resolution 10 m, the "… × … pixels, about … MB per source before compression" line and "The grid is locked because the project has alert sets."), the Masks card with its one mask (Mode Keep, green "Ready", subtitle "Earth Engine · …"), and the "Sources for this period" table with GLAD-L, RADD and GLAD-S2 each green "Ready" in the Status column, each with its "downloaded … · … · N alert pixels" subtitle and its map, Details and Delete harmonized file icons. Crop to the Workflow panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/prepare-step.png
    :alt: The Harmonize step after a run

The project grid
^^^^^^^^^^^^^^^^

Every raster of the project is aligned onto one grid: one projection in metres and one pixel size, over the AOI. Alerts from sources with different pixel sizes can then be combined pixel by pixel, and the minimum alert size in hectares becomes a pixel count.

.. list-table::
    :header-rows: 1
    :widths: 15 40 45

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **EPSG**
        -   The projection of the grid, as a European Petroleum Survey Group (EPSG) code. The target button at the end of the field fills in the Universal Transverse Mercator (UTM) zone of the AOI.
        -   The UTM zone of the AOI's centre. Must be a projected system in metres: a geographic system (like 4326) or one in feet is refused.
    *   -   **Resolution**
        -   The pixel size, in metres.
        -   The finest pixel size among the project's sources: 10 m with RADD or GLAD-S2, 30 m with GLAD-L only, a custom source's own pixel size, or 30 m when nothing is known. Must be greater than 0.

Under the fields, the grid's size is previewed: "width × height pixels, about … per source before compression". Above 2 GB per source, a warning reads **This grid is large: downloads will take a while and use disk space.** (it does not block the step).

Select **Save grid**. The masks and the sources table appear only once a grid is saved.

The grid can change until the first alert set is made. A new grid only harmonizes the sources again from the files already downloaded; it does not download them again. Once the project has an alert set, the card reads **The grid is locked because the project has alert sets.**

.. note::

    Changing the `AOI <defo-aoi_>`_ clears the grid and deletes every download and harmonized file of the project, which were made for the old area. Save the grid again here, then run the rows again.

Masks
^^^^^

A *mask* limits where alerts are kept. It is a raster defined once for the project: a GEE image or image collection, or a GeoTIFF, with one band. A pixel is inside the mask where that band is not zero; zero and no-data pixels are outside it.

Each period chooses a **Mode** for each mask:

.. list-table::
    :header-rows: 1
    :widths: 20 80

    *   -   Mode
        -   Effect on the period's alerts
    *   -   **Off**
        -   The mask is not used in this period.
    *   -   **Keep**
        -   Alerts *outside* the mask are removed (e.g. keep only alerts inside a forest mask).
    *   -   **Exclude**
        -   Alerts *inside* the mask are removed (e.g. drop alerts in plantations or water).

When several masks are on, all of them apply. Masks act on the harmonized sources, so a change of **Mode** makes the period's sources out of date. The **Harmonize** of each row then harmonizes them again without downloading them. A new period starts with the mask choices of the latest period.

Add a mask
""""""""""

.. shot: prepare-mask-add | The "Add a mask" dialog: Name with its hint "At most 24 characters; it also names the mask's files.", Source = Earth Engine, the Hansen forest-change image asset picked, Band = treecover2000 with the hint naming the band suggested as a mask, Mode in the active period = Keep, and the grey note under it. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/prepare-mask-add.png
    :alt: Adding a mask

Select **Add mask** to open the **Add a mask** dialog. The bands are read as soon as the raster is chosen.

.. list-table::
    :header-rows: 1
    :widths: 20 40 40

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **Name**
        -   The mask's name in lists, legends and file names.
        -   Suggested from the asset or file name. At most 24 characters, at least one letter or digit, unique among the project's masks.
    *   -   **Source**
        -   **Earth Engine** (an asset) or **GeoTIFF / VRT** (a file in your SEPAL folder).
        -   **Earth Engine**.
    *   -   Asset or **GeoTIFF / VRT**
        -   The GEE image or image collection, or the .tif file.
        -   
    *   -   **Band**
        -   The band that defines the mask. Shown when the raster has two bands or more; with one band, the form reads "One band (…): the mask is made from it."
        -   The band whose name looks like a mask (e.g. ``datamask``), named in the hint ("… looks like a mask; non-zero pixels are inside it."), else none: pick it.
    *   -   **Mode in the active period**
        -   **Keep** or **Exclude**.
        -   **Keep**. The mask is turned on in the active period only; every other period leaves it off until it is turned on there.

When **Add mask** is selected, the app checks the raster and its band. A problem is shown in red inside the dialog, which stays open for corrections.

The mask list
"""""""""""""

Each row of **Masks** shows:

.. list-table::
    :header-rows: 1
    :widths: 20 80

    *   -   Column
        -   Description
    *   -   **Mask**
        -   The mask's name. The line under it gives its source and size on disk once it is ready ("Earth Engine · 18.9 MB"), or why it needs a run ("not downloaded yet", "the grid changed (…): align again"). It ends with "Off" when the mask is off in the active period.
    *   -   **Mode**
        -   The mask's mode in the active period: **Off**, **Keep** or **Exclude**. A change applies at once; the period's sources then read out of date.
    *   -   **Status**
        -   "Ready", or a button for the mask's next run: **Download** (a GEE mask not downloaded yet) or **Align** (onto the grid). An orange button redoes a file that is out of date. While a run goes on, the cell reads "Downloading 42%", "Aligning" or "Queued".

The icons on the right side of each row:

-   the map icon shows the mask on the map: a GEE mask can be previewed before it is downloaded, a GeoTIFF mask once it is aligned;
-   the information icon opens its **Details** (see `The Details dialog <defo-harmonize-details_>`_); and
-   the **More actions** menu (three dots) holds:

    -   **Download again** (GEE masks only), for an asset that changed. The app asks first: "This fetches the mask again from Earth Engine, replaces its download, then aligns it.";
    -   **Edit**, which opens **Edit mask** *name*: the raster and band can change, the name cannot. Once an alert set used the mask, it can no longer be edited (**An alert set already uses this mask: add a new one instead.**); and
    -   **Delete mask…**, which deletes the mask after you confirm. Its download and aligned file are deleted and every period stops using it. Alert sets that used it keep their alerts and show as out of date.

A mask is downloaded and aligned once for the whole project, whichever period runs it.

.. _defo-harmonize-sources:

Sources for this period
^^^^^^^^^^^^^^^^^^^^^^^

The table has one row per alert source of the active period, with two columns:

.. list-table::
    :header-rows: 1
    :widths: 20 80

    *   -   Column
        -   Description
    *   -   **Source**
        -   The source's name. The line under it says what the row holds or what it waits for (see below). Warnings, such as a partial coverage, and errors show as lines under the row.
    *   -   **Status**
        -   The row's state, or a button for its next run.

The **Status** column reads:

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Status
        -   Meaning
    *   -   "Ready"
        -   Downloaded and harmonized with the current inputs. The line under the name gives the download date, the size on disk and what the harmonized file found: "downloaded 2026-10-20 · 31.7 MB · 2,362,718 alert pixels".
    *   -   **Harmonize**
        -   The download is current, but the harmonized file is missing or out of date (a new download, a new grid, a mask change). Select the button to run the row: it aligns any mask of the period that needs it, then harmonizes the source, without downloading it.
    *   -   "Download or read it in Alerts first"
        -   The source is not downloaded for this period's search window, or its download is out of date. The row has no button: download it in `Alerts <defo-alerts-download_>`_ first.
    *   -   **Retry**
        -   The last run of the row failed. Its error is shown in red under the row.
    *   -   "Downloading 42%", "Harmonizing", "Queued"
        -   The row is running, or waits for its turn in a run ("waiting for the row above"). A row being downloaded in Alerts shows as running here too, and cannot be harmonized until its download ends.
    *   -   "not covered", "no data"
        -   The source cannot run for this period: it does not cover the AOI, or it has no data for the search window. The line under the name gives the reason. See `Alert sources <defo-alerts_>`_ for coverage.
    *   -   "File missing"
        -   The file of a GeoTIFF source is gone (see `Common messages <defo-harmonize-messages_>`_).

In an evaluator's `review copy <defo-evaluation-return_>`_, nothing runs: instead of a button, the column reads "To harmonize" or "To align".

A blue button runs a row for the first time; an orange one redoes a file that is out of date. The line under the name then says why: for example "the grid changed (EPSG:32719 · 30 m → EPSG:32719 · 10 m): harmonize again", "it was downloaded again since: harmonize again" or "mask forest_2000 changed: harmonize again".

The icons on the right side of each row:

-   the map icon (**Show on the map**) shows the harmonized alerts on the map;
-   the information icon opens the row's **Details** (see below); and
-   **Delete harmonized file** removes this period's harmonized file of the source, after you confirm. The download stays: harmonize the source again in this step to rebuild the file. The alert sets of this period built from the source read out of date; their alerts and reviews stay.

.. _defo-harmonize-details:

The Details dialog
""""""""""""""""""

.. shot: prepare-details | The Details dialog of the demo's GLAD-L row: the title GLAD-L, the lead "Ready · 2026-09-01 → 2026-09-30", the Source section (Catalogue, Coverage), the Download section with its date (Search window, Native grid, Size, File) and the Harmonize section with its date (Grid used, Resampling, Masks, Alert pixels, Alert dates, Size, File), and the Close button. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/prepare-details.png
    :alt: The Details dialog of a source

The information icon of a source or a mask opens a read-only summary of what its files were made with. It starts with the row's status and, for a source, the period. When the row is out of date, an orange **Why:** line says what changed.

In `Alerts <defo-alerts_>`_, the information icon of a source opens the same dialog, with two more controls: the **Add to new periods** checkbox (see `Add a source <defo-alerts-new-periods_>`_) and, for a custom source, **Edit**.

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Section
        -   What it lists
    *   -   **Source**
        -   A predefined source: its **Catalogue** and **Coverage** of the AOI, with the last date of data and the day it was checked. A custom source: its **Kind**, **Reference**, **Format**, **Date encoding**, **Bands** and **Native grid**. A points or polygons source: its **Kind**, **Reference**, **Layer**, **Date column** (with how its dates are read) and **Square side (m)**. A mask: its **Reference**, **Band**, **Native grid** and the periods it is **Used in**.
    *   -   **Download** (**Read from file** for a GeoTIFF source)
        -   The **Search window**, the **Native grid** the file was downloaded in, its **Size** and its **File** in the project folder.
    *   -   **Harmonize** (**Align** for a mask)
        -   The **Grid used**, with the current grid when it changed since, the **Resampling**, the **Masks** applied with their mode, the **Alert pixels** kept (and how many the masks removed), the **Alert dates** found, the **Size** and the **File**. For a mask: its **Mask pixels**.

Each section gives the date and time its file was written, or reads "Not run yet". Select **Close**, or press **Esc**, to close the dialog.

.. labels-ok: Esc

Run several rows
""""""""""""""""

Each row runs with its own button. A source's **Harmonize** first aligns the masks on in the period that need it, then harmonizes the source; a mask's **Align** aligns only that mask. Select the buttons of several rows to run them all: each starts its own job, and they queue, one row at a time:

-   rows that read "not covered" or "no data", and rows still to download, have no button;
-   a row that fails shows its error in red under it, and the next row goes on;
-   while one source's run aligns a mask, another source's **Harmonize** that needs the same mask reads "Queued" and starts once the mask is aligned.

The running row shows its own progress bar, which moves without an end while it has no percentage. A started row cannot be stopped; the rows already done stay done.

The run also shows as a task notification titled **Harmonize**, with the row it is on (e.g. "Harmonizing GLAD-L").

.. tip::

    Each row needs free disk space for its files. The app checks it before writing, and stops the row with a message when the disk is too full. The grid size line gives an idea of how big a source can get.

.. _defo-harmonize-messages:

Common messages
^^^^^^^^^^^^^^^

"Not enough free disk space: this needs … GB in …, and … GB is free."
    Free some space in your SEPAL folder, or use a coarser grid.

"A row of this run is already being prepared …"
    The mask whose **Align** you selected is being aligned by another run (another period's, or a source's **Harmonize**), or the row is still running. Run it again once that has finished.

"The AOI's geometry is still being fetched; run this row again in a moment."
    GeoTIFF sources and masks need the AOI's shape. Wait a moment. If it could not be fetched, select **Check again** under the table, then run them.

"Mask … covers none of the AOI: as a keep mask, every alert would be removed."
    The mask misses the area. Check its asset or band, or turn it off.

"A job is writing into this project; save the grid once it has finished."
    The grid, masks and sources cannot change while a download or an **Integrate & vectorize** run is going.

"File missing", with "missing: file not found: …" under the row, or "Mask …: file not found (…). Put the file back at this path to use the mask."
    A GeoTIFF source or mask was moved, renamed or deleted from your SEPAL folder. Put the file back at the path shown, or edit the source or mask to point at its new place.

"A mask on in this period is not aligned on the current grid yet; a source's Harmonize aligns the masks first."
    A source cannot be harmonized before the period's masks are aligned. Select the source's **Harmonize**, or the mask's **Align** button first.

"Mask …: its native grid (projection and scale) is unknown; edit the mask."
    The app does not know how to download this GEE mask. Open it with **Edit** in its **More actions** menu and save it again, so that its raster is checked anew.

.. _defo-integrate:

Integrate & vectorize
---------------------

This step turns the harmonized sources of the active period into an *alert set*: the list of alerts to review in `Analysis <defo-analysis_>`_. It:

-   combines the sources pixel by pixel;
-   removes what earlier periods already reported;
-   groups neighbouring alert pixels into *clusters*; and
-   draws one polygon per cluster. Each cluster it keeps is an alert of the set.

Open the **Integrate & vectorize** step of the **Workflow** panel. It unlocks once at least one source of the active period is ready in `Harmonize <defo-harmonize_>`_.

The form follows the run, in three outlined cards: the sources to combine, the cluster settings and the attribute layers. The **Integrate & vectorize** button is under them. Under the sources, grey lines say what the run also does on its own, without a setting:

-   "Removes the pixels already in N earlier alert sets" (see `What earlier periods already reported <defo-integrate-earlier_>`_); and
-   "Brings back the not-analysable pixels of N earlier sets inside the look-back", counted for the selected sources.

.. shot: integrate-form | The Integrate & vectorize step of the demo project: the first card with GLAD-L, RADD and GLAD-S2 checked, each with its "ready · N alert pixels" note; under them the "Include probable (unconfirmed) alerts" switch (on) with the "Set per source" link; Minimum cluster size 0.5 ha with its hint; Order = Bigger clusters first; "Limit the number of clusters" ticked, with Maximum number of clusters 100 and its hint "Keeps the 100 biggest clusters." in the second card; the attribute layers card with one layer; the grey "Creates or replaces the alert set …" line and the Integrate & vectorize button. Crop to the Workflow panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/integrate-form.png
    :alt: The Integrate & vectorize form

What an alert is
^^^^^^^^^^^^^^^^

An alert is a *cluster*: a group of alert pixels that touch each other, by their sides or corners, whichever source flagged each pixel. Where GLAD-L and RADD pixels touch, they form *one* alert that lists both sources. An alert is never split into one alert per source.

Each alert keeps:

-   the sources that detected it;
-   its first and last detection dates (the earliest and latest date among its pixels);
-   its area in hectares; and
-   a statistic of each attribute layer's bands (see below).

A cluster smaller than the **Minimum cluster size** (see `The options <defo-integrate-options_>`_) does not become an alert: its pixels are set aside as *not analysable*.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/anim/integrate.gif
    :alt: Sources on one grid become clusters; each cluster is measured against the minimum size, and becomes one polygon listing its sources or, when smaller, is set aside

.. _defo-integrate-earlier:

What earlier periods already reported
"""""""""""""""""""""""""""""""""""""

Pixels inside the alerts of an alert set from an *earlier* period (its *footprint*) are removed before the clusters are made. This way, the `look-back <defo-period-lookback_>`_ never reports the same loss twice.

Pixels that did not become alerts (a cluster below the minimum size, or beyond the maximum number of alerts) are kept as *not analysable*. They are not in the footprint: bringing them back is the purpose of the `look-back <defo-period-lookback_>`_.

A later period's run adds those pixels back when both conditions are met:

-   its look-back reaches back into the earlier period (that period ends on or after the start of the new search window); and
-   the two periods share a source.

The pixels come back whatever their detection date within the earlier set's own search window. They join the new pixels that touch them, and a cluster that now reaches the minimum size becomes an alert. Its detection dates can be older than its own period and look-back. With a look-back of 0, the search window starts on the period's own first day, so nothing set aside is reconsidered.

.. _defo-integrate-growth:

Growth of earlier loss
""""""""""""""""""""""

A clearing often keeps growing from one month to the next. The run links each new alert to the *earlier loss* it grows from: the alerts of earlier periods' sets that were saved as **True alert** or **Needs revision**. An earlier alert's shape is the polygon drawn for it in `Refine the polygon <defo-analysis-refine_>`_, or else its detected cluster.

-   A new cluster that lies within one pixel of the grid of an earlier alert's shape, edge to edge, is a *growth alert*, linked to every earlier alert that close. A cluster one empty pixel away still counts; a diagonal gap of one pixel is farther. One without a link is a *new* alert.
-   With **Keep smaller clusters that touch earlier confirmed loss** selected (the default), a cluster smaller than the **Minimum cluster size** is kept when it is that close to earlier loss: it is a growth alert *under the minimum area*. Cleared, every small cluster is set aside. A small cluster that touches nothing is always set aside as *not analysable*.
-   Growth alerts are sorted and limited with the others: **Limit the number of clusters** can leave them out.
-   Sets made before this reach of one pixel keep the links they were made with until they are run again.
-   Only the reviews saved when the run starts count. An earlier alert confirmed afterwards is not linked, but it can be linked by hand in `Earlier alerts <defo-analysis-earlier_>`_.

The alerts linked to each other, across all periods, make the *history* of a clearing. Analysis shows it on each alert, and the `Overview <defo-overview-growth_>`_ sums it up.

.. _defo-integrate-options:

The options
^^^^^^^^^^^

The form opens with the settings of the active alert set (all but the sources), or with the defaults below when there is none.

.. list-table::
    :header-rows: 1
    :widths: 20 50 30

    *   -   Option
        -   Description
        -   Default and limits
    *   -   Sources
        -   The sources whose alerts go into the set, in the first card. Each ready source is listed with what its harmonized file found. A source that does not cover the AOI, or has no data for the period, is listed as disabled, with the reason.
        -   Every ready source. At least one.
    *   -   **Include probable (unconfirmed) alerts**
        -   Shown only when at least one selected source has a *probable* (low-confidence) class. One switch for all such sources. Off, their probable pixels are dropped before anything else, and only their confirmed pixels count. With two or more such sources, **Set per source** unfolds one switch per source (see below).
        -   On.
    *   -   **Minimum cluster size**
        -   Clusters smaller than this are dropped, unless the next option keeps them. The hint gives that size in pixels of the grid (at 10 m, 0.5 ha is "50 pixels on the grid").
        -   0.5 ha. Any number of hectares, 0 or more. Even at 0, a cluster is at least one pixel.
    *   -   **Keep smaller clusters that touch earlier confirmed loss**
        -   Keeps a cluster under the minimum size when it is within one pixel of an earlier alert reviewed as **True alert** or **Needs revision** (see `Growth of earlier loss <defo-integrate-growth_>`_). A line under it says when the run has nothing to link to: "No earlier period has an alert set yet: nothing links in this run." or "No alert of an earlier period is reviewed yet: nothing links in this run."
        -   Selected.
    *   -   **Order**
        -   The order of the clusters in the set, which is the review order: **Bigger clusters first**, **Smaller clusters first**, **Recent clusters first** (by last detection date) or **Older clusters first** (by first detection date).
        -   **Bigger clusters first**.
    *   -   **Limit the number of clusters**
        -   When selected, shows **Maximum number of clusters**: only the first clusters in the chosen **Order** are kept. Its hint says which (e.g. "Keeps the 100 biggest clusters." or "Keeps the 100 most recent clusters."). When cleared, every cluster is kept.
        -   Cleared. When selected, the limit starts at 100. It must be a whole number greater than 0.
    *   -   **Attribute layers**
        -   Rasters whose band statistics are added to every alert (see below).
        -   None.

Probable alerts per source
""""""""""""""""""""""""""

With two or more selected sources that have a probable class, select **Set per source** under **Include probable (unconfirmed) alerts** to give each one its own switch, named after the source:

-   A selected source without a probable class (a custom source that has only detection dates) is listed as "(source): dates only, no probable level".
-   When the sources' switches differ, the main switch reads off, the note **Mixed: the sources below differ.** replaces **Set per source**, and the per-source switches stay open.
-   Turning the main switch on or off sets every source at once.

.. _defo-integrate-attributes:

Attribute layers
""""""""""""""""

An *attribute layer* adds information to each alert from a raster (e.g. the majority land-cover class under the alert, or its mean elevation). The values are columns of the alert table: they are exported with the alerts, and columns of classes can be used in the Analysis filter.

.. shot: integrate-attribute | The "Add an attribute layer" dialog: Layer name "worldcover" with its hint "Cluster columns are named <layer name>_<band>.", Source = Earth Engine with its hint "An Earth Engine image, or a GeoTIFF or VRT in your SEPAL folder.", the ESA WorldCover image picked, the one-band line "One band (Map): its statistic is added to every cluster.", and the band's row with statistic Majority and its column name worldcover_map beside it. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/integrate-attribute.png
    :alt: Adding an attribute layer

To add an attribute layer:

1.  Select **Add attribute layer** to open the **Add an attribute layer** dialog.
2.  Check the **Layer name**, suggested from the raster once it is chosen. The columns are named *layer name*\_\ *band*.
3.  Choose the **Source** (**Earth Engine**, an image, or **GeoTIFF / VRT**, a file in your SEPAL folder), then choose the raster. Its bands are read at once.
4.  With one band, the form reads "One band (…): its statistic is added to every cluster." With two or more, select one or more in **Bands**.
5.  For each band, choose the statistic computed over the alert: **Majority** (for classes), **Mean**, **Minimum**, **Maximum** or **Median**. It starts on **Majority** when the band's name looks like classes (e.g. ``landcover``), and on **Mean** otherwise, marked "(suggested)". The column name is shown beside it.
6.  Select **Add attribute layer**.

Rules:

-   A layer needs at least one band (**Keep at least one band.**).
-   Two layers cannot read the same raster (**Another attribute layer already reads this raster.**).
-   Column names never take the name of an alert column or of another layer's column: a clash gets a suffix.

The list under **Attribute layers** shows each layer with its columns. The pencil icon edits a layer and the bin icon removes it. The layers belong to this form until it runs: they are saved with the alert set.

Run the step
^^^^^^^^^^^^

The grey line above the button names the set the run makes: "Creates or replaces the alert set (period) · (sources)". An alert set is identified by its period and its sources:

-   a new combination of sources makes a new set: a period can hold several sets (e.g. one with GLAD-L only and one with all three sources); and
-   the same combination again *replaces* the set.

Select **Integrate & vectorize**. The button stays disabled until at least one source is selected and, when **Limit the number of clusters** is selected, the limit is valid ("Enter a whole number greater than 0." under the field).

The run goes through "Combining sources", "Vectorizing clusters", "Saving the clusters", "Writing the footprint" and "Building map tiles". When it ends, a message reads "N clusters ready for review", followed by "Linked N clusters to earlier loss (M under the minimum area)" when it found `growth alerts <defo-integrate-growth_>`_, and the new set becomes the *active set*: the one the `Questionnaire <defo-questionnaire_>`_, `Evaluation <defo-evaluation_>`_, `Analysis <defo-analysis_>`_ and `Overview <defo-overview_>`_ work on. The step stays open.

The run also gives every alert the names of the administrative areas it touches: ``admin1`` is the country, ``admin2`` the first-level unit and ``admin3`` the second-level unit, from the FAO GAUL 2024 boundaries. The boundaries are downloaded once for the project's AOI and kept in the project folder (``admin/``). An alert across a border lists every area it touches, separated by commas, the one holding most of it first. If the download fails, the run still ends, with a warning, and the names are filled when an alert is saved.

If no cluster is left, the set is still made, empty: the message reads "No new clusters in this period: the alert set is empty." and gives the reason for each source (e.g. "GLAD-L: all 56 alert pixels removed by masks" or "RADD: probable (unconfirmed) alerts were left out").

.. _defo-integrate-replace:

Replace a set
"""""""""""""

.. shot: integrate-replace | The "Replace this alert set?" confirmation for the demo set, with "N reviewed clusters in this set will be discarded. The evaluator split and its pending returns will be discarded." (the demo set is split), then the list of reviewed alerts ("#0 · Reviewed: confirmed · 383.18 ha" …); the Cancel and orange Replace buttons. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/integrate-replace.png
    :alt: Confirming the replacement of an alert set

When the set about to be replaced has reviewed alerts or an `evaluator split <defo-evaluation_>`_, the **Replace this alert set?** dialog lists what would be lost: the reviewed alerts (up to 20, then "… and N more"), and the split with the reviews that evaluators have not sent back yet. When alerts of later periods grow from this set, it adds "N clusters of later periods are linked to this set; their links will break.": after the run, those links show as "earlier set was re-run" (see `Earlier alerts <defo-analysis-earlier_>`_). Select **Replace** to continue. A set with nothing to lose is replaced without confirmation.

.. attention::

    Replacing a set discards its reviews. To try other settings without losing reviews, choose another combination of sources, which makes a separate set.

.. _defo-integrate-outdated:

When the active set is out of date
""""""""""""""""""""""""""""""""""

If the inputs of the active set changed since it was made (a source downloaded again, a mask switched, the period's look-back, the AOI or the grid changed), an orange line reads: "The active set (…) was built from inputs that have changed since." Run **Integrate & vectorize** again to rebuild it, which discards its reviews.

If the set's files were deleted from the project folder, the line reads: "The active set's files (…) are missing from the project folder."

.. _defo-integrate-map:

View the alerts on the map
^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the project has a set, a heading under the button counts the active set's alerts ("Result · 48 clusters"), and switches under it draw the set on the map:

.. list-table::
    :header-rows: 1
    :widths: 35 65

    *   -   Switch
        -   Description
    *   -   **Show these alerts on the map**
        -   The active set's alerts, coloured by review status. Click on an alert to view "Alert (id) · (status) · (area) ha". Its **Review** button opens it in Analysis.
    *   -   **Show not-analysable pixels**
        -   The alert pixels that did not become alerts: **Too small** or **Over the alert cap**.
    *   -   **Show earlier sets**
        -   The alerts of earlier periods' sets, for context.

The map keeps them in other steps. Turn them off here.

Common messages
^^^^^^^^^^^^^^^

"… is not downloaded and harmonized for this period; download it in Alerts and harmonize it in Harmonize first."
    A source's files are out of date. Download it in `Alerts <defo-alerts-download_>`_, then harmonize it in `Harmonize <defo-harmonize_>`_.

"The footprint of the earlier set … is missing; run Integrate & vectorize on that set again first."
    An earlier period's files were deleted. Make that period active and run its set again.

"Not enough free disk space: …"
    The run writes a few rasters the size of the grid. Free some space.

"The project's period, area of interest or grid changed while the run was going, so the alert set was not recorded."
    Run it again.

"tippecanoe is not installed: the map will show alert points without polygons."
    The set is made; the map shows its alerts as points instead of polygons.

"The map tiles could not be shown (…): showing alert points without polygons."
    The set is made, but its map layer could not be built. The map shows its alerts as points.

"The alert store of … is missing; run Integrate & vectorize for that period again."
    With **Show earlier sets**, an earlier set's alert file is gone from the project folder. Make that period active and run its set again.

.. _defo-layers:

Additional layers
-----------------

Visualization layers support the review of the alerts: a land-cover map, a forest baseline, a recent mosaic. They never change the alerts. A layer is an Earth Engine image or a GeoTIFF. It can be shown on the main map and, with **Show in Analysis** selected, on the two maps of the `Analysis <defo-analysis_>`_ screen.

Open the **Additional layers** step of the **Workflow** panel, the first step of **Set up review**. It unlocks once the project has an alert set (see `Integrate & vectorize <defo-integrate_>`_).

The step is optional: skip it and come back at any time. Its dot in the list of steps is dashed, and the step shows no count until it has a layer.

In a project converted from a `version 1 recipe <defo-project-v1_>`_, this is the only step whose settings can change.

.. note::

    Planet NICFI mosaics are not an additional layer: with NICFI access in your GEE account, they come with the *Planet* images of the `Analysis timeline <defo-analysis-timeline_>`_.

.. shot: layers-list | The Additional layers step of the demo project with its one layer listed: name, the "Earth Engine" chip, the green "in Analysis" chip, the grey summary note under it, and the map / edit / delete icons; the layer switched on, so it shows on the main map with its legend. Crop to the Workflow panel plus the visible part of the map.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/layers-list.png
    :alt: The Additional layers step with one layer

The layer list
^^^^^^^^^^^^^^

Each row of **Visualization layers** shows:

-   the layer's **Name**;
-   a chip with its source (**Earth Engine** or **GeoTIFF / VRT**);
-   an **in Analysis** chip when it is shown on the Analysis maps; and
-   a note with its bands and value range, or, for a categorical layer, its band and number of classes ("band Map · 9 classes").

The icons on the right side of each row:

-   the map icon shows the layer on the main map, with its legend;
-   the pencil icon opens it for editing (**Edit layer** *name*); and
-   the bin icon deletes it. The layer is removed from the project; its file or asset is not touched.

Add a layer
^^^^^^^^^^^

Select **Add layer** to open the **Add a visualization layer** dialog. The form reads from top to bottom: the name, the source, the image, then how its bands are drawn. The bands are read as soon as the image is chosen ("Reading the bands…"), and every choice after that is a dropdown menu.

.. list-table::
    :header-rows: 1
    :widths: 20 40 40

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **Name**
        -   The layer's name in the list, on the maps and in the legend.
        -   Left empty, it is filled from the asset or file name, plus the band or combination. At most 24 characters, unique in the project.
    *   -   **Source**
        -   **Earth Engine** (an image asset) or **GeoTIFF / VRT** (a file in your SEPAL folder).
        -   **Earth Engine**.
    *   -   Asset or **GeoTIFF / VRT**
        -   A GEE *image* (not a collection), or a .tif file.
        -   The GeoTIFF's folder must be writable: the app writes an overview file next to it so that the layer draws quickly.

What comes next depends on the number of bands of the image:

-   One band: the form names it ("One band (…): it is drawn on its own.").
-   Two bands: choose the one to draw in **Band**. RGB needs three bands or more.
-   Three bands or more: **Bands** asks for **Select one band** (then **Band**) or **RGB composite**. **RGB composite** is suggested when the band names give red, green and blue (e.g. ``B4``, ``B3`` and ``B2`` of Sentinel-2). **Band** starts on the first band.

One band
""""""""

.. shot: layers-add-categorical | The "Add a visualization layer" dialog with Source = Earth Engine, the ESA WorldCover image picked, the one-band line "One band (Map): it is drawn on its own.", Raster type = Categorical: a colour per class, Find the classes in the AOI pressed and the classes found listed (swatch, value, Label, eye), Add a value and the Palette button under them, the legend preview with one chip per class, and Show in Analysis ticked. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/layers-add-categorical.png
    :alt: Adding a categorical layer from a land-cover image

A single band takes a **Raster type**:

-   **Continuous: a colour ramp** for measured values (reflectance, elevation, tree cover); or
-   **Categorical: a colour per class** for whole-number classes (a land-cover map, a forest mask, a loss year). It is suggested when the band's name looks like classes (e.g. ``landcover``, ``class``, ``lossyear``, ``datamask``).

A preview of the layer's legend appears under the fields.

.. list-table::
    :header-rows: 1
    :widths: 20 40 40

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **Colour ramp**
        -   *Continuous*: the colours, from **Min** to **Max**: **Grayscale**, **Blues**, **Greens**, **Oranges**, **Cool–warm**, **Viridis**, **Terrain**, **Heat** or **Magma**.
        -   **Grayscale**.
    *   -   **Invert**
        -   *Continuous*: reverses the ramp.
        -   Off.
    *   -   **Min**, **Max**
        -   *Continuous*: the value range stretched over the colours.
        -   0 and 1. Both must be numbers, **Min** below **Max**.
    *   -   **Stretch to the AOI (2–98 %)**
        -   *Continuous*: fills **Min** and **Max** with the band's 2nd and 98th percentiles over the AOI's bounding box.
        -   
    *   -   **Find the classes in the AOI**
        -   *Categorical*: lists the whole values present over the AOI, each with a colour, its value, a **Label** and an eye icon that hides or shows it. When the image names its classes and their colours (as ESA WorldCover does), the classes take them; otherwise each class is labelled with its value.
        -   At most 50 classes. Values not listed and hidden classes are transparent.
    *   -   **Add a value**
        -   *Categorical*: adds a class by hand. Type the whole number, then press **Enter** or select the plus icon.
        -   Each value once.
    *   -   **Palette**
        -   *Categorical*: recolours every class from a palette: **Set1**, **Set2**, **Tab10** or **Paired**. Select a class's colour square to choose its colour by hand.
        -   

.. labels-ok: Enter

When a band holds only 0 and 1 over the AOI, the classes found name 1 after the band and start with 0 hidden: "Only 0 and 1 in the AOI: 1 is named after the band and 0 starts hidden (transparent)." Select the eye icon of 0 to draw it too.

RGB composite
"""""""""""""

.. shot: layers-add-rgb | The "Add a visualization layer" dialog with Source = Earth Engine, the demo's Sentinel-2 image picked, Bands = RGB composite (suggested) with its hint, Composite open on or set to False-colour infrared with its bands named, its hint "Detected from the band names: …", the Red / Green / Blue band selects with their colour dots, Min 0 and Max 4000, the Stretch to the AOI button, and Show in Analysis ticked. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/layers-add-rgb.png
    :alt: Adding an RGB layer from an Earth Engine image

.. labels-ok: True colour; False-colour infrared; SWIR / NIR / red

.. list-table::
    :header-rows: 1
    :widths: 20 40 40

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **Composite**
        -   A standard combination, named with its bands (e.g. "True colour (B4 / B3 / B2)"): **True colour**, **False-colour infrared** (near infrared, red, green) or **SWIR / NIR / red** (shortwave infrared, near infrared, red); or **Custom: pick the bands**. The hint lists the band roles detected from the band names ("Detected from the band names: …").
        -   The first combination the band names allow. A combination whose bands were not all recognized reads "(bands not found)" and cannot be chosen. With no band name recognized, the first three bands are used as red, green and blue.
    *   -   **Red band**, **Green band**, **Blue band**
        -   The bands drawn in red, green and blue.
        -   Filled by the **Composite**. Must be three different bands. Bands chosen by hand that match a combination select it; others select **Custom: pick the bands**.
    *   -   **Min**, **Max**
        -   The value range stretched over the colours, the same for the three bands.
        -   0 and 1. Both must be numbers, **Min** below **Max**.
    *   -   **Stretch to the AOI (2–98 %)**
        -   Fills **Min** and **Max** with one range across the three bands, from their 2nd and 98th percentiles over the AOI's bounding box.
        -   

.. tip::

    Set **Min** and **Max** to the real range of the data (e.g. 0 to 3000 for a Sentinel-2 surface-reflectance image), or select **Stretch to the AOI (2–98 %)**. With the default 0 to 1, most images draw all white.

Show in Analysis
""""""""""""""""

**Show in Analysis** adds the layer to both maps of the `Analysis <defo-analysis_>`_ screen, turned off. Turn it on there from the layer menu. The Analysis maps show no legend for it.

Save a layer
^^^^^^^^^^^^

Select **Add layer** (or **Save** when editing). The app checks the bands, the range or the classes and, for a GeoTIFF, the folder. A problem is shown in red inside the dialog, which stays open. While the check runs, the button reads **Cancel** and stops it.

Layers saved before the visualization styles were added keep their exact look.

Common messages
^^^^^^^^^^^^^^^

"Pick an Earth Engine image."
    Image collections are not accepted as layers. Export a single image first.

"Pick three different bands for red, green and blue."
    Choose a different band for each colour.

"This band has non-integer values: draw it as Continuous."
    **Find the classes in the AOI** found decimal values: the band is not a set of classes. Set **Raster type** to **Continuous: a colour ramp**.

"More than 50 values: this band looks continuous."
    Draw the band as **Continuous: a colour ramp**, or add the classes you need by hand with **Add a value**.

"No values in the AOI." or "The band has no spread of values in the AOI."
    The band has no data over the AOI, or the same value everywhere. Check the image and the band, or enter **Min** and **Max** yourself.

"Find the classes or add a value." or "Show at least one class."
    A categorical layer needs at least one class, and at least one class not hidden.

"The folder … is not writable, so the layer's overviews cannot be built."
    Move the GeoTIFF to a folder of your own in SEPAL.

"The file … no longer exists."
    The file of a GeoTIFF layer was moved or deleted. Edit the layer and choose the file again.

.. _defo-questionnaire:

Questionnaire
-------------

The *questionnaire* holds the questions answered for every alert in `Analysis <defo-analysis_>`_, after its verdict. The answers are:

-   saved with the alert (one column per question);
-   exported with it;
-   charted in the `Overview <defo-overview_>`_; and
-   available to the alert's Word report.

This step also chooses the report template.

Open the **Questionnaire** step of the **Workflow** panel, in **Set up review**. It unlocks once the project has an alert set (see `Integrate & vectorize <defo-integrate_>`_). The questionnaire belongs to the project: every alert set of the project is reviewed with it. The step is optional: without changes, Analysis asks the default question.

.. shot: questionnaire-list | The Questionnaire step of the demo project with two questions: the default "Loss driver" (chips "several answers", "9 options", "typed answers", "True alert", "Needs revision", note {loss_driver}) and one added question (e.g. "Access road nearby?", "one answer", "2 options", "required" in red, "True alert", "Needs revision"); the "Show the questions expanded in Analysis" switch and its hint; the Report template line collapsed ("Report template · Default template", chip "default"). Crop to the Workflow panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/questionnaire-list.png
    :alt: The Questionnaire step

The question list
^^^^^^^^^^^^^^^^^

A new project starts with one question, **Loss driver**:

-   several answers;
-   nine options: **Agriculture expansion**, **Livestock grazing**, **Logging**, **Urban expansion**, **Shifting cultivation**, **Mining**, **Forest fires**, **Hurricanes** and **Other**;
-   typed answers allowed; and
-   asked for **True alert** and **Needs revision** (not for a false positive).

Edit or delete it like any other question.

Each row of **Questions** shows the question and chips that sum it up: **one answer** or **several answers**, the number of options, **typed answers**, **required**, and the verdicts it is asked for (or **all verdicts**). The note under it is its report placeholder, such as ``{loss_driver}``.

The icons on the right side of each row:

-   the arrows move the question up or down: Analysis asks the questions in this order;
-   the pencil icon edits it; and
-   the bin icon deletes it.

With no questions, the list reads **No questions: Analysis will only ask for the verdict.**

**Show the questions expanded in Analysis** (off by default) opens the **Questions** section of Analysis on every alert. When off, the section starts collapsed; it still opens when a verdict needs a required answer.

Add or edit a question
^^^^^^^^^^^^^^^^^^^^^^

.. shot: questionnaire-add | The "Add a question" dialog filled in: Question "Access road nearby?", Answer = One answer, two options "Yes" and "No" with their arrow and close icons, Add option, Allow typed answers off, Required on, Ask when the verdict is: True alert and Needs revision checked, False positive unchecked; the "Report placeholder: {access_road_nearby}" line. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/questionnaire-add.png
    :alt: Adding a question

Select **Add question** (or the pencil icon of a question) to open the **Add a question** (or **Edit question**) dialog.

.. list-table::
    :header-rows: 1
    :widths: 20 45 35

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **Question**
        -   The text shown in Analysis.
        -   Required.
    *   -   **Answer**
        -   **One answer** or **Several answers**. With several, the answers are saved together, separated by commas.
        -   **One answer**.
    *   -   **Options**
        -   The answers to choose from. **Add option** adds one; the arrows reorder them; the cross removes one.
        -   At least one option, unless typed answers are allowed. An option cannot be empty, contain a comma or repeat another option.
    *   -   **Allow typed answers**
        -   Lets the reviewer type an answer that is not in the options.
        -   Off.
    *   -   **Required**
        -   The review cannot be saved without an answer (for the verdicts it is asked for).
        -   Off.
    *   -   **Ask when the verdict is**
        -   The verdicts the question is asked for: **True alert**, **False positive**, **Needs revision**. For the other verdicts, it is hidden.
        -   All three. At least one.

The last line shows the question's report placeholder (e.g. "Report placeholder: {access_road_nearby}"). It is made from the question's text when the question is created and never changes, even if the question is renamed.

Select **Add question** (or **Save**). The dialog shows what is missing in red until the question can be saved.

.. note::

    Renaming a question or one of its options keeps the answers already saved: they are stored under the question's placeholder name and each option's own code, not under their text.

Delete a question
^^^^^^^^^^^^^^^^^

Select the bin icon. The confirmation dialog states how many alerts of the active set answered the question. The answers already saved stay in the alert table, but they are no longer shown, exported or charted.

.. _defo-questionnaire-template:

The report template
^^^^^^^^^^^^^^^^^^^

In Analysis, each reviewed alert can be exported with a Word report (see `Export <defo-export_>`_). The report is built from a .docx template, where *placeholders* such as ``{area_loss}`` are replaced by the alert's values.

.. shot: questionnaire-template | The Report template card expanded: "Report template · Default template" with its "default" chip, the "Report template (.docx)" file picker and its hint, and the placeholder chips under "Placeholders the template can use (click to copy):", the grey ones (ending with {centroid_lat}, {centroid_lon}, {before_radar}, {after_radar}, {image_note} and {radar_summary}) then the green {verdict}, {loss_driver} and the added question's key, with the note under them. Crop to the card.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/questionnaire-template.png
    :alt: The report template and its placeholders

The **Report template** line names the template in use, with a chip: **default** (the app's own template), **custom** (your file) or **missing** (your file was moved or deleted). Open it with the arrow on the right side:

-   **Report template (.docx)**: choose a Word file in your SEPAL folder. Every report of this project is then built from it. Clear the field to go back to the default template, which is in the app's language (English, Spanish, French or Portuguese).
-   **Placeholders the template can use (click to copy):** select a chip to copy its placeholder, then paste it into the template.

.. list-table::
    :header-rows: 1
    :widths: 40 60

    *   -   Placeholder
        -   Replaced by
    *   -   ``{admin1}``, ``{admin2}``, ``{admin3}``
        -   The administrative areas the alert falls in.
    *   -   ``{detection_date1}``, ``{detection_date2}``
        -   The alert's first and last detection dates.
    *   -   ``{confirmation_date}``
        -   The day the alert was reviewed. For an alert reviewed before the app recorded it, the day the report is built.
    *   -   ``{reviewed_by}``
        -   The SEPAL user name of the person who saved the review.
    *   -   ``{before_img}``, ``{after_img}``
        -   The names of the before and after images in the optical pictures, as picked in the review.
    *   -   ``{alert_system}``
        -   The sources that detected the alert.
    *   -   ``{area_loss}``
        -   The alert's area, in hectares (the group's, for a group).
    *   -   ``{centroid}``
        -   The centre of the alert (of the group's outline, for a group) as latitude, longitude in decimal degrees ("-12.345678, -69.123456").
    *   -   ``{centroid_lat}``, ``{centroid_lon}``
        -   The same latitude and longitude, each on its own ("-12.345678", "-69.123456").
    *   -   ``{before_radar}``, ``{after_radar}``
        -   With Sentinel-1 on and a radar pair: the names of the before and after radar images. A radar image that follows the optical pick (not placed by hand) is marked "(nearest radar image)", or "(nearest radar image, other pass)" when it comes from the other pass. Empty otherwise.
    *   -   ``{radar_summary}``
        -   With a radar pair: "Radar images: … (before) and … (after).", the two radar image names, for the summary. Empty otherwise.
    *   -   ``{image_note}``
        -   Always empty. Kept so that older templates still work; a paragraph holding only this placeholder is removed.
    *   -   ``{group_size}``, ``{group_alerts}``
        -   For an alert reviewed in a group: the number of alerts in the group and their numbers ("12, 15, 16"). Otherwise "1" and the alert's own number.
    *   -   ``{verdict}`` (green)
        -   The verdict, in the language of the app.
    *   -   One per question (green)
        -   The answer to that question; empty when the question is not asked for the alert's verdict.

The green placeholders come from the review. Placeholders are replaced in the document's paragraphs and tables, not in headers or footers.

Images in the report
""""""""""""""""""""

The report also holds six pictures of the alert, cut from the before and after images chosen in the review. They are not in the chip list: the template marks where each one goes with a paragraph holding only its marker, from ``[Placeholder for Image 1]`` to ``[Placeholder for Image 6]``. That whole paragraph is replaced by the picture (250 pt wide, or narrower to fit its table cell), so put nothing else in it.

.. list-table::
    :header-rows: 1
    :widths: 60 40

    *   -   Marker
        -   Picture
    *   -   ``[Placeholder for Image 1]``, ``[Placeholder for Image 4]``
        -   The before image.
    *   -   ``[Placeholder for Image 2]``, ``[Placeholder for Image 5]``
        -   The after image.
    *   -   ``[Placeholder for Image 3]``, ``[Placeholder for Image 6]``
        -   The after image with the alert's outline in red.
    *   -   ``[Placeholder for Radar 1]``
        -   The before radar image.
    *   -   ``[Placeholder for Radar 2]``
        -   The after radar image.
    *   -   ``[Placeholder for Radar 3]``
        -   The after radar image with the alert's outline in red.
    *   -   ``[Placeholder for Centroid QR]``
        -   A QR code that opens the alert's centroid in Google Maps (80 pt wide, or narrower to fit its table cell). Without a centroid, the marker is removed.

Images 1–3 are in false colour (near-infrared, red, green) and images 4–6 in true colour (red, green, blue). Images 1–6 show the optical pair as picked. The radar pictures show the radar pair as picked on the timeline (a handle that follows the optical pick gives the nearest radar image to its date, from the same pass as the other radar handle when one is within 30 days, otherwise from either pass), as VV, VH and the VV/VH ratio in red, green and blue. A picture with no image is replaced by a short note. The pictures keep the resolution of the finer of the two images (Sentinel-2 10 m, Sentinel-1 10 m, Landsat 15 m, Planet 4.77 m). The default template lays them out in a grid of three columns (before, after, after with the outline) and two rows (true colour, false colour), and puts the QR code beside the alert details. Its *Radar evidence* row (before, after, after with the outline) is removed from a report without a radar pair. A template without these markers gets a report with no pictures.

.. tip::

    To make a custom template, start from a copy of the default one. Keep every marker alone in its paragraph; in a table cell, a caption can follow it in a paragraph of its own.

The template can show two messages:

-   "… is not a Word file (.docx) in your SEPAL folder; the report template was not changed.": choose a .docx file.
-   **missing**, with "The file is gone: pick it again, or clear it to use the default template.": the card stays open until the file is chosen again or the field is cleared.

.. tip::

    When the alerts are split among evaluators, their review packages carry the questionnaire and the report template. If the questionnaire changes after the packages are built, build them again (see `Evaluation <defo-evaluation_>`_).

Next, go to the `Evaluation <defo-evaluation_>`_ step, where **Start analysis** starts reviewing.

.. _defo-evaluation:

Evaluation
----------

This step decides who reviews the alerts of the active set:

-   review them all yourself; or
-   split them among several evaluators. Each evaluator gets a *review package*, reviews their own alerts in their own SEPAL account, and sends back a *reviewed copy*, which is then merged into the project.

Open the **Evaluation** step of the **Workflow** panel, the last step of **Set up review**. It unlocks once the project has an alert set (see `Integrate & vectorize <defo-integrate_>`_). It works on the active set: a split belongs to one alert set.

In a project converted from a `version 1 recipe <defo-project-v1_>`_, the step reads "Not available for a project converted from version 1: it is reviewed by one person."

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/anim/evaluators.gif
    :alt: The alert set is split into packages, each evaluator reviews theirs, and the reviews are merged back

In the animation, red marks a confirmed loss and green a false positive.

Review mode
^^^^^^^^^^^

Under **Review mode**, select one of two checkboxes:

.. list-table::
    :header-rows: 1
    :widths: 30 70

    *   -   **Review mode**
        -   Description
    *   -   **Solo**
        -   You review every alert. Nothing else to set up: select **Start analysis**.
    *   -   **Multiple evaluators**
        -   The alerts are split among evaluators, and each one gets a review package. The evaluators table appears under it.

A project starts with neither checkbox selected. The note under them reads "Choose who reviews the alerts: only you, or several evaluators.", and the **Evaluation** step of the **Workflow** panel stays empty.

-   Selecting one checkbox clears the other; clearing the selected checkbox leaves no mode again.
-   **Solo** completes the step (its badge reads "1 evaluator").
-   **Multiple evaluators** completes the step once the alerts are split.
-   While a split exists, both checkboxes are disabled on **Multiple evaluators** (**Remove the split to switch to solo.**).

.. _defo-evaluation-group:

Review nearby alerts together
"""""""""""""""""""""""""""""

In its own card, under the review mode (and under the evaluators table with **Multiple evaluators**), the **Review nearby alerts together** checkbox lets `Analysis <defo-analysis-nearby_>`_ review neighbouring alerts as one group: "In Analysis, alerts within this distance can be reviewed with one verdict, one set of answers and one polygon." It works in both modes. Once it is selected:

.. list-table::
    :header-rows: 1
    :widths: 30 45 25

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **Distance (m)**
        -   How close, edge to edge, an alert must be to be offered in the group.
        -   300. From 10 to 5,000.
    *   -   **Include already reviewed alerts**
        -   Also offers alerts reviewed before grouping was on. "Unchecked, alerts reviewed before grouping was on are never offered."
        -   Cleared.

Some changes are locked:

-   Once groups are saved, grouping cannot be turned off and the distance cannot change: "2 groups are saved: remove them to turn grouping off."
-   A split fixes all three settings: "The alerts were split with grouping: remove the split to change it." (or "without grouping").
-   In a review copy, they are "Set by the project's creator."

.. _defo-evaluation-split:

Split the alerts
^^^^^^^^^^^^^^^^

.. shot: evaluation-split | The "Split the alerts" dialog of the demo project: Split by = Names, two name rows filled ("Ana", "Luis") with their close icons, Add evaluator, "Empty rows are skipped.", Include already reviewed alerts unchecked with its hint, and the Split button. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/evaluation-split.png
    :alt: Splitting the alerts between two evaluators

With **Multiple evaluators** selected, select **Split alerts…** under the review mode to open the **Split the alerts** dialog:

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    *   -   Field
        -   Description
        -   Default and limits
    *   -   **Split by**
        -   **Count**: the evaluators are named "Evaluator 1", "Evaluator 2"… **Names**: enter their names.
        -   **Count**.
    *   -   **Number of evaluators**
        -   With **Count**.
        -   2. From 1 to 50.
    *   -   **Evaluator 1**, **Evaluator 2**…
        -   With **Names**: one row per evaluator. **Add evaluator** adds a row; the cross removes one.
        -   Two empty rows. Empty rows are skipped; two rows cannot have the same name; at most 50.
    *   -   **Include already reviewed alerts**
        -   Also deals out alerts that are already reviewed. When cleared, they stay unassigned.
        -   Cleared.

Select **Split**. The alerts are dealt out one by one in the set's order (the **Order** chosen in `Integrate & vectorize <defo-integrate-options_>`_), like cards: the first to evaluator 1, the second to evaluator 2, and so on round the list. Each evaluator gets about the same number of alerts, spread over the whole order.

With **Review nearby alerts together** selected, the split never parts a group. Alerts within the distance of each other, edge to edge, chain into one group of nearby alerts. Each group goes whole to the evaluator with the fewest alerts so far. When one group holds more than an even share, the dialog warns: "One group of nearby alerts holds 30 alerts, more than an even share."

The evaluators table
""""""""""""""""""""

.. shot: evaluation-table | The Evaluation step of the demo project after the split, packages built and one copy merged: Review mode with the Multiple evaluators box ticked (both greyed out) and its note; the Evaluators table with rows "Ana" and "Luis" (Assigned, Reviewed, Merged date for one, a dash for the other) and their green cloud icons, plus the grey "Unassigned" row; "Built …" under it; the Regenerate packages and Merge reviewed copy… buttons; Start analysis. Crop to the Workflow panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/evaluation-table.png
    :alt: The evaluators table

.. list-table::
    :header-rows: 1
    :widths: 20 80

    *   -   Column
        -   Description
    *   -   **Evaluator**
        -   The evaluator's name. A last row, **Unassigned**, counts the alerts no evaluator got.
    *   -   **Assigned**
        -   The number of alerts the evaluator has.
    *   -   **Reviewed** column
        -   The number of them that are reviewed in *your* project (by you, or merged from the evaluator).
    *   -   **Merged**
        -   The date their reviewed copy was last merged, or a dash.

The cloud icon on each row downloads that evaluator's package once it is built.

Change or remove the split
""""""""""""""""""""""""""

**Edit split** (in place of **Split alerts…**) reopens the dialog as **Edit the split**:

-   **Re-split** deals the alerts again with the new names or count. It is a new split: reviews already merged stay, but packages already sent for the old split can no longer be merged (the dialog warns: **Packages already sent for this split will no longer merge.**).
-   **Remove split** clears every assignment. Reviews stay.

.. attention::

    Running `Integrate & vectorize <defo-integrate-replace_>`_ again on the same set replaces it: its reviews and its split are discarded, and reviewed copies of the old set can no longer be merged.

.. _defo-evaluation-packages:

Review packages
^^^^^^^^^^^^^^^

Select **Generate packages**. The app builds one .zip file per evaluator in the alert set's folder (the button reads "Building 1 / 2…"). Each package holds:

-   the set's alerts with their assignments;
-   the questionnaire;
-   the AOI;
-   the list of satellite scenes already found;
-   the earlier alerts that the set's alerts can be linked to (see `Earlier alerts <defo-analysis-earlier_>`_), as they are when the packages are built; and
-   the report template, when a custom one was chosen.

When they are ready, "Built (date and time)" shows under the table and each row's cloud icon becomes a download.

To share the packages:

1.  Download each evaluator's package and send it to them (by email, a shared drive…).
2.  The evaluator copies it into their SEPAL folder and imports it with **Import** in the `Project <defo-project-import_>`_ dialog.

The package opens as a review copy in Analysis, filtered to the evaluator's alerts, with the setup steps locked.

A package needs the AOI's shape. Until it is loaded, the step reads **Packages wait for the AOI geometry: open the AOI step to load it.**

If the `questionnaire <defo-questionnaire_>`_ changes after the packages are built, the cloud icons turn amber ("Built before the questionnaire changed: generate the packages again."). Select **Regenerate packages** and send the new ones.

.. _defo-evaluation-return:

What the evaluator does
^^^^^^^^^^^^^^^^^^^^^^^

.. shot: evaluation-return | The Evaluation step in an evaluator's review copy (imported from a demo package): the "Review copy for …" banner, the Return reviews card with "5 / 23 of your alerts reviewed", its cloud icon, "Built …", "Only your assigned alerts are returned." and the Regenerate reviewed copy button. Crop to the Workflow panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/evaluation-return.png
    :alt: The Return reviews panel in a review copy

In a review copy, the **Evaluation** step shows **Return reviews** instead: the number of the evaluator's alerts that are reviewed ("5 / 23 of your alerts reviewed") and **Generate reviewed copy**.

The evaluator:

1.  reviews their alerts in `Analysis <defo-analysis_>`_;
2.  selects **Generate reviewed copy**, then downloads it with the cloud icon (a .zip file ending in ``__reviewed.zip``); and
3.  sends it back to the project's creator.

Only the evaluator's assigned alerts that they reviewed are returned, with the links they ticked to earlier alerts. A reviewed copy holds the reviews as of its build: after reviewing more, select **Regenerate reviewed copy**. The evaluator can send copies as often as needed. When a newer copy is merged, alerts merged before and reviewed differently since show as conflicts: choose **Take theirs** to take the evaluator's latest reviews.

.. _defo-evaluation-merge:

Merge a reviewed copy
^^^^^^^^^^^^^^^^^^^^^

.. shot: evaluation-merge | The "Merge reviews from Ana" preview: the summary line "Ana: 3 new reviews, 1 conflicts, 1 unchanged, 0 ignored", the "Alerts you reviewed differently" choice with Keep mine selected and Take theirs, and the Merge button. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/evaluation-merge.png
    :alt: Previewing a reviewed copy before merging

To merge a reviewed copy:

1.  Copy the reviewed copy into your SEPAL folder.
2.  Select **Merge reviewed copy…** and choose it in **Reviewed copy (.zip)**. Choose one copy at a time.
3.  Read the preview, titled with the evaluator's name and shown before anything changes (see the table below).
4.  When there are conflicts, choose under **Alerts you reviewed differently**: **Keep mine** (the default) or **Take theirs**.
5.  Select **Merge**.

.. list-table::
    :header-rows: 1
    :widths: 20 80

    *   -   Count
        -   Description
    *   -   new reviews
        -   Alerts the evaluator reviewed that are not reviewed in your project. They are taken.
    *   -   conflicts
        -   Alerts that were also reviewed in your project (by you or an earlier merge), differently. A different link to an earlier alert counts as a difference.
    *   -   unchanged
        -   Alerts whose review is the same on both sides.
    *   -   ignored
        -   Alerts that are not assigned to this evaluator. They are never taken.

With grouping on, each count also gives its number of groups ("3 new reviews (1 group)"). A group is merged whole: when one of its alerts conflicts, the whole group is a conflict.

After the merge, the set's alerts are updated, a message reads "Merged N reviews from (evaluator).", and the **Merged** column shows the date.

The preview may also warn that "The questionnaire changed since the packages were made; answers are merged by question key.", or list columns it ignores. If the alert open in Analysis is among the merged ones, it is reloaded.

.. tip::

    In `Analysis <defo-analysis_>`_, the filter can show the alerts of one evaluator (or the unassigned ones) through its **Evaluator** attribute.

Common messages
^^^^^^^^^^^^^^^

"This copy is for set …; make it the active set to merge."
    Choose that set in the set selector of Analysis or the Overview first.

"The set was re-run since this copy was made." or "This copy was made for an earlier split."
    The copy no longer matches the set's alerts. It cannot be merged.

"This zip is a review package, not a reviewed copy."
    Choose the file the evaluator sent back.

"This return would break a group of alerts, so nothing was merged. Choose Keep mine, or ask the evaluator to update the app and send the review again."
    Taking the evaluator's reviews would split a group saved in your project. Choose **Keep mine**, or ask for a reviewed copy made with an up-to-date app.

"A review copy cannot merge reviewed copies; open the creator's project."
    Merge in the original project.

"This set has an attribute named 'evaluator'; rename that attribute layer and re-run the set."
    The set's alert table already has an ``evaluator`` column, from an attribute layer, so it cannot be split. In `Integrate & vectorize <defo-integrate-attributes_>`_, give that layer another name and run the set again (this replaces the set and its reviews).

"This set's alerts carry evaluator assignments but the project has no split record. Remove the split to start again."
    A split was written to the alerts but not to the project (e.g. the project was closed at that moment). Open **Edit split**, select **Remove split**, then split again.

"This alert set was rewritten while the split was being made, so nothing was changed. Try again."
    A review was saved or a copy merged at the same time. Split again.

"This alert set is being re-run in Integrate & vectorize. Try again once it has finished." (when splitting)
    Wait for the run to end.

"No alerts to assign." (when splitting)
    Every alert may already be reviewed: select **Include already reviewed alerts**.

.. _defo-analysis:

Analysis
--------

.. labels-ok: Google; Esri; Enter

Use the Analysis screen to review the alerts of the active set, one at a time. For each alert:

1.  Compare a *before* and an *after* satellite image.
2.  Give a verdict.
3.  Answer the project's questions.
4.  Save.

The alert's polygon can also be redrawn, by hand or with two auto-detection models, and the alert's files exported.

Open the screen
^^^^^^^^^^^^^^^

The screen opens with the active alert set, from any of these:

-   **Start analysis**, at the bottom of the `Evaluation <defo-evaluation_>`_ step;
-   **Analysis**, in the left rail; or
-   **Review alerts** in the `Overview <defo-overview_>`_, or the **Review** button of an alert clicked on the main map (see `View the alerts on the map <defo-integrate-map_>`_).

It needs an alert set: until `Integrate & vectorize <defo-integrate_>`_ has made one, the counter reads "No alert set is loaded". A set opens on the alert under review when the screen was last left (the position is saved with the project).

**Workflow**, in the upper-left corner, goes back to the workflow steps. The left rail stays usable on this screen: a click on a map folds it back when it is expanded and not pinned, and a pinned, expanded rail moves the screen to its right instead of covering the maps.

The screen
^^^^^^^^^^

.. shot: analysis-screen | The whole Analysis screen of the demo project at 1440×900, on an unreviewed alert in the middle of the set: the top bar (Workflow, "Analysis · <project>", the funnel, the Alert set selector, the tally "12 reviewed · 36 left" over its bar, the help icon, Previous · 13 / 48 · Next and the next-unreviewed icon); the two maps with titles "Before image" and "After image" each followed by an "Optical · Sentinel-2 2026-05-28 · 27%" / "Optical · Sentinel-2 2026-09-27 · 18%" chip and a "Radar" chip, the alert layers cleared in each map's layers menu so the images show bare, the layers icon at the top right of each map, the basemap thumbnail and the scale bar at the bottom left; the timeline under the maps with the optical and radar lanes, all handles placed; the right panel with Source / Detected / Status, the Verdict buttons, the Questions section open with the loss driver and the added "Access road nearby?" question, the Refine polygon section closed, and the dock (Export this alert "available after save", Save filled, Next, the next-unreviewed icon). No crop.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/analysis-screen.png
    :alt: The Analysis screen

.. list-table::
    :header-rows: 1
    :widths: 20 80

    *   -   Part
        -   Content
    *   -   Top bar
        -   The filter, the alert set, the review progress, the help and the navigation.
    *   -   The two maps
        -   The *before* image on the left side, the *after* image on the right side. They move together: pan or zoom one and the other follows.
    *   -   The timeline
        -   Under the maps: every image of the alert's area, on one date axis. Its two handles choose the before and the after image.
    *   -   The review panel
        -   On the right side: what the alert table says about the alert, the verdict, the questions, the drawing tools, the earlier alerts nearby, then a footer that stays at the bottom with the export section and the save buttons. Only this panel scrolls.

The help icon in the top bar opens **About analysis**, a short summary of this subsection.

.. _defo-analysis-topbar:

The top bar
^^^^^^^^^^^

.. shot: analysis-topbar | The top bar of the Analysis screen with the filter menu open below the funnel: "Filter alerts" title, Attribute = Evaluator, Values = Ana (23) selected as a chip, the Clear filter and Apply buttons; to the right the Alert set selector, the tally "5 reviewed · 18 left · filtered · 48 total" over its bar, and Previous · 06 / 23 · Next with the next-unreviewed icon. Crop to the top bar and the open menu.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/analysis-topbar.png
    :alt: The top bar with the filter menu open

From left to right:

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Control
        -   Description
    *   -   Funnel
        -   Opens the filter (see below). While a filter is on, the funnel is filled and a chip names it (e.g. "Evaluator: Ana"). The chip's cross removes the filter.
    *   -   **Alert set**
        -   The set under review: "period · sources · N alerts · N reviewed", newest first. Choosing another set makes it the project's active set, also for the other steps and the Overview.
    *   -   Progress
        -   "12 reviewed · 36 left" over a bar.
    *   -   **Previous** / **Next**
        -   The previous or next alert in the set's order. They stop at the first and the last alert.
    *   -   Counter
        -   The alert's place in the set ("13 / 48"). Select it to open **Jump to alert number**: enter a number and select **Go**, or press **Enter**. In a set made with this version, alerts are numbered from 1 and the place is the alert's number. A set made before keeps its numbers, which start at 0.
    *   -   **Next unreviewed alert** icon
        -   Goes to the next alert without a verdict, starting again from the top after the last one. Disabled when no other alert is left to review.

When the alert on screen has unsaved changes, every way to another alert asks first (see `Save the review <defo-analysis-save_>`_).

The order of the alerts is the **Order** chosen in `Integrate & vectorize <defo-integrate-options_>`_.

Filter the alerts
"""""""""""""""""

The filter keeps one attribute's values and hides the other alerts from the navigation. To filter the alerts:

1.  Select the funnel to open **Filter alerts**.
2.  In **Attribute**, choose what to filter on. The list offers **Evaluator** (when the set is `split <defo-evaluation-split_>`_), **Status**, **Kind** (when the set has `growth alerts <defo-integrate-growth_>`_: choose **Growth** to review them together), each question of the questionnaire, then the set's other columns that hold between 2 and 50 different values, such as the columns of an `attribute layer <defo-integrate-attributes_>`_. If the set has none, the menu reads "No attribute to filter by".
3.  In **Values**, select one or more values, each with its number of alerts (e.g. "Ana (24)"). An alert matches when it has any of them. Empty cells are listed as **Unassigned** for the evaluator and **(empty)** for other columns.
4.  Select **Apply**.

**Clear filter** removes the filter.

With a filter on:

-   **Previous**, **Next** and the **Next unreviewed alert** icon move among the matching alerts only;
-   the counter counts the matches ("06 / 24"), or reads "– / 24" while the alert on screen is not one of them, and the progress line ends with "filtered · 48 total";
-   the jump menu still takes the alert's number in the whole set, but refuses one the filter hides ("Alert 12 is not in the current filter"); and
-   when nothing matches, the counter reads "No alerts match this filter".

When a filter is applied, the screen moves to the alert on screen if it matches, else to the first unreviewed match, else to the first match. Alerts keep their numbers: a filter never renumbers them.

The filter lasts until it is cleared or another alert set is chosen. It is not saved with the project. A `review copy <defo-evaluation-return_>`_ opens already filtered to the evaluator's alerts.

The maps
^^^^^^^^

Both maps centre on the alert when it opens. A yellow dashed box marks the alert's extent.

.. list-table::
    :header-rows: 1
    :widths: 20 25 55

    *   -   Control
        -   Location
        -   Description
    *   -   **Layers**
        -   Upper-right corner of each map
        -   The map's layers, in three sections. Select a layer to show it on that map only.
    *   -   **Basemap**
        -   Lower-left corner of each map
        -   Hover over the thumbnail to choose the basemap: Google, Esri (both satellite), **SEPAL Light** or **SEPAL Dark**. The choice applies to both maps. The default follows the app's theme: **SEPAL Light**, or **SEPAL Dark** in the dark theme. Switching the theme swaps them; a satellite basemap stays.
    *   -   **Zoom to the alert**
        -   Upper-left corner of the after map
        -   Zooms both maps back to the alert.
    *   -   Scale bar
        -   Lower-left corner of each map, under the basemap thumbnail
        -   The map's scale, in metres or kilometres.

The **Layers** menu lists:

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Section
        -   Layers
    *   -   **Imagery**
        -   *True Color* (on) and *False Color* (near infrared, red and green; off): the image chosen for that map.
    *   -   **Alerts**
        -   *Original alert*: the outline of the alert's polygon from `Integrate & vectorize <defo-integrate_>`_, and of the other alerts of its group (see `Nearby alerts <defo-analysis-nearby_>`_), on by default and hidden while drawing. *All alerts*: the alert pixels of the whole set, half transparent (off). *Alert BB*: the alert's bounding box. *Defo Layer*: the polygon saved for the alert (see `Refine the polygon <defo-analysis-refine_>`_). *Earlier alerts* (see `Earlier alerts <defo-analysis-earlier_>`_). *Nearby alerts*, only when nearby alerts are reviewed together.
    *   -   **Additional layers**
        -   The `additional layers <defo-layers_>`_ marked **Show in Analysis**, turned off.

A map displays "Imagery failed to load" when the tiles of its image do not load.

.. _defo-analysis-timeline:

Choose the images: the timeline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. shot: analysis-timeline | The timeline strip of the demo alert at full width: the "Image sources" button with a blue, an orange and a pink dot (Sentinel-2, Landsat and Sentinel-1 on; no Planet), the cloud chip reading 40%, the "?" button, the Collapse the alert window and Expand every month icons, Image area = Normal; the track with "‹ +1 month" and "+1 month ›", the gold alert-window band with two collapsed month blocks in it, Sentinel-2 stripes on top, Landsat under them, a few faded half-height stripes over the cloud limit, the before handle left of the band and the after handle right of it with the "122 days apart" bracket between them; under that optical lane the folded radar strip, with the Sentinel-1 dots, its two hollow diamond handles (following the optical picks) and the chain and arrow icons at its left; the month names on the axis. Crop to the timeline card.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/analysis-timeline.png
    :alt: The image timeline

The timeline shows every image that covers the alert, from about two months before the alert was first detected to two months after it was last detected. Each image source that is switched on in the **Image sources** menu (see below) has its own band:

-   *Sentinel-2* stripes on top;
-   *Landsat* in the middle;
-   *Planet* (the NICFI monthly mosaic) as a bar across its month, only when your GEE account has NICFI access and you switched it on; and
-   *Sentinel-1* radar, only when you switched it on, with one band per pass (*Sentinel-1 asc* and *Sentinel-1 desc*).

A faded, half-height stripe is an image over the cloud limit. The gold band is the *alert window*: the dates over which the alert was detected. On a `growth alert <defo-integrate-growth_>`_, a grey band behind it marks the detection dates of each earlier alert it is linked to: choose a before image taken after the earlier clearing to see only the new loss.

Two handles above the track choose the images: the left one the before image, the right one the after image. The bracket between them states how many days apart they are ("49 days apart"), or warns "the same image on both sides".

To move a handle, use one of these methods:

-   Drag a handle and release it on the chosen image. The before handle cannot pass the after handle.
-   Click on a stripe: the nearest suitable handle moves to it. Images over the cloud limit cannot be selected.
-   With the keyboard: press **Tab** to reach a handle, move along the dates with the left and right arrow keys, jump to the first or last image with **Home** and **End**, and choose with **Enter**.

When an alert opens, the app chooses the image nearest *before* the alert window and the image nearest *after* it, among the images under the cloud limit. It never chooses an image inside the alert window (it would show only part of the clearing) or a Planet mosaic, but both can be chosen by hand. A side with no image under the cloud limit gets the least cloudy image within 30 days of the alert window, or the nearest one if there is none, even over the cloud limit (its map title shows its cloud cover); a side with no image at all is left "not set". A reviewed alert opens on the images it was saved with. If one of them is no longer available, its map title reads "Saved image not available; picked automatically".

Each map's title names its image in an **Optical** chip: "Before image · Optical · Sentinel-2 2026-07-28 · 3%" (collection, date, cloud cover). When the other collection has an image of the same day, a button in the title ("⇄ Landsat") switches to it.

When Sentinel-1 is on, a thin strip under the optical lane holds its images as dots, with two diamond-shaped handles. The arrow at the left of the strip unfolds it into a lane with one band per pass, and folds it again. The radar handles are hollow while they follow the optical picks: each sits on the radar image nearest to the date of its optical handle (from the same pass as the other radar handle when one is within 30 days, otherwise from either pass) and moves with it. Hollow handles are not saved: they are placed again when the alert opens. Drag one, or click a radar stripe in the unfolded lane, and it becomes filled: it is yours and stays where you put it, and saving the alert saves it. The chain icon at the left of the strip is linked while both handles follow the optical picks. Once you move one, the chain is broken: select it (**Follow optical**) to hand both handles back to the optical picks. A map whose side has a radar image gets a **Radar** chip next to the **Optical** one in its title: click a chip to choose what that map shows.

The toolbar above the track:

.. labels-ok: Tab; Home; End

.. list-table::
    :header-rows: 1
    :widths: 25 55 20

    *   -   Control
        -   Description
        -   Default
    *   -   **Image sources** button
        -   Opens the menu of image sources, in two groups: **Optical** (Sentinel-2, Landsat, Planet) and **Radar** (Sentinel-1). The button carries one coloured dot for each source that is on. Each row has a checkbox, the source's dot and name and, on the right, the number of its images in the current view; a second line ("3 over cloud limit") appears when the cloud limit hides some. Planet is greyed out, with "No access with this account", when your GEE account has no NICFI access. The choice is saved with the project (on a review copy, it lasts only for the session), and opening an alert whose saved image comes from a source that is off turns that source on.
        -   Sentinel-2 and Landsat on; Planet and Sentinel-1 off.
    *   -   **?** button
        -   Shows or hides a short legend of the timeline. This section describes the timeline in full.
        -   Hidden.
    *   -   **Collapse the alert window**
        -   Folds the months that lie wholly inside the alert window into blocks that give their number of images. Select a block to unfold its month; select a month's name on the axis to fold it. On a long alert, the folded months share less than half of the track, so that the months before and after the window keep their room. When they get too narrow to read, the folded months of each half-year form one block ("Jan – Jun 2024") with the year on the axis under it; select it to split it into one block per month.
        -   Folded when an alert opens.
    *   -   **Expand every month**
        -   Unfolds every month.
        -
    *   -   **Max cloud**
        -   The cloud limit, chosen in a menu of presets (10, 20, 40, 60 or 80 %, or **All images**), each with the number of images it keeps on the timeline. Images over it are faded and never chosen automatically. Planet mosaics and Sentinel-1 radar images have no cloud figure, so the limit never hides them.
        -   40 %.
    *   -   **Image area**
        -   How far around the alert the images reach: **Normal**, **Large** or **Extra large** (100 m, 1 km or 2.5 km around it). Larger areas take longer to load and export. Saving the review saves the area: the alert opens on it again, and its files and GIF are made on it. An alert never saved opens on **Normal**.
        -   **Normal**.
    *   -   **+1 month** (left and right of the track)
        -   Adds a month before or after the view. The right one stops at the current month.
        -

Sentinel-1 radar images differ from the optical ones:

-   They are fetched only once you turn Sentinel-1 on for the project: until its images are listed, its count reads "–".
-   Both passes are shown, one band per pass, labelled "Sentinel-1 asc" and "Sentinel-1 desc".
-   They are shown raw, with no speckle filter, as VV, VH and the VV/VH ratio in red, green and blue. In the map pane, a radar image has a single "Radar" layer, with no true/false colour switch.
-   Radar sees through clouds, so the cloud limit never hides these images. They have their own lane and handles (see above): the radar handles follow the optical picks until you move them.
-   Both pairs are used as picked. With Sentinel-1 on, the zip holds two composites, the optical one and the radar one, and the report adds a *Radar evidence* row; the radar images that were not placed by hand are marked in the report. The model and the GIF use the optical pair, whatever the radar handles show. **Build files** waits until the radar images are drawn and any radar handle you moved is saved.

The images come from an index of the images over the project's area, kept on disk and refreshed after 24 hours. While it loads, the toolbar reads "Loading the image index…"; an index older than a day reads "Index from (date)". If a refresh fails, the index on screen keeps working, and **Try again** retries.

.. _defo-analysis-panel:

The review panel
^^^^^^^^^^^^^^^^

The top of the panel shows what the alert table says:

.. list-table::
    :header-rows: 1
    :widths: 20 80

    *   -   Row
        -   Description
    *   -   **Source**
        -   The sources that detected the alert.
    *   -   **Detected**
        -   Its first and last detection dates.
    *   -   **Status** row
        -   Its review status, with its colour: **Not reviewed**, **Reviewed: confirmed**, **Reviewed: false positive** or **Reviewed: needs revision**.
    *   -   **Group**
        -   For an alert reviewed with nearby alerts: "group of 4". Hidden otherwise.
    *   -   **Kind**
        -   Whether the alert grows from earlier loss (see `Growth of earlier loss <defo-integrate-growth_>`_): **Growth** (a purple chip), **Growth · under minimum area**, or **New · under minimum area** (a small alert whose links were all removed). Hidden for a new alert.
    *   -   **History**
        -   For an alert linked to earlier loss: the alerts of its history and the area they confirm, for example "3 alerts · 2.1 ha confirmed since Aug 2026 (+0.3 ha not reviewed)". The area counts once where shapes overlap. Hidden when the alert has no history.

If the active set is out of date or its files are missing, an orange line above it says so, as in the `Overview <defo-overview_>`_. The review is still possible.

.. shot: analysis-console | The review panel on an alert being reviewed: Source "GLAD-L, RADD and GLAD-S2", Detected "2026-06-13 → 2026-09-27", Status chip "Not reviewed"; under Verdict the three buttons with True alert filled; the Questions section open with its badge "1 of 2 · required missing", question 1 "Loss driver" with Agriculture expansion picked in its list and a check mark, question 2 "Access road nearby?" with its Required tag and no answer; the dock with Export this alert (badge "available after save"), Save filled, Next and the next-unreviewed icon, and the orange "Unsaved changes on this alert" line. Crop to the right panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/analysis-console.png
    :alt: The review panel: verdict and questions

Verdict
"""""""

Under **Verdict**, select one of:

.. list-table::
    :header-rows: 1
    :widths: 20 30 50

    *   -   Button
        -   Stored status
        -   Use it when
    *   -   **True alert**
        -   **Reviewed: confirmed**
        -   The images show forest loss where the alert is.
    *   -   **False positive**
        -   **Reviewed: false positive**
        -   They show no forest loss: clouds, shadows, a seasonal change…
    *   -   **Needs revision**
        -   **Reviewed: needs revision**
        -   No decision is possible yet, or the alert needs a second look.

An unreviewed alert opens with no verdict: nothing is chosen automatically. A reviewed alert opens on its saved verdict and answers.

Questions
"""""""""

The **Questions** section holds the questions of the `questionnaire <defo-questionnaire_>`_, in their order and numbered. Once a verdict is chosen, it shows only the questions asked for that verdict. The section's badge counts the answers ("1 of 2 answered") and turns orange when a required question has no answer ("1 of 2 · required missing").

-   A question with one answer shows its options as tiles: select one.
-   A question with several answers shows them as chips: select each one that applies.
-   A question that allows typed answers is a list that also accepts typing (**Pick or type answers**).

With no questions in the project, the section reads "This project asks no questions: add some in the Questionnaire step."; when the chosen verdict asks none, "No questions are asked for this verdict."

A **Required** tag marks a question that must be answered before saving. The section starts open or closed as set by **Show the questions expanded in Analysis** in the questionnaire. It opens by itself when the chosen verdict asks a required question with no answer yet, and when a save is refused for that reason.

.. _defo-analysis-refine:

Refine the polygon
""""""""""""""""""

The alert's polygon comes from the alert pixels. In **Refine polygon**, draw the area that was actually lost instead. The saved polygon is stored with the review, shown as *Defo Layer* on the maps, and its area becomes the alert's area. The section's badge reads "nothing drawn" or, for example, "2 shapes · 1.3 ha".

.. shot: analysis-refine | The after map in drawing mode, beside the open Refine polygon section: on the map, the drawing toolbar at the top left (draw polygon, trash), the Fill holes / Remove hole bar under it, the hint "Right-click a vertex to delete it", the patches Model 1 found, drawn with their vertices; in the panel, Stop drawing (in Start drawing's place) and Save drawing, the Model 1 row with Run, the Remove from map icon and "Found 9 patches · 25.9 ha", the Model 2 row with Run and the Add to map icon greyed; the badge "nothing drawn" (no drawing saved yet) and the dock's state line "Save your drawing before saving this review". Crop to the after map and the right panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/analysis-refine.png
    :alt: Drawing the polygon of an alert

To refine the polygon:

1.  Select **Start drawing**. Both maps switch to drawing mode, the alert's box is hidden, and the saved polygon (if any) becomes the drawing, in blue. **Stop drawing** takes the button's place.
2.  Edit the drawing on either map; the other follows:

    -   The polygon button in the upper-left corner draws a new shape: click on its corners, then click on the first one to close it.
    -   Drag a corner to move it, click on the small marker in the middle of a side to add a corner, and right-click a corner to delete it. An edit that would make a shape cross itself is undone.
    -   The bin button deletes the next shape clicked. Its actions **Select area** (drag a box around the shapes to delete) and **Clear all** ask for confirmation first ("Delete 2 shapes?", **Cancel** / **Delete**), with the shapes concerned in red. Press **Esc** to cancel.
    -   **Fill holes** removes the holes of the selected shape, or of every shape when none is selected. **Remove hole**: click inside a hole to remove it; press **Esc** or select the button again to stop.

3.  Select **Save drawing**. The drawing becomes the alert's polygon. A drawing with no shape removes the polygon.
4.  Select **Stop drawing** to leave drawing mode. If the drawing has changes not saved with **Save drawing**, the **Discard unsaved drawing?** dialog asks first: **Keep drawing**, **Save and stop** or **Discard changes**.

.. important::

    **Save drawing** does not save the review: select **Save** afterwards. Until the drawing is saved, the footer reads "Save your drawing before saving this review" and the review cannot be saved.

The two models
##############

Under the drawing buttons, two convolutional neural networks (CNNs) can find the loss on the before and after images on screen: **Model 1** ("Smaller and faster model") and **Model 2** ("Larger but slower model").

To use a model:

1.  Select **Run** on a model's row. The app downloads the two images (the area set by **Image area**) and runs the model. It takes a while; the run shows in the task list.
2.  Read the result on the row (e.g. "Found 3 patches · 2.1 ha"). Patches smaller than the set's **Minimum cluster size** are left out. When the model found nothing, a red warning icon appears instead ("Model did not find forest loss polygons").
3.  Select the map icon with a plus sign (**Add to map**) to add the patches to the drawing (it starts drawing mode if needed): lime for **Model 1**, purple for **Model 2**. The icon then turns into a minus sign (**Remove from map**), which takes them off again.
4.  Edit the result like any drawing, then select **Save drawing**.

Choosing other images or another **Image area** drops the models' results: run them again. If another alert is opened while a model runs, its result is not added ("The model finished after you moved to another alert: its prediction was not added.").

.. _defo-analysis-earlier:

Earlier alerts
""""""""""""""

This section appears when the active set's period has earlier periods with alert sets. It lists the earlier loss near the alert: the alerts of earlier periods reviewed as **Reviewed: confirmed** or **Reviewed: needs revision**, within the distance set in **Within**, in metres (100 m by default, from 10 m to 50 km), plus every alert linked to this one, however far. Use it to check whether an alert continues a clearing already reported, and to link it to that clearing.

The alerts are grouped by period, newest first. Each row shows:

-   a bar in the period's colour;
-   a box, ticked when the alert is linked to this one;
-   the earlier alert's number and area ("#12 · 3.4 ha"), and its status; and
-   how it relates to this alert: "touches" (linked by `Integrate & vectorize <defo-integrate-growth_>`_), "touches · not linked" (the link was removed) or its distance ("40 m").

Select an alert's number to zoom both maps to it.

To link or unlink an alert, tick or clear its box. The change is part of the review: the footer reads "Unsaved changes on this alert", and **Save** saves it with the verdict. Ticking an alert of an earlier period makes this alert a growth alert, even if it does not touch it.

A growth alert smaller than the **Minimum cluster size** is in the set only because of its link. Clearing its last link asks first (**Unlink from the earlier alert?**): for example "Alert #14 is 0.2 ha, under the 0.5 ha minimum. It is an alert only because it is linked to #12." Select **Unlink** to clear the link: the alert stays in the set as **New · under minimum area**.

Some rows have no box:

-   "via #12": the alert belongs to the history through another link (here, alert 12). Clearing the box of alert 12 removes it too.
-   "earlier set was re-run": the earlier alert's set was made again in `Integrate & vectorize <defo-integrate-replace_>`_, so the link no longer points at the same alert. The row is greyed, is not counted in the history, and the link is dropped the next time this alert is saved.

A linked alert that was later reviewed as a false positive stays ticked with "now false positive". It is greyed and left out of the history; clear its box to remove the link.

Turn on **Show on the maps** to outline the listed alerts on both maps. The colour is the period's, and a small legend lists the periods shown, with "solid: confirmed · dashed: needs revision · thick: linked". The switch starts on for a growth alert; on other alerts it keeps your last choice. When the list covers several periods, the **Periods** menu hides some of them. The badge reads "off", "none within 100 m" or, for example, "4 within 100 m · 1 linked".

In a `review copy <defo-evaluation-return_>`_, the list comes from a snapshot of the earlier alerts taken when the packages were built: the section reads "Earlier alerts as of (date)", or "No earlier alerts in this copy" for a package made by an older version of the app.

.. _defo-analysis-nearby:

Nearby alerts
"""""""""""""

This section appears only when **Review nearby alerts together** is selected in `Evaluation <defo-evaluation-group_>`_. One clearing often makes several small alerts side by side. Review them together: one verdict, one set of answers, one pair of images and one polygon for all of them.

The section lists the alerts within the distance set in **Evaluation**, measured edge to edge from the alert on screen: the ticked ones first, then the nearest others, at most 50 ("12 more in range not listed"). Each row shows:

-   a box, ticked when the alert is part of the next save;
-   the alert's number (select it to zoom both maps to it), its first detection date and its area;
-   its distance ("40 m"), or "in this group";
-   "group #12" when it belongs to another group;
-   its status; and
-   in a split set, "assigned to Ana", greyed and with no box, for an alert of another evaluator.

The list offers the alerts not reviewed and the alerts reviewed in a group. Alerts reviewed before grouping was on are offered only with **Include already reviewed alerts**.

The listed alerts are outlined on both maps (*Nearby alerts* layer). Click on a map near an outline to tick or clear that alert. **Select all** ticks every listed alert and **Clear** clears them. The badge reads "3 selected", "5 within 300 m" or "none within 300 m". When a ticked alert lies outside the images, a line says "Some selected alerts are outside the image area: pick a larger area on the timeline."

To review a group:

1.  Tick the alerts that show the same clearing.
2.  Give the verdict, answer the questions, choose the images and draw the polygon as for one alert.
3.  Select **Save**, which then reads "Save for 4 alerts".

When the save changes other reviews, the **Save this group?** dialog lists them first, for example:

-   "#15 (Reviewed: confirmed): its review is replaced";
-   "#16 (Reviewed: confirmed): moves from group #9" or "joins with group #9" (a whole group joins when its main alert is ticked); and
-   "#17 (Not reviewed): leaves the group and goes back to not reviewed" (an alert of this group left unticked).

Select **Save** or **Cancel**.

Every alert of the group gets the same verdict, answers, images and links to earlier alerts. The alert on screen when the group is first saved is its *main* alert: it keeps the drawn polygon. When the group has a drawing, the other alerts get an area of 0, so that the loss counts once.

An alert of a saved group opens with the banner "Reviewed as a group of 4 (main alert #12)", and the **Group** row of the panel reads "group of 4". The *Original alert* layer outlines the whole group. On an alert other than the main one, **Remove from group** takes it out of the group: confirm with **Remove**. The alert goes back to not reviewed.

A group needs one evaluator: "These alerts are assigned to different evaluators: a group needs one." In a review copy, only your own alerts can join: "Some of these alerts are not assigned to you."

.. _defo-analysis-save:

Save the review
^^^^^^^^^^^^^^^

The *dock* stays at the bottom of the panel: the **Export this alert** section, then the buttons, then a state line.

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Button
        -   Description
    *   -   **Save**
        -   Saves the review and stays on the alert. With nearby alerts ticked, it reads "Save for 4 alerts".
    *   -   **Next**
        -   Opens the next alert (the next match under a filter).
    *   -   **Next unreviewed alert** icon
        -   Opens the next alert without a verdict, as in the top bar.

The filled button shows the next step: **Save** while the alert has unsaved changes or no saved review, **Next** once the review is saved.

With unsaved changes, **Next**, the icon and the top bar's **Previous**, **Next**, **Go** and icon ask first. The buttons give way to "This alert has unsaved changes": **Discard** drops the changes and moves on, **Stay** keeps you on the alert.

A change started somewhere else (a **Go** in **Overview** or in a map popup, the alert set picked in **Overview**, or opening, creating, renaming or deleting the open project in **Project**) asks in the **Unsaved changes in Analysis** dialog, over the window you are in. **Continue anyway** drops the changes and does what you selected; **Open Analysis** cancels it and shows the alert, so you can save it. Closing the dialog does nothing.

The state line reads "Unsaved changes on this alert", "Save your drawing before saving this review" or "Saved 14:32".

A save writes into the alert set:

-   the verdict, as the alert's status;
-   the answers to the questions asked for that verdict (the others are left empty);
-   the before and after images chosen, so that the alert reopens on them;
-   the polygon saved in **Refine polygon**, with its area as the alert's area;
-   the earlier alerts ticked in `Earlier alerts <defo-analysis-earlier_>`_, as the alert's links;
-   with nearby alerts ticked, the group (see `Nearby alerts <defo-analysis-nearby_>`_);
-   who reviewed it and when: ``reviewed_by`` (your SEPAL user name, looked up once per session; left empty if it is unknown) and ``reviewed_at`` (the time, in UTC, e.g. ``2026-11-11T14:03:22Z``). A group's members get them too, and an alert reset to not reviewed loses them; and
-   the names of the administrative areas under the alert, if `Integrate & vectorize <defo-integrate_>`_ could not fill them (from the FAO GAUL 2024 boundaries). Names saved by earlier reviews are kept. If the project has no boundaries yet, the first such save downloads them once, and its progress reads "Fetching administrative boundaries for this project (once)…" meanwhile.

``admin1`` is the country, ``admin2`` the first-level unit and ``admin3`` the second-level unit. In a group, each alert keeps its own names; the group's single-alert file and report show all the names of the group.

Reviews show at once in the progress bar, in the set selector and in the `Overview <defo-overview_>`_. A review can change at any time: open the alert, change it and save again.

Export the alert
^^^^^^^^^^^^^^^^

**Export this alert**, at the top of the dock, builds the alert's files once it is saved: a .zip file with its GeoPackage and images, a Word report and, for a true alert, an animated GIF. See `One alert, from Analysis <defo-export-alert_>`_.

.. shot: analysis-footer | The dock of the review panel after Save on a true alert: Export this alert open with its badge "ready to build", the Alert data, Alert report and Timelapse tiles greyed, the Build files tile "Makes the files above from the saved review", then Save outlined, Next filled, the next-unreviewed icon and the green "Saved 14:32" line. Crop to the dock.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/analysis-footer.png
    :alt: The footer: export section and save buttons

Keyboard
^^^^^^^^

The screen has no global keyboard shortcuts. The keys that work:

.. labels-ok: Esc; ←; →; ?

.. list-table::
    :header-rows: 1
    :widths: 30 20 50

    *   -   Key
        -   Location
        -   Action
    *   -   **Tab**, **←** **→**, **Home**, **End**, **Enter**
        -   Timeline handles
        -   Reach a handle, move it along the dates, jump to the first or last image, choose the image.
    *   -   **Enter**
        -   Jump menu
        -   Same as **Go**.
    *   -   **Esc**
        -   Maps
        -   Cancels **Select area** or a delete confirmation; stops **Remove hole**.

Common messages
^^^^^^^^^^^^^^^

"Answer under 'Verdict' before saving."
    Choose a verdict first.

"Answer “(question)” before saving."
    A required question has no answer; the **Questions** section opens on it.

"A false positive cannot have a drawn deforestation polygon: delete the polygon or change the answer."
    Remove the polygon in **Refine polygon** (an empty drawing, then **Save drawing**), or choose another verdict.

"Save your drawing before saving this review."
    Select **Save drawing**, or stop drawing and discard the changes.

"This alert set was rebuilt while you were reviewing it, so the alerts on screen are out of date and this review was not saved."
    The set was run again in `Integrate & vectorize <defo-integrate_>`_. Review the rebuilt alerts.

"The active alert set changed while saving, so this review was not saved." or "These alerts belong to another alert set than the active one, so they were not saved into it."
    Another set became active meanwhile. Open the alert again and save.

"Saved, but you changed this alert while it was saving: save again to store those changes."
    Save again.

"The before and after images for this alert are not both ready, so the model has nothing to run on."
    Choose both images and let the two maps finish drawing them.

"No images cover this alert in this window."
    Add months with **+1 month**, or raise **Max cloud**.

"The images in this window are all in sources you have switched off."
    Switch the source back on in the **Image sources** menu.

"Could not draw the before image: …" or "Could not draw the after image: …"
    Choose the image again, or another one.

.. _defo-overview:

Overview
--------

The Overview sums up an alert set, or every period at once: how many alerts it holds, how many are reviewed, and how much loss was confirmed, where and when; how the source pixels became alerts; and the files to download. Its figures follow the reviews as they are saved.

Open the Overview
^^^^^^^^^^^^^^^^^

Select **Overview** in the left rail. It opens as a large dialog over the map; close it with its cross. It shows the active alert set, or "No alert set yet. Run Integrate & vectorize to produce one." when the project has none.

.. shot: overview-dashboard | The Overview dialog of the demo project, on the newest set with about a third of its 48 alerts reviewed, measure Area (ha), Status tab open: the header with the Alert set selector, Area (ha) filled and Alert count outlined, Review alerts; the four key figures (Confirmed loss 305 ha with "▼ 780 less than 2026-09-01 → 2026-09-30", Detected in total 1,177, Reviewed 33 % "16 of 48 alerts", Largest alert 31.9 "Alert 1 · Peru ·…"); the Map layers button; the tab row; the By review status card with its table and How big the alerts are. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/overview-dashboard.png
    :alt: The Overview dashboard

The header
^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 25 55 20

    *   -   Control
        -   Description
        -   Default
    *   -   **Alert set**
        -   The set summed up. Choosing another one makes it the project's active set, as in `Analysis <defo-analysis-topbar_>`_. Its first item, "All periods · 3 sets · 133 alerts", sums the newest set of every period instead, and leaves the active set as it is.
        -   The active set.
    *   -   **Area (ha)** / **Alert count**
        -   Whether every figure of the page counts hectares or alerts.
        -   **Area (ha)**.
    *   -   **Review alerts**
        -   Closes the Overview and opens `Analysis <defo-analysis_>`_ on this set. Disabled when the set has no alerts, and for **All periods** ("Pick one period to review its alerts").
        -

If the set is out of date or its files are missing, an orange line says so ("This set was built from inputs that have changed since…" or "This set's files are missing from the project folder…"). The figures still show what the set holds. Run `Integrate & vectorize <defo-integrate-outdated_>`_ again to rebuild it, which discards its reviews.

The key figures
^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Figure
        -   Content
    *   -   **Confirmed loss**
        -   The area (or number) of alerts reviewed as **Reviewed: confirmed**. With an earlier period, it compares with that period, in the page's measure ("▼ 780 less than 2026-09-01 → 2026-09-30", or "▲ … more than …"). **All periods** has no comparison.
    *   -   **Detected in total**
        -   The area (or number) of all the set's alerts, whatever their status.
    *   -   **Reviewed**
        -   The share of alerts that have a verdict, and "16 of 48 alerts". It always counts alerts.
    *   -   **Largest alert**
        -   The largest alert's area, its number, its country and its date. It always counts hectares. The country shows for every alert of a set made with this version; in a set made before, once the alert is saved. The number is the alert's number: in a set made with this version, the same as the Analysis counter's number (a set made before numbers from 0, so it is the counter's number minus one).

.. _defo-overview-layers:

Map layers
^^^^^^^^^^

The **Map layers** button beside **Review alerts** opens a list of the layers the Overview can draw on the main map, grouped by period. Tick a layer to draw it: the Overview closes, to show the map. Clear it to take the layer off. Every layer is named with its period ("Alerts · 2026-01-01 → 2026-01-31"), in the list, on the map and in the legend.

-   **This set**: the selected set's **Alerts**, coloured by status, and its not-analysable pixels (too small, or over the alert cap), when the set's run recorded them.
-   **Other periods**: the alerts of every other period's newest set, newest period first, each on its own. When there are several, **Show all** and **Hide all** draw or clear them together.
-   With **All periods** selected, **Every period** lists the alerts and the not-analysable pixels of each period's newest set.

A layer's box is greyed while the layer is being built.

.. _defo-overview-figures:

The tabs
^^^^^^^^

The figures are grouped in tabs, each with two cards side by side.

.. shot: overview-figures | The Overview dialog of the demo project, Pixels tab open, measure Area (ha): the From source pixels to alert pixels card (Source alert pixels, Removed by masks, Kept by the masks, Combined, overlaps once, Too small to analyse, Over the alert limit, In alerts, each with its bar, value and hectares) and the By source card with its table and Masks used. Crop to the dialog.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/overview-figures.png
    :alt: The Overview figures

.. list-table::
    :header-rows: 1
    :widths: 20 80

    *   -   Tab
        -   Cards
    *   -   **Status**
        -   **By review status**: one bar split by status, then a table with, per status, the number of alerts, their area, their share of the measure and the median alert size, and a **Total** row. **How big the alerts are**: the alerts by size, from under 0.5 ha to 25 ha or more.
    *   -   **Over time**
        -   **Across monitoring periods**: one column per monitoring period of the project, split by status, from its newest alert set; a period still under review shows its unreviewed share hatched. With one period only, it reads "This project has one monitoring period. Add a second one and its trend is charted here." **When the loss was detected**: the alerts by the week they were first detected, split by status. Hatched weeks are look-back weeks: they fall before the period started (see `What earlier periods already reported <defo-integrate-earlier_>`_).
    *   -   **Place & source**
        -   **By administrative area**: the reviewed alerts by area, up to eight, the most confirmed loss first: their **Area (ha)**, the hectares **Reviewed: confirmed** and the number of **Alerts**. **Country** or **Province / state** sets the level; a province is shown with its country ("Peru › Madre de Dios"). The areas come from the FAO GAUL 2024 boundaries, recorded for every alert by `Integrate & vectorize <defo-integrate_>`_, but only reviewed alerts are counted; an alert with none recorded is counted as **Not recorded**, and an alert across a border is listed under every area it falls in. **By alert source**: the alerts by the combination of sources that detected them.
    *   -   **Answers**
        -   One card per `question <defo-questionnaire_>`_, with the answers given to reviewed alerts: the five most frequent, then **Other** and **No answer**. An alert with two answers counts under each. Only shown when the project has questions; the tab shows their number.
    *   -   **Pixels**
        -   How the pixels of the sources became the pixels of the alerts (see below).
    *   -   **Clusters**
        -   How those pixels became alerts, the nearby alerts and the alerts linked to earlier loss (see below). The tab shows the number of alerts.
    *   -   **Files**
        -   The **Export alerts** card (see `The whole set, from the Overview <defo-export-set_>`_) and, with **All periods** selected, the **Summary of all periods** (see below).

When a figure cannot be drawn, its card reads "This figure could not be drawn; its numbers are below." and lists them.

Pixels
""""""

The **From source pixels to alert pixels** card follows the pixels step by step, each with a bar, a number and its hectares:

-   **Source alert pixels**: the pixels the sources flagged in the period, all sources together;
-   **Removed by masks** and **Kept by the masks**: what the masks of `Harmonize <defo-harmonize_>`_ took out and left;
-   **Combined, overlaps once**: the pixels once the sources are combined, a pixel flagged by two sources counted once;
-   **Too small to analyse** and **Over the alert limit**: the pixels of clusters below the minimum area, and of clusters left out by the alert limit of `Integrate & vectorize <defo-integrate_>`_; and
-   **In alerts**: the pixels of the set's alerts.

The **By source** card gives the same counts per source (**Alert px**, **Masked**, **Kept**), each with an eye that draws the source's raster on the map, and the **Masks used** with their **Mode**.

A count shows "—" when the set was made before the app recorded it: "—: not recorded for this set. Run Integrate & vectorize again to count it."

.. _defo-overview-growth:

Clusters
""""""""

The **From clusters to alerts** card counts the **Clusters formed** by connected alert pixels, those **Under the minimum size** and **Over the alert limit**, the **Alerts** made from the rest, and how many are **Reviewed**.

Under it, **Nearby alerts** shows how the set's alerts chain into groups: alerts within the distance of **Review nearby alerts together** (see `Evaluation <defo-evaluation-group_>`_), edge to edge, form one group. Its table has two rows:

-   **Found by distance**: the groups the distance makes, and their alerts ("20 of 48 · largest 5"); and
-   **Saved as a review group**: the groups saved in Analysis, and their alerts.

When grouping is off, the card uses the project's distance and adds "Reviewing together is off · turn it on in Evaluation."

The **Linked to earlier loss** card follows the `growth alerts <defo-integrate-growth_>`_: new alerts that touch a clearing confirmed in an earlier period (draw the earlier sets from `Map layers <defo-overview-layers_>`_). Its headline gives the growth alerts and their area ("3 growth alerts · 4.2 ha", or only the number with **Alert count**); the line under it splits them ("Growth: 2 · Under minimum area: 1") and says how many are reviewed. Without any, it reads "No alert is linked to earlier loss."

Its table lists the histories that include an alert of this set, the largest confirmed area first:

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Column
        -   Content
    *   -   **Monitoring periods**
        -   The first and the last period of the history.
    *   -   **Alerts**
        -   The number of alerts in the history, all periods together.
    *   -   **Confirmed (ha)**
        -   The area of the history's alerts reviewed as **Reviewed: confirmed** or **Reviewed: needs revision**, counted once where their shapes overlap.
    *   -   **This set adds (ha)**
        -   The area of this set's alerts in the history, false positives left out.
    *   -   **Review**
        -   Closes the Overview and opens this set's alert of the history in `Analysis <defo-analysis_>`_.

Summary of all periods
""""""""""""""""""""""

With **All periods** selected, the **Files** tab ends with a table of every period, one row each: its **Alerts**, **Confirmed ha**, **Reviewed** share, **Source px**, **Clusters**, review **Groups** and alerts **Linked** to earlier loss. The **Summary CSV** tile under it writes the same table to ``periods_summary.csv`` in the project folder; select it again to download the file. When the numbers have changed since (reviews saved, a set rebuilt), the tile reads "Numbers changed since" and an **Update** button writes it again.

All periods
^^^^^^^^^^^

Choose **All periods** in the **Alert set** selector to sum the newest set of every period: the key figures, the tabs and the export then cover them all. Hectares and alerts are added up; a pixel count that one set did not record shows "—". **Map layers** lists every period's layers (see `Map layers <defo-overview-layers_>`_); **Review alerts** needs one set, so it is disabled. In the **Files** tab, the **Export alerts** card writes every period's alerts to one file, with a ``period`` column (see `The whole set, from the Overview <defo-export-set_>`_).

Common messages
^^^^^^^^^^^^^^^

"No alert set yet. Run Integrate & vectorize to produce one."
    The project has no set: run `Integrate & vectorize <defo-integrate_>`_.

"This set has no alerts."
    The set was made but found no alert; nothing is charted.

"This set's alerts could not be read: …"
    The set's files are damaged or missing. Run `Integrate & vectorize <defo-integrate_>`_ again.

"No reviewed alert answered this yet." or "No alert has been reviewed yet, so no administrative area is on record."
    Review alerts in `Analysis <defo-analysis_>`_ to fill these cards.

.. _defo-export:

Export
------

The app exports alerts in two ways:

-   the files of one reviewed alert, from the Analysis screen; and
-   the alerts of a whole set, or of every period, from the Overview.

Every file is written into the alert set's folder in the project (``periods/<start>_<end>/sets/<set>/``, see `Project <defo-project_>`_), so it can also be found there later, in SEPAL's file browser. The files of **All periods** go to the project folder.

.. _defo-export-alert:

One alert, from Analysis
^^^^^^^^^^^^^^^^^^^^^^^^

The **Export this alert** section sits at the top of the dock of the `Analysis <defo-analysis-save_>`_ review panel. It works on the alert on screen, once its review is saved: its badge reads "available after save", then "ready to build", then "3 files ready".

.. shot: export-alert-files | The Export this alert section of the Analysis dock after Build files on a true alert of the demo project: badge "3 files ready", the Alert data tile "GeoPackage + before/after GeoTIFF · 2.9 MB", the Alert report tile "Word, from the project's template", the Timelapse tile "Animated GIF", each as a download link, and the Rebuild files tile "Makes them again from the saved review"; Save, Next and the next-unreviewed icon under them, the green "Saved 14:32" line. Crop to the dock.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/export-alert-files.png
    :alt: The alert's files, ready to download

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Tile
        -   Description
    *   -   **Build files**
        -   Builds the alert's data and report from the saved review ("Makes the files above from the saved review"). It is disabled until the review on screen is saved: it then reads "Save this alert first", or "Save your changes first" when there are unsaved changes. A reviewed alert opened on the images it was saved with is ready at once. It runs in the task list ("Building files…") and takes a while: it downloads the before and after images.
    *   -   **Alert data**
        -   Downloads a .zip file: the alert's GeoPackage, its before and after images as one GeoTIFF (two with Sentinel-1 on: optical and radar) and, for a true alert, its GIF.
    *   -   **Alert report**
        -   Downloads the alert's Word report.
    *   -   **Rebuild files**
        -   Builds the files again (e.g. after the review changed).
    *   -   **Timelapse**
        -   Makes and downloads an animated GIF of the alert (see below). For an alert not saved as a true alert, it reads "True alerts only".

The files are named after the alert's number (``<n>``). In a set made with this version, it starts at 1 and is the counter's number. A set made before keeps its numbers, which start at 0, and its file names (``alert_0``…):

.. list-table::
    :header-rows: 1
    :widths: 40 60

    *   -   File
        -   Content
    *   -   ``alert_<n>.gpkg``
        -   The alert as one feature with its attributes and answers (the answers in the app's current language). Its geometry is the polygon drawn in `Refine the polygon <defo-analysis-refine_>`_, or else the alert's cluster polygon, never the bounding box. ``geometry_source`` says which (``drawn`` or ``detected``; ``group`` is explained below), and ``detected_area_ha`` is the cluster's area as detected, while ``area_ha`` stays the reviewed area. A second layer, ``alert_<n>_detected``, holds the cluster polygon.
    *   -   ``alert_<n>_<before>_<after>.tif``
        -   The before and after images, cut to the **Image area**. The two date parts name each image's collection (``s`` Sentinel-2, ``l`` Landsat, ``p`` Planet, ``a``/``d`` Sentinel-1 ascending/descending) and date. With Sentinel-1 on there are two: the optical pair and the radar pair, each as picked.
    *   -   ``alert_<n>_<before>_<after>.gif``
        -   The timelapse, when made, named like the GeoTIFF.
    *   -   ``alert_<n>.zip``
        -   The GeoPackage, the GeoTIFF (or the two) and, for a true alert, the GIF.
    *   -   ``alert_<n>.docx``
        -   The Word report.

For an alert of a group (see `Nearby alerts <defo-analysis-nearby_>`_), the files describe the whole group: the GeoPackage holds one feature with the group's summed area, its first and last detection dates, its sources, ``group_size`` (the number of alerts) and ``group_alerts`` (their numbers, e.g. "12, 15, 16"), and the GIF outlines every alert of the group. Its geometry is the group's drawn polygon; without one, it is the union of the group's clusters (``geometry_source`` ``detected``). The ``_detected`` layer holds that union of clusters. The administrative names of the file and the report are all those of the group's alerts.

The links of the tiles are for the review on screen. Choosing other images, saving the alert again or changing the report template hides them: build the files again.

The report
""""""""""

The report is built from the project's Word template, chosen in the `Questionnaire <defo-questionnaire-template_>`_ step, or from the app's default template when the project has none. The template's placeholders are filled with the alert's attributes, its answers and its images. With Sentinel-1 on, the pictures show the optical pair as picked, a *Radar evidence* row shows the radar pair, and the summary names both the optical and the radar images. See `The report template <defo-questionnaire-template_>`_ for the list.

The timelapse
"""""""""""""

The **Timelapse** tile makes an animated GIF that runs through the images of the alert's area, from before to after, with the alert's outline over them. Each frame stays 2 seconds and is labelled with its collection and date. The before and after frames also name their side ("Before · Sentinel-2 2026-07-28").

It is offered for a true alert only: the tile is active when the alert is saved as **Reviewed: confirmed** and the images on screen are those it was saved with. Otherwise, it reads "Save as a true alert, with the images on screen, to create it".

The frames are:

-   the before and after images chosen in the review; and
-   up to two images before the before image and two after the after image, found within 12 months, under the timeline's **Max cloud** limit and never a Planet mosaic.

The GIF is saved next to the other files and, when the alert's files are built, added to the .zip file.

.. _defo-export-set:

The whole set, from the Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Export alerts** card, in the **Files** tab of the `Overview <defo-overview_>`_, writes the alerts of the set shown to a single file. Its top line sums up the alerts that the chosen **Alerts** chip writes, with the set's sources and dates (e.g. "11 alerts · 304.9 ha · GLAD-L + GLAD-S2 + RADD · 2026-10-01 – 2026-10-20" for **Confirmed**). The folder chip next to it copies the folder's path when selected.

.. shot: export-overview-card | The Export alerts card in the Files tab of the Overview of the demo project, on the set 2026-10-01 → 2026-10-20: the summary line ("11 alerts · 304.9 ha · GLAD-L + GLAD-S2 + RADD · 2026-10-01 – 2026-10-20"), the folder chip; the Alerts chips Confirmed (11) selected, All reviewed (16), Not reviewed (32), All (48); the GeoPackage tile written ("11 polygons · answers · 2026-10-20 02:13 · 224 KB", as a download link) and the CSV table tile still to create ("11 rows · all columns, WKT"); the footer line with the file name. Crop to the card.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/export-overview-card.png
    :alt: The Export alerts card of the Overview

To export the set:

1.  Choose the alerts to write with the **Alerts** chips: **Confirmed**, **All reviewed**, **Not reviewed** or **All**. Each chip shows its number of alerts; a chip with none is disabled. **Confirmed** is chosen first when the set has confirmed alerts, **All** otherwise.
2.  Select a format tile to write the file. It reads "Writing 11 alerts…" while it works, and the task list shows **Exporting alerts**.
3.  Select the tile again, now a download link with the time it was written, to download the file.

.. list-table::
    :header-rows: 1
    :widths: 25 75

    *   -   Tile
        -   Content
    *   -   **GeoPackage**
        -   One polygon per alert, with its attributes and answers, in a layer named after the file. The geometry is what the reviewer approved: the polygon drawn in Analysis if there is one, else the alert's cluster polygon, never the bounding box. A second layer, ``<name>_detected``, holds the cluster polygons.
    *   -   **CSV table**
        -   One row per alert with every column, geometries written as well-known text (WKT): ``geometry`` is the reviewed shape and ``detected_geometry``, next to it, the cluster polygon.

Both files add the columns ``geometry_source`` (``drawn``, ``detected`` or ``group``) and ``detected_area_ha`` (the cluster's area as detected; ``area_ha`` is the reviewed area). A member of a group whose main alert has a drawing has no shape of its own: its ``geometry_source`` is ``group`` and its ``review_group`` names the main alert whose drawing covers it. Both files also carry ``reviewed_by`` and ``reviewed_at`` (see `Save the review <defo-analysis-save_>`_) and add three columns on `growth <defo-integrate-growth_>`_:

-   ``kind``: ``new``, ``growth``, ``growth_small`` or ``new_small`` (see **Kind** in `The review panel <defo-analysis-panel_>`_);
-   ``grows_from``: the alert's links, separated by ";", each written as *set*\ ``#``\ *alert number*\ ``@``\ *run of that set*; and
-   ``history_area_ha``: the confirmed area of the alert's history, 0 for an alert without one.

The file is named after the set's sources, its period and the chosen alerts (e.g. ``alerts_glad-l-glad-s2-radd_2026-08-01_2026-09-30_confirmed.gpkg``): ``_reviewed`` for **All reviewed**, ``_unreviewed`` for **Not reviewed**, and no suffix for **All**. The card's last line shows the name. Answers are written in the app's current language.

With **All periods** chosen in the **Alert set** selector, the card writes every period's alerts to one file in the project folder, with a ``period`` column giving each alert's period. Its name joins the sources of every set and runs from the first period's start to the last period's end (e.g. ``alerts_glad-l_2026-08-01_2026-10-23.gpkg``).

When reviews are saved after a file was written, its tile reads **Reviews changed since**, with an **Update** button. Select it to write the file again.

Common messages
^^^^^^^^^^^^^^^

"The before and after images for this alert are not both ready, so its files cannot be built."
    Choose both images on the timeline and let the two maps finish drawing them.

"No alert set is active, so there is nowhere in the project to save the alert files. Run Integrate & vectorize first."
    Run `Integrate & vectorize <defo-integrate_>`_.

"The report template … is gone. Pick it again in the Questionnaire step, or clear it to use the default template."
    The project's template was moved or deleted: see `The report template <defo-questionnaire-template_>`_.

"The alert files are ready, but the GIF could not be made, so the zip has no GIF."
    Try the **Timelapse** tile on its own.

"The before and after images are the same image, so the GIF would show no change."
    Choose two different images on the timeline.

"Fewer than two images could be rendered for this alert, so no GIF was made."
    Choose other before and after images, then try again.

"The alert files finished building after you moved to another alert: they were not offered for download here."
    Go back to the alert: the files are in the set folder.

.. _defo-use-case:

Use case: alert review in Madre de Dios, Peru
---------------------------------------------

.. labels-ok: Admin level 1; Select AOI; True colour

This use case follows a small forest-monitoring team through two monthly rounds in the department of Madre de Dios, in the Peruvian Amazon, on the borders with Brazil and Bolivia. Gold mining and the spread of agriculture both put pressure on its forest, so the team wants to know each month where forest was lost, and why.

The team has:

-   a coordinator, who sets up the project and reviews alerts; and
-   two evaluators, Ana and Luis, who review their share of the alerts from their own SEPAL accounts.

.. note::

    The values in this use case come from the demo project the screenshots of this article are taken from. The verdicts and answers show how the app records a review; they are examples, not a checked assessment of the forest in Madre de Dios.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/anim/workflow.gif
    :alt: The two workflow levels: the Prepare alerts steps, from the area of interest to the alert set, then the Set up review steps, locked until that set exists

Set up the project
^^^^^^^^^^^^^^^^^^

The coordinator sets up the project as follows:

1.  **Project**: in the app, select **New project** and name it ``madre_de_dios`` (see `Create a project <defo-project-create_>`_).
2.  **AOI**: in the `AOI <defo-aoi_>`_ step, choose **Admin level 1**, then Peru, then "Madre De Dios" (as the list spells it), and select **Select AOI**. The area is saved as ``PER_Madre_De_Dios``. A whole department is a large area: every later step takes longer than for a district.

The September round
^^^^^^^^^^^^^^^^^^^

Period
""""""

In `Monitoring period <defo-period_>`_, the coordinator:

1.  selects **New period**;
2.  sets the dates from 2026-09-01 to 2026-09-30;
3.  enters 90 in **Look-back (days)** (a new project's first period starts at 0); and
4.  selects **Add period**.

The search window runs from 2026-06-03 to 2026-09-30, so clusters that started between June and August, and alerts the sources published late, are found too. As the first period, it has no earlier set: every alert in its search window is kept.

Alerts
""""""

In `Alert sources <defo-alerts_>`_, the coordinator adds the three predefined sources: **GLAD-L (Landsat, 30 m)**, **RADD (Sentinel-1, 10 m)** and **GLAD-S2 (Sentinel-2, 10 m)**, each with **Add to new periods** left selected, so that the next periods start with them. Each one covers the whole AOI. Under RADD, the app notes that it detects only in primary humid tropical forest: elsewhere in the department, only GLAD-L and GLAD-S2 can report alerts. Then the **Download** of each row downloads the three sources over the search window.

Harmonize
"""""""""

In `Harmonize <defo-harmonize_>`_, the coordinator:

1.  keeps the suggested grid, the UTM zone of the department (``EPSG:32719``) at 10 m, and selects **Save grid**. The grid is 41425 × 38561 pixels, about 12.8 GB per source before compression, so the app warns that the downloads will take a while;
2.  adds a mask so that only alerts in forest count: **Add mask**, the Hansen Global Forest Change image ``UMD/hansen/global_forest_change_2025_v1_13``, band ``treecover2000``, named ``forest_2000``, mode **Keep**; and
3.  selects the mask's **Align** and, once the mask reads "Ready", **Harmonize** on each source's row, which harmonizes the three sources.

Downloading and harmonizing took about 15 minutes. The mask and each source then read "Ready": GLAD-L with 2362718 alert pixels, RADD with 1508527 and GLAD-S2 with 1462458.

Integrate & vectorize
"""""""""""""""""""""

In `Integrate & vectorize <defo-integrate_>`_, the coordinator:

-   keeps the three sources and **Include probable (unconfirmed) alerts** on;
-   sets **Minimum cluster size** to 1 ha and **Order** to **Bigger clusters first**; and
-   selects **Limit the number of clusters**, with **Maximum number of clusters** set to 48: the team can review about 48 alerts a month, so it starts with the biggest ones.

The run makes the alert set "2026-09-01 → 2026-09-30 · GLAD-L + GLAD-S2 + RADD" with 48 alerts, from 383.18 ha down to 27.84 ha: 2870 ha in all.

The clusters beyond the cap are kept as not analysable. The next period reconsiders them only if its look-back reaches back into September and it uses the same sources. October's 90-day look-back does (see `What earlier periods already reported <defo-integrate-earlier_>`_).

Additional layers
"""""""""""""""""

With the alert set built, **Set up review** unlocks. To judge alerts against a recent image, the coordinator adds one `additional layer <defo-layers_>`_: an **Earth Engine** Sentinel-2 image of 27 September 2026 (tile 19LDF, east of Puerto Maldonado), drawn as an **RGB composite** in **True colour** (B4, B3, B2), **Min** 0 and **Max** 3000, named ``Sentinel-2 2026-09-27``, and **Show in Analysis** selected.

.. note::

    Planet NICFI monthly mosaics would cover the whole department, but the account used for this article has no NICFI access. This is why Planet is greyed out in the **Image sources** menu of the Analysis timeline in the screenshots below.

Review alone, then together
^^^^^^^^^^^^^^^^^^^^^^^^^^^

First reviews
"""""""""""""

Before sharing the work, the coordinator opens `Analysis <defo-analysis_>`_ and reviews the two biggest alerts:

-   alert 1 (383.18 ha) as **True alert**, with the loss driver **Mining**; and
-   alert 2 (146.97 ha) as **False positive**.

Split the alerts
""""""""""""""""

In `Evaluation <defo-evaluation_>`_, the coordinator selects **Multiple evaluators**, then **Split alerts…**, chooses **Names**, enters Ana and Luis, and selects **Split**. The alerts are dealt out in turn: Ana and Luis get 23 each, and the two alerts already reviewed stay **Unassigned**.

Before the packages
"""""""""""""""""""

The coordinator goes on reviewing in the original project while the split is set:

-   alert 3 as **True alert**, with **Agriculture expansion**;
-   alert 4 as **Needs revision**, with **Logging**; and
-   alert 5 as **True alert**, with **Mining**.

These verdicts travel in the packages, so the evaluators see them; alerts 3 and 5 are among Ana's. The coordinator then selects **Generate packages** and sends each evaluator their .zip file.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/anim/evaluators.gif
    :alt: The alert set is split into packages, each evaluator reviews theirs, and the reviews are merged back

Ana's review copy
"""""""""""""""""

Ana copies the package into her SEPAL folder and imports it with **Import** in the `Project <defo-project-import_>`_ dialog. It opens as the project ``madre-de-dios__e01-ana``, on the Analysis screen, already filtered to her alerts ("Evaluator: Ana").

Ana works through them with **Save** and **Next**:

-   the top bar counts "5 reviewed · 18 left · filtered · 48 total" (the coordinator's two reviews of her alerts and three of her own);
-   the counter numbers her alerts from 1 to 23; and
-   her third alert, for example, is saved as **True alert** with **Mining**: the after image shows bare, sandy ground with a green pond at the edge of the forest, which looks like the pits that alluvial gold mining leaves.

.. shot: use-case-ana-copy | The Analysis screen of Ana's review copy (project madre-de-dios__e01-ana): the filled funnel with the "Evaluator: Ana" chip, the tally "5 reviewed · 18 left · filtered · 48 total", the counter "03 / 23"; before and after images of one of her alerts; the review panel with Status "Reviewed: confirmed", True alert chosen and the Loss driver answered "Mining"; the dock with "ready to build" and Next filled; the after image shows sandy ground and a pond. No crop.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/use-case-ana-copy.png
    :alt: Ana's review copy on the Analysis screen

When done for now, Ana selects **Generate reviewed copy** in the `Evaluation <defo-evaluation-return_>`_ step ("5 / 23 of your alerts reviewed") and sends the ``__reviewed.zip`` file back.

Merge Ana's reviews
"""""""""""""""""""

The coordinator copies the file into the SEPAL folder, selects **Merge reviewed copy…** and chooses it. The preview reads "Ana: 3 new reviews, 1 conflicts, 1 unchanged, 0 ignored":

-   the unchanged review is alert 3, which Ana left as the coordinator saved it; and
-   the conflict is alert 5: the coordinator had confirmed it as mining, while Ana marked it as a false positive.

The coordinator keeps the original verdict with **Keep mine**, and plans to look at that alert again with Ana. After **Merge**, the evaluators table shows Ana with five of her 23 alerts reviewed and the date of the merge (see `Merge a reviewed copy <defo-evaluation-merge_>`_).

Add a question
^^^^^^^^^^^^^^

The team also wants to record whether each clearing has an access road nearby. In the `Questionnaire <defo-questionnaire_>`_ step, after the default **Loss driver**, the coordinator adds a second question:

1.  **Add question**;
2.  "Access road nearby?";
3.  **One answer**, with the options Yes and No;
4.  **Required** on; and
5.  asked for **True alert** and **Needs revision** only.

Because the questionnaire changed after the packages were built, their cloud icons in `Evaluation <defo-evaluation-packages_>`_ turn amber. Packages already sent still merge, by question key. For the new question to reach the evaluators, the coordinator selects **Regenerate packages** and sends the new ones.

From then on, a true alert or an alert that needs review gets both answers (a false positive gets neither: both questions are asked only for the other two verdicts). For example, alert 10 is saved as **True alert**, with **Agriculture expansion** as the loss driver and "No" for the access road. Its status reads **Reviewed: confirmed**, and the **Questions** section reads "2 of 2 answered".

.. shot: use-case-reviewed-alert | The Analysis screen of the demo project on alert 10 / 48 of the September set (tally "13 reviewed · 35 left"), reviewed: before and after images; the review panel with Status "Reviewed: confirmed", True alert chosen, the Questions section open with "2 of 2 answered", Loss driver = Agriculture expansion and "Access road nearby?" = No; the dock with Export this alert "ready to build" and Next filled. No crop.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/use-case-reviewed-alert.png
    :alt: A reviewed alert: its verdict and its two answers

Back in the workflow, **Show these alerts on the map** in `Integrate & vectorize <defo-integrate-map_>`_ draws the set over the department. At this zoom, each alert is a dot coloured by its review status:

-   grey for **Not reviewed**;
-   red for **Reviewed: confirmed**;
-   green for **Reviewed: false positive**; and
-   amber for **Reviewed: needs revision**.

With 13 of the 48 alerts reviewed, most dots are still grey. Most alerts lie in the south of the department.

.. shot: use-case-alerts-map | The main map over Madre de Dios with the September set's 48 alerts drawn from Integrate & vectorize's "Show these alerts on the map" switch, after 13 reviews: grey dots (Not reviewed), red (Reviewed: confirmed), green (Reviewed: false positive) and amber (Reviewed: needs revision), most of them in the south; the alert legend ("Alerts · 2026-09-01_2026-09-30 · GLAD-L + GLAD-S2 + RADD"). Crop to the map, between the left rail and the Workflow panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/use-case-alerts-map.png
    :alt: The September alerts on the map of Madre de Dios, coloured by review status

The October round
^^^^^^^^^^^^^^^^^

At the start of the next round, the coordinator selects **New period** in `Monitoring period <defo-period-add_>`_. The dialog is pre-filled: from 2026-10-01 (the day after September ends) to today, with the 90 days of look-back used last time. The coordinator sets the end to 2026-10-20, the day of this round. **Add period** makes it the active period, with the September period's mask choices and the three sources marked **Add to new periods**.

Then:

-   each row's **Download** in `Alerts <defo-alerts_>`_ downloads the three sources for the new window, and each row's **Harmonize** in `Harmonize <defo-harmonize_>`_ harmonizes them; the grid and the mask are already there.
-   In `Integrate & vectorize <defo-integrate_>`_, the coordinator uses the same settings as in September (1 ha, the 48 biggest alerts). Before grouping the pixels into alerts, the run removes every pixel inside September's 48 alerts, so that nothing is reported twice. The new set holds 48 alerts again, for 1177 ha. None of them touches an alert confirmed in September, so the run links none to earlier loss (see `Growth of earlier loss <defo-integrate-growth_>`_).

The team reviews them as in September; 16 are reviewed so far, 11 of them as true alerts. With **Show these alerts on the map** and **Show earlier sets** both on, the map shows the October alerts next to September's, which are drawn in fainter colours. The October alerts lie in the same parts of the department as September's.

.. shot: use-case-periods-map | The main map over Madre de Dios with Integrate & vectorize's "Show these alerts on the map" and "Show earlier sets" both on: the October set's alerts coloured by status, the September set's alerts in faded colours, and the legend with its selector showing the earlier set's legend ("Alerts · 2026-09-01 → 2026-09-30 · …"). Crop to the map, between the left rail and the Workflow panel.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/use-case-periods-map.png
    :alt: The October alerts and the September alerts on the map

Read the figures
^^^^^^^^^^^^^^^^

The `Overview <defo-overview_>`_ sums up the October set. In **Area (ha)**:

-   **Confirmed loss**: 305 ha, with "▼ 780 less than 2026-09-01 → 2026-09-30";
-   **Detected in total**: 1177 ha;
-   **Reviewed**: 33 %, "16 of 48 alerts"; and
-   **Largest alert**: 31.9 ha, the card's "Alert 1". In a set made with this version, the Overview and the Analysis counter share the same numbers, so this is the first alert there.

.. shot: use-case-overview | The Overview dialog on the October set (2026-10-01 → 2026-10-20 · GLAD-L + GLAD-S2 + RADD · 48 alerts), measure Area (ha): the header, then the four key figures: Confirmed loss 305 with "▼ 780 less than 2026-09-01 → 2026-09-30", Detected in total 1,177, Reviewed 33 % "16 of 48 alerts", Largest alert 31.9 "Alert 1 · …". Crop to the dialog, down to the bottom of the key figures, without the tabs.

.. figure:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en/img/use-case-overview.png
    :alt: The key figures of the October set

.. important::

    The comparison needs care. **Confirmed loss** counts only the alerts reviewed as true alerts, and only a third of the October alerts are reviewed; the September figure, too, covers only the September alerts reviewed so far. The arrow means that less loss is *confirmed* so far, not that less forest was lost: the figure grows as the team goes on reviewing.

In the **Over time** tab, **Across monitoring periods** shows the two periods side by side, with the share still under review hatched (2870 ha detected in September, 1177 ha in October).

In the **Answers** tab:

-   the card of the loss-driver question splits the reviewed area by answer (in October: Mining first, then Agriculture expansion); and
-   the card of the new question splits it by its answers (in October: all "No", 358 ha, with 81.2 ha under "No answer").

See `The tabs <defo-overview-figures_>`_ for every card.

Share the results
^^^^^^^^^^^^^^^^^

The whole set
"""""""""""""

In the **Files** tab of the Overview, the **Export alerts** card writes the October set to a file. The coordinator chooses **Confirmed** (11 alerts, 304.9 ha) and selects the **GeoPackage** tile. The file ``alerts_glad-l-glad-s2-radd_2026-10-01_2026-10-20_confirmed.gpkg`` holds one polygon per confirmed alert with its attributes and both answers, ready for a GIS. The **CSV table** tile writes the same alerts as a table for a spreadsheet. See `The whole set, from the Overview <defo-export-set_>`_.

One alert
"""""""""

To report on one alert, the coordinator opens it in Analysis, saves it, and selects **Build files** under **Export this alert**. The result is a .zip file with the alert's GeoPackage and its before and after images, and a Word report built from the project's template. For a true alert, the **Timelapse** tile also makes an animated GIF of the images from before to after. See `One alert, from Analysis <defo-export-alert_>`_.

Every file is also kept in the alert set's folder of the project, under ``periods/2026-10-01_2026-10-20/sets/glad-l-glad-s2-radd/``.

Next month
^^^^^^^^^^

For the next round, the team plans to:

-   select **New period** again: the dates continue the series, and the look-back brings back the clusters set aside as too small the month before, so a slowly growing clearing becomes an alert once it reaches 1 ha, without any pixel being reported twice;
-   review the October alerts before the next run: an alert confirmed by then can become the earlier loss that November's alerts grow from, and a clearing that keeps growing shows its history in Analysis and in the Overview;
-   check the questionnaire before splitting: a question added after the packages are built needs **Regenerate packages**;
-   review the alerts still **Not reviewed** in the earlier sets too, since the Overview's comparison is only as complete as the reviews behind it; and
-   use **Duplicate** in the `Project <defo-project-duplicate_>`_ dialog to monitor a neighbouring area with the same sources, mask and layers.


.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/deforestation-alerts-module/release/doc/en.rst
