Tasks
=====
*Follow the exports of your recipes*

When you export or retrieve a recipe, SEPAL starts a task that runs in the background. The **Tasks** tab works the same way for all recipes; only the recipe type and name differ.

Tasks list
----------

Open the **Tasks** tab (lower-left corner) to follow your exports. Its button shows :icon:`fa-solid fa-spinner` while tasks are running, and :icon:`fa-solid fa-list-check` otherwise. Each task shows the recipe type and destination (e.g. **Radar Mosaic → SEPAL workspace**), and the project and name of the recipe. A running task displays a spinner and its current status (e.g. :code:`Google Earth Engine is exporting`); once it has completed, a green check mark and the duration of the task are displayed.

You can filter the list with :guilabel:`All`, :guilabel:`Active`, :guilabel:`Completed` and :guilabel:`Failed / Canceled`, or find a task with the **Search tasks** field. Select :btn:`<fa-solid fa-xmark>` to stop a running task (you are asked to confirm), and :btn:`<fa-solid fa-trash>` to remove a finished task from the list.

.. thumbnail:: ../_images/feature/tasks/tasks.png
    :width: 49%
    :title: Exports in SEPAL's **Tasks** tab: one completed, one in progress
    :group: tasks

.. thumbnail:: ../_images/feature/tasks/task_details.png
    :width: 49%
    :title: The details of a completed export
    :group: tasks

Task details
------------

Select a task to open its details:

-   **Status**: the duration, submission time and completion (or last update) time of the task.
-   **Recipe configuration**: the recipe type and origin (project and recipe name).
-   **Location**: the destination and output path of the exported data and, for exports to an Earth Engine asset, its access.
-   **Progress**: the export progress, or the error message if the export has failed.

The task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    Tasks run between GEE and SEPAL servers in the background. You can close the SEPAL page without stopping them.
