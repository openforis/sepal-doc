Band Math
=========

The **Band Math** recipe in SEPAL allows you to derive new raster layers from existing ones by evaluating mathematical expressions.  You can combine, scale or subtract spectral bands, build indices or apply logical masks.  This guide walks through the Band Math workflow from start to finish and uses a vegetation index as an example.  The same steps apply whether you are creating a simple ratio or a complex index.

Getting started
---------------

- Open `sepal.io <https://sepal.io>`_ in your web browser and sign in.
- Go to the **Process** page where SEPAL lists your recipes.  If you have not created any recipes yet this list will be empty.

Creating a Band Math recipe
---------------------------

Click :btn:`<fa-solid fa-plus> Add recipe` in the recipe list and choose **Band Math**. SEPAL opens a new tab for your recipe. On the right‑hand side you will see three vertically stacked tabs labelled :guilabel:`IMG`, :guilabel:`CAL` and :guilabel:`OUT` corresponding to *Input imagery*, *Calculations* and *Outputs*.

.. thumbnail:: ../_images/cookbook/band_math/1_select_recipe.png
    :width: 48%
    :title: Recipe selection menu
    :align: center

.. thumbnail:: ../_images/cookbook/band_math/2_recipe_options.png
    :width: 48%
    :title: Band Math recipe interface
    :align: center

Select the :guilabel:`IMG` tab. Click :btn:`<fa-solid fa-plus> Add` and then **Earth Engine Asset**. An entry form appears where you can provide a Google Earth Engine image. Paste a valid asset ID into the **Earth Engine asset ID** field (for example the Landsat 8 Level‑2 scene ``LANDSAT/LC08/C02/T1_L2/LC08_232064_20200119``). Leave the **Image name** as the default (``i1``) unless you intend to add multiple images. Use the tick icon to validate the ID; if the field turns red the asset is not available. Once it loads successfully you will see a section labelled **CONTINUOUS** listing the available bands.

.. thumbnail:: ../_images/cookbook/band_math/3_band_selection.png
    :width: 70%
    :title: Band selection interface
    :align: center

Specify which bands you need. Click the green :btn:`<fa-solid fa-plus> Add` button to insert a row, select the band name from the drop‑down list and leave the :guilabel:`TYPE` as **CONTINUOUS**. Repeat this step for every band referenced in your expression. For a vegetation index select the red band ``SR_B4`` and the near‑infrared band ``SR_B5``. When you have added all your bands, click :btn:`<fa-solid fa-check> Apply` to confirm and then :btn:`<fa-solid fa-check> Done` to return to the map. The :guilabel:`IMG` tab now lists your Earth Engine asset and the chosen bands.

Defining a calculation
----------------------

Switch to the :guilabel:`CAL` tab and click :btn:`<fa-solid fa-plus> Add`. A dialog appears offering two paths: **Function** and **Expression**. Choose **Function** when you want SEPAL to compute built‑in statistics (sum, mean, min, max, product) on your bands. Choose **Expression** when you need to write a custom formula. For indices you will almost always select **Expression**.

.. thumbnail:: ../_images/cookbook/band_math/4_expression_or_function.png
    :width: 70%
    :title: Expression or function selection dialog
    :align: center

In the expression editor type your formula. Refer to each band using its image name and band name, for example ``i1.SR_B5`` for the near‑infrared band of the first image. Parentheses control the order of operations. To compute a vegetation index you can use:

   .. code-block::

      (i1.SR_B5 - i1.SR_B4) / (i1.SR_B5 + i1.SR_B4)

   You could just as easily substitute other bands or constants, for example the Normalised Difference Water Index (NDWI) ``(i1.SR_B3 - i1.SR_B5) / (i1.SR_B3 + i1.SR_B5)`` or a simple ratio like ``i1.SR_B5 / i1.SR_B4``.

Enter a short Band name beneath the editor. This will be the label of the resulting layer – for example ``ndvi`` for a vegetation index.

Click :btn:`<fa-solid fa-check> Apply`. Your calculation appears in the list with an identifier such as ``c1``. You can add additional calculations by repeating this process; each one becomes a separate output band.

.. thumbnail:: ../_images/cookbook/band_math/5_expression.png
    :width: 70%
    :title: Expression editor with NDVI formula
    :align: center

Managing outputs and naming
---------------------------

The :guilabel:`OUT` tab displays the bands produced by your expressions. Check that the band names are correct. You can delete or reorder them using the icons on the right of each row. Above the map the recipe tab uses a default timestamp; rename it by double‑clicking the label, entering a descriptive name (for example ``Amazon_BandMath``) and pressing **Enter**. When everything looks correct close the :guilabel:`OUT` tab.

.. thumbnail:: ../_images/cookbook/band_math/6_output_band.png
    :width: 70%
    :title: Output band configuration
    :align: center

Visualising the results
-----------------------

By default your calculation is not drawn on the map. To create a visualisation:

Locate the small :btn:`<fa-solid fa-bars>` icon near the bottom centre of the map and click it. This opens the **This recipe** panel. If your derived bands appear here they are ready for visualisation; if not, click the :btn:`<fa-solid fa-plus>` button in that panel to create one.

.. thumbnail:: ../_images/cookbook/band_math/7_visualization_entry.png
    :width: 70%
    :title: Visualization panel access
    :align: center

A **Visualisation** dialog opens. Choose the band you want to display from the **Band** drop‑down (for example ``ndvi``). Set **Min** and **Max** values to define the stretch – for indices spanning –1 to 1, values such as –0.2 and 0.8 often provide good contrast.

Select a colour palette. You can load a preset palette from the drop‑down or define your own. To enter custom colours click the :guilabel:`HEX` button; a text box appears containing a comma‑separated list of colour codes. Replace it with your own codes (e.g. ``#ffffcc, #c2e699, #78c679, #31a354, #006837`` for a light‑to‑dark green gradient). Multiple colours create a smooth ramp.

.. thumbnail:: ../_images/cookbook/band_math/8_visualization_opts.png
    :width: 70%
    :title: Visualization options dialog
    :align: center

Click :btn:`<fa-solid fa-check> Apply`. SEPAL renders the band using your settings and adds a legend bar at the bottom of the map. If the map stays blank for more than a few seconds, ensure you added the correct bands and that the area of interest is not outside the footprint of your image.

.. thumbnail:: ../_images/cookbook/band_math/results.png
    :width: 70%
    :title: Final NDVI visualization results
    :align: center


What else can you do with Band Math?
------------------------------------

Band Math is a general‑purpose calculator for raster bands.  Beyond vegetation indices you can:

* Highlight water bodies by computing the Normalised Difference Water Index (NDWI): ``(i1.SR_B3 - i1.SR_B5) / (i1.SR_B3 + i1.SR_B5)``.
* Assess burn severity with the Normalised Burn Ratio (NBR) using near‑infrared and short‑wave infrared bands: ``(i1.SR_B5 - i1.SR_B7) / (i1.SR_B5 + i1.SR_B7)``.
* Perform arithmetic between bands (for example ``i1.SR_B5 - i1.SR_B4``), multiply by constants to convert digital numbers to reflectance or add bands to create composites.
* Create masks based on conditions – for instance ``i1.SR_B5 > 0.3`` to select highly vegetated pixels – and combine them with logical operators (`and`, `or`).

Every expression you add becomes a new band that can be visualised or used in subsequent calculations.  By chaining calculations together you can build complex workflows in SEPAL without writing any external code.
