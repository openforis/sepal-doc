Class change
============

Overview
--------

Very often we want to build the class change map between 2 categorical map sharing the same legend. If the 2 images are taken at different time it will help us understand how the vegetation classification has evolved between these 2 dates. It can be a tidious exercise to build the new legend (forest -> forest, forest -> urban, ...) and to manually write the rules to identify each class. Sepal will automatically build the legend of the rsulting categorical map from the initail legend and compute all the pixels automatically.

.. note::

    This recipe is a very light computation, you can safely reuse the recipe without exporting in other recipes, it will not slow down the downstream processses.

Start
-----

Once the class chane recipe is selected, SEPAL will show you the process in a new tab (1). the parameter will open themselves at the bottom right side of your screen (2).

.. thumbnail:: ../_images/cookbook/class_change/landing.png
    :group: recipe_class_change
    :title: the landing page of the class change recipe.

The first step is to change the name of the recipe. This name will be used to name your files and recipes in the SEPAL folders. Use the best-suited convention for your need. Simply double-click the tab and write a new name. It will default to :code:`Class_change_<now>`.

.. thumbnail:: ../_images/cookbook/class_change/default_title.png
    :title: class change default title 
    :width: 49%

.. thumbnail:: ../_images/cookbook/class_change/title.png
    :title: class change modified title 
    :width: 49%

Parameters
----------

In the bottom right corner, 4 tabs are available. They will allow the user to customize the class change to its needs.

-   :guilabel:`FRM`: the source categorical image
-   :guilabel:`TO`: the destination categorical image
-   :guilabel:`LEG`: the legend of the transition classes
-   :guilabel:`OPT`: the optional parameters of the recipe

.. thumbnail:: ../_images/cookbook/class_change/parameters.png
    :group: recipe_class_change
    :title: the 4 tabls to set up SEPAL class change recipe


Select images
^^^^^^^^^^^^^

The first step is to select the 2 images to compare. :guilabel:`FRM` and :guilabel:`TO` have the same interface so we'll describe them together. 

You need to select a categorical image, this can be a classification recipe, or any categorical asset from your google earthengine account. In both cases you'll need to select the band to use for the transition and the legend.

If the selected asset/recipe is a classification recipe (or its export) the legend will be automatically field with the metadata of the file. else you'll need to updload it manually. click on :btn:`fas fa-edit` to open the legend edition tool. It's the same as the one described in the classification recipe. Please refer to :doc:`classification` if you need extra information.

.. thumbnail:: ../_images/cookbook/class_change/from.png
    :group: recipe_class_change
    :width: 49%
    :title: the "from" image selection. in this example a classification recipe Forest/non-forest for the year 2020.

.. thumbnail:: ../_images/cookbook/class_change/to.png
    :group: recipe_class_change
    :width: 49%
    :title: the "to" image selection. in this example a classification recipe Forest/non-forest for the year 2021.

customize legend
^^^^^^^^^^^^^^^^

Once both **from** and **to** images are selected, SEPAL will build a transition classification legend based on the registered legend in the 2 parameter images. The color can be modified as well as the values.

.. thumbnail:: ../_images/cookbook/class_change/legend.png
    :group: recipe_class_change
    :title: the genereted transition legend from a FNF to another FNF classification. the color have been modified.

.. thumbnail:: ../_images/cookbook/class_change/results.png
    :group: recipe_class_change
    :title: The resulting image with the transition class from 2021 to 2022.

options
^^^^^^^

If the selected asset is from a SEPAL classification, it will embed a probability value for each classified pixel. SEPAL will proposed clever map transitionning based on these values. 

For example a high confidence forest pixel changes in a low confidence non-forest piexl. the change will be taken into account only if the min confidence is reached by the "TO" pixel. By default no filtering is perform and the slider is set to 0. 

.. note::

    if the classified images are from other sources, the probability won't be available and the transition will be applied without verification. 

.. thumbnail:: ../_images/cookbook/class_change/option.png
    :group: recipe_class_change
    :title: The confidence option of the trnasition evauation

Analysis
--------

Export
^^^^^^

Clicking on the :icon:`fas fa-cloud-download-alt` tab will open the retrieve panel where the you can select the exportation parameters.

.. thumbnail:: ../_images/cookbook/class_change/export.png
    :title: the last panel of the class change recipe: the exportation
    :group: recipe_class_change


Bands
"""""

You need to select the band to export in the recipe. You will have access to :guilabel:`transition` which is the new class change values and :guilabel:`confidence` if you selected **classification recipe** assets.

Scale 
"""""

You can set a custom scale for exportation by changing the value of the slider (m). Requesting a smaller resolution than images native resolution will not improve the quality of the output, just its size so keep in mind that Sentinel data native resolution is 10 m and Landsat is 30 m. 

Destination
"""""""""""

You can export the image to :guilabel:`sepal workspace` or to ;guilabel:`google earth engine asset`. The same image will be exported but in the first case you will find it in :code:`.tif` format in the :code:`downloads` folder, in the second one the image will be exported to your GEE account asset list. 

.. warning::

    If :guilabel:`google earth engine asset` is not displayed, it means that your GEE account is not connected to SEPAL, please refer to :doc:`../setup/gee`.

Click on :guilabel:`apply` to start the download process. 

Exportation status
""""""""""""""""""

Going to the task tab (bottom left corner using the :icon:`fa fa-tasks` or :icon:`fa fa-spinner` buttons —depending on the loading status—), you will see the list of the different loading tasks. The interface will provide you with information about the task progress and it will display an error if the exportation has failed. If you are unsatisfied with the way we present information, the task can also be monitored using the `GEE task manager <https://code.earthengine.google.com/tasks>`__.

.. tip::

    This operation is running between GEE and SEPAL servers in the background, you can thus close the SEPAL page without killing the process.

When the task is finished the frame will be displayed in green as shown on the second image.

.. thumbnail:: ../_images/cookbook/class_change/download.png
    :width: 49%
    :title: Evolution of the downloading process of the recipe displayed in the task manager of SEPAL.
    :group: recipe_class_change

.. thumbnail:: ../_images/cookbook/class_change/download_complete.png
    :width: 49%
    :title: Completed downloading process of the recipe displayed in the task manager of SEPAL.
    :group: recipe_class_change

