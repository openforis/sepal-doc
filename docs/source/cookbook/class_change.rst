Class change
============
*Build a class change map between two categorical maps that share the same legend with the Class change recipe*

Overview
--------

Often, we want to build the class change map between two categorical maps that share the same legend. If the two images are taken at different times, this can help us understand how the vegetation classification has evolved between two dates. It can be tedious to build the new legend (forest -> forest, forest -> urban, etc.) and manually write the rules to identify each class. SEPAL will automatically build the legend of the resulting categorical map from the initial legend and compute all pixels automatically.

.. note::

    This recipe is not computationally demanding; you can safely reuse the recipe without exporting other recipes. It will not slow down downstream processes.

Start
-----

Once the **Class change** recipe is selected, SEPAL will present the **Process** in a new tab (see **1** in figure below).

**Parameters** will open in the lower-right side of your screen (2).

.. thumbnail:: ../_images/cookbook/class_change/landing.png
    :group: recipe_class_change
    :title: The landing page of the **Class change** recipe.

The first step is to change the name of the recipe. This name will be used to name your files and recipes in **SEPAL folders**. Use the best-suited convention for your need. Simply double-click the tab and enter a new name (it will default to :code:`Class_change_<now>`).

.. thumbnail:: ../_images/cookbook/class_change/default_title.png
    :title: Class change default title
    :width: 49%

.. thumbnail:: ../_images/cookbook/class_change/title.png
    :title: Class change modified title
    :width: 49%

Parameters
----------

In the lower-right corner, the following four tabs are available, allowing users to customize the class change to their needs:

-   :guilabel:`FRM`: the source categorical image
-   :guilabel:`TO`: the destination categorical image
-   :guilabel:`LEG`: the legend of the transition classes
-   :guilabel:`OPT`: the optional parameters of the recipe

.. thumbnail:: ../_images/cookbook/class_change/parameters.png
    :group: recipe_class_change
    :title: The four tabs to set up SEPAL **Class change** recipe

Select images
^^^^^^^^^^^^^

The first step is to select the two images to compare. Since :guilabel:`FRM` and :guilabel:`TO` have the same interface, they will be described together.

Select a categorical image, which can be a classification recipe or any categorical asset from your Google Earth Engine (GEE) account. In both cases, you'll need to select the band to use for the transition and the legend.

If the selected asset/recipe is a **Classification** recipe (or its export), the legend will be automatically generated with the metadata of the file. If it's not, you'll need to upload it manually.

Select :btn:`fa-solid fa-pen-to-square` to open the **Legend editing** tool. It's the same as the one described in the **Classification** recipe (see :doc:`classification`).

.. thumbnail:: ../_images/cookbook/class_change/from.png
    :group: recipe_class_change
    :width: 49%
    :title: The **from** image selection (in this example, a **Classification** recipe forest/non-forest [FNF] for the year 2020)

.. thumbnail:: ../_images/cookbook/class_change/to.png
    :group: recipe_class_change
    :width: 49%
    :title: The **to** image selection (in this example, a **Classification** recipe forest/non-forest [FNF] for the year 2021)

Customize legend
^^^^^^^^^^^^^^^^

Once both **from** and **to** images are selected, SEPAL will build a transition classification legend based on the registered legend in the two parameter images. The color and the values can be modified.

.. thumbnail:: ../_images/cookbook/class_change/legend.png
    :group: recipe_class_change
    :title: The generated transition legend from an FNF to another FNF classification (the color has been modified)

.. thumbnail:: ../_images/cookbook/class_change/results.png
    :group: recipe_class_change
    :title: The resulting image with the transition class from 2021 to 2022

Options
^^^^^^^

If the selected asset is from a SEPAL classification, it will embed a probability value for each classified pixel. SEPAL will propose clever map transitioning based on these values.

For example, a high-confidence forest pixel changes into a low-confidence non-forest pixel. The change will be taken into account only if the minimum confidence is reached by the **to** pixel. By default, no filtering is performed and the slider is set to 0.

.. note::

    If the classified images are from other sources, the probability won't be available and the transition will be applied without verification.

.. thumbnail:: ../_images/cookbook/class_change/option.png
    :group: recipe_class_change
    :title: The confidence option of the transition evaluation

Analysis
--------

Export
^^^^^^

.. important::

    You cannot export a recipe as an asset or a :code:`.tiff` file without a small computation quota (if you are a new user, see :doc:`../setup/resource`).

Select the :icon:`fa-solid fa-cloud-arrow-down` tab to open the **Retrieve** pane, where you can select the **Exportation parameters**.

.. thumbnail:: ../_images/cookbook/class_change/export.png
    :title: The last pane of the **Class change** recipe: the exportation
    :group: recipe_class_change


Bands
"""""

Select the band to export in the recipe. You will have access to :guilabel:`transition` (the new class change values) and :guilabel:`confidence`, if you selected **Classification recipe assets**.

Scale
"""""

You can set a custom scale for exportation by changing the value of the slider (m). Requesting a smaller resolution than an image's native resolution will not improve the quality of the output, just its size, so keep in mind that the native resolution of Sentinel data is 10 m and Landsat is 30 m.

Destination
"""""""""""

You can export the image to :guilabel:`SEPAL workspace` or to :guilabel:`GEE asset`. The same image will be exported, but in the first case, you will find it in :code:`.tif` format in the :code:`Downloads` folder; in the second case, the image will be exported to your GEE account **Asset** list.

.. attention::

    If :guilabel:`GEE asset` is not displayed, your GEE account is not connected to your SEPAL account (see :doc:`../setup/gee`).

Select :guilabel:`apply` to start the download process.

Exportation status
""""""""""""""""""

In the **Tasks** tab (lower-left corner using the :icon:`fa-solid fa-list-check` or :icon:`fa-solid fa-spinner` buttons, depending on the loading status), you will see the list of different loading tasks. The interface will provide you with information about the task progress and display an error if the exportation has failed.

If you are unsatisfied with the way we present information, the task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    This operation is running in the background between GEE and SEPAL servers, so you can close the SEPAL page without stopping the process.

When the task is finished, the frame will be displayed in green (see the second image below).

.. thumbnail:: ../_images/cookbook/class_change/download.png
    :width: 49%
    :title: Evolution of the downloading process of the recipe displayed in the **Task manager** of SEPAL
    :group: recipe_class_change

.. thumbnail:: ../_images/cookbook/class_change/download_complete.png
    :width: 49%
    :title: Completed downloading process of the recipe displayed in the **Task manager** of SEPAL
    :group: recipe_class_change
