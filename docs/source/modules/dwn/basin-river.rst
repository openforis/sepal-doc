Resilient rivers and basins
===========================

Understand forest cover and forest cover change from a watershed perspective
----------------------------------------------------------------------------

Overview 
________
The **Resilient rivers and basins** beta app is a tool that describes forest cover and forest cover change from a watershed perspective by calculating statistics across subwatersheds over time; watersheds of interest will be defined by the upstream basin draining to any given point. These processes can be conducted directly in your SEPAL instance without requiring additional resources. 

To run this module, we recommend initializing a machine with at least 4 GB RAM (a t2 or m2 instance). For more detailed instructions,  see `Start instance manually <https://docs.sepal.io/en/latest/modules/index.html#start-instance-manually>`__.

Inputs
______

Once you have started an instance,  `search in the apps tab <https://docs.sepal.io/en/latest/modules/index.html#start-applications>`_ for the **Resilient rivers and basins** app, which is composed of two main sections: 

1.  **the left pane**, which displays all of the processes (i.e. inputs and results) at the top, and some helpful links (e.g. bug report, wiki, source code) at the bottom; and 

2.  **the right pane**, which displays process and inputs. 

By default, the **input drawer** will be active. It is divided into two main panes:

1.  **the left pane**, which displays all of the input parameters to derive statistics. 
    
2.  **the right pane**, which displays the map view where calculated layers will be loaded. 

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/basin-rivers/master/doc/img/inputs.png 
    :width: 80% 
    :title: Inputs view
    :group: inputs 

The first input needed is a **coordinate pair**, which will be used to calculate and retrieve all of the upstream sub-basins that drain to that point for any given **hydroBASIN level**. 

To input coordinates, the module has two options: **manual** and **automatic**. 

To use **manual selection**, enter the latitude and longitude coordinates, then select :code:`Next`. The map will set a blue marker at that point and zoom into the area of interest. 

To use **automatic selection**, turn off the manual switch and navigate through the map to find your desired area. Select the exact spot (usually a river confluence or a bridge, but terrestrial areas work as well); a blue marker will be displayed. 

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/basin-rivers/master/doc/img/coordinates.png 
    :width: 55% 
    :title: Inputs view
    :group: inputs 
 
.. note::

    When using the **automatic selection** method, the latitude and longitude input text fields will be deactivated. Notice that the coordinates will be automatically synchronized as you move the cursor over the map.

The next step is to select the **HydroBASIN target level** by using the dropdown list. **HydroBASINs** are delineated basins in the HydroATLAS database. Their levels range from 5 to 12, where higher numbers indicate smaller basins nested inside larger sub-basins. For more information about how these data are obtained, see `HydroSHEDS documentation <https://www.hydrosheds.org/products/hydrobasins>`_.

The forest cover change map is based on the  `Global Forest Change product <https://www.science.org/doi/10.1126/science.1244693>`_ (Hansen *et al.*, 2013), retrieved from `Google Earth Engine <https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2021_v1_9>`_. Created to show forest cover change on a global-scale based on Landsat imagery, the product has forest change data from 2000 to 2001. 

The **Resilient rivers and basins** app will crop and summarize forest cover statistics for each of the forest cover classes at the selected basin scale (i.e. the HydroBASIN level).

To begin, use the sliders to select the **start and end year**. 

Next, select the **forest threshold**, which determines the level of tree cover required for a pixel in the Global Forest Change product to be classified as **forest**. Changing the value will alter the amount of forest cover or forest cover change observed. 

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/basin-rivers/master/doc/img/levels.png 
    :width: 55% 
    :title: Setting levels
    :group: inputs 

Select the :btn:`Get upstream basins` button to run the process. The results will be displayed as a map of forest cover change by sub-basin.  

.. note::
    The amount of time required for calculation depends on the selected **HydroBASIN level** and the **location of the downstream point**. 
    
    Also, the number of **sub-basins** displayed will vary depending on the **downstream point** (e.g. a watershed draining to a point at the mouth of a fairly mountainous area will include more upstream sub-basins than a watershed draining to a higher-level point in the same orography). 

To start a new process, you can use the **trash bin** button in the upper-left of the map to remove the **downstream point** or remove the **sub-basins** selection (for more information, see the next section, which explains how to constrain the analysis to a given set of sub-basins). 

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/basin-rivers/master/doc/img/trash_bin.png 
    :width: 30% 
    :title: Trash bin 
    :group: inputs 

To calculate and display statistical results in the **Results** dashboard, use the **Statistics** tile. There are two selection methods: 

1.  **no filter** (i.e. use all basins); 
2.  **filter**. 
    
When using the **Filter** option, a new dropdown menu will appear at the bottom of the tile with all of the sub-basin IDs. 

Manually select or remove **sub-basins** by selecting each row. Notice that the map will automatically sync the selected basins by displaying a black boundary and zooming in. 

Select the **Calculate statistics** button. 

Once the dashboard is calculated, a red dot will be displayed in the **Results** drawer, as seen in the image below: 

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/basin-rivers/master/doc/img/results_done.png 
    :width: 30% 
    :title: Done drawer
    :group: inputs 
 
Dashboard
_________

The **Dashboard** panel is divided into three main sections: 

1.  the **Settings** tile in the upper-left; 
2.  the **Pie chart** in the upper-right; and 
3.  **detailed charts** at the bottom. 

.. tip::

    All graphs have an option for independent download directly to your browser. Simply hover the cursor in the upper-right corner and select the  :icon:`fa-solid fa-camera`  icon.

In the **Settings** tile, you can choose the variable to display: 

-   **all**, 
-   **gain and loss**, 
-   **loss**, 
-   **non-forest**, 
-   **forest**, and 
-   **gain**. 

By choosing one of these options, all graphs will display the selected statistics. From this menu, you can also filter the data by one or more sub-basins, allowing the possibility of generating dynamic comparisons between areas. 

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/basin-rivers/master/doc/img/stats_card.png 
    :width: 73% 
    :title: Statistics card 
    :group: dashboard 
 
The **Overall ratio** is an interactive pie chart that displays the output variable of each subcategory by proportion. It also allows you to directly select one subcategory to be used in the detailed charts. Simply select any subcategory and the corresponding slice will be showcased. 

.. thumbnail:: https://raw.githubusercontent.com/sepal-contrib/basin-rivers/master/doc/img/overal_pie_ratio.png 
    :width: 55% 
    :title: Overall ratio pie chart
    :group: dashboard 
 
The detailed, interactive charts at the bottom display both the **ratio** and the **total area** of the selected variable. 

On the left, the **pie chart** shows the proportion of the area for each of the selected sub-basins. 

On the right, the **bar chart** displays the absolute values. 

.. note::

    In the Global Forest Change product dataset (Hansen *et al.*, 2013), only forest loss has a temporal dimension. When a new time period is selected, a new graph representing the trend of forest loss will be displayed at the bottom of the screen.

.. image:: https://raw.githubusercontent.com/sepal-contrib/basin-rivers/master/doc/img/interactive_stats.gif

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/basin-rivers/master/doc/en.rst
